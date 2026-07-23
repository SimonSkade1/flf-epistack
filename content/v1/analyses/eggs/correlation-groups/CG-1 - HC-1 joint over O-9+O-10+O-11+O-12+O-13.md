---
type: correlation-group
id: CG-1
to: "[[HC-1 - Overall net effect of moderate habitual egg intake on cardiovascular disease and mortality]]"
members:
  - "[[E-31 - O-9 × HC-1 — Kadoorie 11% lower total CVD]]"
  - "[[E-32 - O-10 × HC-1 — Kadoorie lower IHD and major coronary events]]"
  - "[[E-33 - O-11 × HC-1 — Kadoorie 26% lower haemorrhagic stroke]]"
  - "[[E-34 - O-12 × HC-1 — Kadoorie 10% lower ischaemic stroke]]"
  - "[[E-35 - O-13 × HC-1 — Kadoorie 18% lower CVD mortality]]"
---

Joint likelihood for correlated observations O-9, O-10, O-11, O-12, O-13 (shared basis: D-14). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-1 (HC-1) — ONE joint estimate over E-31..E-35: all five Kadoorie endpoint associations rest on the same
# China Kadoorie cohort/FFQ (basis D-14), so they are ONE witness (rule 1), not five. The whole pattern: a
# graded, monotonic INVERSE dose-response across every CVD endpoint in a large Chinese cohort — total CVD 0.89,
# CVD mortality 0.82, IHD/MCE 0.86-0.88, ischaemic stroke 0.90, and strongest of all haemorrhagic stroke 0.74,
# all with tight CIs and P-trend <0.001, no visible high-intake uptick (ceiling category is "daily"). Members
# in HC-1.hypotheses order [H-6 protective, H-21 null, H-27 harm, H-44 U-shape, H-49 residual]. Anchored on
# H-6 = 1 (rule 7): a Chinese/Asian graded inverse is exactly what causal Asian protection predicts.
lik_kad_H6  = 1.0   # anchor: H-6 (causal protection in Chinese adults) predicts precisely a graded Asian inverse
                    # across endpoints — the tightest fit. A-3 (corrected) only bars exporting the aggregate to the
                    # West; it does NOT lower the fit of this China-internal pattern under H-6, so no dock here.
lik_kad_H21 = 0.45  # 0.45x: under a true null the inverse must be healthy-user/SES confounding (in China higher egg
                    # intake tracks higher SES/better health) — routine in nutritional epi and it readily makes HR
                    # ~0.85-0.9 graded signals, so quite plausible; docked below H-6 because a clean 5-endpoint
                    # dose-response with the extra-strong haemorrhagic-stroke arm (0.74) is a touch more coherent
                    # than pure confounding usually delivers.
lik_kad_H27 = 0.18  # 0.18x: monotonic egg-cholesterol HARM predicts the OPPOSITE sign; producing a strong graded
                    # inverse needs confounding not just to mask but to overturn a real harmful effect — a lot to
                    # ask. Worst fit of the five. H-27's US scope does not rescue it: a universal atherogenic
                    # mechanism should still not read as protective here.
lik_kad_H44 = 0.4   # 0.4x: the descending arm (never/rarely -> daily falling) matches the LEFT side of a U, and the
                    # missing high-intake uptick is hidden by the qualitative FFQ ceiling ("daily", no >1/day or
                    # >=10/week category), so H-44 is not refuted — but it does not specifically predict the
                    # haemorrhagic-stroke-dominant gradient, so below H-6.
lik_kad_H49 = 0.55  # 0.55x: a region-dependent-sign world (Asia inverse) predicts a Chinese inverse about as well
                    # as H-6 but is more diffuse (covers many shapes/regions), so slightly under the anchor;
                    # middling per rule 3, not extreme.
t_kad = 0.6         # cap = trust_score(S-80) = 0.60, the min over {O-9..O-13} (all one source). Left at the cap:
                    # the non-validated single-baseline qualitative FFQ, no >1/day category, and healthy-user
                    # confounding are already priced into 0.60; the confounding is a truth question (it lives in the
                    # H-21/H-6 ratio), not a data-reliability one, so it is not double-docked into t.
evidence("HC-1", ["O-9", "O-10", "O-11", "O-12", "O-13"],
         [lik_kad_H6, lik_kad_H21, lik_kad_H27, lik_kad_H44, lik_kad_H49], t=t_kad)
```
