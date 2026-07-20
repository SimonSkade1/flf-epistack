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

Customisations on top of stock Quartz (`graph.inline.ts`):

1. **Type colouring** (above). The current page's node instead gets the dedicated
   `--node-current` colour — **chartreuse**, the one hue the 10-type palette leaves
   open (max min-distance from every type colour in both themes) — plus a
   high-contrast ring (`--dark`) and 1.6× radius, so "you are here" is unmistakable
   even next to a same-family neighbour.
2. **Hover reveals neighbour titles.** Stock Quartz shows only the hovered
   node's label. Here, hovering also shows the labels of all adjacent nodes, so
   you can read a neighbourhood without clicking. Labels return to the
   zoom-determined baseline opacity when the hover ends.
3. **Node-type filters.** The full-screen graph carries a chip bar — one chip
   per node type, with its colour swatch and a count, plus `other` for pages
   with no `type:` (docs, indexes, manifests). Clicking a chip hides that type.
   Two bulk buttons: **`hide all`** then click one chip = solo that type (instead
   of unchecking nine), **`show all`** clears every filter. The **current page's
   node is never filtered out**, even when its own type is hidden — so soloing a
   type you're not on still shows you where you are.
4. **Expanded graph is local by default.** Stock Quartz's full-screen graph
   always shows the whole vault. Here it opens on the current page's
   neighbourhood at distance 1, with a bottom bar holding a max-distance
   slider (1–3) and a "Show whole vault" toggle (whole vault = `depth: -1`,
   and the only mode that uses the radial layout). This state is deliberately
   not persisted — every page load starts local again. Implemented as a
   `depthOverride` third argument to `renderGraph`; the sidebar mini-graph is
   untouched by it.

### Readability tuning (why the labels don't collide)

EpiStack filenames run to 80+ characters, so stock Quartz's graph is a wall of
overlapping titles at a near-invisible opacity. Four coupled changes fix it,
configured via extra `D3Config` fields in `Graph.tsx` (`initialScale`,
`labelMaxChars`, `collidePadding`):

1. **Starts zoomed in.** `renderGraph` installs the d3-zoom behaviour with an
   initial transform at `initialScale` (2.4× expanded, 1.5× sidebar) centred on
   the page, instead of stock's k=1 — at k=1 a small neighbourhood is a few dots
   lost in an empty box.
2. **Fits to content once the layout settles.** A `fitToContent` pass (on every
   4th sim tick and on `end`) frames the actual node bounding box, but never
   zooms *past* `initialScale`. So a 2-node neighbourhood ends up nicely zoomed
   and a 290-node whole-vault view pulls back to an overview. It stops the moment
   the reader pans/zooms/drags (`userAdjustedView`).
3. **Labels truncate to `labelMaxChars`** (cut at a word boundary, keeping the
   `H-1 -` id prefix), and the **full title returns on hover** — where the label
   also scales up 1.45×, is lifted above every other label, and gets a `--light`
   backdrop plate (`labelBackdrop`, drawn each frame in the animate loop) so you
   can actually read it over a dense hairball.
4. **Label opacity is zoom-gated** (`labelAlphaAt`): near-solid for a bounded
   neighbourhood (fits at k≳1), hidden for the whole-vault view (fits at k≈0.3–0.5)
   so it doesn't become an unreadable wall. Stock divided by 3.75, leaving labels
   at ~0.2 even at 2×.

A 40-node hub (e.g. HC-1, which everything links to) still overlaps *at rest* —
that's unavoidable when readable labels are ~150px wide — but truncation plus the
hover plate make any single node legible on demand.

**Ambiguous-wikilink resolution** (`util/path.ts`, `findNearestSlug`). The
analyses reuse formulaic filenames across runs (`CG-1 - HC-1 joint over O-1+O-2`
exists in both covid1 and eggs1). Stock Quartz's `shortest` strategy gives up on
any non-unique filename and falls back to an absolute-from-root path that 404s.
We instead pick the candidate nearest the linking file in the folder tree —
Obsidian's rule — so a within-analysis `[[CG-1 …]]` resolves to its own run.

### How the filter is wired

- State is a `Set` of hidden types in `localStorage` under `graph-hidden-types`,
  so a filter survives navigation and reloads.
- Filtering happens on the *neighbourhood set* inside `renderGraph`, before
  nodes and links are built. Filtering the node list alone would leave links
  pointing at nodes that no longer exist.
- Toggling a chip tears the graph down and re-renders it, so the force
  simulation re-lays-out the remaining nodes rather than leaving holes.
- The filter applies to the **local sidebar graph too**, so "only hypotheses and
  evidence" holds while you browse. The chips in the full-screen graph are the
  only place to undo it — that graph is one click away in the sidebar header.
- The chip bar is built into `.global-graph-outer`, *not*
  `.global-graph-container`: `renderGraph` calls `removeAllChildren()` on its own
  container, so anything placed inside would be destroyed on every re-render.

## Frontmatter is rendered, and its wikilinks are real links

Stock Quartz parses YAML frontmatter into `file.data.frontmatter` and then
**never shows it and never follows its links** — it only ever walks the note
body. In EpiStack that throws away most of the structure: an evidence-link's
`from:`/`to:`/`group:`/`arguments:`, a hypothesis's `cluster:`, a source's
`trust_score`/`motivatedness`, etc. all live in frontmatter. Three pieces fix
this, all sharing one resolver in `util/frontmatterLinks.ts`:

1. **`Frontmatter` component** (`components/Frontmatter.tsx`, in the `beforeBody`
   layout) renders a collapsible "Properties" table above the article — an
   Obsidian-style properties view. `[[wikilinks]]` in values become real,
   popover-able `internal` links (so they also pick up the node-type link
   colour); bare URLs become links; the `type:` value gets its node-type colour
   as a pill. Quartz-machinery keys (title, tags, dates, `draft`, …) are hidden.
2. **`FrontmatterLinks` transformer** (`plugins/transformers/frontmatterLinks.ts`)
   adds those same wikilinks to `file.data.links`, so they count as **graph edges
   and backlinks**. It roughly doubles the edge count (~530 frontmatter wikilinks
   vs ~559 body ones in v1) and is what connects evidence-links to their cluster.
   It **must run after `CrawlLinks`** in `quartz.config.ts`, because CrawlLinks
   assigns `file.data.links` wholesale and would clobber earlier additions.
3. **The resolver** handles three cases in order: exact full slug, exact filename
   (nearest-wins for cross-run duplicates, as above), then an **EpiStack id
   prefix** — several runs write a bare `source: "[[S-12]]"` instead of the full
   filename, and inside one analysis an id is unique, so `S-12` resolves to
   `S-12 - …` rather than dangling. Anything genuinely unresolvable renders as
   plain dotted-underline text, never a 404 link.

## Explorer & layout

Three departures from stock Quartz, all in `quartz/components/styles/explorer.scss`
and `quartz/styles/variables.scss` (re-apply if ever upgrading Quartz):

1. **Scroll fix.** Stock v4.5.2 puts `overscroll-behavior: contain` on every
   nested explorer `ul`; combined with `overflow: hidden` on `.folder-outer > ul`
   each nested list becomes a scroll-chaining boundary, so wheel events over
   folder contents never reach the actual scroll container (`.explorer-ul`) and
   the tree simply doesn't scroll. The property now sits only on `.explorer-ul`.
2. **Entry separation.** Long node filenames wrap to 2–3 lines; with stock
   spacing a wrapped name is indistinguishable from several entries. Entries now
   use tight `line-height: 1.25` *within* a name and `0.3rem` vertical padding
   *between* entries.
3. **Wider left panel.** `$leftPanelWidth: 380px` (right stays at
   `$sidePanelWidth: 320px`) on the desktop grid, giving filenames more room.

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

Then commit and push the repo as usual. (`public/` is gitignored — the rsynced
copy on the VPS is the only deployed artifact, so always rsync after building.)

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
