---
type: evidence-link
id: "E-59"
from: "[[O-27 - Nationwide survey of -80,000 wildlife, livestock and poultry samples across 31 Chinese provinces found zero SARS-CoV-2 positives]]"
to: "[[HC-1 - Origin of SARS-CoV-2 — natural zoonosis vs research-related incident]]"
---
![[O-27 - Nationwide survey of -80,000 wildlife, livestock and poultry samples across 31 Chinese provinces found zero SARS-CoV-2 positives]]

## Why this is evidence
A nationwide search finding no intermediate host, reservoir, or close relative in Chinese wildlife/livestock is what H-42/H-43 predict (no trade-chain reservoir needed), whereas H-41 (spillover via the animal trade) predicts a findable intermediate — weakly favouring the lab members, heavily caveated by absence-of-evidence (cf. O-26).

## Likelihood

```python
# E-59 (HC-1) — lone edge, one observation O-27 "a nationwide Chinese survey of >80,000 animals across 31
# provinces found zero SARS-CoV-2 positives, and no relative in wildlife". A trade-chain zoonosis (H-41) posits
# a real intermediate/reservoir host that a nationwide search should have some chance of hitting; the lab
# members {H-42, H-43} need NO trade reservoir, so a clean negative is fully expected under both. So the datum
# FAVOURS the lab bloc over H-41, and does NOT discriminate H-42 from H-43. Members in HC-1.hypotheses order
# [H-41, H-42, H-43, H-44]. Anchored on the lab members = 1; H-41 priced as a ratio to that (rule 7). This edge
# points OPPOSITE to E-58/O-26 on the same "was a host found" question — priced here on its own; the runner
# composes E-58's base-rate blunting as a separate factor, so I do NOT re-bake the general "reservoirs are often
# unfound" base rate into this ratio (that would double-count E-58).
lik_survey_H41 = 0.7   # ~0.7x as expected under H-41: a genuine trade-chain host "should" be findable, but this
                       # ratio is kept close to the anchor for weaknesses INTRINSIC to this observation only —
                       # the survey was largely post-outbreak, the sampled species-frame vs the actual trade
                       # chain is undocumented, and market animals were removed before sampling — so a true host
                       # could sit outside the frame and yield a negative even under H-41. The general base rate
                       # that reservoirs stay unfound is deliberately left to E-58. Net: weak tilt to the lab bloc.
lik_survey_H42 = 1.0   # anchor: an unmodified-collection leak needs no trade reservoir, so a nationwide
                       # negative is exactly what it predicts
lik_survey_H43 = 1.0   # identical to H-42: an engineered leak likewise predicts no findable trade host; O-27
                       # does not separate the two lab members
lik_survey_H44 = 0.85  # residual, unconstrained: some unlisted origins imply a findable host and some don't —
                       # middling, slightly below the lab anchor
t_survey = 0.45        # cap = trust_score of S-34 = 0.55 (WHO-China joint report; raw data never shared, large
                       # negatives not independently verifiable). Docked below the cap for the search's timing/
                       # completeness specifically: it was substantially post-outbreak and China-CDC-gatekept
                       # with an undocumented sampling frame, so how much a null result should move us is further
                       # limited beyond the generic unverifiability already in the 0.55 cap.
evidence("HC-1", ["O-27"], [lik_survey_H41, lik_survey_H42, lik_survey_H43, lik_survey_H44], t=t_survey)
```
