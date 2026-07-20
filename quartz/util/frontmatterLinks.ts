import {
  FilePath,
  findNearestSlug,
  FullSlug,
  RelativeURL,
  resolveRelative,
  slugifyFilePath,
  splitAnchor,
} from "./path"

/**
 * Wikilinks that live in YAML frontmatter.
 *
 * Quartz only ever walks the *body* of a note: frontmatter is parsed out into
 * `file.data.frontmatter` before the markdown AST exists, so `[[...]]` values in
 * it are never turned into links, never resolved, and never counted as edges.
 * The EpiStack ontology puts most of its structure exactly there (`cluster:`,
 * `from:`/`to:`, `group:`, `arguments:`, `source:`), so this module re-implements
 * the two things ObsidianFlavoredMarkdown + CrawlLinks would have done:
 *
 *   1. parse the wikilink,
 *   2. resolve it under the same `markdownLinkResolution: "shortest"` rule.
 *
 * Consumed by the `Frontmatter` component (renders real, popover-able links) and
 * by the `FrontmatterLinks` transformer (feeds the graph and the backlinks).
 */

// same shape as ofm's wikilinkRegex, minus the multiline/embed handling we don't need
const wikilinkRegex = /!?\[\[([^[\]|#\\]+)?(#+[^[\]|#\\]+)?(\|[^[\]#]+)?\]\]/g

export type ParsedWikilink = {
  /** the raw `[[...]]` text */
  raw: string
  /** file part, e.g. `HC-1 - Route of the first human SARS-CoV-2 infection` */
  target: string
  /** heading/block anchor including the leading `#`, or "" */
  anchor: string
  /** display text after `|`, if given */
  alias?: string
}

/** Every wikilink in a frontmatter string value, in order. */
export function parseWikilinks(value: string): ParsedWikilink[] {
  const out: ParsedWikilink[] = []
  for (const m of value.matchAll(wikilinkRegex)) {
    const [raw, rawFp, rawHeader, rawAlias] = m
    out.push({
      raw,
      target: (rawFp ?? "").trim(),
      anchor: (rawHeader ?? "").trim(),
      alias: rawAlias?.slice(1).trim(),
    })
  }
  return out
}

/** matches an EpiStack node id used on its own: `S-12`, `HC-1`, `O-10`, `CG-3` */
const bareIdRegex = /^[A-Za-z]{1,3}-\d+$/

/**
 * Resolve a frontmatter wikilink, in order of confidence:
 *
 *   1. exact full slug (a path-prefixed wikilink like `[[v1/docs/index]]`),
 *   2. exact filename, nearest to the linking file if several match,
 *   3. **id prefix** — `[[S-12]]` → `S-12 - Zhong 2019 JAMA - …`, nearest first.
 *      Several runs write the bare id into `source:`/`cluster:` instead of the
 *      full filename (124 such values in v1). Obsidian shows those as unresolved;
 *      inside one analysis an id is unique, so we can do better than dropping them.
 *
 * Returns null when nothing matches, so callers can render plain text rather than
 * emit a link that 404s.
 */
export function resolveWikilink(
  src: FullSlug,
  link: ParsedWikilink,
  allSlugs: FullSlug[],
): { slug: FullSlug; href: RelativeURL } | null {
  const [fp, anchor] = splitAnchor(`${link.target}${link.anchor}`)
  const canonical = slugifyFilePath(fp as FilePath)
  const fileName = canonical.split("/").at(-1)!

  let slug: FullSlug | undefined
  if (allSlugs.includes(canonical)) {
    slug = canonical
  } else {
    slug = findNearestSlug(
      src,
      allSlugs.filter((s) => s.split("/").at(-1) === fileName),
    )
  }

  if (!slug && bareIdRegex.test(link.target.trim())) {
    const prefix = `${fileName}---` // sluggified "<id> - "
    slug = findNearestSlug(
      src,
      allSlugs.filter((s) => s.split("/").at(-1)!.startsWith(prefix)),
    )
  }

  if (!slug) return null
  return { slug, href: (resolveRelative(src, slug) + anchor) as RelativeURL }
}

/**
 * Walk a frontmatter value of any shape (string / array / nested map) and yield
 * every wikilink found in it.
 */
export function collectWikilinks(value: unknown, out: ParsedWikilink[] = []): ParsedWikilink[] {
  if (typeof value === "string") {
    out.push(...parseWikilinks(value))
  } else if (Array.isArray(value)) {
    for (const v of value) collectWikilinks(v, out)
  } else if (value && typeof value === "object") {
    for (const v of Object.values(value)) collectWikilinks(v, out)
  }
  return out
}

/**
 * Frontmatter keys that are Quartz machinery or are already rendered by another
 * component (title, tags, dates), so showing them again is pure noise.
 */
export const MECHANICAL_FRONTMATTER_KEYS = new Set([
  "title",
  "tags",
  "tag",
  "aliases",
  "alias",
  "draft",
  "publish",
  "permalink",
  "cssclasses",
  "cssclass",
  "socialImage",
  "image",
  "cover",
  "socialDescription",
  "enableToc",
  "comments",
  "lang",
  "created",
  "modified",
  "published",
  "date",
  "lastmod",
  "updated",
  "last-modified",
  "publishDate",
])
