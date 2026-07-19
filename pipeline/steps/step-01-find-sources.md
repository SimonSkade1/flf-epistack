# Step 1 — Find primary sources

**Model:** opus, parallelising search over sonnet subagents.

Step 1 seeds the graph. You produce three node types — candidate primary **`source`s** (a wide pool for step 2 to curate down), the fallible **`data-basis`** things those sources rest on, and firmly-established background **`observation`s** — plus two plain orientation files. No trust/usefulness scores and no hypothesis, argument, or evidence-link structure yet; later steps add those.

## Spec

### Output

Per-type folders, one file per node: `sources/` (S), `data-bases/` (D), `observations/` (O). Plus two plain files at the analysis root that are *not* graph nodes: `manifest.md` and `orientation.md`. (Node = markdown file with typed YAML frontmatter + prose body; `PREFIX-N` id; immutable filename `PREFIX-N - Title.md`; full-filename wikilinks — all per `../SKILL.md`.)

### Sizing

`curated_target_N` is a pipeline input — the size step 2 curates to. Survey a large candidate pool cheaply (meta-analyses and reviews let you weigh many at once), **read** primary sources for ~8×N, **write** `source` nodes for ~4×N. Step 2 prunes to ~N, so err toward breadth over polish here.

### `source` node — frontmatter

| field | req | meaning |
|---|---|---|
| type | MUST | `source` |
| id | MUST | `S-N` |
| source_type | MUST | enum: journal-article, preprint, meta-analysis, dataset, report, news, book, webpage, video, other |
| url | MUST | resolvable locator to the primary artifact (URL/DOI) |
| data_basis | MUST-key | list of `[[D-N]]`/`[[S-N]]` for the fallible dataset(s)/actor(s)/instrument(s) this source's findings rest on. Self-link `[[S-N]]` = collected its own data; `[]` = rests on none (pure theory/argument); `unknown` = undetermined. Step 1 may leave `unknown`; step 3 resolves it for curated sources |
| venue | MUST-key | journal/publisher/site; else `unknown` |
| publication_date | MUST-key | ISO date or year; else `unknown` |
| citation_count + citation_count_asof | MUST-key | integer + date read; else `unknown` |
| field | MUST-key | domain (sets replication baselines in later steps); else `unknown` |
| authors | SHOULD | list (kept as its own field so author identity can be stripped when judging) |
| found_via | SHOULD | how surfaced (query / meta-analysis / citation-chase) |
| motivatedness | SHOULD | known agenda / conflict of interest |
| refuted / duplicate_of | SHOULD | flag+note / `[[S-N]]` — recorded, not deleted |

`MUST-key` = the key is present; give a value when reasonably obtainable, else the literal `unknown`. Body: a 1–3-sentence `summary` (MUST) and a one-line `relevance_note` (SHOULD — why it plausibly bears on the main question). No score fields and no outgoing observation/hypothesis/argument links at step 1 (steps 2 and 3 add those).

### `data-basis` node — a shared fallible thing

Several sources' findings can rest on the same dataset, reporting actor, instrument, or analysis pipeline. Give each such thing one `D` node so that "these two findings share a basis" is captured as **node identity**, not matching free text — that is how step 5 later detects correlated evidence, which must not be counted as independent (criterion 3).

| field | req | meaning |
|---|---|---|
| type | MUST | `data-basis` |
| id | MUST | `D-N` |
| basis_type | MUST | enum: dataset, actor, instrument, pipeline |
| url | MUST-key | locator if one exists; else `unknown` |

Body (SHOULD): a one-line `known_biases` — the failure mode that would move everything resting on this basis together. Mint rule: *is this a citable artifact you could extract observations from?* Yes → it is an `S`; no → a `D`. So a `data_basis` entry may point at either. Reuse an existing `D`/`S` before minting a new one.

### `observation` node — background fact

| field | req | meaning |
|---|---|---|
| type | MUST | `observation` |
| id | MUST | `O-N` |
| statement | MUST | one sentence; clearly-true / firmly-established |
| general | MUST | `true` (marks a step-1 background obs; step-3 paper observations leave it absent/false) |
| verification | MUST | how known: `firmly-established` / `common-knowledge`, or a note |
| source_check | MUST-if-uncertain | locator to a trustworthy source; required when not fully certain |
| source | SHOULD | at most one `[[S-N]]` if a source was consulted (may be absent — a background fact need not rest on one) |

Only firmly-established, uncontested facts belong here, and only when they help orient the reader; be sparing. Anything contested or uncertain is a **hypothesis**, entered in step 3 — not an observation. This folder may be empty if no background facts are needed. (`source` is singular throughout the pipeline; only later merge-survivors carry extra provenance.)

### `manifest.md` and `orientation.md`

`manifest.md` (plain file): `main_question` **verbatim** — the whole run turns on this string, written once, here — plus `search_scope` (one line: what was searched), `exclusions` (list of {what, why} for items dropped at ingestion: refuted, duplicate, out-of-scope), and `generated` (date).

`orientation.md` (plain file) orients the step-2 curator: ~1 paragraph on the pool (size, shape, notable gaps), then every `source` as a `[[wikilink]]`, grouped under `source_type` headings and, within each group, ordered best-first by your rough quality×usefulness impression. That impression lives **only** as this ordering — do not write it as a number on any node; step 2 does the real scoring.

### Micro-example

Main question: "What drove the extinction of Sahul's megafauna around 45–40 ka?"
- `S-1` — `sources/S-1 - Re-dated last-appearance ages for Sahul's extinct megafauna.md`; source_type journal-article; publication_date 2019; citation_count 120 (asof 2026-07-18); field Quaternary science; url \<doi\>; data_basis `[[D-4 - Continental late-Quaternary age compilation, group R]]` (ages drawn from group R's compilation, not collected fresh); found_via review reference list. Body summary "Re-runs the youngest reliable ages for the 12 securely dated extinct genera against a published screening protocol."; relevance_note "direct primary re-measurement of the last-appearance ages the debate turns on."
- `D-4` — `data-bases/D-4 - Continental late-Quaternary age compilation, group R.md`; basis_type dataset; url \<repository\>. Body known_biases "screening and site selection are group R's; everything resting on it moves together if the screen is systematically too permissive or too strict."
- `O-1` — `observations/O-1 - Radiocarbon ages beyond ~40 ka sit at the practical limit of the method.md`; statement "Radiocarbon ages beyond ~40 ka sit at the practical limit of the method and require luminescence or U-series cross-dating."; general true; verification firmly-established; source_check \<methods-review URL\>.
- `manifest.md` — main_question "What drove the extinction of Sahul's megafauna around 45–40 ka?"; search_scope "reviews of the extinction debate + their reference lists + keyword search on the age compilations"; exclusions [{preprint P, "venue below bar"}].
- `orientation.md` — "~30 candidates, thin on independent datasets — most re-analyse the same compilation. **meta-analysis:** [[S-14 - …]], [[S-5 - …]]; **journal-article:** [[S-1 - …]], [[S-4 - …]], …" (each group best-first).

### Checks (binary)

1. Every node file sits in its type folder, has a `type` in {source, observation, data-basis} and a unique `PREFIX-N` id matching its filename. No id repeats.
2. Every source has `source_type` (in enum), a resolving `url`, and a body `summary`; the keys venue / publication_date / citation_count(+asof) / field / data_basis are each present (value or `unknown`).
3. No source carries a trust/usefulness score field or an outgoing obs/hyp/arg link.
4. Every observation has `general: true`, a one-sentence `statement`, and `verification`; if `verification` is not firmly-established/common-knowledge, `source_check` is present; spot-check that none is a contested/uncertain claim.
5. `manifest.md` exists with non-empty `main_question` and `search_scope`.
6. `orientation.md` exists and links every `source` node (each ≥1×), grouped under `source_type` headings.
7. Every `data-basis` node has `type: data-basis`, a unique `D-N` matching its filename, `basis_type` in enum, and `url` present (value or `unknown`); every `data_basis` entry on a source resolves to an existing `D`/`S` (or is `[]`/`unknown`); every `D` node has ≥1 inbound `data_basis` link.

### Interface

Step 2 (curate) reads each source's frontmatter, body summary/relevance_note, and `url`, starting from `orientation.md`; it writes trust + usefulness scores onto the same node (keyed by id, never renumbering) and flags the curated ~N subset. You own the descriptive fields; step 2 owns the scores — leave them blank. Downstream, step 3 opens curated sources, extracts their paper observations, populates each source's outgoing links, and resolves any `data_basis: unknown`; step 5 uses each observation's `data_basis` to find correlated evidence — so that detection is only as good as the `D`/`S` bases you identify now.

## Process

1. **Anchor on the question.** Write `main_question` verbatim first and keep it in view — every later step reads that string, and a pool built against a fuzzy question wastes step 2's budget. Record `search_scope` and `exclusions` as you go, so the method stays legible (criterion 8) and step 2 knows what was and wasn't looked at.
2. **Survey wide, then read deep.** Start from the cheap high-coverage sources — recent systematic reviews and meta-analyses — to map the debate and harvest their reference lists. Then snowball: **backward** (mine reference lists for earlier work) and **forward** ("cited by" / newer papers citing a key one), reiterating on each new find. Cross-check with a keyword database search; snowballing and database search each catch what the other misses. Useful indexes and tools: Google Scholar, Semantic Scholar, OpenAlex, PubMed (biomedical), arXiv/bioRxiv/medRxiv (preprints), and citation-graph explorers like Connected Papers / Research Rabbit / LitMaps.
3. **Get to the primary artifact.** A review is a discovery hub, not the node you want for a load-bearing claim: the graph must reach a primary source in ≤2 hops (criterion 5), so record the paper that actually made the measurement or holds the data, not the article that merely mentions it. (A review can still be its own `S` when you will use its synthesis directly.)
4. **Build for independence and balance — the main quality lever.** Forty sources that all re-analyse one dataset are nearly one source. Deliberately seek sources resting on *genuinely independent* data bases, and sources on every side of the contested question; a lopsided or secretly-correlated pool is the failure this whole machinery exists to prevent (criterion 3). Note the pool's gaps honestly in `orientation.md` (criterion 16).
5. **Mint data-basis nodes as you read.** For each source ask "what fallible thing do its findings rest on?" and link or create the `D` (or `S`) for it, reusing existing ones so a shared basis is a single identity. This is cheap now and load-bearing later — step 5 can only spot correlated evidence through the bases you record.
6. **Capture metadata on the page.** While the source is open, grab venue, date, citation count (+ date read), field, and any known motivatedness/COI. These are step 2's raw material; `unknown` is allowed, but a lazy `unknown` you could have filled costs a re-open. Record venue/citations/motivatedness as plain data — they enter the verdict only as a data-reliability signal much later (criterion 15), never as deference now.
7. **Be sparing with background observations.** Add a general `observation` only for a firmly-established, uncontested fact that genuinely orients the reader. If it is arguable, it is a hypothesis for step 3, not an observation.
8. **Don't score, and don't gold-plate.** Hold quality only as the best-first ordering in `orientation.md`. Read ~8×N, write ~4×N, then stop — polishing sources step 2 will cut is wasted effort.
9. **Parallelise with subagents.** Fan search out to sonnet subagents — one per sub-topic, side of the debate, or search thread — each returning candidates with metadata and a short relevance note. Keep id assignment and file-writing coordinated (hand subagents disjoint id ranges, or have them return drafts you write) so parallel writers don't collide on `S-N`/`D-N` numbers, and dedupe by `url`/DOI as you fold results in.
