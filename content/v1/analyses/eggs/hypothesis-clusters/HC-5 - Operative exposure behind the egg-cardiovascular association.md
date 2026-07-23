---
type: hypothesis-cluster
id: HC-5
hypotheses:
  - "[[H-3 - Dietary fat quality is a larger determinant of plasma cholesterol than dietary cholesterol quantity]]"
  - "[[H-26 - Dietary cholesterol content, not egg per se, is the operative exposure behind the egg-CVD association]]"
  - "[[H-54 - Some other operative exposure]]"
exclusivity: "At most one factor is the dominant operative exposure: egg-derived dietary cholesterol (H-26) or accompanying dietary fat saturation with cholesterol comparatively minor (H-3)."
exhaustive_by_construction: false
independence: "Which exposure is operative is separable from whether eggs net-harm (HC-1) - either agent is compatible with any overall sign; the mechanism shared with HC-6 is noted in depends_on."
depends_on:
  - "HC-1: H-27 bundles egg-cholesterol causality with the harmful overall verdict"
  - "HC-6: egg-cholesterol->LDL is the mechanism linking this exposure to harm"
question: "What is the operative exposure carrying the egg-CVD association - egg-derived dietary cholesterol, or accompanying dietary fat quality?"
relevance: "Determines whether 'eggs' or 'the cholesterol in eggs' (or neither) is the thing to act on."
---

![[H-3 - Dietary fat quality is a larger determinant of plasma cholesterol than dietary cholesterol quantity]]

![[H-26 - Dietary cholesterol content, not egg per se, is the operative exposure behind the egg-CVD association]]

![[H-54 - Some other operative exposure]]

## Carving

The sub-question is which exposure actually carries the egg-CVD association. H-26 makes egg-derived dietary cholesterol the operative agent - the egg association attenuating to null once dietary cholesterol is adjusted while dietary cholesterol keeps a monotonic dose-response; H-3 makes dietary fat saturation the larger determinant of plasma cholesterol, demoting egg cholesterol to a minor contributor. At most one is the dominant driver. Residual H-54 covers a non-cholesterol egg component being operative, or no real operative exposure at all (the association being an artefact of dietary-pattern confounding). Separated from HC-1 (whether eggs harm) and HC-6 (the biomarker lipid effect); the cholesterol-causality it shares with HC-1's H-27 and the cholesterol->LDL mechanism it shares with HC-6 are logged in depends_on rather than merged, since attribution, direction, and biomarker are three different questions.

## Prior

```python
# HC-5 prior -- operative exposure behind the egg-CVD association.
# Members in HC-5.hypotheses order:
#   [H-3  dietary fat quality (saturation) is the larger determinant of plasma cholesterol,
#    H-26 egg-derived dietary cholesterol content is the operative exposure,
#    H-54 residual: some OTHER operative exposure (non-cholesterol egg component) or NO real exposure at all
#         (the egg-CVD association being pure dietary-pattern confounding)].
# exhaustive_by_construction: false -> H-54 residual carries its OWN argued weight (rule 4).
# No no-observation arguments exist for this cluster (no_observation_arguments.py --cluster HC-5 -> none).
# Evidence split: the egg-SPECIFIC discriminating observations are left UNMARKED for step 8 -- homeostatic
# buffering (O-1/O-3, CG-13), the dietary-cholesterol dose-response and cholesterol-adjustment attenuation
# (O-41/O-58/O-60, CG-14), the confounding reversal (O-43/O-44, CG-15), the choline->TMAO null and rise
# (O-62/O-64, CG-16; O-103/O-105, CG-18), the genotype contrast (O-81/O-82, CG-17), plus O-32, O-48, O-75.
# The ONE datum folded into this prior is O-71 (E-116, used_for_prior): a general nutritional-cohort-vs-RCT
# reference-class fact, not an egg observation -- so it anchors a base rate rather than discriminating.

# H-3 -- fat quality is the larger determinant of plasma cholesterol than dietary cholesterol quantity.
# For H-3 to be the operative-exposure answer, the saturated/unsaturated fat accompanying eggs (and the diet at
# large), not the egg's own cholesterol, must be what moves plasma cholesterol and hence CVD risk. Reference
# class: mainstream modern lipidology -- the Keys and Hegsted regression equations weight dietary saturated fat
# several-fold above dietary cholesterol, and the 2015 US Dietary Guidelines dropped the 300 mg/day cholesterol
# cap while keeping the saturated-fat limit. This is the position I hold most likely a priori; take it as the
# unit anchor and price the others as odds against it. Does not cover the case that neither intrinsic agent
# matters (that is H-54).
w_fat = 1.0

# H-26 -- egg-derived dietary cholesterol is the operative exposure. For H-26, the cholesterol in eggs (not the
# accompanying fat, not an artefact) must be the graded lever carrying the association. Reference class:
# controlled-feeding meta-analyses show dietary cholesterol does raise LDL, but per-mg its effect is materially
# smaller than saturated fat's, and much of the population homeostatically buffers it. A coherent, recently
# defended claim (the operative-exposure thesis of a large pooled US-cohort analysis), but a priori weaker than
# the fat-quality view -> priced below the anchor. Confidence: lower than H-3, higher than the residual.
chol_vs_fat_odds = 0.72   # a priori odds that egg cholesterol, not the accompanying fat, is the dominant lever on plasma cholesterol / CVD
w_chol = chol_vs_fat_odds * w_fat

# H-54 residual -- the operative exposure is something the two named agents cannot express. Two escapes:
#   (a) ARTEFACT: no stable egg-intrinsic exposure at all; the egg-CVD association is dietary-pattern confounding.
#   (b) NON-CHOLESTEROL COMPONENT: a distinct egg constituent (choline -> TMAO route) is the operative agent.
# Its OWN argued weight (rule 4), not a leftover. What an unmodelled answer looks like concretely: the egg signal
# is fully explained by co-consumed foods/lifestyle (artefact), or carried by a non-lipid egg constituent.
beta_carotene_cohort_rr = 0.69    # O-71 / E-116 (used_for_prior): serum beta-carotene shows a protective mortality RR 0.69 in cohorts that RCTs entirely exclude -- exemplar of an objectively-measured nutritional-cohort association that is pure confounding
p_nutricohort_confounded = 0.35   # base rate a comparable objectively-measured nutritional cohort association is pure confounding rather than causal, anchored on the beta-carotene exemplar above
frac_no_intrinsic_agent = 0.8     # share of that confounded mass implying NO stable egg-intrinsic agent (the H-54 artefact pole) rather than a merely-shrunken cholesterol/fat effect
p_artefact_branch = p_nutricohort_confounded * frac_no_intrinsic_agent   # ~0.28 vs the fat anchor
p_noncholesterol_branch = 0.22    # a priori odds (vs the fat anchor) that a non-cholesterol egg component (choline->TMAO) is the operative exposure
w_residual = p_artefact_branch + p_noncholesterol_branch   # H-54, own weight ~0.50

prior("HC-5", [w_fat, w_chol, w_residual])
```

