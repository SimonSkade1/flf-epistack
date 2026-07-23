---
id: E-131
type: evidence-link
from: "[[O-17 - Meta-analysis region gradient - egg-T2D RR US 1.18, Europe 0.99, Asia 0.82, p-interaction 0.01]]"
to: "[[HC-2 - Regional-population modification of the egg-cardiovascular association]]"
arguments:
  - "[[A-5 - Region- and diet-quality-dependence plus incomplete attenuation point to the US egg-T2D signal being confounded by the Western dietary pattern]]"
---
![[O-17 - Meta-analysis region gradient - egg-T2D RR US 1.18, Europe 0.99, Asia 0.82, p-interaction 0.01]]

## Why this is evidence

The same US-harm / Asia-protective gradient appears, statistically significant (p-interaction 0.01), for an independent outcome (T2D). A reproducible cross-outcome gradient argues against H-50's chance/publication-artefact sub-explanation and supports region genuinely (or systematically, via exposure range) modifying egg-disease associations (H-22 / H-50-exposure-range). Pure chance predicts no reproducible cross-outcome gradient.

## Likelihood

```python
# E-131 (HC-2) — lone edge, one observation O-17 "16-cohort meta-analysis: per-egg/day T2D RR differs by
# region (P-interaction 0.01) — US 1.18, Europe 0.99, Asia 0.82; the same US-harm / Asia-protective gradient
# as for CVD, on an INDEPENDENT outcome." Members in HC-2.hypotheses order [H-7, H-22, H-50]. Anchored on
# H-22 = 1 (its direct signature); others as ratios (rule 7).
lik_o17_H22 = 1.0   # anchor: a reproducible, significant (P-interaction 0.01) cross-outcome region gradient is
                    # exactly what genuine systematic region-modification predicts — region should modify
                    # egg-disease associations across outcomes, not CVD alone
lik_o17_H7  = 0.85  # 0.85×: systematic region-correlated confounding reproduces the same gradient across
                    # outcomes because the confounders are shared — healthy-user in Asia, the Western dietary
                    # pattern eggs mark in the US; A-5 (approved) reads the T2D gradient as confounding-by-
                    # Western-pattern rather than a portable causal effect. Docked slightly because H-7 is
                    # framed around the Asian inverse, whereas this observation centers the US-harm arm
lik_o17_H50 = 0.55  # 0.55×: the cross-outcome reproducibility argues AGAINST H-50's chance / publication-
                    # artefact sub-explanation (pure chance predicts no reproducible cross-outcome gradient),
                    # a real hit to part of the residual; its exposure-range/measurement sub-explanations are
                    # systematic and survive, so middling rather than low — residual stays off the extremes
t_o17 = 0.78        # cap = trust_score of O-17's source S-4 = 0.78. Region stratification with wide/NS Asian
                    # (0.62-1.09) and European strata limits precision, but that is discriminating-power, not
                    # data reliability; no specific data weakness to dock, kept at cap (rule 4)
evidence("HC-2", ["O-17"], [lik_o17_H7, lik_o17_H22, lik_o17_H50], t=t_o17)
```
