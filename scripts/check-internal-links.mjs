#!/usr/bin/env node
/**
 * Verify that every internal link in the built site resolves to an emitted page.
 *
 * Why this exists: grepping the built HTML for `class="internal broken"` does NOT
 * work as a link check. Quartz only emits that class when the ObsidianFlavoredMarkdown
 * transformer runs with `disableBrokenWikilinks: true`, which is *false* by default
 * (see quartz/plugins/transformers/ofm.ts). With the default config the grep always
 * returns 0 hits, whether or not links are broken.
 *
 * This script instead walks the emitted HTML, resolves every <a class="internal ...">
 * href relative to its own page, and asserts a corresponding file exists in public/.
 *
 * Usage: node scripts/check-internal-links.mjs [publicDir]
 * Exit code 0 = all internal links resolve, 1 = at least one broken link.
 */

import fs from "node:fs"
import path from "node:path"

const publicDir = path.resolve(process.argv[2] ?? "public")

function walk(dir, out = []) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name)
    if (entry.isDirectory()) walk(full, out)
    else out.push(full)
  }
  return out
}

if (!fs.existsSync(publicDir)) {
  console.error(`No such directory: ${publicDir} — run \`npx quartz build\` first.`)
  process.exit(1)
}

const allFiles = walk(publicDir)
const htmlFiles = allFiles.filter((f) => f.endsWith(".html"))
const existing = new Set(allFiles.map((f) => path.relative(publicDir, f)))

// Quartz serves extensionless slugs; Caddy's try_files maps /a/b -> a/b.html or a/b/index.html.
const resolves = (rel) => {
  const clean = rel.replace(/\/$/, "")
  return (
    existing.has(clean) ||
    existing.has(`${clean}.html`) ||
    existing.has(path.join(clean, "index.html")) ||
    (clean === "" && existing.has("index.html"))
  )
}

const anchorRe = /<a\b[^>]*>/gi
const broken = []
let internalCount = 0

for (const file of htmlFiles) {
  const pageRel = path.relative(publicDir, file)
  const pageDir = path.dirname(pageRel)
  const html = fs.readFileSync(file, "utf8")

  for (const [tag] of html.matchAll(anchorRe)) {
    const classMatch = tag.match(/class="([^"]*)"/i)
    if (!classMatch || !classMatch[1].split(/\s+/).includes("internal")) continue
    const hrefMatch = tag.match(/href="([^"]*)"/i)
    if (!hrefMatch) {
      // Quartz emits <a class="internal broken"> with no href for unresolved wikilinks.
      broken.push({ page: pageRel, href: "(no href — broken wikilink)", tag })
      continue
    }
    let href = hrefMatch[1]
    if (/^(https?:)?\/\//i.test(href) || href.startsWith("mailto:") || href.startsWith("#")) continue
    href = href.split("#")[0].split("?")[0]
    if (href === "") continue
    internalCount++

    const target = href.startsWith("/")
      ? decodeURIComponent(href.slice(1))
      : decodeURIComponent(path.normalize(path.join(pageDir, href)))

    if (!resolves(target)) broken.push({ page: pageRel, href, target })
  }
}

console.log(`pages scanned:   ${htmlFiles.length}`)
console.log(`internal links:  ${internalCount}`)
console.log(`broken links:    ${broken.length}`)

if (broken.length) {
  console.log("")
  for (const b of broken) console.log(`BROKEN  ${b.page}\n        href=${b.href}\n        -> ${b.target}`)
  process.exit(1)
}
console.log("OK — every internal link resolves to an emitted page.")
