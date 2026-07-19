# The EpiStack website

Developer documentation for the site itself — how it's built, deployed, and
customised. This is *not* the FLF submission documentation; that lives in
`content/v1/docs/` and is published at <https://epistack.simonskade.org/v1/docs/>.

## What it is

A [Quartz](https://github.com/jackyzha0/quartz) v4.5.2 static site. Quartz was
chosen because it renders an Obsidian vault essentially as-is: `[[wikilinks]]`,
`![[transclusions]]`, callouts, LaTeX, fenced code, per-folder index pages,
backlinks, an interactive graph, and client-side full-text search — all without
rewriting the pipeline's markdown into another format.

- **Live:** <https://epistack.simonskade.org> (also `http://91.98.229.7/`, the
  pre-DNS fallback block, still live as a backup entry point)
- **Repo:** <https://github.com/SimonSkade1/flf-epistack>
- **Served by:** Caddy on the Hetzner VPS (`91.98.229.7`), static files only

## Repo layout

```
content/            # the published markdown — this IS the site
  index.md          #   / — version-agnostic landing (the shell)
  v1/               #   /v1/ — everything about the current FLF submission
    index.md
    analyses/<name>/   # one folder per analysis run
    docs/              # submission-facing documentation
docs/website.md     # this file (developer docs, NOT published)
pipeline/           # the runnable EpiStack pipeline (copy of the vault skill)
quartz/             # Quartz source — patched, see "Customisations"
scripts/
  check-internal-links.mjs   # real broken-link checker (see "Link checking")
public/             # build output; rsynced to the VPS. Not the source of truth.
```

## URL structure and versioning

The **site shell is general and version-agnostic**; the **content is versioned**:

| URL | what |
|---|---|
| `/` | what EpiStack is, links to the iterations |
| `/v1/` | the current FLF-contest submission (analyses + docs) |
| `/v2/` | a future significantly-different iteration — just add `content/v2/` |

Quartz maps `content/` folders straight onto URL paths, so a new version needs
**no config change**: create `content/v2/`, build, deploy. `baseUrl` stays the
bare domain — do not put a path in it.

The point of versioning is a **stable URL**: the contest submission links
`/v1/...` and those URLs keep working as development continues.

### Adding a new analysis

Drop the pipeline's output folder into `content/v1/analyses/<analysis-name>/`,
then build + deploy. Quartz generates the folder index page automatically.

## Node-type colours

Each EpiStack node type has a colour, applied in two places from **one
definition** in `quartz/styles/custom.scss`:

1. **Link colours** — every link is tinted by the type of the note it points at,
   in body text, folder listings, backlinks, and the explorer sidebar.
2. **Graph node colours** — `quartz/components/scripts/graph.inline.ts` reads the
   same `--node-*` CSS variables via `getComputedStyle`.

Both light and dark themes are defined. To change a colour or add a type, edit
the `:root` / `:root[saved-theme="dark"]` blocks and the `$node-folders` map in
`custom.scss`, and add the type to `NODE_TYPES` in `graph.inline.ts`.

### The one coupling to know about

The **graph** colours nodes from the `type:` frontmatter field (it has the whole
content index available, so this is exact and survives any renaming).

The **link colours** key off the *folder segment* of the URL (`/hypotheses/`,
`/sources/`, …), because when Quartz renders a link it does not have the target
file's frontmatter available. This is correct as long as the pipeline keeps
writing each node type into its own folder — which it does.

**If the pipeline ever renames those folders, update the `$node-folders` map.**
Node *filenames* can change freely (e.g. dropping the `MR-`/`CR-` prefixes);
only folder names matter here.

The main report sits at the analysis root rather than in a type folder, so it has
no link colour — it does get its graph colour, from frontmatter. This is
deliberate: it's a single entry-point document, not a class of node you need to
tell apart at a glance.

## Graph behaviour

Two customisations on top of stock Quartz (`graph.inline.ts`):

1. **Type colouring** (above). The current page's node keeps the standard
   highlight colour, which wins over its type colour.
2. **Hover reveals neighbour titles.** Stock Quartz shows only the hovered
   node's label. Here, hovering also shows the labels of all adjacent nodes, so
   you can read a neighbourhood without clicking. Labels return to the
   zoom-determined baseline opacity when the hover ends.

## Build, deploy, verify

The VPS **cannot pull from GitHub** and runs no node build. Deploy is
build-locally-then-rsync:

```bash
cd external-projects/flf-epistack

npx quartz build                        # → public/
node scripts/check-internal-links.mjs public   # must report 0 broken

rsync -az --delete public/ \
  simon@91.98.229.7:/home/simon/workspace/external-projects/flf-epistack/public/

curl -s -o /dev/null -w "%{http_code}\n" https://epistack.simonskade.org/
```

Then commit and push the repo as usual. `public/` is committed too, so the repo
and the live site stay in step.

### Local preview

```bash
npx quartz build --serve      # http://localhost:8080, hot reload
```

Note: a plain `python3 -m http.server` over `public/` will 404 on internal links,
because Quartz emits extensionless slugs and only Caddy's `try_files` resolves
them. Use `--serve`, or append `.html` manually.

## Link checking

`scripts/check-internal-links.mjs` resolves every emitted `<a class="internal">`
href against the files actually present in `public/`, and exits non-zero if any
dangle. **Run it after every content move.**

It exists because the obvious check is a trap: grepping the build output for
Quartz's `internal broken` class returns zero hits whether or not links are
broken, since that class is only emitted when `ObsidianFlavoredMarkdown` runs
with `disableBrokenWikilinks: true`, and it defaults to `false`
(`quartz/plugins/transformers/ofm.ts`).

### Wikilink gotchas

1. **`markdownLinkResolution: "shortest"` matches on bare filenames.** A
   path-prefixed wikilink like `[[docs/index]]` is resolved as a full slug from
   the content root, so moving a folder silently breaks it. Prefer bare
   filenames: `[[running-the-model]]`.
2. **Filename collisions across versions are dangerous.** If `content/v2/`
   reuses v1 filenames (`H-3 - …`, `manifest.md`), bare wikilinks become
   ambiguous in *both* trees and Quartz silently falls back to an
   absolute-from-root path that 404s. Either give each iteration distinct ids
   (`v1-H-3`) or run the link checker religiously after building v2.

## Server setup

Caddy config at `/etc/caddy/Caddyfile` on the VPS (edit as `root@91.98.229.7`):

```caddy
(epistacksite) {
    root * /home/simon/workspace/external-projects/flf-epistack/public
    encode gzip
    try_files {path} {path}.html {path}/index.html   # extensionless slugs
    file_server
    handle_errors {
        rewrite * /404.html
        file_server
    }
}

epistack.simonskade.org { import epistacksite }
http://91.98.229.7      { import epistacksite }
```

After editing: `caddy validate --config /etc/caddy/Caddyfile && systemctl reload caddy`.

- **DNS:** A record `epistack` → `91.98.229.7`. Caddy provisions Let's Encrypt
  automatically once it resolves.
- **Permissions:** serving out of `/home/simon` required `chmod o+x /home/simon`
  (0750 → 0751, traverse-only, not listable). The alternative, if that's
  unwanted, is to serve from `/var/www/flf-epistack` and add a copy step to the
  deploy.
- **Don't touch** the `voice.simonskade.org` block in the same Caddyfile.

## Adding a new site to this VPS

Each site gets its own subdomain, not a path: add an A record
`<name>.simonskade.org` → `91.98.229.7`, add a Caddy block, reload. Caddy routes
by the `Host` header, so sites never collide and each gets its own auto-TLS
certificate. The raw-IP block is a pre-DNS convenience and can only ever point at
one site.
