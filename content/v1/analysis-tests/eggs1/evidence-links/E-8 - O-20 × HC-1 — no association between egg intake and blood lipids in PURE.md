---
type: evidence-link
id: E-8
from: "[[O-20 - Egg intake was not significantly associated with blood lipids, mortality, or major CVD in the PURE 21-country cohort]]"
to: "[[HC-1 - Magnitude and mechanism of egg's effect on atherogenic blood lipids]]"
---
![[O-20 - Egg intake was not significantly associated with blood lipids, mortality, or major CVD in the PURE 21-country cohort]]

## Why this is evidence

Only the blood-lipid arm of this observation is diagnostic here. H-1 predicts a visible cross-sectional lipid gradient with habitual egg intake; H-5, H-8 and H-11 all predict essentially none at habitual intakes. (Weak evidence - observational lipid comparisons are heavily confounded.)

## Likelihood

```python
# E-8 (HC-1) - lone edge, one observation O-20, and only its BLOOD-LIPID arm is diagnostic here (the
# hard-endpoint arm of O-20 is priced elsewhere, as CG-6 into the direction cluster). Members in
# HC-1.hypotheses order: [H-1 large ApoB rise, H-5 poor bioavailability, H-8 real but saturating,
# H-11 residual]. Anchored on H-8 = 1 and priced as ratios (rule 7).
lik_pure_H8 = 1.0    # anchor: a saturating dose-response predicts essentially no cross-sectional lipid
                     # gradient across the habitual intake range PURE spans, which is exactly what the
                     # primary analyses report. Best fit of the four.
lik_pure_H5 = 1.0    # equally expected: poor egg-matrix absorption also predicts a flat cross-sectional
                     # lipid gradient. This observation does not separate H-5 from H-8 at all - the
                     # absorption-vs-saturation split needs mechanism data (E-3/E-4), not a cohort null.
lik_pure_H1 = 0.5    # ~0.5x: a large, CVD-relevant ApoB rise should leave some visible gradient, so a
                     # clean null is a mild surprise. Only mild, and not lower, because this is an FFQ
                     # observational comparison, not a feeding study: residual confounding (higher egg
                     # eaters differing in SFA, BMI, statin use, healthy-user status across 21 countries)
                     # plus regression dilution from single FFQ measurement can flatten a real gradient.
                     # Step 5 flagged this edge as weak/confounded and that is what caps the discrimination.
lik_pure_H11 = 0.8   # 0.8x: unlisted characterization is unconstrained. A "no atherogenic-lipid effect at
                     # all" residual predicts the null strongly, but a non-ApoB-pathway residual is neutral
                     # about a standard lipid panel; the mixture lands slightly below the anchor.
t_pure = 0.55        # cap = trust_score of O-20's source S-11 = 0.8. Docked well below it: the step from
                     # raw data to "no lipid association" runs through self-reported FFQ intake in 21
                     # countries with heterogeneous dietary assessment, and the lipid arm is a
                     # cross-sectional secondary analysis whose adjustment set I could not inspect.
evidence("HC-1", ["O-20"], [lik_pure_H1, lik_pure_H5, lik_pure_H8, lik_pure_H11], t=t_pure)
```
