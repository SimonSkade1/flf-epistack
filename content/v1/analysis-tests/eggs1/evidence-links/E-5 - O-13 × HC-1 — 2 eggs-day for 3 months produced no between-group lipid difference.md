---
type: evidence-link
id: E-5
from: "[[O-13 - High-egg vs low-egg diet showed no between-group difference in blood lipids over 3 months in prediabetes-T2D (DIABEGG RCT)]]"
to: "[[HC-1 - Magnitude and mechanism of egg's effect on atherogenic blood lipids]]"
---
![[O-13 - High-egg vs low-egg diet showed no between-group difference in blood lipids over 3 months in prediabetes-T2D (DIABEGG RCT)]]

## Why this is evidence

A 3-month 2-eggs/day RCT null on LDL-C is what H-8 (saturation at already-high habitual Western intake), H-5 (poor absorption) and H-11 (no effect) predict. H-1 predicts a detectable LDL-ApoB rise at this dose, so this is the sharpest discrimination against H-1.

## Likelihood

```python
# E-5 (HC-1) - lone edge, one observation O-13 "no between-group lipid difference at 2 eggs/d for 3
# months in prediabetes/T2D (n=140)". Members in HC-1.hypotheses order:
# [H-1 large ApoB rise, H-5 poor bioavailability, H-8 real-but-saturating, H-11 residual].
# Anchored on H-8 = 1 (rule 7): a null at 2 eggs/d on a Western baseline is exactly what saturation
# predicts, so it is the most-expected member and a convenient anchor.
lik_diabegg_H8 = 1.0   # anchor: at habitual Western intake (~300 mg/d) the extra ~400 mg/d sits on the
                       # flat part of the curve; a null at n=140 over 3 months is the modal outcome
lik_diabegg_H5 = 1.0   # equally expected: if egg-matrix cholesterol is poorly absorbed the dose barely
                       # enters, so a null is just as unsurprising. This edge does not separate H-5/H-8
lik_diabegg_H1 = 0.30  # 0.3x as expected: H-1 predicts a detectable LDL-C rise at +400 mg/d. But the
                       # trial is not decisive against it - n=140, 3 months, free-living compliance and
                       # background-diet substitution give real power to miss a ~0.1-0.2 mmol/L effect,
                       # so a null is possible-but-surprising rather than near-excluded
lik_diabegg_H11 = 0.9  # residual, unconstrained (rule 3): a no-effect or non-LDL-mass characterization
                       # accommodates a null easily; a hair below the anchor only because some unlisted
                       # characterizations (e.g. subgroup-specific large effects) would have shown up
t_diabegg = 0.62       # cap = trust_score of O-13's source S-1 = 0.70. Docked for the gap between raw
                       # data and the stated observation: free-living self-reported adherence, and a
                       # between-group null in a diabetic/prediabetic population may not transfer to the
                       # general habitual-intake question this cluster is about
evidence("HC-1", ["O-13"], [lik_diabegg_H1, lik_diabegg_H5, lik_diabegg_H8, lik_diabegg_H11], t=t_diabegg)
```
