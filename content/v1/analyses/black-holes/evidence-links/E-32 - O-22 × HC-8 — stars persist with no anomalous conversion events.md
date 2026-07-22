---
id: E-32
type: evidence-link
from: "[[O-22 - Earth, Sun, white dwarfs, neutron stars and the stars at large have survived billions of years of cosmic-ray bombardment]]"
to: "[[HC-8 - Runaway growth of a stopped negative strangelet]]"
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

H-29 predicts that (meta)stable negative strangelets produced at rest in interstellar cosmic-ray collisions — where no stopping is needed, closing the lunar bound's rapidity loophole — would be swept into forming stars and trigger runaway conversion, appearing as anomalous supernova-like events well above the observed rate; the stellar population persisting for gigayears with all large-scale phenomena conventionally accounted for is then improbable to the degree such production ever occurred. H-40 predicts persistence unconditionally: a seeded star just carries an inert strangelet. Direction: toward H-40; the metastability window (decay in space, stability after stopping) is the escape the attached arguments price, not the observation.

## Likelihood

```python
# E-32 (HC-8) — lone edge, one observation O-22 "Earth, Sun, white dwarfs, neutron stars and the stars at
# large persist after Gyr of cosmic-ray bombardment". Members in HC-8.hypotheses order [H-29 runaway,
# H-40 no-runaway], no residual. Conditioning as in E-30. Its distinctive discrimination for HC-8:
# interstellar cosmic-ray collisions produce strangelets AT REST (no stopping needed), closing the lunar
# bound's rapidity loophole; under H-29 such strangelets swept into forming stars trigger runaway
# conversion -> anomalous supernova-like events above the observed rate. Anchor H-40 = 1 (rule 7).
lik_stars_H40 = 1.0   # anchor: under no-runaway a seeded star just carries an inert strangelet and
                      # persists — the stellar population is observed with certainty
lik_stars_H29 = 0.1   # 0.10x, the STRONGEST decrement of the three: A-33 (approved) makes the bound
                      # velocity-assumption-free (production at rest in space), and A-60 (approved) prices
                      # the supernova-rate bound at 2e-8, tightening to ~1e-21 with Fe/AGS physics. Its sole
                      # escape is metastability (decay between ~1e-7 s and the Myr of star formation) — a
                      # loophole DISJOINT from E-30's rapidity loophole, so this edge's own increment is
                      # closing the rapidity escape, legitimately multiplied against E-30 rather than
                      # re-counting the shared chain. (WD/NS args A-29/A-30 concern black holes, not the
                      # strangelet cluster — excluded here.)
t_stars = 0.82        # cap = trust_score(O-22 source S-1) = 0.82; stellar / Sun / WD / NS persistence is an
                      # uncontested background fact with no selection/dating weakness — held at the cap
evidence("HC-8", ["O-22"], [lik_stars_H29, lik_stars_H40], t=t_stars)
```
