---
title: The 10-step pipeline
---

> [!note] Draft — summarised from `pipeline/steps/`. The step files are authoritative.

Each step is one mode of the `flf-epistack` skill, run in place on a single analysis directory, then handed to the next. No step invents numbers before step 7.

1. **Find sources** — from the main question, gather candidate primary sources and firmly-established background observations; record a `manifest.md` (verbatim question, scope, exclusions).
2. **Curate sources** — score each source by trust and relevance; keep the best ~1/5, move the rest to `sources/non-curated/` (never delete). Sets each source's `trust_score`.
3. **Extract** — per curated paper, extract `observation`, `hypothesis`, and `argument` nodes, and resolve each source's `data_basis` (the shared datasets/instruments findings rest on).
4. **Structure hypotheses** — merge near-duplicate hypotheses, drop off-topic ones, and carve the survivors into mutually-exclusive `hypothesis-cluster` nodes, each with a residual "none of these" member.
5. **Link evidence** — for every observation that *discriminates* a cluster's members, mint an `evidence-link` edge; flag correlated observations that share a data basis; attach prior-shaping arguments to hypotheses.
6. **Assess arguments** — judge each argument's inferential validity (`approved` / `corrected` / `rejected`), separately from how strong it is.
7. **Likelihoods** — price each edge: P(observation | member) as a runnable `## Likelihood` code block; correlated observations get one joint estimate.
8. **Priors** — a Fermi `## Prior` block per cluster, before its evidence is read.
9. **Cluster reviews** — one human-readable review per cluster: what it concluded, what the model may miss, what would help, where evidence conflicts.
10. **Final report** — one `main-report` answering the main question, over the whole graph, with ≤10 curated entry points.

Steps 7-8 write the code the [model runner](running-the-model.md) executes; steps 9-10 are the prose layer a judge reads.
