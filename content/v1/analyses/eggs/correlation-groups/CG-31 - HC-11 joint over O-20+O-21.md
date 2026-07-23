---
type: correlation-group
id: CG-31
to: "[[HC-11 - Whether early egg introduction causally prevents egg allergy in high-risk infants]]"
members:
  - "[[E-5 - O-20 x HC-11 — PETIT RCT confirmed-allergy 8% vs 38%]]"
  - "[[E-7 - O-21 x HC-11 — PETIT acute-reaction-admission pattern bounds dropout artefact]]"
---

Joint likelihood for correlated observations O-20, O-21 (shared basis: S-15). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-31 (HC-11) — ONE joint estimate over members E-5 (O-20) + E-7 (O-21): both are the PETIT trial itself,
# shared basis S-15 (rule 1). Members in HC-11.hypotheses order [H-10 causal tolerance prevention,
# H-46 no causal effect / reduced incidence non-causal]. EXHAUSTIVE — 2 members, NO residual. Judge the whole
# pattern: a blinded, OFC-confirmed 8% vs 38% reduction (RR 0.221, p=0.0001) TOGETHER WITH acute-allergic-event
# counts similar across arms (15% egg vs 18% placebo) while hospital admissions run higher in the egg arm
# (10% vs 0%). Anchored on H-10 = 1 (rule 7); H-46 priced as a ratio.
lik_petit_H10 = 1.0   # anchor: the whole pattern is exactly what induced oral tolerance predicts — a large
                      # OFC-confirmed reduction, plus more acute reactions/admissions in the arm actually fed egg
                      # (real exposure) yet overall acute-event counts still similar. A-4 (approved): identical
                      # aggressive eczema treatment in both arms isolates egg introduction as the cause, closing
                      # the co-intervention explanation the carving flags.
lik_petit_H46 = 0.15  # ~0.15x as expected under the non-causal account. Randomisation + blinding leave H-46 only
                      # the differential-dropout artefact (already-reacting egg-arm infants removed before the
                      # OFC) to manufacture a 30-point gap — but O-21's similar acute-event counts (15% vs 18%)
                      # BOUND that dropout, and protocol non-generalizability is an external-validity claim that
                      # does not lower the within-trial likelihood at all. Kept non-trivial for interim-stopping
                      # inflation and small n (121; the 6-vs-0 admissions are small counts).
t_petit = 0.8         # cap = min trust_score over {O-20, O-21} = 0.8 (both via S-15). At the cap: OFC-confirmed,
                      # preregistered, objective endpoints — the interim-stopping / small-n caveats bear on effect
                      # MAGNITUDE (priced in the ratio), not on the reliability of the stated counts.
evidence("HC-11", ["O-20", "O-21"], [lik_petit_H10, lik_petit_H46], t=t_petit)
```
