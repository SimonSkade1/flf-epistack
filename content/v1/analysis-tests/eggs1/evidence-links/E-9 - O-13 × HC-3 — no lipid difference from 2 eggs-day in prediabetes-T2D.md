---
type: evidence-link
id: E-9
from: "[[O-13 - High-egg vs low-egg diet showed no between-group difference in blood lipids over 3 months in prediabetes-T2D (DIABEGG RCT)]]"
to: "[[HC-3 - Whether egg's effect varies by subgroup or individual responder type]]"
---
![[O-13 - High-egg vs low-egg diet showed no between-group difference in blood lipids over 3 months in prediabetes-T2D (DIABEGG RCT)]]

## Why this is evidence
H-6 predicts exactly this: a null lipid response in the named vulnerable subgroup. H-13 (homogeneous effect) predicts the subgroup tracks whatever the population-average lipid response is, so a clean null here is only expected if that average is also null. H-7 predicts a mixed group of hypo- and hyper-responders whose group mean can wash out, so it is compatible but less sharply predictive.
## Likelihood

```python
# E-9 (HC-3) - lone edge, one observation O-13 (DIABEGG: 2 eggs/day vs <2 eggs/wk, n=140 prediabetes/T2D,
# 3 months, no between-group lipid difference). Members in HC-3.hypotheses order:
# [H-6 diabetic subgroup not harmed, H-7 hypo/hyper-responder trait, H-13 residual: homogeneous].
# Anchored on H-6 = 1 (rule 7).
lik_diabegg_H6 = 1.0   # anchor: H-6 IS this prediction - a null lipid response to 2 eggs/day in exactly
                       # the named vulnerable subgroup, in a randomised design. Best possible fit.
lik_diabegg_H7 = 0.85  # 0.85x: a mixed population of hypo- and hyper-responders averages toward a null
                       # group mean, so this is nearly as expected under H-7. But H-7 is near-SILENT on a
                       # diabetes-defined split - it says nothing about this subgroup in particular - so
                       # the observation barely discriminates H-6 from H-7. Deliberately not manufacturing
                       # a discrimination the evidence layer does not contain (the H-6/H-7 non-exclusivity
                       # is already logged as a known limitation at cluster level).
lik_diabegg_H13 = 0.7  # 0.7x: under homogeneity the subgroup just tracks the population-average lipid
                       # response, so a clean null here is expected only insofar as that average is itself
                       # ~null. Given the wider evidence that the average whole-egg lipid effect at these
                       # doses is small, a null is fairly unsurprising under H-13 too - hence only a modest
                       # penalty, not a strong one.
t_diabegg = 0.60       # cap = trust_score of O-13's source S-1 = 0.70. Docked for: 3 months is short for a
                       # lipid endpoint only in the sense of adherence drift, n=140 gives limited power so
                       # a null is partly an absence-of-evidence artifact, and both arms were embedded in a
                       # weight-maintenance diet whose background composition I could not inspect.
evidence("HC-3", ["O-13"], [lik_diabegg_H6, lik_diabegg_H7, lik_diabegg_H13], t=t_diabegg)
```
