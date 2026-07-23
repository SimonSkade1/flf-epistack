---
id: E-107
type: evidence-link
from: "[[O-32 - Dietary choline or TMAO supplementation increases atherosclerosis in Apoe--- mice, correlating with plasma TMAO and not with plasma lipids]]"
to: "[[HC-5 - Operative exposure behind the egg-cardiovascular association]]"
arguments:
  - "[[A-11 - Germ-free-antibiotic necessity plus TMAO-supplementation sufficiency plus host-genetic segregation jointly establish a causal choline--flora--TMAO--atherosclerosis chain in mice]]"
---
![[O-32 - Dietary choline or TMAO supplementation increases atherosclerosis in Apoe--- mice, correlating with plasma TMAO and not with plasma lipids]]

## Why this is evidence
Choline/TMAO raise atherosclerosis in mice with no rise in cholesterol/TG/lipids — a non-lipid atherogenic route, the kind of non-cholesterol 'other exposure' H-54 posits. H-26 requires cholesterol/lipid mediation and H-3 fat quality; this supports H-54's mechanistic plausibility over both.

## Likelihood

```python
# E-107 (HC-5) — lone edge, one observation O-32 "lipid-independent atherogenic pathway in mice". Members in
# HC-5.hypotheses order [H-3 fat-quality, H-26 dietary-cholesterol, H-54 residual]. Choline/TMAO supplementation
# raised aortic plaque in Apoe-/- mice with plasma TMAO (not lipids) tracking plaque — a non-lipid atherogenic
# route, established causally by A-11 (approved: germ-free/antibiotic necessity + TMAO sufficiency + host-genetic
# segregation). This is the non-cholesterol mechanism H-54 posits; H-26 needs cholesterol/lipid mediation and
# H-3 fat quality. Anchored on H-54 = 1.0.
lik_mouse_H54 = 1.0  # anchor: a lipid-independent choline->TMAO->atherosclerosis chain is exactly H-54's
                     # non-cholesterol branch made mechanistically concrete.
lik_mouse_H26 = 0.5  # 0.5x: a non-lipid atherogenic route competes with H-26's cholesterol-mediation story, so
                     # mildly disfavours it — but this is a mouse model, so it does not refute egg-derived
                     # cholesterol being operative for the human egg-CVD association.
lik_mouse_H3 = 0.5   # 0.5x: same magnitude — a mouse TMAO-atherosclerosis result is orthogonal-to-mildly-awkward
                     # for H-3's claim about fat vs cholesterol as the plasma-cholesterol lever.
t_mouse = 0.72       # cap = trust of O-32's source S-28 (Wang 2011 Nature) = 0.72. Held at cap: the mouse
                     # experiment is well-controlled and A-11 establishes the causal chain within mice; the
                     # mouse->human relevance limit is carried in the modest 1.0-vs-0.5 ratio, not a t dock.
evidence("HC-5", ["O-32"], [lik_mouse_H3, lik_mouse_H26, lik_mouse_H54], t=t_mouse)
```
