---
type: correlation-group
id: CG-3
to: "[[HC-6 - Origin of the UHECR spectral structure]]"
members:
  - "[[E-8 - O-15 × HC-6 — Auger instep above 5.5 sigma]]"
  - "[[E-9 - O-16 × HC-6 — declination-independent spectra]]"
---

Joint likelihood for correlated observations O-15, O-16 (shared basis: D-2). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-3 (HC-6) — ONE joint estimate over members E-8 + E-9: both observations are the same Auger 2025
# dataset (shared basis D-2), so treat them as one witness (rule 1). The whole pattern judged together:
# (a, O-15) a distinct INSTEP feature established >5.5 sigma between ankle and suppression, plus ankle
# and suppression; (b, O-16) the spectrum is sky-uniform — five declination bands from -90 to +44.8 deg
# consistent with the all-sky spectrum (departure prob. 13-71%) and with Telescope Array. Members in
# HC-6.hypotheses order [H-9 GZK extragalactic-proton, H-12 He/CNO mass components, H-21 heavy-Galactic-
# to-light-extragalactic transition, H-37 residual]. Anchored on H-12 = 1 (rule 7): it is the only member
# predicting BOTH halves — the instep as a source-composition crossover feature AND sky-uniformity from a
# numerous distributed population.
lik_spec_H12 = 1.0   # anchor: He/CNO account predicts a feature exactly where the instep sits (source
                     # rigidity maximum / mass-group crossover) and, being a numerous source population,
                     # predicts the observed declination-independence. Strengthened by A-16 (approved):
                     # the sky-uniformity positively disfavors the few-foreground-source rival and favors
                     # a whole-sky common cause — i.e. H-12's numerous-population reading
lik_spec_H9  = 0.3   # 0.3x vs H-12: the extragalactic-proton flux is numerous, so O-16's uniformity is
                     # well predicted, but a pure-proton GZK spectrum predicts a FEATURELESS power law
                     # between ankle and suppression — the >5.5 sigma instep (O-15) is surprising under
                     # H-9 (E-8 body). Uniformity fits, the instep does not; net well below the anchor
lik_spec_H21 = 0.2   # 0.2x: the instep lies above the ~10^18.5 eV dip, in H-21's light-extragalactic
                     # regime, so like H-9 it predicts no instep there (surprising); and a heavy Galactic
                     # component below the dip would be expected to leave more directional structure than
                     # the mild dipole seen, so O-16's uniformity is mildly surprising too. Both halves
                     # pull down — the worst-fitting listed member
lik_spec_H37 = 0.4   # 0.4x: unlisted/exotic cause, unconstrained — could accommodate an instep-like
                     # feature (e.g. a shared cross-experiment energy-scale artifact) and sky-uniformity,
                     # so middling. Not higher: its salient few-foreground-source branch predicts
                     # declination-DEPENDENCE, which A-16 (approved) disfavors. Not near zero — I can't
                     # rule out an unlisted sky-uniform cause of the feature (rule 3)
t_spec = 0.9         # cap = min trust_score over {O-15, O-16} = 0.9 (both via S-75). Held at the cap: the
                     # dominant 14% energy-scale systematic is already what caps S-75 below 1, the instep
                     # significance is explicitly robust to +/-14% shifts (stays >5.5 sigma), and O-16 is a
                     # band-to-band relative comparison in which that common systematic largely cancels —
                     # no further step-to-observation weakness to dock for (rule 4)
evidence("HC-6", ["O-15", "O-16"], [lik_spec_H9, lik_spec_H12, lik_spec_H21, lik_spec_H37], t=t_spec)
```
