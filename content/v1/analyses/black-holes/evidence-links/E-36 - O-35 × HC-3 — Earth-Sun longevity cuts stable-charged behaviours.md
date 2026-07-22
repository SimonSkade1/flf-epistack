---
id: E-36
type: evidence-link
from: "[[O-35 - Earth and Sun have existed for about 4.5 billion years and the Sun has about 5 billion years remaining]]"
to: "[[HC-3 - Nature and decay of an LHC-produced strong-gravity object]]"
arguments:
  - "[[A-45 - Charged stable black holes would stop in Earth or the Sun, so their multi-billion-year survival excludes that scenario]]"
  - "[[A-46 - Neutral cosmic-ray-produced black holes punch through Earth and Sun, voiding the naive cosmic-ray safety argument]]"
---
![[O-35 - Earth and Sun have existed for about 4.5 billion years and the Sun has about 5 billion years remaining]]

## Why this is evidence

This observation splits the space of stable behaviours: a stable hole retaining electric or color charge would stop in ordinary matter, so charged-stable variants — which live in the residual H-35, since H-24 is defined as neutral — predict Earth/Sun destruction over 4.5 Gyr of cosmic-ray exposure and are disfavored by their survival. H-24 evades it by construction (neutral relativistic holes pass through Earth and Sun without stopping), and prompt-decay members H-10 and H-14 predict survival trivially. So the observation discriminates the charged-stable region of H-35 against every other member, while leaving H-24 untouched — the asymmetry that pushes the surviving stability question onto the neutral case.

## Likelihood

```python
# E-36 (HC-3) — lone edge, one observation O-35 "Earth & Sun survive ~4.5 Gyr". batch-5 prices the
# white-dwarf / neutron-star survival edges (the NEUTRAL-stable corner, H-24); this edge adds ONLY what
# Earth/Sun longevity contributes, which per `## Why this is evidence` is the CHARGED-stable exclusion.
# A-45 (approved): a charge-retaining stable hole stops in Earth (<~7 TeV) and the Sun (>100 TeV) and would
# accrete — 4.5 Gyr of cosmic-ray implantation would have destroyed both. A-46 (approved): neutral holes
# punch through Earth/Sun, so this observation carries NO information about neutral variants. Hence every
# listed member — H-7 metastable (decays in ms–yr, never accumulates), H-10/H-14 prompt-decay, H-24 neutral
# by construction — predicts survival trivially: anchor them all at 1 (rule 7). Only the residual H-35 is
# docked, for the fraction of its unlisted-behaviour space that is charged-and-stable, which Earth/Sun
# survival excludes — the sole member this edge moves.
lik_surv_H7  = 1.0   # metastable microcanonical hole is not a persistent charged accretor — survival trivial
lik_surv_H10 = 1.0   # anchor: prompt canonical decay, nothing to accrete — survival trivial
lik_surv_H14 = 1.0   # prompt near-threshold decay — survival trivial
lik_surv_H24 = 1.0   # neutral by construction; A-46: neutral holes traverse Earth/Sun, untouched by this datum
p_surv_given_H35 = 0.7  # unlisted behaviour, unconstrained; ~30% of its space is charged-stable-and-Earth-
                        # destructive (A-45), which 4.5-Gyr survival excludes — middling dock, not extreme (rule 3)
t_surv = 0.82        # cap = trust_score of O-35's source S-37 = 0.82; Earth/Sun age is a rock-solid,
                     # generally-known datum, so no dock below the cap (rule 4)
evidence("HC-3", ["O-35"], [lik_surv_H7, lik_surv_H10, lik_surv_H14, lik_surv_H24, p_surv_given_H35], t=t_surv)
```
