# EpiStack

A browsable knowledge base and the runnable pipeline behind it. The pipeline turns one contested empirical question into a Bayesian, navigable graph of typed Obsidian-style notes; this repo also serves that graph as a static website via [Quartz](https://quartz.jzhao.xyz/). Built for the **Future of Life Foundation epistemics competition** (that entry is `v1`).

Live site: **https://epistack.simonskade.org** (Let's Encrypt TLS via Caddy; also reachable at http://91.98.229.7, kept as a DNS-independent fallback).

**Full website documentation: [`docs/website.md`](docs/website.md)** — layout, versioning, node-type colours, graph customisations, the build/deploy recipe, Caddy + DNS setup, and the wikilink gotchas. Start there for anything about the site itself.

## Start here

1. **The submission document** — [`content/v1/docs/submission.md`](content/v1/docs/submission.md), rendered at <https://epistack.simonskade.org/v1/docs/submission>. The written core of the entry: principles, the 10-step pipeline, the node ontology, the Bayesian logic, the case studies, the limitations, and how to reproduce it.
2. **Three end-to-end runs** under [`content/v1/analysis-tests/`](content/v1/analysis-tests) — COVID origins, LHC black holes, and eggs-and-health. All ten steps ran on each and every posterior recomputes from the notes (see *Run the Bayesian model* below). They are deliberately **low-N shakedown runs** (5–10 curated sources each), so read them as a demonstration of the method rather than as settled answers. Fuller runs land in `content/v1/analyses/`.
3. **The failure-modes appendix** — [`content/v1/analysis-tests/APPENDIX - known failure modes.md`](content/v1/analysis-tests/APPENDIX%20-%20known%20failure%20modes.md). Across the three runs, **3 BLOCKERs and 33 MAJORs**, each logged by an agent *inside* the run that hit it — including one BLOCKER the run subsequently checked and retracted.
4. **The pipeline itself** — [`pipeline/SKILL.md`](pipeline/SKILL.md) and [`pipeline/steps/`](pipeline/steps). The same files ship at `.claude/skills/flf-epistack/` so the reproduction command below resolves in a fresh clone.

### Reproduce a run

Needs [Claude Code](https://claude.com/claude-code). One command per case, from a clone of this repo:

```
cd content/v1/analyses/black-holes && claude -p "/flf-epistack 0 — curated_target_N=25" \
  --model fable --effort max --permission-mode bypassPermissions
```

Every file in an analysis folder is produced from its `initial_prompt.md` by that command, with no hand-editing. Swap the folder and `curated_target_N` for the other cases (`covid` at 25, `eggs` at 50).

## Content versioning

The **site shell** — the Quartz reading surface and the pipeline — is version-agnostic and lives at the root. **Project content is versioned**: everything for one iteration sits under `content/vN/` and is served at `epistack.simonskade.org/vN/…`. Quartz maps content folders straight to URL paths, so no path-prefix config is involved; `baseUrl` stays the bare domain.

`v1` is the FLF-competition iteration. A future iteration that changes the method or the question set becomes `content/v2/` and is served alongside v1, so URLs already handed out keep resolving. Git tags freeze the *code*; `/vN/` freezes the *URLs*.

## Layout

1. `content/` — the site content (Quartz reads this).
   1. `content/index.md` — version-agnostic root landing page (what EpiStack is, links to the iterations).
   2. `content/v1/` — the FLF-competition iteration → `/v1/`.
      1. `content/v1/analyses/` — one folder per full-N analysis; each currently holds only its `initial_prompt.md`.
      2. `content/v1/analysis-tests/` — the three completed **low-N shakedown runs**, plus the known-failure-modes appendix. Kept separate from `analyses/` so the distinction stays legible.
      3. `content/v1/docs/` — the submission document and supporting documentation.
      4. `content/v1/index.md` — v1 landing page; doubles as the `/v1/` folder page.
2. `pipeline/` — the runnable EpiStack pipeline (a copy of the `flf-epistack` skill): `SKILL.md`, `steps/step-01…10`, and `runner/`. Not versioned by folder — use git tags.
   1. `.claude/skills/flf-epistack/` — the identical skill, at the path Claude Code resolves, so the reproduction command works in a fresh clone.
3. `quartz/`, `quartz.config.ts`, `quartz.layout.ts` — the Quartz static-site generator and its config. Patched in two places: node-type colours and hover-reveals-neighbours in the graph (`quartz/components/scripts/graph.inline.ts`), and the colour definitions in `quartz/styles/custom.scss`.
4. `scripts/check-internal-links.mjs` — post-build link check (see below).
5. `docs/website.md` — developer documentation for the website itself (not published to the site).

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

Needs only python 3 — no dependencies. One line per hypothesis-cluster, in `HC.hypotheses` order:

```
python3 pipeline/runner/run.py content/v1/analysis-tests/covid1
# HC-1  prior [0.3695, 0.1132, 0.5173]  posterior [0.4952, 0.0809, 0.4238]  (4 evidence block(s))
```

Every number in the graph is a **named variable with its reasoning beside it**, so any disputed assumption is one flag from a re-run. `--set BLOCK:var=value` re-prices one: `BLOCK` is a note id, `var` a named variable in that note's python block.

```
python3 pipeline/runner/run.py content/v1/analysis-tests/covid1 --set HC-1:uplift_coincident_lab_city=1.0
# HC-1  prior [0.4063, 0.0249, 0.5688]  posterior [0.5263, 0.0179, 0.4558]
#   ^ drop the one unsourced Fermi factor behind the lab-leak prior
```

That single re-setting takes the research-incident hypothesis from 8.1% to 1.8% — which is why the run's own report declines to treat that number as a finding. Setting a reliability weight `t=0` recovers the prior exactly.

`python3 pipeline/runner/test_run.py` self-checks the runner against the step 7/8 specs' published numbers, plus determinism, edge-order commutativity, and the sandbox guard.

## Deploy

The VPS cannot pull from GitHub, so deploy = build locally and `rsync` to the VPS, where Caddy serves `public/` as static files.

---

Built with [Quartz v4](https://quartz.jzhao.xyz/).
