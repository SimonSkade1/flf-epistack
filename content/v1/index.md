---
title: EpiStack v1 — FLF competition
---

**v1** is the iteration built for the [Future of Life Foundation](https://futureoflife.org/) epistemics competition. Everything below — analyses and docs — belongs to this iteration and keeps its URL under `/v1/` permanently; later iterations land at `/v2/` and so on. ([[index|What EpiStack is]].)

A browsable knowledge base for the **FLF epistemic-stack pipeline**: turning one contested empirical question into a Bayesian, navigable Obsidian-style graph — sources, observations, hypotheses, evidence links with runnable likelihood/prior code, per-cluster reviews, and one final report that answers the question.

This site is the reading surface. The [runnable pipeline](https://github.com/SimonSkade1/flf-epistack) that produces these knowledge bases lives in the same repository under `pipeline/`.

## Start here

1. [[MR-1 - What drove the extinction of Sahul's megafauna around 45-40 ka|Sample analysis — the final report]] — read one analysis top-to-bottom in ten minutes, then follow the backlinks down into the graph.
2. [[manifest|Sample analysis — manifest]] and [[structuring-manifest|its cluster map]] — how an analysis is scoped and decomposed.
3. [[v1/docs/index|Documentation]] — what the pipeline does, and how to read the node types.

## What an analysis looks like

Every box in the debate is one markdown note with typed frontmatter, linked to the others:

1. **sources** (`S-N`) and **data-bases** (`D-N`) — the evidence base and the shared datasets it rests on.
2. **observations** (`O-N`) — findings that follow ~with certainty from a source's data.
3. **hypotheses** (`H-N`), grouped into mutually-exclusive **hypothesis-clusters** (`HC-N`).
4. **evidence-links** (`E-N`) — observation → cluster edges, each carrying a runnable `## Likelihood` code block.
5. **arguments** (`A-N`), **cluster-reviews** (`CR-N`), and the **main-report** (`MR-1`) that answers the question.

The current sample ([[MR-1 - What drove the extinction of Sahul's megafauna around 45-40 ka|Sahul megafauna extinction]]) is a hand-written **structural demo** — illustrative numbers, but every node type, folder, wikilink, embed, and code block a real run produces. Real analyses replace it as they finish.

> [!info] How to read the published runs
> `analysis-tests/` holds three end-to-end runs, one per case study, at 5–10 curated sources each (COVID origins and eggs at N=10, LHC black holes at N=5). These are deliberately small shakedown runs: all ten steps ran and every posterior recomputes from the notes, but each rests on a thin evidence base, so read them as a demonstration of the method rather than as settled answers. Fuller runs land in `analyses/`. Defects the runs exposed are listed in the failure-modes appendix rather than quietly fixed.
