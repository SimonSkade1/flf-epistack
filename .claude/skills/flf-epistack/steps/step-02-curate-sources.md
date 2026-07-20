# Step 2 — Curate sources

Score every candidate `source` from step 1 for data-reliability (`trust_score`) and usefulness, then flag the ~N best as the *curated* subset that step 3 will read in depth. From the same methods read you also map each source's data provenance: create the shared `data-basis` (`D`) nodes and set each source's `data_basis`. No `source` is renumbered or deleted — you add fields and mint `D` nodes, and the sources that don't make the cut move aside with their scores intact as the exclusion record.

## Substeps

The step splits in two, because scoring is per-source work and the cut is not.

**2a — score + map data provenance** (several children in parallel). The orchestrator splits the pool by source id — roughly 10 sources each — and gives you your ids. Score **only** those, writing `trust_score`, `trust_reason`, `usefulness`, `usefulness_reason`, `method_read`, `standing` and `angle` onto each. From the same methods read, set each source's `data_basis` and mint the `data-basis` (`D`) nodes it needs (schema below). Slices are disjoint for source files, but two scorers blind to each other can mint duplicate `D` nodes for the same dataset — 2b reconciles those. You do **not** compute `combined_score`, set `curated`, or move anything: those need the whole pool in view.

**2b — reconcile + select** (one child, once every scorer has returned). First merge duplicate `D` nodes that parallel scorers minted for the same dataset (repointing every source's `data_basis` to the survivor), since step 5's correlation detection keys on shared `D`-node identity. Then run `curation_select.py`, decide the cut, write `combined_score` + `curated` + `curation_reason` on every source, move the non-curated aside, and write `agent-notes/curation.md`.

Both substeps read this file. Where a section says (2a) or (2b), it belongs to that substep only.

## Relevant context

Step 2 scores `source` nodes step 1 created — a pool ~4× the target size, all **primary** sources (reviews/meta-analyses were used to find them, not minted as nodes). Their step-1 frontmatter (2a reads these; the score fields 2a/2b add are in the Spec):

| field | meaning |
|---|---|
| type / id | `source` / `S-N` |
| source_type | enum: journal-article, preprint, dataset, report, news, book, webpage, video, other |
| url | the primary artifact — open it, the methodology read is the point |
| venue / publication_date / citation_count (+`_asof`) / field | each a value or `unknown` || motivatedness | known agenda / COI, if any |
| found_via | how it was surfaced |
| refuted / duplicate_of | flag / `[[S-N]]` it duplicates — recorded, not deleted |
| authors | list (kept separate so identity can be stripped when judging) |

Body: a 2-5-sentence `summary` + one-line `relevance_note`. Step 1's agents also wrote notes in `agent-notes/orientation/`; the consolidated overview there is **2b's** entry point for pool shape — a **2a** scorer works from the nodes themselves (its slice is a list of ids). Step 1 created no `data-basis` nodes — you create them here (schema below).

## Interface

You own the fields above (plus each source's `data_basis` and the `D` nodes); do not modify step 1's descriptive fields — one exception: 2a may refine `motivatedness` if the methodology read reveals an undocumented conflict of interest.

Hand-off to step 3: the curated subset = the `source` nodes with `curated: true` (equivalently, those left directly in `sources/`), a flag **2b** sets. Step 3 opens exactly these via `url`. Each source's `trust_score` travels with it — the paper observations step 3 creates **inherit `trust_score` as their data-reliability**, so a 2a scorer's number is what the later Bayesian steps rest on; get it calibrated rather than generous. Each source's `data_basis` travels too — step 3 reads it to attribute every observation to the source's own data or an external basis, so getting the bases right here is what lets step 5 detect correlated evidence. `motivatedness` travels too (its data-trust effect is already priced into `trust_score`; its separate effect on *which* arguments a source presents is handled downstream). Step 3 uses neither `usefulness` nor `combined_score` — those served only the cut here.

`trust_score` is the single sanctioned channel through which venue, citation and prestige enter the whole analysis, and only as *data-reliability*. No later step may reuse venue or author identity as evidence for the *truth* of a claim: the verdict has to stay derivable with author and venue stripped.

## Spec

### Fields you write on each source

| field | req | substep | meaning |
|---|---|---|---|
| trust_score | MUST | 2a | [0,1]; data-reliability (scale below). From how the work was done — never from whether you find its conclusion believable. |
| trust_reason | MUST | 2a | one line naming the signals that drove it |
| usefulness | MUST | 2a | float on a log scale, ~1-5; how much the data would move the question *if true* |
| usefulness_reason | MUST | 2a | one line |
| method_read | SHOULD | 2a | one line or a rough [0,1]: what the design and statistics themselves imply |
| standing | SHOULD | 2a | one line: venue, citations, and whether anyone has independently corroborated it |
| angle | SHOULD | 2a | short tag for the approach (e.g. "direct-dating", "climate-proxy") — the skew check groups on it, so use a small consistent vocabulary |
| data_basis | MUST | 2a | list of `[[D-N]]`/`[[S-N]]` the source's findings rest on (self-link `[[S-N]]` = own data; `[]` = pure theory/argument, rests on none). Mint or reuse `D` nodes as needed (schema below) |
| combined_score | MUST | 2b | ranking key = `usefulness × (trust_score − baseline)`, baseline default 0.8; ≤ 0 ⇒ not curated |
| curated | MUST | 2b | bool |
| curation_reason | MUST | 2b | one line; always name the reason when the call departs from rank order |

`method_read` and `standing` exist so the trust estimate reads as legible parts rather than one opaque number a skeptic can't argue with. `combined_score` is a cached derived value: if you change the baseline, re-run the script and rewrite every one of them, or they go stale.

### `data-basis` node — a shared dataset (2a)

Several sources' findings can rest on the same dataset, reporting actor, instrument, or analysis pipeline. Give each such thing one `D` node so that "these two findings share a basis" is captured as **node identity** rather than matching free text — that is how step 5 later detects correlated evidence, which must not be counted as independent.

| field | req | meaning |
|---|---|---|
| type | MUST | `data-basis` |
| id | MUST | `D-N` |
| basis_type | MUST | enum: dataset, actor, instrument, pipeline |
| url | MUST-key | locator if one exists; else `unknown` |

Body (SHOULD): a one-line `known_biases` — the failure mode that would move everything resting on this basis together.

Mint a `D` only for an unambiguous, well-identified thing that many papers predictably reuse: a named public dataset, a national statistics agency, a specific instrument or survey programme. A source's own data collection or a one-off is not a `D` — point `data_basis` at the source itself (`[[S-N]]`) or at the upstream source the data came from. A source that ran its own experiment *is* the shared basis for everyone who later reuses its data, so two sources pointing at the same `[[S-N]]` come out correlated exactly as if they shared a `D`. Reuse an existing `D`/`S` before minting a new one — and because parallel 2a scorers can't see each other's new `D` nodes, 2b reconciles duplicates for the same dataset.

### The anchor: score the data, not the paper

Both scores judge **the data and its analysis** — not the paper's conclusions, not its framing, not the authors' broader position. A well-run study whose conclusion you doubt still produced reliable data; a sloppy study whose conclusion you like did not. Two consequences worth holding onto:

- **Surprisingness never moves `trust_score`.** A result that cuts against your expectations is not thereby less reliable. There is a real Bayesian sense in which a surprising claim is more likely false, but that is priced downstream by the priors and likelihoods — letting it into trust as well would double-count the same intuition, and it is the standard route by which a pipeline quietly confirms what it already believed. Surprisingness belongs to `usefulness`, where it is a virtue.
- **A source's conclusions are not your business here.** Step 3 extracts what the paper found and step 6 assesses its arguments. Your job is how much weight the measurement can bear.

### trust_score ∈ [0,1]

The question to answer: *if I had never seen this result, what probability would I give that the key finding holds up under a clean, well-powered replication, with the effect size in the same ballpark?* That is more than "is it fabricated" — it prices how *cleanly* it replicates and how much room the method left for bias.

#### Signals, roughly in order of how much they should move you

1. **Independent corroboration.** A finding independently replicated or re-analysed by a group with no stake in it is the strongest signal available, and the only one that directly answers the question being asked.
2. **The study's own statistics.** How far the key result sits from the significance threshold; the effect size and its precision; sample size and power. These are the best predictors available from the paper alone.
3. **Design and transparency.** Preregistration; whether the design can actually support the claim made; selection and measurement bias; availability of data and code; conflicts of interest and funding.
4. **Venue and citations.** Cheap to read and genuinely informative about how much scrutiny the work has had and whether it cleared any bar at all — treat them as a floor, and as a strong negative signal when absent (an uncited preprint in no venue). Be careful using them as a *positive* driver: see the statistics below.

#### Calibration statistics

Numbers worth carrying, chosen because they are themselves well-replicated:

1. **Base rates are worse than intuition suggests.** In the Open Science Collaboration's 100-study psychology replication (2015), 97% of the original papers reported a significant result and 36% of the replications did; replication effect sizes averaged about half the originals (r ≈ .40 → .20). Expect regression toward smaller effects as the default, not the exception.
2. **Citations do not track reliability.** Papers that failed to replicate are cited *more* than those that replicated, and their citation rates barely dip after the failure is published (Serra-Garcia & Gneezy 2021). Citation count measures attention and interestingness. High-impact venues did not replicate detectably better in the major replication projects either. So: use venue and citations to rule work *in* as serious, not to push a score high.
3. **Preregistration is a large signal.** Registered Reports report positive results ~44% of the time against ~96% in the standard literature (Scheel et al. 2021) — the gap is publication and analytic flexibility, and a preregistered null is strong evidence the pipeline was honest.
4. **Power is usually low and this compounds.** Median statistical power in neuroscience was ~21% (Button et al. 2013), and comparable figures recur across fields. Low power lowers the odds the finding is real *and* inflates the published effect size, so an underpowered study reporting a large effect is doubly suspect.
5. **Distance from p = .05 carries real information.** Across the replication projects, originals with p < .001 replicated at roughly two to three times the rate of those with .01 < p < .05. A result that only just cleared the threshold is the single most common thing that later evaporates.
6. **This task is tractable.** Prediction markets and expert surveys forecast replication outcomes at roughly 70-75% accuracy across the psychology and economics projects, working from much the same information you have. A careful read of design and statistics genuinely carries signal — you are not guessing.

Do not let any one of these dominate. A confident score wants agreement across several: a well-powered preregistered study with a far-from-threshold effect, in a real venue, that someone else has since reproduced.

#### Hard rules

- **`unknown` caps the score.** If you can't assess the venue, the method, or the statistics, the score cannot be high, and `trust_reason` says which gap capped it.
- **No rounding to the ends.** Don't push confident sources to 1.0 or bury decent ones near 0. Ask whether you would actually take these odds that the finding holds under replication; leave the honest residual either way.
- **Pure-theory or argument sources** (no empirical finding) get the same question read as *would this calculation or argument survive careful expert scrutiny*; whether the world realised its premise is a usefulness/hypothesis matter. Such a score is curation-only — argument sources emit no observations, so nothing downstream inherits it.

### usefulness

How much the data would move the main question *if it is true* — a separate axis from whether it is true. Drivers: surprising beats expected; more dimensions and larger datasets beat fewer and smaller; results that separate the leading hypotheses beat narrow side-points. Judge on the object level and **ignore citation count** — it is a popularity signal, it already fed `standing`, and reusing it here double-counts.

The scale is **logarithmic**: usefulness `n` ≈ as valuable as **two** sources at `n−1` spanning *different* methodologies (not replications of each other). Float, and most sources land between 1 and 5 — use the decimals, the rungs are landmarks rather than buckets:

1. a small, unsurprising, single-dimension result on a side point.
2. one clean moderate-n result on a sub-question.
3. a well-powered multi-dimension study with clear bearing, or a moderately surprising result.
4. a large detailed dataset, or a surprising result that directly separates the leading hypotheses.
5. landmark: large, detailed, surprising, and on its own strongly discriminating.

### The cut (2b)

`combined_score = usefulness × (trust_score − baseline)`, baseline default **0.8**. Subtracting the baseline cuts everything below baseline trust (≤ 0 ⇒ not curated) and weights trust heavily, so the pipeline spends its effort on a few reliable sources rather than many shaky ones. Only the ordering matters, so the small absolute values are fine. Treat the baseline as a corpus-fit knob: if almost nothing clears 0.8 the corpus is weak — lower it and say so rather than curate nothing; if nearly everything clears it, raise it so it discriminates.

Run:

```
python3 .claude/skills/flf-epistack/scripts/curation_select.py <analysis-dir> --target-n <N> [--baseline 0.8]
```

It ranks every scored source, marks the prospective top-N, and reports how that cut is distributed across `field`, `angle` and `data_basis`, flagging any value holding more than 40% of the cut or shut out of it entirely, with the next-best swap candidates. It only reports — you make the call and apply it by hand, so the reasoning stays visible in `curation_reason`.

Then decide, in this order:

1. Anything with `combined_score ≤ 0`, `refuted`, or a `duplicate_of` is `curated: false`. No exceptions beyond point 3.
2. Take the top ~`curated_target_N` by rank (an orchestrator-set input, not a function of corpus size).
3. **Fix the skew.** Where the script flags over-representation, swap a marginal top-N source for the best candidate from an under-represented `angle`, `field` or `data_basis`. This matters most for `data_basis`: sources resting on the same dataset are not independent evidence, they rise and fall together, and a curated set that is secretly one dataset is how the later Bayesian steps manufacture false confidence. Trading a ranking point for genuine independence is usually right. On a contested question you may also include the single strongest source for an otherwise unrepresented position even if its `combined_score` ≤ 0 — representing a side is a coverage decision, and its unchanged low `trust_score` keeps discounting it downstream.
4. Log every departure from rank order in that node's `curation_reason`, and don't pad to N with near-duplicates — a short curated set beats a padded one.

Then set `curated` on every node, move each `curated: false` node into `sources/non-curated/` (curated ones stay in `sources/`), and write the note.

### agent-notes/curation.md

One plain file (not a node, and not at the analysis root): `initial_count`; `curated_target_N`; `curated_count`; `trust_baseline` (value used + one-line reason); `scoring_rubric` (1-2 lines: the two scales and the formula actually used); `rank_departures` (id + why, for every swap and every different-angle include); the script's ranking output, pasted; `generated` (date). The main question is not repeated here — it lives in `initial_prompt.md`.

### Checks (binary)

1. Every step-1 `source` node has `trust_score` ∈ [0,1], `usefulness` (float), `combined_score`, `curated` ∈ {true,false}, and non-empty `trust_reason` / `usefulness_reason` / `curation_reason`. `curation_select.py` reports no unscored sources.
2. Recomputing `usefulness × (trust_score − baseline)` with the note's baseline matches `combined_score` for every node, and every node with `combined_score ≤ 0` is `curated: false` (sole sanctioned exception: one logged unrepresented-position include).
3. Node count unchanged and no `id` renumbered vs step 1; every `curated: false` node sits in `sources/non-curated/`, every `curated: true` node in `sources/`; nothing deleted.
4. `curated_count` equals `curated_target_N`, or differs only by swaps and includes each logged in `curation_reason` and in `rank_departures`.
5. Spot-check 3 `trust_reason`s: each cites how the work was done, with no appeal to whether its conclusion is true or how surprising it is.
6. Every source flagged `refuted` or `duplicate_of` is `curated: false`.
7. The final cut carries no skew flag that isn't consciously accepted and explained in the note.
8. Every `data-basis` node has `type: data-basis`, a unique `D-N` matching its filename, `basis_type` in enum, and `url` present (value or `unknown`); every `data_basis` entry on a source resolves to an existing `D`/`S` (or is `[]`); every `D` node has ≥1 inbound `data_basis` link, and no two live `D` nodes represent the same dataset.

## Process

### 2a — scoring your slice

1. **Score against the rubric, never against your slice.** You see ~10 sources; someone else sees the next 10, and 2b ranks all of them together. Both scales are absolute — `trust_score` is a probability about a replication, `usefulness` is pinned to described rungs — so anchor on those definitions and never on "best of the ten I happen to hold". A slice-relative score silently corrupts the pool-wide ranking.
2. **Open the `url`.** The methodology read is the part that carries the signal; frontmatter alone gets you `standing` and nothing else. Skim for the key result's statistics, sample size and power, whether the design supports the claim, preregistration, data availability, and funding or conflicts. **While the methods are open, map the data provenance:** the paper's own experiment (self-link `[[S-N]]`), an external dataset/actor/instrument (link or mint its `D` node), or both — then write the source's `data_basis`, reusing an existing `D` before minting.
3. **Write the parts, then the number.** Put what the design and statistics imply in `method_read` and the venue/citation/corroboration picture in `standing`, then set `trust_score` as your integration of the two. Recording the parts is what lets a later reader disagree with the specific step you got wrong rather than the whole number.
4. **Then usefulness, on the object level.** How many independent dimensions does the data have, how surprising is the result, does it separate the leading hypotheses or decorate a side point? The log scale means one landmark dataset can rightly outweigh a pile of small confirmatory studies.
5. **Keep every reason to one line**, and where a call is genuinely uncertain prefer an honest mid-range score with a stated gap to false precision.

### 2b — making the cut

6. **Sanity-check comparability first.** Read the consolidated overview in `agent-notes/orientation/`, then look across slices before ranking: if one scorer's numbers sit systematically high or low, or their `angle` tags don't share a vocabulary, fix that before the ranking inherits it. Rescore the outliers yourself rather than ranking incomparable numbers.
7. **Reconcile duplicate `D` nodes, then run the script and judge the set.** First merge any `data-basis` nodes that parallel 2a scorers minted for the same dataset — survivor = lowest id, repoint every source's `data_basis` to it — so the skew report and step 5 both see one identity per dataset. Then run the script: the ranking is arithmetic and the skew report is the part that needs you: spend swaps on independent methods and datasets, set the baseline to fit the corpus, and accept a flagged skew only where you can say in the note why it is the right pool anyway.
8. **Failure modes:** deferring to prestige instead of reading the method; letting agreement with a claim, or surprise at it, leak into trust; double-counting citation count into both axes; and a curated set that is a methodological monoculture. Let the scores carry the ranking and the note carry the departures.
