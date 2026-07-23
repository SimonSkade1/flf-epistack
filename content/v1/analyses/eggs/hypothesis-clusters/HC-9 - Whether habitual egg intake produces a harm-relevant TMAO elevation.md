---
type: hypothesis-cluster
id: HC-9
hypotheses:
  - "[[H-28 - The form-food-matrix of choline, not total choline content, determines TMAO generation]]"
  - "[[H-29 - Habitual whole-egg consumption does not meaningfully raise TMAO in people with normal renal function]]"
  - "[[H-30 - Impaired renal function may modify the TMAO response to egg-choline intake]]"
  - "[[H-42 - Eating eggs (-=2 yolks) raises TMAO production, feeding egg choline into the TMAO pathway]]"
  - "[[H-43 - The egg-induced TMAO rise may be clinically benign because it is postprandial and unaccompanied by inflammatory-oxidative changes]]"
  - "[[H-56 - Some other egg-TMAO relationship]]"
exclusivity: "Read as the single best summary of the egg->TMAO exposure and its relevance, the members give incompatible bottom-lines (negligible/form-limited, no fasting rise, renal-only, a real production rise, or a benign postprandial excursion), so at most one is correct."
exhaustive_by_construction: false
independence: "How much eggs raise TMAO is a food-exposure question separable from whether TMAO is causal (HC-8) and from the lipid pathway (HC-6)."
depends_on:
  - "HC-8: this exposure bears on harm only if TMAO is causal there"
question: "Does habitual egg intake produce a harm-relevant TMAO elevation, and under what conditions?"
relevance: "The egg-specific half of the TMAO thread - do eggs even feed the pathway meaningfully."
---

![[H-28 - The form-food-matrix of choline, not total choline content, determines TMAO generation]]

![[H-29 - Habitual whole-egg consumption does not meaningfully raise TMAO in people with normal renal function]]

![[H-30 - Impaired renal function may modify the TMAO response to egg-choline intake]]

![[H-42 - Eating eggs (-=2 yolks) raises TMAO production, feeding egg choline into the TMAO pathway]]

![[H-43 - The egg-induced TMAO rise may be clinically benign because it is postprandial and unaccompanied by inflammatory-oxidative changes]]

![[H-56 - Some other egg-TMAO relationship]]

## Carving

The sub-question is whether habitual egg intake produces a harm-relevant TMAO elevation and under what conditions. The members are competing characterizations of the magnitude/conditions of any egg-driven rise: negligible because egg phosphatidylcholine-choline is poorly converted relative to free choline (H-28); no meaningful fasting/steady-state rise in people with normal renal function (H-29); a rise only where renal clearance is impaired (H-30); a real postprandial production rise as egg choline enters the pathway at >=2 yolks (H-42); or a rise that occurs but is clinically benign, being postprandial and unaccompanied by inflammatory-oxidative change (H-43). Read as the single best bottom-line, at most one holds; the task's explicit poles H-42 (postprandial rise) and H-29 (fasting null) are the anchors, reconciled in reality by the postprandial-versus-fasting distinction that the members turn into competing summary verdicts. Residual H-56 covers a meaningful chronic steady-state elevation with clinical import. Its relevance is gated by HC-8 (whether TMAO is causal), noted in depends_on.

## Prior

```python
# HC-9 prior — whether habitual egg intake produces a harm-relevant TMAO elevation, and under what
# conditions. Members in HC-9.hypotheses order:
# [H-28 form/matrix governs (egg-PC poorly converted), H-29 no meaningful fasting rise in normal-renal,
#  H-30 renal-impairment-only rise, H-42 eggs (>=2 yolks) raise TMAO production, H-43 rise is clinically
#  benign, H-56 residual].
# Evidence split: nothing is marked used_for_prior. Every inbound edge is a case-specific trial result —
# the Wilcox mechanistic RCT (CG-27) and the Miller dose-response (CG-28) — all discriminating, all left
# for step 8. no_observation_arguments.py --cluster HC-9 returns none, so no argument moved a number.
# The prior rests on the mechanistic outside view only. The members overlap in reality (a postprandial
# rise, a fasting null, and benignity can all co-occur); the cluster forces the single best *summary
# verdict*, and these weights price which verdict is a priori most apt.

# H-42 anchor — "eggs (>=2 yolks) raise TMAO production." The mechanistic default: two yolks deliver
# ~250-300 mg choline, choline is an established TMA precursor, gut microbiota convert it, so a measurable
# (postprandial) rise is the naively expected consequence of eating a choline-dense food. The most apt
# default headline before any egg-specific trial is priced.
w_h42 = 1.0   # unit anchor: the mechanistic default "eggs feed the pathway"

# H-29 no meaningful fasting/steady-state rise in normal-renal people, odds vs H-42. What must hold: acute
# postprandial flux does not carry into fasting/steady-state levels because renal clearance and homeostasis
# buffer them. Reference class: habitual-intake biomarker questions where the chronic steady state is what
# bears on harm. Near-co-equal to H-42 (the two named poles of the carving); just below because the
# mechanistic default is that a choline load does move the marker at least acutely.
odds_h29_vs_h42 = 0.85   # the fasting-null pole, near-co-equal to the postprandial-rise anchor
w_h29 = odds_h29_vs_h42 * w_h42

# H-43 the rise occurs but is clinically benign, odds vs H-42. What must hold: a real postprandial
# excursion that saturates above ~4 yolks and moves no inflammatory/oxidative marker, so it does not
# translate to harm. Reference class: postprandial-metabolite excursions without downstream surrogate
# change. A strong contender for the true bottom line of the whole harm question, hence third; below the
# two anchors because it makes an extra (harm-irrelevance) claim.
odds_h43_vs_h42 = 0.70   # makes an added harm-irrelevance claim on top of a rise, so below the anchors
w_h43 = odds_h43_vs_h42 * w_h42

# H-28 chemical form / food-matrix (not total choline) governs TMA generation, egg-PC poorly converted,
# odds vs H-42. What must hold: phosphatidylcholine-bound choline is substantially less TMA-bioavailable
# than free choline, and form dominates amount. Reference class: choline-form bioavailability studies. More
# specific than the anchors (requires form to be the controlling variable), so below them.
odds_h28_vs_h42 = 0.55   # a stronger, more specific mechanistic claim than the anchors
w_h28 = odds_h28_vs_h42 * w_h42

# H-30 renal-impairment-only rise ("for whom"), odds vs H-42. What must hold: a normal-renal null but a
# rise where clearance is reduced, since TMAO is almost exclusively renally cleared (mechanistically well
# grounded). Reference class: renally-cleared-metabolite accumulation in CKD. Narrower than the others as
# THE single best overall summary because it speaks only to the impaired-renal minority, so below them.
odds_h30_vs_h42 = 0.40   # mechanistically sound but a subgroup-only summary of the whole question
w_h30 = odds_h30_vs_h42 * w_h42

# H-56 residual — a relationship none of the five express: a meaningful *chronic steady-state* TMAO
# elevation with clinical import in ordinary (normal-renal) people, or a route other than egg choline. Its
# own argued weight (rule 4): disfavoured because renal clearance and homeostasis are expected to buffer
# steady-state levels, but real (e.g. a high-conversion + slow-clearance subpopulation sustaining an
# elevation).
odds_other = 0.35   # ~0.35 : 1 vs the unit anchor; ~9% of the mass once normalised
w_h56 = odds_other

prior("HC-9", [w_h28, w_h29, w_h30, w_h42, w_h43, w_h56])
```
