# Step 0 — Orchestrate the run

You run the whole pipeline on one analysis directory: steps 1→10, in order, by briefing and spawning the children that do each step's work. You do none of that work yourself — your job is deciding how much of it happens, how it splits across children, and giving each child a brief it can act on without further context.

**v0.1** — steps 1 and 2 are worked out below; steps 3-10 carry only a parallelism default and will be refined.

## Inputs

1. **main question** — verbatim; the string the whole run turns on. Read it (with the FLF case framing) from `<analysis-dir>/initial_prompt.md`.
2. **`curated_target_N`** — passed at invocation, not stored in `initial_prompt.md`: roughly how many sources step 2 should curate down to. The step-1 budgets are multiples of it.
3. **analysis directory** — passed at invocation; the folder to build in (it holds `initial_prompt.md`); create it if missing.

**First actions, before spawning anything.** Lay out the directory, then record what was asked:

```
mkdir -p <analysis-dir>/{sources,data-bases,observations-and-facts,hypotheses,hypothesis-clusters,arguments,evidence-links,agent-notes/orientation}
```

`<analysis-dir>/initial_prompt.md` holds the case **verbatim** — the main question plus the FLF case framing. Usually it is pre-staged, so just read it; if you were instead handed the case inline, write it there first. It does **not** carry `N` — that is passed at invocation. You are the only one holding the framing first-hand; every child downstream works from your paraphrase unless it can read the original. (`create_node.py` makes folders on demand, so the skeleton is for legibility, not necessity.)

## Running a step

Spawn children with the Agent tool — one per unit of work, in parallel where the units are independent. (Workflows may replace this later; for now, subagents.) **Models (set explicitly per child if the harness allows — if it can't set a child's model, no worries: just inherit and continue).** Run the step-1 planner and consolidator (1a, 1c) and both step-2 substeps (2a, 2b) on **opus** — these judgment-heavy steps want opus-level reasoning, so give them opus even when your own session model is a *pricier* one (e.g. fable): don't upgrade them above opus. The only exception: if your own session model is *cheaper/weaker* than opus (e.g. sonnet, haiku), let those steps use your session model rather than upgrading to opus. Searchers (1b, top-up rounds included) run on **sonnet**. Every other child — steps 3–10, fixers — gets no model override and so inherits your session model (usually fable). Children never spawn children of their own: all fan-out is yours, so ids, budgets and slices stay under one controller.

Every child gets a brief on this template — filled in, nothing left implicit:

```
Read .claude/skills/flf-epistack/steps/<mode file> — it is your full instruction set.
Analysis directory: <path>
Main question (verbatim): "<main_question>"
Your slice: <the one search thread / paper / cluster you own, and what you must not touch>
Budget: <how much to read and write, in the step's own units>
Mint every id'd node with:
  python3 .claude/skills/flf-epistack/scripts/create_node.py <analysis-dir> --type <type> --title "..."
Never hand-pick an id, and do not spawn subagents.
Return: <what you need back — ids created, gaps hit, a short report>
```

The slice and the budget are what make parallel children safe: two children with overlapping slices duplicate work, and a child without a budget spends the whole step's allowance.

## Step 1 — find sources

**1a — plan the search** (one child). Brief it with the question, the FLF case framing from `initial_prompt.md` (the case's scope and what matters), `N`, and the step-1 budget: ~4N `source` notes written, ~8N sources read properly, and far more skimmed through meta-analyses, related-work sections and reference lists. It surveys which literatures bear on the question, which sides the debate has, and which datasets keep recurring, then divides the search into slices — subfield, side of the debate, or search thread. Require it to plan for **balance and independence**: every side represented, and slices aimed at sources resting on genuinely independent data rather than at forty re-analyses of one dataset. No individual searcher can see the pool, so this is the only place that shape gets chosen.

Its deliverable is **the finished prompt for each 1b child**, each written on the template above and each stating how many `source` notes that searcher creates and how many sources it reads properly — the per-searcher counts summing to the step-1 totals. 1a plans and writes prompts; it does not search and does not spawn. Have it put plan and prompts in its own file under `agent-notes/orientation/`, so the division survives context loss and 1c can audit against it. Check each prompt is complete — slice, counts, mode file, what to return — then spawn it as written.

**1b — search** (one child per slice, in parallel). Spawn exactly the prompts 1a wrote. Each reads `steps/step-01-find-sources.md` and finishes by writing its own note in `agent-notes/orientation/` covering the slice it worked.

**1c — consolidate** (one child, once every searcher has returned; it also reads `steps/step-01-find-sources.md`, where the orientation-note spec lives). It resolves duplicates — the same source minted twice by searchers working blind to each other — then writes its own file in `agent-notes/orientation/`: the consolidated pool overview that step 2 starts from, the union of the searchers' exclusions, and an audit against 1a's plan reporting which sides or independent-data axes came out thin. On a thin report, spawn a top-up round of searchers for the gap and re-run the audit.

## Step 2 — curate sources

**2a — score** (one child per ~10 sources, in parallel). Split the pool **by source id** and give each child its ids as its slice — disjoint id lists mean no two scorers ever open the same file. Each scores only its own, maps its data provenance (creating `data-basis` (`D`) nodes and setting each source's `data_basis`), and writes no cut decision. Both scales are absolute, so slices don't need to see each other; tell each child its slice is a list of ids, not a share of the ranking.

**2b — select** (one child, once every scorer has returned). It first reconciles duplicate `D` nodes minted by parallel scorers, then runs `scripts/curation_select.py`, checks the slices scored comparably, makes the cut, moves the non-curated aside and writes `agent-notes/curation.md`. Brief it with `curated_target_N`. Keep this single: the baseline knob and the skew trade-offs need the whole pool in view.

## Step 3 — extract

**One child per ~5 curated papers, in parallel** (~N/5 children). Split the curated pool **by source id** and give each child a disjoint list of ~5 ids as its slice — disjoint slices mean no two children open the same paper. Each reads `steps/step-03-extract.md`, extracts the `observation` / `hypothesis` / `argument` nodes for its papers, attributes each observation's data provenance, and returns the ids it created. Every node is minted through `create_node.py` (next free id under a lock), so parallel children never collide on `O` / `H` / `A` / `D` ids — no id blocks to hand out.

**Then one consolidator child** (once every extractor has returned; it also reads `steps/step-03-extract.md`) does two global cleanups: (1) merges duplicate `D` nodes that parallel extractors minted as stragglers for the same dataset (step 2 created and deduped the bulk; step 5's correlated-evidence detection keys on shared `D`-node identity, so a duplicate would hide real correlation); (2) merges near-duplicate `generally_known` observations, since the same generally-known fact referenced by two papers is one fact, not independent evidence (the Consolidate step in step 3). Same split-by-id-then-consolidate shape as step 1's 1c.

## Step 4 — structure hypotheses

Two children in sequence, each single because its judgment needs the whole hypothesis set in one view.

**4a — deduplicate + drop** (one child). It reads `steps/step-04-structure-hypotheses.md`, merges near-duplicate `H` nodes (survivor = lowest id, absorbed nodes tombstoned to `hypotheses/merged/`) and drops the off-topic to `hypotheses/dropped/`, leaving a deduplicated set of `active` hypotheses. One child — the merge test weighs every hypothesis against every other, so the whole pile must be in one view; a split would merge blind.

**4b — cluster** (one child, once 4a returns; also reads `steps/step-04-structure-hypotheses.md`). It groups the surviving `active` hypotheses into mutually-exclusive `HC` clusters, mints the `HC` nodes and any residual/constructed members via `create_node.py`, sets each active's `cluster` backlink, and writes the cluster map to `agent-notes/structure.md`. One child — the carving needs every survivor in view.

## Step 5 — link evidence

**One child per hypothesis-cluster, in parallel.** Give each child one `HC` as its slice; it reads `steps/step-05-link-evidence.md` and mints the `evidence-link` (`E`) edges from every observation that discriminates its cluster's members. It does **not** touch arguments or correlation — both are wired mechanically by the consolidator. Slices are disjoint by construction — each active `H` belongs to exactly one cluster and each child creates only its cluster's edges — so no two children touch the same file, and `create_node.py` keeps `E` ids collision-free.

**Then one consolidator child** (once every cluster-child has returned) does three global jobs in order: (1) runs `python3 .claude/skills/flf-epistack/scripts/attach_argument_backlinks.py <analysis-dir>`, which writes each edge's `arguments` list from the step-3 `affects_observations` backlinks and moves an argument to `arguments/orphan/` only when it has no `affects_hypotheses` entry and none of its `affects_observations` sits on a live edge; (2) runs `python3 .claude/skills/flf-epistack/scripts/build_correlation_groups.py <analysis-dir>`, which mints the `correlation-group` (`CG`) nodes over connected components of edges whose observations share a data basis and writes each member edge's `group`; (3) sets `link_state` on every `O` — linked iff it is the `from` of some edge, else orphan — and moves orphan observations to `observations-and-facts/orphan/`. All three are global: an observation is an orphan only if *no* cluster linked it, so none can be decided per cluster. End the step with `python3 .claude/skills/flf-epistack/scripts/check_missing_evidence_links.py <analysis-dir> --cluster all` (reports only): it flags (observation, argument) pairs implying an evidence-link no cluster-child created — spawn a fixer for any real gap before gating.

## Step 6 — assess arguments

**One child per batch of ≤20 arguments, in parallel.** Run `python3 .claude/skills/flf-epistack/scripts/batch_arguments.py <analysis-dir>` (reports only — it never edits or moves a file) to batch every top-level argument into ≤20s. Spawn one child per batch reading `steps/step-06-arguments.md`, its batch (the argument paths) as its slice; each assesses its own arguments' validity, writing `status` / `reason_if_not_false` (and, for a `corrected` argument, an edited `statement` + `## Original`) on its own arguments only. Batches are disjoint, so parallel writes never collide.

Gate step 6's Checks before step 7.

## Step 7 — estimate priors

**One child per cluster, in parallel** (small — a prior block is a few lines). Each reads `steps/step-07-priors.md`; its slice is one `HC` node. It consults the cluster's connected evidence-links and its no-observation arguments (`python3 .claude/skills/flf-epistack/scripts/no_observation_arguments.py <analysis-dir> --cluster HC-N`), selects the prior-relevant links (e.g. base rates), writes a single `## Prior` block pricing that cluster's members, and marks each edge it used `used_for_prior: true` so step 8 won't double-count it. Clusters are disjoint, so no two children touch the same file, and these priors are in before step 8's likelihoods.

## Step 8 — estimate likelihoods

Work splits **by evidence-link, not by cluster**: correlated edges are priced by one joint call and every other edge on its own, and those units are independent, so hand them out directly. Run `python3 .claude/skills/flf-epistack/scripts/batch_likelihoods.py <analysis-dir>` (reports only — it never edits a file) to get the units; each is either one `correlation-group` (`CG-N`, built by step 5's consolidator) or a batch of ≤3 lone edges. Edges step 7 marked `used_for_prior` are excluded from the units and instead listed under "already accounted for in the prior — do not double-count" (with each cluster's no-observation arguments), so step 8 never re-prices what the prior already spent. Raise `--batch-size` for fewer, larger children.

**One child per unit, in parallel.** Each reads `steps/step-08-likelihoods.md`; its slice is exactly the edges the script assigned it and nothing else — pass the unit's edge ids (`assess`) and where to write (`block_on`: the CG node, or each edge note) from the script's JSON straight into the brief.

- a `CG-N` unit → the child prices its member edges **jointly** and writes the group's single `## Likelihood` block on the `CG-N` node;
- an independent batch → the child prices each of its ≤3 lone edges and writes one `## Likelihood` block per edge note.

Units are disjoint by construction — each edge belongs to exactly one — so no two children touch the same file, and a child's batch may span clusters (each edge names its own `to`). No consolidator: nothing here is global.

## Steps 9-10

Defaults for how many children each step takes:

| step | children |
|---|---|
| 9 | one per cluster |
| 10 | one — it reads the cluster reviews and writes the single report |

## Gating

Each mode file ends with binary **Checks**. Run them before starting the next step; on failure, spawn a fixer child with the failing check and the offending files, then re-check. Later steps assume the invariants hold, so a half-finished step is worse than one that never ran.

**After step 8, before step 9, run the model once:** `python3 .claude/skills/flf-epistack/runner/run.py <analysis-dir>` composes each cluster's step-8 likelihoods with its step-7 prior and prints `HC-N  prior [...]  posterior [...]` per cluster. Step 7 writes the priors and step 8 the likelihoods, so this is the first point at which a fully-composed posterior exists — making it the gate that catches a wrong-length vector, a cluster missing a prior or likelihood, or a banned token, and the reason no step-8 child composes the model itself. Steps 9-10 read the posteriors it produces.
