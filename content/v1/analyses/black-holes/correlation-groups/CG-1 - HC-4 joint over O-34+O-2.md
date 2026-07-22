---
type: correlation-group
id: CG-1
to: "[[HC-4 - Fate of the Earth under a hypothetically stable trapped black hole]]"
members:
  - "[[E-40 - O-34 × HC-4 — gigayear neutron stars and their binary companions survive]]"
  - "[[E-41 - O-2 × HC-4 — a specific gigayear-old massive neutron star persists]]"
---

Joint likelihood for correlated observations O-34, O-2 (shared basis: S-66, S-80). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-1 (HC-4) — ONE joint estimate over E-40 + E-41: both observations trace to the same pulsar-timing
# basis S-66/S-80 (rule 1). Members in HC-4.hypotheses order: [H-8 catastrophic, H-22 negligible over the
# Sun's remaining lifetime, H-36 residual intermediate]. The whole pattern judged jointly: a POPULATION of
# neutron stars survives intact for >1e9 yr at supranuclear density (O-34), and ONE concretely dated
# instance — PSR J1614-2230, ~2 Msun, characteristic age 5.2 Gyr, held at ~2-5x nuclear saturation for that
# span (O-2). Anchored on H-22 = 1 (rule 7); H-8 and H-36 priced as ratios to it.
lik_ns_H22 = 1.0   # anchor: old gigayear neutron stars are exactly what H-22 predicts — a captured hole
                   # accretes too slowly to matter, and their survival is the observation H-22 expects.
lik_ns_H8  = 0.12  # 0.12x the anchor: under catastrophic fast-accretion physics a hole captured in the
                   # densest matter accretes FASTEST of all — A-52 (approved) puts consumption at <~10 Myr
                   # (D=11 worst case; <~50 yr for D<=7) << the Gyr ages, so a whole Gyr-old population plus
                   # a 5.2-Gyr instance is strongly improbable. Kept well off zero, NOT via the prior's
                   # A-7/A-8 gaps (already counted), but by A-52's OWN internalized escape hatch: the bound
                   # fails only if cosmic rays are almost purely heavy AND the cosmogenic-neutrino flux is
                   # absent/non-reactive — two independent unlikely failures at once, so residual-small but
                   # nonzero. A-53 (approved) removes the one out that would raise it: no Eddington throttle
                   # lengthens the neutron-star destruction time, so H-8 cannot cheaply explain survival.
lik_ns_H36 = 0.5   # 0.5x: unlisted intermediate outcome, unconstrained (rule 3) — an accretion regime slow
                   # enough to spare Gyr neutron stars yet non-negligible for Earth can accommodate the
                   # pattern, but sub-gigayear intermediate regimes (E-40 body: "likewise disfavored") would
                   # consume such dense stars, so middling, below the anchor. Higher would assert the middle
                   # predicts old-NS survival as well as H-22; lower would deny any middle could produce it.
t_ns = 0.82        # cap = min trust_score over the named observations' sources: O-34 via S-37 = 0.82,
                   # O-2 via S-66 = 0.90 -> min 0.82. At the cap: the raw datum (neutron stars survive Gyr
                   # at ~2 Msun) is a clean, independently re-timed Shapiro-delay / spectroscopic measurement;
                   # S-37's 0.82 already books the model-dependence of the survival chain, so no further dock.
evidence("HC-4", ["O-34", "O-2"], [lik_ns_H8, lik_ns_H22, lik_ns_H36], t=t_ns)
```
