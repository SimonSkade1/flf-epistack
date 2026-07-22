---
id: E-43
type: evidence-link
from: "[[O-35 - Earth and Sun have existed for about 4.5 billion years and the Sun has about 5 billion years remaining]]"
to: "[[HC-4 - Fate of the Earth under a hypothetically stable trapped black hole]]"
arguments:
  - "[[A-45 - Charged stable black holes would stop in Earth or the Sun, so their multi-billion-year survival excludes that scenario]]"
  - "[[A-46 - Neutral cosmic-ray-produced black holes punch through Earth and Sun, voiding the naive cosmic-ray safety argument]]"
---
![[O-35 - Earth and Sun have existed for about 4.5 billion years and the Sun has about 5 billion years remaining]]

## Why this is evidence

Discriminates through the charged-hole channel: a stable hole that keeps electric charge stops even at cosmic-ray speeds in ordinary matter, so under H-8-type dangerous accretion (or an H-36 regime damaging on timescales short against the ages involved) the Earth and Sun would not have survived their multi-billion-year cosmic-ray exposure. H-22 predicts their survival and uses it to exclude the charged-stable-hole configurations outright, leaving only the neutral case for the compact-star bounds. For neutral holes the observation is near-silent (relativistic holes pass through Earth), so the diagnostic weight is confined to that channel.

## Likelihood

```python
# E-43 (HC-4) — lone edge, one observation O-35 "Earth and Sun themselves have survived ~4.5 Gyr". Members in
# HC-4.hypotheses order [H-8 catastrophic, H-22 negligible, H-36 residual]. This is the WEAKEST H-8 exclusion
# of my three edges, for TWO independent reasons, both reflected below. (i) Its discrimination is confined to
# the CHARGED-hole channel (A-45, approved): neutral cosmic-ray holes punch straight through Earth and Sun
# (A-46, approved), so their survival says nothing about the neutral case that the WD/NS bounds carry. (ii)
# Earth/Sun survival is selection-contaminated by the anthropic shadow (A-19/A-20 family): every historical
# record is conditioned on no observer-extinguishing catastrophe, so P(we observe Earth survived | H-8) is
# inflated toward 1 in a way WD/NS/astronomical evidence (A-21) is NOT. Both effects push lik_H8 up toward the
# anchor, i.e. weaken the update. Anchor H-22 = 1 (rule 7).
lik_es_H22 = 1.0   # anchor: negligible growth trivially predicts Earth and Sun surviving their exposure
lik_es_H8 = 0.55   # 0.55x as expected as under H-22 — only mildly below 1, the honest contrast with E-39's
                   # 0.1. Under H-8 only the charged sub-case would destroy Earth/Sun (neutral holes pass
                   # through, A-46), and even that exclusion is anthropic-shadowed since we can only observe a
                   # surviving Earth. Held below 1 because billions of accumulated charged holes (A-45) could
                   # leave NON-fatal observable effects the shadow does not protect, giving some residual grip
lik_es_H36 = 0.8   # 0.8x: an intermediate regime is even less constrained by the narrow charged-only,
                   # shadow-limited channel; near the anchor, unconstrained (rule 3)
t_es = 0.80        # cap = trust_score of O-35's source S-37 = 0.82; kept near the cap because the Earth/Sun
                   # age is rock-solid data with no measurement/dating weakness. The anthropic shadow is a
                   # selection effect on what the observation can DISCRIMINATE, so it is priced in lik_es_H8
                   # above, not double-counted here in t (rule 5)
evidence("HC-4", ["O-35"], [lik_es_H8, lik_es_H22, lik_es_H36], t=t_es)
```
