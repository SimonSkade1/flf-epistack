# Critics, dissent, risk-methodology, historical precedent (searcher 1B-C)

## Sources by topic (best-first within each group)

**The Plaga <-> Giddings-Mangano critic exchange** (the one scientific back-and-forth this slice owns in full)
1. [[S-16 - Potential catastrophic risk from metastable quantum black holes (Plaga 2008)]] — the critique.
2. [[S-17 - Comments on claimed risk from metastable black holes (Giddings-Mangano reply to Plaga)]] — the direct reply. Neither side of this exchange ever passed peer review (both are stand-alone arXiv notes with no journal reference); recorded as a data-reliability signal on both nodes, not just the critic's.

**Rössler's critique** (the highest-public-visibility dissent)
3. [[S-18 - Rössler's Abraham-solution critique of LHC black-hole safety (2008)]] — self-published, non-peer-reviewed; body also carries CERN's commissioned rebuttal (Nicolai 2008; Giulini & Nicolai 2008) in his own node rather than as a separate one (see Exclusions).

**Legal/public**
4. [[S-19 - Sancho v. U.S. Department of Energy - the Wagner-Sancho LHC lawsuit (D. Haw. 2008)]] — the federal suit; dismissed on jurisdiction, never reached the physics.

**Risk-assessment methodology** (how to bound a theory-error-dominated catastrophe probability)
5. [[S-21 - Probing the Improbable - risk-argument flaw ceiling (Ord, Hillerbrand, Sandberg 2010)]] — most direct, most formal, uses the LHC case as its own worked example; ranked first.
6. [[S-23 - Is a doomsday catastrophe likely - the observer-selection bound (Tegmark and Bostrom 2005)]] — Nature; short but sharp — undercuts the empirical cosmic-ray-survival argument itself (anthropic selection), not just risk-communication norms.
7. [[S-22 - A critical look at risk assessments for global catastrophes (Kent 2004)]] — earliest (written 2000 re: RHIC, published 2004), narrower/RHIC-strangelet-flavored, foreshadows the other two.

**Historical precedent / methodological analogue**
8. [[S-20 - LA-602 (1946) - Ignition of the Atmosphere with Nuclear Bombs]] — the founding a-priori catastrophe-bound calculation (given starting material).

## search_scope

Targeted search per named seed (WebSearch on each author/title/arXiv-id pair); arXiv abstract pages fetched directly for authors, dates, subject class and journal-ref (or its absence); Semantic Scholar Graph API (`api.semanticscholar.org/graph/v1/paper/arXiv:<id>`) for citation counts — worked for 4/6 attempts (rate-limited, HTTP 429, on the other 2 after repeated calls); Wikipedia's "Safety of high-energy particle collision experiments" article used as a citation-chase hub, which is where the Rössler primary PDFs, the CERN/Nicolai-Giulini rebuttal PDFs, and the exact Sancho docket number/citation all came from; case-law aggregators (justia, vLex, casemine) and contemporaneous news (The Register, SWI, NBC) cross-checked the lawsuit's facts; the LA-602 PDF (given URL) was read directly via local file (page-range read of the fetched binary) since WebFetch cannot parse its scanned-image text.

## exclusions

1. CERN's rebuttal to Rössler (Nicolai 2008; Giulini & Nicolai 2008, `environmental-impact.web.cern.ch`) — found, high-quality, on-topic, but folded into S-18's body as prose instead of a dedicated node, to keep the written-node count closer to budget (see Slice shape below). Nothing lost: both PDFs and their conclusions are named on S-18, just not independently id'd.
2. Rössler's *other* legal action — a separate suit at the European Court of Human Rights (filed Aug 2008, summarily rejected same day) — mentioned in passing on S-18 but not separately noded; the brief named only the Wagner-Sancho US suit as this slice's legal target.
3. Casadio & Harms (2002) — the quantum-black-hole-remnant model Plaga's argument is built on — a discovery-hub background paper, not itself a critic/methodology primary; not noded.
4. Meade & Randall and all slice-A/slice-B seeds (LSAG, Blaizot 2003, production/Hawking theory, CERN FAQ, Giddings-Mangano's main astrophysical-bounds paper, cosmic-ray/white-dwarf/neutron-star/strangelet data) — untouched per the brief's slicing, only mined as discovery hubs where encountered.
5. The original Wagner-Sancho complaint text and the full Gillmor dismissal opinion — no free full-text mirror found (PACER-gated); `url` instead points to the (working) Justia docket page, with the case's official reporter citation (578 F.Supp.2d 1258) given in `venue` as an alternate locator for anyone with law-database access.
6. Wayback Machine snapshots (Rössler's PDFs, CERN's rebuttal PDFs) could not be fetched directly — my WebFetch tool refuses `web.archive.org` outright — so their content is reported second-hand via Wikipedia's direct quotations of them, not independently verified by me. Flagged on S-18, not logged as a pipeline problem (tool limitation, not a pipeline bug).

## Slice shape

8 source nodes written against a stated budget of 6 (12 read against a budget of 12, roughly on target) — a deliberate, disclosed overshoot: the seed list named ~9 distinct, cheaply-verifiable primary artifacts (2 in the critic exchange, 1-2 for Rössler, 1 legal, 3 methodology, 1 historical), more than the per-slice budget assumed, and this is the one slice whose whole point is balance/independence, so under-covering it seemed like the worse failure mode. I partially offset by folding the CERN/Nicolai-Giulini rebuttal into Rössler's own node rather than giving it a ninth. Everything here was fast and cheap to find — this is a well-documented 2008 media episode, not a literature needing heavy snowballing — so the overshoot cost little time. Substantively, the slice's shape is: one real scientific disagreement (Plaga/GM) that both sides only ever aired outside peer review; one non-physicist's critique (Rössler) that the physics community considers a basic GR error but which drove most of the public alarm and both lawsuits; one legal test that never touched the physics; and three methodology papers converging on the same point from different angles (RHIC-era policy-consistency, LHC-specific argument-flaw-ceiling, and an anthropic objection to the empirical safety argument itself) — together the strongest candidate content for the final report's "what does it hinge on" section. I did not find any other distinct, citable scientific dissenter from this era beyond Plaga and Rössler; other "concerned" voices circulating in 2008 were amateur/forum-level and not worth a node.
