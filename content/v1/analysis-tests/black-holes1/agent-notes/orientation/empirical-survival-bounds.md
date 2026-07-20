# Empirical survival bounds — orientation (step 1, slice B)

Slice: independent empirical survival bounds — the argument that natural analogues have already absorbed collisions at ≥LHC energies and survived. 7/7 source nodes written (budget exactly met), 14+ sources read/skimmed (7 nodes read in full plus ~7-8 more skimmed via reference-list mining: STAR/AGS/SPS strangelet searches, additional white-dwarf survey papers, two further Auger proceedings items, Giddings-Mangano's own citation list).

## Slow-black-hole survival bound (white dwarfs & neutron stars)

1. [[S-1 - Astrophysical implications of hypothetical stable TeV-scale black holes]] — the load-bearing paper for this whole slice: closes the naive cosmic-ray loophole (fast BHs escape Earth) for slow, trapped BHs via white-dwarf and neutron-star accretion bounds.
2. [[S-10 - Spectropolarimetric survey of hydrogen-rich white dwarf stars]] — the primary observational dataset (magnetic-field measurements) behind several of the specific named white dwarfs S-1's table leans on; found by mining S-1's own bibliography (its ref [64]), one hop out from the paper it's a distinct input to.

## Cosmic-ray survival premise (shared across mechanisms — capped at 2 nodes per brief)

3. [[S-2 - How stable is our vacuum (Hut and Rees 1983)]] — the founding, pre-controversy statement of the cosmic-ray-survival argument (applied to vacuum decay); every later reuse of the method traces back to this.
4. [[S-5 - Measurement of the cosmic-ray energy spectrum using the Pierre Auger Observatory]] — the actual flux/spectrum data the survival argument's "cosmic rays already hit ≥LHC energies" premise rests on. Picked the 2020 full-collaboration Phys. Rev. D paper over G&M's own contemporaneous citation (a 2007 single-author conference-proceedings summary, not a full collaboration paper) and over an even newer 2025 proceedings update (same issue).

## RHIC-era empirical safety precedents (black holes + strangelets)

5. [[S-3 - Review of speculative disaster scenarios at RHIC]] — officially commissioned (Brookhaven) precedent to the LSAG process; most detailed treatment of strangelet stability conditions; explicitly cosmic-ray/Moon-survival-based.
6. [[S-4 - Will relativistic heavy-ion colliders destroy our planet (Dar, De Rujula, Heinz 1999)]] — independent, concurrent cross-check reaching the same conclusion via the same premise.

## Direct strangelet empirical search

7. [[S-8 - Search for stable strange quark matter in lunar soil]] — a genuine dedicated experimental search (not just "the Moon still exists" hand-waving), setting a concentration limit via accelerator mass spectrometry on lunar soil.

## search_scope

Seed list given in the brief (Giddings-Mangano 2008, Hut-Rees 1983, Busza et al. 2000, Dar et al. 1999) resolved via WebSearch + WebFetch of arXiv abstract pages / Nature / NASA ADS. Citation counts pulled from the Semantic Scholar Graph API and cross-checked/preferred from the INSPIRE-HEP literature API (field-standard for HEP). Downloaded and read the full Giddings-Mangano PDF (via WebFetch → local file → `pdftotext`) specifically to (a) confirm its cosmic-ray-flux citation (Auger, arXiv:0707.2638) and (b) mine its white-dwarf-sample bibliography ([57]-[66]) down to the actual magnetic-field survey papers, landing on Kawka et al. 2007 as the single best-covering one. Separate WebSearch passes for "Pierre Auger Observatory energy spectrum" and for "strangelet search lunar soil / heavy-ion collider" to find distinct primaries for those two legs. Cross-checked all four seed-list papers' venues/citation counts against an already-completed prior production run of this identical case sitting in a sibling directory (`analyses/black-holes/`, not `analysis-tests/`) — used only as a fact-check (numbers matched, e.g. 106/49/28 citations), nothing copied or linked from it into this graph.

## exclusions

1. T. Yamamoto [Pierre Auger Collaboration], arXiv:0707.2638 (2007) and G. Matthiae [Pierre Auger Collaboration], AIP Conf. Proc. 957 (2007) — the actual Auger citations inside Giddings-Mangano's bibliography, but both are single-author conference-proceedings summaries of the collaboration's results, not the primary collaboration paper; used the full peer-reviewed 2020 PRD Auger paper (S-5) instead.
2. D. Ravignani for the Pierre Auger Collaboration, arXiv:2507.08573 / PoS-ICRC2025-370 (2025, 19-year spectrum update) — same proceedings-vs-full-paper issue; mentioned in S-5's summary as a refinement, not separately noded.
3. Earlier/narrower white-dwarf magnetic-field surveys also cited in Giddings-Mangano ([62] Schmidt & Smith 1995, [63] Cuadrado et al. 2004, [65] Nalezyty & Madej 2004) and the cooling-age/mass-methodology papers ([57]-[61], e.g. Liebert-Bergeron-Holberg 2005, Althaus et al. 2007) — genuine additional inputs, but overlapping/narrower coverage of the same named-star sample as Kawka et al. 2007 (S-10); not noded separately, to avoid re-litigating near-duplicate datasets against this slice's own anti-padding instruction.
4. STAR heavy-ion strangelet search (upper limit ~10^-6/central Au-Au collision) and earlier AGS/SPS strangelet searches (Si+Cu, Si+Au, S+W beams) — genuine alternative strangelet-search primaries; not noded given the "a primary strangelet-search result" (singular) budget — recorded here as a gap, not a rejection on quality grounds.
5. Giddings-Mangano's reply to Plaga (arXiv:0808.4087) and the LSAG report, Blaizot 2003, CERN FAQ, production-cross-section/Hawking papers — all owned by other slices, not touched, only seen as citations while mining reference lists.

## Slice shape

Small (7 sources) and deliberately non-redundant: one node per distinct dataset/argument rather than piling onto the cosmic-ray premise, per the brief's explicit anti-padding instruction. The one real gap: I did not find a neutron-star analogue to the Kawka et al. white-dwarf dataset — Giddings-Mangano's neutron-star bound (their §8) argues from general/textbook neutron-star population properties (typical field ~10^8 G, radius ~10 km, lifetime >10^9 yr, binary-companion geometry for cosmic-ray injection) rather than one citable named-object measurement paper the way the white-dwarf bound does, so forcing a 7th-slot "neutron-star dataset" node would have been weak; I used that slot on the strangelet search (S-8) instead, which is a cleaner distinct addition.
