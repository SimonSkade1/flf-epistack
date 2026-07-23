---
type: correlation-group
id: CG-13
to: "[[HC-5 - Operative exposure behind the egg-cardiovascular association]]"
members:
  - "[[E-105 - O-1 x HC-5 — most subjects buffer added dietary cholesterol]]"
  - "[[E-106 - O-3 x HC-5 — plasma cholesterol tracks fat quality over cholesterol quantity]]"
---

Joint likelihood for correlated observations O-1, O-3 (shared basis: S-25). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-13 (HC-5) — ONE joint estimate over E-105 + E-106: both observations rest on S-25 (McNamara 1987),
# so priced together as one witness (rule 1). Members in HC-5.hypotheses order
# [H-3 fat-quality, H-26 dietary-cholesterol, H-54 residual]. Joint pattern: in 69% of metabolic-ward diet
# periods added dietary cholesterol was homeostatically buffered (O-1), and cohort-mean plasma cholesterol
# tracked fat quality more than cholesterol quantity (O-3) — the direct signature of fat-quality dominance.
# Anchored on H-3 = 1.0.
lik_buffer_H3 = 1.0    # anchor: H-3 (fat quality the larger determinant) is exactly what predicts a buffering
                       # majority plus fat>cholesterol sensitivity. A-1 (corrected) affirms a real
                       # feedback-control buffering mechanism (not random variation) drives the 69% compensation.
lik_buffer_H26 = 0.35  # 0.35x: H-26 predicts dietary cholesterol reliably raises plasma cholesterol as the
                       # graded lever; a 69% buffering majority AND O-3's direct finding that plasma cholesterol
                       # is more sensitive to fat quality than to cholesterol dose both cut against it. Not driven
                       # near zero — the ~31% non-suppressors leave cholesterol a residual population lever.
lik_buffer_H54 = 0.5   # 0.5x middling: whether the operative CVD exposure is a non-cholesterol egg component or
                       # pure dietary-pattern confounding, a feeding study's fat-vs-cholesterol sensitivity is
                       # largely orthogonal — the residual neither predicts nor forbids this pattern (rule 3).
t_buffer = 0.72        # cap = min trust over {O-1, O-3} = S-25 trust_score 0.72. Held at cap: O-1 is
                       # depth-limited (scanned page images, per-period not per-subject accounting), but the
                       # population-level buffering frequency and fat>cholesterol sensitivity I use are stated
                       # directly in the abstract and affirmed by A-1, not the individual-level reading.
evidence("HC-5", ["O-1", "O-3"], [lik_buffer_H3, lik_buffer_H26, lik_buffer_H54], t=t_buffer)
```
