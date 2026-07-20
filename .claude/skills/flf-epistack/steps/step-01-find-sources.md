# Step 1 — Find primary sources

You produce candidate primary **`source`s** (a wide pool for step 2 to curate down) — plus your own orientation note.

## Interface

Step 2 (curate) reads each source's frontmatter, body summary/relevance_note, and `url`, starting from the consolidated overview in `agent-notes/orientation/`; from its methods read it writes trust + usefulness scores, creates the shared `data-basis` (`D`) nodes and sets each source's `data_basis`, and flags the curated ~N subset. You own the descriptive fields; step 2 owns the scores and the data-basis links — leave them blank. Downstream, step 3 opens curated sources and extracts their observations, attributing each to the source's own data or an external basis; step 5 uses those bases to find correlated evidence.

## Spec

### Output

Per-type folders, one file per node: `sources/` (S). Plus one file that is *not* a graph node: your own orientation note in `agent-notes/orientation/`. (Node = markdown file with typed YAML frontmatter + prose body; `PREFIX-N` id; immutable filename `PREFIX-N - Title.md`; full-filename wikilinks — all per `../SKILL.md`.)

### Minting node files

Searchers write at the same time, so ids are never chosen by hand — a script assigns them under a lock, which is the only thing keeping parallel writers off the same `S-N`. Pipe the note's markdown (frontmatter + body, with `{{ID}}` wherever the bare id belongs, at minimum `id: {{ID}}`) to:

```
python3 .claude/skills/flf-epistack/scripts/create_node.py <analysis-dir> --type source --title "Descriptive title, no id"
```

It prints the assigned id and the path; use that filename for wikilinks. `--type` takes any node type of the pipeline. Your orientation note carries no id — write that one directly.

### Sizing

`curated_target_N` is a pipeline input — the size step 2 curates to. Survey a large candidate pool cheaply (meta-analyses and reviews let you weigh many at once), **read** primary sources for ~8×N, **write** `source` nodes for ~4×N. These are step-1 totals across all searchers, not your personal quota; your orchestrator gives you your share. Step 2 prunes to ~N, so err toward breadth over polish.

### `source` node — frontmatter

The pool is **primary sources only**: whatever actually made the measurement, ran the experiment, or holds the record. Reviews and meta-analyses are discovery hubs — mine them for the primaries they cite and note that under `found_via`; never give one its own `source` node.

| field                                | req      | meaning                                                                                                                                                                                                                                                                                                                                    |
| ------------------------------------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| type                                 | MUST     | `source`                                                                                                                                                                                                                                                                                                                                   |
| id                                   | MUST     | `S-N`                                                                                                                                                                                                                                                                                                                                      |
| source_type                          | MUST     | enum: journal-article, preprint, dataset, report, news, book, webpage, video, other                                                                                                                                                                                                                                                        |
| url                                  | MUST     | resolvable locator to the primary artifact (URL/DOI)                                                                                                                                                                                                                                                                                       |
| venue                                | MUST-key | journal/publisher/site; else `unknown`                                                                                                                                                                                                                                                                                                     |
| publication_date                     | MUST-key | ISO date or year; else `unknown`                                                                                                                                                                                                                                                                                                           |
| citation_count + citation_count_asof | MUST-key | integer + date read; else `unknown`                                                                                                                                                                                                                                                                                                        |
| field                                | MUST-key | domain (sets replication baselines in later steps); else `unknown`                                                                                                                                                                                                                                                                         |
| authors                              | SHOULD   | list (kept as its own field so author identity can be stripped when judging)                                                                                                                                                                                                                                                               |
| found_via                            | SHOULD   | how surfaced (query / review or meta-analysis mined / citation-chase)                                                                                                                                                                                                                                                                      |
| motivatedness                        | SHOULD   | known agenda / conflict of interest                                                                                                                                                                                                                                                                                                        |
| refuted / duplicate_of               | SHOULD   | flag+note / `[[S-N]]` — recorded, not deleted                                                                                                                                                                                                                                                                                              |

`MUST-key` = the key is present; give a value when reasonably obtainable, else the literal `unknown`. Body: a 2-5-sentence `summary` (MUST) and a one-line `relevance_note` (SHOULD — why it plausibly bears on the main question). No score fields, no `data_basis`, and no outgoing observation/hypothesis/argument links at step 1 (steps 2 and 3 add those).

#### Example

`sources/S-1 - Re-dated last-appearance ages for Sahul's extinct megafauna.md` — source_type journal-article; publication_date 2019; citation_count 120 (asof 2026-07-18); field Quaternary science; url \<doi\>; found_via review reference list. Body summary "Re-runs the youngest reliable ages for the 12 securely dated extinct genera against a published screening protocol."; relevance_note "direct primary re-measurement of the last-appearance ages the debate turns on."

### Your orientation note

Every agent in step 1 writes one file of its own in `agent-notes/orientation/` — the planner its plan, each searcher the slice it worked, the consolidator the merged overview step 2 starts from. Nobody edits anyone else's; that is what makes writing in parallel safe. Name yours after your slice (`megafauna-dating.md`, not `notes3.md`).

Yours covers your slice, and holds four things:

1. **Your sources**, each as a `[[wikilink]]`, grouped under rough **topic** headings — the sub-questions or lines of evidence your slice split into — and within each group ordered best-first by your rough quality×usefulness impression. That impression lives **only** as this ordering — do not write it as a number on any node; step 2 does the real scoring.
2. **`search_scope`** — what you actually searched: queries, indexes, reviews mined, chains followed.
3. **`exclusions`** — {what, why} for each item you dropped at ingestion (refuted, duplicate, out of scope), so a reader can tell a considered rejection from a gap.
4. ~1 paragraph on the slice: its size and shape, plus anything you went looking for and could not find.

#### Example

`agent-notes/orientation/megafauna-dating.md` — "~12 candidates, most re-analysing the same age compilation. **Dating the extinction window:** [[S-1 - …]], [[S-4 - …]]; **Human arrival and site overlap:** [[S-7 - …]], …" (each group best-first); search_scope "reviews of the extinction debate + their reference lists + keyword search on the age compilations"; exclusions [{preprint P, "superseded by its own published version"}].

### Checks (binary)

1. Every node file sits in `sources/`, has `type: source` and a unique `S-N` id matching its filename. No id repeats.
2. Every source has `source_type` (in enum), a resolving `url`, and a body `summary`; the keys venue / publication_date / citation_count(+asof) / field are each present (value or `unknown`).
3. No source carries a trust/usefulness score field, a `data_basis`, or an outgoing obs/hyp/arg link.
4. You wrote exactly one file in `agent-notes/orientation/`; it links every `source` you created (each ≥1×) under topic headings, and records your `search_scope` and `exclusions`.

## Process

1. **Work to the brief.** Take the question, the search slice, and the number of notes to write from the prompt your orchestrator gives you. Keep a running note of what you searched and what you dropped at ingestion (refuted, duplicate, out-of-scope) — it becomes your orientation note's `search_scope` and `exclusions`, and the method has to stay legible to a reader who wasn't there.
2. **Mint every node through the script** (see above), never by writing a file with a hand-picked id.
3. **Survey wide, then read deep.** Start from the cheap high-coverage sources — recent systematic reviews and meta-analyses — to map the debate and harvest their reference lists. Then snowball: **backward** (mine reference lists for earlier work) and **forward** ("cited by" / newer papers citing a key one), reiterating on each new find. Cross-check with a keyword database search; snowballing and database search each catch what the other misses. Useful indexes and tools: Google Scholar, Semantic Scholar, OpenAlex, PubMed (biomedical), arXiv/bioRxiv/medRxiv (preprints), and citation-graph explorers like Connected Papers / Research Rabbit / LitMaps.
4. **Get to the primary artifact.** A review is a discovery hub, not the node you want for a load-bearing claim: the graph must reach a primary source in ≤2 hops, so record the paper that actually made the measurement or holds the data, not the article that merely mentions it.
5. **Capture metadata on the page.** While the source is open, grab venue, date, citation count (+ date read), field, and any known motivatedness/COI. These are step 2's raw material; `unknown` is allowed, but a lazy `unknown` you could have filled costs a re-open. Record venue/citations/motivatedness as plain data — they enter the verdict only as a data-reliability signal much later, never as deference now.
