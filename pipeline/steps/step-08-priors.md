# Step 8 — Estimate priors

This file is your full instruction set for step 8. Steps 1-7 have already run on the analysis directory: the graph holds sources, observations, hypotheses grouped into mutually-exclusive `hypothesis-cluster` (`HC`) nodes, observation→cluster evidence-link (`E`) edges, and a step-7 likelihood block on each edge. Your job: price each cluster's members *before its evidence is read*, by writing one prior block into that cluster's own note.

## Spec

**Orientation.** For each `HC`, write one fenced `python` block — a Fermi decomposition per member (named quantities, each carrying the reason it holds that value, multiplied into one relative weight) ending in a single `prior(hc, w)` call that registers the weights. Step 7 has already registered each cluster's likelihoods and owns the composition, so once your priors are in, a cluster's whole conclusion recomputes from its notes and nothing else. The arithmetic is trivial and is not the point; the point is that every number is named, argued right beside itself, and overridable — so a skeptic can substitute their own value and re-run (criterion 7).

**Boundary — the prior must not have seen this cluster's evidence.** No weight may condition on any observation that step 5 linked into this cluster (i.e. any observation sitting on an `E` edge whose target is this `HC`). That evidence enters exactly once, at step 7; a prior that has already absorbed it double-counts, and no later step can unpick which half is which (criterion 3). Background facts that sit on no edge into this cluster are legitimate prior inputs.

### Artifact

One fenced `python` block under a `## Prior` heading in the cluster's own `HC` note. That heading — plus an OPTIONAL `external_consensus` line on the `HC` node — is all step 8 owns: no new node type, no new prefix, no generated file, no index, and **no derived number in frontmatter**. A cached weight vector goes stale silently and announces nothing when it does, so the block stays the sole copy; the runner recomputes from it every run.

`external_consensus`: one optional line recording what the field currently believes, for steps 9-10 to set beside this analysis. It enters no expression, the block never reads it, and it is written *after* your weights are fixed, or not at all — written first it is anchoring with a label on (criterion 15).

The block makes exactly one call: `prior(hc, w)`, where `hc` is this cluster's id string (e.g. `"HC-2"`) and `w` is the list of relative weights in `HC.hypotheses` order (see rule 2). The runner injects `prior`; the block itself is pure arithmetic over named variables — no import, file, network, clock, RNG or LLM, so the same notes always give the same numbers (criterion 14).

### Rules

1. **Every number is a named variable with a reason** (MUST). No estimated quantity appears as a bare literal inside an expression; arithmetic identities like `1 - p_x` are not estimates and need none. The reason sits on that line or the one above and says what would have to be true for the value to be right — not merely what the variable is already named.
2. **One weight expression per member, in `HC.hypotheses` order** (MUST). `HC.hypotheses` is the cluster's ordered list of member hypotheses, fixed at step 4 (ascending id, the residual last); it is the vector index everything downstream uses. Each member's segment opens with prose: what would have to be true for this member, what reference class or basis its factors come from, what the estimate does not cover, and how confident you are relative to the other members. Step 9's cluster review reads exactly this prose — it is what a bare vector cannot hold.
3. **Weights are relative** (MUST) — odds, not probabilities. `prior()` normalises within the cluster, so nothing has to sum to anything and no expression divides by a total. Do not import another cluster's member probability: priors are per-cluster (step 4 recorded, in each cluster's `independence` line, why its prior factorizes from the other clusters'). Where step 4 flagged a residual cross-cluster dependence in `depends_on`, treat it as an approximation noted in the member's prose, not something to repair here.
4. **The residual gets its own argued weight** (MUST), never `1 - sum(others)` or any function of the other members. The residual is step 4's catch-all member (`residual: true`, always last in `hypotheses`) — "the answer is something not listed here." A complement is a rescaling artifact, not an estimate, and hides both failure modes at once: too small and no evidence can ever lift it, too large and it soaks up every posterior. Its comment says what an unmodelled answer would concretely look like. A cluster marked `exhaustive_by_construction: true` at step 4 (its members logically cover the space) carries no residual, and this rule does not apply to it.
5. **Arguments in, linked observations out** (MUST). Each active member hypothesis carries an `arguments` list (written at step 5) — the standalone arguments bearing on that member's prior independently of any single observation. Open those argument notes; use the ones step 6 marked `approved` or `corrected` (for a corrected one, its edited `statement`), ignore any marked `rejected`, and say in the affected number's comment where an argument moved it (SHOULD). An argument enters as reasoning you read while choosing a number, never as a multiplicative term of its own — that would double-count a strength step 6 deliberately did not score. No counterfactual value is owed and there is no per-argument field.
6. **Two frameworks for one number is a mixture written inline** (MAY): `c_chain = 0.7  # credence the mechanistic model beats the empirical one` then `p = c_chain * p_theory + (1 - c_chain) * p_empirical`. That is the whole of the support it needs — no field, no switch. There is no per-cluster "my decomposition might be wrong" scalar: out-of-model mass is the residual member's job, where it also carries a likelihood and competes in the posterior visibly (criterion 2).

### Micro-example

Cluster `HC-2` — "When did first human occupation of Sahul begin?", members in id order: `H-8` (before 50 ka) · `H-19` (50-45 ka) · `H-52` (residual). **Numbers illustrative and uncalibrated.**

```python
# HC-2 prior — when did first human occupation of Sahul begin? Members in HC-2.hypotheses order.
# H-8, before 50 ka. True if the oldest luminescence horizons date occupation and not reworked
# sediment; priced off continental first-arrival dates, which have moved older more often than
# younger since 1990. Not covered: whether onset was a single event at all. Weakest of the three.
p_pre50_sound = 0.35       # 1 of the 3 published pre-50 ka horizons survived independent re-dating
width_pre50_kyr = 10.0     # 60-50 ka; a flat-in-time colonisation prior gives mass by window width
w_early = p_pre50_sound * width_pre50_kyr
# H-19, 50-45 ka. True if the dense cluster of accepted ages is the arrival signal rather than
# where the dating methods happen to overlap best. Same reference class; site sampling not covered.
p_window_sound = 0.80      # three independent dating methods agree across this window
width_window_kyr = 5.0     # 50-45 ka
w_window = p_window_sound * width_window_kyr
# H-52, residual. Occupation after 45 ka, or a run of failed landfalls with no single onset — an
# unmodelled answer here is a shape the other two cannot express, not merely a later date.
p_post45_live = 0.08       # no accepted horizon after 45 ka, but the claim is not closed either
width_post45_kyr = 3.0     # 45-42 ka, the youngest window anyone still argues for
p_no_single_onset = 0.10   # multi-founder colonisations are common elsewhere; one window's worth of mass, not the leftover
w_residual = p_post45_live * width_post45_kyr + p_no_single_onset * width_window_kyr
prior("HC-2", [w_early, w_window, w_residual])
```

Weights `[3.5, 4.0, 0.74]` → prior `[0.4248, 0.4854, 0.0898]`. Overriding `p_pre50_sound` to 0.6 and re-running gives `[0.5587, 0.3724, 0.0689]` — the entire cost of pricing that assumption, with no edit to the note and nothing to re-synchronise.

### Checks (binary)

1. Every active `HC` has exactly one `## Prior` block, calling `prior()` once with its own id and a list of length `len(HC.hypotheses)` in that order; no other node type carries one.
2. All blocks run together without error and re-run identically; every member's weight is finite and strictly positive, and every normalised prior sums to 1.
3. No estimated number appears as a bare literal inside an expression, and every number assigned carries a reason comment on or above its line.
4. Each member's segment opens with the prose of rule 2, and the residual's expression names only its own variables — no `1 -`, no `sum(`, no reference to another member's weight.
5. No frontmatter field anywhere holds a prior, weight, odds value or probability. Spot-check each cluster's variables against its inbound `E` edges: none restates or conditions on one of those observations.

### Interface

**Consumes.** From step 4, per cluster: `HC.hypotheses` (the member order and the normalisation set), whether it has a residual member or is `exhaustive_by_construction`, its `exclusivity` / `independence` lines (why comparing and normalising within the cluster is meaningful), any `depends_on` note, and each member's `statement`. From step 5: the `arguments` list on each active member. From step 6: each of those arguments' `status`, to include (`approved` / `corrected`) or drop (`rejected`) it. Reads no observation on an edge into this cluster, and no `trust_score` — data-reliability is step 7's concern. `merged_from` on a hypothesis counts absorbed papers, not evidence — never read it as prior weight.

**Produces.** For step 7: one registered prior vector per cluster in `HC.hypotheses` order (step 7 registers the likelihoods, owns the composition, and consumes this vector). For steps 9-10: the per-member prose, the named variables and their values (quoted, not re-derived), plus `external_consensus`, labelled as external and mixed into no number.

## Process

The block is short arithmetic; the real work is choosing weights you would bet on and arguing each one where it sits. A workable order:

1. **Frame each cluster before writing any value.** Open the `HC` note: read the sub-question, the members in `hypotheses` order, the residual / `exhaustive_by_construction` status, and the `exclusivity` / `independence` / `depends_on` lines. Lay out the members as named weight variables with the reasoning written but the numbers still blank; decide the decomposition first and fill values last. This stops you from picking a gut probability and back-filling justification for it.
2. **Take the outside view first, then adjust.** For each member ask: across the broadest class of comparable cases, how often does something like this hold? Name that reference class in the prose and start from its base rate, then adjust for what is specific to this case, keeping the adjustment visible as its own factor. Base-rate / reference-class reasoning is the main defence against the overconfidence that comes from reasoning only from the specifics in front of you.
3. **Fermi-decompose the members with moving parts.** Rather than one gut number, split a weight into factors you can each judge better — e.g. P(the dating method is sound) × (window width), as in the example — and give each factor its own base rate and reason. Stop decomposing once a factor is something you can estimate directly and defend; over-decomposition just multiplies noisy guesses.
4. **Guard the boundary — this is the step's most damaging error.** A linked observation that leaks into a prior gets counted a second time at step 7 and silently manufactures confidence. Before finalising a weight, look at the cluster's inbound `E` edges and confirm no factor restates or conditions on one of those observations. Facts that sit on no edge into this cluster are fair game.
5. **Fold in the arguments and price the residual concretely.** Read each member's `approved` / `corrected` arguments as reasoning while you choose its number, noting in the comment where one moved it. For the residual, picture what an answer nobody modelled would actually look like and weight it by how often the listed members miss the truth in questions like this — not by whatever is left over. Too small and no evidence can raise it; too large and it eats every posterior. This is where out-of-model and unknown-unknown mass lives (criterion 2), so resist sanding it to zero.
6. **Calibrate: would you bet at these odds?** Read the normalised prior and sanity-check it as a bet. Watch for the standard failures: base-rate neglect, overconfidence (extreme weights on thin grounds), and anchoring on the current consensus — which is exactly why `external_consensus`, if you record it at all, is written only after your weights are fixed.
7. **Run and verify.** Run the runner over the analysis directory (path shown relative to the vault root): `python3 .claude/skills/flf-epistack/runner/run.py <analysis-dir>`. It prints `HC-N  prior [...]  posterior [...]` per cluster and fails loudly on a non-positive weight, a wrong-length vector, or a banned token. Re-run to confirm identical output, then price one assumption with `--set HC-N:var=value` to confirm the variable is genuinely load-bearing and named as you intended; if a small override swings the answer a lot, that variable is a driver worth flagging in the prose for steps 9-10.
