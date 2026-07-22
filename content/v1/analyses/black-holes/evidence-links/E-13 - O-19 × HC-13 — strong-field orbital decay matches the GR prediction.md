---
id: E-13
type: evidence-link
from: "[[O-19 - PSR J0348+0432 orbital decay matches the general-relativistic gravitational-wave prediction]]"
to: "[[HC-13 - Validity of general relativity in the strong-field regime]]"
arguments:
  - "[[A-22 - Orbital-decay agreement with GR excludes dipolar radiation and significant strong-field deviations for 2-solar-mass neutron stars]]"
---
![[O-19 - PSR J0348+0432 orbital decay matches the general-relativistic gravitational-wave prediction]]

## Why this is evidence

H-13 predicts Pb-dot(obs)/Pb-dot(GR) consistent with unity in this system; H-45's flagged deviation channels — dipolar gravitational radiation or scalarization from long-range extra fields — would generically add an extra energy-loss term, pushing the ratio away from unity, and this system probes roughly twice the fractional gravitational binding energy of any previously tested binary, so the deviation regime H-45 posits is directly sampled rather than extrapolated to. The residual insensitivity noted on the cluster (a deviation the orbital-decay test happens not to see) is the caveat, not the prediction — the members still predict this measurement materially differently.

## Likelihood

```python
# E-13 (HC-13) — lone edge, one observation O-19 "PSR J0348+0432 orbital decay matches the GR prediction".
# Members in HC-13.hypotheses order: [H-13 GR valid, H-45 GR fails]. No residual
# (exhaustive_by_construction). Anchored on H-13 = 1 (rule 7).
lik_o19_H13 = 1.0   # anchor: GR valid predicts Pb-dot(obs)/Pb-dot(GR) consistent with unity; the measured
                    # 1.05 +/- 0.18 is exactly that
lik_o19_H45 = 0.2   # ratio to H-13: given GR fails in this regime, deviation channels (dipolar radiation,
                    # scalarization) generically add an energy-loss term pushing the ratio off unity. A-22
                    # (approved) turns this agreement into |alpha_PSR - alpha_0| < 0.005, excluding
                    # significant strong-field scalarization in exactly the ~2x-binding-energy regime H-45
                    # posits (directly sampled, not extrapolated). Not crushed to zero: A-22's own scope
                    # leaves short-range fields (mass > ~1e-19 eV/c^2) and other channels this orbital-decay
                    # test happens not to see, so some realizations of H-45 still reproduce this measurement
t_o19 = 0.92        # cap = trust_score(S-80) = 0.92. No specific weakness in the timing-data -> observation
                    # step (kinematic correction negligible, mass-loss and tidal contaminants excluded, decay
                    # stable with no higher derivatives), so t sits at the cap
evidence("HC-13", ["O-19"], [lik_o19_H13, lik_o19_H45], t=t_o19)
```
