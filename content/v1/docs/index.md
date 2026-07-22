---
title: Documentation
---

> [!note] What is authoritative here
> [[submission|The submission document]] is the frozen FLF entry. The authoritative specification of the method is the pipeline itself, published step by step at [[v1/pipeline/index|/v1/pipeline/]] (source: `content/v1/pipeline/SKILL.md` + `content/v1/pipeline/steps/` in the [repository](https://github.com/SimonSkade1/flf-epistack)). Anything else on this site is a reading aid.

## Pages

0. [[submission|The submission document]] — **start here.** The ≤10-page written core of the FLF entry: the principles, the pipeline (with the agent fan-out graphic), the ontology, the Bayesian logic, the cases, the limitations, and how to run it.
1. [[navigating-an-analysis|How to navigate an analysis]] — the node types and folder layout, one worked chain from the answer down to the dataset it rests on, how the `## Prior` / `## Likelihood` code blocks compose into a posterior, and how to re-price any number yourself. Written after the deadline.
2. [[v1/pipeline/index|The pipeline]] — the 10-step specification the analyses were produced by, browsable step by step, plus the runner and scripts.

## What this is

The EpiStack pipeline takes **one contested empirical question** and builds a Bayesian knowledge base that a human can audit: not a single opaque answer, but a graph of typed notes where every number is a named, overridable variable with its reasoning beside it. The design targets a set of [cross-cutting criteria](https://github.com/SimonSkade1/flf-epistack) — auditability, navigability (a bounded top layer with curated entry points), updateability (add evidence and re-run), and honest treatment of out-of-model mass (a residual member that competes in every posterior).
