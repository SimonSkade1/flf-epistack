---
id: E-29
type: evidence-link
from: "[[O-3 - As of 1998 no laboratory or astrophysical constraint excluded a TeV type-I string scale]]"
to: "[[HC-1 - Short-distance structure and fundamental scale of gravity]]"
---
![[O-3 - As of 1998 no laboratory or astrophysical constraint excluded a TeV type-I string scale]]

## Why this is evidence

Survival-style discrimination. If H-2 is true, it is guaranteed that no correct laboratory or astrophysical measurement excludes a TeV fundamental scale — the scenario cannot fail a valid test. If instead H-27 (or a residual H-33 completion with a high fundamental scale) is true, the then-existing precision data — compositeness bounds on contact operators, electroweak measurements, astrophysical energy-loss arguments — had some chance of already contradicting the specific low-scale pattern H-2 requires, since nothing protects a false low-scale hypothesis from exclusion. That H-2 passed every test it could have failed shifts weight toward it, though only weakly: the strongest relevant probe reached far below the string scale in question, so the tests' power was low. H-4 is not addressed by this observation's constraint set either way. Direction: weakly toward H-2, at the expense of H-27 and H-33.

## Likelihood

```python
# E-29 (HC-1) — lone edge, one observation O-3 "as of 1998 no lab/astrophysical constraint excluded a TeV
# type-I string scale". Survival-style discrimination: a true low-scale scenario cannot fail a valid test, a
# false one had some chance of already being excluded. Weak, because 1998 probes had low power — the
# four-electron contact vertex was tested accurately only to ~100 GeV, far below the ~1 TeV string scale.
# Members in HC-1.hypotheses order [H-2, H-4, H-27, H-33]. Anchored on H-2 = 1 (rule 7).
lik_O3_H2  = 1.0   # anchor: if the TeV type-I string scenario is real it CANNOT be excluded by a valid test,
                   # so the 1998 no-exclusion state is guaranteed
lik_O3_H27 = 0.9   # standard gravity: the low-scale pattern is false, but the low-power 1998 data had only a
                   # small chance of already excluding a >1 TeV scale, so no-exclusion is only slightly less
                   # expected than under H-2
lik_O3_H4  = 0.95  # RS1 is not addressed by this TeV-string constraint set either way — near-neutral, set
                   # between the guaranteed-survival anchor and H-27 so the observation barely moves it
lik_O3_H33 = 0.9   # residual (rule 3): a high-scale completion is in H-27's boat (small chance of exclusion),
                   # a low-scale one survives like H-2 — averages to middling, docked at H-27's level
t_O3 = 0.75        # cap = trust_score(S-17, Antoniadis et al. 1998) = 0.88; docked: "no constraint we are
                   # aware of" is the proposers' own survey, which could under-weight constraints they did not consider
evidence("HC-1", ["O-3"], [lik_O3_H2, lik_O3_H4, lik_O3_H27, lik_O3_H33], t=t_O3)
```
