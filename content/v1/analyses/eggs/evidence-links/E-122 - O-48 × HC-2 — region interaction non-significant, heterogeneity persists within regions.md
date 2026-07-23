---
id: E-122
type: evidence-link
from: "[[O-48 - Egg-CVD meta-association inverse in Asian cohorts (0.92) but null in US (1.01) and Europe (1.05)]]"
to: "[[HC-2 - Regional-population modification of the egg-cardiovascular association]]"
arguments:
  - "[[A-18 - Region-structured heterogeneity favors population effect-modification over a universal egg-CVD null]]"
---
![[O-48 - Egg-CVD meta-association inverse in Asian cohorts (0.92) but null in US (1.01) and Europe (1.05)]]

## Why this is evidence

Region is only the marginal, non-significant (p-interaction 0.07) leading source of heterogeneity, with within-region I2 of 30-65% still unexplained. H-22 (genuine, clean region-modification) predicts region should largely resolve the heterogeneity; H-50 (other origin / chance) and H-7 predict region is not the true axis, leaving the residual within-region heterogeneity and sub-significant interaction seen here.

## Likelihood

```python
# E-122 (HC-2) — lone edge, one observation O-48 "region-stratified egg-CVD meta-association: Asia inverse
# 0.92, US null 1.01, Europe null 1.05; region a marginal heterogeneity source (P-interaction 0.07); within-
# region I2 30-65% unexplained." Members in HC-2.hypotheses order [H-7 confounding, H-22 genuine modification,
# H-50 residual]. Anchored on H-22 = 1 (its direct signature); others as ratios (rule 7).
lik_o48_H22 = 1.0   # anchor: the Asia-inverse / West-null directional contrast IS H-22's stated pattern
lik_o48_H7  = 0.8   # 0.8×: region-correlated healthy-user/residual confounding reproduces the same contrast
                    # (A-18 corrected: differential bias explains the structure "equally well"), and the
                    # sub-significant interaction + large residual within-region I2 fit H-7's "region is not
                    # the clean causal axis"; docked only slightly below H-22 as the directional Asia-inverse
                    # is a hair more natural under genuine modification
lik_o48_H50 = 0.8   # 0.8×: exposure-range/measurement/chance equally reproduce a region-structured-but-messy
                    # pattern; the marginal interaction and unresolved within-region I2 fit "region not the
                    # true axis" as well as they fit H-7 — this observation barely separates H-7 from H-50
t_o48 = 0.82        # cap = trust_score of O-48's source S-19 = 0.82; no specific data-reliability weakness in
                    # the meta-analytic region stratification (its imprecision is discriminating-power, not
                    # data reliability), kept at cap (rule 4)
evidence("HC-2", ["O-48"], [lik_o48_H7, lik_o48_H22, lik_o48_H50], t=t_o48)
```
