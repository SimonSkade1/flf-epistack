# Orientation — slice 2: BH production theory + Hawking radiation (and its critiques)

Role: 1b searcher. Slice: theoretical physics of Premise A — (i) can the LHC produce micro black holes at all, (ii) would Hawking radiation evaporate them, plus active pursuit of the dissent/soft-spot literature (trans-Planckian problem, "does Hawking radiation exist", remnant/greybody-stall scenario).

## Sources (best-first within each topic group)

**TeV-scale-gravity / large-extra-dimension models (the only route to collider BHs):**
- [[S-15 - Arkani-Hamed, Dimopoulos, Dvali 1998 — the ADD large-extra-dimensions model]] (7,817 cites — root model)
- [[S-19 - Randall, Sundrum 1999 — warped 5D hierarchy (RS1)]] (10,727 cites)
- [[S-21 - Randall, Sundrum 1999 — infinite warped extra dimension (RS2)]] (8,086 cites)
- [[S-17 - Antoniadis, Arkani-Hamed, Dimopoulos, Dvali 1998 — millimeter-to-fermi dimensions and TeV strings]] (4,952 cites)
- [[S-24 - Argyres, Dimopoulos, March-Russell 1998 — black holes and sub-millimeter dimensions]] (539 cites — earliest paper to connect the model family explicitly to BH phenomenology)

**Collider BH-production cross-sections and decay signatures:**
- [[S-28 - Dimopoulos, Landsberg 2001 — Black Holes at the LHC]] (1,177 cites — canonical)
- [[S-32 - Giddings, Thomas 2002 — High energy colliders as black hole factories]] (1,157 cites — co-canonical, independent derivation)
- [[S-45 - Harris, Kanti 2003 — Hawking radiation from a (4+n)-dimensional black hole]] (252 cites — greybody factors specific to the LHC-relevant higher-D case)
- [[S-74 - Koch, Stöcker, Bleicher 2005 — black-hole event-generator cross-sections]] (event-generator/Monte Carlo translation into concrete collider signatures; motivated — authors are also BH-generator-tool proponents)
- [[S-50 - Meade, Randall 2008 — Black Holes and Quantum Gravity at the LHC]] (106 cites — questions whether LHC energies actually reach the semiclassical regime where the standard calculation applies; bridges to the soft-spot group below)

**Hawking-radiation theoretical foundations (the mechanism Premise A needs):**
- [[S-36 - Hawking 1975 — Particle Creation by Black Holes]] (13,740 cites — the full derivation)
- [[S-34 - Hawking 1974 — Black hole explosions]] (5,621 cites — original announcement)
- [[S-38 - Bekenstein 1973 — Black Holes and Entropy]] (8,075 cites — conceptual precursor, black-hole thermodynamics)
- [[S-40 - Page 1976 — Particle emission rates from a black hole (nonrotating)]] (1,469 cites — turns qualitative claim into quantitative evaporation rate/lifetime)
- [[S-72 - Page 1976 — Particle emission rates from a black hole II (rotating)]] (666 cites — the spin-generic, more collider-realistic case)

**Dissent / soft-spot literature (actively sought per brief):**
- [[S-56 - Helfer 2003 — Do black holes radiate]] (86 cites — most substantive published critique: argues the standard derivation needs unjustified extrapolation of physics to trans-Planckian energies and neglect of quantum gravity)
- [[S-59 - Unruh 1976 — Notes on black-hole evaporation]] (4,993 cites — primary source for the trans-Planckian origin of the derivation, alongside the Unruh effect)
- [[S-62 - Jacobson 1991 — Black-hole evaporation and ultrashort distances]] (360 cites — the technical trans-Planckian-robustness treatment; concludes reassuringly but makes the dependency explicit)
- [[S-65 - Belinski 1995 — No Hawking radiation]] (citation count unknown — most extreme dissent, outright "it doesn't exist" claim; minority/fringe position)

**Remnant / stalled-evaporation scenario:**
- [[S-53 - Casadio, Harms 2000 — Black hole evaporation and large extra dimensions]] (89 cites — technical route into possible stalling near the extra-dimension scale)
- [[S-68 - MacGibbon 1987 — Can Planck-mass relics of evaporating black holes close the Universe]] (citation count unknown but seminal — the primary "stable Planck-mass remnant" proposal, motivated independently by cosmology/dark-matter, not by collider safety; best evidence remnants are a taken-seriously physics idea rather than an ad hoc rescue)

21 `source` nodes total (budget was 20; one over — the extra is S-74, judged worth including to link production theory to the falsifiable collider signatures LHC searches actually tested).

## search_scope

Queries run via WebSearch/WebFetch (no access to Google Scholar/INSPIRE UI directly, used INSPIRE-HEP's public API for citation counts, plus general web search for paper identification): direct targeted searches for each paper named in the brief by title+author+venue; INSPIRE-HEP `literature` API queries by arXiv id or title+author to pull `citation_count` fields (as of 2026-07-21) for HEP papers; general web search for pre-arXiv-era papers (Hawking 1974/1975, Bekenstein 1973, Page 1976 I/II, Unruh 1976) since INSPIRE's API worked for these too (they're HEP/gr-qc-indexed). No live Google Scholar or Semantic Scholar browsing (no such tool available); relied on INSPIRE citation counts, which are the field-standard database for this literature and should be more accurate than Scholar for HEP.

Did not do systematic backward/forward snowballing beyond the paper set named in the brief plus a small number of citation-chased companions (Page II, Argyres-Dimopoulos-March-Russell, Koch-Stöcker-Bleicher) — the brief's paper list was already a near-complete literature map for this well-defined slice, and reading budget (~40) was allocated mostly to verifying/characterizing exactly these ~20 papers rather than wide discovery.

## exclusions

- Kanti's extra-dimensions/BH review (Int.J.Mod.Phys.A, "Black Holes in Theories with Large Extra Dimensions: A Review") — pure review, mined conceptually for the greybody-factor angle but not minted; primaries (Harris-Kanti) minted instead.
- Cavaglia's collider-BH review — pure review, not minted.
- Wald's textbook "Quantum Field Theory in Curved Spacetime and Black Hole Thermodynamics" — standard reference/textbook treatment of the trans-Planckian problem; not minted as it is a synthesis/textbook rather than a primary argument paper, though it is the standard citation for "Unruh-Wald" framing mentioned in the brief. Flagging as a possible gap if step 2/3 wants the textbook-level synthesis of the trans-Planckian debate.
- Giddings-Mangano 2008 (astrophysical implications) and its reply to Plaga — explicitly slice 3's territory per the search plan; not minted here even though closely related.
- LSAG report, CERN FAQ, other official safety documents — slice 1's territory; not minted.
- Plaga's critique paper — slice 6's territory; not minted (would have been directly relevant to the "soft spot" theme but ownership is explicit in the search plan).

## Shape of the slice

~21 sources, cleanly split three ways: (1) 5 papers establishing the TeV-gravity model family that is the *sole* theoretical route to LHC black holes (ADD, RS1/RS2, plus two direct extensions), (2) 5 papers on production cross-sections/decay signatures at colliders specifically, (3) 5 papers on the Hawking-radiation mechanism itself (Bekenstein precursor through the two Page evaporation-rate papers), and (4) 6 papers making up the dissent/soft-spot side (4 direct critiques of varying strength — Helfer, Unruh's own trans-Planckian-origin paper, Jacobson's technical treatment, Belinski's outright rejection — plus 2 on the remnant/stalled-evaporation alternative). This gives Premise A's mechanism and its most serious acknowledged weakness roughly balanced coverage, per the brief's instruction to actively surface the soft spot rather than let it be crowded out.

What I could not find: a clean, recent (post-2010) primary paper specifically re-litigating trans-Planckian robustness for the LHC-collider-BH case in particular (most of the trans-Planckian literature is generic astrophysical-BH-evaporation theory from the 1990s, not collider-specific) — the connection from "Hawking radiation might not be fully secure in general" to "therefore an LHC micro-BH specifically might not evaporate" is made by the searcher/synthesis, not by a single citable primary source. Also could not confirm citation counts for Belinski 1995 and MacGibbon 1987 (both marked `unknown`; likely low-triple-digits and mid-hundreds respectively based on secondary mentions, but I did not want to guess a specific number).
