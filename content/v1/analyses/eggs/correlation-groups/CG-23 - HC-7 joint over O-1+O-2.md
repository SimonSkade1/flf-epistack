---
type: correlation-group
id: CG-23
to: "[[HC-7 - Nature of inter-individual variation in cholesterol response to dietary cholesterol]]"
members:
  - "[[E-8 - O-1 x HC-7 — 69-31 compensation split]]"
  - "[[E-11 - O-2 x HC-7 — rise tracks failed synthesis suppression]]"
---

Joint likelihood for correlated observations O-1, O-2 (shared basis: S-25). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-23 (HC-7) — ONE joint estimate over O-1 + O-2: both rest on S-25 (McNamara 1987 metabolic-ward
# feeding), so priced jointly (rule 1). Pattern judged whole: a 69/31 per-period split where the majority
# hold plasma cholesterol nearly flat by MEASURED down-regulation of fractional absorption/synthesis (O-1),
# AND the plasma rise falls specifically in the periods that fail to suppress endogenous synthesis (O-2).
# Members in HC-7.hypotheses order [H-1 discrete split, H-2 feedback mechanism, H-35 continuous trait,
# H-36 ApoE-null, H-55 residual]. Anchored on H-2 = 1.0 (best fit). A-1 is CORRECTED and used as reasoning:
# it APPROVES the feedback-MECHANISM reading (rise<->failed-suppression is what a real feedback system
# predicts and noise does not) but only WEAKLY supports an individualized per-SUBJECT responder trait,
# because O-1/O-2 are counted per diet-period (within-person state variation reproduces the same alignment)
# — this keeps H-2 above H-1.
lik_mcnamara_H2 = 1.0    # anchor: H-2 uniquely predicts BOTH halves — the compensating majority via
                         # absorption/synthesis feedback AND the distinctive rise<->failed-synthesis-
                         # suppression coupling; A-1 (corrected) approves exactly this mechanism reading
lik_mcnamara_H1 = 0.8    # 0.8x: the 69/31 split is H-1's classic framing and fits O-1 well, but H-1 is
                         # agnostic about the O-2 synthesis coupling, and A-1 (corrected) downgrades the
                         # per-period split to only weak support for a stable per-subject responder axis
lik_mcnamara_H35 = 0.55  # 0.55x: a continuous ~normal trait can produce the 69/31 as a threshold cut of a
                         # mostly-positive distribution, so O-1 is compatible; but H-35 does not predict the
                         # mechanistic synthesis-suppression coupling O-2, unlike the mechanism/discrete pair
lik_mcnamara_H36 = 0.5   # 0.5x: H-36 is a claim about ApoE identifiability; the McNamara data tests no
                         # genotype, so O-1/O-2 barely discriminate it — sits at the marginal/uninformative level
lik_mcnamara_H55 = 0.42  # 0.42x: residual real but below middling — its "largely noise / regression to the
                         # mean" sub-reading is specifically argued against (the rise tracks a MEASURED
                         # physiological state, not scatter; A-1), while its "different dominant determinant"
                         # sub-reading stays neutral. Not lower: an unlisted structure could still fit
t_mcnamara = 0.65        # cap = trust_score(S-25) = 0.72; docked modestly: the observation is extracted from
                         # the abstract + step-2 summary only (full text is scanned page images, results not
                         # auditable), and subject n / per-subject structure is not recoverable from the text
evidence("HC-7", ["O-1", "O-2"], [lik_mcnamara_H1, lik_mcnamara_H2, lik_mcnamara_H35, lik_mcnamara_H36, lik_mcnamara_H55], t=t_mcnamara)
```
