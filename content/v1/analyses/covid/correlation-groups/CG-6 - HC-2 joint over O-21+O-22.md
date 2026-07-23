---
type: correlation-group
id: CG-6
to: "[[HC-2 - Number of independent introductions of SARS-CoV-2 into humans]]"
members:
  - "[[E-4 - O-21 × HC-2 — two-introduction Bayes factor cut by the erratum]]"
  - "[[E-5 - O-22 × HC-2 — asymmetric two-introduction likelihood inflated support]]"
---

Joint likelihood for correlated observations O-21, O-22 (shared basis: S-1). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-6 (HC-2) — ONE joint estimate over members E-4 (O-21) + E-5 (O-22): both are Weissman's re-reading
# of the SAME Pekar 2022 analysis (data_basis S-1), so priced jointly (rule 1) — one witness, not two.
# Members in HC-2.hypotheses order: [H-5 two-or-more introductions, H-16 single introduction];
# exhaustive_by_construction, so NO residual (two-entry vector only).
#
# The joint pattern these two observations describe: Pekar's headline two-introduction Bayes factor is only
# ~4.3 after the 2024 coding-error erratum (O-21), AND that BF was computed with an ASYMMETRIC
# conditionalization — the two-introduction likelihood scored on the squared polytomy criterion alone, while
# the single-introduction likelihood also had to satisfy the size-ratio and sequence-difference conditions
# (O-22). Per A-35 (status: CORRECTED, checked): imposing the same size-ratio and sequence-difference
# conditions on the two-introduction model I2 collapses P(tau|I2) by ~an order of magnitude and REVERSES the
# Bayes factor to a factor of ORDER 4 (~3.9–4.4) FAVOURING a single introduction. So this unit's evidence,
# correctly interpreted, points to H-16.
#
# A correctly-computed Bayes factor IS the likelihood ratio P(observed topology | one intro)/P(... | two
# intros), so the *corrected* BF is directly this evidence's likelihood ratio between the two members.
# Anchored on H-16 = 1 (the member the corrected analysis favours, i.e. the best fit); H-5 priced as a ratio
# to it (rule 7). (This group and CG-5 bear on HC-2 in opposite directions; priced here on its own merits —
# the runner composes the two, so no attempt to net against CG-5's phylodynamic signal.)

lik_bf_H16 = 1.0   # anchor: H-16 (single introduction). If exactly one introduction is true, a
                   # symmetric-conditioning recomputation of Pekar's own topology data should land favouring a
                   # single introduction — which is exactly what O-21 + O-22 + A-35 report. Best-fitting member.

lik_bf_H5 = 0.25   # ~1/4 as expected as under H-16. A-35 (corrected) puts the properly-conditioned Bayes
                   # factor at order 4 (~3.9–4.4) FOR single introduction, i.e. the topology data are ~4x less
                   # expected under two introductions than under one. Uses the CORRECTED order-4 magnitude —
                   # NOT the pre-correction "at least 4.4" and NOT the unreconciled ~7.4 second route (A-35
                   # flags the precise size as unsettled, and notes Weissman's parameters were chosen to favour
                   # I2, so order-4 is already the conservative end of the reversal). Not pushed below ~0.25
                   # (i.e. no stronger ratio) because the corrected BF still rests on Pekar's model- and
                   # ascertainment-dependent FAVITES+BEAST framework; that residual softening is carried by t,
                   # not by inflating this ratio (rule 5 — dispute over the diagnosis is not a separate factor).

t_bf = 0.5         # cap = min trust_score over {O-21, O-22} = 0.5 — both are sourced to S-22 (Weissman;
                   # trust 0.5); the underlying Pekar data they re-read (S-1) is 0.6. Left AT the cap, not
                   # docked further: O-21 and O-22 are direct quotes from Pekar's version-of-record and
                   # supplement, so the DATA (what Pekar reported and how the calc was structured) is reliably
                   # transcribed. The contested part — whether the asymmetry is genuinely an error (disputed by
                   # Stansifer) — is an argument-validity question that A-35's "corrected" status adjudicates in
                   # direction, and it is already priced into S-22's 0.5 trust_score; t=0.5 keeps half the
                   # update weight on the prior (rule 4).

evidence("HC-2", ["O-21", "O-22"], [lik_bf_H5, lik_bf_H16], t=t_bf)
```
