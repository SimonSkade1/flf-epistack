---
id: E-44
type: evidence-link
from: "[[O-7 - Torsion-balance experiments limit the RS2 warping length L to below 44 microns]]"
to: "[[HC-4 - Fate of the Earth under a hypothetically stable trapped black hole]]"
arguments:
  - "[[A-9 - The allowed warping-length range up to 44 microns permits Casadio-Harms critical masses for which black-hole growth is catastrophic]]"
---
![[O-7 - Torsion-balance experiments limit the RS2 warping length L to below 44 microns]]

## Why this is evidence

H-8 requires the warped-scenario parameter region in which Casadio-Harms growth turns catastrophic, and that region lives inside the experimentally still-allowed window below the torsion-balance limit — H-8 entails the window being open, so the observation's precise location is a precondition it predicts. H-22 asserts every faster-accretion configuration is excluded, but by white-dwarf and neutron-star survival rather than by laboratory gravity tests, so it is compatible with the window being open or closed. The asymmetry — entailed by one member, unconstrained by the others — is weak evidence favoring the member that needs it; the disputed question of whether the open window really hosts dangerous configurations sits in the attached arguments.

## Likelihood

```python
# E-44 (HC-4) — lone edge, one observation O-7 "torsion-balance null leaves L < 44 um, with the 15.3-44 um
# range experimentally allowed". Members in HC-4.hypotheses order [H-8 catastrophic, H-22 negligible,
# H-36 residual]. This is a WEAK edge: the observation is a fixed experimental fact both members must
# accommodate; the only discrimination is that H-8 REQUIRES the window open while H-22 is agnostic. Anchored
# on H-8 = 1 (rule 7); ratios kept near unity to reflect the weak asymmetry.
lik_window_H8  = 1.0   # anchor: H-8's dangerous Casadio-Harms corner must sit inside an experimentally
                       # allowed window, so an open window at 15.3-44 um is a precondition H-8 predicts.
                       # A-9 (approved) is what makes the open window discriminating: it shows the allowed
                       # range permits catastrophic critical masses M_c (1.1e5-2.2e6 kg), turning "window
                       # open" into a satisfied precondition rather than an inert fact. Best fit.
lik_window_H22 = 0.85  # ~0.85x: H-22 excludes every fast-accretion channel by white-dwarf / neutron-star
                       # survival, not by lab gravity, so it is compatible with the window open OR closed.
                       # The open window is unremarkable but not required under H-22 — only weakly less
                       # expected than under H-8, hence a ratio close to 1 (weak edge).
lik_window_H36 = 0.9   # ~0.9x: unlisted intermediate outcome, unconstrained (rule 4) — neither needs nor
                       # forbids the window being open; a middling value near unity, not an extreme.
t_window = 0.3         # cap = trust_score of O-7's source S-30 = 0.3, at the cap: O-7 is a firmly
                       # established experimental limit (Kapner et al. 2007, 95% CL) with no
                       # measurement / selection weakness in the raw-data -> observation step to dock for.
evidence("HC-4", ["O-7"], [lik_window_H8, lik_window_H22, lik_window_H36], t=t_window)
```
