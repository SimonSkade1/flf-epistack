---
id: E-2
type: evidence-link
from: "[[O-42 - Fifteen years of searches found no stable strange matter - terrestrial isotope, astrophysical, and AGS-SPS accelerator searches all null]]"
to: "[[HC-7 - Stability of bulk strange quark matter]]"
arguments:
  - "[[A-58 - Coalescence and thermal production models bound dangerous strangelet yield near 1e-46 per collision, peaking below AGS energies rather than at RHIC]]"
---
![[O-42 - Fifteen years of searches found no stable strange matter - terrestrial isotope, astrophysical, and AGS-SPS accelerator searches all null]]

## Why this is evidence

H-28 (stable bulk strange matter) makes positives plausible on all three fronts: stable strangelets seeded in terrestrial matter would show up as ultraheavy isotopes of normal elements, stable strange matter would permit quark stars with astrophysical signatures (e.g. sub-millisecond pulsars), and heavy-ion collisions could yield detectable strangelets. H-39 predicts every one of these searches comes up null. The uniform nulls are therefore more probable under H-39 — though not decisively, since H-28 is compatible with the nulls if formation or delivery mechanisms are absent (a stable ground state nobody has occasion to reach).

## Likelihood

```python
# E-2 (HC-7) — lone edge, one observation O-42 "fifteen years of null strange-matter searches: terrestrial
# ultraheavy-isotope, astrophysical (no sub-ms pulsar/quark star), and AGS-SPS accelerator, all null".
# Members in HC-7.hypotheses order [H-28 stable in bulk, H-39 not stable]; exhaustive, no residual.
# Anchored on H-39 = 1 (rule 7): the null is essentially certain if strange matter is not stable, so it is
# the clean unit; H-28 priced as "how expected is this uniform null if bulk strange matter WERE stable".
# NOTE the no-observation arguments A-56, A-65 are already in HC-7's prior — not re-used here. This edge
# rests on the terrestrial + astrophysical absences (distinct from E-3's RHIC/STAR collision null), so the
# discrimination is leaned on those fronts, not on the collision-production front E-3 carries (rule: don't
# re-use the same underlying absence twice).
lik_strange_H39 = 1.0   # anchor: if strange matter is not the ground state (H-39), every one of these
                        # searches is predicted null — essentially certain.
lik_strange_H28 = 0.4   # 0.4× vs anchor: the sharpest discriminator is the terrestrial ultraheavy-isotope
                        # null — under H-28 a stable light strangelet seeded in terrestrial matter would
                        # masquerade as an anomalously heavy isotope (Blackman-Jaffe), so the strong limits
                        # are somewhat surprising; the astrophysical null (no quark-star/sub-ms-pulsar
                        # signature) adds. Not driven low: H-28 survives if no natural formation/delivery
                        # path exists (a ground state nobody reaches). A-58 (approved) bounds accelerator
                        # yield ~1e-46/collision, so the AGS-SPS portion of the null is expected even under
                        # H-28 — that front carries little weight, which is why the ratio stays well above 0.
t_strange = 0.8         # cap = trust_score of O-42's source S-3 = 0.85. Docked slightly: the observation is
                        # a review's compilation of many heterogeneous searches (terrestrial, astrophysical,
                        # accelerator) whose individual sensitivity/limit claims were not independently
                        # audited here — an aggregation step below the reliability of a single dataset.
evidence("HC-7", ["O-42"], [lik_strange_H28, lik_strange_H39], t=t_strange)
```
