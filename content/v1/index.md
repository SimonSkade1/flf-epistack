---
title: EpiStack v1 — FLF competition
---

**v1** is the iteration built for the [Future of Life Foundation](https://futureoflife.org/) epistemics competition. Everything below — analyses and docs — belongs to this iteration and keeps its URL under `/v1/` permanently; later iterations land at `/v2/` and so on. ([[index|What EpiStack is]].)

A browsable knowledge base for the **FLF epistemic-stack pipeline**: turning one contested empirical question into a Bayesian, navigable Obsidian-style graph — sources, observations, hypotheses, evidence links with runnable likelihood/prior code, per-cluster reviews, and one final report that answers the question.

This site is the reading surface. The [runnable pipeline](https://github.com/SimonSkade1/flf-epistack) that produces these knowledge bases lives in the same repository under `pipeline/`.

## Start here

1. [[submission|The submission document]] — the written core of the FLF entry: principles, pipeline, ontology, Bayesian logic, cases, limitations.
2. **The three end-to-end runs**, each a real pipeline output you can read top-to-bottom and then follow down into the graph:
	1. [[main report - Did SARS-CoV-2 first infect humans through natural zoonotic spillover or through a research-related incident|COVID origins]]
	2. [[main report - Was the risk that LHC collisions destroy the Earth truly put to rest and what does that conclusion hinge on|LHC black holes]]
	3. [[main report - Is habitual egg consumption net beneficial, harmful, or neutral for human health|Eggs and health]]
3. [[APPENDIX - known failure modes|Known failure modes]] — 3 BLOCKERs and 33 MAJORs, each logged by an agent inside the run that hit it, including one defect claim the run then retracted.
4. [[v1/pipeline/index|The pipeline itself]] — the 10-step specification the runs were produced by, browsable step by step.
5. [[v1/docs/index|Documentation]] — what the pipeline does, and how to read the node types.

## What an analysis looks like

Every box in the debate is one markdown note with typed frontmatter, linked to the others:

1. **sources** (`S-N`) and **data-bases** (`D-N`) — the evidence base and the shared datasets it rests on.
2. **observations** (`O-N`) — findings that follow ~with certainty from a source's data.
3. **hypotheses** (`H-N`), grouped into mutually-exclusive **hypothesis-clusters** (`HC-N`).
4. **evidence-links** (`E-N`) — observation → cluster edges, each carrying a runnable `## Likelihood` code block.
5. **arguments** (`A-N`), **cluster-reviews** (`CR-N`), and the **main-report** (`MR-1`) that answers the question.

A hand-written structural demo of this schema (`sample-sahul-megafauna`) used to sit here. It was withdrawn after the submission deadline: its numbers were illustrative rather than pipeline-computed, which on a site whose whole claim is that every number recomputes from the notes is a liability rather than an aid. The three runs above are the real thing.

> [!info] How to read the published runs
> `analysis-tests/` holds three end-to-end runs, one per case study, at 5–10 curated sources each (COVID origins and eggs at N=10, LHC black holes at N=5). These are deliberately small shakedown runs: all ten steps ran and every posterior recomputes from the notes, but each rests on a thin evidence base, so read them as a demonstration of the method rather than as settled answers. Fuller runs land in `analyses/`. Defects the runs exposed are listed in the [[APPENDIX - known failure modes|failure-modes appendix]] rather than quietly fixed.
