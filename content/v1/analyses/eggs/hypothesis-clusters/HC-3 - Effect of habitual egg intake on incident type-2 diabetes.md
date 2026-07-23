---
type: hypothesis-cluster
id: HC-3
hypotheses:
  - "[[H-8 - Egg-T2D association is region-population-dependent - positive in US, null in Europe, null-to-inverse in Asia]]"
  - "[[H-9 - US egg-T2D association reflects residual confounding by the co-consumed Western dietary pattern, not a causal egg effect]]"
  - "[[H-51 - Some other egg-T2D structure]]"
exclusivity: "Reading H-8 as a real region-dependent difference in the causal effect and H-9 as a uniformly null causal effect (the US-positive association being confounding), at most one can be the correct structure."
exhaustive_by_construction: false
independence: "Incident-T2D causation is a different outcome from CVD (HC-1/HC-2) and from the effect in already-diabetic people (HC-4); its base rate does not shift with those answers."
depends_on: []
question: "Does habitual egg intake causally raise incident type-2 diabetes, and how uniform is that across regions?"
relevance: "One arm of the 'overall health' verdict beyond CVD, and part of 'for whom'."
---

![[H-8 - Egg-T2D association is region-population-dependent - positive in US, null in Europe, null-to-inverse in Asia]]

![[H-9 - US egg-T2D association reflects residual confounding by the co-consumed Western dietary pattern, not a causal egg effect]]

![[H-51 - Some other egg-T2D structure]]

## Carving

The sub-question is whether habitual egg intake causally raises incident type-2 diabetes and how uniform that is. H-8 says the effect is genuinely region-dependent - modestly positive in US/Western cohorts, null in Europe, null-to-inverse in Asia; H-9 says there is no causal egg->T2D effect anywhere and the US-positive association is residual confounding by the co-consumed diabetogenic Western dietary pattern. Read as a real difference in the causal effect (H-8) versus uniform-null-via-confounding (H-9), at most one holds. Residual H-51 covers a uniform modest causal effect (positive or inverse) present across all regions, which neither paper endorses. The regional meta-analytic gradient (US 1.18 / Europe 0.99 / Asia 0.82) and the healthy-user/diet-quality signals discriminate the two. Distinct from HC-4, which concerns people who already have diabetes rather than incident disease in the general population.

## Prior

```python
# HC-3 prior -- structure of the habitual-egg / incident-type-2-diabetes relationship.
# Members in HC-3.hypotheses order:
#   [H-8  region-DEPENDENT genuine causal effect (US positive ~14-18% per egg/day, Europe null, Asia null-to-inverse),
#    H-9  UNIFORM NULL via confounding (no causal egg effect anywhere; the US-positive association is residual
#         confounding by the co-consumed diabetogenic Western dietary pattern),
#    H-51 residual: some OTHER structure, e.g. a UNIFORM modest causal effect (positive or inverse) in every region].
# exhaustive_by_construction: false -> H-51 residual carries its OWN argued weight (rule 4).
# No no-observation arguments exist for this cluster (no_observation_arguments.py --cluster HC-3 -> none).
# Evidence split: NO inbound edge is marked used_for_prior. Every HC-3 observation is an egg-T2D-SPECIFIC
# discriminating datum -- the region gradient (O-17/O-31, CG-8), the European and Japanese nulls (O-29/O-55),
# the diet-quality interaction (O-18), the confounder-correlation structure (O-43), the substitution pattern
# (O-19), the sex split (O-15) -- and all are left for step 8. The prior therefore rests purely on the OUTSIDE
# VIEW for a weak single-food nutritional association, before that egg-T2D record is read.

# H-9 -- uniform null; the association is confounding. Reference class: modest single-food cohort associations
# (RR ~1.1-1.2) in nutritional epidemiology are, at base rate, dominated by healthy-user / dietary-pattern
# residual confounding rather than causation. This is the modal a-priori explanation for such a signal, so take
# it as the unit anchor. For H-9 to be right, adjustment simply cannot fully strip the co-consumed diabetogenic
# pattern. Requires no genuine egg biology. Highest confidence of the three a priori.
w_conf = 1.0

# H-8 -- genuinely region-dependent CAUSAL effect. Two things must hold: a real causal egg->T2D effect exists,
# and it is region/context-modified rather than uniform. Reference class: effect modification of a food's effect
# by background diet/population is common in nutrition, but a weak association being causal AT ALL is a priori
# less likely than its being confounding -> priced below the anchor. Does not cover a uniform effect (H-51) or
# no effect (H-9).
real_vs_confounding = 0.85   # a priori odds a genuine causal egg->T2D effect exists at all, vs pure confounding (weak-association base rate keeps this below 1)
frac_region_modified = 0.65  # of genuine-effect worlds, the fraction where the effect is region/context-modified (effect modification by background diet is the nutritional norm) -> H-8
w_region = real_vs_confounding * frac_region_modified   # H-8, ~0.55 vs the confounding anchor

# H-51 residual -- a uniform modest causal effect (positive or inverse) present in EVERY region. Its OWN argued
# weight (rule 4), not the leftover of the genuine-effect mass. What an unmodelled answer looks like concretely:
# a consistent same-direction HR across US, Europe and Asia -- the uniform-effect account neither curated paper
# endorses. Plausible but disfavoured a priori because context-modification is the nutritional norm; kept
# non-trivial so no single observation can pin it to zero. Lowest confidence of the three.
w_uniform = 0.30   # H-51, own odds vs the confounding anchor

prior("HC-3", [w_region, w_conf, w_uniform])
```

