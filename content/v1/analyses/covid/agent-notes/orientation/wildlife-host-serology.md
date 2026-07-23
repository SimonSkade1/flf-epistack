# Orientation — Wildlife trade / host-range / serology (slice F)

Searcher F's own note. Not a graph node. Covers the animal side of the spillover question: what was sold, what's susceptible, what surveillance found (or didn't), and the SARS-1/MERS precedent for how a market-amplified zoonosis actually looks in the primary record.

## My sources, by topic (best-first)

**Wildlife on sale at Wuhan markets**
- [[S-19 - Xiao et al. 2021 — animal sales from Wuhan wet markets pre-pandemic.md]] — the primary survey (own data, May 2017-Nov 2019): 47,381 animals, 38 species, no pangolins/bats, raccoon dogs/civets/mink all present live.

**Host-susceptibility / experimental infection (SARS-CoV-2)**
- [[S-20 - Freuling et al. 2020 — raccoon dog experimental SARS-CoV-2 infection.md]] — raccoon dogs (the lead market-species candidate) susceptible, shed high titer, transmit to contacts, minimal clinical signs.
- [[S-27 - Oreshkova et al. 2020 — SARS-CoV-2 outbreak on Dutch mink farms.md]] — real-world (not just experimental) farmed-mink outbreak with farm-to-worker transmission.
- [[S-29 - Shi et al. 2020 — susceptibility of ferrets, cats, dogs and other domesticated animals to SARS-CoV-2.md]] — broad screen: cats susceptible/airborne-transmitting, dogs marginal, pigs/poultry not susceptible.
- [[S-28 - Sia et al. 2020 — pathogenesis and transmission of SARS-CoV-2 in golden hamsters.md]] — foundational small-mammal model, efficient airborne transmission.
- [[S-33 - Damas et al. 2020 — comparative-structural ACE2 host-range prediction for SARS-CoV-2.md]] — computational cross-check across 410 vertebrates; flags civets as a species nobody seems to have tested experimentally for SARS-CoV-2 (see gaps below).

**Intermediate-host search & animal surveillance (largely negative)**
- [[S-34 - WHO-China joint report 2021 — animal and environmental sampling section.md]] — >80,000 national wildlife/livestock/poultry samples, zero positives; 457 market-animal samples (18 species) also all negative.
- [[S-37 - Deng et al. 2020 — 35-species serosurvey excludes intermediate hosts.md]] — 1,914 sera, 35 species (incl. farmed fox/mink/civet), zero positives, but untargeted (no confirmed human-case contact).
- [[S-40 - Xiao K. et al. 2020 — isolation of SARS-CoV-2-related coronavirus from Malayan pangolins.md]] — the one non-bat species with an actual isolated close relative, despite being absent from the Wuhan market sales data.

**Human serosurveys (pre-Dec-2019)**
- [[S-38 - Chang et al. 2022 — Wuhan blood-donor serosurvey, September-December 2019.md]] — the primary data behind the disputed "early Wuhan antibodies" claim; raw reactive counts plus the neutralization-negative resolution.

**SARS-1 / MERS spillover precedent (market-amplification pattern)**
- [[S-41 - Guan et al. 2003 — SARS-CoV-like viruses isolated from market civets, southern China.md]] — foundational SARS-1 civet-market isolation.
- [[S-44 - Kan et al. 2005 — SARS-CoV-like virus in market civets vs farmed civets.md]] — the primary source for "market amplification": positive in all market civets/raccoon dogs, negative in 1,107 farmed civets.
- [[S-45 - Reusken et al. 2013 — MERS-CoV neutralising antibodies in dromedary camels.md]] — the second precedent case: camel seroprevalence found well before MERS spillover was recognized.

## search_scope

Started from the canonical anchors named in the slice brief (Xiao 2021, Freuling, WHO-China report, Guan 2003) and confirmed/extended each via: (1) targeted WebSearch per anchor plus obvious adjacent-species queries (mink, hamster, ferret/cat/dog, civet, pangolin, MERS camel); (2) OpenAlex API (`api.openalex.org/works`) for authoritative venue/date/citation-count/author metadata on every candidate, cross-checked against the search snippets; (3) WebFetch on the two sources where I needed methodology detail beyond the search snippet (Xiao 2021 via PMC to confirm it's primary survey data, not a reanalysis; Freuling 2020 via PMC for exact study design). Snowballed from the WHO-China report's "recommended further studies" list (farmed ferret-badger/civet/mink/raccoon-dog surveys) and from citation trails around the Guan 2003 / Kan 2005 civet-market pair toward the MERS camel analogue. Did not do a systematic database search beyond this; relied on search-engine coverage + citation counts as a proxy for "did I miss something load-bearing."

## exclusions

- Lam et al. 2020 Nature, "Identifying SARS-CoV-2-related coronaviruses in Malayan pangolins" — read, not minted: independent group, overlapping pangolin-seizure sample set, same finding as [[S-40 - Xiao K. et al. 2020 — isolation of SARS-CoV-2-related coronavirus from Malayan pangolins.md]]; dropped for budget, flagged as a possible step-2/3 gap-fill if the pangolin evidence turns out to be curated in.
- Tu et al. 2004 EID, "Antibodies to SARS coronavirus in civets" — read, not minted: same market-vs-farm civet contrast as [[S-44 - Kan et al. 2005 — SARS-CoV-like virus in market civets vs farmed civets.md]], via serology rather than viral RNA/isolation; dropped for budget as largely corroborating.
- Song et al. 2005 PNAS, "Cross-host evolution of SARS coronavirus in palm civet and human" — read, not minted: SARS-1 civet-to-human adaptation-signature paper; dropped for budget, precedent already covered by Guan 2003 + Kan 2005.
- Haagmans et al. 2013 Lancet Infect Dis, "MERS-CoV in dromedary camels: an outbreak investigation" (Qatar farm, direct virus isolation linked to a human cluster) — read, not minted: dropped for budget in favor of Reusken 2013's broader serology discovery; both are strong, either could be swapped in.
- Structural civet/SARS-1 ACE2-compatibility papers (e.g. J Virol 2008 "Structural Analysis of Major Species Barriers...") — out of scope: about SARS-1, superseded for SARS-CoV-2 purposes by [[S-33 - Damas et al. 2020 — comparative-structural ACE2 host-range prediction for SARS-CoV-2.md]].
- Huanan market environmental/metagenomic papers (Liu/Gao et al. Nature 2023 China CDC report; Crits-Christoph et al. 2023/2024 raccoon-dog metagenomics) — explicitly out of scope, slice A's territory (I own animals-sold/susceptibility/serology, not the market surface swabs); read as shared hubs only.
- Worobey et al. 2022 Science (case geolocation/market map) — out of scope, slice B's territory.

## Slice shape & gaps

~13 sources, cleanly split across five sub-questions: what was for sale (1 source, but it's comprehensive), experimental/natural susceptibility (5 sources covering raccoon dog/mink/cat/dog/ferret/hamster + a computational cross-check), the intermediate-host surveillance record (3 sources, uniformly negative except the pangolin isolation), human serosurveys (1 source), and the SARS-1/MERS precedent (3 sources). The clearest gap: I could not find any dedicated SARS-CoV-2 experimental-infection study for civets specifically — the SARS-1 intermediate host has, as far as I could find, never been directly challenged with SARS-CoV-2 in the way raccoon dogs, mink, hamsters, ferrets and cats have; Damas et al.'s computational ACE2 score is the only available proxy. A second, softer gap: I found no post-2021 dedicated farmed-wildlife (raccoon dog/mink/civet) serosurvey conducted specifically in response to the 2022-23 market-metagenomics controversy that would sit in my lane rather than slice A's — if one exists it would strengthen the negative-surveillance case considerably.
