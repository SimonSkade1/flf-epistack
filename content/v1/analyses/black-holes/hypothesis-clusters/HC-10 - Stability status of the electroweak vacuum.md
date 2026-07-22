---
id: HC-10
type: hypothesis-cluster
question: "Is our vacuum a metastable false vacuum that can decay by bubble nucleation?"
hypotheses:
  - "[[H-31 - Our vacuum may be a metastable false vacuum that decays by true-vacuum bubble nucleation]]"
  - "[[H-42 - Our electroweak vacuum is exactly stable with no decay channel]]"
exclusivity: "Either a true-vacuum bubble-nucleation channel exists (our vacuum is a false vacuum) or none does; the members are a claim and its negation."
exhaustive_by_construction: true
independence: "The vacuum's stability status is fixed by the scalar potential of nature, not by the gravity-scale, strangelet, or astrophysical answers."
depends_on: []
relevance: "Vacuum decay is the most extreme proposed collision-triggered catastrophe; whether a decay channel exists at all is its physical premise."
---
![[H-31 - Our vacuum may be a metastable false vacuum that decays by true-vacuum bubble nucleation]]
![[H-42 - Our electroweak vacuum is exactly stable with no decay channel]]

False-vacuum metastability against absolute stability. Exhaustive by construction: proposition and logical complement. A failure of the analysis would look like the effective-potential extrapolation being invalidated by physics beyond the corpus's assumptions (new fields between the weak and Planck scales), and would favour whichever member that new physics selects — the named failure modes in the corpus (higher-dimension operators destabilizing the potential) favour the first member.

## Prior

```python
# HC-10 prior — stability status of the electroweak vacuum. exhaustive_by_construction, so no residual
# (rule 4 does not apply). Members in HC-10.hypotheses order:
#   [H-31 metastable false vacuum — a true-vacuum bubble-nucleation channel exists at a nonzero calculable rate,
#    H-42 exactly stable — our vacuum is the true minimum (or its decay rate is exactly zero), no channel].
#
# This is an OUTSIDE-VIEW prior: what a prior over "a decay channel exists vs exactly none" should look like
# BEFORE the measured Higgs and top masses are folded in. The mass measurements are the case evidence, not
# base-rate facts: the Degrassi-style effective-potential verdict (O-4 NNLO bound, O-5 metastability;
# edges E-4, E-10, correlation group CG-7) and past-light-cone survival (O-40; edge E-12) all DISCRIMINATE
# between the two members conditional on this specific vacuum's inputs, so none is marked used_for_prior —
# they are left, unmarked, for step 8 to price. Nothing here rests on a graph observation, so no edge is
# marked (rule 5, "select nothing" case). The cluster's no-observation arguments from
# `no_observation_arguments.py . --cluster HC-10` (A-63, A-64, both Coleman-De Luccia gravitational
# corrections) enter as reasoning only, never as a multiplicative term (rule 6): A-64 moves a number below;
# A-63 concerns the *consequences* of a decay (constants of nature change), not which member is true, so it
# does not move the stability-status split.

# H-31 metastable false vacuum — anchor at unit weight. Reference class: scalar potentials of unified
# electroweak and GUT completions, which S-16 (§1) states false vacua "occur naturally" in. Generic
# multi-field landscapes, once Planck-scale / higher-dimension operators are admitted, almost always develop
# a lower-lying minimum somewhere, so a nucleation channel generically exists; the note's named failure mode
# (destabilizing higher-dimension operators) sits on this side. This is the a-priori-favoured member. Does
# not cover *how fast* the channel decays — that rate is exactly the case-specific quantity step 8 prices.
w_false_vacuum = 1.0  # H-31 anchor: a decay channel generically exists in a multi-minimum BSM landscape

# H-42 exactly stable — priced as two disjoint routes to "no accessible decay channel", as odds vs H-31.
# Route 1: our vacuum is the global minimum, so there is simply no lower vacuum to tunnel to. Being the
# absolute minimum of a generic multi-field potential is special but not rare — one vacuum among the low
# ones has to be lowest.
p_global_min = 0.30   # fraction of generic BSM/GUT landscapes in which the EW vacuum is the absolute minimum
# Route 2: among the remaining cases a lower vacuum DOES exist, A-64 (approved, thin-wall Coleman-De Luccia)
# shows gravity can *totally quench* decay when epsilon <= 6 pi G sigma^2 = (3/4) kappa sigma^2 — the bubble
# radius diverges and the decay probability vanishes, i.e. the rate becomes exactly zero, which satisfies
# H-42's "rate exactly zero" clause even though a deeper vacuum is present.
frac_grav_quenched = 0.20   # A-64: share of lower-vacuum cases where gravitational quenching drives the rate to exactly zero
odds_stable = p_global_min + (1 - p_global_min) * frac_grav_quenched   # H-42 : H-31 (two disjoint routes)
w_stable = odds_stable * w_false_vacuum  # H-42

prior("HC-10", [w_false_vacuum, w_stable])
```

The weights `[1.0, 0.44]` normalise to ≈ `[0.56, 0.44]` — a deliberately mild outside-view lean toward metastability, leaving the measured Higgs/top masses (step 8, via CG-7) to do the discriminating work. `p_global_min` is the driver: raising it to 0.5 lifts H-42 to ≈ 0.48 (near-even), lowering it to 0.15 drops H-42 to ≈ 0.32 — the entire cost of the pre-measurement landscape assumption, with no other edit.
