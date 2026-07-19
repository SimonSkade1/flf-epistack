# Step 7 — Estimate likelihoods per (cluster, observation)

One mode of the flf-epistack skill. Read `../SKILL.md` first — the KB conventions, the cross-cutting criteria (cited below by number), and **the runner** live there and are not repeated here. You run this step in place on one analysis directory.

**What step 7 does.** Step 5 built the evidence layer: for each observation that *discriminates* between a cluster's mutually-exclusive answers, it created an `evidence-link` node pointing that observation at that cluster. Step 7 prices each edge — for every cluster, and every group of observations that must be judged together, how likely those observations are under each member, P(obs | H) — written as a fenced `python` block the runner composes with step 8's prior into that cluster's posterior. Every number is a named variable with its reasoning in the comment beside it, and any number can be overridden and re-run, so what the answer hangs on gets priced rather than asserted (criteria 6, 7).

## Spec

### Inputs you read (all written by earlier steps; read-only)

1. **`evidence-link` (`E-N`), from step 5** — one node per (observation → cluster) edge, created wherever the cluster's members predict that observation differently. Fields you use: `from` (`[[O-N]]`, the observation), `to` (`[[HC-N]]`, the cluster), `correlated_with` (sibling edges into the *same* cluster whose observations rest on shared data — see rule 1), `arguments` (optional `[{id, role}]`, where `role` is one line on what the argument changes about how this observation bears on these hypotheses), and an optional `## Why this is evidence` body naming which members predict the observation which way. You append a `## Likelihood` section; step 5 owns the rest of the note.
2. **`hypothesis-cluster` (`HC-N`), from step 4** — one sub-question plus its mutually-exclusive answers. `hypotheses` = the ordered member list, ascending id with the `residual` catch-all member last; **this fixed order is the index of every likelihood vector you write**. `residual` = the "the answer is something not listed here" member. `exclusivity` = one line on why at most one member is true — it is what makes the within-cluster likelihood *ratios* meaningful.
3. **`trust_score`, from step 2** — a data-reliability weight in (0, 1] on each `source`, judging how far the *data* can be trusted, separately from whether any claim built on it is true. An observation inherits it through its `source`; resolve it live, it is never copied onto the observation node.
4. **argument `status`, from step 6** — `approved` (the inference holds), `corrected` (holds only in an adjusted form — use the corrected `statement`), or `rejected` (does not hold). Read `approved`/`corrected` arguments while choosing numbers; exclude `rejected` ones. (The `reason_if_not_false` field is an audit signal for step 9, not an input here.)

### The artifact

One fenced `python` block under a `## Likelihood` heading on the evidence-link note. The block makes one call:

`evidence(hc, obs, lik, t)` — `hc` = cluster id string (e.g. `"HC-1"`); `obs` = list of the observation ids this call covers; `lik[i]` = P(**all** of `obs` together | member i), in `HC.hypotheses` order (residual included); `t` = reliability in (0, min `trust_score` over the observations in `obs`]. The runner composes these across a cluster's edges with step 8's `prior(hc, w)` into the posterior — the composition formula and the `--set` override mechanism are in `../SKILL.md`'s runner section; step 7 owns that composition but does not re-implement it. The reading that fixes `t`: **`posterior = t·(posterior at t=1) + (1−t)·prior`** — `t` is literally how far you let this evidence carry you off the prior; at `t=0` the edge does nothing. Determinism (criterion 14): arithmetic over named variables only — no import, RNG, clock, network, filesystem or LLM.

**Where the block lives when observations are correlated.** A correlated group (rule 1) shares **one** block holding **one** `evidence()` call that names every observation in the group, placed in the group's **lowest-id** edge note; each other note in the group carries only a one-line prose pointer to it under its own `## Likelihood` heading (no field, no key — the call already names the observations it covers). An edge with no correlated siblings gets its own block covering its single observation.

### Rules

1. **Correlated observations get ONE joint estimate** — the load-bearing rule here. Step 5's `correlated_with` groups edges into a cluster whose observations trace to a shared `data-basis` node (the same dataset / instrument / compilation). One `evidence()` call covers the whole group and states P(all of them | H) *jointly*. Never one call per observation: that re-counts the same underlying data as independent, which is the standard way Bayesian aggregation manufactures false confidence (criterion 3). Treat the shared data as one witness — if it is wrong, every observation resting on it is wrong together.
2. **Every number is a named variable with a reason** — no bare numeric literal inside any expression or argument list. The comment says what would have to be true for the value, the reference class or mechanism it came from, what it does not cover, and its confidence against the sibling members; shorthand and several lines are both fine. Two competing framings for one number is a mixture written inline as ordinary arithmetic, each weight itself a named variable.
3. **The residual member gets a real, argued likelihood** like any other member, so unmodelled explanations compete in the posterior visibly (criterion 2). Being unconstrained, it usually neither strongly predicts nor forbids a given pattern — a middling value; setting it near zero asserts "no unlisted cause could produce this," which you rarely know. Add nothing else for model uncertainty here — no per-cluster uncertainty scalar, no cap on ratios, no floor tying the residual to its siblings. Structural doubt is argued in prose in step 9, where it can be read.
4. **`t` is capped by trust and argued downward**: `t ≤ min trust_score` over the observations named in the call. That cap is the ceiling; go lower for weakness in the step from raw data to the stated observation (measurement or dating error, selection/survivorship effects, an analysis pipeline you could not inspect), never higher — the data cannot be more reliable than step 2 found it.
5. **Arguments enter as reasoning, not as a factor.** Read the edge's `approved`/`corrected` arguments and the `## Why this is evidence` body to decide *which way* and *how far* the observation discriminates; name any argument that moved a number in that number's comment. No argument gets a multiplicative term of its own — that double-counts strength step 6 deliberately did not score.
6. **Nothing derived is cached.** No posterior, prior, likelihood or ratio in frontmatter, and none in prose except quoted as the output of a named run. The run is the only copy; a hand-maintained number goes stale silently and announces nothing when it does.

### Micro-example

`HC-1`, members in order `[H-3 direct predation, H-11 indirect human impact, H-21 climate aridification, H-42 residual]`, step 8's prior `[0.22, 0.40, 0.28, 0.10]`. Observations `O-14` and `O-22` both rest on the same continental age compilation `D-4`, so step 5 flagged them correlated; they get one joint block, placed here in `E-14` (the lower-id edge). *Numbers illustrative and uncalibrated.*

```python
# HC-1 — ONE joint estimate for E-14 + E-22: both observations rest on D-4 (rule 1). The
# pattern is judged whole — 8/12 genera within ~2 kyr of arrival (O-14), 3 persisting >5 kyr (O-22).
p_ages_H3 = 0.30   # fits the tight cluster; fits 3 genera surviving 5 kyr of active hunting worst.
                   # Raised from ~0.22 by A-7 (approved): repeated arrival waves widen the window
p_ages_H11 = 0.50  # a habitat squeeze is staggered by construction — most genera go with the burning
                   # front, refugial taxa persist. Only member predicting both halves of the pattern
p_ages_H21 = 0.10  # aridification predicts the ages track the aridity maximum, not the arrival
                   # window; reproducing this needs a coincidence between the two
p_ages_H42 = 0.20  # unlisted driver: unconstrained, so it neither predicts the pattern nor forbids
                   # it. Lower would assert no unlisted driver could produce it, which I don't know
t_dates = 0.55     # cap = min trust_score over {O-14, O-22} = 0.9 (both via S-1). Docked well
                   # below it: Signor-Lipps truncation and reworked specimens bias youngest ages
                   # in opposite directions, and D-4's screening protocol was never read
evidence("HC-1", ["O-14", "O-22"], [p_ages_H3, p_ages_H11, p_ages_H21, p_ages_H42], t=t_dates)
```

`E-22` then carries only a pointer under its `## Likelihood` heading, e.g. "Joint estimate with O-14 in `[[E-14 - …]]` (shared basis D-4)."

Running the analysis gives `HC-1` posterior `[0.2146, 0.5303, 0.1750, 0.0800]`. `t_dates` is doing visible work: at `t=0.9` (the cap) it is `[0.2112, 0.6132, 0.1083, 0.0673]`, at `t=1` `[0.2102, 0.6369, 0.0892, 0.0637]`, at `t=0` exactly the prior. Pricing that is one `--set` and a re-run — which is what rule 2 buys.

### Checks (binary)

1. Every evidence-link is covered by exactly one `evidence()` call; every `correlated_with` group is covered by a single call naming every observation in it (the group's other notes hold only a pointer); no observation appears in two calls for the same cluster.
2. Every `lik` has `len(HC.hypotheses)` entries in that order; every `t` ∈ (0, min `trust_score` over the observations named]; every cluster with a `prior()` block has ≥1 `evidence()` call and vice versa.
3. No bare numeric literal appears inside any expression or argument list: every vector entry and every `t` is a named variable defined in the same block, each with a non-empty reason comment; no `rejected` argument is cited in a comment as support.
4. The run is reproducible and clean: running the extracted blocks twice gives byte-identical output; no import / RNG / clock / network / filesystem call appears in any block; no posterior, prior, likelihood or ratio sits in any frontmatter field, and every such number in prose is quoted from a named run.

### Interface

1. **Consumes, read-only** — the four inputs listed above. `exclusivity` is what makes the within-cluster ratios meaningful; you touch no other cluster's numbers, since each cluster composes alone.
2. **Owns** — the `## Likelihood` section and its `evidence()` block on evidence-link notes, plus the composition into the posterior. No node type, no prefix, no frontmatter field on any node, no generated file, no index, no `.base` view. Step 8's `prior(hc, w)`, registered once per cluster in `HC.hypotheses` order, is the entire shared surface between you and it.
3. **Hands to steps 9-10** — they read your blocks and the posteriors they produce. The per-number prose is step 9's raw material for what the model may not capture; overriding a named variable and re-running is how step 10 prices a driver. Neither is owed a sensitivity number or a ranked driver list from you — naming what the answer hangs on is prose.

## Process

Work **cluster by cluster**. For each cluster, list its evidence-links (step 5 notes whose `to` is this `HC`), partition them by `correlated_with`, and you have exactly one `evidence()` call to write per correlated group and per lone edge. For each call, read the observation statement(s), the member statements in `HC.hypotheses`, the edge's `## Why this is evidence` body, and its `approved`/`corrected` arguments. Then estimate:

1. **Estimate relatively, not absolutely — this is the crux.** The update only uses the *ratios* between members; the absolute P(obs | H) is often ill-defined (it depends on how finely you slice the outcome space). So do not elicit N independent absolute probabilities. Pick the member the observation fits best, anchor its value, then for each other member ask "how many times less expected is *this exact* observation if that member were true?" Direct absolute-probability elicitation is measurably worse-calibrated than reasoning in discriminating ratios.
2. **Condition strictly on H.** P(obs | H) assumes the member is true; do not let "H seems unlikely" pull its likelihood down — that is the prior's job (step 8), and mixing it in double-counts. Ask only: *given* this member holds, how expected is the observation?
3. **Judge the correlated group as one pattern.** Picture the whole pattern the group describes and ask, under each member, how surprised you would be to see that whole pattern — not the product of per-observation guesses, which is exactly the independence error rule 1 forbids.
4. **Keep ratios honest.** A single edge rarely justifies a 100:1 likelihood ratio between members; treat any ratio past ~10:1 from one observation as a claim the argument must actually carry. The test is "would I bet at these odds?" (criterion 2). If members come out near-equal the observation is not discriminating — but step 5 already filtered for discrimination, so a flat vector usually means you have missed which way it cuts; re-read `## Why this is evidence`.
5. **Residual: an unconstrained explanation.** It can accommodate most patterns, so its likelihood is usually middling and rarely the extreme in either direction (rule 3).
6. **Choose `t` for data reliability, not truth.** Start at the cap (min `trust_score` over the named observations) and dock for everything between the raw data and the stated observation — measurement/dating error, selection or survivorship bias, reworking, a processing pipeline you could not audit. `t` says nothing about whether the member is true. With mixed trust in a group, the cap is the minimum.
7. **Let arguments set direction and size, then cite them.** The `## Why this is evidence` body tells you which members split and which way; an `approved`/`corrected` argument may widen or narrow a member's fit — name it in the comment of the number it moved (as the example does with A-7). Exclude `rejected` arguments entirely.
8. **Sketch variables first, values last.** Name all the likelihood variables and `t` with their reasoning, then fill numbers — it keeps you comparing members against each other rather than committing to isolated absolutes (criterion 7).
9. **Verify with the runner and read the shift.** After writing a cluster's blocks, run the analysis and ask whether the move from prior to posterior is one you would defend; re-run at `t=cap` and `t=1` to see how much of the shift is trust versus likelihood. If the output surprises you, fix the reasoning, not just the number. Commands (paths are from the workspace/vault root, since an executing agent's working directory varies):
   1. `python3 .claude/skills/flf-epistack/runner/run.py <analysis-dir>` — runs every block and prints `HC-N  prior [...]  posterior [...]` per cluster.
   2. `python3 .claude/skills/flf-epistack/runner/run.py <analysis-dir> --set E-14:t_dates=0.9 --set …` — override a named variable in a note (the `BLOCK` before the colon is the note's id) and re-run; this is how you price an assumption.
   3. `python3 .claude/skills/flf-epistack/runner/test_run.py` — self-check; the micro-example above is one of its fixtures.
