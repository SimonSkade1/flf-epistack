---
type: evidence-link
id: E-21
from: "[[O-19 - Up to at least 1 egg-day was not associated with incident CVD in pooled NHS-NHSII-HPFS cohorts]]"
to: "[[HC-2 - Net direction of egg's effect on hard cardiovascular and mortality endpoints]]"
---
![[O-19 - Up to at least 1 egg-day was not associated with incident CVD in pooled NHS-NHSII-HPFS cohorts]]

## Why this is evidence

Per-member (H-2, H-3, H-4, H-9, H-10, H-12):
1. H-2: disconfirmed - with 14,806 events and 5.5M person-years a real protective effect at ~1/day should be detectable; the point estimate 0.93 is nominally in H-2's direction but not significant.
2. H-3: disconfirmed on CVD events at up to 1/day.
3. H-4: predicted (null on ischemic endpoints).
4. H-9: this is the single best-fitting observation for H-9 - generally healthy Western adults, exactly up to ~1/day.
5. H-10: predicted, though H-10's scope is broader than these US cohorts so it gains less than H-9.
6. H-12: compatible (a population-average null can hide offsetting subgroups) but unexplanatory.

## Likelihood

```python
# E-21 (HC-2) - lone edge, one observation O-19 "no egg-CVD association up to >=1/day, pooled NHS/NHSII/HPFS,
# 215,618 people, 14,806 events, HR 0.93 with CI crossing 1". Members in HC-2.hypotheses order:
# [H-2 protective, H-3 harmful, H-4 null-IHD/reverse-causation, H-9 null-healthy-Western-<=1/day,
# H-10 null-diverse-global, H-12 residual: direction varies]. Anchored on H-9 = 1 (rule 7a).
# The three null members assert the same direction and differ only by scope rider (strain already logged at
# step 4 - not re-logged); the spread below is driven ENTIRELY by how well each rider matches this study's
# population (US health professionals, ordinary intakes up to ~1/day), not by three separate direction calls.
lik_cvd_H9  = 1.0   # anchor: H-9's scope is generally healthy Western adults up to ~1/day - almost exactly
                    # this study's population and exposure range. The single best-fitting observation for H-9;
                    # a well-powered null here is close to what H-9 predicts outright
lik_cvd_H10 = 0.85  # 0.85x: H-10 also predicts this null, but its content is a null across low-, middle- and
                    # high-income populations; US health professionals are one easy corner of that claim, so
                    # the observation confirms only a fraction of H-10's scope and gains less than H-9
lik_cvd_H4  = 0.8   # 0.8x: H-4 predicts a null too, but is restricted to ischemic heart disease and carries a
                    # reverse-causation rider; this is composite incident CVD, and the mildly inverse point
                    # estimate 0.93 is what H-4 would attribute to reverse causation - consistent but a looser
                    # fit to the stated endpoint than H-9
lik_cvd_H2  = 0.45  # 0.45x: H-2 (protective at ~1/day) is disconfirmed but not excluded. With 5.5M
                    # person-years a real protective effect should have cleared significance; still, HR 0.93
                    # sits in H-2's direction, and H-2's source claim is Chinese-population-specific, where
                    # baseline intake is far lower - so a US null is not fatal to it
lik_cvd_H3  = 0.2   # 0.2x: H-3 predicts higher mortality at >=7/week, most strongly in diabetics. A null at
                    # exactly that intake in the best-powered Western cohort set is the observation H-3 fits
                    # worst. Not lower, because H-3's endpoint is all-cause mortality (not incident CVD) and
                    # its diabetic subgroup is a small slice of these cohorts
lik_cvd_H12 = 0.6   # 0.6x: a direction-varying / J-shaped effect readily produces a flat population average
                    # over the 0-to-1/day range, especially since >1/day is barely sampled here. Middling and
                    # unconstrained (rule 3) - it accommodates the null without predicting it
t_cvd = 0.6         # cap = trust_score of O-19's source S-9 = 0.70. Docked to 0.6 for FFQ exposure
                    # measurement error (attenuates any true association toward the null, i.e. biases in the
                    # direction of the observed result) and healthy-user confounding in a self-selected
                    # health-professional cohort with an unauditable multivariable adjustment pipeline
evidence("HC-2", ["O-19"], [lik_cvd_H2, lik_cvd_H3, lik_cvd_H4, lik_cvd_H9, lik_cvd_H10, lik_cvd_H12], t=t_cvd)
```
