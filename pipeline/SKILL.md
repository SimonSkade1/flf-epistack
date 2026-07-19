---
name: flf-epistack
description: The FLF EpiStack analysis pipeline — turning one contested empirical question into a Bayesian, navigable Obsidian knowledge base in 10 steps. Invoked explicitly for a single step (by number 1-10 or a step description); not auto-triggered.
---

# FLF EpiStack pipeline

A 10-step pipeline that turns one contested empirical question (COVID origins, LHC black-hole risk, egg health, …) into a navigable Obsidian knowledge base whose Bayesian conclusion recomputes from the notes. Built for the FLF "Epistemic Stack" competition. The graph is the artifact; the answer is a report over it.

Each step is a **mode** of this skill with its own instruction file under `steps/`. An orchestrator invokes the skill once per step; you do exactly one step, in place, on a given **analysis directory** (a folder of markdown notes), then hand off to the next.

## Selecting your mode

You are invoked with a step number (1-10) or a short description. Match it to the table, then **read that mode file — it is your full instruction set for the step** (schema, rules, process, checks, and how it connects to neighbouring steps). Read the shared sections below too; the mode files rely on them and don't repeat them.

| step | mode file | does | model |
|---|---|---|---|
| 1 | steps/step-01-find-sources.md | seed the graph: candidate primary `source`s + firmly-established background `observation`s | opus + sonnet subagents |
| 2 | steps/step-02-curate-sources.md | score trust + usefulness per source; flag the curated ~N subset | opus |
| 3 | steps/step-03-extract.md | one subagent per curated paper: extract its `observation`/`hypothesis`/`argument` nodes | fable |
| 4 | steps/step-04-structure-hypotheses.md | drop / merge / cluster hypotheses into mutually-exclusive `hypothesis-cluster`s | fable |
| 5 | steps/step-05-link-evidence.md | obs→cluster `evidence-link`s where they discriminate + per-hypothesis argument lists | fable |
| 6 | steps/step-06-assess-arguments.md | merge duplicate arguments, then assess each survivor's validity | fable |
| 7 | steps/step-07-likelihoods.md | write P(obs\|H) python blocks per (cluster, correlated group); compose posteriors | fable |
| 8 | steps/step-08-priors.md | write a prior-weight python block per cluster | fable |
| 9 | steps/step-09-cluster-review.md | one human-readable `cluster-review` per cluster | fable |
| 10 | steps/step-10-final-report.md | one `main-report` answering the main question | fable |

Steps run 1→10; each consumes the earlier steps' output and adds its own, never rewriting theirs.

## The knowledge base (shared by every step)

1. **An analysis = one directory of markdown notes**, edited in place. The whole run turns on `manifest.main_question` (verbatim, written at step 1).
2. **Every graph node is one markdown file:** typed YAML frontmatter (the fields) + prose body, in a per-type folder — `sources/`, `data-bases/`, `observations/`, `hypotheses/`, `arguments/`, `hypothesis-clusters/`, `evidence-links/`, `cluster-reviews/`, and the `MR-*` report at the root. Plain files (`manifest.md`, `orientation.md`, `*-manifest.md`) are not nodes.
3. **Ids and filenames.** Each node has an id `PREFIX-N` (integer counter, no zero-padding, no upper bound), fixed at creation and never reused or renumbered. Filename = `PREFIX-N - Descriptive title.md` — there is no `title` field, the filename is the title. **Filenames are immutable:** every reference is a full-filename `[[wikilink]]` (`[[S-1 - Re-dated last-appearance ages for Sahul's extinct megafauna]]`), so renaming breaks inbound links. This holds even when a later edit makes a filename read wrong (e.g. a corrected argument) — fix the story in the body, keep the name.
4. **Reserved prefixes:** `S` source · `D` data-basis · `O` observation (step-1 background + step-3 paper obs, distinguished by the `general` field) · `H` hypothesis · `HC` hypothesis-cluster · `A` argument · `E` evidence-link · `CR` cluster-review (one per `HC`, shares its number) · `MR` main-report.
5. **Additive edits, clear ownership.** Each step mostly *adds* fields to existing nodes; each mode file's Interface says which fields it owns. Don't renumber ids and don't overwrite another step's fields.
6. **Move, never delete.** Retired nodes move to a sub-folder, keeping their links and content, so the diff shows the change and the record stays auditable: `sources/non-curated/` (step 2), `hypotheses/merged/` + `hypotheses/dropped/` (step 4), `observations/orphan/` + `arguments/orphan/` (step 5), `arguments/merged/` (step 6).
7. **Merge bookkeeping** (steps 4, 6). Survivor = **lowest id** in the merge set. Absorbed nodes become tombstones (`merged_into` → survivor, resolving in **one hop**, never a chain) and move to `.../merged/`; the survivor keeps its own single `source`, lists the absorbed nodes' sources in `additional_sources`, and carries a per-source `locator` list. This is the one place a node ends up resting on >1 source.

## Cross-cutting criteria

The output is judged against these; mode files cite them by number, and they are the reason the machinery is shaped the way it is. Keep them in view rather than treating them as a checklist. (Numbers are criterion ids, not list order.)

**2. Calibration** — probabilities carry an explicit out-of-model / unknown-unknown term (the residual member is where it lives), neither sanded off nor inflated; would you bet at these odds?
**3. Correct aggregation** — correlated evidence (observations sharing a `data-basis` node) is never counted as independent; it gets one joint likelihood. Treating it as independent is the standard way Bayesian aggregation manufactures false confidence.
**4. Trust separated from truth** — data-reliability comes from source features (`trust_score`); the truth of a claim is judged independently and arguments on their own merits; refuted items excluded.
**5. Provenance** — every load-bearing claim reaches a primary source in ≤2 hops via `source`/`locator`.
**6. Driver visibility** — name (in prose) the few things the answer hangs on; naming them is required, pricing them with a re-run is optional.
**7. Structure / weights separation** — the graph reads with zero numbers present; all weights are named python variables a skeptic can override and re-run. Nothing derived is cached in frontmatter.
**8. Method legibility** — scope, inclusion/exclusion, and assumptions are explicit at point of use.
**9-12. Interrogable / navigable / updateable / composable** — typed nodes with queryable frontmatter; a bounded top layer (≈ the judges' 10-page reading budget) with curated entry points; new evidence can be added and the posterior re-run; the same types serve any question.
**14. Reproducibility** — the python blocks are deterministic: arithmetic over named variables, no import/RNG/clock/network/LLM. Same notes → same posterior.
**15. Independent impression** — conclusions come from your own modelling, not deference to prestige/consensus. `trust_score` is the *only* channel venue/author/citations enter, and only as data-reliability; the verdict must stay derivable with author/venue stripped. External consensus is stored labelled (`external_consensus`) and mixed into no number.
**16. Explicit gaps** — what's missing / what would change the answer is listed and tied to specifics; distinguish what the debate settled from what it merely performed.

Two Simon calls: **criterion 1** (the conclusion must be *recomputable* from the graph) is **not endorsed** — the cluster-level Bayesian machinery answers sub-questions and step 10 draws them together in prose; keep "don't overreach, don't contradict the model", drop "recomputable". **Criterion 13** (adversarial robustness; actively searching counterarguments for motivated sources) is real but deprioritized for the deadline — still remember motivatedness has two effects: it lowers data-trust *and* makes a source's presented arguments unrepresentative.

Also cited by the steps: **bottom-up carving** — start concrete with low-level observations and let the hypothesis boundaries fall out, rather than guessing them top-down; and **numbers-as-variables** — sketch every estimate in named variables first, fill values last (criterion 7).

## The runner

Steps 7-8 write the priors and likelihoods as fenced `python` blocks inside the notes; the runner executes them and composes each cluster's posterior, so the conclusion lives in the notes and nowhere else.

1. **Run:** `python3 runner/run.py <analysis-dir>` — collects every `## Prior` and `## Likelihood` block across the notes, runs them together, prints `HC-N  prior [...]  posterior [...]` per cluster.
2. **Price an assumption:** `python3 runner/run.py <analysis-dir> --set BLOCK:var=value …`, where `BLOCK` is the note's id — e.g. `--set HC-2:p_pre50_sound=0.6`, `--set E-14:t_dates=0.9`. Overriding a named variable and re-running is how steps 9-10 show what the answer hangs on, with nothing to re-synchronise.
3. **Contract** (full detail in the step 7/8 mode files): step 8 calls `prior(hc, w)` once per cluster — `w` = relative weights in `HC.hypotheses` order; step 7 calls `evidence(hc, obs, lik, t)` once per (cluster, correlated group) — `lik[i]` = P(all named obs | member i), `t` = reliability. Composition: `lik_eff[i] = t·lik[i] + (1−t)·Σⱼ p[j]·lik[j]`, then `posterior ∝ p[i]·Π lik_eff[i]`, normalised. Blocks are arithmetic over named variables only — the runner rejects `import`/`open`/`eval`/`exec`/dunders and injects no I/O, so runs are deterministic (criterion 14).
4. **Self-check:** `python3 runner/test_run.py` checks the runner against every number in the step 7/8 examples; run it after editing `run.py`.
