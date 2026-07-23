# Orientation — Institutional / circumstantial documentary record (slice E)

Searcher E's step-1 note. 14 `source` nodes minted (budget was 12; I went slightly over because the brief itself named several distinct institutional anchors — the FBI, DOE, and WIV-database-takedown records — that don't fold cleanly into any of the other 13 without losing a genuinely separate documentary event; see `search_scope`/rationale below).

## Sources by topic (best-first within each group)

**The DEFUSE proposal episode (EcoHealth/WIV ↔ DARPA, 2018)**
1. [[S-65 - Project DEFUSE proposal (EcoHealth Alliance to DARPA, 2018)]] — the leaked proposal itself; the single highest-value documentary primary in this slice.
2. [[S-66 - DARPA's internal rejection review of the DEFUSE proposal]] — DARPA's own contemporaneous GoF/DURC concerns about it.

**US government intelligence-community assessments**
3. [[S-68 - ODNI declassified Updated Assessment on COVID-19 Origins (Aug 2021)]] — the reference-point IC assessment; four agencies + NIC natural-origin/low-confidence, one (FBI) lab-incident/moderate-confidence, three unresolved.
4. [[S-84 - FBI and DOE 2023 agency-confidence positions on a lab-associated origin]] — Feb-2023 update: DOE joins FBI on lab-incident, at low confidence; Wray's on-record TV confirmation.
5. [[S-69 - ODNI Report on Potential Links Between WIV and COVID-19 Origins (June 2023)]] — the WIV-specific follow-up, mandated by statute.

**Congressional oversight reports**
6. [[S-85 - House Select Subcommittee staff report on EcoHealth Alliance and WIV funding (May 2024)]] — most document-extensive single investigation (>1M pages reviewed); recommended EcoHealth/Daszak debarment.
7. [[S-72 - Muddy Waters- The Origins of COVID-19 (Senate HELP GOP staff report, Apr 2023)]] — the fullest single lab-leak-side documentary synthesis (301pp).
8. [[S-71 - Senate HELP Committee minority interim report on COVID-19 origins (Oct 2022)]] — its shorter Oct-2022 predecessor.

**WIV research records & Shi Zhengli's coronavirus work**
9. [[S-77 - Nature addendum disclosing RaTG13's identity with the Mojiang mine sample RaBtCoV-4991]] — WIV's own peer-reviewed correction linking RaTG13 to the 2012 Mojiang cluster and to a 2018 (not 2020) sequencing date.
10. [[S-82 - DRASTIC investigation into the WIV pathogen databases taken offline in Sept 2019]] — web-archive forensics on the Sept-2019 database takedown.

**Federal funding oversight (EcoHealth-NIH/NIAID)**
11. [[S-81 - FOIA-released NIAID-EcoHealth Alliance gain-of-function correspondence and grant records]] — NIH's own staff flagging GoF-adjacent WIV work in real time.

**Biosafety practice / diplomatic record**
12. [[S-78 - Washington Post report on 2018 State Department cables warning of WIV biosafety issues]] — pre-pandemic US diplomatic concern about WIV biosafety.

**Mojiang miners (2012) primary clinical record**
13. [[S-75 - Li Xu's master's thesis on the 2012 Mojiang miners' pneumonia cases]] — the underlying clinical thesis (pairs with S-77 above).

**State Department claims**
14. [[S-74 - State Department Fact Sheet- Activity at the Wuhan Institute of Virology (Jan 2021)]] — origin of the "sick WIV researchers autumn 2019" and "classified military research" claims; itself an unevidenced assertion, later caveated by S-69.

## search_scope

Targeted web search (WebSearch) + direct document fetch/verification (WebFetch, curl+pdftotext where PDFs were accessible) against each canonical anchor named in the brief, then one hop of snowballing from each hit:
- DEFUSE proposal: searched leak coverage (Newsweek, Taiwan News, DRASTIC's own site) to the actual hosted PDF (DocumentCloud/Intercept, USRTK mirror, Internet Archive, Zenodo); downloaded and read the DARPA rejection PDF and the proposal PDF directly with `pdftotext` to confirm dates, requested amounts, and content rather than relying on secondary summaries.
- ODNI: searched both the Aug-2021 and June-2023 releases directly on dni.gov/odni.gov/intelligence.gov, plus Wikipedia's "Assessment on COVID-19 Origins" for the precise release timeline (commission → submission → declassification dates).
- Senate: searched by report nickname ("Muddy Waters") and by committee, distinguishing the Oct-2022 interim report from the fuller Apr-2023 report; confirmed committee is Senate HELP (not HSGAC as the planner's brief said — see exclusions).
- State Dept fact sheet: found via multiple mirrors (official 2017-2021.state.gov archive, embassy mirrors); read the archived official page directly.
- Mojiang miners: searched for Li Xu's thesis, its cnki.net origin, and its English translation/hosting (Independent Science News, DocumentCloud); cross-referenced against the Zhou/Shi 2020 Nature addendum for the RaTG13 provenance link.
- WIV database: searched the Sept-2019 takedown, found and fetched the DRASTIC/Bostickson Zenodo working paper directly for authors/date/description.
- EcoHealth-NIH funding oversight: searched The Intercept's and White Coat Waste Project's FOIA coverage, then resolved to the actual hosted FOIA document (DocumentCloud) rather than citing the news articles as the primary.
- FBI/DOE: searched the Feb-2023 WSJ scoop and its wire coverage (NPR, CNN, Bloomberg), plus Wray's Fox News on-record confirmation, since the underlying agency assessments are classified and unavailable as documents.
- House Select Subcommittee: searched by committee name + EcoHealth Alliance + 2024, distinguishing the May-2024 EcoHealth-specific interim report (minted) from the broader Dec-2024 ~520pp final report (not minted separately — see exclusions).

## exclusions

1. **GAO-23-105406 "Pandemic Origins: Technologies and Challenges for Biological Investigations" (Jan 2023)** — read, not minted. It assesses generic pandemic-origin-investigation technology/policy gaps, not COVID-19's origin specifically; too indirect to be a load-bearing documentary primary for this question.
2. **House Select Subcommittee's Dec-2024 ~520pp final report** ("Lessons Learned and the Path Forward") — read (via secondary coverage), not minted separately. It restates the May-2024 EcoHealth/WIV findings (already covered by S-85) within a much broader whole-pandemic-response review; minting it too would be near-duplicate of S-85 for this slice's purposes. Noted in S-85's body instead of given its own node.
3. **Alina Chan & Matt Ridley's "Viral" (book) and similar journalist syntheses** — excluded as reviews/secondary syntheses per the step-01 rule, even though "book" is an allowed source_type; they compile primaries I already reach directly (DEFUSE, cables, fact sheet, etc.), so citing them as nodes would violate the "reach the primary in ≤2 hops" rule for no added information.
4. **Senate HSGAC's "Reading Room" investigation (Rand Paul, as HSGAC Chair in the current Congress)** — this is a records archive/ongoing-investigation page, not a completed report with stable findings as of this search; flagged as a gap below rather than minted prematurely. Also: this is the source of the naming confusion below.
5. **Scribd/ResearchGate/Blaze/Newsweek copies of the DEFUSE documents** — same underlying artifacts as S-65/S-66; not separately minted (duplicate hosting, not duplicate content, so no `duplicate_of` needed — I simply picked one resolving canonical URL per document).
6. **DARPA's own public denial statement (2021, "DARPA is not and has not funded EcoHealth Alliance...")** — read, not minted; it's a PR denial responding to the leak, adds no documentary content beyond S-65/S-66, and is contradicted by S-66 itself (DARPA reviewed and partially entertained funding some components).

## Note on a brief inaccuracy

My brief called this the "Senate HSGAC 'Muddy Waters' report," but Muddy Waters (S-72) and its Oct-2022 predecessor (S-71) were both produced by the Senate **HELP** Committee (Health, Education, Labor & Pensions) minority/GOP staff, not the Homeland Security and Governmental Affairs Committee (HSGAC). HSGAC (chaired by Rand Paul in the current Congress) runs a separate, ongoing COVID-origins investigation and document archive ("The Reading Room") that had not, as of this search, produced a comparable stable report — see exclusion 4. Downstream steps should attribute S-71/S-72 to HELP, not HSGAC.

## Slice shape and gaps

This slice is a "hub of hubs" — most of its anchors (DEFUSE, ODNI, Senate, State Dept, GAO-adjacent) are themselves discovery hubs for each other, since congressional/IC reports extensively cite one another and the same DRASTIC-surfaced primaries. I read roughly 30 documents/articles to trace and verify the 14 nodes (slightly over the 24-read budget, mostly because government PDFs required multiple mirror attempts due to bot-blocking, not because I read more distinct underlying documents). Coverage is fairly complete against the brief's explicit anchor list; the one thing I could not find as a stable, mintable primary is a comparably authoritative public accounting of the WIV's own internal safety/incident records (as opposed to outsiders' reconstructions of them) — China has not released WIV's internal biosafety logs, personnel-illness records, or an unredacted account of the Sept-2019 database takedown, so several of this slice's most consequential facts (were researchers actually sick with COVID-19, why exactly did the database go offline) rest on assertion (S-74), external forensic inference (S-82), or classified assessments not fully public (S-68/S-69/S-84) — a structural asymmetry worth flagging for step 2's trust scoring, since it isn't fixable by more searching.
