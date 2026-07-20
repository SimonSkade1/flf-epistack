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

> [!info] Status at the submission deadline
> I ran out of Claude usage allowance before the large runs finished, so what is **complete at the deadline** are three end-to-end **shakedown runs** — one per case study, under `analysis-tests/` (COVID origins and eggs at N=10, LHC black holes at N=5 curated sources). They are small but real: every posterior on those pages recomputes from the notes, and all ten steps ran.
>
> Larger runs (N=25–50) are queued and should land here within roughly a day. If the pipeline itself improves rather than just the runs, that work will appear under `/v2/` alongside v1 rather than overwriting it — read whichever is more informative. Known defects the shakedown surfaced are listed in the failure-modes appendix rather than quietly fixed.
