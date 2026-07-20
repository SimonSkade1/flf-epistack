---
type: hypothesis-cluster
id: HC-1
question: By what route did SARS-CoV-2 first infect a human?
hypotheses:
  - "[[H-1 - SARS-CoV-2 first infected humans via zoonotic spillover at the Huanan market]]"
  - "[[H-5 - SARS-CoV-2 first infected humans through a research-related incident at the WIV]]"
  - "[[H-6 - The first human infection arose by neither route listed here]]"
exclusivity: There was one first human infection, and it happened at one place by one mechanism; a market spillover, a WIV research-related incident, and anything else are mutually exclusive descriptions of that single event.
exhaustive_by_construction: false
independence: This is the only cluster in the analysis, so there is no other cluster's base rate for its prior to factorize from.
depends_on: []
relevance: This cluster *is* the main question — natural zoonotic spillover (H-1) versus a research-related incident (H-5), with H-6 covering the routes neither named option captures.
---

![[H-1 - SARS-CoV-2 first infected humans via zoonotic spillover at the Huanan market]]

![[H-5 - SARS-CoV-2 first infected humans through a research-related incident at the WIV]]

![[H-6 - The first human infection arose by neither route listed here]]

## Why this carving

The three surviving hypotheses do not form three competing answers to one question, so the carving decision was not free.

**H-1 and H-5 are genuinely exclusive** and both answer the same dimension — where and how the index infection occurred. Their step-3 `question` fields agree, and here the labels match the statements.

**H-3 (natural evolution/recombination in the wild *Rhinolophus* sarbecovirus reservoir) is not exclusive with either of them.** A virus can evolve naturally in bats *and* spill over at the Huanan market; it can equally evolve naturally in bats, be collected into a laboratory, and escape. H-3 is therefore compatible with every member of this cluster and cannot sit in it as a competing answer — putting it in would break exclusivity and make the cluster stop being a probability space.

**The tempting second cluster was rejected as evidence double-counting.** The obvious alternative is a second cluster on the *evolutionary origin* dimension: {H-3 "natural evolution", + a constructed complement "the genome was deliberately manipulated in a laboratory", + a residual}. That complement is, in this evidence base, H-5's own content restated: H-5 explicitly reads "potentially involving an engineered furin cleavage site of the kind proposed in DEFUSE", and the three observations that would discriminate the constructed cluster — O-10 (no furin cleavage site anywhere in the BANAL clade), O-11 (DEFUSE proposed inserting exactly such sites at the WIV), O-12 (DARPA rejected DEFUSE) — are the same three that discriminate H-5 from H-1 in this cluster, pushing in the same direction in both. Two clusters that are alternative slicings of one sub-question double-count that evidence at step 8, and rule 3 states plainly that no `depends_on` note repairs it. So the second cluster was not built.

**H-3 was therefore dropped as a straggler that clusters nowhere** — not because it is off-topic (it is not), but because it is a *background* claim rather than a competing answer: it is entailed by H-1, consistent with H-5, and its distinguishing content (natural versus engineered genome) already lives inside H-5's statement, where O-10/O-11/O-12 will score it exactly once. The genomic observations O-6 to O-9 are not orphaned by this: a naturally circulating, human-ACE2-binding sarbecovirus reservoir bears directly on H-1 versus H-5 within this cluster, since it speaks to whether a natural progenitor was available without laboratory involvement. See `agent-notes/structure.md` and the problem log for the pipeline tension this exposed (the ≥2-members rule leaves no non-distorting home for a true-but-non-competing hypothesis).

**Grain.** The two named members sit at comparable specificity — each names a place plus a mechanism (Huanan market via live wildlife; WIV via a research-related incident) — so neither is an over-narrow member competing against a broad one. H-6 carries everything outside both frames, which matters here because the curated evidence is doubly frame-bound: the market observations sample only Huanan, and the research observations concern only the WIV/EcoHealth DEFUSE consortium.

**Not exhaustive by construction**, hence the residual: the two named members are the two positions this literature argues, not a logical partition of the space of first infections.

## Prior

```python
# HC-1 prior — route of the first human SARS-CoV-2 infection. Members in HC-1.hypotheses order:
# [H-1 Huanan market spillover, H-5 WIV research-related incident, H-6 residual].
#
# EVIDENCE SELECTION (rule 5): NOTHING is marked used_for_prior. All 9 inbound edges sit in one of
# 4 correlation groups (CG-1..CG-4) and marking is all-or-none per group, so there is no way to pull
# a base-rate fact in without also removing a case-specific discriminating one. The candidate was
# CG-2: O-4 (47,381 live animals of 38 species at Wuhan markets, incl. susceptible raccoon dogs) is a
# genuine precondition/base-rate fact, but its group-mate O-5 (no bats or pangolins on sale) is
# explicitly discriminating — the edge note itself says it "mildly favours H-5/H-6". Marking CG-2
# would delete that discrimination from step 8 to buy a base rate the prior can carry as a reasoned
# factor instead. Same verdict for CG-1, CG-3, CG-4, which are all case-specific. So: pure outside-view
# prior, built from emergence-event base rates only, and step 8 prices all 9 edges.
# `no_observation_arguments.py --cluster HC-1` returns none (A-5 is skipped by the helper), so no
# argument input reaches this block (rule 6 is vacuous here).

# ---------------------------------------------------------------------------------------------
# Anchor. Take "the virus reached its first human host by natural zoonotic transmission somewhere in
# the wildlife/livestock chain" as the unit of relative weight. Reference class: novel human-pathogenic
# virus emergence events of the last century (SARS-1, MERS, HIV-1/2, Ebola, Nipah, Hendra, influenza
# reassortants), which are overwhelmingly natural.
w_natural_route_total = 1.0   # unit anchor; scale is free (rule 3)

# Odds that an emergence event is research-related rather than natural, before any Wuhan-specific fact.
# Reference class: documented laboratory-origin human outbreaks that spread in the community — the 1977
# H1N1 re-emergence, Birmingham smallpox 1978, the 2004 Beijing SARS-1 escapes (4 separate escape events
# after the natural outbreak ended). For this value to be right, roughly 1 in ~30 novel-agent community
# outbreaks would have to trace to a research incident. Lab-acquired *infections* are far commoner than
# this; the rarity is in seeding onward community spread.
r_research_vs_natural_base = 0.035

# Visible adjustment for the setting, not for any case-specific observation: the outbreak city hosts the
# world's largest bat-sarbecovirus collection and sampling programme. Under a research-incident account
# the coincidence of place is expected; under a natural account it is a coincidence. For this factor to
# be right, the geographic coincidence would have to be worth ~one bit of evidence — a coarse
# order-of-magnitude judgement, and the single most arguable number in this block.
uplift_coincident_lab_city = 5.0
w_research_route_total = r_research_vs_natural_base * uplift_coincident_lab_city * w_natural_route_total

# ---------------------------------------------------------------------------------------------
# H-1 — zoonotic spillover at the Huanan market via live wildlife sold there.
# What would have to be true: a susceptible live animal carrying an ancestral sarbecovirus was physically
# present at Huanan and infected a human *there*, i.e. the market is the site of the index infection, not
# merely an amplifier. Basis: the natural-emergence anchor above, times the share of natural spillovers
# whose first human case occurs at the retail node of the chain rather than upstream (farm, trapper,
# trader, transport) — SARS-1's own index infections were largely at market/restaurant/handler nodes,
# which is why this share is sizeable rather than small. What it does NOT cover: any of the market's own
# evidence (case geolocation, environmental swab clustering) — those are step 8's. Confidence: moderate;
# this is the member whose weight will move most once CG-1/CG-2 are priced.
p_index_case_at_retail_market_given_natural = 0.40   # retail node is the highest-human-contact link, but one of ~4-5 plausible links
w_h1 = w_natural_route_total * p_index_case_at_retail_market_given_natural

# ---------------------------------------------------------------------------------------------
# H-5 — a research-related incident at the WIV, possibly involving an engineered furin cleavage site.
# What would have to be true: a WIV worker was infected during collection, culture, passage or
# engineering work and carried the virus into the city. Basis: the lab-outbreak reference class above,
# uplifted for the coincidence of city, then narrowed to the WIV specifically among Wuhan institutions
# that handle bat coronaviruses (WIV, Wuhan CDC, university and hospital labs). What it does NOT cover:
# DEFUSE (O-11/O-12) or the furin-site genomics (O-10) — deliberately left unpriced here so step 8 prices
# them once. Confidence: this is the least confident of the three; both factors are order-of-magnitude
# judgements and a reader who rejects uplift_coincident_lab_city should re-run with it set to 1.
p_wiv_given_research_incident = 0.70   # WIV ran by far the largest sarbecovirus programme in the city; other Wuhan institutions handled such material at much lower volume
w_h5 = w_research_route_total * p_wiv_given_research_incident

# ---------------------------------------------------------------------------------------------
# H-6 — residual: neither listed route. Concretely this looks like (a) a natural spillover to a farmer,
# trapper, trader or transporter upstream of Huanan, or at one of Wuhan's other markets, with the virus
# then carried into the Huanan crowd and amplified there; (b) a spillover hundreds of km away with silent
# transmission into Wuhan before detection; or (c) a research-related incident at a non-WIV Wuhan
# institution. Argued in its own right (rule 4), not as a leftover. Basis: the same emergence reference
# class — in most historically resolved zoonoses (SARS-1, MERS, HIV, Ebola) the index infection turned out
# NOT to be at the venue where the outbreak was first noticed, and the venue of first detection is a
# strongly biased estimator of the venue of first infection. What it does not cover: it inherits the
# uncertainty of the two named members' own decompositions. Confidence: high that this deserves a large
# weight; the curated evidence base is doubly frame-bound (only Huanan sampled, only WIV/DEFUSE examined),
# so an unmodelled route is exactly the kind of answer this graph could not see.
w_h6_natural_offmarket_leg = 0.50   # relative to the unit natural anchor: upstream-chain or distant-spillover-with-silent-introduction routes, collectively about as likely as the market-index route
w_h6_research_nonwiv_leg  = 0.06   # a research incident at a Wuhan institution other than the WIV; small because the WIV dominates the relevant material volume
w_h6 = w_h6_natural_offmarket_leg + w_h6_research_nonwiv_leg

prior("HC-1", [w_h1, w_h5, w_h6])
```
