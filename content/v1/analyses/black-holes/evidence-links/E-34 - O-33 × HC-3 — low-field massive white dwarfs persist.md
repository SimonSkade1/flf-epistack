---
id: E-34
type: evidence-link
from: "[[O-33 - Massive white dwarfs with very low magnetic fields and ages from 100 Myr to gigayears are observed]]"
to: "[[HC-3 - Nature and decay of an LHC-produced strong-gravity object]]"
arguments:
  - "[[A-49 - Solar-mass white dwarfs provide enough column density to stop cosmic-ray-produced neutral black holes for D up to 7]]"
  - "[[A-50 - Cosmic rays produce thousands of black holes on low-field white dwarfs within tens of millions of years under any composition]]"
  - "[[A-51 - White-dwarf survival excludes every scenario in which Earth accretion would be dangerous - the accretion-time ratio is about 2e4]]"
  - "[[A-53 - No Eddington limit throttles micro-black-hole accretion in Earth, white dwarfs, or neutron stars]]"
---
![[O-33 - Massive white dwarfs with very low magnetic fields and ages from 100 Myr to gigayears are observed]]

## Why this is evidence

These stars are exactly the objects that discriminate stability from prompt decay: massive enough to stop cosmic-ray-produced neutral black holes, weakly magnetized enough that cosmic-ray primaries reach the surface unscreened, and old enough that a captured stable hole would already have destroyed them. Under H-24 (stable neutral) their observed persistence at 100 Myr–Gyr ages is strongly unexpected; under H-10 and H-14 it is certain; H-7 is disfavored only in its longest-lifetime regime (holes surviving long enough to be brought to rest and accrete). H-35's stable behaviours are cut the same way as H-24.

## Likelihood

```python
# E-34 (HC-3) — lone edge, one observation O-33 "massive (M >~ 1 Msun), low-field (B_p <~ few e5 G), 100 Myr–Gyr
# white dwarfs". The SHARP white-dwarf anchor of the stable-hole exclusion, covering D<=7 (A-49 approved: D=5,6
# stop in a solar-mass WD, D=7 needs >~1.1 Msun, D>=8 exceeds WD stopping power and is handed to neutron stars →
# E-35). Chain: A-50 copious cosmic-ray production on these low-field stars, A-51 a stopped hole accretes and
# destroys the star in <<Gyr, A-53 no Eddington throttle. Prompt-decay members predict survival with certainty;
# anchor H-10 = 1. Members in HC-3.hypotheses order [H-7, H-10, H-14, H-24, H-35].
lik_wd_H7  = 0.88   # metastable: only its longest-lifetime regime (holes surviving long enough to stop and
                    # accrete in the WD) is disfavored; the ms-to-years bulk decays first. Slightly less strained
                    # than by O-22 — WD capture needs the extreme tail specifically
lik_wd_H10 = 1.0    # anchor: prompt Hawking decay, WD survival certain
lik_wd_H14 = 1.0    # near-threshold prompt decay, astrophysically safe — survival certain, matches H-10
lik_wd_H24 = 0.15   # stable neutral: for D<=7 the G-M chain (A-49/A-50/A-51/A-53) makes these old massive
                    # low-field WDs strongly unexpected — they should already have been destroyed. Nonzero
                    # because this edge does NOT constrain D>=8 (A-49: those exceed WD stopping power), so H-24
                    # parameter space with D>=8 survives WDs regardless — that residual room is what E-35 closes
lik_wd_H35 = 0.55   # residual: stable-accreting variants cut as H-24; other unmodelled fates survive. Middling,
                    # slightly under O-22's value since this is the sharper destructive prediction (rule 3)
t_wd = 0.74         # cap = trust_score(S-37 G-M) = 0.82, docked for the ~10% column-density systematics
                    # (temperature/composition) on the masses and the cooling-model ages (D-10 SDSS + Hansen
                    # cooling models) that set both the stopping margin and the age clock — the raw-data-to-
                    # observation step, not the argument chain (rule 4)
evidence("HC-3", ["O-33"], [lik_wd_H7, lik_wd_H10, lik_wd_H14, lik_wd_H24, lik_wd_H35], t=t_wd)
```
