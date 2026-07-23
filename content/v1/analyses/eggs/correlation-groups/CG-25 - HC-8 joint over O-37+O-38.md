---
type: correlation-group
id: CG-25
to: "[[HC-8 - Causal status of elevated TMAO for human atherosclerosis]]"
members:
  - "[[E-70 - O-37 x HC-8 — TMAO predicts 3-year incident events in humans]]"
  - "[[E-71 - O-38 x HC-8 — TMAO dose-dependent with prevalent CVD, adjusted]]"
---

Joint likelihood for correlated observations O-37, O-38 (shared basis: D-4). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-25 (HC-8) — ONE joint estimate over E-70+E-71: O-37 and O-38 both rest on the Cleveland Clinic GeneBank
# angiography cohort D-4 (rule 1). One pattern: plasma TMAO/choline/betaine prospectively predict 3-yr incident
# MI/stroke/death in a small metabolomics sub-cohort (O-37), and show a dose-dependent association with prevalent
# CVD that survives traditional-risk adjustment and tracks coronary burden, n=1876 (O-38). A-12 (approved):
# observational, referral-selected — supports but cannot itself establish human causality. Members in
# HC-8.hypotheses order [H-15, H-16, H-45]. A clear human association is POSITIVELY predicted by both H-16
# (causally) and H-45 (via renal / dysbiosis / diet confounding), but only weakly by H-15 (human translation
# explicitly open). Anchored on H-16 = 1 (rule 7).
lik_human_H16 = 1.0  # anchor: a real human causal factor straightforwardly yields a prospective, dose-dependent,
                     # adjustment-surviving association
lik_human_H45 = 0.9  # ~0.9x: a confounded marker of renal function / unhealthy diet produces exactly this
                     # association in an angiography cohort (the classic overturned-biomarker story — cf. the
                     # prior's homocysteine/CRP reference class). Just below H-16 because per E-71 the association
                     # held after traditional-risk adjustment (a pure diet marker might attenuate more) — but renal
                     # function was NOT adjusted and O-38 is cross-sectional, so reverse causation + renal
                     # confounding keep H-45 nearly as high
lik_human_H15 = 0.6  # ~0.6x: H-15 leaves human translation open, so it neither predicts nor forbids a clear human
                     # association — this observation lifts H-16/H-45 over it (E-70/E-71). Not lower because the
                     # same confounding pathways available to H-45 also operate in an H-15 world
t_human = 0.72       # cap = trust_score(S-28) = 0.72 (O-37/O-38 source S-28). At cap: the small untargeted
                     # discovery subcohort (50v50 / 25v25) is a mild reliability concern, but this joint call
                     # includes the n=1876 confirmation cohort; referral-selection is an interpretation/confounding
                     # matter priced in the ratios (H-45), not a data-reliability dock
evidence("HC-8", ["O-37", "O-38"], [lik_human_H15, lik_human_H16, lik_human_H45], t=t_human)
```
