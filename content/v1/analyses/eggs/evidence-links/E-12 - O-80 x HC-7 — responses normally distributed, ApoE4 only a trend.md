---
id: E-12
type: evidence-link
from: "[[O-80 - Individual cholesterol responsiveness varied widely, appeared normally distributed, and was mostly positive; ApoE4 only a non-significant trend]]"
to: "[[HC-7 - Nature of inter-individual variation in cholesterol response to dietary cholesterol]]"
---
![[O-80 - Individual cholesterol responsiveness varied widely, appeared normally distributed, and was mostly positive; ApoE4 only a non-significant trend]]

## Why this is evidence
A wide, approximately normal (unimodal) spread of responses is H-35's signature and argues against H-1's discrete bimodal split. The ApoE4 effect being only a non-significant trend supports H-36 (ApoE does not by itself tag hyper-responders) against a reading of H-55 in which ApoE is the dominant genetic determinant.

## Likelihood

```python
# E-12 (HC-7) — lone edge, one observation O-80: individual cholesterol responsiveness varied widely,
# appeared ~normally (unimodally) distributed, mostly positive, with ApoE4 only a non-significant trend
# (S-42, Ginsberg 1994, n=20). Members in HC-7.hypotheses order [H-1, H-2, H-35, H-36, H-55]. Anchored on
# H-35 = 1.0 (its signature).
lik_ginsberg_H35 = 1.0   # anchor: "responsiveness varied but appeared normally distributed" is H-35's exact
                         # signature — a continuous, unimodal spread
lik_ginsberg_H1 = 0.35   # 0.35x: a unimodal ~normal spread argues against a discrete bimodal hypo/hyper
                         # split; not crushed because n=20 has little power to exclude a subtly bimodal shape
lik_ginsberg_H2 = 0.6    # 0.6x: H-2 is agnostic on distributional form, but a feedback mechanism with
                         # variable set-points naturally yields a continuous spread, so mildly compatible; it
                         # predicts neither the normal shape nor the ApoE null specifically
lik_ginsberg_H36 = 0.7   # 0.7x: the ApoE4 effect being only a non-significant trend directly matches H-36
                         # (ApoE does not by itself tag responders); below H-35 because the main normal-
                         # distribution finding is neutral for H-36
lik_ginsberg_H55 = 0.45  # 0.45x: residual real but below middling — its "ApoE is the dominant genetic
                         # determinant" sub-reading is argued against by the null ApoE trend, and "mostly
                         # positive" cuts against a pure-noise reading; a different determinant stays neutral
t_ginsberg = 0.8         # cap = trust_score(S-42) = 0.82; docked slightly: "appeared normally distributed"
                         # is a qualitative/visual read at n=20 with no formal modality test reported
evidence("HC-7", ["O-80"], [lik_ginsberg_H1, lik_ginsberg_H2, lik_ginsberg_H35, lik_ginsberg_H36, lik_ginsberg_H55], t=t_ginsberg)
```
