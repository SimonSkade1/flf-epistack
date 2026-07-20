---
type: correlation-group
id: CG-1
to: "[[HC-1 - Route of the first human SARS-CoV-2 infection]]"
members:
  - "[[E-1 - O-1 × HC-1 — environmental positives cluster in the live-wildlife section]]"
  - "[[E-2 - O-2 × HC-1 — no animal-origin sample at Huanan tested positive]]"
---

Joint likelihood for correlated observations O-1, O-2 (shared basis: D-2). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-1 (HC-1) — ONE joint estimate over members E-1 + E-2: O-1 and O-2 both rest on D-2, the same China
# CDC Huanan swab campaign reported in S-2, so they are one witness and are priced together (rule 1).
# Members in HC-1.hypotheses order: [H-1 Huanan market spillover, H-5 WIV research incident, H-6 residual].
#
# THE PATTERN, judged whole (process 3): "SARS-CoV-2 contamination is present and spatially concentrated
# in the western live-wildlife section (74/923 swabs, one carrying a lineage-A genome), while none of the
# 457 animal-origin samples across 18 species is positive." Not the product of two separate guesses —
# the second half is largely explained away by the same sampling campaign's timeline that produced the
# first half, so the pair is far less surprising jointly than the halves look separately.
# Anchored on H-1 = 1; the other two priced as ratios to it (rule 7a).

lik_swabs_H1 = 1.0    # ANCHOR. H-1 is the member that predicts the spatial half of the pattern outright:
                      # if the index infection happened at Huanan via live wildlife, contamination should
                      # be densest exactly where those animals were caged and slaughtered, which is what
                      # the western-section gradient shows. The animal-negative half is a mild miss even
                      # here — under H-1 a timely sample would plausibly have caught something — but A-1
                      # (corrected) prices that miss down a long way: collection of animal material began
                      # 18 Jan, after the 1 Jan closure, disinfection, and removal of most live wildlife,
                      # so the taxa most likely to be infected were physically absent from the sampled
                      # pool. Not zero cost though: 457 samples across 18 species were actually obtained,
                      # so per A-1 the attenuation is severe but partial. Anchor scale is free.

lik_swabs_H5 = 0.3    # ~0.3x as expected as under H-1. Conditioning strictly on H-5 being true (process
                      # 2 — H-5's plausibility is the prior's job, priced in step 7, not mine): a WIV
                      # incident makes Huanan a pure human-amplification venue, so contamination is
                      # expected there, and the animal-negative half is predicted with near-certainty,
                      # which fits better than under H-1. What it fits badly is the spatial gradient:
                      # human shedding should track footfall, stall density, drains and toilets, not the
                      # live-wildlife stalls specifically. Not much lower, because the western section
                      # was also crowded, poorly ventilated and wet, and the concentration is a gradient
                      # rather than an exclusive localisation, so a footfall/environment confound can
                      # reproduce a fair fraction of it. Most arguable number in the block.

lik_swabs_H6 = 0.55   # ~0.55x. Real and argued (rule 3), and genuinely middling because H-6 is a mixture
                      # that straddles the pattern rather than an explanation blind to it. Its dominant
                      # leg — spillover upstream in the supply chain (farm, trapper, trader) with an
                      # infected animal or handler then arriving at Huanan — reproduces the wildlife-
                      # section gradient about as well as H-1 does, and predicts the animal-negative
                      # result slightly better since fewer market animals need ever have been infected.
                      # Its smaller legs (distant spillover with silent human introduction into Wuhan; a
                      # research incident at a non-WIV Wuhan institution) look like H-5 on this pattern.
                      # Sitting between the two named members is the honest reading, not a hedge.

t_huanan_swabs = 0.62 # cap = trust_score of S-2, the source behind both O-1 and O-2, = 0.72 (min over
                      # {O-1, O-2}; same source, so no mixed-trust question). Docked below the cap for two
                      # named weaknesses in the step from raw data to the stated observations, both about
                      # the data pipeline rather than about whether any member is true (rule 4):
                      # (i) SITE SELECTION — swab locations were chosen by the field teams after the
                      # market was already publicly implicated, so the spatial distribution of *sampling
                      # effort* is not independent of the spatial hypothesis the positives are read as
                      # supporting, and the per-section denominators needed to rule that out are not
                      # recoverable from the report; (ii) the ~13-month lag before the raw metagenomic
                      # reads were released meant the positivity calls and the section-level mapping went
                      # unauditable by outside groups for that whole period, and the analysis pipeline
                      # that produced them could not be independently inspected. Post-disinfection timing
                      # is deliberately NOT docked here: A-1 already moved it into the likelihoods above,
                      # and docking t as well would count the same weakness twice.

evidence("HC-1", ["O-1", "O-2"], [lik_swabs_H1, lik_swabs_H5, lik_swabs_H6], t=t_huanan_swabs)
```
