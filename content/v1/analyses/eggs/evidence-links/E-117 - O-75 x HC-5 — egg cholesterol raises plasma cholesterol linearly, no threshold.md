---
id: E-117
type: evidence-link
from: "[[O-75 - Fasting total cholesterol rose 1.47 mg-dL per 100 mg dietary cholesterol across a 0-4 egg-day crossover (linear, no threshold)]]"
to: "[[HC-5 - Operative exposure behind the egg-cardiovascular association]]"
---
![[O-75 - Fasting total cholesterol rose 1.47 mg-dL per 100 mg dietary cholesterol across a 0-4 egg-day crossover (linear, no threshold)]]

## Why this is evidence
Feeding 0-4 eggs/day raises total cholesterol linearly with the cholesterol dose and no threshold: egg's cholesterol content is a real graded lever on the biomarker (H-26). This argues against H-54's non-cholesterol component and, at the population-mean level, tempers H-3's homeostatic-buffering emphasis (O-1).

## Likelihood

```python
# E-117 (HC-5) — lone edge, one observation O-75 "linear no-threshold plasma-cholesterol dose-response to egg
# cholesterol". Members in HC-5.hypotheses order [H-3 fat-quality, H-26 dietary-cholesterol, H-54 residual]. In
# a 20-man 8-week 0/1/2/4 egg/day crossover, fasting total cholesterol rose 1.47 mg/dL per 100 mg dietary
# cholesterol, linearly with no threshold — egg cholesterol is a real graded lever on the biomarker.
# Anchored on H-26 = 1.0.
lik_dose_H26 = 1.0  # anchor: a clean linear, no-threshold dose-response of plasma cholesterol to egg cholesterol
                    # is H-26's graded-lever signature.
lik_dose_H3 = 0.65  # 0.65x: H-3 grants cholesterol a real but MINOR lever, and 1.47 mg/dL per 100 mg is a modest
                    # slope (~+11 mg/dL at the 858 mg/day top dose), compatible with H-3 — but a population-mean
                    # linear rise with no threshold tempers H-3's homeostatic-buffering emphasis (cf O-1),
                    # a mild tilt to H-26.
lik_dose_H54 = 0.6  # 0.6x: a graded biomarker response is basic physiology, near-neutral for H-54's artefact
                    # branch (this is an RCT, no confounding to null), while mildly against the non-cholesterol
                    # branch since egg cholesterol demonstrably moves the biomarker itself.
t_dose = 0.82       # cap = trust of O-75's source S-42 (Ginsberg 1994) = 0.82. Held at cap: a within-subject
                    # crossover with a verified design (step-2a correction) and P<0.001; small n=20 is offset by
                    # the efficient crossover, no raw-data->observation weakness.
evidence("HC-5", ["O-75"], [lik_dose_H3, lik_dose_H26, lik_dose_H54], t=t_dose)
```
