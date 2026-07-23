---
id: E-1
type: evidence-link
from: "[[O-7 - High-egg group reported greater postbreakfast satiety and less hunger despite matched protein]]"
to: "[[HC-13 - Whether eggs enhance satiety beyond their protein content]]"
---
![[O-7 - High-egg group reported greater postbreakfast satiety and less hunger despite matched protein]]

## Why this is evidence
Protein was matched between arms, so H-47 (satiety fully explained by protein/energy) predicts no satiety difference, whereas H-5 (a beyond-protein egg-specific effect) predicts exactly the greater postbreakfast fullness and reduced hunger observed in the high-egg arm. The observation therefore separates the two members and points toward H-5 (subject to the unblinded-rating caveat).

## Likelihood

```python
# E-1 (HC-13) — lone edge, one observation O-7 "greater postbreakfast satiety and less hunger despite MATCHED
# protein" (DIABEGG, unblinded RCT). Members in HC-13.hypotheses order [H-5 beyond-protein egg-specific satiety,
# H-47 satiety fully explained by protein/energy]. EXHAUSTIVE — 2 members, NO residual. Anchored on H-5 = 1
# (rule 7).
lik_sat_H5  = 1.0   # anchor: with protein matched, greater fullness in the high-egg arm is exactly what a
                    # beyond-protein egg-specific channel (food matrix, lipid, slower gastric emptying) predicts.
lik_sat_H47 = 0.45  # ~0.45x the anchor: protein matched, H-47 predicts NO difference, so it must route the
                    # observed difference through an artefact — but for an UNBLINDED, self-reported appetite
                    # outcome the expectation-effect / imperfect-protein-matching artefact the carving flags is
                    # common and easy, so H-47 accommodates the result readily. A single soft subjective outcome
                    # therefore discriminates only weakly.
t_sat = 0.7         # cap = trust_score of O-7's source S-26 = 0.7. At the cap: the unblinded-rating concern is a
                    # DISCRIMINATION issue already priced into lik_sat_H47 (real effect vs expectation artefact),
                    # not a raw-data-reliability defect, so no further dock.
evidence("HC-13", ["O-7"], [lik_sat_H5, lik_sat_H47], t=t_sat)
```
