---
type: correlation-group
id: CG-27
to: "[[HC-9 - Whether habitual egg intake produces a harm-relevant TMAO elevation]]"
members:
  - "[[E-28 - O-62 x HC-9 — 4 eggs-day no fasting TMAO rise (normal renal)]]"
  - "[[E-29 - O-63 x HC-9 — free choline raises fasting TMAO 6-fold]]"
  - "[[E-30 - O-64 x HC-9 — phosphatidylcholine (no matrix) also no TMAO rise]]"
  - "[[E-44 - O-65 x HC-9 — choline absorbed in egg arm despite TMAO null]]"
  - "[[E-45 - O-67 x HC-9 — egg white doesn't suppress choline-driven TMAO]]"
---

Joint likelihood for correlated observations O-62, O-63, O-64, O-65, O-67 (shared basis: S-60). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-27 (HC-9) — ONE joint estimate over E-28+E-29+E-30+E-44+E-45: all five observations are arms of the
# same Wilcox 2021 RCT (shared basis S-60), so priced jointly (rule 1). The whole pattern: 4 eggs/day x4wk
# leaves fasting TMAO flat (O-62) while choline was absorbed (O-65); free choline raises fasting TMAO ~6-fold
# (O-63) but phosphatidylcholine — egg-yolk's chemical form without the whole-egg matrix — does not (O-64);
# and egg white fails to suppress the choline-driven rise (O-67). A form-dissection signature. Members in
# HC-9.hypotheses order [H-28 form-governs, H-29 fasting-null, H-30 renal-only, H-42 real-postprandial-rise,
# H-43 benign, H-56 residual]. Anchored on H-28 = 1.0 (rule 7).
lik_wilcox_H28 = 1.0   # anchor / best fit: "chemical form, not total choline, governs TMA generation" is the
                       # ONLY member predicting the full contrast — free choline positive, egg + PC null,
                       # matrix (egg white) irrelevant. A-22 (approved) chains the four arm facts to isolate
                       # form as the operative variable; this pattern is its exact fingerprint.
lik_wilcox_H29 = 0.85  # egg fasting null (O-62) is precisely H-29's claim, so strongly consistent; priced just
                       # below the anchor because H-29 speaks only to the egg readout and does not itself
                       # predict the free-choline/PC form contrast (consistent with it, not entailing it).
lik_wilcox_H30 = 0.55  # 0.55x: the normal-renal null is what a renal-only-rise expects for this intact-
                       # clearance sample, and A-23 (approved) holds the null cannot extrapolate to impaired
                       # renal — so not discriminated against; but a 6-fold free-choline rise in the same
                       # normal-renal people shows clearance alone does not keep TMAO flat, and H-30 does not
                       # explain the form contrast, so below the fasting-null poles.
lik_wilcox_H42 = 0.35  # 0.35x: a chronic 4-egg/day dose leaving FASTING TMAO flat is evidence against "eggs
                       # raise TMAO production" as the best summary; not lower because Wilcox measures only
                       # fasting, leaving H-42's postprandial rise (the Miller pattern) an available escape.
lik_wilcox_H43 = 0.65  # 0.65x: a fasting null is consistent with a rise that is purely postprandial/benign
                       # (H-43 locates the rise off the fasting axis), but H-43 does not predict the
                       # free-choline/PC form contrast, so below the fasting-null and form poles.
lik_wilcox_H56 = 0.4   # 0.4x residual, kept real and middling (rule 3): a 4-week fasting null argues against
                       # its concrete reading (a chronic steady-state elevation in normal-renal people), and
                       # E-45 disfavours a matrix-inhibitor alternative, but an unlisted route is unconstrained.
t_wilcox = 0.72        # cap = min trust_score over {O-62,O-63,O-64,O-65,O-67}, all via S-60 = 0.72; kept at
                       # cap — the modest egg-arm n=18 is already priced into S-60's trust_score, and the
                       # far-from-threshold positive control (p<0.0001) shows the egg null is genuine, not underpowering.
evidence("HC-9", ["O-62", "O-63", "O-64", "O-65", "O-67"], [lik_wilcox_H28, lik_wilcox_H29, lik_wilcox_H30, lik_wilcox_H42, lik_wilcox_H43, lik_wilcox_H56], t=t_wilcox)
```
