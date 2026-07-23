---
id: E-111
type: evidence-link
from: "[[O-48 - Egg-CVD meta-association inverse in Asian cohorts (0.92) but null in US (1.01) and Europe (1.05)]]"
to: "[[HC-5 - Operative exposure behind the egg-cardiovascular association]]"
arguments:
  - "[[A-18 - Region-structured heterogeneity favors population effect-modification over a universal egg-CVD null]]"
---
![[O-48 - Egg-CVD meta-association inverse in Asian cohorts (0.92) but null in US (1.01) and Europe (1.05)]]

## Why this is evidence
An egg-intrinsic operative exposure (cholesterol H-26 or fat quality H-3) should act in the same direction everywhere; an inverse association in Asian cohorts but null in US/Europe implicates dietary context/confounding (H-54) rather than a fixed egg component.

## Likelihood

```python
# E-111 (HC-5) — lone edge, one observation O-48 "egg-CVD direction differs by region". Members in
# HC-5.hypotheses order [H-3 fat-quality, H-26 dietary-cholesterol, H-54 residual]. The egg-CVD meta-association
# is inverse in Asian cohorts (0.92), null in US (1.01) and Europe (1.05), with region the main heterogeneity
# source. A region-varying DIRECTION implicates dietary context / confounding rather than a fixed egg component
# (A-18, corrected: population/dietary-context effect-modification). Anchored on H-54 = 1.0.
lik_region_H54 = 1.0  # anchor: a sign-flipping-by-region association is the signature of dietary-context
                      # confounding / effect-modification — H-54's artefact pole.
lik_region_H3 = 0.6   # 0.6x: H-3's operative agent is the accompanying dietary fat quality, which genuinely
                      # varies by region (eggs eaten with different foods in Asia vs the West), so a
                      # region-varying association is moderately consistent with H-3 — more so than the edge's
                      # "same direction everywhere" framing, which treats fat as egg-intrinsic.
lik_region_H26 = 0.45 # 0.45x: an egg-cholesterol operative exposure raises LDL in the same direction across
                      # populations, so the Asian inverse vs US/Europe null is awkward, accommodatable only via
                      # region-differing confounding structure.
t_region = 0.82       # cap = trust of O-48's source S-19 = 0.82. Held at cap: the stratified region RRs are
                      # reliably reported; the marginal interaction (P=0.07) and within-region heterogeneity
                      # (I2 up to 64.7%) weaken discrimination strength, carried in the moderate ratios rather
                      # than a t dock.
evidence("HC-5", ["O-48"], [lik_region_H3, lik_region_H26, lik_region_H54], t=t_region)
```
