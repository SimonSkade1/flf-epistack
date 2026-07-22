---
id: E-12
type: evidence-link
from: "[[O-40 - No vacuum-decay transition has occurred anywhere in our past light cone]]"
to: "[[HC-10 - Stability status of the electroweak vacuum]]"
arguments:
  - "[[A-55 - 1e47 comparable cosmic-ray collisions in our past light cone bound a RHIC-triggered vacuum transition below 2e-36]]"
---
![[O-40 - No vacuum-decay transition has occurred anywhere in our past light cone]]

## Why this is evidence
H-42 predicts this with certainty — no channel, no decay, ever. H-31 predicts it only with probability short of certainty, and the shortfall grows the faster the nucleation rate: survival of our whole past light cone rules out the rapid-decay corner of the false-vacuum possibility while leaving the long-lifetime metastable regime essentially untouched. (Observer-selection caveats on this survival evidence are handled at the argument layer.)

## Likelihood

```python
# E-12 (HC-10) — lone edge, one observation O-40 "no vacuum-decay transition in our past light cone".
# Members in HC-10.hypotheses order: [H-31 metastable false vacuum, H-42 exactly stable]. No residual
# (exhaustive_by_construction). A-63/A-64 are no-observation arguments already priced into the prior — not
# re-counted here (rule 5). Anchored on H-42 = 1 (rule 7). What this edge prices is almost entirely the
# observation-selection caveat A-55 (corrected) attaches to O-40, with A-25 supplying the light-cone step.
lik_o40_H42 = 1.0   # anchor: exact stability => no decay channel ever => past-light-cone survival is
                    # guaranteed, P(O-40 | H-42) = 1
lik_o40_H31 = 0.9   # ratio to H-42: metastability still predicts survival with near-certainty across its
                    # long-lifetime bulk — survival of ~1e47 comparable Fe-Fe collisions (A-25's light-cone /
                    # frame-independence step: a bubble expands at light speed whatever the production frame)
                    # only suppresses the rapid-nucleation corner, so the observation mildly favours H-42.
                    # Kept near 1, not lower, because A-55 (corrected) notes the anthropic shadow pushes
                    # P(O-40 | H-31, we observe) back toward 1 — a decay-destroys-all-observers catastrophe
                    # is seen as "survived" by every surviving observer regardless of the nucleation rate
t_lc = 0.3          # cap = trust_score(S-3) = 0.85. Docked hard for observation selection: A-55 (corrected)
                    # states past-light-cone survival is a biased witness of the stability split — every
                    # possible observer sees O-40 whatever p-bar — so the unbiased 2e-36 bound is set aside
                    # and only a far weaker selection-aware bound survives; this edge should barely move the
                    # prior. The markdown IS the price of the selection effect A-55 directs step 8 to charge
evidence("HC-10", ["O-40"], [lik_o40_H31, lik_o40_H42], t=t_lc)
```
