import { Root } from "hast"
import { QuartzTransformerPlugin } from "../types"
import { SimpleSlug, simplifySlug } from "../../util/path"
import {
  collectWikilinks,
  MECHANICAL_FRONTMATTER_KEYS,
  resolveWikilink,
} from "../../util/frontmatterLinks"

interface Options {
  /** frontmatter keys whose wikilinks should NOT become edges */
  ignoreKeys: string[]
}

const defaultOptions: Options = { ignoreKeys: [] }

/**
 * Count frontmatter wikilinks as real outgoing links.
 *
 * Without this, `cluster:`, `from:`/`to:`, `group:`, `arguments:` and `source:`
 * are invisible to the link graph — which in EpiStack means the single most
 * important edge in the ontology (evidence-link → hypothesis-cluster) is missing,
 * and correlation-group / argument nodes float unconnected. It roughly doubles
 * the edge count (~530 frontmatter wikilinks vs ~559 body ones in v1).
 *
 * MUST be registered *after* CrawlLinks, which assigns `file.data.links`
 * wholesale and would otherwise clobber whatever we add here.
 */
export const FrontmatterLinks: QuartzTransformerPlugin<Partial<Options>> = (userOpts) => {
  const opts = { ...defaultOptions, ...userOpts }
  const ignore = new Set(opts.ignoreKeys)

  return {
    name: "FrontmatterLinks",
    htmlPlugins(ctx) {
      return [
        () => {
          return (_tree: Root, file) => {
            const frontmatter = file.data.frontmatter
            if (!frontmatter) return

            const src = file.data.slug!
            const outgoing = new Set<SimpleSlug>(file.data.links ?? [])
            const self = simplifySlug(src)

            for (const [key, value] of Object.entries(frontmatter)) {
              if (ignore.has(key) || MECHANICAL_FRONTMATTER_KEYS.has(key)) continue
              for (const link of collectWikilinks(value)) {
                if (link.target === "") continue
                const resolved = resolveWikilink(src, link, ctx.allSlugs)
                if (!resolved) continue
                const simple = simplifySlug(resolved.slug)
                if (simple !== self) outgoing.add(simple)
              }
            }

            file.data.links = [...outgoing]
          }
        },
      ]
    },
  }
}
