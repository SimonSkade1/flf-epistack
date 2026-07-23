---
type: correlation-group
id: CG-6
to: "[[HC-1 - Overall net effect of moderate habitual egg intake on cardiovascular disease and mortality]]"
members:
  - "[[E-42 - O-108 × HC-1 — China-PAR U-shaped egg-CVD]]"
  - "[[E-43 - O-109 × HC-1 — China-PAR U-shaped egg-mortality]]"
---

Joint likelihood for correlated observations O-108, O-109 (shared basis: S-81). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-6 (HC-1) — ONE joint estimate over E-42 (O-108) + E-43 (O-109): both rest on the same China-PAR cohort
# (basis S-81), one witness (rule 1). The pattern: a clear U-shape in a large Chinese cohort across BOTH
# endpoints, minimum risk at 3-<6 eggs/week, elevated at both extremes (CVD: <1/wk 1.22, >=10/wk 1.39;
# mortality: <1/wk 1.29, >=10/wk 1.13). Members in HC-1.hypotheses order. Anchored on H-44 = 1 (rule 7):
# China-PAR is H-44's own source and this is its exact claim.
lik_cpar_H44 = 1.0   # anchor: an interior-minimum U with harm at both tails in Chinese adults IS H-44. A-41
                     # (approved) makes the non-monotonicity a definitional consequence of the reported HRs.
lik_cpar_H6  = 0.35  # 0.35x: H-6 (monotonic protection) fits the descending low->optimum arm — and A-42
                     # (approved) says the low arm overstates harm (SES/reverse causation), which if anything
                     # helps a protective reading — but the ascending high-intake arm (CVD 1.39) directly
                     # contradicts monotonic protection. Partial fit.
lik_cpar_H21 = 0.35  # 0.35x: under a true null, a clean two-sided U significant on both arms across two endpoints
                     # needs confounding to manufacture BOTH tails; A-42 (approved) supplies the low arm (deprivation
                     # + reverse causation), but the high-intake arm is less cleanly explained as bias. A specific
                     # pattern for a null to reproduce.
lik_cpar_H27 = 0.2   # 0.2x: monotonic no-threshold harm cannot produce an interior minimum — A-41 (approved)
                     # explicitly refutes any monotone dose-response here. The high arm fits H-27, the protective
                     # descending arm does not. Worst fit.
lik_cpar_H49 = 0.5   # 0.5x: the residual explicitly covers non-monotone shapes other than the simple U and
                     # subgroup/region dependence, so it accommodates a U comfortably though less sharply than the
                     # named U-member H-44; middling per rule 3.
t_cpar = 0.65        # cap = trust_score(S-81) = 0.68, min over {O-108, O-109}. Docked slightly to 0.65 for a
                     # specific raw-data->observation gap: the intermediate categories (1-<3/wk, 6-<10/wk) were
                     # paywalled/unread, so the U rests on the reported extremes plus the interior reference
                     # (O-108 note). The U's existence still holds from those points, so the dock is small; the
                     # baseline-FFQ/low-arm-confounding limits are already inside the 0.68 cap.
evidence("HC-1", ["O-108", "O-109"],
         [lik_cpar_H6, lik_cpar_H21, lik_cpar_H27, lik_cpar_H44, lik_cpar_H49], t=t_cpar)
```
