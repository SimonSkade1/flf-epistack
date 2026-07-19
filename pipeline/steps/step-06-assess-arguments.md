# Step 6 — Assess argument validity

Every `argument` node (`A-N`) was created in step 3 by extracting a paper's reasoning: a one-line `statement` (the inferential claim), a `reasoning` prose body, a single `source` (`[[S-N]]`, the paper it came from) and a `locator` (where in that paper). Step 5 then attached each argument to the hypotheses it bears on and set `link_state: linked`; arguments that attached to nothing were moved to `arguments/orphan/`.

Step 6 turns that raw argument layer into a **deduplicated, validity-assessed** one, in two phases:

1. **Merge** near-duplicate arguments so one argument = one node, however many papers restate it.
2. **Assess** each survivor's validity — does the *inference* actually hold — tagging it `approved` / `corrected` / `rejected`.

Step 6 creates no new nodes and deletes nothing; it adds fields, edits a few, and moves absorbed duplicates aside.

## Spec

**Assessment set** = the arguments that get both phases: `link_state: linked` arguments that are not tombstones — i.e. everything in `arguments/` except `arguments/orphan/` (unlinked, from step 5) and `arguments/merged/` (tombstones, created below). Orphans are skipped entirely: they attach to nothing, so merging or assessing them would be wasted budget.

Validity is judged **on the argument's own merits, conditional on its premises**: assume the premises, ask whether the conclusion follows — independent of whether the premises or the conclusion are actually *true* (their truth is priced later, in steps 7-8). This is criterion 4 (trust separated from truth) applied to reasoning.

SHOULD produce `validity.base` — an Obsidian Base over `arguments/`, one row per assessed argument (`id`, `status`, `reason_if_not_false`, `merged_from`) plus counts per value, so a reader sees at a glance how much of the analysis rests on `trusted` (unchecked) reasoning.

### Phase 1 — merge

Follows the shared merge-bookkeeping convention (survivor = lowest id in the merge set; absorbed nodes become tombstones and move to `arguments/merged/`), specialised to arguments:

| field | on | meaning |
|---|---|---|
| `merged_into` | tombstone | `[[A-N]]` of the survivor — **one hop, never a chain** (if the survivor is itself later absorbed, rewrite this to the final survivor). Every other field is left untouched, so the per-paper wording stays auditable. |
| `merged_from` | survivor | absorbed ids. Survivor = **lowest id** in the set (deterministic; criterion 14). |
| `source` | survivor | **never edited** — stays the survivor's own single `[[S-N]]` from step 3. |
| `additional_sources` | survivor | the *extra* sources picked up by merging (the absorbed arguments' `source` values); absent if none. What an `A` rests on = `source` + `additional_sources`. |
| `locator` | survivor | one entry per source, `["S-N: <locator>", …]`. |

Merge rules:

1. **Merge on reasoning-identity, never conclusion-identity.** Merge two arguments iff their **load-bearing inferential step is the same**. Two papers reaching the same conclusion by *different* routes are two genuinely independent arguments and must not be merged — that error deletes independent support, which is worse than the double-counting merging fixes. The clean case: paper B restates or cites paper A's argument. (Observations are *not* merged this way even when identical, because they are evidence-by-instance — two measurements of the same thing are two data points — whereas an argument is evidence-by-content, and restating it adds no validity.)
2. **Candidate set, not an all-pairs sweep.** Only compare arguments that either (a) attach to the same hypothesis or the same observation-edge (an `evidence-link`, `E-N`; see rule 4) — where duplication actually double-counts — or (b) have near-identical `statement`s. Confirm by reading both `reasoning` bodies (phase 2 reads them in depth anyway).
3. **`merged_from` counts papers, not independent endorsement.** The merge set is by construction restatements of one argument, so a `trusted` verdict (below) must not be strengthened by how many sources the survivor ended up with.
4. **Repoint references (must).** Step 5 recorded each argument's attachments in two places: every observation-edge (`evidence-link`, `E-N`) carries an `arguments[]` list whose entries name an argument id + its `role`; and every hypothesis step 4 kept active (`H-N`) carries an `arguments` list of `[[A-N]]` (this is where prior-shaping arguments live, rather than on an edge of their own). Rewrite every entry naming an absorbed id to the survivor, then collapse the duplicates that creates: two `arguments[]` entries with the same id become one (union their `role` lines); an `H.arguments` list naming the survivor twice keeps one. Without this every downstream consumer would have to resolve tombstones itself.

### Phase 2 — assess

Written onto each assessment-set survivor:

| field | req | meaning |
|---|---|---|
| `status` | must | `approved` = the inference holds as stated. `corrected` = it holds only in a weaker/adjusted form. `rejected` = the inference does not hold. |
| `reason_if_not_false` | must unless `rejected` | `checked` = the load-bearing step was actually traced (skimming ≠ checked). `trusted` = tracing it is infeasible at reasonable cost (long derivation, specialist formalism), so validity is trusted from the source. |

A **`corrected`** argument is fixed in place: edit `statement` to the version that does hold, and preserve the pre-edit text under a `## Original` heading in the body — so downstream reads the corrected claim directly, with no extra field. The **filename is never edited**, even when the correction makes it read wrong: it is the link target every other node reaches this argument by, so renaming it breaks every inbound link. A filename that no longer matches the corrected `statement` is the expected end state; `## Original` plus the edited `statement` carries the true story.

The `reasoning` body may be expanded to make the argument legible: the traced steps behind a `checked` verdict, the specific failure behind a `rejected` one, or why a direct check wasn't feasible and what makes the source credible for a `trusted` one.

Assessment rules:

5. **`status` is about whether the inferential step is real, not how strong the argument is.** A valid-but-weak argument is still `approved`; how much it moves a number is steps 7-8's job (keeping these apart prevents double-counting strength).
6. **`checked` vs `trusted` is judged from the `reasoning` body**, and length alone isn't the trigger — a long but elementary chain is `checked`. Take `trusted` only where tracing the load-bearing step is genuinely infeasible.
7. **A `checked` verdict is author-blind** — it rests on the reasoning, never on author, venue, or citation count (criterion 15); source identity may inform only a `trusted` verdict.
8. **`rejected` arguments are kept, not deleted** — their edges stay intact. "This step doesn't go through" is a result; downstream simply excludes them.

### Micro-example

Main question "What drove the extinction of Sahul's megafauna around 45–40 ka?".
1. **Merge.** `A-101` (from `S-1`) and `A-233` (from `S-14`) both argue that the continental synchrony of the extinction pulse with first human arrival favours a human driver over a climate driver, by the same step — `S-14` cites `S-1`. `A-101` survives: `merged_from: [[A-233 - …]]`, `source: [[S-1 - …]]` (unchanged), `additional_sources: [[[S-14 - …]]]`, `locator: ["S-1: §Discussion", "S-14: §4"]`. `A-233` → `merged_into: [[A-101 - …]]`, moved to `arguments/merged/`; edge `E-14`'s `arguments[]` entry for `A-233` collapses into its `A-101` entry.
2. **Not merged.** `A-140` (paleoclimate simulation) and `A-152` (charcoal/pollen record) reach the same conclusion — climate alone is insufficient — by different load-bearing steps, so they stay two independent arguments (rule 1).
3. **`corrected`.** `A-101` → `status: corrected`, `reason_if_not_false: checked`. `statement` edited to "…synchrony is *evidence for* a human driver over a climate driver"; the filename still reads "…favours a human driver" and is left as-is; `## Original` keeps the as-stated claim; body: "as stated the implication fails — a climate excursion that also tracks the arrival interval reproduces the synchrony; the evidential version goes through."
4. **`approved` + `trusted`.** `A-118` "The OSL age model's systematic uncertainty keeps first occupation within ±2 kyr" → `status: approved`, `reason_if_not_false: trusted`. Body: "multi-page quantitative derivation, not traceable quickly; independently redone by a second lab, no published refutation."
5. **`rejected`.** `A-14` "No butchery site is known for 11 of the 12 genera, so humans did not drive the extinction" → `status: rejected` (no `reason_if_not_false`). Body: "needs an unstated premise that butchery sites would preserve and be discovered at a detectable rate; without it the conclusion doesn't follow — a validity failure, independent of whether that premise is true."

### Checks (binary)

1. Every assessment-set argument has `status` ∈ {approved, corrected, rejected}, and every non-`rejected` one also has `reason_if_not_false` ∈ {checked, trusted}. Tombstones and orphans have neither.
2. Every `corrected` argument's `statement` reflects the corrected claim and preserves the pre-edit text under `## Original`. No argument's filename differs from its step-3 filename.
3. Every tombstone has `merged_into` resolving in one hop to an assessment-set member and sits in `arguments/merged/`; every survivor has `merged_from`, its original single `source` unchanged, `additional_sources` = exactly the absorbed arguments' sources (disjoint from `source`), a `locator` entry per source, and is the lowest id in its set.
4. No step-5 reference (an `E.arguments[]` entry or an `H.arguments` list) names an absorbed id; no edge and no `H.arguments` list holds the same argument id twice.
5. Spot-check 3 `checked` arguments (none rests on author, venue, or citation count) and 2 merges (both members' `reasoning` share the load-bearing step, not merely the conclusion).
6. `A` file count unchanged vs step 3; every `rejected` argument still present with its edges intact. No file renamed.

### Interface

**Consumes** — from step 3: `statement` + the `reasoning` body (the whole input to both the merge test and the `checked` path). From step 5: `link_state` (defines the assessment set) and the attachment references (`E.arguments[]` membership, `H.arguments` membership), which give the merge candidate set and are what phase 1 repoints. Source features (via `source`, plus `additional_sources` after merging) inform only the `trusted` path.

**Owns** — `status`, `reason_if_not_false`, `merged_into`, `merged_from`, `additional_sources`; edits `statement` on `corrected` arguments (never the filename) and `locator` on survivors; repoints step-5 references to survivors. Touches nothing else.

**Downstream** — an argument enters a step-7 likelihood or step-8 prior *by its status*: `approved`/`corrected` are included (corrected form for `corrected`), `rejected` excluded. It enters as **reasoning the estimator reads while choosing a number**, cited in that number's comment — never as a multiplicative term of its own, which would double-count the strength this step deliberately does not score. After phase 1 each argument appears once per estimate, so no consumer resolves a tombstone. `reason_if_not_false` is an audit signal for step 9 (which accepted arguments rest on unchecked trust), not an input to any number.

## Process

Work one hypothesis-cluster at a time: its arguments are the natural batch, and the duplication you need to catch lives among arguments bearing on the same cluster.

**Phase 1 — merge first, so you assess each argument once.**

1. For a cluster, gather the candidate set: arguments sharing an observation-edge or listed on the same hypothesis, plus any with near-identical `statement`s. Ignore everything else — do not sweep all pairs.
2. For each candidate pair, read both `reasoning` bodies and ask one question: *is the load-bearing inferential step the same?* Same step (typically B restates or cites A) → merge. Same conclusion reached by a different mechanism → leave them separate; collapsing them silently deletes independent support, the more damaging error.
3. Do the bookkeeping in full: pick the lowest id as survivor, tombstone the rest and move them to `arguments/merged/`, and repoint every step-5 reference before moving on — a half-repointed merge is worse than none.

**Phase 2 — assess each survivor.** The reliable method is *reconstruct, then evaluate*, kept apart: most bad verdicts come from judging an argument you never actually pinned down.

4. **Reconstruct.** State the premises and the conclusion explicitly, then name the single inferential step that carries the argument. Real arguments are usually enthymemes — a load-bearing premise is left implicit — so the core move is surfacing that hidden premise. Reconstruct it in its strongest reasonable form (the principle of charity), but stop short of *completion by force*: if the only premise that rescues the argument is one no one would grant, or one so strong it does all the work itself, that is a fault in the argument, not a licence to invent.
5. **Evaluate the step, conditional on the premises.** Assume the premises true and ask whether the conclusion follows. The productive probe is the *undercutting defeater* — an alternative that breaks the link between reason and conclusion without denying the premises (e.g. "the synchrony is equally explained by a climate excursion that also tracks the arrival interval"). No such defeater survives → `approved`. One survives but a weaker conclusion is immune to it → `corrected` to that weaker form; in practice this is the most common outcome — a "proves / refutes" claim that only really supports an "is evidence for". The step needs a premise that fails completion-by-force → `rejected`.
6. **Keep validity separate from truth.** You are not asking whether the conclusion is true, or whether a premise is factually right — a premise's truth is priced as a likelihood or prior in steps 7-8. Reject only when the *inference* fails; an argument with a false premise but a sound step is still `approved`.
7. **`checked` vs `trusted`.** Trace the load-bearing step yourself and mark `checked` whenever that is feasible — this is the default, and it must not lean on who wrote the paper. Reserve `trusted` for steps whose verification is genuinely out of reach at reasonable cost (specialist formalism, a multi-page derivation); there, say in the body why a direct check wasn't feasible and what makes the source credible (independent replication, no published refutation). `trusted` is a cost concession, not deference — keep it rare, since criterion 15 wants the verdict to stay derivable with author and venue stripped.
8. **Leave a trace.** Record the verdict's reasoning in the body as you go — for `corrected`, what failed and what holds; for `rejected`, the missing premise. This body is what step 9 audits and what makes a `trusted` call defensible; a bare status with no trace is the main thing to avoid.
