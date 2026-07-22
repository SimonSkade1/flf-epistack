---
id: E-39
type: evidence-link
from: "[[O-33 - Massive white dwarfs with very low magnetic fields and ages from 100 Myr to gigayears are observed]]"
to: "[[HC-4 - Fate of the Earth under a hypothetically stable trapped black hole]]"
arguments:
  - "[[A-49 - Solar-mass white dwarfs provide enough column density to stop cosmic-ray-produced neutral black holes for D up to 7]]"
  - "[[A-50 - Cosmic rays produce thousands of black holes on low-field white dwarfs within tens of millions of years under any composition]]"
  - "[[A-51 - White-dwarf survival excludes every scenario in which Earth accretion would be dangerous - the accretion-time ratio is about 2e4]]"
  - "[[A-53 - No Eddington limit throttles micro-black-hole accretion in Earth, white dwarfs, or neutron stars]]"
---
![[O-33 - Massive white dwarfs with very low magnetic fields and ages from 100 Myr to gigayears are observed]]

## Why this is evidence

H-22 turns on exactly these stars: a stable hole accretes far faster in white-dwarf matter than in Earth, so any configuration that could harm Earth within the solar lifetime would have destroyed cosmic-ray-exposed massive, weakly magnetized white dwarfs well inside their observed cooling ages — their continued existence is what H-22 predicts and what excludes the fast-accretion configurations. Under H-8 (or an H-36 intermediate regime), applying the same accretion physics to holes trapped in these denser stars makes their survival to gigayear ages improbable — a hole radiating or growing dangerously in Earth-density matter does so vastly faster at white-dwarf density. The members therefore predict this observation materially differently; whether H-8's parameter region truly evades the bound is contested in the attached arguments, not here.

## Likelihood

```python
# E-39 (HC-4) — lone edge, one observation O-33 "old low-field massive white dwarfs survive". Members in
# HC-4.hypotheses order [H-8 catastrophic, H-22 negligible, H-36 residual]. This is the STRONGEST H-8 exclusion
# of my three edges and the one that escapes the anthropic shadow: WD survival is an astronomical observation
# not conditioned on terrestrial survival (A-21 family), so unlike Earth/Sun evidence its likelihoods are
# clean. Anchor H-22 = 1 and price the others as ratios to it (rule 7).
lik_wd_H22 = 1.0   # anchor: under negligible growth the dense-star bound holds and these old WDs are exactly
                   # what H-22 predicts survive
lik_wd_H8 = 0.1    # 0.1x as expected as under H-22. A stable hole accretes ~1.9e4x faster in WD matter than
                   # in Earth (A-51, approved), and cosmic rays produce >100 holes on a low-field WD within
                   # 50 Myr even for 100% iron (A-50, approved) with no Eddington throttle (A-53, approved) —
                   # so a catastrophic fast-accretion configuration would have destroyed these >~Gyr stars.
                   # Kept off zero, not lower: A-49 (approved) bounds only D<=7 via WDs (the D>=8 danger region
                   # is stopped by neutron stars, not here), and the A-7/A-8 compact-star gaps already priced
                   # into the prior (Eddington-invisible / sub-M_min holes) let a sliver of H-8 evade this bound
lik_wd_H36 = 0.5   # 0.5x: an intermediate regime is partly caught — the borderline D=7 case (accretion up to
                   # ~80 Myr in WD, A-51) would still disrupt many old WDs — but some H-36 regimes sit in the
                   # D>=8 / gap region WDs cannot reach; unconstrained, so middling, not extreme (rule 3)
t_wd = 0.72        # cap = trust_score of O-33's source S-37 = 0.82. Docked for the ~10% column-density
                   # systematics on mass/age/field (temperature, composition) noted on O-33; A-50's worst-case
                   # (pure Fe) shows production survives that, so only a modest dock. No shadow dock: WD
                   # evidence is not selection-contaminated
evidence("HC-4", ["O-33"], [lik_wd_H8, lik_wd_H22, lik_wd_H36], t=t_wd)
```
