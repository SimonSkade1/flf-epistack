---
id: E-31
type: evidence-link
from: "[[O-39 - Cosmic-ray data imply 1e28 iron-iron collisions at AGS-equivalent energies on the Moon and 1e47 in our past light cone]]"
to: "[[HC-8 - Runaway growth of a stopped negative strangelet]]"
arguments:
  - "[[A-55 - 1e47 comparable cosmic-ray collisions in our past light cone bound a RHIC-triggered vacuum transition below 2e-36]]"
  - "[[A-59 - Lunar persistence bounds dangerous strangelet production at p below 2e-11 - unless production is confined to exactly central rapidity]]"
  - "[[A-60 - Strangelets born in interstellar space would convert stars in supernova-like events - the observed supernova rate bounds RHIC danger below 2e-8, tightening to 1e-21 - unless strangelets are metastable]]"
---
![[O-39 - Cosmic-ray data imply 1e28 iron-iron collisions at AGS-equivalent energies on the Moon and 1e47 in our past light cone]]

## Why this is evidence

Not diagnostic as a bare flux fact — both members predict the same cosmic-ray record. What discriminates is the conjunction the observation makes precise: an enormous count of heavy-ion collisions capable of leaving near-rest products (lunar Fe-Fe at AGS-equivalent energies; interstellar collisions with all CM-velocity components small) has coexisted with the Moon and the stars remaining ordinary matter. Under H-29 every such collision was a trial that, on producing a stoppable negative strangelet, ends in runaway conversion of the host body — so the larger the exposure, the more improbable the ordinary-matter outcome we in fact observe. Under H-40 the exposure count carries no such tension. Direction: toward H-40, with strength scaling with the per-collision production-and-stopping probability (the rapidity-suppression and metastability escapes are the attached arguments' subject).

## Likelihood

```python
# E-31 (HC-8) — lone edge, one observation O-39 "cosmic-ray exposure counts: ~1e28 lunar Fe-Fe at
# AGS-equivalent energies, interstellar at-rest Fe-Fe rate, ~1e47 in the past light cone". Members in
# HC-8.hypotheses order [H-29 runaway, H-40 no-runaway], no residual. As a bare flux fact O-39 is
# non-diagnostic (both members predict the same cosmic-ray record); it discriminates only as the TRIAL
# COUNT underlying the persistence bounds. Anchor H-40 = 1 (rule 7). Deliberately WEAK to avoid
# triple-counting: the persistence force is already priced through E-30 (lunar) and E-32 (stellar) —
# this edge's honest own increment is only that N is enormous and well-measured, plus the light-cone scale.
lik_counts_H40 = 1.0  # anchor: the exposure record is exactly as observed under no-runaway
lik_counts_H29 = 0.5  # 0.5x: under runaway a larger measured N sharpens how improbable the observed
                      # ordinary-matter outcome is (A-59 lunar p<2e-11; A-60 approved, interstellar->stellar
                      # supernova bound 2e-8 tightening to ~1e-21). But those bounds' persistence content
                      # lives on O-23 / O-22 (priced in E-30 / E-32); O-39 supplies only the count, so its
                      # marginal HC-8 decrement beyond them is modest — kept near 1. A-55 (corrected) is
                      # light-cone VACUUM decay (O-40), a different cluster, so it adds nothing to HC-8 here.
t_counts = 0.75       # cap = trust_score(O-39 source S-3) = 0.85; docked to 0.75 because O-39 is a DERIVED
                      # quantity — fluxes folded with lunar Fe abundance (Apollo f_Fe=0.012), geometric
                      # cross sections, and Hut-Rees light-cone integration — a pipeline with real
                      # extrapolation, though order-of-magnitude and conservative
evidence("HC-8", ["O-39"], [lik_counts_H29, lik_counts_H40], t=t_counts)
```
