---
id: E-35
type: evidence-link
from: "[[O-34 - Neutron stars with gigayear lifetimes, fields of 10^8 G and up, and long-lived binary companions are observed]]"
to: "[[HC-3 - Nature and decay of an LHC-produced strong-gravity object]]"
arguments:
  - "[[A-52 - Neutron-star survival bounds the D of 8 and higher scenarios via binary beam dumps and cosmogenic neutrinos]]"
  - "[[A-53 - No Eddington limit throttles micro-black-hole accretion in Earth, white dwarfs, or neutron stars]]"
---
![[O-34 - Neutron stars with gigayear lifetimes, fields of 10^8 G and up, and long-lived binary companions are observed]]

## Why this is evidence

Neutron stars stop even the neutral holes white dwarfs cannot (higher-dimensional cases D ≥ 8), so their observed Gyr lifetimes discriminate the same way as the white-dwarf observation but cover the remaining parameter space: unexpected under H-24 (stable neutral) given cosmic-ray or cosmogenic-neutrino production reaching them (the binary-companion beam-dump geometry evades magnetic screening), certain under prompt-decay H-10 and H-14, and pressuring only the extreme-lifetime end of H-7. Together with the white-dwarf case this is the pair of observations the stable-hole exclusion actually rests on.

## Likelihood

```python
# E-35 (HC-3) — lone edge, one observation O-34 "Gyr-old neutron stars, B >~ 1e8 G, long-lived binary companions".
# The neutron-star anchor covering D>=8 — exactly the parameter space white dwarfs cannot stop (A-52 approved:
# NS stop any hole at d_0 <~ 0.01 cm; production reaches them via binary-companion beam dumps + GZK cosmogenic
# neutrinos, both evading the >~1e8 G magnetic screening; a captured hole consumes the star in <~10 Myr). A-53:
# no Eddington throttle lengthens that. Prompt-decay members predict survival with certainty; anchor H-10 = 1.
# With E-34 this is the complementary-D pair the exclusion rests on. Order [H-7, H-10, H-14, H-24, H-35].
lik_ns_H7  = 0.88   # metastable: only the extreme-lifetime end is pressured (holes surviving long enough to be
                    # captured and accrete); the short-lived bulk decays first. Mild ratio below the anchor
lik_ns_H10 = 1.0    # anchor: prompt decay, NS survival certain
lik_ns_H14 = 1.0    # near-threshold prompt decay, astrophysically safe — survival certain, matches H-10
lik_ns_H24 = 0.15   # stable neutral: for D>=8 the NS bound (A-52) makes Gyr-old NS with long-lived binaries
                    # strongly unexpected. Not near zero — A-52's own escape hatch needs cosmic rays almost
                    # purely heavy AND the cosmogenic-neutrino flux absent/non-reactive simultaneously (two
                    # independent unlikely failures), a small but real slice of H-24 space. Comparable teeth to
                    # the WD edge over its complementary D-range, so priced the same
lik_ns_H35 = 0.55   # residual: stable-accreting variants cut as H-24; other unmodelled fates survive fine —
                    # middling (rule 3)
t_ns = 0.76         # cap = trust_score(S-37 G-M) = 0.82, docked modestly for the FCE/binary-demographics
                    # modeling (companion solid-angle exposure) and field measurements feeding the production
                    # side; the core datum — Gyr-old NS at two-solar-mass Shapiro-delay pulsar ages (S-66/S-80) —
                    # is very solid, so a smaller dock than the WD edge
evidence("HC-3", ["O-34"], [lik_ns_H7, lik_ns_H10, lik_ns_H14, lik_ns_H24, lik_ns_H35], t=t_ns)
```
