---
type: correlation-group
id: CG-16
to: "[[HC-5 - Operative exposure behind the egg-cardiovascular association]]"
members:
  - "[[E-114 - O-62 x HC-5 — habitual egg dose leaves steady-state TMAO unmoved]]"
  - "[[E-115 - O-64 x HC-5 — egg-form choline is inert for TMAO]]"
---

Joint likelihood for correlated observations O-62, O-64 (shared basis: S-60). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-16 (HC-5) — ONE joint estimate over E-114 + E-115: both rest on S-60 (Wilcox 2021 RCT), so priced together
# (rule 1). Members [H-3, H-26, H-54]. Joint pattern: a habitual dose (4 eggs/day, 4 weeks) left fasting TMAO
# and platelet reactivity unmoved (O-62), and phosphatidylcholine capsules at a matched choline dose likewise
# (O-64) — egg-form choline is inert for steady-state TMAO. This undercuts H-54's non-cholesterol choline->TMAO
# branch specifically; it does not separate H-3 from H-26 (neither makes egg-choline the operative pathway).
# Anchored on H-3 = 1.0.
lik_tmaonull_H3 = 1.0    # anchor: under H-3 (fat operative) egg-choline is not the pathway, so an inert TMAO
                         # readout is fully expected.
lik_tmaonull_H26 = lik_tmaonull_H3   # tied to the anchor: under H-26 (cholesterol operative) egg-choline is
                         # likewise not the pathway — this observation does not discriminate H-26 from H-3.
# H-54 as an inline mixture of its two branches (rule 2): the artefact/confounding pole makes no prediction about
# a TMAO feeding study (fits like the anchor), while the choline->TMAO pole predicted a rise and is disfavoured
# by the null. The within-H-54 branch split mirrors the residual's structural composition (artefact vs
# non-cholesterol), a decomposition of what H-54 encompasses, independent of H-54's overall prior weight.
fit_artefact_branch = 1.0     # artefact pole fits like the anchor — a TMAO feeding null is uninformative for pure confounding
frac_artefact_of_res = 0.56   # share of H-54 that is the artefact pole
frac_choline_of_res = 0.44    # share that is the non-cholesterol choline->TMAO pole
fit_choline_branch = 0.2      # how expected the double null is if egg-choline WERE operative — A-22 (approved)
                              # shows choline was absorbed yet TMAO did not rise, excluding under-dosing, so a
                              # choline-operative world should have moved TMAO. Not zero: a steady-state readout
                              # could miss a small or renally-gated effect (A-23, approved: null non-generalizable
                              # to renal impairment).
lik_tmaonull_H54 = frac_artefact_of_res * fit_artefact_branch + frac_choline_of_res * fit_choline_branch  # ~0.65
t_tmaonull = 0.72        # cap = trust over {O-62, O-64} = S-60 0.72. Held at cap: a null with modest n (18/10) is
                         # underpowered, but A-22 confirms it is a true form-dependent null not a dosing failure,
                         # and I keep the H-54 ratio moderate rather than docking t.
evidence("HC-5", ["O-62", "O-64"], [lik_tmaonull_H3, lik_tmaonull_H26, lik_tmaonull_H54], t=t_tmaonull)
```
