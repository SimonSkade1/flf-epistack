# Step 1 search plan (role 1a) — LHC black-hole safety case

Main question: "Was the risk that LHC collisions destroy the Earth (via stable micro black holes or other proposed mechanisms) truly put to rest, and what does that conclusion hinge on?"

Scope/intent (FLF framing): probe the *safety argument* for its dependencies and key considerations, and surface its weakest / most speculative points. So the source pool must cover (a) the official safety case, (b) the physics premises each leg rests on, (c) the genuinely independent empirical datasets those legs invoke, (d) the alternative disaster mechanisms, and (e) the critics and the risk-assessment/philosophy-of-safety literature that dispute whether the case is airtight.

## 1. Survey: literatures, sides, recurring datasets

**Dependency structure of the safety case** (this is what the slices map onto). The modern official argument (LSAG 2008, resting on Giddings–Mangano 2008) is a two-premise cascade:
- **Premise A — evaporation.** Any micro black hole (BH) that could form decays via Hawking radiation, so nothing persists. This rests on Hawking-radiation theory (GR + QFT), which is experimentally unconfirmed — the acknowledged soft spot.
- **Premise B — empirical safety even if A fails.** *Even if* Hawking radiation is wrong and BHs are stable, they are harmless, because Nature already runs the experiment: ultra-high-energy cosmic rays have struck the Earth, Sun, and dense stars for billions of years at energies exceeding the LHC. The subtle loophole is that cosmic-ray-produced BHs are ultra-relativistic (they punch through Earth and escape) whereas a collider could produce slow/trapped ones. Giddings–Mangano close this by moving to **white dwarfs and neutron stars**: their density would trap even slow BHs, yet these objects survive for Gyr — bounding stable-BH production or accretion. A parallel **accretion-timescale** calculation shows even a trapped stable BH would take longer than the age of the Universe to grow dangerously.

**Literatures that bear on the question:**
1. Institutional safety reports (LSAG, RHIC-era reviews, CERN FAQ, SPC endorsement).
2. TeV-scale-gravity / extra-dimensions phenomenology + collider BH-production cross-sections (the *only* way the LHC could make BHs at all).
3. Hawking-radiation theory and its critiques.
4. Astrophysical survival argument + accretion physics + compact-star observations.
5. Ultra-high-energy cosmic-ray (UHECR) spectrum and flux measurements.
6. Alternative mechanisms: strangelets/strange quark matter, Higgs-vacuum decay, magnetic monopoles.
7. Critics of the safety case + meta-level risk-assessment / decision-theory / legal-philosophy literature.

**Sides of the debate:**
- *Safety-case proponents:* Ellis, Giudice, Mangano, Tkachev, Wenninger (LSAG); Giddings, Mangano; Busza, Jaffe, Sandweiss, Wilczek; Dar–De Rújula–Heinz; Koch–Bleicher–Stöcker.
- *Critics / dissenters:* Rössler (stable growing BHs); Plaga (metastable-BH catastrophe scenario); Wagner & Sancho (litigation); and the *risk-methodology* critics who don't claim danger but claim the safety **argument** is under-rigorous: Kent, Ord–Hillerbrand–Sandberg, Johnson, Calogero, Posner.

**Recurring / independent datasets** (the independence axis — slices are drawn so different legs rest on different data, not on re-analyses of one):
- UHECR flux/spectrum (Auger, HiRes, AGASA, Fly's Eye "Oh-My-God" event) — one independent empirical pillar (slice 4).
- White-dwarf & neutron-star masses/densities/ages (SDSS WD catalogs, NS cooling ages) — a *different* independent empirical pillar (slice 3).
- Hawking-radiation theory — a theoretical (not data) pillar; independent of both above (slice 2).
- BH-production cross-sections / extra-dimension model parameters — theoretical, independent again (slice 2).

## 2. Slice division & rationale

Six searchers. Budgets sum to the step-1 totals: **100 `source` notes written, 200 sources read properly** (skim far more via reviews/reference lists). curated_target_N = 25 (→ ~4×N write, ~8×N read).

| # | Slice | Write | Read |
|---|-------|-------|------|
| 1 | Official safety case & institutional reports | 12 | 24 |
| 2 | BH production theory + Hawking radiation (& its critiques) | 20 | 40 |
| 3 | Astrophysical survival argument + accretion + compact-star data | 20 | 40 |
| 4 | Ultra-high-energy cosmic-ray flux/spectrum data | 16 | 32 |
| 5 | Alternative mechanisms: strangelets, vacuum decay, monopoles | 16 | 32 |
| 6 | Critics & risk-assessment / philosophy-of-safety literature | 16 | 32 |
| | **Total** | **100** | **200** |

**Balance:** slices 1–5 build up the safety case and its physics premises; slice 6 is dedicated to the critical side, and slices 2/5 are each told to actively seek the dissenting/soft-spot papers within their own physics (Hawking-radiation skeptics; vacuum-metastability worriers) so criticism is not ghettoised into slice 6 alone.

**Independence:** the two empirical legs of Premise B are deliberately split — slice 4 owns the cosmic-ray dataset, slice 3 owns the compact-star dataset — so the pool contains two genuinely independent empirical bases, not many re-analyses of one. Slice 2 supplies the theoretical premises (production + evaporation) that are independent of both. This is the only place that shape is chosen, since no searcher sees the pool.

**Primary-source rule applied to this case:** the official safety reports (LSAG, Blaizot, Busza et al., CERN FAQ) are the *object being probed*, so they are treated as primary artifacts and get `source` nodes; but any literature-review content *inside* them is mined for the primaries it cites. Scholarly argument papers (Kent, Ord et al., Plaga, Giddings–Mangano) are primary artifacts of a position and get nodes. Pure textbook reviews / encyclopedia articles do **not** get nodes — mine them and record under `found_via`.

**Boundary / de-duplication rules given to searchers:**
- Slice 1 owns the safety *reports themselves*; slice 6 owns *critiques of* those reports.
- Slice 3 owns Giddings–Mangano 2008 **and** its formal reply to Plaga (same authors, astrophysical content). Slice 6 owns Plaga's critique; it mines the reply via `found_via` but does not mint it.
- Slice 2 owns Hawking-radiation theory and BH-production cross-sections; slice 3 owns what happens to an *already-produced stable* BH (accretion/survival). The Dimopoulos–Landsberg / Giddings–Thomas production papers belong to slice 2.
- Strangelets/vacuum/monopoles belong to slice 5 even where an official report discusses them; slice 1 mints only the report node and points to slice 5 for the mechanism primaries.
- If a searcher finds a paper it believes another slice owns, it records it under `found_via` and does not mint it.

## 3. Searcher prompts

### Searcher 1 — Official safety case & institutional reports

```
Read /home/simonskade/workspace/.claude/skills/flf-epistack/steps/step-01-find-sources.md — it is your full instruction set. Your role is a 1b searcher.
Analysis directory: /home/simonskade/workspace/external-projects/flf-epistack/content/v1/analyses/black-holes
Main question (verbatim): "Was the risk that LHC collisions destroy the Earth (via stable micro black holes or other proposed mechanisms) truly put to rest, and what does that conclusion hinge on?"
Your slice: The official / institutional safety case — the reports that constitute and endorse the "it's safe" verdict, treated here as PRIMARY artifacts because they are the object being probed. Cover: the LHC Safety Assessment Group (LSAG) report (Ellis, Giudice, Mangano, Tkachev, Wenninger, "Review of the Safety of LHC Collisions," J.Phys.G 35 (2008) 115004, arXiv:0806.3414); the 2003 CERN heavy-ion study (Blaizot, Iliopoulos, Madsen, Ross, Sonderegger, Specht, CERN-2003-001); the RHIC-era review (Busza, Jaffe, Sandweiss, Wilczek, "Review of Speculative Disaster Scenarios at RHIC," Rev.Mod.Phys. 72 (2000) 1125, arXiv:hep-ph/9910333); Dar, De Rújula, Heinz, "Will relativistic heavy ion colliders destroy our planet?" (Phys.Lett.B 470 (1999) 142, hep-ph/9910471); the CERN FAQ page (https://home.cern/resources/faqs/will-cern-generate-black-hole); the CERN Scientific Policy Committee endorsement of LSAG; and the 1946 Konopinski–Marvin–Teller LA-602 atmospheric-ignition report (https://blog.nuclearsecrecy.com/wp-content/uploads/2018/06/1946-LA-602-Konopinski-Marvin-Teller-Ignition-fo-the-Atmsophere.pdf) as the canonical historical precedent for pre-experiment catastrophe assessment. Also look for any Koch–Bleicher–Stöcker "exclusion of black hole disaster scenarios" reanalysis and any official update/response documents. Mine each report's reference list for primaries but, when a cited primary is a black-hole-production paper (slice 2), an astrophysical-survival/accretion paper (slice 3), a cosmic-ray-flux paper (slice 4), or a strangelet/vacuum/monopole paper (slice 5), record it under found_via and do NOT mint it — those slices own it. Do NOT mint critiques of these reports (slice 6 owns those). Textbook/encyclopedia reviews get no node — mine and cite under found_via.
Budget: 12 `source` notes created, ~24 sources read properly; skim more via reference lists.
Mint every id'd node by piping its markdown on stdin (the body carries {{ID}}; the title never does):
  cat <<'EOF' | python3 /home/simonskade/workspace/.claude/skills/flf-epistack/scripts/create_node.py /home/simonskade/workspace/external-projects/flf-epistack/content/v1/analyses/black-holes --type source --title "Descriptive title, no id"
  ---
  id: {{ID}}
  type: source
  ...
  ---
  body
  EOF
Never hand-pick an id, and do not spawn subagents.
Return: the S-ids you created, your orientation-note path, gaps you hit, and a ≤10-line report.
```

### Searcher 2 — Black-hole production theory + Hawking radiation

```
Read /home/simonskade/workspace/.claude/skills/flf-epistack/steps/step-01-find-sources.md — it is your full instruction set. Your role is a 1b searcher.
Analysis directory: /home/simonskade/workspace/external-projects/flf-epistack/content/v1/analyses/black-holes
Main question (verbatim): "Was the risk that LHC collisions destroy the Earth (via stable micro black holes or other proposed mechanisms) truly put to rest, and what does that conclusion hinge on?"
Your slice: The theoretical physics of Premise A of the safety case — (i) whether the LHC could produce micro black holes at all, and (ii) whether Hawking radiation would evaporate them. This is the pool for both the mechanism and its acknowledged soft spot. Cover: TeV-scale-gravity / large-extra-dimension models that are the ONLY route to collider BHs (Arkani-Hamed, Dimopoulos, Dvali 1998 "The Hierarchy Problem and New Dimensions at a Millimeter," Phys.Lett.B 429; Randall, Sundrum 1999 warped extra dimensions, PRL 83); collider BH-production cross-section papers (Dimopoulos, Landsberg "Black Holes at the LHC," PRL 87 (2001) 161602; Giddings, Thomas "High energy colliders as black hole factories," Phys.Rev.D 65 (2002) 056010); Hawking radiation foundations (Hawking 1974 "Black hole explosions?" Nature 248; Hawking 1975 "Particle Creation by Black Holes," Commun.Math.Phys. 43; Page evaporation-rate papers). ACTIVELY seek the dissent/soft-spot literature: papers questioning whether Hawking radiation is real or complete (e.g. Helfer "Do black holes radiate?" 2003; Unruh–Wald and the trans-Planckian problem; Belinski's objections), and any papers on the greybody/remnant scenario where evaporation stalls and a stable remnant survives. Boundary: what happens to an ALREADY-PRODUCED STABLE BH (accretion, astrophysical survival) belongs to slice 3 — record such papers under found_via, do not mint. Official safety reports belong to slice 1. Mine reviews for primaries; reviews get no node.
Budget: 20 `source` notes created, ~40 sources read properly; skim more via reference lists and citation-chasing.
Mint every id'd node by piping its markdown on stdin (the body carries {{ID}}; the title never does):
  cat <<'EOF' | python3 /home/simonskade/workspace/.claude/skills/flf-epistack/scripts/create_node.py /home/simonskade/workspace/external-projects/flf-epistack/content/v1/analyses/black-holes --type source --title "Descriptive title, no id"
  ---
  id: {{ID}}
  type: source
  ...
  ---
  body
  EOF
Never hand-pick an id, and do not spawn subagents.
Return: the S-ids you created, your orientation-note path, gaps you hit, and a ≤10-line report.
```

### Searcher 3 — Astrophysical survival argument, accretion, compact-star data

```
Read /home/simonskade/workspace/.claude/skills/flf-epistack/steps/step-01-find-sources.md — it is your full instruction set. Your role is a 1b searcher.
Analysis directory: /home/simonskade/workspace/external-projects/flf-epistack/content/v1/analyses/black-holes
Main question (verbatim): "Was the risk that LHC collisions destroy the Earth (via stable micro black holes or other proposed mechanisms) truly put to rest, and what does that conclusion hinge on?"
Your slice: Premise B of the safety case — the argument that a stable BH would still be harmless, and the INDEPENDENT COMPACT-STAR dataset it rests on. Cover: the load-bearing paper Giddings, Mangano "Astrophysical implications of hypothetical stable TeV-scale black holes," Phys.Rev.D 78 (2008) 035009, arXiv:0806.3381, AND its formal reply to Plaga (you own both — same authors, astrophysical content). Cover the accretion physics: Bondi 1952 accretion, electromagnetic/Coulomb accretion in condensed matter, and the accretion-timescale calculations bounding how fast a trapped stable BH could grow. Cover the empirical compact-star inputs the neutron-star/white-dwarf survival bound relies on — grab a FEW representative PRIMARY observational sources (e.g. an SDSS white-dwarf mass catalog such as Kepler et al.; a neutron-star mass-measurement or cooling-age paper; white-dwarf/neutron-star density and Gyr-age evidence) so the independent-data leg is concrete; do not exhaustively mine stellar astrophysics. Also cover the closely related Koch–Bleicher–Stöcker "Exclusion of black hole disaster scenarios at the LHC" (Phys.Lett.B 672 (2009) 71) if not taken by slice 1 — coordinate via found_via. Boundaries: BH PRODUCTION cross-sections and Hawking radiation belong to slice 2; UHECR flux/spectrum measurements belong to slice 4; Plaga's own critique paper belongs to slice 6 (mine it via found_via, don't mint). Mine reviews for primaries; reviews get no node.
Budget: 20 `source` notes created, ~40 sources read properly; skim more via reference lists and citation-chasing.
Mint every id'd node by piping its markdown on stdin (the body carries {{ID}}; the title never does):
  cat <<'EOF' | python3 /home/simonskade/workspace/.claude/skills/flf-epistack/scripts/create_node.py /home/simonskade/workspace/external-projects/flf-epistack/content/v1/analyses/black-holes --type source --title "Descriptive title, no id"
  ---
  id: {{ID}}
  type: source
  ...
  ---
  body
  EOF
Never hand-pick an id, and do not spawn subagents.
Return: the S-ids you created, your orientation-note path, gaps you hit, and a ≤10-line report.
```

### Searcher 4 — Ultra-high-energy cosmic-ray flux & spectrum data

```
Read /home/simonskade/workspace/.claude/skills/flf-epistack/steps/step-01-find-sources.md — it is your full instruction set. Your role is a 1b searcher.
Analysis directory: /home/simonskade/workspace/external-projects/flf-epistack/content/v1/analyses/black-holes
Main question (verbatim): "Was the risk that LHC collisions destroy the Earth (via stable micro black holes or other proposed mechanisms) truly put to rest, and what does that conclusion hinge on?"
Your slice: The other INDEPENDENT empirical pillar of Premise B — the ultra-high-energy cosmic-ray (UHECR) flux and spectrum, which underwrites "Nature has already run ~10^31 LHC-equivalent collisions on Earth, the Sun and stars for billions of years." This is a genuinely independent dataset from the compact-star data (slice 3); own the cosmic-ray measurements themselves. Cover PRIMARY measurement sources: Pierre Auger Observatory energy-spectrum papers; the High Resolution Fly's Eye (HiRes) spectrum; AGASA spectrum; the original Fly's Eye "Oh-My-God" ~3×10^20 eV event (Bird et al. 1995, ApJ 441); and any source establishing the cosmic-ray flux at and above LHC-equivalent centre-of-mass energy (~14 TeV, i.e. ~10^17 eV fixed-target) needed to compute how many natural high-energy collisions the Earth/Sun/stars have absorbed. Also grab the primary papers doing the "cosmic rays as a natural safety experiment" flux-to-collisions computation if they are distinct from the LSAG/Giddings–Mangano reports (those reports themselves belong to slices 1/3 — mine via found_via). Boundaries: the safety reports (slice 1), BH production/Hawking (slice 2), compact-star survival/accretion (slice 3). Mine review/spectrum-compilation papers for the underlying primary detector results; pure reviews get no node.
Budget: 16 `source` notes created, ~32 sources read properly; skim more via reference lists.
Mint every id'd node by piping its markdown on stdin (the body carries {{ID}}; the title never does):
  cat <<'EOF' | python3 /home/simonskade/workspace/.claude/skills/flf-epistack/scripts/create_node.py /home/simonskade/workspace/external-projects/flf-epistack/content/v1/analyses/black-holes --type source --title "Descriptive title, no id"
  ---
  id: {{ID}}
  type: source
  ...
  ---
  body
  EOF
Never hand-pick an id, and do not spawn subagents.
Return: the S-ids you created, your orientation-note path, gaps you hit, and a ≤10-line report.
```

### Searcher 5 — Alternative mechanisms: strangelets, vacuum decay, monopoles

```
Read /home/simonskade/workspace/.claude/skills/flf-epistack/steps/step-01-find-sources.md — it is your full instruction set. Your role is a 1b searcher.
Analysis directory: /home/simonskade/workspace/external-projects/flf-epistack/content/v1/analyses/black-holes
Main question (verbatim): "Was the risk that LHC collisions destroy the Earth (via stable micro black holes or other proposed mechanisms) truly put to rest, and what does that conclusion hinge on?"
Your slice: The "other proposed mechanisms" named in the main question — every collider-doomsday route OTHER than micro black holes. Three sub-threads: (1) STRANGELETS / strange quark matter converting ordinary matter — Witten "Cosmic separation of phases," Phys.Rev.D 30 (1984) 272; Farhi, Jaffe "Strange matter," Phys.Rev.D 30 (1984) 2379; the strangelet-safety analyses (mine the Busza et al. RHIC report and Dar–De Rújula–Heinz for their strangelet primaries but leave the reports to slice 1); any measurement bounding stable strangelet existence. (2) HIGGS / ELECTROWEAK VACUUM DECAY (true-vacuum bubble nucleation destroying spacetime) — Coleman, De Luccia "Gravitational effects on and of vacuum decay," Phys.Rev.D 21 (1980) 3305; Turner, Wilczek "Is our vacuum metastable?" Nature 298 (1982); the modern SM metastability computations (Degrassi et al. 2012 "Higgs mass and vacuum stability in the Standard Model at NNLO," arXiv:1205.6497; Espinosa et al.); actively include this as a live soft spot. (3) MAGNETIC MONOPOLES catalysing nucleon decay (Rubakov–Callan effect) — Rubakov 1981/82, Callan 1982, and any collider-monopole-search or safety bound. Boundaries: micro black holes belong to slices 2/3; the safety reports themselves to slice 1; risk-methodology critiques to slice 6. Mine reviews for primaries; reviews get no node.
Budget: 16 `source` notes created, ~32 sources read properly; skim more via reference lists.
Mint every id'd node by piping its markdown on stdin (the body carries {{ID}}; the title never does):
  cat <<'EOF' | python3 /home/simonskade/workspace/.claude/skills/flf-epistack/scripts/create_node.py /home/simonskade/workspace/external-projects/flf-epistack/content/v1/analyses/black-holes --type source --title "Descriptive title, no id"
  ---
  id: {{ID}}
  type: source
  ...
  ---
  body
  EOF
Never hand-pick an id, and do not spawn subagents.
Return: the S-ids you created, your orientation-note path, gaps you hit, and a ≤10-line report.
```

### Searcher 6 — Critics & risk-assessment / philosophy-of-safety literature

```
Read /home/simonskade/workspace/.claude/skills/flf-epistack/steps/step-01-find-sources.md — it is your full instruction set. Your role is a 1b searcher.
Analysis directory: /home/simonskade/workspace/external-projects/flf-epistack/content/v1/analyses/black-holes
Main question (verbatim): "Was the risk that LHC collisions destroy the Earth (via stable micro black holes or other proposed mechanisms) truly put to rest, and what does that conclusion hinge on?"
Your slice: The dissenting side — everyone who argued the danger was real OR that the safety ARGUMENT is under-rigorous, plus the meta-level risk-assessment / decision-theory / legal-philosophy literature. This slice guarantees the debate's critics are represented. Two sub-threads: (A) PHYSICS/CATASTROPHE DISSENTERS — Otto Rössler (e.g. "Abraham-Solution to Schwarzschild Metric Implies That CERN Miniblack Holes Pose a Planetary Risk," 2008, and related notes claiming stable growing BHs); Rainer Plaga "On the potential catastrophic risk from metastable quantum-black holes produced at particle colliders" (arXiv:0808.1415) — you OWN Plaga's critique; the Giddings–Mangano reply is slice 3's, mine it via found_via; the Wagner & Sancho v. CERN/DOE litigation filings (US District Court, Hawaii, 2008). (B) RISK-METHODOLOGY / PHILOSOPHY-OF-SAFETY — Adrian Kent "A Critical Look at Risk Assessments for Global Catastrophes" (Risk Analysis 24 (2004) 157, arXiv:hep-ph/0009204); Ord, Hillerbrand, Sandberg "Probing the Improbability of Catastrophe: Methodological Challenges for Risk Assessment of Rare Events" (arXiv:0810.5515); Eric E. Johnson "The Black Hole Case: The Injunction Against the End of the World" (Tennessee Law Review 76 (2009) 819); Francesco Calogero "Might a laboratory experiment destroy planet Earth?" (Interdisciplinary Science Reviews 25 (2000) 191); Richard Posner "Catastrophe: Risk and Response" (2004, relevant chapter). These argument papers are PRIMARY artifacts of a position — mint them. Boundaries: the pro-safety reports (slice 1), the physics premises (slices 2–5) — cite via found_via, don't mint. Mine reviews for primaries; encyclopedia/news roundups get no node (cite under found_via).
Budget: 16 `source` notes created, ~32 sources read properly; skim more via reference lists.
Mint every id'd node by piping its markdown on stdin (the body carries {{ID}}; the title never does):
  cat <<'EOF' | python3 /home/simonskade/workspace/.claude/skills/flf-epistack/scripts/create_node.py /home/simonskade/workspace/external-projects/flf-epistack/content/v1/analyses/black-holes --type source --title "Descriptive title, no id"
  ---
  id: {{ID}}
  type: source
  ...
  ---
  body
  EOF
Never hand-pick an id, and do not spawn subagents.
Return: the S-ids you created, your orientation-note path, gaps you hit, and a ≤10-line report.
```

## Notes for the consolidator (1c) / audit

- Per-searcher write budgets sum to 100; read budgets sum to 200. If a slice underfills, the shortfall most likely lands in slice 3 (compact-star primary observations are a rabbit hole and were deliberately capped) and slice 6 (some items are legal filings / books, not indexed papers).
- The independence guarantee lives in the slice-4 vs slice-3 split (cosmic-ray data vs compact-star data as the two empirical legs of Premise B). If the pool ends up dominated by one, that is a balance failure to flag.
- Each searcher writes exactly one orientation note in agent-notes/orientation/ named after its slice (e.g. official-safety-case.md, bh-production-hawking.md, astrophysical-survival.md, cosmic-ray-flux.md, alternative-mechanisms.md, critics-and-risk-assessment.md).
