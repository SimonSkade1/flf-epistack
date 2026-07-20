---
type: evidence-link
id: E-1
from: "[[O-1 - White dwarfs of about one solar mass with Gyr ages and low magnetic fields are observed intact]]"
to: "[[HC-1 - Fate of a stable LHC black hole trapped in Earth]]"
arguments:
  - "[[A-1 - Relativistic-escape loophole in the Earth cosmic-ray argument is closed by white-dwarf and neutron-star stopping power]]"
  - "[[A-2 - Every fast-accretion scenario is excluded by white-dwarf and neutron-star survival]]"
---
![[O-1 - White dwarfs of about one solar mass with Gyr ages and low magnetic fields are observed intact]]

## Why this is evidence

H-1 (catastrophic accretion) predicts that cosmic-ray-produced stable black holes stopped in these dense old stars would have destroyed them within their Gyr ages; H-2 predicts they survive. Observed intactness is expected under H-2, surprising under H-1.

## Likelihood

```python
# E-1 (HC-1) — lone edge, one observation O-1 "old low-field WDs observed intact". Members in
# HC-1.hypotheses order: [H-1 catastrophic accretion, H-2 no macroscopic risk, H-6 residual].
# Anchored on H-2 (rule 7). Covers O-1 ALONE — NS survival and the exposure record are CG-1's
# joint call, not re-counted here.
lik_wd_H2 = 1.0   # anchor: if trapped holes are macroscopically harmless within the solar
                  # lifetime, catalogued Gyr-old WDs surviving is exactly what you expect.
lik_wd_H1 = 0.1   # given catastrophic Earth-accretion is real, A-2 (approved): the same
                  # short-distance gravity destroys far denser WDs well inside 1 Gyr, and A-1
                  # (approved) closes the relativistic-escape loophole — cosmic-ray production
                  # + trapping in WDs follows. Intactness then needs a premise failure the
                  # low-B selection was designed to exclude (residual magnetic screening,
                  # UHECR flux/threshold shortfall at the WD surface) or the minority
                  # fast-on-Earth-slow-in-WD regime A-2's P1 denies. Not lower: those escape
                  # routes are real physics uncertainties, not exotica.
lik_wd_H6 = 0.6   # residual (unlisted fate, e.g. sub-catastrophic damage): most such fates
                  # leave a WD observably intact, but some partial-accretion regimes would
                  # disrupt or dim these stars — above middling, below the H-2 anchor.
t_wd = 0.74       # = cap: trust_score of O-1's source S-1 (0.74). No extra dock — the
                  # low-B/age screening is already built into the observation statement and
                  # no approved argument names a further data-level weakness.
evidence("HC-1", ["O-1"], [lik_wd_H1, lik_wd_H2, lik_wd_H6], t=t_wd)
```
