---
id: E-94
type: evidence-link
from: "[[O-48 - Egg-CVD meta-association inverse in Asian cohorts (0.92) but null in US (1.01) and Europe (1.05)]]"
to: "[[HC-10 - Intrinsic versus comparator-background-diet contingency of egg-health (is the verdict well-posed)]]"
arguments:
  - "[[A-18 - Region-structured heterogeneity favors population effect-modification over a universal egg-CVD null]]"
---
![[O-48 - Egg-CVD meta-association inverse in Asian cohorts (0.92) but null in US (1.01) and Europe (1.05)]]

## Why this is evidence
Region-dependent direction of the egg-CVD association (inverse in Asia, null in US/Europe) supports background-diet-indexing (H-38) over a fixed intrinsic egg-CVD effect (H-17).

## Likelihood

```python
# E-94 (HC-10) — lone edge, one observation O-48 "egg-CVD meta-association inverse in Asia (0.92), null in US
# (1.01) and Europe (1.05); region is the main heterogeneity source, P-interaction=0.07". Members in
# HC-10.hypotheses order [H-17 intrinsic-fixed-rank, H-18 ill-posed/fully-contingent, H-23 substitution-indexed,
# H-38 background-diet-indexed, H-57 residual-hybrid]. This edge's body: region-DEPENDENT direction supports
# background-diet-indexing (H-38) over a fixed intrinsic effect (H-17). Anchored H-38 = 1.0 (rule 7).
lik_region_H38 = 1.0   # anchor / best fit: background-diet-indexing directly predicts and reconciles the
                       # Asia-inverse / West-null direction gradient (eggs displacing rice/veg vs Western foods).
lik_region_H23 = 0.8   # 0.8x: substitution-indexing maps onto region (Asian vs Western diets displace
                       # different foods), so it accommodates the gradient, but does not pin its specific
                       # direction the way H-38 does.
lik_region_H18 = 0.75  # 0.75x: full ill-posedness is consistent with structured heterogeneity but predicts
                       # only "no fixed answer", not the Asia-inverse direction specifically.
lik_region_H57 = 0.6   # 0.6x residual, middling (rule 3): a partly-intrinsic/partly-contingent hybrid
                       # accommodates a region gradient; unconstrained.
lik_region_H17 = 0.45  # 0.45x: a region-VARYING direction is against a comparator-stable intrinsic unhealthy
                       # rank; kept off the floor because A-18 (CORRECTED) shows region-correlated cohort
                       # artifacts (measurement, background diet, healthcare) could produce the same structure,
                       # i.e. a fixed effect plus differential bias is not excluded.
t_region = 0.75        # cap = trust_score of O-48's source S-19 = 0.82; docked to 0.75 for the gradient's
                       # marginal significance (P-interaction=0.07; within-region I2 up to 64.7% in Europe) —
                       # a genuine noise/robustness weakness in the stated region gradient, per A-18 (corrected).
evidence("HC-10", ["O-48"], [lik_region_H17, lik_region_H18, lik_region_H23, lik_region_H38, lik_region_H57], t=t_region)
```
