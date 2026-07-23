---
type: hypothesis-cluster
id: "HC-3"
question: "What causal role did the Huanan Seafood Market play in the emergence — the site of the primary spillover into humans, a venue that amplified a virus introduced from outside, or a detection artifact that was not causally special?"
hypotheses:
  - "[[H-14 - The market environmental pattern reflects wildlife-associated emergence at the Huanan market]]"
  - "[[H-15 - The market may have been an amplification venue seeded by infected humans, not necessarily the origin]]"
  - "[[H-19 - The Huanan-market early-case clustering is largely an ascertainment-bias artifact, not evidence of a market spillover]]"
  - "[[H-45 - The market's role is something not listed here]]"
exclusivity: "The market was either where the animal-to-human spillover first occurred (H-14), or a downstream venue that amplified a virus introduced from outside — infected people or contaminated goods (H-15), or not causally special at all, its early-case prominence being a detection/ascertainment artifact (H-19). These causal roles are mutually exclusive; the residual holds any other role."
exhaustive_by_construction: false
independence: "The market's role is a distinct sub-question scored by its own case-geography, environmental-sampling and wildlife-trade evidence; its prior does not require fixing the origin mechanism, though its answer is strongly correlated with origin (see depends_on)."
depends_on:
  - "[[HC-1]]: a primary wildlife-to-human spillover at the market (H-14) essentially entails natural zoonosis, and the 'market is a detection artifact' answer (H-19) is the position associated with a non-market (e.g. research-related) origin, so this cluster's answer is strongly correlated with HC-1; kept separate (distinct market/geospatial/wildlife evidence) so treat the priors as only approximately independent."
  - "[[HC-2]]: under natural zoonosis the two inferred introductions are both placed at the market, so the wildlife-spillover answer (H-14) co-varies with the two-or-more-introductions answer of HC-2; this is mediated by the shared zoonosis picture rather than a direct dependence."
relevance: "If the market was the primary spillover site, natural zoonosis is favoured; if its early-case prominence is a detection artifact, a non-market origin — including a research-related one — is left open."
---
A genuinely separable sub-question with its own evidence: early-case geography and its statistical critiques, the distribution of environmental positives and species genetic material within the market, and the pre-pandemic wildlife-trade inventory.

![[H-14 - The market environmental pattern reflects wildlife-associated emergence at the Huanan market]]

![[H-15 - The market may have been an amplification venue seeded by infected humans, not necessarily the origin]]

![[H-19 - The Huanan-market early-case clustering is largely an ascertainment-bias artifact, not evidence of a market spillover]]

![[H-45 - The market's role is something not listed here]]

## Carving

**Exclusivity.** The three named roles are causally distinct: H-14 makes the market the origin of the spillover; H-15 makes it a downstream amplifier of a virus that arrived from outside (whether via infected people or contaminated cold-chain goods — H-20, merged in); H-19 makes it causally incidental, prominent only because early testing concentrated on market-linked people. At most one is the market's true role; the residual (H-45) covers any other.

**Why H-10 (agnostic epicenter) and H-23/H-25/H-26 (the wildlife-vector claims) are merged into H-14, not co-members.** H-10 ("the market was the initial focus, mechanism unspecified") is logically the disjunction of the wildlife-spillover and amplifier readings, so it cannot be a mutually-exclusive co-member; it is merged into H-14 as the weaker form of the same "market was the origin" claim. H-23 (raccoon dogs were the intermediate host), H-25 (pangolins/bats were not the vector) and H-26 (the wildlife trade was a viable route) are not separate answers to *this* sub-question but sub-claims elaborating the wildlife-spillover answer; a standalone "which intermediate host" cluster would answer the same question as H-14 sliced by species and would double-count the species-correlation evidence (O-40, O-50, O-51). They are therefore merged into H-14, and that same species/route evidence discriminates H-14 from H-15 within this cluster at step 5. (This extends 4a's merges: 4a's note on H-14 had left H-23/H-10 out on the discriminability test — correct for dedup, but for MECE clustering they belong under H-14's answer.)

**Not exhaustive by construction — residual required.** Roles other than the three named ones are conceivable (e.g. the market as a coincidental super-spreading venue with no special relation to the origin), so H-45 keeps the cluster a proper probability space.

## Prior

```python
# HC-3 prior — causal role of the Huanan Seafood Market. Members in HC-3.hypotheses order:
# [H-14 primary wildlife-to-human spillover origin, H-15 externally-seeded amplifier (infected people or
#  cold-chain), H-19 detection/ascertainment artifact, H-45 residual].
# OUTSIDE VIEW ONLY: the base rate for what role a high-throughput venue plays when a novel outbreak's
# earliest detected cluster centers on it, BEFORE Wuhan's own geospatial / environmental / metagenomic
# evidence. Reference class = the precedents already in the graph, read here as base rates: SARS-CoV-1
# live-animal markets, where the market was the true spillover / amplifying interface (O-54, O-57 — HC-1
# inbound edges E-60/E-61, cited as precedent only, NOT marked here since they are not HC-3 inbound), vs the
# Ebola-Yambuku hospital (O-25/O-26) and the general superspreading-overdispersion (O-23) precedents, where a
# high-throughput venue amplified or merely recorded transmission it did not originate.
#
# Evidence marked used_for_prior (step 8 drops these): E-27 (O-23 superspreading base rate) and the
# correlation group CG-9 = E-28 + E-29 (O-25/O-26 Ebola precedent), marked all-or-none. These are
# outside-view reference-class facts about how first-detected venue clusters form, so they belong in the
# prior, not in a Wuhan-specific likelihood.
# LEFT UNMARKED for step 8 (case-specific, discriminating): E-6..E-26 — Wuhan early-case geography and its
# statistical critiques (O-1/O-2/O-7/O-30/O-31/O-32), the market environmental-positive distribution and
# species co-location (O-17..O-20/O-28/O-29/O-33/O-39..O-42/O-50/O-51), and the pre-pandemic wildlife-trade
# inventory (O-43/O-44). No-observation argument A-40 (approved, affects_hypotheses -> H-19, rule 6) informs
# H-19's weight via its GENERAL biased-case-finding mechanism only; A-40's Wuhan-specific strands (lineage
# A/B ordering, Bloom host-DNA non-correlation, Weibo/CDC geolocation, Levin reanalysis) are case-specific
# and are priced at step 8, not here. Arguments A-41 (-> O-23) and A-42 (-> O-25/O-26) enter as the reasoning
# behind the two marked base rates, not as terms of their own.
# depends_on (approximation noted per step 4, no number imported): H-14 essentially entails HC-1 natural
# zoonosis and co-varies with HC-2's two-introductions answer; H-19 is the reading associated with a
# non-market / research-related origin. Step 4 recorded these priors as only approximately independent of
# HC-1/HC-2; nothing cross-cluster is imported into the arithmetic below.

# Two-level decomposition. Level 1: is the venue causally special to the emergence at all, or a pure
# detection artifact? Level 2: given causally special, is it the origin or a downstream amplifier?

# H-14 primary spillover origin — the venue is where the animal-to-human jump first occurred. Would need the
# first-detected market cluster to reflect a real spillover interface (as SARS-CoV-1 markets did), not merely
# where a superspreader landed or where testing looked. Modal reading for a market venue-type, but held well
# under 50% on the outside view: it is precisely the Wuhan-specific environmental/geospatial evidence (left
# for step 8) that is meant to lift it, not the base rate. Most confident member, but only narrowly.

# H-15 externally-seeded amplifier — the market amplified a virus introduced from outside, by infected people
# or contaminated cold-chain goods. Would need the venue to be downstream of an origin elsewhere. This is the
# modal outcome across the hospital/farm precedents (Ebola-Yambuku, MERS nosocomial clusters, Nipah pig
# farms), which is why it sits nearly level with H-14. Does not cover a pure testing artifact (that is H-19).

# H-19 detection/ascertainment artifact — the market is causally incidental, prominent only because early
# case-finding over-sampled venue-linked people. Overdispersed individual infectiousness (O-23, SARS k~0.16;
# argument A-41) means a chance superspreader can manufacture a venue cluster unrelated to the spillover
# point, and early case definitions can over-represent one setting (A-40's general mechanism). But across
# emerging outbreaks the first-recognized venue cluster is more often causally connected than pure
# coincidence, so this stays below a third. Least confident of the three named readings, but non-trivial.
p_artifact = 0.22   # H-19: venue causally incidental; needs the cluster to be mostly testing/superspreading coincidence

# Level 2 — origin vs amplifier, given the venue IS causally special. The crux the Wuhan-specific evidence
# later resolves, so the outside view is deliberately near-balanced. The SARS-CoV-1 market precedent (venue =
# true spillover interface) pulls toward origin; the Ebola/MERS/Nipah precedents (venue = amplifier of an
# externally-seeded introduction) pull toward amplifier. Reasoning over BOTH precedent families — not the
# wildlife-market specifics, which are E-25/E-26 evidence reserved for step 8 — leaves only a slight edge to
# origin for a market venue-type. This 0.52 is the single most load-bearing number in the block (flag for
# steps 9-10): moving it to 0.5 equalises H-14 and H-15 in the prior.
share_origin = 0.52   # origin : amplifier ~ 0.52 : 0.48 given causally special

w_H14 = (1 - p_artifact) * share_origin        # H-14 primary spillover origin
w_H15 = (1 - p_artifact) * (1 - share_origin)  # H-15 externally-seeded amplifier
w_H19 = p_artifact                              # H-19 detection/ascertainment artifact

# H-45 residual — its own argued weight (rule 4), not 1 - sum. What an unmodelled market role would concretely
# look like: a genuine but non-primary co-spillover site among several locations (not "the primary site"), or
# a role entangled with the origin that none of the three clean readings captures — e.g. cold-chain as the
# actual origin rather than a mere amplification seed, or a single infected individual seeding the market in a
# way that is neither generic external amplification nor pure ascertainment. Weighted by how often, in
# comparable venue-cluster questions, the truth escaped a clean origin/amplifier/artifact trichotomy —
# uncommon, since those three roles are near-exhaustive, but nonzero.
w_H45 = 0.06   # ~6% of normalised mass; unmodelled-role catch-all

prior("HC-3", [w_H14, w_H15, w_H19, w_H45])
```

