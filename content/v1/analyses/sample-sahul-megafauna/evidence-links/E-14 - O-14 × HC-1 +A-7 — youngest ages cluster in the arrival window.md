---
type: evidence-link
id: E-14
from: "[[O-14 - Youngest reliable ages for 8 of 12 dated genera fall within ~2 kyr of first human occupation]]"
to: "[[HC-1 - Dominant driver of the extinction pulse]]"
arguments:
  - id: A-7
    role: "repeated arrival waves widen the effective colonisation window, raising P(obs | H-3) relative to a single-front reading"
correlated_with:
  - "[[E-22 - O-22 × HC-1 — late survivors postdate the arrival window]]"
---

![[O-14 - Youngest reliable ages for 8 of 12 dated genera fall within ~2 kyr of first human occupation]]

## Why this is evidence

The two human members predict the youngest ages pile up **inside** the arrival window; [[H-21 - Climate-driven aridification drove the extinction]] predicts they track the aridity maximum instead. Between the two human members the pattern is less decisive — [[H-11 - Indirect human impact through burning and habitat transformation drove the extinction]] predicts it slightly better because a habitat squeeze also accommodates the survivor tail (see the correlated edge [[E-22 - O-22 × HC-1 — late survivors postdate the arrival window]]).

## Likelihood

```python
# HC-1 — ONE joint estimate for E-14 + E-22: both observations rest on the same age compilation D-4
# (step 5 flagged them correlated), so the pattern is priced whole — 8/12 genera within ~2 kyr of
# arrival (O-14) AND 3 persisting >5 kyr (O-22). Members in HC-1.hypotheses order. Illustrative.
p_ages_H3 = 0.30    # fits the tight cluster; fits 3 genera surviving 5 kyr of active hunting worst.
                    # Raised from ~0.22 by A-7 (approved): repeated arrival waves widen the window
p_ages_H11 = 0.50   # a habitat squeeze is staggered by construction — most taxa go with the burning
                    # front, refugial taxa persist. Only member predicting both halves of the pattern
p_ages_H21 = 0.10   # aridification predicts the ages track the aridity maximum, not the arrival
                    # window; reproducing this pattern needs a coincidence between the two
p_ages_H42 = 0.20   # unlisted driver: unconstrained, so it neither predicts the pattern nor forbids
                    # it. Lower would assert no unlisted driver could produce it, which I don't know
t_dates = 0.55      # cap = min trust_score over {O-14, O-22} = 0.9 (both via S-1). Docked well below
                    # it: Signor-Lipps truncation and reworked specimens bias youngest ages in
                    # opposite directions, and D-4's screening protocol was never read
evidence("HC-1", ["O-14", "O-22"], [p_ages_H3, p_ages_H11, p_ages_H21, p_ages_H42], t=t_dates)
```
