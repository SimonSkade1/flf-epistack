---
title: Documentation
---

> [!note] Draft
> Placeholder documentation for the FLF submission. The prose here is a dummy scaffold; the authoritative spec is the pipeline itself (`pipeline/SKILL.md` + `pipeline/steps/` in the [repository](https://github.com/SimonSkade1/flf-epistack)).

## Pages

0. [[submission|The submission document]] — **start here.** The ≤10-page written core of the FLF entry: the principles, the pipeline (with the agent fan-out graphic), the ontology, the Bayesian logic, the cases, the limitations, and how to run it.
1. [[pipeline-overview|The 10-step pipeline]] — what each step consumes and produces.
2. [[reading-an-analysis|Reading an analysis]] — the node types and folder layout, and how to follow the graph.
3. [[running-the-model|Running the model]] — how the `## Prior` / `## Likelihood` code blocks compose into a posterior.

## What this is

The EpiStack pipeline takes **one contested empirical question** and builds a Bayesian knowledge base that a human can audit: not a single opaque answer, but a graph of typed notes where every number is a named, overridable variable with its reasoning beside it. The design targets a set of [cross-cutting criteria](https://github.com/SimonSkade1/flf-epistack) — auditability, navigability (a bounded top layer with curated entry points), updateability (add evidence and re-run), and honest treatment of out-of-model mass (a residual member that competes in every posterior).
