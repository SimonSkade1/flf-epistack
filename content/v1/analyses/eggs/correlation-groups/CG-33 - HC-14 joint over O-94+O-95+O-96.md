---
type: correlation-group
id: CG-33
to: "[[HC-14 - Whether dietary choline is an essential nutrient for humans]]"
members:
  - "[[E-6 - O-94 × HC-14 — plasma choline depletes on choline-free diet]]"
  - "[[E-9 - O-95 × HC-14 — ALT rise (liver dysfunction) on choline-free diet]]"
  - "[[E-10 - O-96 × HC-14 — serum cholesterol falls on choline-free diet]]"
---

Joint likelihood for correlated observations O-94, O-95, O-96 (shared basis: S-7). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-33 (HC-14) — ONE joint estimate over members E-6 (O-94) + E-9 (O-95) + E-10 (O-96): all three are the
# Zeisel 1991 depletion trial, shared basis S-7 (rule 1). Members in HC-14.hypotheses order [H-39 choline
# essential, H-48 not essential (PEMT synthesis suffices)]. EXHAUSTIVE — 2 members, NO residual. Judge the whole
# pattern: in the deficient arm ONLY (concurrent control flat), plasma choline/PC fell ~30%, serum ALT rose
# 0.42->0.62 ukat/L (incipient liver dysfunction), and serum cholesterol fell ~15% — all reversing on
# repletion. Anchored on H-39 = 1 (rule 7).
lik_chol_H39 = 1.0   # anchor: pool depletion + an ORGAN-dysfunction sign + lipid-export derangement, arm-
                     # specific and reversible with a flat concurrent control, is precisely the classical
                     # essentiality signature. A-33 (approved): removal-plus-reversal under a concurrent control,
                     # methionine/folate adequate-but-not-excess (PEMT not artificially starved), meets the
                     # essentiality criterion.
lik_chol_H48 = 0.2   # ~0.2x the anchor: "synthesis suffices" can accommodate the plasma fall alone (a marker
                     # dropping with intake need not mean functional deficiency), but it predicts AGAINST the
                     # reversible ALT rise and the cholesterol derangement — functional deficiency signs the
                     # deficient arm shows and the control does not. Kept non-trivial for the small, male-only,
                     # short-term sample and the argument that one modest ALT elevation may be sub-clinical /
                     # non-generalizable (the carving's failure mode).
t_chol = 0.72        # cap = min trust_score over {O-94, O-95, O-96} = 0.72 (all via S-7). At the cap: objective
                     # lab biomarkers under a concurrent control; the small-n / male-only / short-term caveats
                     # bear on generalization (priced in the ratio), not on the reliability of the measured
                     # arm-specific, reversible changes.
evidence("HC-14", ["O-94", "O-95", "O-96"], [lik_chol_H39, lik_chol_H48], t=t_chol)
```
