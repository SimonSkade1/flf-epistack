# Structure note — step 4 (4b) — COVID origins

**generated:** 2026-07-23 04:14 CEST

## Counts

- **H handed in (step-3 total):** 40 (`H-1`…`H-40`)
- **active after 4b:** 10 — the cluster members (5 from papers + 5 minted here)
- **merged:** 28 (4a's 4 + 4b's 24)
- **dropped (stragglers):** 7
- **clusters:** 3
- **minted at 4b:** 5 `H` (3 constructed members `H-41/H-42/H-43`, 2 residuals `H-44/H-45`) + 3 `HC`
- total `H` files on disk: 45 (nothing deleted; ≥ 40)

## Cluster inventory (the top-level map)

1. **[[HC-1]] — Origin of SARS-CoV-2 (natural zoonosis vs research-related incident).** *The main question.* Members: **[[H-41]]** natural zoonotic spillover, no research · **[[H-42]]** research-related leak of an unmodified natural virus (zoonotic collection) · **[[H-43]]** research-related origin of a laboratory-manipulated virus (engineered lab leak) · **[[H-44]]** residual. All object-level empirical evidence (genome, geography, phylodynamics, institutional) attaches here.
2. **[[HC-2]] — Number of independent introductions of SARS-CoV-2 into humans.** Members: **[[H-5]]** two or more separate introductions · **[[H-16]]** a single introduction. `exhaustive_by_construction: true` (a count of 1 vs ≥2; no residual). `depends_on` HC-1.
3. **[[HC-3]] — Causal role of the Huanan Seafood Market.** Members: **[[H-14]]** primary wildlife-to-human spillover origin · **[[H-15]]** externally-seeded amplifier (infected people or cold-chain goods) · **[[H-19]]** detection/ascertainment artifact, not causally special · **[[H-45]]** residual. `depends_on` HC-1 and HC-2.

## Member composition (what each member absorbed)

- **H-41 (natural zoonosis, constructed):** H-4, H-12 (+H-13), H-28 (natural-origin verdicts); H-31, H-32, H-33, H-36, H-37, H-38 (natural-genome / natural-adaptation object-level claims).
- **H-42 (natural-virus lab leak, constructed):** H-3 (Rootclaim zoonotic-collection).
- **H-43 (engineered lab leak, constructed):** H-1, H-2, H-17, H-27 (engineered/lab verdicts); H-22, H-34 (+H-35), H-39, H-40 (engineering-mechanism claims).
- **H-5 (≥2 introductions):** absorbs H-6 (intermediate haplotypes did not genuinely circulate — a premise about the count, not a separate answer).
- **H-14 (market spillover origin):** 4a had absorbed H-21, H-24; 4b adds H-10 (agnostic epicenter — logical disjunction of the spillover/amplifier answers), H-23 (raccoon-dog intermediate host), H-25 (not pangolin/bat), H-26 (viable wildlife route).
- **H-15 (amplifier):** absorbs H-20 (cold-chain introduction — a second external seed route).

## Verdict / testimony resolution (trap 2)

The bottom-line conclusions were merged into the object-level origin member each asserts, never placed as co-members (that would double-count and break MECE): Rootclaim's four scenarios → H-1/H-2→H-43, H-3→H-42, H-4→H-41; Judge Eric H-12/H-13 → H-41; Andersen H-31 → H-41; Weissman synthesis H-17 → H-43; FBI/DOE H-27 → H-43; IC-plurality H-28 → H-41. Provenance is preserved in each survivor's `additional_sources`, and 53 arguments had their `affects_hypotheses` repointed from the absorbed nodes to the survivors (e.g. the IC-split argument A-75 now bears on both H-43 and H-41).

## Genome "engineered vs natural" is NOT a separate cluster (trap 1)

Carving H-31/32/33/34/36/37/38/39/40 as their own cluster would re-partition HC-1 (engineered ≈ H-43, natural ≈ H-41∪H-42) and double-count the genome evidence. Instead the engineered claims merged into H-43 and the natural ones into H-41; the genome observations (O-58…O-77, O-34…O-38) discriminate the engineered member from the natural members inside HC-1 at step 5. H-31/36/37/38 also support H-42 (shared natural genome); because step 5 scores each observation per-member, their bookkeeping home (H-41) does not deny H-42 that support.

## Cross-cluster dependence (`depends_on`)

- **HC-2 → HC-1:** two-or-more introductions essentially requires a repeatable zoonotic source (very unlikely under one leak), so it is strongly correlated with H-41; a single introduction is neutral. Kept separate (distinct phylodynamic evidence) rather than merged.
- **HC-3 → HC-1:** a primary wildlife spillover at the market (H-14) essentially entails natural zoonosis; the "artifact" answer (H-19) is the position associated with a non-market/research origin. Strong correlation, kept separate (distinct geospatial/environmental/wildlife evidence).
- **HC-3 → HC-2:** under zoonosis both inferred introductions are placed at the market, so H-14 co-varies with the ≥2-introductions answer; mediated by the shared zoonosis picture.

HC-1's `depends_on` is empty: it is the root question, and the reverse dependences are recorded on the dependent clusters per the brief.

## Stragglers dropped as "clusters nowhere" (traps 3 & 4)

Seven hypotheses assert no distinct MECE answer to any cluster's sub-question and were dropped as stragglers; each is on-topic base-rate / precedent / timing input whose evidential content lives in observations that attach to the clusters directly at step 5 (not off-topic):

- **H-18** — numeric prior/base-rate parameter for a research origin; feeds **step 7's origin prior**, not a member.
- **H-7** — cryptic-circulation timing (no substantial pre-December-2019 circulation); evidence O-6/O-7.
- **H-11** — early-transmission fact (H2H by mid-December 2019); evidence O-7/O-9/O-10.
- **H-8, H-9** — Dutch-mink host-competence / spillback precedent (a different host system); evidence O-11…O-15.
- **H-29, H-30** — SARS-civet market-amplification / host-role precedent (a different virus); evidence O-54…O-57.

## Deviations from the brief's illustrative carving

- **HC-3 members.** The brief illustrated "H-14 vs H-15 vs H-10 (unspecified epicenter)". H-10 is logically the disjunction of the spillover and amplifier answers, so it cannot be a mutually-exclusive co-member; it is merged into H-14. The genuine third answer is **H-19** (the market is a detection artifact — the lab-leak-side stance), which is promoted to a member, giving a cleaner MECE partition {spillover-origin, amplifier, artifact, residual}.
- **Extending 4a's merges (H-10, H-23, H-25, H-26 → H-14; H-20 → H-15).** 4a's note on H-14 had deliberately left H-23/H-10 unmerged on the dedup discriminability test (correct for dedup). For MECE clustering these are sub-claims of the wildlife-spillover answer, not separate answers; a standalone intermediate-host cluster would double-count the species-correlation evidence (O-40/O-50/O-51). They are therefore folded into H-14, and that evidence discriminates H-14 vs H-15 inside HC-3.
