---
type: evidence-link
id: E-31
from: "[[O-31 - The interior aridity maximum postdates the first-occupation window by several kyr]]"
to: "[[HC-1 - Dominant driver of the extinction pulse]]"
correlated_with: []
---

![[O-31 - The interior aridity maximum postdates the first-occupation window by several kyr]]

## Why this is evidence

Direct timing test of [[H-21 - Climate-driven aridification drove the extinction]]: if aridity drove the pulse, its maximum should coincide with the extinction window. It postdates it by several kyr, so this observation lowers the climate member and mildly favours every other member. Independent of the dating pair — it rests on the speleothem instrument [[D-7 - Speleothem oxygen-isotope instrument record (S-5)]], not the D-4 compilation (`correlated_with: []`), so it is a genuinely separate likelihood factor.

## Likelihood

```python
# HC-1 — O-31: the interior aridity maximum postdates the first-occupation window. Independent basis
# D-7 (its own speleothem instrument), so a separate factor from the E-14/E-22 dating pair. Members
# in HC-1.hypotheses order. Illustrative and uncalibrated.
p_arid_H3 = 0.50    # predation is indifferent to aridity timing; a mismatch is unsurprising under it
p_arid_H11 = 0.50   # indirect human impact likewise does not require aridity to coincide
p_arid_H21 = 0.12   # climate-as-driver predicts the aridity maximum lands ON the pulse; a several-kyr
                    # lag is what you would NOT expect if aridity did the work — the discriminating value
p_arid_H42 = 0.35   # unlisted driver: unconstrained on aridity timing, so middling
t_arid = 0.45       # cap = trust_score(S-5) = 0.85. Docked hard: one cave, one growth axis, and the
                    # δ18O age model still leans on D-4, so "several kyr" carries real dating slop
evidence("HC-1", ["O-31"], [p_arid_H3, p_arid_H11, p_arid_H21, p_arid_H42], t=t_arid)
```
