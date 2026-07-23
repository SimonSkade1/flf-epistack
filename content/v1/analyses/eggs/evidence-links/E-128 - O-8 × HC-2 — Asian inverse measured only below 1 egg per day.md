---
id: E-128
type: evidence-link
from: "[[O-8 - China Kadoorie egg intake calibrated to 0.29-0.76 eggs per day across categories]]"
to: "[[HC-2 - Regional-population modification of the egg-cardiovascular association]]"
---
![[O-8 - China Kadoorie egg intake calibrated to 0.29-0.76 eggs per day across categories]]

## Why this is evidence

The salient Asian "inverse" (China Kadoorie) is measured entirely below ~1 egg/day (top category 0.76/day). H-50's differential-exposure-range explanation needs precisely this: the protective Asian signal sits on the low-intake limb of the dose-response. H-22 and H-7 do not specifically predict that the Asian cohorts cluster at a narrow low intake range.

## Likelihood

```python
# E-128 (HC-2) — lone edge, one observation O-8 "China Kadoorie egg intake (single non-validated FFQ,
# calibrated) spans only 0.29-0.76 egg/day — the salient Asian inverse is measured entirely below ~1
# egg/day." Members in HC-2.hypotheses order [H-7, H-22, H-50]. No edge arguments. Anchored on H-50 = 1
# (best fit); others as ratios (rule 7).
lik_o8_H50 = 1.0   # anchor: H-50's exposure-range explanation needs exactly this — the salient Asian inverse
                   # sitting on the low-intake limb of one dose-response, reframing "inverse in Asia" as
                   # inverse-at-low-intake (dose-position)
lik_o8_H22 = 0.6   # 0.6×: genuine region-modification neither needs nor predicts the Asian cohort clustering
                   # at a narrow low intake; the low ceiling conflates region with dose-position, mildly
                   # against a clean regional-causal reading. Not lower because low Asian egg intake is a
                   # real-world fact roughly independent of which member holds
lik_o8_H7  = 0.65  # 0.65×: healthy-user/residual confounding likewise does not specifically predict the low
                   # intake range — roughly neutral; a touch above H-22 because the single non-validated FFQ
                   # (reproducibility r=0.58) noted here fits a confounding/measurement-artefact framing
                   # marginally better than genuine modification
t_o8 = 0.6         # cap = trust_score of O-8's source S-80 = 0.6 (already low; the non-validated crude FFQ is
                   # why it is low). The exposure-range datum rests on the 2013-14 resurvey calibration and is
                   # solid for its purpose; kept at cap (rule 4)
evidence("HC-2", ["O-8"], [lik_o8_H7, lik_o8_H22, lik_o8_H50], t=t_o8)
```
