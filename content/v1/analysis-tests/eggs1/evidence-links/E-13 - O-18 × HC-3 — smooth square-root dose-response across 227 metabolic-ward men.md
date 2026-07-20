---
type: evidence-link
id: E-13
from: "[[O-18 - Serum total cholesterol rises with dietary cholesterol (50-1450 mg-d) with diminishing returns, fit by a square-root dose-response]]"
to: "[[HC-3 - Whether egg's effect varies by subgroup or individual responder type]]"
arguments:
  - "[[A-6 - Square-root dose-response implies each additional egg's serum-cholesterol effect shrinks at high baseline intake]]"
---
![[O-18 - Serum total cholesterol rises with dietary cholesterol (50-1450 mg-d) with diminishing returns, fit by a square-root dose-response]]

## Why this is evidence
A single well-fitting dose-response curve across 19 controlled comparisons is what H-13 predicts. H-7 predicts the aggregate curve masks a mixture of steep and flat individual slopes, so the population fit is uninformative about any one person. Note the diminishing-returns shape is an alternative, within-person explanation for apparent hypo-response at high habitual intake, which cuts against H-7's trait reading of the same data.
## Likelihood

```python
# E-13 (HC-3) - lone edge, one observation O-18 "smooth square-root dose-response fitting 227 men across 19
# metabolic-ward comparisons". Members in HC-3.hypotheses order: [H-6 T2D subgroup not harmed, H-7 stable
# hypo/hyper-responder trait, H-13 residual: homogeneous]. Anchored on H-13 = 1 (rule 7a).
# KEY JUDGEMENT: this is a POPULATION-LEVEL aggregate curve fitted across group-mean responses. A good
# aggregate fit is what H-13 predicts, but it is only weakly informative against H-7, because a smooth mean
# curve is fully compatible with wide individual scatter around it - the published fit reports the mean
# response, not the within-person residual spread. A-6 (approved) further shows the concave shape gives a
# WITHIN-person diminishing-returns explanation for apparent hypo-response at high habitual intake, i.e. a
# rival explanation for the very data H-7 reads as a trait. That cuts H-7's likelihood but does not collapse
# it: the ambiguity is priced, not resolved.
lik_dose_H13 = 1.0   # anchor: a single well-fitting curve across all 19 comparisons is exactly what
                     # homogeneity predicts. Still not a strong test - group means fit smoothly under
                     # heterogeneity too, so the anchor is deliberately not far above H-7
lik_dose_H7  = 0.7   # 0.7x: H-7 predicts the aggregate curve masks a mixture of steep and flat slopes; a
                     # clean population fit is mildly surprising under it but wholly compatible (mixtures of
                     # monotone slopes still aggregate to a smooth monotone curve). Docked from ~0.85 to 0.7
                     # by A-6 (approved): concavity supplies a within-person alternative to the trait reading
lik_dose_H6  = 0.9   # 0.9x: H-6 is about T2D/prediabetes subgroup safety. This series is 227 (largely
                     # non-diabetic) metabolic-ward men, so it barely bears on H-6 at all; near-uninformative,
                     # set just below the anchor only because a subgroup-modification world would slightly
                     # more often show a ragged aggregate fit
t_dose = 0.7         # cap = trust_score of O-18's source S-8 = 0.80. Docked to 0.7: the square-root form is a
                     # fitted functional choice over pooled group means from heterogeneous 1960s-80s ward
                     # protocols, and the raw within-study individual scatter was not inspectable
evidence("HC-3", ["O-18"], [lik_dose_H6, lik_dose_H7, lik_dose_H13], t=t_dose)
```
