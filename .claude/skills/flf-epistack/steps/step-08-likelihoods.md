# Step 8 — Estimate likelihoods per (cluster, observation)

**What step 8 does.** Step 5 built the evidence layer: for each observation that *discriminates* between a cluster's mutually-exclusive answers, it created an `evidence-link` node pointing that observation at that cluster. Step 8 prices each edge — for every cluster, and every group of observations that must be judged together, how likely those observations are under each member, P(obs | H) — written as a fenced `python` block the runner composes with step 7's prior into that cluster's posterior. Every number is a named variable with its reasoning in the comment beside it, and any number can be overridden and re-run, so what the answer hangs on gets priced and can be challenged rather than asserted.

## Relevant context

Everything you read is written by earlier steps and read-only; step 8 adds only `## Likelihood` blocks. The frontmatter it consumes:

**`evidence-link` (`E`, step 5)** — one node per (observation → cluster) edge.

| field | meaning |
|---|---|
| from | `[[O-N]]` — the observation |
| to | `[[HC-N]]` — the cluster whose members you price the observation under |
| group | `[[CG-N]]` or absent — set by step 5's consolidator; **present ⇒ this edge's likelihood is assessed jointly on that correlation-group node, not on the edge** (rule 1) |
| arguments | optional `[[A-N]]` list, written by step 5's consolidator — the arguments about this edge's observation; read the linked notes as reasoning |
| used_for_prior | `true` iff step 7 priced this edge into the prior (its datum is a base rate / outside-view fact). Such edges are dropped from your to-do set by `batch_likelihoods.py` and carry no `## Likelihood` block — already accounted for in the prior, never re-count them |
| `## Why this is evidence` (body) | prose naming which members predict the observation which way |

**`correlation-group` (`CG`, step 5)** — one node per connected group of correlated edges into a cluster.

| field | meaning |
|---|---|
| to | `[[HC-N]]` — the cluster all members edge into |
| members | `[[E-N]]` list (≥2) — the grouped edges; their `from` observations are what your one joint call names |

**`hypothesis-cluster` (`HC`, step 4)**

| field | meaning |
|---|---|
| hypotheses | ordered `[[H-N]]` list (ascending id, catch-all `residual` last) — **the frozen index of every likelihood vector you write** |
| exclusivity | one line on why at most one member is true — what makes the within-cluster likelihood *ratios* meaningful |

The `residual` member (`hypotheses[-1]`, the "answer is something not listed here" catch-all; absent only when the cluster is `exhaustive_by_construction`) gets a real likelihood like any other member.

**`source.trust_score` (step 2)** — a data-reliability weight in [0,1] on each `source`, judging how far the *data* can be trusted, separately from whether any claim built on it is true. An observation inherits it through its `source`; resolve it live, never copied onto the observation. It caps `t`.

**`argument.status` (step 6)** — `approved` (the inference holds), `corrected` (holds only in an adjusted form — use the corrected `statement`), or `rejected` (does not hold). Read `approved`/`corrected` arguments while choosing numbers; exclude `rejected` ones. (`reason_if_not_false` is step 9's audit signal, not an input here.)

## Interface

1. **Consumes, read-only** — the types in Relevant context. You touch no other cluster's numbers, since each cluster composes alone; `exclusivity` is what makes its within-cluster ratios meaningful.
2. **Owns** — the `## Likelihood` block(s) for the unit(s) you were assigned: one joint block on a `correlation-group` node, or one block on each lone evidence-link note. No node type, no prefix, no frontmatter field on any node, no generated file, no index, no `.base` view. **You do not run the composition** — `runner/run.py` does, injecting step 7's `prior(hc, w)`; that per-cluster prior, registered once in `HC.hypotheses` order, is the entire shared surface between the two steps.
3. **Hands to steps 9-10** — they read your blocks and the posteriors they produce. The per-number prose is step 9's raw material for what the model may not capture; overriding a named variable and re-running is how step 10 prices a driver. Neither is owed a sensitivity number or a ranked driver list from you — naming what the answer hangs on is prose.

## Spec

### The artifact

One fenced `python` block under a `## Likelihood` heading — on the evidence-link note for a lone edge, or on the `correlation-group` node for a grouped estimate. The block makes one call:

`evidence(hc, obs, lik, t)` — `hc` = cluster id string (e.g. `"HC-1"`); `obs` = the observation ids this call covers — normally just this edge's single observation (`["O-N"]`), and more than one only for a **correlation group** (a `CG-N` node), whose one joint call names every observation in the group (rule 1, below); `lik[i]` = P(**all** of `obs` together | member i), in `HC.hypotheses` order (residual included); `t` = reliability in (0, min `trust_score` over the observations in `obs`]. **The composition is implemented once, in `runner/run.py`, and you do not re-implement it:** the runner normalises the prior, then for each edge multiplies every member's running value by `t·lik[i] + (1−t)·marg`, where `marg` is the prior-weighted average likelihood, and renormalises at the end. Because each edge mixes against the *prior* marginal rather than the running posterior, a cluster's edges commute. The one-edge reading of that step: **`posterior = t·(posterior at t=1) + (1−t)·prior`** — `t` is literally how far you let this evidence carry you off the prior; at `t=0` the edge does nothing. Any named variable can be overridden and the model re-run with `--set BLOCK:var=value` (`BLOCK` = the note's id). Determinism — same notes, same numbers — needs arithmetic over named variables only: no import, RNG, clock, network, filesystem or LLM.

**Where the block lives when observations are correlated.** Step 5's consolidator groups edges into the same cluster whose observations share a `data-basis` node into a `correlation-group` (`CG-N`) node carrying their `members`. That group's **one** block — **one** `evidence()` call naming every observation in the group — lives on the `CG-N` node. Each member edge instead carries `group: [[CG-N]]` and holds **no** `## Likelihood` block of its own: the `group` link is the pointer, and Obsidian surfaces the CG on each edge as a backlink. An edge with no `group` (no correlated siblings) gets its own block on the edge note, covering its single observation.

### Rules

1. **Correlated observations get ONE joint estimate** — the load-bearing rule here. Step 5's consolidator groups edges into the same cluster whose observations trace to a shared `data-basis` node (the same dataset / instrument / compilation) — a whole connected component of such edges — into one `correlation-group` (`CG-N`) node. One `evidence()` call on that node covers the group and states P(all of them | H) *jointly*. Never one call per observation: that re-counts the same underlying data as independent, the standard way Bayesian aggregation manufactures false confidence. Treat the shared data as one witness — if it is wrong, every observation resting on it is wrong together.
2. **Every number is a named variable with a reason** — no bare numeric literal inside any expression or argument list. The comment says what would have to be true for the value, the reference class or mechanism it came from, what it does not cover, and its confidence against the sibling members; shorthand and several lines are both fine. Two competing framings for one number is a mixture written inline as ordinary arithmetic, each weight itself a named variable.
3. **The residual member gets a real, argued likelihood** like any other member, so unmodelled explanations compete in the posterior visibly. Being unconstrained, it usually neither strongly predicts nor forbids a given pattern — a middling value; setting it near zero asserts "no unlisted cause could produce this," which you rarely know. Add nothing else for model uncertainty here — no per-cluster uncertainty scalar, no cap on ratios, no floor tying the residual to its siblings. Structural doubt is argued in prose in step 9, where it can be read.
4. **`t` is capped by trust and argued downward**: `t ≤ min trust_score` over the observations named in the call. **Usually `t` just equals that cap** — the data is as reliable as step 2 found it and no more. Drop below it only for a specific, named weakness in the step from raw data to the stated observation (measurement or dating error, selection/survivorship effects, an analysis pipeline you could not inspect); an `approved`/`corrected` argument about the observation can be exactly what justifies the markdown. Never above the cap — the data cannot be more reliable than step 2 found it.
5. **Arguments enter as reasoning, not as a factor.** Read the edge's `approved`/`corrected` arguments and the `## Why this is evidence` body to decide *which way* and *how far* the observation discriminates; name any argument that moved a number in that number's comment. No argument gets a multiplicative term of its own — that double-counts strength step 6 deliberately did not score.
6. **Nothing derived is cached.** No posterior, prior, likelihood or ratio in frontmatter, and none in prose except quoted as the output of a named run. The run is the only copy; a hand-maintained number goes stale silently and announces nothing when it does.
7. **Anchor by ratio, or use a base rate.** Only the *ratios* between members matter — the scale cancels in the posterior — so estimate whichever way is more reliable, and don't eyeball all members' absolute probabilities at once. Two routes, mixable across members: **(a) anchor** — set one member's likelihood to 1 (any member; the best fit is often convenient) and price each other member as a ratio to it, named `lik_<obs>_<H>` (no `given`, since the value is a ratio to the anchor, not a conditional probability); **(b) absolute** — when a member's P(obs | H) is a base rate off a reference class, estimate it outright, named `p_<obs>_given_<H>`. Normalising the final vector changes nothing (the runner normalises), so the anchor's scale is free.

### Micro-example

`HC-1`, members in order `[H-3 direct predation, H-11 indirect human impact, H-21 climate aridification, H-42 residual]`, with step 7's prior over those members. Observations `O-14` "arrival-synchronised extinctions" and `O-22` "refugial survivors" both rest on the same continental age compilation `D-4`, so step 5 grouped them into `CG-1` (`members: [[E-14]], [[E-22]]`); its one joint block lives on that node. *Numbers illustrative and uncalibrated.*

```python
# CG-1 (HC-1) — ONE joint estimate over members E-14 + E-22: both observations rest on D-4 (rule 1). The
# pattern is judged whole — 8/12 genera within ~2 kyr of arrival (O-14 "arrival-synchronised extinctions"),
# 3 persisting >5 kyr (O-22 "refugial survivors"). Anchored on H-11 = 1; others priced as ratios to it (rule 7).
lik_ages_H11 = 1.0   # anchor: the staggered habitat squeeze is the only member predicting BOTH halves —
                     # most genera go with the burning front, refugial taxa persist past 5 kyr
lik_ages_H3  = 0.6   # 0.6× as expected as under H-11: predation fits the tight cluster but fits the 3
                     # genera surviving 5 kyr of active hunting worst. Raised by A-7 (approved): repeated
                     # arrival waves widen the window
lik_ages_H21 = 0.2   # 0.2×: aridification predicts ages track the aridity maximum, not the arrival
                     # window; reproducing this pattern needs a coincidence between the two
lik_ages_H42 = 0.4   # 0.4×: unlisted driver, unconstrained — neither predicts the pattern nor forbids
                     # it. Lower would assert no unlisted driver could produce it, which I don't know
t_dates = 0.55       # cap = min trust_score over {O-14, O-22} = 0.9 (both via S-1). Docked well below
                     # it: Signor-Lipps truncation and reworked specimens bias youngest ages in
                     # opposite directions, and D-4's screening protocol was never read
evidence("HC-1", ["O-14", "O-22"], [lik_ages_H3, lik_ages_H11, lik_ages_H21, lik_ages_H42], t=t_dates)
```

`E-14` and `E-22` each carry `group: [[CG-1]]` and no `## Likelihood` block of their own — the `CG-1` node holds the block above; Obsidian surfaces it on each edge as a backlink.

The anchor's scale is free — the runner normalises `lik`, so any rescaling of the vector gives the same result. With step 7's prior in, once the orchestrator runs the model this gives `HC-1`'s posterior, shifted off the prior toward `H-11` (indirect human impact). `t_dates` is doing visible work: raising it toward the cap (`t=0.9`) and on to `t=1` concentrates more of the update on `H-11`, while `t=0` returns the prior exactly. Pricing that is one `--set` and a re-run — which is what naming every variable (rule 2) buys, and it is step 10's lever, not yours.

**Absolute, from a base rate** — a second edge, different cluster. `HC-3` "what produced the age structure at site X", members `[H-5 ambush hunting, H-9 natural attrition, H-40 residual]`. `E-31` is a lone edge (no correlated siblings), so its block lives on the `E-31` note. `O-31` "prime-age mortality profile": the bone bed is >70% prime-age adults. Each member's likelihood is a base rate readable off actualistic reference classes, so absolute estimation is the natural way in — no anchoring needed.

```python
# E-31 (HC-3) — lone edge, one observation O-31 "prime-age mortality profile". Absolute likelihoods: the
# base rate of a prime-dominated profile under each regime is directly estimable from actualistic
# reference classes, so estimate P(obs | H) outright (rule 7).
p_profile_given_H5  = 0.55  # selective ambush hunting takes prime adults — prime-dominated in ~55% of
                            # actualistic hunting assemblages
p_profile_given_H9  = 0.10  # natural attrition (drought, disease) culls young + old first —
                            # prime-dominated in ~10%
p_profile_given_H40 = 0.25  # unlisted driver, unconstrained: a middling base rate, neither expects nor
                            # forbids a prime-dominated profile
t_profile = 0.70            # cap = trust_score of O-31's source S-4 = 0.8; docked for a small assemblage
                            # (n≈40) and age estimation from tooth wear
evidence("HC-3", ["O-31"], [p_profile_given_H5, p_profile_given_H9, p_profile_given_H40], t=t_profile)
```

`E-31` carries no `group`, so this block lives on the edge note itself.

### Checks (binary)

1. Every observation is covered by exactly one `evidence()` call for its cluster: a grouped edge through its `correlation-group` node's single call (which names every member observation), a lone edge through its own call. No member edge carries a `## Likelihood` block, and no observation appears in two calls for the same cluster.
2. Every `lik` has `len(HC.hypotheses)` entries in that order, and every `t` ∈ (0, min `trust_score` over the observations named]. (Whether every evidenced cluster also has a prior is the post-step-8 runner gate's check, not yours.)
3. No bare numeric literal appears inside any expression or argument list: every vector entry and every `t` is a named variable defined in the same block, each with a non-empty reason comment; no `rejected` argument is cited in a comment as support.
4. The blocks are deterministic and clean: no import / RNG / clock / network / filesystem call appears in any block; no posterior, prior, likelihood or ratio sits in any frontmatter field, and every such number in prose is quoted from a named run.

## Process

You are handed your unit(s) — either **one correlation-group** (`CG-N`), priced with a single joint `evidence()` call over its `members`, written on the CG node; or **up to three lone evidence-links**, each priced with its own call over its single observation, written on the edge note. (Which you get comes from the orchestrator; you don't scan for it.) The batcher (`batch_likelihoods.py`) has already dropped every edge step 7 marked `used_for_prior: true` — and any correlation group with a marked member — from what it hands you, and lists them, together with this cluster's no-observation arguments, under **ALREADY ACCOUNTED FOR IN THE PRIOR — do not double-count**. Treat that list as closed: you neither price those edges nor re-read or re-derive the prior calculation; step 7 owns it. For each call, read the observation statement(s), the member statements in `HC.hypotheses` (found via the edge's `to`), the edge's `## Why this is evidence` body, and its `approved`/`corrected` arguments. Then estimate:

1. **Estimate relatively or absolutely — whichever is more reliable (rule 7).** Only the *ratios* between members enter the posterior, so you needn't pin absolute probabilities. Usually easier: **anchor** one member at likelihood 1 (any member — no need to pick the best-fitting one) and ask, for each other member, "how many times more or less expected is *this exact* observation if that member were true?", as example 1 does with `lik_ages_H11 = 1`. When a member's P(obs | H) is a clean base rate off a reference class, estimate it **absolutely** instead (`p_profile_given_H5`, example 2). Absolute elicitation is otherwise often ill-defined — it can depend on how finely you slice the outcome space.
2. **Condition strictly on H.** P(obs | H) assumes the member is true; do not let "H seems unlikely" pull its likelihood down — that is the prior's job (step 7), and mixing it in double-counts. Ask only: *given* this member holds, how expected is the observation?
3. **Judge the correlated group as one pattern.** Picture the whole pattern the group describes and ask, under each member, how surprised you would be to see that whole pattern — not the product of per-observation guesses, which is exactly the independence error rule 1 forbids.
4. **Residual: an unconstrained explanation.** It can accommodate most patterns, so its likelihood is usually middling and rarely the extreme in either direction (rule 3).
5. **Choose `t` for data reliability, not truth.** Start at the cap (min `trust_score` over the named observations) and dock for everything between the raw data and the stated observation — measurement/dating error, selection or survivorship bias, reworking, a processing pipeline you could not audit. `t` says nothing about whether the member is true. With mixed trust in a group, the cap is the minimum.
6. **Let arguments set direction and size, then cite them.** The `## Why this is evidence` body tells you which members split and which way; an `approved`/`corrected` argument may widen or narrow a member's fit — name it in the comment of the number it moved (as the example does with A-7). Exclude `rejected` arguments entirely.
7. **Sketch variables first, values last.** Name all the likelihood variables and `t` with their reasoning, then fill numbers — it keeps you comparing members against each other rather than committing to isolated absolutes.
8. **Sanity-check your block; leave the composition to the gate.** Step 7's priors already exist, so a posterior is computable now — but composing it is the orchestrator's gate (`runner/run.py`, run once every likelihood is in), not yours. Check each block another way: members indexed in `HC.hypotheses` order, the anchor and ratios reading as your comments claim, `t` at or below its cap, no bare literal slipped in. Step 10 prices drivers with `--set`; a number you doubt is a comment you leave for them, not a run to chase now.
