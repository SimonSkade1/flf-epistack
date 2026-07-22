---
type: correlation-group
id: CG-7
to: "[[HC-10 - Stability status of the electroweak vacuum]]"
members:
  - "[[E-4 - O-4 × HC-10 — NNLO stability bound excluded by the measured Higgs mass]]"
  - "[[E-10 - O-5 × HC-10 — metastability verdict from measured Higgs and top masses]]"
---

Joint likelihood for correlated observations O-4, O-5 (shared basis: D-1). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-7 (HC-10) — ONE joint estimate over members E-4 + E-10: both O-4 (NNLO absolute-stability bound
# Mh > 129.4 GeV, excluded at 98% CL by the measured Mh = 125.5) and O-5 (metastable, lifetime >> age of
# universe) are the SAME Degrassi NNLO effective-potential verdict read off the SAME measured Higgs/top
# masses (data-basis D-1) — one witness, priced jointly (rule 1). Members in HC-10.hypotheses order:
#   [H-31 metastable false vacuum (a decay channel exists), H-42 exactly stable (no channel)].
# exhaustive_by_construction, so NO residual. The joint pattern judged whole: measured masses put the
# pure-SM potential in the metastable wedge — below the absolute-stability boundary, instability scale
# ~10^11 GeV, huge lifetime. Anchored on H-31 = 1 (rule 7). A-6 (approved) sets direction and size but
# enters only as reasoning (rule 5), not as a factor.

lik_verdict_H31 = 1.0   # anchor: metastability is *exactly* what H-31 predicts — a channel exists, the
                        # measured masses landing in the metastable region with enormous lifetime is the
                        # expected outcome, not a coincidence

# H-42 (exactly stable) is priced as a mixture of the two disjoint ways exact stability can hold given the
# data, following A-6's two hinges (approved):
ratio_H42_smvalid = 0.12  # SM-valid hinge: if pure SM holds to M_Pl (A-6's no-new-physics hinge), exact
                          # stability needs lambda(M_Pl) >= 0, i.e. Mt <~ 171 GeV — 2-3 sigma below the
                          # 173.1 +- 0.7 world average (A-6). Then the observed "metastable at 98% CL"
                          # verdict is the ~2-sigma tail; Gaussian density ~exp(-2) ~ 0.12x the H-31 anchor
ratio_H42_bsm = 1.0       # BSM hinge: if new physics / Planck-scale threshold corrections below M_Pl set
                          # the true stability (A-6's second hinge), the pure-SM verdict O-4/O-5 no longer
                          # tracks the real potential — the measured SM masses are then unremarkable and
                          # this verdict is ~as expected as under H-31, so uninformative (ratio 1)
w_H42_smvalid = 0.65      # prior share of H-42 realizations in which the pure-SM extrapolation is the
                          # operative description (exact stability most naturally = the SM potential is
                          # genuinely the global min) vs a more contrived BSM/quench rescue
lik_verdict_H42 = w_H42_smvalid * ratio_H42_smvalid + (1 - w_H42_smvalid) * ratio_H42_bsm  # ~0.43

t_verdict = 0.80  # cap = min trust_score over {O-4, O-5} = 0.85 (both via S-20 Degrassi). Docked ~0.05 for
                  # a named data-to-statement weakness: the hadron-collider pole top-mass carries an
                  # O(Lambda_QCD) ~0.3 GeV irreducible nonperturbative interpretation ambiguity beyond the
                  # quoted +-0.7 (A-6 approved; D-1 known_biases), so the Mt input feeding the verdict is
                  # slightly less faithful than the world-average error alone implies. Not docked further —
                  # the method itself is the leading first-complete-NNLO computation
evidence("HC-10", ["O-4", "O-5"], [lik_verdict_H31, lik_verdict_H42], t=t_verdict)
```
