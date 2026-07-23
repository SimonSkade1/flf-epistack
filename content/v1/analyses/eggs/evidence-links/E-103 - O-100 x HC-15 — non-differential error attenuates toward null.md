---
id: E-103
type: evidence-link
from: "[[O-100 - Non-differential dietary measurement error attenuates diet-disease associations toward the null]]"
to: "[[HC-15 - Whether nutritional-cohort associations can support causal egg-health claims]]"
arguments:
  - "[[A-35 - Non-differential, calibratable dietary error biases against not toward positive findings, so measurement error is correctable rather than fatal]]"
---
![[O-100 - Non-differential dietary measurement error attenuates diet-disease associations toward the null]]

## Why this is evidence
If dietary omission error is non-differential it biases associations toward the null, so an observed positive diet-disease association is an underestimate rather than an artifact. H-41 relies on exactly this to argue measurement error weakens rather than manufactures findings; H-31 disputes the non-differential premise (cf. the BMI-correlated error). Discriminates toward the defence pole.

## Likelihood

```python
# E-103 (HC-15) — lone edge, one observation O-100 "non-differential dietary error attenuates toward the null", so an
# observed positive diet-disease association is an underestimate, not an artifact (defence-supporting). Members in
# HC-15.hypotheses order [H-31 reform; H-41 defence; H-59 residual]. Anchored on H-41 = 1 (best fit); others as ratios
# (rule 7). Condition strictly on H.
lik_nondiff_H41 = 1.0   # anchor: the defence pole relies on exactly this — measurement error weakens rather than
                        # manufactures findings, so error is a bounded/correctable problem
lik_nondiff_H31 = 0.55  # 0.55x: reform disputes the non-differential premise (BMI-correlated error, CG-34). Not much
                        # lower because A-35 (corrected/checked) shows the attenuation guarantee is a theorem only for
                        # DICHOTOMOUS exposures and can fail for the graded per-egg exposures actually modelled —
                        # which blunts how far this fact favours the defence
lik_nondiff_H59 = 0.75  # 0.75x: intermediate — the fact holds in its weaker (usually-attenuating, correctable) form
                        # A-35 endorses, a middling-high fit for real-but-limited causal support
t_nondiff = 0.62        # cap = trust_score(O-100 via S-100) = 0.62; O-100 is a correctly-stated general
                        # measurement-error theorem, no extra raw->observation weakness beyond the source trust
evidence("HC-15", ["O-100"], [lik_nondiff_H31, lik_nondiff_H41, lik_nondiff_H59], t=t_nondiff)
```
