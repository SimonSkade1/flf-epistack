---
id: E-127
type: evidence-link
from: "[[O-108 - China-PAR U-shaped egg-CVD association lowest at 3 to under 6 eggs per week higher at both extremes]]"
to: "[[HC-2 - Regional-population modification of the egg-cardiovascular association]]"
arguments:
  - "[[A-41 - Elevated risk at both intake extremes within one cohort refutes any monotone egg-CVD dose-response for this population]]"
  - "[[A-42 - The low-intake arm of the U may overstate harm because very low egg intake marks low socioeconomic status and poor health]]"
---
![[O-108 - China-PAR U-shaped egg-CVD association lowest at 3 to under 6 eggs per week higher at both extremes]]

## Why this is evidence

Within a Chinese cohort the egg-CVD association is U-shaped (higher risk below ~1/week and above ~10/week, lowest at 3-<6/week), i.e. one universal non-linear dose-response. This lets H-50's differential-exposure-range explanation reframe the "regional modification" as different regions sampling different arms of one curve (China Kadoorie sits entirely on the low, descending limb). H-22 (a true regional difference in the causal effect) and H-7 (monotone healthy-user confounding, which cannot generate harm at high intake) predict this pattern less well.

## Likelihood

```python
# E-127 (HC-2) — lone edge, one observation O-108 "China-PAR: within one Chinese cohort the egg-CVD
# association is U-shaped — lowest at 3-<6 eggs/wk, <1/wk HR 1.22, >=10/wk HR 1.39." Members in
# HC-2.hypotheses order [H-7, H-22, H-50]. Anchored on H-50 = 1 (best fit); others as ratios (rule 7).
lik_o108_H50 = 1.0   # anchor: a within-cohort U-shape is the direct signature of H-50's differential-
                     # exposure-range explanation — one universal non-linear dose-response, with regions
                     # (Kadoorie on the low descending limb) sampling different arms; A-41 (approved) confirms
                     # no monotone model fits this population
lik_o108_H22 = 0.4   # 0.4×: a within-Asia U-shape (harm at both extremes) undercuts a clean causal "inverse
                     # in Asia"; genuine region-modification predicts this pattern less well. Not lower
                     # because modification could in principle co-exist with a dose-shape
lik_o108_H7  = 0.35  # 0.35×: healthy-user/residual confounding is monotone and CANNOT generate the high-
                     # intake harm arm (HR 1.39 at >=10/wk); A-42 (approved) shows it DOES explain the
                     # inflated low-intake arm (HR 1.22, reverse-causation / low-SES), so partial fit — but
                     # the unexplained right arm makes it the poorest of the three
t_o108 = 0.62        # cap = trust_score of O-108's source S-81 = 0.68; docked to 0.62 for a specific
                     # weakness — the intermediate category HRs were paywalled/unread, so the "U" shape is
                     # inferred from the two reported extremes plus the interior reference (rule 4)
evidence("HC-2", ["O-108"], [lik_o108_H7, lik_o108_H22, lik_o108_H50], t=t_o108)
```
