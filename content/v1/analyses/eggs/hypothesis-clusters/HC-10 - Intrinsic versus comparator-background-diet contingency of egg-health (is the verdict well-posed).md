---
type: hypothesis-cluster
id: HC-10
hypotheses:
  - "[[H-17 - Eggs are a relatively unhealthy protein source; benefit comes from replacing eggs with plant or fish protein]]"
  - "[[H-18 - The egg-health effect is a property of the comparator not of eggs alone, so eggs good-or-bad is ill-posed]]"
  - "[[H-23 - Egg's CVD impact is relative to the food it replaces (neutral vs healthy proteins, better than red-processed meat)]]"
  - "[[H-38 - The health effect of eggs depends on background diet, being least harmful when displacing refined carbohydrate]]"
  - "[[H-57 - Some other egg-health characterization]]"
exclusivity: "At most one best characterization holds: a fixed intrinsic egg property (H-17) versus one of the contingency framings (unconditional-ill-posed H-18, substitution-indexed H-23, or background-diet-indexed H-38)."
exhaustive_by_construction: false
independence: "Whether egg-health is intrinsic or comparator-contingent is a framing question separable from the numeric overall sign (HC-1) and the region pattern (HC-2), noted in depends_on; its base rate does not factor through them."
depends_on:
  - "HC-1: contingency undercuts a single unconditional overall verdict"
  - "HC-2: background diet is a candidate mechanism for the regional differences"
question: "Is egg-health an intrinsic fixed property of eggs, or a property of the comparator and background diet - i.e. is an unconditional 'eggs are good/bad' even well-posed?"
relevance: "Directly answers the case framing's 'how can we tell / is the question well-posed'."
---

![[H-17 - Eggs are a relatively unhealthy protein source; benefit comes from replacing eggs with plant or fish protein]]

![[H-18 - The egg-health effect is a property of the comparator not of eggs alone, so eggs good-or-bad is ill-posed]]

![[H-23 - Egg's CVD impact is relative to the food it replaces (neutral vs healthy proteins, better than red-processed meat)]]

![[H-38 - The health effect of eggs depends on background diet, being least harmful when displacing refined carbohydrate]]

![[H-57 - Some other egg-health characterization]]

## Carving

The sub-question is whether egg-health is an intrinsic fixed property of eggs or a property of the comparator and background diet - i.e. whether an unconditional verdict is even well-posed. H-17 asserts an intrinsic property: eggs are among the least-healthy protein sources and benefit accrues from replacing them. The contingency pole holds that there is no fixed effect - the verdict is a property of the displaced food and background diet - expressed generally (H-18, the unconditional verdict is ill-posed), as substitution-indexing (H-23, neutral versus fish/poultry/plant proteins, preferable to red/processed meat), and as background-diet-indexing (H-38, least harmful displacing refined carbohydrate, which also reconciles protective Asian and null/harmful Western findings). At most one best characterization holds. The contingency members are refinements at a shared grain, discriminated from H-17 by the large within-dataset substitution swings (egg-removal ranging from null vs processed meat to strongly protective vs nuts/whole grains). Residual H-57 covers a partly-intrinsic, partly-contingent mix. Kept distinct from HC-1 and HC-2 (this is a well-posedness/framing question, not a numeric sign or a geographic pattern), with the couplings logged in depends_on.

## Prior

```python
# HC-10 prior — is egg-health an intrinsic fixed property of eggs or a property of the comparator / background diet?
# Members in HC-10.hypotheses order: [H-17 intrinsic-unhealthy fixed rank; H-18 unconditional verdict ill-posed
# (fully comparator-contingent); H-23 substitution-indexed; H-38 background-diet-indexed; H-57 residual]. Non-exhaustive,
# residual last. Evidence split: all nine inbound E edges are EGG-SPECIFIC discriminating observations — the
# substitution rankings (E-88/89/90 in CG-30; E-87/91 in CG-29) and the region/diet-quality gradients (E-92/93/95 in
# CG-29, E-94) tell H-17 from the contingency framings and separate the contingency flavours — so NONE is marked
# used_for_prior; all are priced at step 8. no_observation_arguments.py --cluster HC-10 returns none. This prior is
# therefore a pure OUTSIDE VIEW on the framing question, resting on a methodological base rate, not on the egg data.

# H-17 intrinsic anchor — the unit weight. What must hold: eggs carry a comparator-STABLE low rank (a fixed property,
# benefit accruing from replacing them), not merely a rank that flips with the displaced food. Reference class: single
# foods whose health effect is claimed to be intrinsic rather than substitution-defined. This is the minority framing
# because the field's default (below) runs the other way, but eggs' distinctive cholesterol/choline load makes a
# stable-ish signal plausible, so it keeps real weight — comparable to each single contingency member.
w_intrinsic = 1.0  # H-17 anchor: a stable intrinsic egg rank is plausible but is the minority framing

# Contingency family (H-18 + H-23 + H-38) as odds vs the intrinsic pole. In nutritional epidemiology a single food's
# modelled effect is an isocaloric substitution quantity — the difference of two food coefficients — so "what does it
# replace / against what background" is near-definitionally load-bearing, and the field's default frame is contingency.
# Hence the contingency family outweighs the intrinsic pole several-fold a priori.
contingency_vs_intrinsic = 3.0  # would be right if the framing splits ~75% contingency / ~25% intrinsic across foods
w_contingency_family = contingency_vs_intrinsic * w_intrinsic

# Partition the contingency family across its three flavours (shares sum to 1 by construction). H-18 (general
# ill-posedness) is the broadest and most defensible, so the largest share; H-23 (substitution-indexing) is the
# standard analytic frame, nearly as broad; H-38 (background-diet-indexing) makes the most SPECIFIC directional claim
# (least harmful displacing refined carbohydrate, reconciling Asian-protective / Western-null), so the smallest share.
share_illposed = 0.40       # H-18: broadest contingency framing -> largest slice
share_substitution = 0.35   # H-23: substitution-indexing, the routine analytic frame
share_bgdiet = 0.25         # H-38: most specific directional claim -> smallest slice; 0.40+0.35+0.25 = 1.0
w_h18 = w_contingency_family * share_illposed
w_h23 = w_contingency_family * share_substitution
w_h38 = w_contingency_family * share_bgdiet

# H-57 residual — the truth is a characterization none of the four clean framings captures, most concretely a
# partly-intrinsic / partly-contingent hybrid (a stable egg component PLUS comparator/background modulation). Its own
# argued weight (rule 4), not a leftover: genuinely plausible for a messy real diet, but the four framings — H-18
# especially — already span most of the space, so it sits below each modelled member.
w_residual = 0.5  # ~0.5:1 vs the intrinsic anchor; ~11% of the mass once normalised

prior("HC-10", [w_intrinsic, w_h18, w_h23, w_h38, w_residual])
```
