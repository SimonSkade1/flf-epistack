---
type: correlation-group
id: CG-21
to: "[[HC-6 - Effect of egg-egg-cholesterol intake on the atherogenic blood-lipid profile]]"
members:
  - "[[E-21 - O-75 x HC-6 — TC rose 1.47 mg-dL per 100 mg cholesterol, linear]]"
  - "[[E-22 - O-76 x HC-6 — LDL rose 1.38 mg-dL per 100 mg cholesterol]]"
  - "[[E-23 - O-77 x HC-6 — no HDL-TG dose response to dietary cholesterol]]"
  - "[[E-24 - O-78 x HC-6 — apoB rose ~10% across 0-4 egg diets]]"
  - "[[E-25 - O-80 x HC-6 — cholesterol responsiveness wide but mostly positive]]"
---

Joint likelihood for correlated observations O-75, O-76, O-77, O-78, O-80 (shared basis: D-22). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-21 (HC-6) — ONE joint estimate over O-75 + O-76 + O-77 + O-78 + O-80, all from Ginsberg 1994 (S-42,
# shared basis D-22), rule 1. Pattern whole: an 0/1/2/4-egg crossover in healthy young men gave a linear
# fasting rise of TC (+1.47/100mg) and LDL (+1.38/100mg, P<0.001) with NO HDL/TG dose response, apoB up
# ~10%, and responsiveness wide, normally distributed, mostly positive. Members in HC-6.hypotheses order
# [H-20, H-34, H-40, H-53]. Anchored on H-34 (rule 7): this IS its definition — a linear ~1.4-1.5/100mg
# absolute rise borne by LDL/apoB, not HDL.
lik_ginsberg_H34 = 1.0    # anchor: the linear dose-response + apoB rise + HDL-flat is H-34's exact
                          # fingerprint. A-27 (approved): the parallel ~10% apoB rise means added particles
                          # (atherogenic particle number), the specific H-34 claim
lik_ginsberg_H40 = 0.12   # 0.12×: strongly against — LDL rose (not preserved), HDL flat (not up), and the
                          # mostly-positive spread INCLUDING high responders contradicts H-40's "neutral
                          # even in hyper-absorbers" (E-25). Not near-zero: Ginsberg's non-CRD background
                          # sits outside H-40's carb-restricted scope, its only defence
lik_ginsberg_H20 = 0.3    # 0.3×: H-20 is on the same "raises atherogenic lipids" side but claims only a
                          # comparator-relative effect with LDL falling absolutely — a clean absolute linear
                          # rise is against that specific "no absolute rise" claim, though H-20 doesn't
                          # forbid a dose-response in a different (healthy, high-dose) population
lik_ginsberg_H53 = 0.35   # 0.35×: unlisted effect — the apoB rise specifically argues against an H-53
                          # particle-quality-ONLY effect that would leave apoB flat (E-24), so its most
                          # prominent flavour is disfavoured; middling overall (rule 3)
t_ginsberg = 0.8          # cap = min trust over the five obs = S-42 = 0.82; docked a hair for n=20 making
                          # O-80's distributional shape and the exact slopes less certain. Core effects are
                          # P<0.001 and robust, so near cap
evidence("HC-6", ["O-75", "O-76", "O-77", "O-78", "O-80"], [lik_ginsberg_H20, lik_ginsberg_H34, lik_ginsberg_H40, lik_ginsberg_H53], t=t_ginsberg)
```
