# Step 6 — Assess argument validity

An **argument** carries no information of its own: it is a universally-valid logical/mathematical validity (theorem or inference schema). Being universally valid, it bears on our world only through what it attaches to — it MUST attach to ≥1 `affects_observations` and/or `affects_hypotheses`, and **most arguments attach to an observation**. An argument attaching only to a hypothesis (no observation) is rare — mainly math / theoretical-physics reasoning.

Step 6 judges whether each argument's **inference actually holds** and tags it `approved` / `corrected` / `rejected`. It assesses **every** argument — both those attaching to an observation (`affects_observations`) and those attaching only to a hypothesis (`affects_hypotheses`). It mints no nodes and renames nothing; it only adds validity fields, editing a `corrected` argument's `statement` in place.

Validity is judged **on the argument's own merits, conditional on its premises**: assume the premises, ask whether the conclusion follows — independent of whether the premises or the conclusion are actually *true*. Their truth is priced later, as a likelihood (step 8) or prior (step 7); mixing it in here double-counts.

Step 6 runs as children over batches of ~20 arguments; the orchestrator batches every argument with `scripts/batch_arguments.py <analysis-dir>` and briefs each child with the rest of this file (see `steps/step-00-orchestrate.md`).

## Relevant context

You read `argument` (`A`, step 3) nodes and write the two validity fields:

| field | set by | meaning |
|---|---|---|
| statement | step 3 | the one-line inferential claim; you edit it only on a `corrected` argument |
| reasoning (body) | step 3 | the inferential content / calculation — the whole input to your judgment; you expand it to record your verdict's reasoning |
| affects_observations / affects_hypotheses | step 3 | what the argument attaches to (≥1 non-empty); you don't change these, but they tell you what it feeds — step 8 for a with-observation argument, step 7 for a no-observation one |

## Interface

**Consumes** — from step 3: `statement`, the `reasoning` body, and the attachments `affects_observations` / `affects_hypotheses`. Source features (via `source`) inform only a `trusted` validity verdict.

**Owns** — `status` / `reason_if_not_false` on `A` nodes; edits `statement` on `corrected` arguments (never the filename); records each verdict's reasoning in the body. Touches nothing else.

**Feeds step 8 (likelihoods)** — each **with-observation** argument's `status` (include `approved`/`corrected`, exclude `rejected`) and its clarified `reasoning` body, read while pricing the observation it rides on. The clearer the body, the better step 8 can judge what probability to assign.

**Feeds step 7 (priors)** — each **no-observation** argument (empty `affects_observations`, attaching only via `affects_hypotheses`) contributes its `status` and clarified body, which step 7 consults when Fermi-estimating that hypothesis-cluster's prior.

**Feeds step 9** — `reason_if_not_false` flags which accepted arguments rest on unchecked `trusted` reasoning; it is an audit signal for the cluster review, not an input to any number.

## Spec

Write onto each argument in your batch:

| field | req | meaning |
|---|---|---|
| status | MUST | `approved` = the inference holds as stated. `corrected` = it holds only in a weaker/adjusted form. `rejected` = the inference does not hold |
| reason_if_not_false | MUST unless `rejected` | `checked` = you traced the load-bearing step yourself (skimming ≠ checked). `trusted` = tracing it is infeasible at reasonable cost (long derivation, specialist formalism), so validity is trusted from the source |

A **`corrected`** argument is fixed in place: edit `statement` to the version that does hold, and preserve the pre-edit text under a `## Original` heading in the body — so downstream reads the corrected claim directly. **Never edit the filename**, even when the correction makes it read wrong: it is the link target every other node reaches this argument by. A filename that no longer matches the corrected `statement` is the expected end state; `## Original` plus the edited `statement` carries the true story.

Record your verdict's reasoning in the `reasoning` body as you go — the traced steps behind a `checked` verdict, the specific failure behind a `rejected` one, or why a direct check wasn't feasible and what makes the source credible for a `trusted` one. This body is what step 9 audits and what makes a `trusted` call defensible; a bare status with no trace is the main thing to avoid.

### Rules

1. **`status` is about whether the inferential step is real, not how strong the argument is.** A valid-but-weak argument is still `approved`; how much it moves a number is steps 7-8's job (keeping these apart prevents double-counting strength).
2. **`checked` vs `trusted` is judged from the `reasoning` body**, and length alone isn't the trigger — a long but elementary chain is `checked`. Take `trusted` only where tracing the load-bearing step is genuinely infeasible.
3. **A `checked` verdict is author-blind** — it rests on the reasoning, never on author, venue, or citation count; source identity may inform only a `trusted` verdict.
4. **`rejected` arguments are kept, not deleted** — their links stay intact. "This step doesn't go through" is a result; downstream simply excludes them.

### Micro-example

Main question "What drove the extinction of Sahul's megafauna around 45-40 ka?".
1. **`corrected`.** `A-101` "continental synchrony of the pulse with first arrival *favours* a human driver" → `status: corrected`, `reason_if_not_false: checked`. `statement` edited to "…synchrony is *evidence for* a human driver over a climate driver"; the filename still reads "…favours a human driver" and is left as-is; `## Original` keeps the as-stated claim; body: "as stated the implication fails — a climate excursion that also tracks the arrival interval reproduces the synchrony; the evidential version goes through."
2. **`approved` + `trusted`.** `A-118` "the OSL age model's systematic uncertainty keeps first occupation within ±2 kyr" → `status: approved`, `reason_if_not_false: trusted`. Body: "multi-page quantitative derivation, not traceable quickly; independently redone by a second lab, no published refutation."
3. **`rejected`.** `A-14` "no butchery site is known for 11 of the 12 genera, so humans did not drive the extinction" → `status: rejected` (no `reason_if_not_false`). Body: "needs an unstated premise that butchery sites would preserve and be discovered at a detectable rate; without it the conclusion doesn't follow — a validity failure, independent of whether that premise is true."

### Checks (binary)

1. Every argument in your batch has `status` ∈ {approved, corrected, rejected}, and every non-`rejected` one also has `reason_if_not_false` ∈ {checked, trusted}.
2. Every `corrected` argument's `statement` reflects the corrected claim and preserves the pre-edit text under `## Original`; no argument's filename differs from its step-3 filename.
3. Every argument carries a body trace for its verdict; spot-check 3 `checked` arguments — none rests on author, venue, or citation count.
4. No argument was moved, deleted, or renamed; no argument outside your batch was touched; `affects_observations` / `affects_hypotheses` are unchanged.

## Process

The reliable method is *reconstruct, then evaluate*, kept apart — most bad verdicts come from judging an argument you never actually pinned down.

1. **Reconstruct.** State the premises and the conclusion explicitly, then name the single inferential step that carries the argument. Real arguments are usually enthymemes — a load-bearing premise is left implicit — so the core move is surfacing that hidden premise. Reconstruct it in its strongest reasonable form (the principle of charity), but stop short of *completion by force*: if the only premise that rescues the argument is one no one would grant, or one so strong it does all the work itself, that is a fault in the argument, not a licence to invent.
2. **Evaluate the step, conditional on the premises.** Assume the premises true and ask whether the conclusion follows. The productive probe is the *undercutting defeater* — an alternative that breaks the link between reason and conclusion without denying the premises (e.g. "the synchrony is equally explained by a climate excursion that also tracks the arrival interval"). No such defeater survives → `approved`. One survives but a weaker conclusion is immune to it → `corrected` to that weaker form; in practice this is the most common outcome — a "proves / refutes" claim that only really supports an "is evidence for". The step needs a premise that fails completion-by-force → `rejected`.
3. **Keep validity separate from truth.** You are not asking whether the conclusion is true, or whether a premise is factually right — a premise's truth is priced as a likelihood or prior in steps 7-8. Reject only when the *inference* fails; an argument with a false premise but a sound step is still `approved`.
4. **`checked` vs `trusted`.** Trace the load-bearing step yourself and mark `checked` whenever that is feasible — this is the default, and it must not lean on who wrote the paper. Reserve `trusted` for steps whose verification is genuinely out of reach at reasonable cost (specialist formalism, a multi-page derivation); there, say in the body why a direct check wasn't feasible and what makes the source credible (independent replication, no published refutation). `trusted` is a cost concession, not deference — keep it rare.
