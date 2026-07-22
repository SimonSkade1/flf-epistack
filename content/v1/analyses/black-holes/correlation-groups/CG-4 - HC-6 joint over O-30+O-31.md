---
type: correlation-group
id: CG-4
to: "[[HC-6 - Origin of the UHECR spectral structure]]"
members:
  - "[[E-14 - O-30 × HC-6 — Fly's Eye dip at 10^18.5 eV]]"
  - "[[E-15 - O-31 × HC-6 — 3e20 eV proton-like event]]"
---

Joint likelihood for correlated observations O-30, O-31 (shared basis: D-13). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-4 (HC-6) — ONE joint estimate over members E-14 + E-15: both observations rest on the Fly's Eye
# detector D-13 / Bird et al. 1994 (S-43), so they are one witness (rule 1). Members in HC-6.hypotheses
# order: [H-9 GZK extragalactic protons, H-12 He/CNO source-rigidity-max composition, H-21 Galactic-heavy
# to extragalactic-light transition at the dip, H-37 residual]. The pattern judged whole: (a) a dip at
# 10^18.5 eV + flattening above 10^19 eV (O-30), and (b) one 3e20 eV, proton-like X_max event far above
# the GZK suppression (O-31). Anchored on H-9 = 1; others priced as ratios to it (rule 7).

lik_flyseye_H9 = 1.0    # anchor: both halves are textbook GZK-proton predictions — a pair-production dip
                        # near 10^18.5 eV, and a super-GZK proton event tolerable from a nearby source under
                        # GZK propagation. Best joint fit.
lik_flyseye_H12 = 0.3   # 0.3× the anchor: He/CNO does not own the dip (its feature is the instep/steepening,
                        # though it does not forbid a dip), and the highest-energy half fits worst on two
                        # counts — a proton-like X_max=852 g/cm^2 contradicts a heavy top composition, and a
                        # single event a factor of several above a *sharp* source-rigidity cutoff is
                        # surprising. Not lower: one event, X_max error +68/-100 and a gamma primary not
                        # excluded, so the discrimination is real but soft.
lik_flyseye_H21 = 1.0   # ≈ anchor: this witness does not separate the two protonic accounts (E-14: the dip
                        # "raises H-9 and H-21 jointly"; E-15: proton X_max "expected under H-9, H-21"). The
                        # dip is H-21's defining crossover feature and its top composition is light/protonic,
                        # so both halves fit as well as under H-9.
lik_flyseye_H37 = 0.4   # 0.4×: unlisted cause, unconstrained — neither predicts nor forbids this exact
                        # pattern (rule 3, middling). Docked below par because A-43 (approved) closes the
                        # resolution/aperture/epoch artifact channels, so the dip is a real feature rather
                        # than the instrumental branch of the residual (E-14 "Why"). Not near zero: exotic
                        # top-down or unproposed-propagation sub-branches can accommodate a proton super-GZK
                        # event.
t_flyseye = 0.85        # cap = min trust_score over {O-30, O-31} = 0.85 (both via S-43). Held at the cap:
                        # A-43 (approved) shows the dip survives resolution, aperture, and epoch checks and
                        # that cross-experiment (Akeno/Haverah/Yakutsk) breaks agree to <0.2 in slope, so the
                        # step from raw fluorescence data to the stated features carries no extra weakness
                        # beyond what S-43's score already reflects.
evidence("HC-6", ["O-30", "O-31"], [lik_flyseye_H9, lik_flyseye_H12, lik_flyseye_H21, lik_flyseye_H37], t=t_flyseye)
```
