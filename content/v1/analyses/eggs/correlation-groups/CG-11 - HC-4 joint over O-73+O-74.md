---
type: correlation-group
id: CG-11
to: "[[HC-4 - Cardiometabolic effect of eggs in people with diabetes, prediabetes, or metabolic syndrome]]"
members:
  - "[[E-83 - O-73 x HC-4 — egg-CVD HR 2.81 in diabetics only (KoGES)]]"
  - "[[E-84 - O-74 x HC-4 — egg intake not associated with fasting lipids (KoGES)]]"
---

Joint likelihood for correlated observations O-73, O-74 (shared basis: D-16). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-11 (HC-4) — ONE joint estimate over E-83+E-84: O-73 (egg-CVD HR 2.81 in diabetics only, null in
# non-diabetics) and O-74 (no egg-lipid association across quartiles), both from KoGES/Jang 2018 (S-14,
# basis D-16), priced jointly (rule 1). Whole pattern: a large diabetic-SPECIFIC egg-CVD hazard WITHOUT any
# accompanying lipid difference. Anchored on H-24 = 1.0 (rule 7). Members in HC-4.hypotheses order.
lik_koges_H24 = 1.0   # anchor: a diabetic-only CVD excess with a null non-diabetic stratum IS H-24's 'for whom'
                      # prediction; the lipid null (O-74) is neutral for an endpoint-level harm claim
lik_koges_H33 = 0.45  # 0.45x: H-33 rationalises the diabetic CVD harm but REQUIRES an egg-lipid derangement —
                      # O-74 shows none, so the joint pattern (harm without lipid change) is specifically awkward for it (E-84 body)
lik_koges_H4  = 0.35  # 0.35x: O-74 lipid-null fits H-4's neutrality, but the big diabetic HR is against the safe
                      # pole. Not lower: A-24 (approved) — 79 cases, CI lower bound 1.25, likely winner's-curse
                      # inflated, so a spurious large subgroup HR is not improbable if eggs are truly safe
lik_koges_H19 = 0.32  # 0.32x: same safe-pole penalty from O-73 as H-4, and H-19 gets no lipid-null credit (silent on lipids)
lik_koges_H52 = 0.55  # 0.55x: unlisted effect — a diabetic-specific harm with no lipid trace is one thing it can accommodate; middling (rule 3)
t_koges = 0.5         # cap = min trust over {O-73,O-74} = S-14 0.55; docked to 0.5 for the 79-case diabetic
                      # subgroup (A-24, approved: wide CI, magnitude fragile) — a named weakness in the datum
evidence("HC-4", ["O-73", "O-74"], [lik_koges_H4, lik_koges_H19, lik_koges_H24, lik_koges_H33, lik_koges_H52], t=t_koges)
```
