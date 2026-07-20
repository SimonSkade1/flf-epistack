---
type: correlation-group
id: CG-2
to: "[[HC-1 - Route of the first human SARS-CoV-2 infection]]"
members:
  - "[[E-3 - O-4 × HC-1 — susceptible live wildlife routinely sold at Huanan]]"
  - "[[E-4 - O-5 × HC-1 — no bats or pangolins on sale at Wuhan markets]]"
---

Joint likelihood for correlated observations O-4, O-5 (shared basis: S-4). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-2 (HC-1) — ONE joint estimate over E-3 + E-4: O-4 and O-5 are presence and absence columns of the
# SAME census (S-4, May 2017-Nov 2019), so they are one witness, not two (rule 1). The pattern judged
# whole: "SARS-CoV-2-susceptible intermediate hosts (raccoon dogs, hog badgers) present in quantity at
# Huanan — 47,381 animals, 38 species — while the reservoir taxa (bats, pangolins) are entirely absent."
# Members in HC-1.hypotheses order: [H-1 Huanan market spillover, H-5 WIV research incident, H-6 residual].
# Anchored on H-1 = 1; H-5 and H-6 priced as ratios to it (rule 7). Each member is conditioned on strictly
# (process 2) — no prior-flavoured "lab leak is unlikely" leaks in here.

lik_census_H1 = 1.0   # anchor. H-1 (spillover at Huanan via live wildlife sold there) *entails* the
                      # first half: susceptible live mammals had to be physically on sale at Huanan, and
                      # the census confirms exactly that, in quantity, from pre-pandemic data collected
                      # before anyone had a thesis to defend. The second half cuts the other way but only
                      # within the zoonosis family: per A-2 (approved, checked), the bat/pangolin absence
                      # contradicts a necessary condition of the *direct* bat- or pangolin-sale route
                      # while contradicting no condition of the intermediate-host route that H-1's
                      # statement actually runs on. So the pattern removes H-1's simplest mechanism and
                      # supplies its needed precondition; net, still the member that predicts the whole
                      # pattern best, so it takes the anchor rather than a discount.

lik_census_H5 = 0.6   # 0.6x as expected as under H-1. Conditional on a WIV research incident, the
                      # species inventory of a Wuhan wet market is causally irrelevant — the pattern is
                      # then just the base rate for a large Chinese urban live-animal market. That base
                      # rate is not low: susceptible farmed mammals in the fur/meat trade are routine
                      # stock, and bats are essentially never sold for meat in central China, so the
                      # observed pattern is unremarkable under H-5. It is nonetheless less expected than
                      # under H-1, which forces the presence half rather than merely permitting it.
                      # Not below ~0.5: nothing in the pattern is improbable given H-5.

lik_census_H6 = 0.85  # 0.85x. Unconstrained member, so middling by default (rule 3), but nudged toward
                      # H-1 rather than to the midpoint: H-6's largest leg is a natural spillover
                      # upstream of Huanan (farmer/trapper/trader/transport) or at another Wuhan market,
                      # and that leg needs the same susceptible-mammal supply chain the census documents,
                      # while being positively comfortable with the reservoir taxa never reaching a
                      # retail floor at all. H-6's smaller non-WIV-research leg behaves like H-5. Kept
                      # below the anchor because H-6 only makes the pattern likely, it does not require
                      # it, and its research leg is indifferent to it.

t_census = 0.7        # cap = trust_score of S-4 = 0.8 (both observations, one source). Docked for two
                      # specific raw-data-to-observation weaknesses that step 6 explicitly left to be
                      # priced here (A-2's defeater probe): (i) the survey window ends Nov 2019 and the
                      # monthly vendor visits sample stock intermittently, so it does not directly
                      # observe what was on sale in the Nov-Dec 2019 window that matters; (ii) it records
                      # what surveyors saw and vendors reported over shop visits, not an exhaustive
                      # inventory, so a low-volume or clandestine taxon (exactly the case for a
                      # protected species like pangolin) could be under-recorded — an absence claim is
                      # more exposed to this than the presence claim, and the joint call inherits the
                      # weaker of the two. Not docked further: the counts are large, itemised and
                      # pre-registered against no origins thesis.

evidence("HC-1", ["O-4", "O-5"], [lik_census_H1, lik_census_H5, lik_census_H6], t=t_census)
```
