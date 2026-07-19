---
title: Reading an analysis
---

> [!note] Draft. Worked against the sample [[MR-1 - What drove the extinction of Sahul's megafauna around 45-40 ka|Sahul megafauna analysis]].

An analysis is one folder of markdown notes. Read it top-down:

1. Start at the **main-report** `MR-1` — the bottom line and ≤10 curated entry points.
2. Follow an entry point into a **cluster-review** `CR-N` (prose) or a **hypothesis-cluster** `HC-N` (the members + the prior).
3. From there, backlinks take you down to the **evidence-links**, **observations**, and **sources** doing the work.

## Node types and where they live

| prefix | type | folder | what it is |
|---|---|---|---|
| `S-N` | source | `sources/` (dropped → `sources/non-curated/`) | a paper/dataset/book; carries `trust_score` |
| `D-N` | data-basis | `data-bases/` | a shared dataset/instrument several findings rest on |
| `O-N` | observation | `observations/` (unlinked → `observations/orphan/`) | a finding that follows ~with certainty from data |
| `H-N` | hypothesis | `hypotheses/` (`merged/`, `dropped/`) | an uncertain candidate answer |
| `HC-N` | hypothesis-cluster | `hypothesis-clusters/` | one sub-question + its mutually-exclusive answers; holds the `## Prior` |
| `E-N` | evidence-link | `evidence-links/` | observation → cluster edge; holds the `## Likelihood` |
| `A-N` | argument | `arguments/` (`merged/`, `orphan/`) | a nontrivial inference or calculation |
| `CR-N` | cluster-review | `cluster-reviews/` | the human-readable review of one cluster |
| `MR-1` | main-report | analysis root | the answer to the main question |

Plain files (`manifest.md`, `orientation.md`, `structuring-manifest.md`) are maps, not graph nodes.

## Reading the graph

1. **Nothing is deleted, only moved.** A merged hypothesis, an orphaned observation, a non-curated source all keep their links in a sub-folder — the record stays auditable.
2. **Correlation matters.** Two observations resting on the same `D-N` are one witness; the site shows this as a shared backlink and a joint likelihood block.
3. **Every number is overridable.** See [[running-the-model|Running the model]].
