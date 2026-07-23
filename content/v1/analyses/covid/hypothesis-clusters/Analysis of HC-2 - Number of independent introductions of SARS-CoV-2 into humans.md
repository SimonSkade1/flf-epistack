---
type: cluster-review
cluster: "[[HC-2 - Number of independent introductions of SARS-CoV-2 into humans]]"
---

#### What the analysis says

The cluster asks whether the two co-circulating early lineages A and B were seeded by one introduction of SARS-CoV-2 into humans or by two or more. Its two members are the exhaustive cases of that count: [[H-5 - Early A-B diversity reflects two or more separate zoonotic introductions, not one]] (two-or-more) and [[H-16 - SARS-CoV-2 early lineages A and B are better explained by a single introduction than by two]] (single). There is no residual — a count given a human epidemic is either one or two-or-more.

The prior is **[0.29, 0.71]**, favouring a single introduction (~71%): an outside-view base rate over how novel human-establishing emergences are seeded, with >=2 treated as the real-but-minority case, anchored largely on SARS-CoV-1's documented multiple civet-to-human introductions and nudged up by [[A-5 - Both lineages spread without within-human adaptation, implying a pre-adapted animal reservoir]].

The posterior is **[0.2644, 0.7356]** — it barely moves, landing ~74% single, because the two evidence blocks nearly cancel. [[CG-5 - HC-2 joint over O-4+O-5+O-6]] scores Pekar's phylodynamic pattern (two-lineage/two-mutation topology, no genuine circulating intermediate, two separately dated primaries) as ~2.2x more expected under two introductions (likelihood 1.0 vs 0.45) — but deliberately shrunk from the headline, because [[A-3 - Single introduction almost never reproduces the two-lineage two-mutation topology, favoring two or more introductions]] was **corrected**: the 2024 erratum cut Pekar's Bayes factor from ~60 to ~4.3, leaving only a weak, sign-contested residual. Opposing it, [[CG-6 - HC-2 joint over O-21+O-22]] scores Weissman's asymmetric-conditioning critique as ~4x favouring a single introduction (0.25 vs 1.0), per [[A-35 - Correcting Pekar 2022 asymmetric conditionalization reverses its Bayes factor to at least 4.4 favouring a single introduction]] (also **corrected**: reversal direction robust, magnitude order-4). Both blocks are capped at trust 0.5, so the prior does most of the work.

#### What the model may not capture

The bearing on the origin question is subtler than this cluster's citation history suggests (the synthesis itself is step 10's). Per the cluster's own `depends_on`, ">=2 introductions" is strong evidence *for* zoonosis — two natural spillovers are natural and near-impossible under a one-off lab leak — while "single introduction" is the null, consistent with either origin (a single zoonotic spillover is the default). Because the analysis found the two-introduction claim weak and let the prior dominate, **this cluster does not deliver the strong pro-zoonosis signal it is often cited for**; equally, its ~74%-single posterior does not favour a lab leak. The cluster mostly withholds a signal rather than supplying one.

Structurally the members are genuinely exhaustive, so the "is the answer on the list" risk is not a missing member but a shared-model failure: both members are scored off one possibly-misspecified simulation framework (the cluster's own analysis-failure note concedes this). "Two-or-more" also lumps 2 with Pekar's estimated ~8 spillovers-most-extinct; the topology identifies *establishing* introductions, and whether that is the quantity the prior prices is not airtight. The >=2 arm rests on essentially one analog (SARS-CoV-1) — my estimate: a reference class of size ~1, thin for a 0.45 conditional.

#### What would help

1. An independent, **non-Pekar** phylodynamic reconstruction of the count on fresh sequence data — the single most decisive input, since it would break the one-dataset dependence. McCowan's "new balanced-framework simulations" (referenced via Weissman as reaching the same reversal by a different route) are the nearest thing but are *exists, unread* — not ingested as their own source node, and not independent of Weissman given a shared anti-Pekar stake. A genuinely independent reconstruction: *does not exist*.
2. A neutral-statistician adjudication of whether Pekar's I1/I2 conditioning is genuinely asymmetric (Stansifer disputes A-35's premise) — *does not exist*.
3. Read-level coverage/lab data behind the 20 intermediate genomes ([[O-5 - The 20 apparent A-B intermediate genomes are low-coverage and lab-clustered]]), to test whether all are artifacts or some genuine-but-unsampled — *exists, inaccessible*.

#### Confusions and contradictions

The cluster is a genuine standoff on **one shared dataset**. Both CG-5 and CG-6 rest on Pekar's S-1 analysis — the same topology read two ways: as the classic >=2-introduction signature, and (after imposing symmetric conditioning) as ~4x evidence for one. This is an irreducible methodological dispute — two competent reanalyses of a single analysis pointing opposite directions, with the corrected Bayes factor contested in *sign*, not merely magnitude. The runner composes the two blocks as if they were two witnesses updating a common prior; the shared-basis flags and the 0.5 trust caps acknowledge the non-independence, but the arithmetic still treats them as separable. Shipped unfixed, honestly so: from within these sources I cannot tell which reading is correct, and the near-cancellation is as much an artifact of two disputants of equal assigned trust as a real informational wash.

#### External consensus

The version of record still favours two introductions — Pekar et al. 2022 (S-1, 187 cites) remains the mainstream phylodynamic position, and the Weissman/McCowan reversal is heterodox (Econ Journal Watch, 0 cites; un-refereed arXiv companion). At ~74% single the analysis lands *against* the current mainstream — a deliberate, traceable consequence of taking the erratum and the conditioning critique at face value while discounting Pekar's headline. Whether that is seeing something the field has been slow to correct or over-weighting a motivated minority is the open question the trust caps encode rather than resolve.
