---
type: correlation-group
id: CG-4
to: "[[HC-1 - Overall net effect of moderate habitual egg intake on cardiovascular disease and mortality]]"
members:
  - "[[E-37 - O-59 × HC-1 — +half egg-day higher CVD and mortality (US pooled)]]"
  - "[[E-51 - O-58 × HC-1 — dietary-cholesterol dose-response harm, no threshold]]"
---

Joint likelihood for correlated observations O-59, O-58 (shared basis: D-1). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-4 (HC-1) — ONE joint estimate over E-37 (O-59) + E-51 (O-58): both rest on the same Zhong 6-cohort US pool
# (basis D-1), one witness (rule 1). The pattern: in US cohorts, each +half-egg/day is POSITIVELY associated
# with CVD (1.06) and mortality (1.08) before cholesterol adjustment, and each +300 mg/day dietary cholesterol
# is positively, MONOTONICALLY and THRESHOLD-FREELY associated (1.17, 1.18). A-21 (approved): the egg signal is
# statistically carried by dietary cholesterol (near-collinear). Members in HC-1.hypotheses order. Anchored on
# H-27 = 1 (rule 7): a monotonic no-threshold dietary-cholesterol/egg dose-response in US adults is its core.
lik_zhong_H27 = 1.0   # anchor: this IS H-27's textbook prediction — egg-cholesterol -> atherogenic -> more CVD,
                      # monotonic, no threshold, US population. Tightest fit; A-21 (approved) makes cholesterol
                      # the operative exposure, exactly H-27's framing.
lik_zhong_H21 = 0.45  # 0.45x: under a true null the positive HRs are single-baseline-diet residual confounding /
                      # regression dilution — and the class of modest HRs (1.06-1.18) here is exactly the class
                      # that attenuated to null in the repeated-measure Harvard cohorts (S-21 trust_reason), so
                      # confounding is a live reading; below H-27 because the clean monotonic cholesterol gradient
                      # is more specifically harm-shaped.
lik_zhong_H6  = 0.3   # 0.3x: H-6 is Asian-scoped, silent on the US; a US POSITIVE association is the wrong sign
                      # for a protective mechanism and would need confounding to overwhelm any protection. Low.
lik_zhong_H44 = 0.35  # 0.35x: a threshold-free monotonic increase is the opposite of a U's interior minimum;
                      # H-44 fits only if the sampled US range sits entirely on the U's ascending (high-intake)
                      # arm, and H-44 is Chinese-scoped anyway. Low-middling.
lik_zhong_H49 = 0.5   # 0.5x: a region-dependent-sign world (US harmful, Asia protective) accommodates a US
                      # positive; middling per rule 3, unconstrained.
t_zhong = 0.57        # cap = trust_score(S-21) = 0.57, min over {O-59, O-58}. Left at the cap: the
                      # mostly-single-baseline diet (regression dilution/residual confounding) is already in 0.57,
                      # and the egg/cholesterol near-collinearity flagged by A-21 is a which-exposure
                      # interpretation issue (it lives in the H-27:H-21 ratio), not a defect in the measured
                      # association, so t is not docked further.
evidence("HC-1", ["O-59", "O-58"],
         [lik_zhong_H6, lik_zhong_H21, lik_zhong_H27, lik_zhong_H44, lik_zhong_H49], t=t_zhong)
```
