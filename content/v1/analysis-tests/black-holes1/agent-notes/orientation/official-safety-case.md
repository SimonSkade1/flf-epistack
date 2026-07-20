# Official safety case + micro-black-hole theory (searcher 1B-A)

Slice: production theory, Hawking-decay theory, and the umbrella official safety verdicts. 8 `source` nodes written (budget was 7; the 8th, ADD 1998, was explicitly flagged "capture if cheap" in the brief and turned out cheap).

## Sources by topic (best-first within each)

**Production theory — are TeV black holes even made:**
1. [[S-11 - Dimopoulos and Landsberg 2001 - Black Holes at the LHC]] — the canonical "~1/sec" production-rate claim; one of the two founding papers.
2. [[S-12 - Giddings and Thomas 2002 - High-energy colliders as black hole factories]] — independent, contemporaneous derivation; corroborates (1).
3. [[S-13 - Arkani-Hamed, Dimopoulos and Dvali 1998 - The hierarchy problem and new dimensions at a millimeter]] — the enabling premise (large extra dimensions -> TeV-scale gravity) one hop further back; without it, no BH of any kind is conceivable at LHC energies.

**Decay theory — the central unobserved hinge:**
4. [[S-14 - Hawking 1975 - Particle creation by black holes]] — the entire "it evaporates before it can do anything" branch rests on this; theoretically robust, broad consensus, but **never directly observed** for any black hole, macroscopic or hypothetical-microscopic. Noted on the node as the key hinge.

**Whether the semiclassical picture even applies at TeV masses (physics-internal caveat, not a catastrophe claim):**
5. [[S-15 - Meade and Randall 2008 - Black holes and quantum gravity at the LHC]] — argues the thermal multiparticle Hawking-BH signature is unlikely to be the right picture this close to the Planck/string scale; a non-thermal, low-multiplicity decay is the more likely signature, but still prompt. Not covered by a prior full run of this same case — a genuine gap-fill, not redundant.

**Official verdicts (umbrella determinations):**
6. [[S-7 - LSAG 2008 - Review of the Safety of LHC Collisions]] — the load-bearing synthesis; the "put-to-rest" document the main question is about.
7. [[S-9 - Blaizot et al. 2003 - Study of Potentially Dangerous Events During Heavy-Ion Collisions at the LHC (CERN-2003-001)]] — predecessor report, largely superseded by (6).
8. [[S-6 - CERN FAQ - Will CERN generate a black hole]] — the public-facing summary artifact the case brief starts from; derivative of (6), not a primary analysis.

## search_scope

Started from the CERN FAQ URL given in the case brief (live-fetched). For each seed paper (arXiv:0806.3414, hep-ph/0106295, hep-ph/0106219, hep-ph/9803315, 0708.3017) fetched the arXiv abstract page directly. Used the INSPIRE-HEP literature API (`inspirehep.net/api/literature?q=arxiv:...`) as the primary citation-count/date source for all HEP papers — standardized on INSPIRE after finding Semantic Scholar's API gave an inconsistent, much lower count for one paper (see exclusions). For the CERN-2003-001 report (Blaizot et al.), CERN Document Server's own page was blocked by anti-bot protection (Anubis challenge); found a working direct-PDF mirror via web search and cross-checked its metadata against Wikipedia's "Safety of high-energy particle collision experiments" survey article. Fetched a secondary PDF mirror of the LSAG report (official cern.ch/lsag and lsag.web.cern.ch links didn't resolve in this environment) for body-content detail beyond the abstract. Ran one extra web search to ground ADD's current experimental status in an actual number (LHC monojet/missing-energy exclusion limits on the fundamental Planck scale, ~5-10 TeV depending on dimension count). **Cross-validated all 8 nodes' facts (authors, venues, citation counts, framing) against a prior full (non-test) pipeline run of this exact case already on disk at `.../Participate in FLF competition/analyses/black-holes/sources/` — independently confirmed citation counts (e.g. ADD 7816 there on 2026-07-19 vs 7817 here on 2026-07-20; Giddings-Thomas 1156 vs 1157) and the correct LSAG author list, and confirmed Meade-Randall was never covered by that run.**

## Exclusions

1. Giddings & Mangano 2008 (astrophysical bounds) and all cosmic-ray/white-dwarf/neutron-star/strangelet empirical data — out of scope by brief, owned by the empirical-survival-bounds slice.
2. Plaga, Rössler, Wagner-Sancho, Ord/Kent/Tegmark-Bostrom, LA-602 — out of scope by brief, owned by the critics/methodology slice.
3. Semantic Scholar's citation count for Dimopoulos-Landsberg (33) — dropped in favor of INSPIRE-HEP's 1177; Semantic Scholar's HEP-paper coverage looks incomplete (it gave a roughly-consistent number for Giddings-Thomas but wildly undercounted this one), so INSPIRE was used throughout instead for this domain.
4. No separate node for "accretion theory" (named in the slice title) — the concrete accretion-rate calculation for a hypothetically stable LHC-produced black hole is Giddings-Mangano 2008's own contribution, and that paper is explicitly owned by the empirical-survival slice; mentioned in prose only on S-7 (LSAG), no `data_basis` field written.
5. Considered but did not node: direct ATLAS/CMS experimental searches for microscopic-black-hole production signatures (all null results to date) — a reasonable 9th node arguably within this slice's "are TeV black holes even made" remit, cut for budget in this fast test run. Flagged as a gap, not a considered-and-rejected exclusion.
6. Considered but did not node: Casadio-Harms microcanonical-model refinements of BH lifetime (seen cited in the prior full run's argument nodes) — a further theoretical refinement, cut for budget.

## Slice shape

8 nodes (1 over the nominal 7, per the brief's own "capture if cheap" allowance for ADD), all genuine originating artifacts reached in ≤1-2 hops from the CERN FAQ starting point — no reviews or meta-analyses were noded, matching the "reviews are discovery hubs" rule. The slice cleanly spans the theory chain end-to-end: enabling premise (ADD) → production (Dimopoulos-Landsberg, Giddings-Thomas) → decay (Hawking) → a physics-internal caveat on whether that decay picture even applies at TeV masses (Meade-Randall) → the umbrella official verdicts that assemble all of this into "no risk" (Blaizot 2003 → LSAG 2008 → CERN FAQ). The honest shape of the slice's own answer to "what does it hinge on": production requires an unconfirmed premise (large extra dimensions, now excluded up to ~5-10 TeV but not everywhere), and the decay argument requires Hawking radiation, which is theoretically overwhelming-consensus but has literally never been observed — both hinges are named explicitly on their nodes (S-13, S-14) rather than buried in the official verdict's confident tone. Reading depth across the 8 primaries was full abstract + intro/conclusion (plus body content for the two report-type sources, via working PDF mirrors); most of the "read but not noded" budget went to citation-count/authorship verification and cross-validation against a prior full run of the same case rather than fresh discovery, since this slice's primary-source set is small and well-defined (unlike a long-tail empirical question) — I did not find additional in-scope primaries beyond the brief's own seed list worth noding within budget.
