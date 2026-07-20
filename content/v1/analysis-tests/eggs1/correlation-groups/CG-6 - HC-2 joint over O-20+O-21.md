---
type: correlation-group
id: CG-6
to: "[[HC-2 - Net direction of egg's effect on hard cardiovascular and mortality endpoints]]"
members:
  - "[[E-22 - O-20 x HC-2 - PURE 21-country null for lipids, mortality and major CVD]]"
  - "[[E-23 - O-21 x HC-2 - PURE-only lower-MI signal failed to replicate in ONTARGET-TRANSCEND]]"
---

Joint likelihood for correlated observations O-20, O-21 (shared basis: D-7). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-6 (HC-2) - ONE joint estimate over E-22 + E-23. Both observations come from S-11 / the PURE
# programme resting on D-7 (rule 1), so they are one witness, not two. The pattern judged whole is:
# a 21-country, 146k-participant, 14.7k-event cohort finds NO association on lipids, all-cause
# mortality or major CVD, AND its one deviating secondary signal (higher intake -> lower MI) fails
# to replicate in ONTARGET/TRANSCEND and is disowned by the authors. Read jointly this is a single
# clean null, NOT "a null plus a protective finding": the non-replication is part of the null.
# Members in HC-2.hypotheses order: [H-2, H-3, H-4, H-9, H-10, H-12].
# Anchored on H-10 = 1 (rule 7); others are ratios to it.

lik_pure_H10 = 1.0   # ANCHOR. PURE is exactly H-10's stated scope - diverse global populations across
                     # low/middle/high income - and reports nulls on precisely H-10's three endpoint
                     # families (lipids, CVD, mortality). This is the single most direct test of the
                     # broad-scope null that exists in this evidence set; the joint pattern (null +
                     # a spurious sub-signal that does not replicate) is what a true global null
                     # generates. Nothing else in the cluster predicts this pattern as tightly.

lik_pure_H4  = 0.55  # 0.55x. H-4 also says ~null, and its reverse-causation rider positively predicts
                     # the second half (apparent inverse signals turning out artefactual, which is
                     # exactly the ONTARGET/TRANSCEND non-replication). Docked because H-4's claim is
                     # scoped to ischemic heart disease and says nothing about all-cause mortality or
                     # lipids - two thirds of the observed null are outside what H-4 commits to, so it
                     # would have been unsurprised by a positive mortality signal here. Does not cover
                     # non-Western populations explicitly.

lik_pure_H9  = 0.40  # 0.40x. H-9 asserts a null only in generally healthy Western adults up to ~1/day.
                     # PURE is majority non-Western and mostly low-intake, so most of the observed
                     # pattern falls OUTSIDE H-9's scope: H-9 is compatible with it but does not
                     # predict it - a non-Western signal in either direction would leave H-9 intact.
                     # Lowest of the three null members for that reason (per the flagged scope-overlap
                     # issue: the spread across nulls is driven by whose scope PURE actually tests).

lik_pure_H2  = 0.12  # 0.12x. H-2 (moderate ~1/day protective on CVD) predicts a visible protective
                     # association on major CVD in a 14.7k-event cohort spanning 21 countries. It got
                     # none, and the one protective-looking signal (MI) failed external replication -
                     # the worst joint fit in the cluster. Not lower because PURE's egg intake is low
                     # in most regions, so the ~1/day contrast H-2 speaks to is thinly sampled.

lik_pure_H3  = 0.15  # 0.15x. H-3 (high intake raises all-cause mortality, esp. diabetics) predicts a
                     # positive mortality association; PURE's primary all-cause-mortality analysis is
                     # flat. Marginally above H-2 only because PURE has little high-intake exposure at
                     # all, so its power against the specifically HIGH-intake arm of H-3 is weak, and
                     # the diabetic subgroup is not what the primary analysis reports.

lik_pure_H12 = 0.45  # 0.45x. Residual / direction-varies (rule 3). Unconstrained members accommodate
                     # most patterns, and H-12 can absorb this one - a J-shape averaging to null across
                     # 21 heterogeneous countries is entirely possible. Docked below the null members
                     # because a genuinely direction-varying effect would be the likeliest of all to
                     # show heterogeneity SOMEWHERE across 21 countries and income levels, and PURE's
                     # regional analyses surfaced none that survived. Kept well clear of zero: an
                     # unmodelled or intake-dependent mechanism producing a flat global average is not
                     # something this observation rules out.

t_pure = 0.60        # cap = trust_score of S-11 = 0.8 (both observations share that source). Docked
                     # to 0.60 for weaknesses between raw data and the stated observation, per D-7's
                     # known_biases: diet from a single baseline FFQ varying by country and language
                     # (large non-differential misclassification, which biases toward the null - and a
                     # null is precisely what is observed here, so this is not a neutral flaw); low egg
                     # intake in most PURE regions leaving little high-intake contrast; residual
                     # confounding by region and income level. Not docked further because the endpoint
                     # ascertainment (14,700 adjudicated composite events) is the strong part.

evidence("HC-2", ["O-20", "O-21"],
         [lik_pure_H2, lik_pure_H3, lik_pure_H4, lik_pure_H9, lik_pure_H10, lik_pure_H12],
         t=t_pure)
```
