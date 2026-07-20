---
title: The pipeline
---

This is the **specification the analyses were produced by** — the `flf-epistack` Claude Code skill, published here so the method is auditable without cloning anything. It is the same text the agents actually execute, not a write-up of it.

The pipeline runs as one orchestrator plus per-step child agents. Each step below states what it consumes, what it must write, and the checks that gate it before the next step starts.

## Read it

1. [[SKILL|The skill definition]] — the entry point: node ontology, folder layout, the rules every step obeys, and the invocation contract.

### The ten steps

1. [[step-00-orchestrate|Step 0 — Orchestrate the run]]
2. [[step-01-find-sources|Step 1 — Find primary sources]]
3. [[step-02-curate-sources|Step 2 — Curate sources]]
4. [[step-03-extract|Step 3 — Extract observations, hypotheses, and arguments from a paper]]
5. [[step-04-structure-hypotheses|Step 4 — Structure hypotheses]]
6. [[step-05-link-evidence|Step 5 — Link observations to hypothesis-clusters]]
7. [[step-06-arguments|Step 6 — Assess argument validity]]
8. [[step-07-priors|Step 7 — Estimate priors]]
9. [[step-08-likelihoods|Step 8 — Estimate likelihoods per (cluster, observation)]]
10. [[step-09-cluster-review|Step 9 — Per-cluster review of the analysis]]
11. [[step-10-final-report|Step 10 — Final report answering the main question]]

## The code

Rendered on GitHub, which does code better than this site does:

1. [`runner/run.py`](https://github.com/SimonSkade1/flf-epistack/blob/main/pipeline/runner/run.py)
2. [`runner/test_run.py`](https://github.com/SimonSkade1/flf-epistack/blob/main/pipeline/runner/test_run.py)
3. [`scripts/attach_argument_backlinks.py`](https://github.com/SimonSkade1/flf-epistack/blob/main/pipeline/scripts/attach_argument_backlinks.py)
4. [`scripts/batch_arguments.py`](https://github.com/SimonSkade1/flf-epistack/blob/main/pipeline/scripts/batch_arguments.py)
5. [`scripts/batch_likelihoods.py`](https://github.com/SimonSkade1/flf-epistack/blob/main/pipeline/scripts/batch_likelihoods.py)
6. [`scripts/build_correlation_groups.py`](https://github.com/SimonSkade1/flf-epistack/blob/main/pipeline/scripts/build_correlation_groups.py)
7. [`scripts/check_missing_evidence_links.py`](https://github.com/SimonSkade1/flf-epistack/blob/main/pipeline/scripts/check_missing_evidence_links.py)
8. [`scripts/create_node.py`](https://github.com/SimonSkade1/flf-epistack/blob/main/pipeline/scripts/create_node.py)
9. [`scripts/curation_select.py`](https://github.com/SimonSkade1/flf-epistack/blob/main/pipeline/scripts/curation_select.py)
10. [`scripts/no_observation_arguments.py`](https://github.com/SimonSkade1/flf-epistack/blob/main/pipeline/scripts/no_observation_arguments.py)

The runner (`runner/run.py`) is the piece that makes the answer recompute: it extracts the `## Prior` and `## Likelihood` python blocks from the notes, enforces determinism (arithmetic over named variables only — no imports, randomness, clock or I/O), and composes each cluster's posterior. `runner/test_run.py` checks it against the numbers the step 7 and 8 specs publish.

> [!note] Generated copy
> These pages are generated from `pipeline/` by `scripts/sync-pipeline-to-content.mjs`. Edit the source, not these. Wikilinks appearing in the step specs are *syntax examples*, shown verbatim rather than linked.
