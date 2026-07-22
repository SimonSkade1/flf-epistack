---
type: correlation-group
id: CG-2
to: "[[HC-6 - Origin of the UHECR spectral structure]]"
members:
  - "[[E-6 - O-10 × HC-6 — TA ankle and 5.5-sigma suppression]]"
  - "[[E-7 - O-11 × HC-6 — cross-experiment spectrum agreement]]"
---

Joint likelihood for correlated observations O-10, O-11 (shared basis: D-3). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-2 (HC-6) — ONE joint estimate over E-6 (O-10) + E-7 (O-11): both rest on the single TA SD dataset
# D-3, so one witness (rule 1). Members in HC-6.hypotheses order: [H-9 GZK extragalactic-proton
# propagation, H-12 He/CNO source-rigidity account, H-21 Galactic-heavy→extragalactic-light transition at
# the dip, H-37 residual]. The whole pattern judged as one: TA sees an ankle at 4.6e18 eV, a 5.5-sigma
# suppression at 5.4e19 eV, and E_1/2 = 10^19.72 eV — landing exactly on the parameter-insensitive
# GZK-proton value (O-10; A-14 approved) — AND that structure is reproduced by three technique- and
# hemisphere-independent experiments (HiRes, TA, Auger up to a 20% scale shift), with a residual 3-sigma
# TA-vs-Auger break-energy difference (O-11). Anchored on H-9 = 1 (rule 7); others priced as ratios.
lik_ta_H9 = 1.0    # anchor: H-9 is the only member that predicts BOTH the ankle+suppression pair AND that
                   # the suppression sits at the near-parameter-free GZK value 10^19.72 (A-14, approved:
                   # instrument artifact / intrinsic source cutoff have no reason to land on that energy).
                   # Cross-experiment agreement is fully expected. The 3-sigma break-energy split cuts
                   # mildly against a single common propagation scale, so short of a perfect fit but best.
lik_ta_H12 = 0.6   # 0.6× as expected: H-12 predicts a steepening too, but as a source-rigidity cutoff not
                   # tied to the GZK scale, so the exact E_1/2 = 19.72 coincidence is unexplained (docks
                   # it). Partly recovered because source astrophysics naturally allows N/S skies to
                   # differ, fitting the 3-sigma break-energy discrepancy better than a common propagation
                   # feature (E-7 "## Why this is evidence"). Cross-experiment agreement fully expected.
lik_ta_H21 = 0.45  # 0.45×: H-21 owns the ~10^18.5 dip as a Galactic/extragalactic crossover and predicts
                   # the agreement fine, but the high-energy suppression and its precise GZK-value E_1/2
                   # are not distinctively its own (its pair-production dip overlaps what H-9 explains),
                   # so it borrows the suppression's location rather than predicting it — below H-12.
lik_ta_H37 = 0.3   # 0.3×: unconstrained, but this specific pattern is adverse to its natural branches —
                   # 3 independent techniques/hemispheres seeing the same structure disfavors a shared
                   # instrumental artifact (E-7), and the precise E_1/2→GZK match is unexpected from a
                   # generic unlisted cause. Not near zero: an exotic top-down source could mimic parts.
t_ta = 0.9         # cap = min trust_score over {O-10, O-11} = 0.9 (both via S-71). No dock: the ankle and
                   # suppression are 5.5-sigma robust and cross-corroborated; the 22% energy-scale
                   # systematic is folded into the quoted E_1/2 = 19.72 ± 0.05, and the 3-sigma break
                   # difference is part of the stated observation, not a data-reliability defect.
evidence("HC-6", ["O-10", "O-11"], [lik_ta_H9, lik_ta_H12, lik_ta_H21, lik_ta_H37], t=t_ta)
```
