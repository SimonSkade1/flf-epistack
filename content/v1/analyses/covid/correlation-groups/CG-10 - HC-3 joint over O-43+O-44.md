---
type: correlation-group
id: CG-10
to: "[[HC-3 - Causal role of the Huanan Seafood Market in the emergence]]"
members:
  - "[[E-25 - O-43 × HC-3 — wildlife trade present at Huanan]]"
  - "[[E-26 - O-44 × HC-3 — susceptible mammals sold live in volume]]"
---

Joint likelihood for correlated observations O-43, O-44 (shared basis: S-19). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-10 (HC-3) — ONE joint estimate over members E-25 + O-43 and E-26 + O-44: both observations rest on
# S-19 (Xiao et al. 2021), the same pre-pandemic vendor survey (rule 1). Members in HC-3.hypotheses order:
# [H-14 primary wildlife-to-human spillover origin, H-15 externally-seeded amplifier, H-19 detection
# artifact, H-45 residual]. The pattern judged whole: systematic monthly surveys documenting 47,381 wild
# animals across 38 species with 7 wild-animal shops AT Huanan (O-43), including SARS-CoV-2-susceptible
# mammals on sale in VOLUME — raccoon dog ~38/mo, civet ~11/mo, mink ~10/mo (O-44). This establishes the
# animal-side PRECONDITION for a market spillover, not the spillover event (A-53 approved: feasibility ≠
# occurrence — the survey shows the opportunity existed, provides no infected animal, so the update is
# BOUNDED). Anchored on H-14 = 1; other members priced as ratios to it (rule 7).

lik_wildlife_H14 = 1.0   # anchor: H-14 (spillover origin at the market) REQUIRES susceptible host species
                         # physically present and sold under high-contact conditions — so documented
                         # susceptible mammals on sale in volume is near-entailed by this member (~1.0).
                         # A-53 (approved): the same taxa (raccoon dog/civet) as the 2003 SARS-CoV-1 civet-
                         # market spillover, sold live, caged/stacked, on-site slaughter → both animal-side
                         # preconditions met. Best-fitting member for this observation.

lik_wildlife_H15 = 0.6   # 0.6× as expected as under H-14: an externally-seeded amplifier (infected people /
                         # cold-chain) does NOT require susceptible wildlife to be present — the animals are
                         # incidental to the mechanism. Not forbidden, though: Wuhan wet markets like Huanan
                         # commonly traded wildlife in volume pre-2020, so seeing it is only modestly
                         # surprising under H-15. The observation defeats a specific "no live mammals sold"
                         # counterclaim but not H-15 itself, which is compatible with wildlife present →
                         # discrimination kept modest (a precondition met, per A-53, not the event).

lik_wildlife_H19 = 0.6   # 0.6×, same as H-15: a detection/ascertainment artifact (market causally
                         # incidental, cluster from biased case-finding) likewise does not require or predict
                         # susceptible animals — their presence is background, at the same wet-market base
                         # rate as under H-15. No reason to split H-15 and H-19 on THIS observation.

lik_wildlife_H45 = 0.7   # 0.7×: unlisted market role, unconstrained — neither expects nor forbids
                         # susceptible wildlife on sale. Middling, slightly above H-15/H-19 because some
                         # residual roles (e.g. a genuine but non-primary co-spillover site among several
                         # locations) would also involve susceptible animals, while others would not. Lower
                         # would assert no unlisted role could produce the pattern, which I don't know (rule 3).

t_wildlife = 0.80        # cap = min trust_score over {O-43, O-44} = S-19 = 0.80, taken at the cap (rule 4):
                         # systematic pre-pandemic monthly surveys, not origins-motivated, independently
                         # corroborated by later market-photo evidence of the same species/stalls. The one
                         # data limitation (vendor-reported quantities; O-44 counts aggregated across the four
                         # markets, not broken out per-market) is already priced into the 0.80 trust_score and
                         # does not touch the observation's load-bearing claim (susceptible wildlife on sale in
                         # volume, incl. Huanan wild-animal shops), so no further markdown.

evidence("HC-3", ["O-43", "O-44"], [lik_wildlife_H14, lik_wildlife_H15, lik_wildlife_H19, lik_wildlife_H45], t=t_wildlife)
```
