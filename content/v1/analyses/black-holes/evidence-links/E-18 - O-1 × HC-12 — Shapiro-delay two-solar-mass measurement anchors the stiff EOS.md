---
id: E-18
type: evidence-link
from: "[[O-1 - PSR J1614-2230 pulsar mass measured at 1.97 solar masses via Shapiro delay]]"
to: "[[HC-12 - Stiffness of the cold supranuclear equation of state]]"
arguments:
  - "[[A-13 - A measured 1.97-solar-mass neutron star bounds the maximum density of cold matter at about 4e15 g per cm3]]"
---
![[O-1 - PSR J1614-2230 pulsar mass measured at 1.97 solar masses via Shapiro delay]]

## Why this is evidence

H-1 (stiff EOS) predicts neutron stars up to and beyond this mass exist and will eventually be found; H-44 (softened by exotic degrees of freedom) predicts a lower maximum mass, so a precisely measured pulsar at this mass should not exist. The measurement rests only on general-relativistic orbital dynamics (the HC-13 dependency), not on neutron-star structure models, so within GR it directly separates the two members.

## Likelihood

```python
# E-18 (HC-12) — lone edge, one observation O-1 "PSR J1614-2230 = 1.97 Msun via Shapiro delay". Members in
# HC-12.hypotheses order: [H-1 stiff EOS, H-44 softened by exotic dof]. No residual
# (exhaustive_by_construction). The mass rests only on GR orbital dynamics, not on NS structure models, so
# within GR it separates the members cleanly (the HC-13 dependency is noted at cluster level, not repriced
# in t here). Anchored on H-1 = 1 (rule 7).
lik_o1_H1  = 1.0    # anchor: a stiff EOS expects neutron stars at and beyond 1.97 Msun, so this measurement
                    # is exactly what H-1 predicts
lik_o1_H44 = 0.27   # ratio to H-1: exotic softening pulls the maximum mass down. A-13 (approved) shows
                    # 1.97 Msun excludes every EOS with Mmax below it and rules out the soft
                    # hyperon/kaon-condensate models (GS1, GM3), so most softened EOSs cannot produce this
                    # star at all. Not zero: A-13 notes some strange-quark-matter models survive and
                    # repulsive-interaction hyperonic EOSs can still reach ~2 Msun (cf. the prior's
                    # p_stiff_if_exotic ~ 0.25)
t_o1 = 0.9          # cap = trust_score(S-66) = 0.9. Shapiro delay involves essentially no astrophysical
                    # model assumptions (high significance, dense-campaign timing, MCMC error analysis), so
                    # there is no data-to-observation weakness to dock for; t at the cap
evidence("HC-12", ["O-1"], [lik_o1_H1, lik_o1_H44], t=t_o1)
```
