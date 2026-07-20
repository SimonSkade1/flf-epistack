---
type: correlation-group
id: CG-4
to: "[[HC-1 - Route of the first human SARS-CoV-2 infection]]"
members:
  - "[[E-8 - O-11 × HC-1 — DEFUSE proposed inserting furin cleavage sites at the WIV]]"
  - "[[E-9 - O-12 × HC-1 — DARPA rejected the DEFUSE proposal]]"
---

Joint likelihood for correlated observations O-11, O-12 (shared basis: S-15). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-4 (HC-1) — ONE joint estimate over members E-8 + E-9: O-11 and O-12 both rest on S-15, the leaked
# DEFUSE artifact (rule 1), so they are one witness and are judged as one pattern (process 3):
# "the exact spike modification SARS-CoV-2 exhibits was formally proposed by the implicated institutions
# ~18 months before emergence, and was rejected and left unfunded by that route."
# Members in HC-1.hypotheses order: [H-1 Huanan market spillover, H-5 WIV research incident, H-6 residual].
# Anchored on H-5 = 1 and the others priced as ratios to it (rule 7). O-12's discount lives inside this
# single call — it is not a second, independent update.

lik_defuse_H5 = 1.0   # anchor. Given a WIV research-related incident actually occurred, this documentary
                      # pattern is close to what you would expect to find: the institution that had the
                      # accident is exactly the institution that wrote down the plan for exactly this
                      # feature. Cited: A-5 (approved) — documented specific intent + capability raises
                      # P(furin site | lab origin at these institutions) while leaving the natural-origin
                      # denominator unmoved, i.e. LR > 1 on H-5. The anchor is NOT 1 "because H-5 is true":
                      # note the pattern is only partly expected even under H-5, since H-5 also covers
                      # collection/culture/passage incidents with an unmodified natural virus, for which
                      # the DEFUSE document is as much a coincidence as under H-1. The rejection (O-12)
                      # is what stops this member being priced far above the others: the proposal being
                      # unfunded by DARPA, with no leaked document showing the work ran via another
                      # funder, means intent is not execution (A-5's own stated bound), so a large part
                      # of what O-11 alone would buy is given straight back here.

lik_defuse_H1 = 0.40  # 0.40x as expected as under H-5. Deliberately NOT near zero: conditional on natural
                      # spillover at Huanan, the DEFUSE proposal still exists — its existence is a fact
                      # about a real, ongoing sarbecovirus research programme aimed at a genuinely
                      # circulating natural virus family in the same region, not a fact about how the
                      # pandemic started. A programme that studies the family that spilled over will
                      # plausibly have written proposals about that family's spike biology. So the
                      # coincidence required under H-1 is the tight match of the *specific* proposed
                      # feature (furin site insertion) to the feature the pandemic virus has, which is a
                      # real but far-from-impossible coincidence. Weakest number in the block; a reader
                      # who thinks the feature match is more of a fluke should raise it toward the anchor.

lik_defuse_H6 = 0.45  # 0.45x — middling and unconstrained (rule 3), slightly above H-1. H-6's two natural
                      # legs (upstream-supply-chain spillover; distant spillover with silent introduction)
                      # behave exactly like H-1 with respect to this document, which is what pins it near
                      # H-1's value. Its research-at-a-non-WIV-Wuhan-institution leg pushes in two
                      # directions at once and roughly cancels: O-11 names WIV/EcoHealth/Duke-NUS/UNC
                      # specifically and names no other Wuhan institution, so under a non-WIV research
                      # incident the document is a near-coincidence (arguing DOWN, and this is the
                      # discrimination E-8's body claims against H-6); but that leg is small inside H-6,
                      # and a non-WIV Wuhan lab plausibly sits in the same collaborative/technique milieu
                      # the proposal describes, so it is not wholly unexpected either. Net: a shade above
                      # H-1 because the leg is not fully coincidental, far below the anchor.

t_defuse = 0.70       # cap = min trust_score over {O-11, O-12} = 0.8 (both via S-15). Step 2 scored that
                      # 0.8 as authenticity of the leaked artifact, not as evidence any experiment ran.
                      # Docked to 0.70 for one named weakness in the raw-data-to-stated-observation step:
                      # O-12's "rejected ... citing gain-of-function and biosafety concerns" rests on
                      # secondary reporting of DARPA's decision rather than on the primary rejection
                      # letter in the leak, and the leak's completeness is unverifiable (an unreleased
                      # revised or successor submission would not appear in it), so the stated observation
                      # is slightly weaker than the artifact's authenticity alone would license.
                      # NOT docked for "the experiment may not have happened" — that is a likelihood
                      # judgement about the members and is priced above, not a data-reliability fact
                      # (rule 4 / process 5).

evidence("HC-1", ["O-11", "O-12"], [lik_defuse_H1, lik_defuse_H5, lik_defuse_H6], t=t_defuse)
```
