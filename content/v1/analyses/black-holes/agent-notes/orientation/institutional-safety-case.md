## Slice: the official/institutional safety case (searcher 1b)

Treats the "it's safe" verdict itself as the primary artifact under scrutiny — the chain of reports/statements that constitute and endorse it — rather than as evidence for a hypothesis. Small, closed set: essentially every item named in the brief was findable and confirmable, so this slice is close to exhaustive rather than a sample.

### Topics

**The LHC verdict chain (report → institutional endorsement → public restatement):**
- [[S-1 - LSAG report- Review of the Safety of LHC Collisions]] — the 2008 expert-group report itself; the load-bearing node.
- [[S-6 - CERN Scientific Policy Committee- independent review endorsing the LSAG report]] — CERN Council-level ratification of LSAG.
- [[S-5 - CERN FAQ- Will CERN generate a black hole]] — public-facing compressed restatement (no independent analysis).

**Precedents the LHC review chain explicitly builds on (RHIC-era, 2000):**
- [[S-3 - Busza, Jaffe, Sandweiss, Wilczek- Review of Speculative Disaster Scenarios at RHIC]] — BNL-commissioned, the direct structural template LSAG follows (cosmic-ray-survival master argument).
- [[S-4 - Dar, De Rújula, Heinz- Will relativistic heavy ion colliders destroy our planet]] — independent (non-BNL-commissioned) contemporaneous corroboration, mostly strangelet-focused.
- [[S-2 - CERN-2003-001- Study of potentially dangerous events during heavy-ion collisions at the LHC]] — CERN's own intermediate 2003 heavy-ion-only study, the direct predecessor LSAG updates/extends to full pp running.

**Independent (non-official-chain) technical check on the specific black-hole-growth mechanism:**
- [[S-10 - Koch, Bleicher, Stöcker- Exclusion of black hole disaster scenarios at the LHC]] — published within weeks of LSAG, not derived from or commissioned alongside it; useful as an outside check on the Hawking-evaporation-beats-accretion claim.

**Historical methodological precedent for the genre:**
- [[S-7 - Konopinski, Marvin, Teller- LA-602, Ignition of the Atmosphere with Nuclear Bombs]] — 1946 pre-Trinity atmospheric-ignition assessment; same structural genre (institution assesses its own catastrophic risk before a first-of-kind experiment), track record known (correct).

### search_scope

Started from the explicit item list in the orchestrator's brief (all 8 named artifacts) and confirmed/located each via: arXiv abstract pages (LSAG, Busza et al., Dar et al., Koch-Bleicher-Stöcker) fetched directly; CERN Document Server (CDS) search for CERN-2003-001 and the SPC report (CDS pages were behind an Anubis bot-check when fetched directly, so I used WebSearch summaries instead of raw page fetch for S-2 and S-6's page text); home.cern FAQ page (redirect-followed); Semantic Scholar API for citation counts (rate-limited after ~2 calls — got counts for S-3 and S-4 only, others left `unknown`); WebSearch for LA-602 (direct PDF fetch failed — OCR garbled — so metadata/summary sourced from secondary confirmation, e.g. nuclearsecrecy.com blog and LessWrong "LA-602 vs. RHIC Review," cross-checked against two independent search hits for consistency). No database/citation-graph tool beyond Semantic Scholar was needed since the set was small and named.

### exclusions

- Giddings & Mangano, "Astronomical [sic Astrophysical] implications of hypothetical stable TeV-scale black holes" (arXiv:0806.3381) — the companion paper the SPC panel reviewed alongside LSAG, and the one LSAG itself leans on for the "even if stable, no risk" argument. This is an astrophysical-accretion primary, not an institutional-verdict primary — belongs to slice 3 (astrophysical-survival/accretion). Recorded here only as found_via context for S-1 and S-6.
- CERN's "public-archive.web.cern.ch/en/LHC/Safety-en.html" landing page — DNS did not resolve when fetched; from search-result descriptions it appears to be a hub page linking to LSAG/SPC/FAQ, not new primary content, so not worth a retry given it would likely be a discovery hub, not a primary — dropped rather than minted.
- CERN news item "CERN reiterates safety of LHC on eve of first beam" — a news/press-release restatement of the same LSAG verdict; would duplicate S-1/S-5/S-6's content without adding a new institutional actor or argument, and news items generally aren't primaries. Not minted.
- Textbook/Wikipedia/HandWiki summaries of the safety debate (used during search to locate primaries, e.g. "Safety of high-energy particle collision experiments") — mined for pointers only, per instructions, no node.

### Shape / gaps

8 sources minted (S-1,2,3,4,5,6,7,10), all primary institutional-chain artifacts, essentially the full set named in the brief plus nothing more — this slice is naturally small and closed rather than something to snowball further; adding more would mean minting secondary restatements. Gap: could not get citation counts for S-1, S-2, S-5, S-6, S-7, S-10 (Semantic Scholar API rate-limited after 2 calls, S-5/S-7 likely have no formal citation count as webpage/grey-lit anyway) — left `unknown`, fillable later if step 2 needs it. Also could not directly read CDS-hosted PDF text for S-2/S-6 (bot-check page); relied on corroborated WebSearch summaries instead of primary-page text — a re-open with a different fetch path may be worth it if step 2/3 needs exact wording (e.g. exact SPC panel language) rather than paraphrase.
