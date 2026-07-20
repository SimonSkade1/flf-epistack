---
type: evidence-link
id: E-7
from: "[[O-1 - White dwarfs of about one solar mass with Gyr ages and low magnetic fields are observed intact]]"
to: "[[HC-2 - Evaporation of TeV-scale black holes]]"
arguments:
  - "[[A-1 - Relativistic-escape loophole in the Earth cosmic-ray argument is closed by white-dwarf and neutron-star stopping power]]"
  - "[[A-2 - Every fast-accretion scenario is excluded by white-dwarf and neutron-star survival]]"
---
![[O-1 - White dwarfs of about one solar mass with Gyr ages and low magnetic fields are observed intact]]

## Why this is evidence

H-7 (evaporation fails): cosmic-ray-produced TeV black holes stopped inside these dense WDs would, if they accrete catastrophically, have destroyed them within their Gyr ages — survival is then unexpected. H-4 (rapid evaporation): survival is certain. Discrimination is partial: it also depends on accretion being fast (HC-1's question).

## Likelihood

```python
# E-7 (HC-2) — lone edge, one observation O-1 "old low-field WDs observed intact". Members in
# HC-2.hypotheses order: [H-4 evaporates near-instantly, H-7 evaporation fails]. Anchored on
# H-4 (rule 7). Covers O-1 alone for THIS cluster; the NS/exposure edges (E-8, E-9) are
# priced by their own unit.
lik_wd_H4 = 1.0   # anchor: rapid evaporation means no hole survives to be trapped — WD
                  # survival is certain, the observation carries no surprise.
lik_wd_H7 = 0.5   # the edge's discrimination is partial by construction: given evaporation
                  # fails, cosmic-ray holes ARE trapped in WDs (A-1, approved), but their
                  # destruction additionally needs fast accretion — HC-1's unresolved question.
                  # In the denser WD interior a larger slice of the a-priori accretion-rate
                  # range is fast (A-2's P1 direction), so survival is genuinely surprising
                  # but far from excluded under H-7: roughly even odds that the trapped
                  # holes accrete a WD within its Gyr age.
t_wd7 = 0.74      # = cap: trust_score of O-1's source S-1 (0.74). Same data as E-1's call
                  # (different cluster, so no double-cover); no named data-level weakness
                  # beyond what step 2 priced.
evidence("HC-2", ["O-1"], [lik_wd_H4, lik_wd_H7], t=t_wd7)
```
