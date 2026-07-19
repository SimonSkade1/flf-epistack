# FLF EpiStack

A browsable knowledge base and the runnable pipeline behind it, for the **Future of Life Foundation epistemics competition**. The pipeline turns one contested empirical question into a Bayesian, navigable graph of typed Obsidian-style notes; this repo also serves that graph as a static website via [Quartz](https://quartz.jzhao.xyz/).

Live site: **https://flf.simonskade.org** (also reachable at http://91.98.229.7 until DNS propagates).

## Layout

1. `content/` — the site content (Quartz reads this).
   1. `content/analyses/` — one folder per analysis. `sample-sahul-megafauna/` is a hand-written **structural demo** exercising every node type, folder, wikilink, embed, and code block a real run produces (illustrative numbers). Real runs are added here.
   2. `content/docs/` — documentation (draft).
   3. `content/index.md` — landing page.
2. `pipeline/` — the runnable FLF EpiStack pipeline (a copy of the `flf-epistack` skill): `SKILL.md`, `steps/step-01…10`, and `runner/`.
3. `quartz/`, `quartz.config.ts`, `quartz.layout.ts` — the Quartz static-site generator and its config.

## Build the site

```
npm i                     # once
npx quartz build          # emits ./public
npx quartz build --serve  # local preview at http://localhost:8080
```

## Run the Bayesian model of an analysis

```
python3 pipeline/runner/run.py content/analyses/sample-sahul-megafauna
# HC-1  prior [...]  posterior [...]  (N evidence block(s))

# price any named variable and re-run:
python3 pipeline/runner/run.py content/analyses/sample-sahul-megafauna --set E-14:t_dates=1.0
```

`pipeline/runner/test_run.py` self-checks the runner against the specs' published numbers.

## Deploy

The VPS cannot pull from GitHub, so deploy = build locally and `rsync` to the VPS, where Caddy serves `public/` as static files.

---

Built with [Quartz v4](https://quartz.jzhao.xyz/).
