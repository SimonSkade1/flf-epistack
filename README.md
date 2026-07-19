# EpiStack

A browsable knowledge base and the runnable pipeline behind it. The pipeline turns one contested empirical question into a Bayesian, navigable graph of typed Obsidian-style notes; this repo also serves that graph as a static website via [Quartz](https://quartz.jzhao.xyz/). Built for the **Future of Life Foundation epistemics competition** (that entry is `v1`).

Live site: **https://epistack.simonskade.org** (Let's Encrypt TLS via Caddy; also reachable at http://91.98.229.7, kept as a DNS-independent fallback).

## Content versioning

The **site shell** — the Quartz reading surface and the pipeline — is version-agnostic and lives at the root. **Project content is versioned**: everything for one iteration sits under `content/vN/` and is served at `epistack.simonskade.org/vN/…`. Quartz maps content folders straight to URL paths, so no path-prefix config is involved; `baseUrl` stays the bare domain.

`v1` is the FLF-competition iteration. A future iteration that changes the method or the question set becomes `content/v2/` and is served alongside v1, so URLs already handed out keep resolving. Git tags freeze the *code*; `/vN/` freezes the *URLs*.

## Layout

1. `content/` — the site content (Quartz reads this).
   1. `content/index.md` — version-agnostic root landing page (what EpiStack is, links to the iterations).
   2. `content/v1/` — the FLF-competition iteration → `/v1/`.
      1. `content/v1/analyses/` — one folder per analysis. `sample-sahul-megafauna/` is a hand-written **structural demo** exercising every node type, folder, wikilink, embed, and code block a real run produces (illustrative numbers). Real runs are added here.
      2. `content/v1/docs/` — documentation (draft).
      3. `content/v1/index.md` — v1 landing page; doubles as the `/v1/` folder page.
2. `pipeline/` — the runnable EpiStack pipeline (a copy of the `flf-epistack` skill): `SKILL.md`, `steps/step-01…10`, and `runner/`. Not versioned by folder — use git tags.
3. `quartz/`, `quartz.config.ts`, `quartz.layout.ts` — the Quartz static-site generator and its config.
4. `scripts/check-internal-links.mjs` — post-build link check (see below).

## Build the site

```
npm i                     # once
npx quartz build          # emits ./public
npx quartz build --serve  # local preview at http://localhost:8080
```

### Checking links after a build

```
node scripts/check-internal-links.mjs        # exits 1 if any internal link 404s
```

Run this after moving content around. Note that grepping the built HTML for `class="internal broken"` is **not** a valid link check: Quartz only emits that class when `ObsidianFlavoredMarkdown` is configured with `disableBrokenWikilinks: true`, which is `false` by default, so the grep returns 0 hits regardless. The script instead resolves every emitted `<a class="internal">` href against the files in `public/`.

Wikilinks resolve by `markdownLinkResolution: "shortest"` — a bare `[[filename]]` works as long as that filename is unique across all of `content/`. Path-prefixed wikilinks must be full slugs from the content root (`[[v1/docs/index]]`), not partial paths.

## Run the Bayesian model of an analysis

```
python3 pipeline/runner/run.py content/v1/analyses/sample-sahul-megafauna
# HC-1  prior [...]  posterior [...]  (N evidence block(s))

# price any named variable and re-run:
python3 pipeline/runner/run.py content/v1/analyses/sample-sahul-megafauna --set E-14:t_dates=1.0
```

`pipeline/runner/test_run.py` self-checks the runner against the specs' published numbers.

## Deploy

The VPS cannot pull from GitHub, so deploy = build locally and `rsync` to the VPS, where Caddy serves `public/` as static files.

---

Built with [Quartz v4](https://quartz.jzhao.xyz/).
