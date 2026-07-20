---
type: correlation-group
id: CG-2
to: "[[HC-2 - Evaporation of TeV-scale black holes]]"
members:
  - "[[E-8 - O-2 × HC-2 — intact old neutron stars bound non-evaporating black holes]]"
  - "[[E-9 - O-4 × HC-2 — Earth-Sun survival bounds stopped non-evaporating black holes]]"
---

Joint likelihood for correlated observations O-2, O-4 (shared basis: D-1). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-2 (HC-2) — ONE joint estimate over members E-8 + E-9: O-2 (NSs of 10^8-10^9 yr observed intact)
# and O-4 (Earth/Sun survived ~4.5 Gyr of super-LHC cosmic-ray bombardment) share data-basis D-1
# (rule 1). Members in HC-2.hypotheses order: [H-4 evaporates near-instantly, H-7 long-lived].
# Anchored on H-4 (rule 7): if micro holes evaporate near-instantly, nothing accretes anywhere and
# the whole survival pattern is certain.
lik_surv_H4 = 1.0   # anchor: under H-4 both observations are guaranteed — evaporation kills any
                    # cosmic-ray-produced hole before it can accrete.
# H-7: the joint pattern is unexpected only on the path (cosmic rays actually produce TeV holes) AND
# (they reach/stop in a NS) AND (accretion then eats the star within its observed age). Each leg is a
# named branch weight; the complement branches leave the observations certain, so the total is a
# mixture. O-4 does almost no extra work under H-7: per A-6 (corrected), Earth/Sun survival is
# conditioned on our existence, so its likelihood ratio is ~1 for the stopped/charged sub-cases
# (A-3, corrected, keeps only the weakened "subject to observer-selection" form); the neutral
# sub-case escapes Earth/Sun anyway (E-9 body). So the discriminating force is carried by O-2,
# whose distant-body selection bias is only partial (A-6 corrected verdict).
p_cr_production = 0.7    # cosmic-ray production of TeV holes needs the fundamental gravity scale
                         # near a TeV — a separate question (HC-3) not settled by H-7 itself; the
                         # edge's evidential force exists only in this branch. Sizeable but not
                         # certain; without production the observations say nothing about H-7.
p_ns_shielded = 0.2      # O-2's own caveat: the NS bound needs cosmic-ray primaries to penetrate
                         # NS magnetospheres; in the shielded corner no hole is ever delivered and
                         # NS survival is unsurprising. Minority corner — G-M treat it as an extra
                         # assumption, not a likely escape.
p_ns_survives_hit = 0.05 # given production + delivery: NS density (~10^14 g/cm^3) stops any TeV
                         # hole (A-1, approved, closes the relativistic-escape loophole), and A-2
                         # (approved) finds no fast-accretion scenario compatible with Gyr survival
                         # — so intact 10^8-10^9 yr NSs are strongly unexpected; small residual
                         # for slow-accretion corners A-2's sweep might not cover.
lik_surv_H7 = (1 - p_cr_production) \
    + p_cr_production * (p_ns_shielded + (1 - p_ns_shielded) * p_ns_survives_hit)
t_surv = 0.74            # cap = min trust_score over {O-2, O-4} = 0.74 (both via S-1); kept at the
                         # cap — the delivery/production caveats are already priced inside
                         # lik_surv_H7, docking t too would double-count them.
evidence("HC-2", ["O-2", "O-4"], [lik_surv_H4, lik_surv_H7], t=t_surv)
```
