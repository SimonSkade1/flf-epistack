---
id: E-78
type: evidence-link
from: "[[O-49 - Meta-analysis in type-2-diabetes populations- higher egg intake associated with higher CVD risk (RR 1.25-1.40)]]"
to: "[[HC-4 - Cardiometabolic effect of eggs in people with diabetes, prediabetes, or metabolic syndrome]]"
---
![[O-49 - Meta-analysis in type-2-diabetes populations- higher egg intake associated with higher CVD risk (RR 1.25-1.40)]]

## Why this is evidence
A diabetic-restricted pooled egg-CVD RR of 1.25-1.40 is the direct 'for whom' harm signal H-24 predicts (and H-33 rationalises), whereas the safe pole (H-4/H-19) predicts RR near 1.0 in this population.

## Likelihood

```python
# E-78 (HC-4) — lone edge, one observation O-49: a diabetic-RESTRICTED pooled egg-CVD RR 1.25 (per +1 egg/day)
# to 1.40 (high-vs-low), CIs touching 1.0, considerable heterogeneity. Anchored on H-24 = 1.0 (rule 7).
# Members in HC-4.hypotheses order.
lik_dc_meta_H24 = 1.0   # anchor: a diabetic-restricted egg-CVD excess is the direct 'for whom' harm signal H-24 predicts
lik_dc_meta_H33 = 0.9   # 0.9x: H-33 rationalises the same diabetic harm; just below H-24 since its lipid mechanism is unshown here
lik_dc_meta_H4  = 0.4   # 0.4x: safe pole predicts RR near 1.0 in diabetics — RR 1.25-1.40 is against it, but
                        # softened because CIs touch 1.0 and heterogeneity is considerable (residual confounding can yield ~1.3)
lik_dc_meta_H19 = 0.4   # 0.4x: same as H-4 wrt this CVD signal (glycemic member, predicts no diabetic CVD harm)
lik_dc_meta_H52 = 0.6   # 0.6x: unlisted effect can accommodate a diabetic harm signal; middling (rule 3)
t_dc_meta = 0.7         # cap = trust S-19 0.82; docked for the pooled observational estimate's considerable
                        # between-study heterogeneity and borderline CIs — a named weakness in the datum
evidence("HC-4", ["O-49"], [lik_dc_meta_H4, lik_dc_meta_H19, lik_dc_meta_H24, lik_dc_meta_H33, lik_dc_meta_H52], t=t_dc_meta)
```
