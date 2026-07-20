---
type: evidence-link
id: E-6
from: "[[O-10 - Habitable-planet formation times span many Gyr and Earth's formation date is unremarkably late]]"
to: "[[HC-4 - Bound on the exogenous terminal-catastrophe rate]]"
arguments:
  - "[[A-7 - Earth's unremarkably late formation time yields a selection-bias-free catastrophe-rate bound near 1 per Gyr]]"
---
![[O-10 - Habitable-planet formation times span many Gyr and Earth's formation date is unremarkably late]]

## Why this is evidence

H-5 predicts Earth's formation date sits typically within the habitable-planet formation-time distribution: with a low exogenous catastrophe rate, observer-selection does not push observers toward early-formed planets. H-10 (a high, unbounded rate) predicts surviving observers should find themselves on anomalously early-formed planets — the later a planet forms, the longer its past light-cone exposure to catastrophe. Earth's unremarkably late formation date is thus expected under H-5 and surprising under H-10.

## Likelihood

```python
# E-6 (HC-4) — lone edge, one observation O-10 "Earth's formation date typical, not anomalous".
# Members in HC-4.hypotheses order: [H-5 bound holds, H-10 not bounded]. Absolute estimation
# (rule 7): "how typical a date do surviving observers see" is a base rate readable off the
# observer-weighted formation-time distribution under each rate regime (A-7, approved).
p_typical_given_H5  = 0.7   # with rate < ~1/Gyr the observer-weighted distribution barely
                            # tilts off the raw one, so a near-typical date is the modal
                            # outcome; not 1.0 — any single planet can still sit in a tail.
p_typical_given_H10 = 0.15  # H-10 spans rates from just-above-1/Gyr to huge. A-7 (approved):
                            # at high rates observers are pushed onto anomalous formation
                            # dates and a typical date has P <~ 0.001; but H-10's marginal
                            # sub-range (~1-3/Gyr) suppresses typicality only mildly. This is
                            # the rate-mixture average, dominated by that marginal sub-range.
t_typ = 0.8                 # = cap: trust_score of O-10's source S-23 (0.8). No extra dock:
                            # validity of the formation-time distribution model is already
                            # priced in HC-4's prior (p_dist_model) — docking t for it too
                            # would double-count the same failure mode.
evidence("HC-4", ["O-10"], [p_typical_given_H5, p_typical_given_H10], t=t_typ)
```
