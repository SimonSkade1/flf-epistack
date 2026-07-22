---
id: E-28
type: evidence-link
from: "[[O-7 - Torsion-balance experiments limit the RS2 warping length L to below 44 microns]]"
to: "[[HC-1 - Short-distance structure and fundamental scale of gravity]]"
arguments:
  - "[[A-9 - The allowed warping-length range up to 44 microns permits Casadio-Harms critical masses for which black-hole growth is catastrophic]]"
---
![[O-7 - Torsion-balance experiments limit the RS2 warping length L to below 44 microns]]

## Why this is evidence

The members predict the outcome of sub-millimeter gravity tests differently. H-27 (ordinary Einstein gravity, Planckian scale) and H-4 (RS1, whose single warped dimension is only tens of fundamental lengths, far below any laboratory scale) predict a null with certainty at these distances. H-2's parameter space, however, includes the two-extra-dimension case whose compactification radius sits in the sub-millimeter range — exactly where these torsion-balance tests looked — so under H-2 there was a live chance of a detected deviation, and the null truncates H-2's allowed range from the top while leaving its smaller-radius (higher-n) realizations untouched. H-33's residual space likewise includes completions modifying gravity in the newly probed window, which the null now excludes. Direction: against the large-radius corner of H-2 and part of H-33, neutral between H-4 and H-27.

## Likelihood

```python
# E-28 (HC-1) — lone edge, one observation O-7 "sub-mm torsion-balance null bounds the RS2 warping length
# L < 44 um (15.3-44 um still allowed)". Members in HC-1.hypotheses order [H-2 ADD/TeV-string, H-4 RS1,
# H-27 Planckian, H-33 residual]. A null at sub-mm distances is generic — almost every member predicts it —
# so the update is weak; only H-2's large-radius (n=2) corner would have shown a deviation. Anchored on
# H-27 = 1 (rule 7).
lik_L_H27 = 1.0   # anchor: a Planckian fundamental scale predicts a null at laboratory distances with certainty
lik_L_H4  = 1.0   # RS1's single warped dimension is only tens of fundamental lengths, far below any lab
                  # scale — null certain, identical to standard gravity
lik_L_H2  = 0.82  # 0.82x: only the n=2 large-radius corner of H-2's parameter space sits in the probed sub-mm
                  # window and would have produced a detection; higher-n (smaller-radius) realizations predict
                  # a null anyway, so the null only shaves the top slice. Kept near 1 because A-9 (approved)
                  # confirms the 95% CL limit leaves L = 15.3-44 um OPEN — a shallow, not deep, truncation
lik_L_H33 = 0.85  # residual (rule 3): mostly null-predicting like any generic completion, docked modestly
                  # because the part of its space that modifies gravity in the newly probed window is now excluded
t_L = 0.3         # cap = trust_score(S-30, Plaga) = 0.3; the underlying Kapner et al. 2007 limit is firmly
                  # established, so no dock below the source cap
evidence("HC-1", ["O-7"], [lik_L_H2, lik_L_H4, lik_L_H27, lik_L_H33], t=t_L)
```
