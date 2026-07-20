---
title: "FLF EpiStack pipeline"
---

# FLF EpiStack pipeline

A 10-step pipeline that turns one contested empirical question (COVID origins, LHC black-hole risk, egg health, …) into a navigable Obsidian knowledge base whose Bayesian conclusion recomputes from the notes. Built for the FLF "Epistemic Stack" competition. The graph is the artifact; the answer is a report over it.

You are invoked with a step number (0-10) or a short description. Match it to the table, then **read that mode file — it is your full instruction set.** Steps 1-10 each do exactly one step, in place, on a given **analysis directory**; step 0 is the orchestrator that runs the whole pipeline by spawning the others. Steps run 1→10; each consumes the earlier steps' output and adds its own, never rewriting theirs.

| step | mode file                             | does                                                                                               |
| ---- | ------------------------------------- | -------------------------------------------------------------------------------------------------- |
| 0    | steps/step-00-orchestrate.md          | run the whole pipeline: brief and spawn each step's children                                       |
| 1    | steps/step-01-find-sources.md         | seed the graph: candidate primary `source`s (a wide pool for step 2)         |
| 2    | steps/step-02-curate-sources.md       | score trust + usefulness per source and map its data-basis (2a, ~10 each); one selector reconciles `D`s + flags curated ~N (2b)         |
| 3    | steps/step-03-extract.md              | extract each curated paper's `observation`/`hypothesis`/`argument` nodes (~5 papers/child)         |
| 4    | steps/step-04-structure-hypotheses.md | 4a merge near-duplicates + drop off-topic; 4b cluster survivors into `hypothesis-cluster`s         |
| 5    | steps/step-05-link-evidence.md        | one child per cluster: obs→cluster `evidence-link`s where they discriminate; consolidator wires args + correlation groups |
| 6    | steps/step-06-arguments.md            | assess each argument's validity (batched)                     |
| 7    | steps/step-07-priors.md               | select prior-relevant evidence-links (mark `used_for_prior`) + no-observation args, then write a prior block per cluster                                                      |
| 8    | steps/step-08-likelihoods.md          | one child per correlation-group (joint) or per ≤3 lone edges: write P(obs\|H) python blocks         |
| 9    | steps/step-09-cluster-review.md       | one human-readable review per cluster, beside its HC                                               |
| 10   | steps/step-10-final-report.md         | one main report answering the main question                                                        |

Filepaths are relative to the skill folder (`.claude/skills/flf-epistack/`).

## Node types

The analysis directory is a graph: each node is one markdown file (typed YAML frontmatter + prose body) in a per-type folder; edges are frontmatter wikilinks. An `evidence-link` note specifies an obs→cluster edge rather than a node in its own right. Two things are *not* nodes: `initial_prompt.md` at the analysis root, and everything under `agent-notes/` — agents' working notes, starting with `agent-notes/orientation/`, to which later steps may add subfolders of their own.

| prefix | folder | type |
|---|---|---|
| S | sources/ | source |
| D | data-bases/ | data-basis — shared underlying data; observations resting on the same one are correlated |
| O | observations-and-facts/ | observation (a.k.a. observations and facts: empirical findings and general facts about our world; henceforth just 'observation') |
| H | hypotheses/ | hypothesis |
| HC | hypothesis-clusters/ | hypothesis-cluster (mutually exclusive members) |
| A | arguments/ | argument |
| E | evidence-links/ | evidence-link |
| CG | correlation-groups/ | correlation-group — joint-likelihood home for edges whose observations share a data basis (built by step 5's consolidator) |

Two output files carry no id/prefix: the per-cluster review lives beside its cluster in `hypothesis-clusters/`, named `Analysis of HC-N - {rest of HC-N's title}.md`; the single final report sits at the analysis root, named `main report - {core research question}.md`.

## Shared conventions

1. The whole run turns on the main question, verbatim. It lives (with the FLF case framing) in the run's `initial_prompt.md` — the orchestrator reads the pre-staged file, or writes it if handed the case inline; every child gets the question quoted in its brief. `curated_target_N` and the analysis directory are passed at invocation, not stored in that file.
2. **Ids and filenames:** every node has an id = `PREFIX-N` (integer counter, no zero-padding), fixed at creation, never reused or renumbered. Filename = `PREFIX-N - Descriptive title.md`; there is no `title` field. (The two report files above are the exception — no id, fixed-form names.) Filenames are immutable — every reference is a full-filename `[[wikilink]]`, so renaming breaks inbound links; if a later edit makes a filename read wrong, fix the story in the body, keep the name.
3. **Additive edits, clear ownership:** steps mostly *add* fields to existing nodes; each mode file's Interface says which fields it owns. Don't overwrite another step's fields.
4. **Move, never delete:** retired nodes move to a sub-folder (`non-curated/`, `merged/`, `dropped/`, `orphan/`), keeping links and content, so the record stays auditable.
5. **Merges** (steps 3–4): survivor = lowest id in the merge set; absorbed nodes become tombstones (`merged_into` → survivor, resolving in one hop, never a chain) and move to `.../merged/`; the survivor lists the absorbed nodes' sources in `additional_sources` with a per-source `locator` list.
