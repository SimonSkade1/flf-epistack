---
id: E-42
type: evidence-link
from: "[[O-22 - Earth, Sun, white dwarfs, neutron stars and the stars at large have survived billions of years of cosmic-ray bombardment]]"
to: "[[HC-4 - Fate of the Earth under a hypothetically stable trapped black hole]]"
arguments:
  - "[[A-24 - Nature has already run the LHC collision programme 1e31 times on bodies that still exist, bounding any collider disaster mechanism]]"
  - "[[A-25 - Cosmic-ray collisions would already have nucleated any vacuum bubble the LHC could - and a bubble expands regardless of production frame]]"
  - "[[A-26 - Dangerous magnetic monopoles are excluded - GUT monopoles are far too heavy for the LHC, and cosmic-ray-produced ones would have stopped in Earth harmlessly]]"
  - "[[A-29 - Stable black holes from cosmic rays would be charged, stop in Earth or Sun, and accumulate in billions - the absence of any effect excludes the scenario]]"
  - "[[A-30 - Even hypothetically stable neutral black holes would have destroyed observed white dwarfs and neutron stars - their survival closes the last case]]"
  - "[[A-33 - Interstellar heavy-ion collisions would have seeded stars with strangelets - the absence of strangelet-triggered stellar explosions bounds the danger with no velocity assumption]]"
---
![[O-22 - Earth, Sun, white dwarfs, neutron stars and the stars at large have survived billions of years of cosmic-ray bombardment]]

## Why this is evidence

The survival half of the cosmic-ray argument as it bears on the trapped-hole fate: if stable holes with H-8-style dangerous accretion were produced by cosmic rays and stopped in dense stars, the exposed populations would show destroyed stars or astrophysical black holes that conventional astrophysics cannot account for — neither is observed. H-22 predicts exactly this quiet sky; H-8 and sub-solar-lifetime H-36 variants make it improbable. The extra content beyond the specific compact-star observations is the absence of any anomalous or unexplained black-hole population among the exposed stars.

## Likelihood

```python
# E-42 (HC-4) — lone edge, one observation O-22 "exposed astronomical bodies persist with no anomalies".
# Members in HC-4.hypotheses order [H-8 catastrophic, H-22 negligible, H-36 residual]. Broad LSAG survival
# statement whose discriminating content here is the compact-star survival PLUS the absence of any anomalous
# black-hole population conventional astrophysics cannot explain. The compact-star / population content
# escapes the anthropic shadow (A-30, approved: neutral holes would destroy observed WD/NS; A-29, approved:
# charged holes accumulate in Earth/Sun), but the observation also bundles the shadow-contaminated Earth/Sun
# survival, and is qualitative where E-39 is a specific quantitative WD bound — so a shade weaker than E-39.
# Anchor H-22 = 1 (rule 7).
lik_cr_H22 = 1.0   # anchor: negligible growth predicts exactly this quiet sky — surviving stars, no
                   # unexplained black-hole population
lik_cr_H8 = 0.15   # 0.15x as expected as under H-22: cosmic-ray-produced dangerous stable holes would have
                   # left destroyed dense stars or an anomalous BH population (A-29/A-30, approved); their
                   # absence is improbable under catastrophic accretion. Slightly above E-39's 0.1 because the
                   # statement is broad/qualitative and its Earth-Sun component is shadow-softened, so it
                   # discriminates a touch less sharply than the direct WD bound
lik_cr_H36 = 0.55  # 0.55x: an intermediate regime could evade the highly-visible-destruction signature while
                   # still being dangerous on long timescales; unconstrained, middling (rule 3)
t_cr = 0.68        # cap = trust_score of O-22's source S-1 (LSAG) = 0.82. Docked more than E-39: this is a
                   # qualitative review-level summary that bundles the anthropic-contaminated Earth/Sun
                   # survival with the clean compact-star/population content, so the raw-data-to-observation
                   # step is looser
evidence("HC-4", ["O-22"], [lik_cr_H8, lik_cr_H22, lik_cr_H36], t=t_cr)
```
