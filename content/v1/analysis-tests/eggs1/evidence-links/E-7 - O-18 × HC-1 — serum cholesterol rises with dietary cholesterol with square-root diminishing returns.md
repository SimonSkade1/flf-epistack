---
type: evidence-link
id: E-7
from: "[[O-18 - Serum total cholesterol rises with dietary cholesterol (50-1450 mg-d) with diminishing returns, fit by a square-root dose-response]]"
to: "[[HC-1 - Magnitude and mechanism of egg's effect on atherogenic blood lipids]]"
arguments:
  - "[[A-6 - Square-root dose-response implies each additional egg's serum-cholesterol effect shrinks at high baseline intake]]"
---
![[O-18 - Serum total cholesterol rises with dietary cholesterol (50-1450 mg-d) with diminishing returns, fit by a square-root dose-response]]

## Why this is evidence

This is H-8's defining shape: a genuine but strongly saturating effect. H-5 predicts a flat, small effect attributable to absorption rather than a dose-response with a real slope at low intake. H-1 predicts a large effect that does not flatten in the habitual range. H-11's no-effect variant predicts no dose-response at all.

## Likelihood

```python
# E-7 (HC-1) - lone edge, one observation O-18 "serum total cholesterol rises across 50-1450 mg/d with
# strongly diminishing returns, best fit by a square-root term (227 men, 19 metabolic-ward comparisons)".
# Members in HC-1.hypotheses order:
# [H-1 large ApoB rise, H-5 poor bioavailability, H-8 real-but-saturating, H-11 residual].
# This is H-8's defining curve shape. Anchored on H-8 = 1 (rule 7).
lik_sqrt_H8 = 1.0    # anchor: a real slope at low intake that flattens at high intake IS the hypothesis.
                     # A-6 (approved) makes the inference explicit - d/dx k*sqrt(x) = k/(2*sqrt(x)) is
                     # strictly decreasing, so each additional egg does less at high baseline intake
lik_sqrt_H1 = 0.25   # 0.25x: H-1 needs the effect to stay steep across the habitual range. The fit does
                     # show a genuine rise (so not near-zero for H-1 - a real effect exists), but the
                     # square-root shape is the wrong shape for a large marginal effect at ~300 mg/d
lik_sqrt_H5 = 0.20   # 0.20x: poor bioavailability predicts a flat, small response attributable to
                     # absorption, not a steep well-resolved slope at the low end of a 50-1450 mg/d range.
                     # Slightly below H-1 because the low-dose slope is the part H-5 fits worst
lik_sqrt_H11 = 0.35  # residual, unconstrained (rule 3): an unlisted characterization neither predicts
                     # nor forbids a square-root curve in total cholesterol; middling, but below the
                     # anchor since it does not specifically expect this shape
t_sqrt = 0.78        # cap = trust_score of O-18's source S-8 = 0.80. Metabolic-ward feeding with all
                     # other diet variables held constant is about as clean as this data gets; docked
                     # only slightly because the functional form is a post-hoc curve fit and the endpoint
                     # is total cholesterol rather than the LDL-ApoB this cluster is ultimately about
evidence("HC-1", ["O-18"], [lik_sqrt_H1, lik_sqrt_H5, lik_sqrt_H8, lik_sqrt_H11], t=t_sqrt)
```
