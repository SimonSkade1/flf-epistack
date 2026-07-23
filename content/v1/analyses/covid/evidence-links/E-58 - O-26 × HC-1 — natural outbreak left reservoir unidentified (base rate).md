---
type: evidence-link
id: "E-58"
from: "[[O-26 - The natural reservoir and the index case exposure route were not identified by the 1976 Ebola investigation]]"
to: "[[HC-1 - Origin of SARS-CoV-2 — natural zoonosis vs research-related incident]]"
arguments:
  - "[[A-42 - The hospital-centred Ebola case series reflects iatrogenic amplification, so the detected cluster locates the amplifying venue not the zoonotic spillover]]"
---
![[O-26 - The natural reservoir and the index case exposure route were not identified by the 1976 Ebola investigation]]

## Why this is evidence
That a clearly natural outbreak (1976 Ebola) left its animal reservoir and index source unidentified is a base rate showing that failure to find SARS-CoV-2's reservoir (O-27) is weak lab evidence — raising P(no reservoir found | H-41) and blunting the inference toward the lab members.

## Likelihood

```python
# E-58 (HC-1) — lone edge, one observation O-26 "a confirmed natural zoonosis (1976 Yambuku Ebola) left its
# animal reservoir and index exposure route unidentified". A BASE-RATE / precedent datum: it establishes that
# reservoirs commonly go unfound even for outbreaks known to be natural, which makes SARS-CoV-2's own missing
# reservoir (O-27, priced separately at E-59) consistent with natural origin. It therefore FAVOURS H-41 over
# the lab bloc {H-42, H-43}; it does NOT distinguish H-42 from H-43 (neither needs a trade reservoir, so the
# precedent carries no differential pull between them). Members in HC-1.hypotheses order [H-41, H-42, H-43,
# H-44]. Anchored on H-41 = 1; lab members priced as ratios to it (rule 7). A-42 (approved) reinforces the
# datum: the visible Yambuku cluster is an iatrogenic-amplification/ascertainment artifact and the true
# spillover was left permanently unresolved by the outbreak record — i.e. a genuine natural zoonosis whose
# reservoir the data never located. NOTE: this edge points OPPOSITE to E-59 on the same "was a host found"
# question; each is priced on its own and the runner composes them.
lik_ebola_H41 = 1.0    # anchor: under natural zoonosis the "no reservoir found" state is exactly what this
                       # precedent shows to be normal, so O-26 sits most comfortably here
lik_ebola_H42 = 0.8    # ~0.8x: under an unmodified-collection leak SARS-CoV-2's missing host is explained by
                       # there being no trade reservoir at all, so the reservoir-unfound precedent adds little
                       # — modestly less favoured than under H-41
lik_ebola_H43 = 0.8    # identical to H-42: an engineered leak likewise needs no trade reservoir, and O-26 does
                       # not discriminate the two lab members
lik_ebola_H44 = 0.9    # residual, unconstrained: some unlisted/hybrid origins involve natural spillover and
                       # some don't — middling, near-neutral
t_ebola = 0.85         # cap = trust_score of S-88 = 0.85 (International Commission 1978, canonical first Ebola
                       # investigation, hospital-amplification finding never overturned in 45 yr). At cap: the
                       # raw datum — that the 1976 reservoir/index source was never identified — is solidly
                       # established (the excluded "seropositive villagers" detail is already stripped in O-26,
                       # so no measurement weakness remains in what is stated). The one-Ebola-case reference-class
                       # generalisation is an inference-strength matter, priced in the modest ratio above, not a
                       # data-reliability dock.
evidence("HC-1", ["O-26"], [lik_ebola_H41, lik_ebola_H42, lik_ebola_H43, lik_ebola_H44], t=t_ebola)
```
