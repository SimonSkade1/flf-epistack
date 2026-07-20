# 1a — Search plan (step 1, LHC black-holes)

Main question: "Was the risk that LHC collisions destroy the Earth (via stable micro black holes or other proposed mechanisms) truly put to rest, and what does that conclusion hinge on?"
curated_target_N = 5. Step-1 totals across all searchers: **~20 `source` nodes written, ~40 read properly** (more skimmed via reference lists). This plan uses **3 searcher slices**.

## Literature map (what bears on the question)

The verdict "no risk" is a *conjunction* of independent sub-arguments, each with its own literature and its own weakest link. The graph's value is showing which link each mechanism hangs on.

1. **Official safety case + micro-BH theory.** Whether TeV black holes are even *produced* (large-extra-dimension / ADD models: production cross-sections), and whether they *decay* (Hawking radiation). The umbrella safety determinations: LSAG report (Ellis–Giddings–Mangano–Sandweiss–Wilczek 2008) and its predecessor (Blaizot et al. 2003). Hinge: Hawking radiation is theoretically robust but **never observed**; if it fails, a produced BH could be stable, and the whole load shifts to the empirical bounds (slice 2).
2. **Independent empirical survival bounds.** The empirical backbone: natural analogues have absorbed collisions at ≥LHC energies for eons and survived. Cosmic-ray survival argument (Hut–Rees 1983 for vacuum; Busza–Jaffe–Sandweiss–Wilczek 2000 and Dar–De Rújula–Heinz 1999 for RHIC-era strangelets/BH). The **load-bearing refinement**: cosmic-ray-produced BHs move fast and escape Earth, so the naive cosmic-ray argument does *not* cover slow LHC-produced BHs — Giddings–Mangano 2008 closes that loophole with white-dwarf / neutron-star survival bounds. Also strangelet conversion and its empirical searches.
3. **Critics, dissent, risk-methodology, historical precedent.** The side the CERN-affiliated reports argue against: Plaga 2008 (metastable-BH catastrophe scenario) and the Giddings–Mangano reply; Rössler's critique and CERN's rebuttal; the Wagner–Sancho US federal lawsuit (2008). Meta-level: how do you bound an a-priori catastrophe probability when the dominant uncertainty is theory error, not measurement error? — Ord–Hillerbrand–Sandberg 2010, Kent 2004, Tegmark–Bostrom 2005, and the 1946 LA-602 atmospheric-ignition report as methodological analogue.

## Sides of the debate

1. Pro-safety establishment (CERN/LSAG, Giddings–Mangano, RHIC reviewers) — dominant, peer-reviewed.
2. Critics/dissenters (Plaga, Rössler, Wagner & Sancho) — minority, partly non-peer-reviewed / legal.
3. Meta / risk-methodology (Ord et al., Kent, Tegmark–Bostrom) — argue the *form* of the risk argument, not the physics; largely orthogonal to which side "wins."

Slice 3 owns sides 2 and 3 so dissent and methodology are represented rather than crowded out by safety reports.

## Recurring datasets / argument-bases (flag for step 2's shared `D`-nodes)

1. **Cosmic-ray survival argument** — the single most-reused premise; routes through BH, strangelet AND vacuum-decay mechanisms. Give it ONE identity. Searchers: when a source rests on it, say so in `summary`/`relevance_note` (do NOT write `data_basis` — step 2 owns that), so step 2 can build the shared basis and avoid counting 40 re-analyses of one dataset as independent.
2. **White-dwarf / neutron-star survival bound** (Giddings–Mangano) — independent astrophysical dataset that closes the cosmic-ray loophole for *slow* BHs; distinct from #1.
3. **Hawking radiation** — theoretical basis for evaporation; unobserved. If it holds, mechanisms 1–2 are backup; if it fails, they carry everything.
4. **Production cross-section under large extra dimensions** — premise that BHs form at all (and is itself contested, e.g. Meade–Randall).
5. **A-priori risk-bounding methodology** — theory-error-dominated probability estimates; LA-602 as the founding analogue.

## Slicing & budget

Collision control: each canonical primary is owned by exactly ONE slice (lists below). Other slices mine it as a discovery hub but must NOT create a node for it. Giddings–Mangano 2008 → slice B; LSAG report → slice A; the critic papers → slice C.

| slice | owns | written | read |
|---|---|---|---|
| A — official safety case + micro-BH theory (production/Hawking/accretion theory) | 7 | 14 |
| B — independent empirical survival bounds (cosmic-ray, white-dwarf/neutron-star, strangelet) | 7 | 14 |
| C — critics, dissent, risk-methodology, historical precedent | 6 | 12 |
| **total** | | **20** | **40** |

Gaps I anticipate (told to each searcher): Rössler's material is largely non-peer-reviewed/self-published; the Wagner–Sancho lawsuit is legal/news, not scientific — capture as `report`/`news`, don't force a journal citation.

---

## SEARCHER PROMPTS (copy-paste each block between the delimiters)

═══════════ BEGIN SEARCHER 1B-A PROMPT ═══════════

Read .claude/skills/flf-epistack/steps/step-01-find-sources.md — it is your full instruction set. You are a **1b searcher**.
Analysis directory: projects/create a useful aligning (AI-)macroagents agenda/Participate in FLF competition/analysis-tests/black-holes1
(Quote the path in shell commands; cwd = vault root /home/simonskade/workspace.)
Main question (verbatim): "Was the risk that LHC collisions destroy the Earth (via stable micro black holes or other proposed mechanisms) truly put to rest, and what does that conclusion hinge on?"

Your slice: **Official safety case + micro-black-hole theory (production, Hawking decay, accretion theory).** You own the establishment/pro-safety *theoretical* case: whether TeV micro black holes are produced at all, and whether they evaporate. Snowball out from the CERN FAQ starting material (https://home.cern/resources/faqs/will-cern-generate-black-hole) to the primary safety analyses and the underlying theory. Target primaries (seed list — snowball backward/forward from these, don't stop at them):
- CERN FAQ webpage (create a node as the canonical public "put-to-rest" statement; source_type webpage; then snowball past it — it is a summary, not a primary analysis).
- LSAG report: Ellis, Giddings, Mangano, Sandweiss, Wilczek, "Review of the Safety of LHC Collisions", J. Phys. G 35 (2008) 115004, arXiv:0806.3414. (The umbrella safety determination — treat as a primary artifact of the official verdict AND as a discovery hub for its reference list.)
- Blaizot, Iliopoulos, Madsen, Ross, Sonderegger, Specht, "Study of Potentially Dangerous Events During Heavy-Ion Collisions at the LHC" (LHC Safety Study Group, CERN-2003-001, 2003) — the first LHC-specific safety report.
- Micro-BH production theory: Dimopoulos & Landsberg, "Black Holes at the LHC", PRL 87 (2001) 161602; Giddings & Thomas, "High-energy colliders as black-hole factories", Phys. Rev. D 65 (2002) 056010. (Enabling premise: large extra dimensions — Arkani-Hamed–Dimopoulos–Dvali 1998 — capture if cheap.)
- Hawking radiation as the decay basis: Hawking, "Particle creation by black holes", Commun. Math. Phys. 43 (1975) 199. Note explicitly in your summary that it is theoretically central but never observed (this is a key hinge).
- A dissenting-*theory* primary on whether TeV BH production/semiclassical treatment is even robust: Meade & Randall, "Black holes and quantum gravity at the LHC", JHEP 2008. (This is a physics-internal caveat, not a catastrophe claim — it belongs here, not in slice C.)
Do NOT touch (owned by other slices — mine as discovery hubs, do NOT create nodes): Giddings–Mangano 2008 astrophysical-bounds paper and all cosmic-ray / white-dwarf / neutron-star / strangelet empirical-survival data (slice B); Plaga, Rössler, Wagner–Sancho, Ord/Kent/Tegmark-Bostrom risk-methodology, and LA-602 (slice C). When you note in a summary that a source rests on the cosmic-ray survival argument, describe it in prose only — do NOT write a `data_basis` field (step 2 owns that).

Budget: **7 source notes written, 14 sources read properly** (skim many more via reference lists). Primary sources only; get to the artifact that made the claim in ≤2 hops; reviews are discovery hubs, not nodes.
Mint every id'd node with:
  python3 .claude/skills/flf-epistack/scripts/create_node.py "projects/create a useful aligning (AI-)macroagents agenda/Participate in FLF competition/analysis-tests/black-holes1" --type source --title "..."
(Pipe the node markdown with `{{ID}}` placeholders on stdin per the mode file; never hand-pick an id, and do not spawn subagents.)
Return: the S-ids you created, any gaps you hit, and a short report. Before returning, write your orientation note at agent-notes/orientation/official-safety-case.md per the mode file (sources as wikilinks under topic headings best-first; search_scope; exclusions; one paragraph on slice shape).

┌─ TEST-RUN NOTICE — copy verbatim into every subagent brief ─────────────┐

This is a **quick test run under time pressure**, not a production analysis. The goal is only to surface **major errors or problems in the pipeline**, not to produce an optimal output. Work **fast**, and don't worry about your output being imperfect or sub-optimal — a rough, correct-enough pass is exactly what's wanted; do not polish or iterate. **Do not log minor imperfections.** If you hit a real problem — a pipeline bug, a broken or ambiguous cross-step interface, missing or contradictory instructions, a script that errors, or anything that blocks or corrupts the run — append ONE entry to the problem log with a severity tag (`BLOCKER` or `MAJOR`) and one line of context (which step, which slice, what happened). The log is at:
`projects/create a useful aligning (AI-)macroagents agenda/Participate in FLF competition/analysis-tests/black-holes1/problem-log.md`
Append with a single write (e.g. a `>>` shell append) so parallel appends don't clobber each other; never edit or delete other agents' entries. Then keep going if you can.

└──────────────────────────────────────────────────────────────────────────┘

═══════════ END SEARCHER 1B-A PROMPT ═══════════

═══════════ BEGIN SEARCHER 1B-B PROMPT ═══════════

Read .claude/skills/flf-epistack/steps/step-01-find-sources.md — it is your full instruction set. You are a **1b searcher**.
Analysis directory: projects/create a useful aligning (AI-)macroagents agenda/Participate in FLF competition/analysis-tests/black-holes1
(Quote the path in shell commands; cwd = vault root /home/simonskade/workspace.)
Main question (verbatim): "Was the risk that LHC collisions destroy the Earth (via stable micro black holes or other proposed mechanisms) truly put to rest, and what does that conclusion hinge on?"

Your slice: **Independent empirical survival bounds — the empirical backbone.** You own the argument that natural analogues have survived collisions at ≥LHC energies: cosmic-ray survival bounds, white-dwarf / neutron-star survival bounds, and strangelet empirical searches. This is where the "genuinely independent data" lives — but the task warns against padding with **40 re-analyses of one cosmic-ray dataset**: capture the cosmic-ray flux/survival premise with 1–2 primary nodes at most, then spend the rest of the budget on *distinct* datasets (white-dwarf cooling, neutron-star existence, lunar/heavy-ion strangelet searches). Target primaries (seed list — snowball backward/forward):
- Giddings & Mangano, "Astrophysical implications of hypothetical stable TeV-scale black holes", Phys. Rev. D 78 (2008) 035009, arXiv:0806.3381. **This paper is yours** — it is the core empirical safety analysis (white-dwarf/neutron-star survival closing the cosmic-ray loophole for slow BHs, plus accretion-rate bounds). Node it; also mine its reference list.
- Hut & Rees, "How stable is our vacuum?", Nature 302 (1983) 508 — seminal cosmic-ray survival bound (vacuum decay). 
- RHIC-era empirical reviews (both are primary safety analyses for their era, and discovery hubs): Busza, Jaffe, Sandweiss, Wilczek, "Review of speculative disaster scenarios at RHIC", Rev. Mod. Phys. 72 (2000) 1125, arXiv:hep-ph/9910333; Dar, De Rújula, Heinz, "Will relativistic heavy-ion colliders destroy our planet?", Phys. Lett. B 470 (1999) 142.
- The cosmic-ray premise itself: ONE primary node for the ultra-high-energy cosmic-ray flux/spectrum the survival argument uses (e.g. Pierre Auger Observatory spectrum). Do not multiply these.
- Strangelet empirical bounds: a primary strangelet-search result (e.g. lunar-soil or AMS / heavy-ion strangelet search) constraining strangelet existence/stability.
- If cheap: a primary white-dwarf or neutron-star observational dataset (cooling ages / masses) that the survival bound leans on, if distinct from what's inside Giddings–Mangano.
Do NOT touch (owned by other slices — mine as discovery hubs, do NOT create nodes): the LSAG report, Blaizot 2003, production-cross-section and Hawking-radiation theory papers, CERN FAQ (slice A); Plaga, Rössler, Wagner–Sancho, risk-methodology papers, LA-602 (slice C). When a source rests on the cosmic-ray survival argument, say so in prose in the `summary`/`relevance_note` — do NOT write a `data_basis` field (step 2 owns the shared data-basis).

Budget: **7 source notes written, 14 sources read properly** (skim more via reference lists). Primary sources only; ≤2 hops to the artifact; reviews are discovery hubs, not nodes.
Mint every id'd node with:
  python3 .claude/skills/flf-epistack/scripts/create_node.py "projects/create a useful aligning (AI-)macroagents agenda/Participate in FLF competition/analysis-tests/black-holes1" --type source --title "..."
(Pipe the node markdown with `{{ID}}` placeholders on stdin per the mode file; never hand-pick an id, and do not spawn subagents.)
Return: the S-ids you created, any gaps you hit, and a short report. Before returning, write your orientation note at agent-notes/orientation/empirical-survival-bounds.md per the mode file (sources as wikilinks under topic headings best-first; search_scope; exclusions; one paragraph on slice shape).

┌─ TEST-RUN NOTICE — copy verbatim into every subagent brief ─────────────┐

This is a **quick test run under time pressure**, not a production analysis. The goal is only to surface **major errors or problems in the pipeline**, not to produce an optimal output. Work **fast**, and don't worry about your output being imperfect or sub-optimal — a rough, correct-enough pass is exactly what's wanted; do not polish or iterate. **Do not log minor imperfections.** If you hit a real problem — a pipeline bug, a broken or ambiguous cross-step interface, missing or contradictory instructions, a script that errors, or anything that blocks or corrupts the run — append ONE entry to the problem log with a severity tag (`BLOCKER` or `MAJOR`) and one line of context (which step, which slice, what happened). The log is at:
`projects/create a useful aligning (AI-)macroagents agenda/Participate in FLF competition/analysis-tests/black-holes1/problem-log.md`
Append with a single write (e.g. a `>>` shell append) so parallel appends don't clobber each other; never edit or delete other agents' entries. Then keep going if you can.

└──────────────────────────────────────────────────────────────────────────┘

═══════════ END SEARCHER 1B-B PROMPT ═══════════

═══════════ BEGIN SEARCHER 1B-C PROMPT ═══════════

Read .claude/skills/flf-epistack/steps/step-01-find-sources.md — it is your full instruction set. You are a **1b searcher**.
Analysis directory: projects/create a useful aligning (AI-)macroagents agenda/Participate in FLF competition/analysis-tests/black-holes1
(Quote the path in shell commands; cwd = vault root /home/simonskade/workspace.)
Main question (verbatim): "Was the risk that LHC collisions destroy the Earth (via stable micro black holes or other proposed mechanisms) truly put to rest, and what does that conclusion hinge on?"

Your slice: **Critics, dissent, risk-methodology, and historical precedent.** You own the side the safety reports argue *against*, plus the meta-level question of how to bound an a-priori catastrophe probability. Balance and independence are the whole point of this slice — represent the dissenters in their own words, not only as filtered through CERN rebuttals. Target primaries (seed list — snowball backward/forward):
- Scientific critics: Plaga, "On the potential catastrophic risk from metastable quantum-black holes produced at particle colliders", arXiv:0808.1415 (2008); AND the Giddings–Mangano reply to Plaga (arXiv:0808.4087) — capture BOTH as the critic exchange. Rössler's safety critique (largely self-published / non-peer-reviewed) and CERN's/LSAG's rebuttal to it — capture what you can find, flag `motivatedness`/non-peer-reviewed status.
- Legal/public: the Wagner & Sancho federal lawsuit (US District Court, Hawaii, 2008) seeking to halt LHC startup — capture as report/news (legal filing or contemporaneous coverage), not a journal article.
- Risk-assessment methodology (how to bound theory-error-dominated catastrophe probabilities): Ord, Hillerbrand & Sandberg, "Probing the improbability of a catastrophe", J. Risk Research (2010), arXiv:0810.5515; Kent, "A critical look at risk assessments for global catastrophes", Risk Analysis (2004); Tegmark & Bostrom, "Is a doomsday catastrophe likely?", Nature 438 (2005) 754.
- Historical precedent / methodological analogue (starting material): the 1946 LA-602 Konopinski–Marvin–Teller "Ignition of the Atmosphere with Nuclear Bombs" report (https://blog.nuclearsecrecy.com/wp-content/uploads/2018/06/1946-LA-602-Konopinski-Marvin-Teller-Ignition-fo-the-Atmsophere.pdf) — the founding a-priori catastrophe-bound calculation; node it as source_type report.
Do NOT touch (owned by other slices — mine as discovery hubs, do NOT create nodes): the LSAG report, Blaizot 2003, production/Hawking theory, CERN FAQ (slice A); Giddings–Mangano 2008 astrophysical-bounds paper and the cosmic-ray/white-dwarf/neutron-star/strangelet empirical data (slice B). You MAY node the Giddings–Mangano *reply-to-Plaga* (0808.4087) because it is part of the critic exchange, but not the main astrophysical-bounds paper. Record `motivatedness`/COI on the page (e.g. lawsuit plaintiffs, self-published critics) as plain data — do not defer to it or dismiss it.

Budget: **6 source notes written, 12 sources read properly** (skim more via reference lists). Primary artifacts (the critic's own paper, the actual filing, the actual report), not commentary about them; ≤2 hops.
Mint every id'd node with:
  python3 .claude/skills/flf-epistack/scripts/create_node.py "projects/create a useful aligning (AI-)macroagents agenda/Participate in FLF competition/analysis-tests/black-holes1" --type source --title "..."
(Pipe the node markdown with `{{ID}}` placeholders on stdin per the mode file; never hand-pick an id, and do not spawn subagents.)
Return: the S-ids you created, any gaps you hit, and a short report. Before returning, write your orientation note at agent-notes/orientation/critics-and-methodology.md per the mode file (sources as wikilinks under topic headings best-first; search_scope; exclusions; one paragraph on slice shape).

┌─ TEST-RUN NOTICE — copy verbatim into every subagent brief ─────────────┐

This is a **quick test run under time pressure**, not a production analysis. The goal is only to surface **major errors or problems in the pipeline**, not to produce an optimal output. Work **fast**, and don't worry about your output being imperfect or sub-optimal — a rough, correct-enough pass is exactly what's wanted; do not polish or iterate. **Do not log minor imperfections.** If you hit a real problem — a pipeline bug, a broken or ambiguous cross-step interface, missing or contradictory instructions, a script that errors, or anything that blocks or corrupts the run — append ONE entry to the problem log with a severity tag (`BLOCKER` or `MAJOR`) and one line of context (which step, which slice, what happened). The log is at:
`projects/create a useful aligning (AI-)macroagents agenda/Participate in FLF competition/analysis-tests/black-holes1/problem-log.md`
Append with a single write (e.g. a `>>` shell append) so parallel appends don't clobber each other; never edit or delete other agents' entries. Then keep going if you can.

└──────────────────────────────────────────────────────────────────────────┘

═══════════ END SEARCHER 1B-C PROMPT ═══════════
