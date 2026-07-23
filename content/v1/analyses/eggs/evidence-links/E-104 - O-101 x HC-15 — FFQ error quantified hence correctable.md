---
id: E-104
type: evidence-link
from: "[[O-101 - FFQ nutrient validity coefficients (~0.4-0.7; energy vs DLW r~0.25-0.32) allow measurement-error correction of estimates]]"
to: "[[HC-15 - Whether nutritional-cohort associations can support causal egg-health claims]]"
arguments:
  - "[[A-35 - Non-differential, calibratable dietary error biases against not toward positive findings, so measurement error is correctable rather than fatal]]"
---
![[O-101 - FFQ nutrient validity coefficients (~0.4-0.7; energy vs DLW r~0.25-0.32) allow measurement-error correction of estimates]]

## Why this is evidence
Validity coefficients (~0.4-0.7) from biomarker-validation studies let diet-disease estimates be de-attenuated by regression/biomarker calibration. H-41 reads FFQ error as quantified and therefore correctable (manageable); H-31 notes the low absolute-energy coefficients (0.25-0.32) concede the exposure is poorly measured. Discriminates.

## Likelihood

```python
# E-104 (HC-15) — lone edge, one observation O-101 "FFQ validity coefficients ~0.4-0.7 (energy vs DLW r~0.25-0.32)
# allow measurement-error correction". Discriminates toward defence (error is quantified, hence correctable) but the
# low absolute-energy coefficients concede the exposure is poorly measured. Members in HC-15.hypotheses order
# [H-31 reform; H-41 defence; H-59 residual]. Anchored on H-41 = 1 (best fit); others as ratios (rule 7).
lik_valcoef_H41 = 1.0   # anchor: defence reads FFQ error as quantified by validation substudies and de-attenuable by
                        # regression/biomarker calibration (A-35 corrected: sub-step 2, correctability, traces cleanly)
lik_valcoef_H31 = 0.65  # 0.65x: closer to the anchor than O-100 because the low energy coefficients (r~0.25-0.32) give
                        # reform a real foothold — the absolute exposure is poorly measured — partly offsetting the
                        # correctability reading
lik_valcoef_H59 = 0.85  # 0.85x: intermediate fits the "quantified and correctable in principle yet genuinely noisy"
                        # picture nearly as well as the defence anchor
t_valcoef = 0.62        # cap = trust_score(O-101 via S-100) = 0.62; O-101 reports referenced external
                        # validity-coefficient magnitudes, no extra raw->observation weakness beyond the source trust
evidence("HC-15", ["O-101"], [lik_valcoef_H31, lik_valcoef_H41, lik_valcoef_H59], t=t_valcoef)
```
