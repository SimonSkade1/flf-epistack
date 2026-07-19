# Step 2 — Curate sources

**Mode of the flf-epistack skill.** Score every candidate `source` from step 1 for data-reliability (`trust_score`) and usefulness, then flag the ~N best as the *curated* subset that step 3 will read in depth. You create no nodes and delete nothing — you add score fields and move the non-curated sources aside.

Model: opus.

## Spec

**What step 1 left you.** A pool of candidate `source` nodes in `sources/` (roughly 5× the target curated size). You read, per source: `source_type` (enum: journal-article, preprint, meta-analysis, dataset, report, news, book, webpage, video, other); `url` (opens the primary artifact — open it for the methodology read); `venue`, `publication_date`, `citation_count` (+`citation_count_asof`), `field` (the domain, which sets a replication baseline) — each a value or `unknown`; `motivatedness` (a known agenda/COI note, if any); `refuted` / `duplicate_of` (flags step 1 recorded; `duplicate_of` points at the `[[S-N]]` it duplicates); `found_via`; `data_basis` (the dataset/actor/instrument the findings rest on, possibly `unknown`); and the body's `summary` (1-3 sentences) + `relevance_note` (one line). Start from `orientation.md`, a plain-file overview grouping the sources by `source_type`, each group ordered best-first by the finder's rough impression. Background `observation` and `data-basis` nodes also exist; step 2 does not touch them.

**Your output.** (a) Add the score fields below to every `source` node; (b) move each node you mark `curated: false` into a `sources/non-curated/` sub-folder (curated ones stay in `sources/`); (c) write one plain `curation-manifest.md`. No node is created, renumbered, or deleted. The curated set is thus a flagged subset, and the non-curated nodes keep their scores as the exclusion log.

### Fields you write on each source

| field | req | meaning |
|---|---|---|
| trust_score | MUST | [0,1]; data-reliability (scale below). From source features only — never from whether you agree with the source's claims (criterion 4). |
| trust_reason | MUST | one line, citing the features used (venue, date, citations, field baseline, replication, methodology) |
| usefulness | MUST | float on a log scale, ~1-5; how much the data would move the question *if true* (scale below) |
| usefulness_reason | MUST | one line |
| combined_score | MUST | ranking key = `usefulness × (trust_score − baseline)`, baseline default 0.8; ≤ 0 ⇒ not curated |
| curated | MUST | bool |
| curation_reason | MUST | one line for the in/out call; name the justification whenever it departs from combined_score rank (different-angle include, refuted, baseline change) |
| angle | SHOULD | short tag for the source's approach/perspective (e.g. "direct-dating", "climate-proxy") — supports the diversity leeway below |
| replication_baseline / looks_good_adj | SHOULD | the two named factors trust_score decomposes into — a field/venue/date/citation baseline × a methodology adjustment from your read — so the estimate stays as legible parts, not one opaque number (criterion 7) |

### Scales

**trust_score ∈ [0,1]** — answer one question: *if I hadn't seen the data, what probability would I assign that the key finding holds up under a clean, well-powered replication, with the effect size in the same ballpark?* This covers more than "is it fabricated / will it replicate at all" — it also prices how *cleanly* it replicates and whether the method left room for bias. Judge from source features only; any `unknown` feature caps the score (say which, in trust_reason). Rough guide: 0.9+ replicated result / meta-analysis / strong venue + sound method; ~0.6 single decent study, not yet replicated; <0.5 preprint / weak venue / small-n / visible method concerns.

**usefulness** — how much the data would move the main question *if it is true* (a separate axis from whether it's true). Drivers: surprising > expected; more detail (many dimensions) and larger datasets > less; results bearing directly on the main question and separating the leading hypotheses > narrow side-points. Judge on the object level — **not** from citation counts. The scale is **logarithmic**: usefulness `n` ≈ as valuable as **two** sources at `n−1` spanning *different* methodologies (not replications of each other). Float; most sources land in 1-5:
1. small, unsurprising, single-dimension result on a side point.
2. one clean moderate-n result confirming an expected effect on a sub-question.
3. well-powered multi-dimension study with clear bearing, or a moderately surprising result.
4. large detailed (many-dimension) dataset, or a surprising result that directly separates the leading hypotheses.
5. landmark: large + detailed + surprising + on its own strongly discriminates the main hypotheses.

**combined_score = usefulness × (trust_score − baseline)**, baseline default **0.8**. Subtracting the baseline deliberately cuts everything below baseline trust (≤ 0 ⇒ not curated) and weights trust heavily, so the pipeline spends its effort on a few reliable sources rather than many shaky ones. Only the ordering matters (it is a ranking key), so the small absolute values are fine. You MAY raise or lower 0.8 if it doesn't fit the corpus (most often: lower it when too few sources clear it); record the value used + a one-line reason in the manifest.

### Curation decision

Score every node. Anything with combined_score ≤ 0 (trust below baseline) is `curated: false`. Rank the rest by combined_score and take the top ~`curated_target_N` — a pipeline input parameter set by the orchestrator (step 1 aimed at ~5× it), not a function of corpus size. Then apply leeway: you MAY swap in lower-ranked sources covering a materially different `angle`, since a spread of methods gives a fuller, less-correlated picture — no hard cap, use judgment, and log each such include in its curation_reason. Sources flagged `refuted` or `duplicate_of` are always `curated: false`.

### curation-manifest.md

One plain file (not a node): `main_question`; `initial_count`; `curated_target_N`; `curated_count`; `trust_baseline` (value used + one-line reason); `scoring_rubric` (1-2 lines: the trust + usefulness scales + the combined-score formula actually used); `different_angle_includes` (list of `id` + why); `generated` (date).

### Micro-example

Main question: "What drove the extinction of Sahul's megafauna around 45-40 ka?"
- `S-1` — trust_score 0.9; trust_reason "strong venue, ages independently re-run by a second lab, screening protocol published → high P finding holds under replication"; usefulness 4; usefulness_reason "large multi-taxon age compilation that directly separates the leading drivers"; combined_score 0.4 (= 4 × (0.9 − 0.8)); curated true; curation_reason "top combined_score"; angle "direct-dating". Stays in `sources/`.
- `S-2` — trust_score 0.6; trust_reason "single site, small n, no independent re-dating, known contamination risk at that depth"; usefulness 3; combined_score −0.6 (= 3 × (0.6 − 0.8)); curated false; curation_reason "trust below 0.8 baseline". Moves to `sources/non-curated/`.
- `curation-manifest.md` — initial_count 40; curated_target_N 8; curated_count 9 (one different-angle include `S-14`, a review that adjudicates the debate rather than dating anything itself); trust_baseline "0.8 (default; enough sources clear it)"; scoring_rubric "trust = P(key finding holds under clean replication); usefulness = log-scale data-value-if-true; combined = usefulness × (trust − 0.8)".

### Checks (binary)

1. Every step-1 `source` node now has trust_score ∈ [0,1], usefulness (float), combined_score, curated ∈ {true,false}, and non-empty trust_reason / usefulness_reason / curation_reason.
2. Recomputing `usefulness × (trust_score − baseline)` with the manifest's baseline matches combined_score for every node, and every node with combined_score ≤ 0 has `curated: false`.
3. Node count unchanged and no `id` renumbered vs step 1; every `curated: false` node sits in `sources/non-curated/`, every `curated: true` node in `sources/`; nothing deleted.
4. `curated_count` equals `curated_target_N`, or exceeds it only by different-angle includes each logged in curation_reason; manifest records initial_count / curated_target_N / curated_count / trust_baseline(+reason).
5. Spot-check 3 trust_reasons: each cites source features only, with no appeal to whether the source's claims are true (criterion 4).
6. Every step-1 source flagged `refuted` or `duplicate_of` has `curated: false`.

### Interface to neighbouring steps

You own the fields above; do not modify step 1's descriptive fields — one exception: you MAY refine `motivatedness` if the methodology read reveals an undocumented conflict of interest.

Hand-off to step 3: the curated subset = the `source` nodes with `curated: true` (equivalently, those left directly in `sources/`). Step 3 opens exactly these via `url` and extracts their content. Each source's `trust_score` travels with it — the paper observations step 3 creates **inherit trust_score as their data-reliability**, so your score is what the later Bayesian steps rest on; get it calibrated. `motivatedness` travels too (its data-trust effect is already priced into trust_score; its separate effect on *which* arguments a source presents is handled downstream). Step 3 does not use usefulness or combined_score — those only served the cut here.

trust_score is the single sanctioned channel through which venue / citation / prestige enters the whole analysis, and only as *data-reliability* (criterion 15). No later step may reuse venue or author identity as evidence for the *truth* of a claim; the verdict must stay derivable with author and venue stripped.

## Process

1. **One pass, variables before values.** Read `orientation.md` for the shape and gaps of the pool, then go source by source. For each, hold trust as a decomposition — a field/venue baseline × a methodology adjustment — and fix the actual numbers in a final sweep across the whole corpus, so scores stay comparable (a ranking is only as good as its consistency).

2. **trust_score — start from a field base rate, then read the method.** Replication rates differ sharply by field; rough anchors from replication projects: experimental economics ~60%, social sciences ~50% overall, psychology ~35-40%, cancer/preclinical biology ~25-40%. Use the base rate for *this* source's field, not a generic one — a single unreplicated study in a low-replication field starts well below 0.6 however prestigious the venue. Then do the "looks-good read": open the `url` and skim the methods for sample size / statistical power, whether the design fits the claim, selection bias, preregistration, independent replication or re-analysis, data availability, and funding / conflicts of interest. Adjust up for clean, powerful, replicated methods; down for small-n, post-hoc, or COI-shaped results. Meta-analyses and independently replicated findings sit highest; lone small preprints lowest. If you genuinely can't assess venue or method (an `unknown`), that caps the score and you say so.

3. **Keep trust about the data, not the claim (criterion 4).** The score must not move because a finding strikes you as plausible or congenial. A well-run study whose conclusion you doubt is still reliable *data*; a sloppy study you happen to agree with is not. And weigh the bet honestly (criterion 2): would you actually take these odds that the finding holds under replication? Don't round confident sources to 1.0 or bury a decent study near 0 — leave the honest residual.

4. **usefulness — object-level value if true, blind to trust and citations.** Ask how many independent dimensions the data has, how surprising the result is, and whether it discriminates the leading hypotheses or merely decorates a side-point. Ignore citation count here: it is a popularity signal, not an information signal, and it already fed trust — reusing it would double-count. The log scale means one landmark dataset can rightly outweigh a pile of small confirmatory studies.

5. **The cut — judge the set, not just each source (criterion 3).** Rank by combined_score and take ~N, then step back: if the top N all rest on the same dataset or one method, they are correlated — they rise and fall together, and downstream that manufactures false confidence. Spend the different-angle leeway to bring in independent methods/data even at some cost in individual score; diversity of data-basis is worth more than a marginal ranking point. Don't pad to N with near-duplicates. And treat the baseline as a corpus-fit knob: if almost nothing clears 0.8 the corpus is weak — lower it and note why rather than curate nothing; if nearly everything clears it, raise it so it discriminates.

6. **Failure modes to avoid:** deferring to prestige instead of reading the method (criterion 15); letting agreement-with-the-claim leak into trust (criterion 4); double-counting citation count into both axes; and a curated set that is a methodological monoculture (criterion 3). Keep every reason to one line and let the scores, not prose, carry the ranking; where a call is genuinely uncertain, an honest mid-range score with a one-line reason beats false precision.
