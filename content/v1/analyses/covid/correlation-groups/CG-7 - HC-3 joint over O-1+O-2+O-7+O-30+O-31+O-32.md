---
type: correlation-group
id: CG-7
to: "[[HC-3 - Causal role of the Huanan Seafood Market in the emergence]]"
members:
  - "[[E-6 - O-1 × HC-3 — marginal, unstable market centrality]]"
  - "[[E-7 - O-2 × HC-3 — alternative landmark equally admissible center]]"
  - "[[E-8 - O-7 × HC-3 — declining early market-linkage fraction]]"
  - "[[E-9 - O-30 × HC-3 — cases cluster on market vs population null]]"
  - "[[E-10 - O-31 × HC-3 — both lineages cluster near market]]"
  - "[[E-11 - O-32 × HC-3 — unlinked cases even closer than linked]]"
---

Joint likelihood for correlated observations O-1, O-2, O-7, O-30, O-31, O-32 (shared basis: D-2). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-7 (HC-3) — ONE joint estimate over members E-6+E-7+E-8+E-9+E-10+E-11: all six observations rest on the
# SAME early-Wuhan case-location dataset D-2 (rule 1), so they are one witness — the crux geospatial dataset,
# judged as a single pattern, not six independent draws. Members in HC-3.hypotheses order:
# [H-14 market spillover origin, H-15 externally-seeded amplifier, H-19 detection/ascertainment artifact, H-45 residual].
#
# THE WHOLE PATTERN: cases tightly cluster on the market vs a population-density null (O-30: median 4.28 vs
# 16.11 km, p<0.001), both independent lineages A and B center there (O-31), market-UNLINKED cases live even
# CLOSER than linked ones (O-32: 4.00 vs 5.74 km, p=0.029), and early market-linkage falls 55%->8.6% over time
# (O-7). Against this, the Stoyan/Chiu re-analysis finds the market only marginally/unstably the case center,
# decaying to non-significance as the sample shrinks (O-1) and sitting at the EDGE of the centroid cloud with
# Wanda Plaza an equally admissible center (O-2). Anchored on H-14 = 1 (best-fit member); others as ratios.
#
# H-14 and H-15 are NOT separated by geospatial clustering alone — a market that is the true spillover origin
# and a market that amplifies an externally-seeded introduction both predict market-centered cases, both
# lineages there, and unlinked-cases-even-closer. That origin-vs-amplifier split is carried by the metagenomic
# unit (CG-8), so it is deliberately NOT priced here; setting them equal leaves their ratio to the prior + CG-8.
lik_geo_H14 = 1.0   # anchor: a causally-central market is the natural generator of the whole pattern — tight
                    # clustering, both lineages centering, and (the load-bearing datum) unlinked cases even
                    # closer than linked (O-32, A-44 approved). Not dinged below 1 by the Stoyan/Chiu
                    # marginality (O-1/O-2): centrality != origin cuts both ways (A-2 approved), so a true
                    # origin's case centroid can sit off-market as cases radiate into denser residential areas.
lik_geo_H15 = 1.0   # set EQUAL to H-14: geospatial clustering does not discriminate origin from amplifier
                    # (both predict a market-centered case cloud incl. both lineages and unlinked-even-closer).
                    # The tiny "amplifier from outside should leave some pre-market origin cases" asymmetry is
                    # NOT priced here to avoid manufacturing a split the metagenomics (CG-8) is meant to carry.
lik_geo_H19 = 0.4   # ~2.5x less expected than a causally-central market. H-19 (pure ascertainment artifact)
                    # comfortably accommodates O-1/O-2 (it PREDICTS weak, unstable market centrality) and O-7
                    # (inflated by market-seeking case-finding, A-18 approved). It strains on O-31 (both
                    # INDEPENDENT lineages centering) and above all O-32: market-LINK ascertainment predicts
                    # linked cases nearest, yet unlinked are closer (A-44 approved) — H-19 must fall back on a
                    # distinct residual proximity/hospital-catchment ascertainment (A-44's caveat) to survive.
                    # Kept off ~0.3 (not lower) because A-1/A-2 (approved) genuinely blunt the market-causal
                    # inference ("data cannot single out the market") and that hospital-catchment escape is a
                    # live, if strained, route to spatial clustering. Kept off ~1.0 because O-32/O-31 are real
                    # anti-artifact signal. Scoped: the critiques attack "single out the market," not "clustering
                    # is fake," so they cap H-14's support without matching H-19 to it.
lik_geo_H45 = 0.6   # residual, unconstrained (rule 3): most unlisted market roles that are causally special in
                    # SOME way (non-primary co-spillover site, cold-chain-as-origin, single-individual seeding)
                    # still make the market a genuine geographic focus and so reproduce this pattern — hence
                    # middling-high, below the clean causal members but well above the pure-artifact reading.
t_geo = 0.50        # cap = min trust_score over the named observations = min(S-23=0.72 for O-1/O-2, S-13=0.78
                    # for O-7, S-17=0.55 for O-30/O-31/O-32) = 0.55. Docked to 0.50 for one specific weakness in
                    # D-2 not fully inside S-17's 0.55: the residential locations themselves are ascertainment-
                    # biased (field teams concentrated on central-Wuhan hospitals near the market — D-2
                    # known_biases, the A-44 caveat), a proximity mechanism distinct from the market-LINK bias,
                    # that could inflate even the unlinked-even-closer result the whole pattern's edge rests on.
evidence("HC-3", ["O-1", "O-2", "O-7", "O-30", "O-31", "O-32"], [lik_geo_H14, lik_geo_H15, lik_geo_H19, lik_geo_H45], t=t_geo)
```
