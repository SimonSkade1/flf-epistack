---
id: E-126
type: evidence-link
from: "[[O-72 - KoGES (Korea) - egg intake not associated with CVD incidence in the whole cohort]]"
to: "[[HC-2 - Regional-population modification of the egg-cardiovascular association]]"
arguments:
  - "[[A-24 - Adverse egg-CVD HR confined to the diabetic stratum supports effect-modification by diabetes, but the small subgroup makes it imprecise]]"
---
![[O-72 - KoGES (Korea) - egg intake not associated with CVD incidence in the whole cohort]]

## Why this is evidence

A second Asian (Korean) cohort shows no egg-CVD inverse (HR 1.14, NS), contradicting a uniform "inverse in Asia." H-22 predicts Asian populations show the protective association; H-7 and H-50 predict the Kadoorie inverse is cohort-specific / not a robust regional feature, so other Asian cohorts need not reproduce it.

## Likelihood

```python
# E-126 (HC-2) — lone edge, one observation O-72 "KoGES (Korea): egg intake NOT associated with CVD in the
# whole cohort (HR 1.14, 0.87-1.49, p-trend 0.7)." Members in HC-2.hypotheses order [H-7, H-22, H-50].
# Anchored on H-7 = 1 (best fit); others as ratios (rule 7).
lik_o72_H7  = 1.0   # anchor: H-7 (the Kadoorie Asian inverse is cohort-specific healthy-user confounding, not
                    # a robust regional feature) predicts a second Asian cohort need not reproduce the inverse
                    # — KoGES's null / slightly-positive HR is exactly expected
lik_o72_H22 = 0.45  # 0.45×: genuine "inverse in Asia" predicts KoGES also protective; instead HR 1.14 NS —
                    # evidence against. Not lower because the CI (0.87-1.49) still admits a masked modest
                    # inverse, and A-24 (approved) shows the whole-cohort null partly reflects dilution of a
                    # diabetic-specific harm rather than a true zero effect
lik_o72_H50 = 0.9   # 0.9×: "the Kadoorie inverse is not a robust regional feature, other Asian cohorts vary"
                    # is squarely H-50's non-region / exposure-range / chance story — nearly as expected as
                    # H-7, marginally lower as a diffuse residual
t_o72 = 0.55        # cap = trust_score of O-72's source S-14 = 0.55 (already low, single mid-size cohort). No
                    # further dock: the whole-cohort HR rests on 570 cases and is reasonably precise (A-24's
                    # imprecision concern is about the 79-case diabetic subgroup O-73, not this datum); at cap
evidence("HC-2", ["O-72"], [lik_o72_H7, lik_o72_H22, lik_o72_H50], t=t_o72)
```
