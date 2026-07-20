---
type: correlation-group
id: CG-3
to: "[[HC-2 - Net direction of egg's effect on hard cardiovascular and mortality endpoints]]"
members:
  - "[[E-14 - O-4 x HC-2 - CKB dose-response inverse association with CVD-IHD-stroke]]"
  - "[[E-15 - O-5 x HC-2 - CKB 18 percent lower CVD mortality with daily eggs]]"
---

Joint likelihood for correlated observations O-4, O-5 (shared basis: D-8). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-3 (HC-2) - ONE joint estimate over E-14 + E-15. O-4 and O-5 both rest on D-8 (CKB) and come from the
# same paper (S-13): they are ONE witness, not two (rule 1). The pattern judged whole: in a 461k Chinese
# cohort with low baseline intake (~0.76 egg/day), daily consumers show a graded inverse gradient across
# hard endpoints (CVD 0.89, IHD 0.88, MCE 0.86, hemorrhagic stroke 0.74, ischemic stroke 0.90) AND an 18%
# lower CVD mortality, with a significant monotone dose-response trend. Because it is one witness, the
# vector is priced as for a single coherent finding - no squaring of a per-observation ratio.
# Members in HC-2.hypotheses order: [H-2, H-3, H-4, H-9, H-10, H-12 residual]. Anchored on H-2 = 1 (rule 7).

lik_ckb_H2 = 1.0    # ANCHOR (protective at ~1/day): predicts exactly this - a graded inverse on events plus
                    # a mortality-level inverse. The best fit of any member. Note the CKB range (0 to ~1/day)
                    # sits inside H-2's "moderate" scope, so no extrapolation strain.
lik_ckb_H3 = 0.10   # 0.10x: harmful predicts the OPPOSITE sign on both halves, and specifically on
                    # all-cause/CVD mortality where the 18% inverse is most direct. Not ~0 because CKB
                    # excluded baseline diabetics (H-3's strongest subgroup) and intake is low, so H-3's
                    # claim is about high intake and could coexist with a null-to-inverse signal here;
                    # producing a MONOTONE inverse gradient under H-3 still needs strong confounding.
lik_ckb_H4 = 0.40   # 0.40x: H-4 asserts an IHD null and explicitly attributes the apparent inverse to
                    # reverse causation, so a weak inverse is part of what it predicts - much better placed
                    # than the other null variants on this observation. Docked because (i) A-4 (approved):
                    # the significant monotone dose-response is harder for a reverse-causation artifact than
                    # a threshold difference, though A-4 concedes graded confounding is not excluded, and
                    # (ii) CKB excluded prevalent CVD/cancer/diabetes at baseline, weakening the reverse-
                    # causation route H-4 relies on. Also H-4 is scoped to IHD and says nothing about the
                    # hemorrhagic-stroke 0.74 or CVD mortality, so half the pattern is unaddressed.
lik_ckb_H9 = 0.72   # 0.72x: scope rider is "generally healthy WESTERN adults up to ~1/day". CKB is a
                    # Chinese, largely rural/LMIC cohort, so this observation is nearly out of scope and
                    # barely discriminates - it should sit near the uninformative level rather than near
                    # H-10. Not 1.0 because H-9 does assert a null direction and a null account gives no
                    # positive reason to expect a monotone gradient of this size; a mild dock, no more.
lik_ckb_H10 = 0.15  # 0.15x: H-10 is the one null variant squarely IN scope - "no material effect across
                    # diverse global populations INCLUDING low/middle-income". CKB is the flagship LMIC
                    # test, and an 18% CVD-mortality difference with a monotone trend is material. This is
                    # the strongest disconfirmation in the set. Kept above H-3 (not below) because a null
                    # can still generate a modest inverse through residual healthy-user confounding in a
                    # single-FFQ observational design, whereas H-3 must produce a sign reversal.
lik_ckb_H12 = 0.85  # 0.85x: "direction varies by population/intake level" positively predicts protection in
                    # a LOW-baseline-intake population at the bottom of the intake range - close to the
                    # anchor. Slightly below H-2 only because H-12 is unconstrained about which way any
                    # particular population goes, so it spreads probability over the opposite result too.

t_ckb = 0.55        # cap = trust_score of S-13 (both observations) = 0.7. Docked to 0.55 for the raw-data ->
                    # observation step specifically: a single-occasion baseline FFQ in coarse frequency
                    # categories (never grams), with intake never re-measured over 8.9 y, so the exposure
                    # contrast "daily vs non/rare" is a noisy proxy that also tracks affluence and general
                    # diet quality (D-8 known_biases). Not lower: 461k participants and 84k events make the
                    # estimates precise, endpoints are registry/death-certificate based rather than self-
                    # reported, and CKB is an audited cohort.

evidence("HC-2", ["O-4", "O-5"],
         [lik_ckb_H2, lik_ckb_H3, lik_ckb_H4, lik_ckb_H9, lik_ckb_H10, lik_ckb_H12], t=t_ckb)
```
