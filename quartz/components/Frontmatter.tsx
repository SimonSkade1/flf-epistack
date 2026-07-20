import { JSX } from "preact"
import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import { classNames } from "../util/lang"
import style from "./styles/frontmatter.scss"
import { FullSlug } from "../util/path"
import {
  MECHANICAL_FRONTMATTER_KEYS,
  parseWikilinks,
  resolveWikilink,
} from "../util/frontmatterLinks"

interface Options {
  /** extra keys to hide on top of the Quartz-machinery ones */
  hide: string[]
  /** these keys are pulled to the top, in this order; the rest keep file order */
  order: string[]
  /** render collapsed by default */
  collapsed: boolean
  /** heading shown on the toggle */
  title: string
}

const defaultOptions: Options = {
  hide: [],
  // the EpiStack identity fields first, then the structural edges, then prose
  order: ["type", "id", "state", "question", "statement", "cluster", "from", "to", "group"],
  collapsed: false,
  title: "Properties",
}

const urlRegex = /(https?:\/\/[^\s<>()[\]]+)/g

/** `[[wikilinks]]` and bare URLs inside a frontmatter string become real links. */
function renderString(
  value: string,
  slug: FullSlug,
  allSlugs: FullSlug[],
): (string | JSX.Element)[] {
  const links = parseWikilinks(value)
  if (links.length === 0) return linkifyUrls(value)

  const out: (string | JSX.Element)[] = []
  let cursor = 0
  for (const link of links) {
    const at = value.indexOf(link.raw, cursor)
    if (at > cursor) out.push(...linkifyUrls(value.slice(cursor, at)))
    cursor = at + link.raw.length

    if (link.target === "") continue
    const resolved = resolveWikilink(slug, link, allSlugs)
    if (!resolved) {
      // a reference to something that doesn't exist — say so instead of emitting
      // a link that 404s
      out.push(
        <span class="fm-unresolved" title="unresolved link">
          {link.alias ?? link.target}
        </span>,
      )
      continue
    }
    out.push(
      // `internal` + `data-slug` are what Quartz's popover and the node-type link
      // colours key off, so frontmatter links behave exactly like body ones
      <a href={resolved.href} class="internal" data-slug={resolved.slug}>
        {link.alias ?? link.target}
      </a>,
    )
  }
  if (cursor < value.length) out.push(...linkifyUrls(value.slice(cursor)))
  return out
}

function linkifyUrls(value: string): (string | JSX.Element)[] {
  const parts = value.split(urlRegex)
  return parts.map((part, i) =>
    i % 2 === 1 ? (
      <a href={part} class="external" rel="noopener">
        {part}
      </a>
    ) : (
      part
    ),
  )
}

function isEmpty(value: unknown): boolean {
  if (value === null || value === undefined) return true
  if (typeof value === "string") return value.trim() === ""
  if (Array.isArray(value)) return value.length === 0
  return false
}

function renderValue(value: unknown, slug: FullSlug, allSlugs: FullSlug[]): JSX.Element {
  if (isEmpty(value)) return <span class="fm-empty">—</span>

  if (Array.isArray(value)) {
    return (
      <ul class="fm-list">
        {value.map((item) => (
          <li>{renderValue(item, slug, allSlugs)}</li>
        ))}
      </ul>
    )
  }

  if (typeof value === "object") {
    return (
      <dl class="fm-nested">
        {Object.entries(value as Record<string, unknown>).map(([k, v]) => (
          <div class="fm-row">
            <dt>{k}</dt>
            <dd>{renderValue(v, slug, allSlugs)}</dd>
          </div>
        ))}
      </dl>
    )
  }

  if (typeof value === "boolean" || typeof value === "number") {
    return <span class="fm-scalar">{String(value)}</span>
  }

  return <span>{renderString(String(value), slug, allSlugs)}</span>
}

export default ((opts?: Partial<Options>) => {
  const options: Options = { ...defaultOptions, ...opts }
  const hidden = new Set([...MECHANICAL_FRONTMATTER_KEYS, ...options.hide])

  const Frontmatter: QuartzComponent = ({
    fileData,
    ctx,
    displayClass,
  }: QuartzComponentProps) => {
    const frontmatter = fileData.frontmatter
    if (!frontmatter) return null

    const entries = Object.entries(frontmatter).filter(([key]) => !hidden.has(key))
    if (entries.length === 0) return null

    entries.sort(([a], [b]) => {
      const ia = options.order.indexOf(a)
      const ib = options.order.indexOf(b)
      if (ia === -1 && ib === -1) return 0
      if (ia === -1) return 1
      if (ib === -1) return -1
      return ia - ib
    })

    const slug = fileData.slug!
    const allSlugs = ctx.allSlugs

    return (
      <details class={classNames(displayClass, "frontmatter")} open={!options.collapsed}>
        <summary>
          {options.title}
          <span class="fm-count">{entries.length}</span>
        </summary>
        <dl>
          {entries.map(([key, value]) => (
            <div class="fm-row" data-key={key}>
              <dt>{key}</dt>
              <dd>
                {key === "type" && typeof value === "string" ? (
                  <span class="fm-type" data-node-type={value}>
                    {value}
                  </span>
                ) : (
                  renderValue(value, slug, allSlugs)
                )}
              </dd>
            </div>
          ))}
        </dl>
      </details>
    )
  }

  Frontmatter.css = style
  return Frontmatter
}) satisfies QuartzComponentConstructor<Partial<Options>>
