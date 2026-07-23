---
type: correlation-group
id: CG-5
to: "[[HC-1 - Overall net effect of moderate habitual egg intake on cardiovascular disease and mortality]]"
members:
  - "[[E-39 - O-86 × HC-1 — PURE egg intake null for CVD and mortality]]"
  - "[[E-40 - O-87 × HC-1 — PURE lower MI not replicated in ONTARGET]]"
  - "[[E-41 - O-89 × HC-1 — ONTARGET-TRANSCEND egg-CVD null]]"
  - "[[E-65 - O-85 × HC-1 — no adverse lipid shift undercuts the cholesterol-mediated harm mechanism]]"
  - "[[E-66 - O-88 × HC-1 — isolated non-replicated protective subgroup signal fits noise around null]]"
---

Joint likelihood for correlated observations O-86, O-87, O-89, O-85, O-88 (shared basis: S-91). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-5 (HC-1) — ONE joint estimate over E-39/40/41/65/66: all five rest on the same Dehghan-2020 report of the
# PURE + ONTARGET/TRANSCEND cohorts (basis S-91), one witness (rule 1). The whole pattern: a large, multinational,
# PRECISE null on composite CVD/mortality/major CVD (O-86; upper bound ~1.04), replicated in secondary-prevention
# ONTARGET/TRANSCEND (O-89), with NO adverse lipid shift and slightly lower BP (O-85, so the cholesterol->lipid
# harm mechanism is not engaged), and the only protective blips (MI O-87; prevalent-CVD subgroup O-88) isolated,
# non-replicated and non-significant-interaction. Members in HC-1.hypotheses order. Anchored on H-21 = 1 (rule 7):
# a precise, mechanistically-coherent null with noise-level blips is the null's signature; S-91 is H-21's own
# additional source.
lik_pure_H21 = 1.0   # anchor: precise null across 50 countries (A-30 corrected: well-powered against harm above
                     # ~4%), mechanism absent (A-31 approved: flat LDL/TC removes the main harm pathway), and the
                     # protective signals read as chance (A-32 approved: multiplicity + non-replication). Best fit.
lik_pure_H6  = 0.4   # 0.4x: H-6 (Asian protection) gets weak support from the isolated MI/prevalent-CVD blips and
                     # the lower BP, but A-32 (approved) calls those chance, and PURE's results were CONSISTENT
                     # across regions with a precise overall null — a protective Asian subset should have shown,
                     # so the regional homogeneity is mild tension. Below null.
lik_pure_H27 = 0.2   # 0.2x: strongly disfavoured — the precise null excludes CVD/mortality harm above ~4% (A-30)
                     # and the harm mechanism is absent (O-85, A-31 approved). Only the ONTARGET heart-failure
                     # positive trend (HR 1.25, P-trend 0.01) offers any harm hint. Worst fit.
lik_pure_H44 = 0.4   # 0.4x: the >=7-vs-<1/week contrast compares two arms a U puts at similar (elevated) height,
                     # so a U could read ~null on that contrast — BUT PURE's per-0.5-egg and cubic-spline analyses
                     # were also null (P>0.10), which would tend to reveal a U, and H-44 is Chinese-scoped. Middling.
lik_pure_H49 = 0.45  # 0.45x: region/subgroup-dependent sign is dented by PURE's cross-region CONSISTENCY and by
                     # the subgroup blips failing to replicate; middling per rule 3.
t_pure = 0.78        # cap = trust_score(S-91) = 0.78, min over the five observations (one source). Left at the
                     # cap: FFQ single-assessment error is already in 0.78; A-30's caveat that the CI bounds
                     # random not systematic error shapes how far the null carries (the ratios), not the data's
                     # reliability, so no further dock.
evidence("HC-1", ["O-86", "O-87", "O-89", "O-85", "O-88"],
         [lik_pure_H6, lik_pure_H21, lik_pure_H27, lik_pure_H44, lik_pure_H49], t=t_pure)
```
