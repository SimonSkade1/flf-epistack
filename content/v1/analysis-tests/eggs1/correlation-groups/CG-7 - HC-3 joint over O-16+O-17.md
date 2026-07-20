---
type: correlation-group
id: CG-7
to: "[[HC-3 - Whether egg's effect varies by subgroup or individual responder type]]"
members:
  - "[[E-11 - O-16 × HC-3 — individual cholesterol responsiveness reproducible across repeated trials]]"
  - "[[E-12 - O-17 × HC-3 — responsiveness independent of habitual intake and body weight]]"
---

Joint likelihood for correlated observations O-16, O-17 (shared basis: S-5). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-7 (HC-3) - ONE joint estimate over E-11 + E-12: O-16 and O-17 are two results of the same
# Katan/Beynen 1987 feeding study (shared basis S-5), so they are one witness (rule 1). The pattern is
# judged whole: 32 volunteers x 3 alternating low-/high-cholesterol trials give a within-person
# reproducible responsiveness classification (O-16) that correlates with the HDL2/total-cholesterol rise
# but NOT with habitual cholesterol intake or body weight (O-17). Members in HC-3.hypotheses order:
# [H-6 T2D/prediabetes subgroup not harmed, H-7 intrinsic responder trait, H-13 residual: homogeneous].
# Anchored on H-7 = 1 (rule 7a).
#
# SCOPE LIMIT (inherited from step 4's flagged exclusivity strain; already logged, not repairable here):
# this pair bears on the responder-trait axis (H-7) and is close to silent on the diabetic-subgroup axis
# (H-6). No number below should be read as discriminating H-6 from H-7 - the evidence layer cannot.

lik_katan_H7 = 1.0    # anchor: H-7 is precisely what this pattern describes. A stable, lifestyle-independent
                      # hypo/hyperresponder trait predicts both halves at once - reproducibility across three
                      # alternating trials AND null correlation with habitual intake / body weight (the
                      # "lifestyle-independent" clause). A-5 (approved) is the reasoning: reproducibility is
                      # what rules out the noise reading, so the pair is H-7's core positive evidence.

lik_katan_H6 = 0.85   # ~0.85x, i.e. deliberately close to the anchor, NOT a discrimination. H-6 is about a
                      # named clinical subgroup (T2D/prediabetes) being unharmed; it makes no prediction
                      # about within-person reproducibility in a general volunteer sample (the study reports
                      # no diabetic stratum). Under H-6 this pattern is about as expected as it is a priori.
                      # Docked slightly below 1 only because H-6 as carved emphasises a *clinically
                      # identifiable* modifier, which sits marginally awkwardly with O-17's finding that
                      # responsiveness tracks no observable marker. Treat as ~uninformative for H-6.

lik_katan_H13 = 0.25  # 0.25x. H-13 as a strict homogeneity claim predicts between-trial response differences
                      # are measurement noise, hence NOT reproducible within person - it fits O-16 badly, and
                      # a strictly homogeneous world also has no responsiveness axis for O-17's HDL2
                      # correlation to attach to. Not pushed lower because H-13 is the residual and also
                      # absorbs heterogeneity along axes neither member names (APOE, microbiome, baseline
                      # LDL); such an unlisted axis would itself produce reproducible individual classes, so
                      # part of the residual's mass predicts this pattern well. n=32 with 3 trials also leaves
                      # room for a chance-reproducible split under pure noise, though not much.

t_katan = 0.55        # cap = trust_score of S-5 = 0.68 (the only source; both observations inherit it).
                      # Docked below the cap for: n=32 in one Dutch volunteer cohort, a 1987 analysis whose
                      # responder-classification and correlation pipeline could not be inspected (regression
                      # to the mean across repeat trials is the standard failure mode for exactly this
                      # design), and a surrogate serum-cholesterol endpoint.

evidence("HC-3", ["O-16", "O-17"], [lik_katan_H6, lik_katan_H7, lik_katan_H13], t=t_katan)
```
