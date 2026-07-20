---
title: "Step 7 — Estimate priors"
---

# Step 7 — Estimate priors

This file is your full instruction set for step 7. Steps 1-6 have already run on the analysis directory: the graph holds sources, observations, hypotheses grouped into mutually-exclusive `hypothesis-cluster` (`HC`) nodes, observation→cluster evidence-link (`E`) edges, and arguments attached to hypotheses and observations. Your job: price the members of the cluster(s) you're handed, by writing one prior block into each such cluster's own note.

## Spec

**Orientation.** For each `HC`, write one fenced `python` block — a Fermi decomposition per member (named quantities, each carrying the reason it holds that value, multiplied into one relative weight) ending in a single `prior(hc, w)` call that registers the weights. Step 8 registers each cluster's likelihoods and owns the composition; once your priors are in and those likelihoods follow, a cluster's whole conclusion recomputes from its notes and nothing else. The arithmetic is trivial and is not the point; the point is that every number is named, argued right beside itself, and overridable — so a skeptic can substitute their own value and re-run.

**The split — you choose which evidence the prior rests on, then mark it.** The prior is not evidence-blind. Look over every evidence-link into this cluster **and** its no-observation arguments (`no_observation_arguments.py <analysis-dir> --cluster HC-N`). Some of those observations are outside-view / base-rate facts a well-formed prior should already rest on — a reference-class rate, a general uncontested fact; use them here, and set `used_for_prior: true` on each such `E` edge's frontmatter. Step 8's to-do set (`batch_likelihoods.py`) then drops every marked edge and prices only the rest, so each datum counts exactly once: the base-rate facts in the prior, the case-specific discriminating observations in the likelihoods. The marking **is** the partition between the two steps — mark nothing case-specific and you double-count; mark something discriminating and you silently drop live evidence. The no-observation arguments are consulted here and nowhere else — step 8 never sees them.

### Artifact

One fenced `python` block under a `## Prior` heading in the cluster's own `HC` note. Beyond that block, step 7 writes exactly one thing into the graph: `used_for_prior: true` on the frontmatter of each `E` edge whose datum it used (rule 5). No new node type, no new prefix, no generated file, no index, and **no derived number in frontmatter** — a cached weight vector goes stale silently and announces nothing when it does, so the block stays the sole copy; the runner recomputes from it every run.

The block makes exactly one call: `prior(hc, w)`, where `hc` is this cluster's id string (e.g. `"HC-2"`) and `w` is the list of relative weights in `HC.hypotheses` order (see rule 2). The runner injects `prior`; the block itself is pure arithmetic over named variables — no import, file, network, clock, RNG or LLM, so the same notes always give the same numbers. A fact you looked up (rule 8) enters as an ordinary named variable with a source comment, so determinism still holds.

### Rules

1. **Every number is a named variable with a reason** (MUST). No estimated quantity appears as a bare literal inside an expression; arithmetic identities like `1 - p_x` are not estimates and need none. The reason sits on that line or the one above and says what would have to be true for the value to be right — not merely what the variable is already named.
2. **One weight expression per member, in `HC.hypotheses` order** (MUST). `HC.hypotheses` is the cluster's ordered list of member hypotheses, fixed at step 4 (ascending id, the residual last); it is the vector index everything downstream uses. Each member's segment opens with prose: what would have to be true for this member, what reference class or basis its factors come from, what the estimate does not cover, and how confident you are relative to the other members. Step 9's cluster review reads exactly this prose — it is what a bare vector cannot hold.
3. **Weights are relative** (MUST) — odds, not probabilities. `prior()` normalises within the cluster, so nothing has to sum to anything and no expression divides by a total; the overall scale is free. Price each member either by decomposing it into factors (rule 7, process 3) or by anchoring one member's weight at 1 and giving the others as odds against it. Do not import another cluster's member probability: priors are per-cluster (step 4 recorded, in each cluster's `independence` line, why its prior factorizes from the other clusters'). Where step 4 flagged a residual cross-cluster dependence in `depends_on`, treat it as an approximation noted in the member's prose, not something to repair here.
4. **The residual gets its own argued weight** (MUST), never `1 - sum(others)` or any function of the other members. The residual is step 4's catch-all member (`residual: true`, always last in `hypotheses`) — "the answer is something not listed here." A complement is a rescaling artifact, not an estimate, and hides both failure modes at once: too small and no evidence can ever lift it, too large and it soaks up every posterior. Its comment says what an unmodelled answer would concretely look like. A cluster marked `exhaustive_by_construction: true` at step 4 (its members logically cover the space) carries no residual, and this rule does not apply to it.
5. **Choose the prior's evidence and mark it `used_for_prior`** (MUST). Run `no_observation_arguments.py <analysis-dir> --cluster HC-N` and look over the cluster's inbound `E` edges. Select the edges carrying outside-view / base-rate information the prior should rest on — a reference-class rate, a general fact — use them in your Fermi, and set `used_for_prior: true` on each such edge's frontmatter (a manual edit on the `E` node). Step 8 then skips them (`batch_likelihoods.py`), so the datum counts once; leave every case-specific, discriminating observation unmarked for step 8. **Correlation groups mark all-or-none**: if an edge you use belongs to a `CG`, mark every member edge of that group (or none), because `batch_likelihoods.py` excludes the whole group when any member is marked. This is the only frontmatter step 7 writes.
6. **Arguments enter as reasoning, not as a term** (SHOULD). The cluster's no-observation arguments reach it via `affects_hypotheses` → a member `H` (which is how `no_observation_arguments.py` finds them); they carry no observation of their own. Read the ones step 6 marked `approved` or `corrected` (for a corrected one, its edited `statement`), ignore any `rejected`, and say in the affected number's comment where an argument moved it. An argument enters as reasoning you weigh while choosing a number, never as a multiplicative term of its own — that would double-count a strength step 6 deliberately did not score. No counterfactual value is owed and there is no per-argument field.
7. **Two frameworks for one number is a mixture written inline** (MAY): `c_chain = 0.7  # credence the mechanistic model beats the empirical one` then `p = c_chain * p_theory + (1 - c_chain) * p_empirical`. That is the whole of the support it needs — no field, no switch. There is no per-cluster "my decomposition might be wrong" scalar: out-of-model mass is the residual member's job, where it also carries a likelihood and competes in the posterior visibly.
8. **Look a missing fact up** (MAY). If a Fermi factor needs a specific fact you lack — a base rate, a constant, a population — a quick `WebSearch` is fine. The value enters the block as a named variable with a source comment (`# <value>, per <source> <date>`); it is then a fixed number like any other, so determinism holds. A fact already in the graph as an observation belongs in rule 5 instead — mark its edge; only look up facts that are not already nodes.

### Micro-example

Cluster `HC-1` — "Dominant driver of the megafauna extinction pulse" (the cluster step 8 prices likelihoods for), members in id order: `H-3` (direct predation) · `H-11` (indirect human impact) · `H-21` (climate aridification) · `H-42` (residual). This step consulted the cluster's no-observation arguments (here `A-3`) and its inbound `E` edges, pulled one base-rate observation into the prior — marking its edge `used_for_prior: true` — and left the continent's own dated record for step 8. **Numbers illustrative and uncalibrated.**

```python
# HC-1 prior — dominant driver of the megafauna extinction pulse. Members in HC-1.hypotheses order:
# [H-3 direct predation, H-11 indirect human impact, H-21 climate aridification, H-42 residual].
# Inputs: the outside view across other Late-Quaternary pulses, one base-rate observation this step pulled
# into the prior (E-9, now marked used_for_prior: true, so step 8 skips it), and the cluster's no-observation
# arguments from `no_observation_arguments.py <analysis-dir> --cluster HC-1` (here A-3). This continent's own
# dated record (E-14, E-22) is left unmarked — it discriminates, and is priced at step 8.

# H-21 climate aridification — the anchor. Across comparable well-studied pulses, climate and a human
# driver are named the dominant cause at broadly similar rates, so take climate as the unit weight.
w_climate = 1.0

# Human driver (predation + indirect) as odds vs climate. O-9 is a meta-analysis of comparable
# Late-Quaternary pulses (evidence-link E-9): a human driver is named the dominant cause ~2× as often as
# climate. That is a base rate, not this pulse's own record, so it belongs in the prior — E-9 is marked
# used_for_prior: true and will not be re-counted at step 8.
base_human_vs_climate = 2.2   # E-9: human driver named dominant ~2× as often as climate across comparable pulses
w_human = base_human_vs_climate * w_climate

# Split the human mass into H-3 direct predation vs H-11 indirect impact. No-observation argument A-3
# (approved, reached via affects_hypotheses -> H-11, rule 6): across comparable settings the dominant human
# mechanism is more often indirect (habitat change, fire, competition) than the direct kill route, so
# indirect takes the larger share.
share_indirect = 0.65         # indirect : direct ~ 0.65 : 0.35 within the human driver
w_predation = w_human * (1 - share_indirect)   # H-3
w_indirect  = w_human * share_indirect          # H-11

# H-42 residual — the driver is something the three listed members cannot express (hyperdisease, a bolide).
# Weighted by how often, in comparable pulses, the eventual dominant cause fell outside a menu like this —
# uncommon but real. Its own argued weight, not a leftover (rule 4).
w_residual = 0.36             # ~0.36 : 1 vs climate; ~10% of the mass once normalised

prior("HC-1", [w_predation, w_indirect, w_climate, w_residual])
```

The four `w_*` weights `[0.77, 1.43, 1.0, 0.36]` normalise to ≈ `[0.22, 0.40, 0.28, 0.10]` — the vector step 8's micro-example uses as HC-1's stand-in. Overriding `base_human_vs_climate` to `1.0` (pricing the human driver and climate as equally likely a priori) and re-running shifts ~19 points off the human drivers, most of it onto climate — the entire cost of pricing that assumption, with no edit to the note and nothing to re-synchronise.

### Checks (binary)

1. Every active `HC` has exactly one `## Prior` block, calling `prior()` once with its own id and a list of length `len(HC.hypotheses)` in that order; no other node type carries one.
2. All blocks run together without error and re-run identically; every member's weight is finite and strictly positive, and every normalised prior sums to 1.
3. No estimated number appears as a bare literal inside an expression, and every number assigned carries a reason comment on or above its line; a looked-up value (rule 8) names its source.
4. Each member's segment opens with the prose of rule 2, and the residual's expression names only its own variables — no `1 -`, no `sum(`, no reference to another member's weight.
5. Every `E` edge whose datum entered a prior Fermi carries `used_for_prior: true`, and every edge so marked is one a prior actually used — no orphan marks; a marked edge in a correlation group has all its sibling members marked too. No frontmatter field anywhere holds a prior, weight, odds value or probability.

### Interface

**Consumes.** From step 4, per cluster: `HC.hypotheses` (the member order and the normalisation set), whether it has a residual member or is `exhaustive_by_construction`, its `exclusivity` / `independence` lines (why comparing and normalising within the cluster is meaningful), any `depends_on` note, and each member's `statement`. From step 5: the cluster's inbound `E` edges (their observations, and any `CG` grouping) — the ones you price into the prior you mark `used_for_prior: true`, the rest you leave for step 8. From `no_observation_arguments.py`: the cluster's no-observation arguments, each with its step-6 `status` (include `approved` / `corrected`, drop `rejected`). Reads no `trust_score` — data-reliability is step 8's concern. `merged_from` on a hypothesis counts absorbed papers, not evidence — never read it as prior weight.

**Produces.** For the cluster's probabilistic model — this is the prior half, composed by the runner with step 8's likelihood blocks into the posterior: one registered prior vector per cluster in `HC.hypotheses` order. Into the graph: `used_for_prior: true` on each edge the prior used, which partitions the evidence so step 8 prices the remainder. For steps 9-10: the per-member prose, and the named variables and their values (quoted, not re-derived).

## Process

The block is short arithmetic; the real work is choosing weights you would bet on and arguing each one where it sits. A workable order:

1. **Frame each cluster before writing any value.** Open the `HC` note: read the sub-question, the members in `hypotheses` order, the residual / `exhaustive_by_construction` status, and the `exclusivity` / `independence` / `depends_on` lines. Lay out the members as named weight variables with the reasoning written but the numbers still blank; decide the decomposition first and fill values last. This stops you from picking a gut probability and back-filling justification for it.
2. **Take the outside view first, then adjust.** For each member ask: across the broadest class of comparable cases, how often does something like this hold? Name that reference class in the prose and start from its base rate, then adjust for what is specific to this case, keeping the adjustment visible as its own factor. Base-rate / reference-class reasoning is the main defence against the overconfidence that comes from reasoning only from the specifics in front of you.
3. **Fermi-decompose the members with moving parts.** Rather than one gut number, split a weight into factors you can each judge better — e.g. P(the dating method is sound) × (window width) — and give each factor its own base rate and reason. Stop decomposing once a factor is something you can estimate directly and defend; over-decomposition just multiplies noisy guesses.
4. **Select the prior's evidence and mark it — the step's most consequential call.** Run `no_observation_arguments.py <analysis-dir> --cluster HC-N` and scan the cluster's inbound `E` edges. Pull in the outside-view / base-rate observations a sound prior should rest on, and set `used_for_prior: true` on each edge you use (all-or-none across a correlation group). Leave the case-specific, discriminating observations for step 8. Get the partition wrong in either direction and it costs: a discriminating observation left in the prior is counted again at step 8 and manufactures confidence; a base rate you forget to mark is dropped from the prior and re-enters step 8 as if it discriminated. If a Fermi factor needs a fact that is not in the graph at all, look it up (rule 8) and drop the sourced value straight into the block.
5. **Fold in the arguments and price the residual concretely.** Read each no-observation argument the helper returned that step 6 marked `approved` / `corrected` as reasoning while you choose a number, noting in the comment where one moved it. For the residual, picture what an answer nobody modelled would actually look like and weight it by how often the listed members miss the truth in questions like this — not by whatever is left over. Too small and no evidence can raise it; too large and it eats every posterior. This is where out-of-model and unknown-unknown mass lives, so resist sanding it to zero.
6. **Calibrate: would you bet at these odds?** Read the normalised prior and sanity-check it as a bet. Watch for the standard failures: base-rate neglect, overconfidence (extreme weights on thin grounds), and anchoring on the current consensus — so fix your weights before you look up what the field currently believes, not after.
7. **Run and verify.** Run the runner over the analysis directory (path shown relative to the vault root): `python3 .claude/skills/flf-epistack/runner/run.py <analysis-dir>`. Step 8's likelihoods don't exist yet, so each cluster's posterior comes back equal to its prior — which is exactly what to check here. It prints `HC-N  prior [...]  posterior [...]` per cluster and fails loudly on a non-positive weight, a wrong-length vector, or a banned token. Re-run to confirm identical output, then price one assumption with `--set HC-N:var=value` to confirm the variable is genuinely load-bearing and named as you intended; if a small override swings the prior a lot, that variable is a driver worth flagging in the prose for steps 9-10.
