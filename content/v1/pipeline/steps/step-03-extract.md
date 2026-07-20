---
title: "Step 3 — Extract observations, hypotheses, and arguments from a paper"
---

# Step 3 — Extract observations, hypotheses, and arguments from a paper

Step 3 fills in the paper-derived body of the graph. You are one child in a parallel fan-out; your slice is ~5 curated sources. Read each of your papers end-to-end, one at a time, and extract that paper's `observation` / `hypothesis` / `argument` nodes (each resting on exactly that one source), then write an ordered `extracted` link list back onto the source node. No scoring, no cross-paper merging, no clustering, no observation↔hypothesis edges — those are later steps (4-8).

## Relevant context

You extract from `source` (`S`) nodes — created in step 1, scored and curated in step 2. The fields you read (you never rewrite a step 1/2 field):

| field | set by | meaning |
|---|---|---|
| type / id | step 1 | `source` / `S-N` |
| url | step 1 | open this to read the paper |
| source_type | step 1 | enum (journal-article, preprint, dataset, …) |
| data_basis | step 2 | `[[D-N]]`/`[[S-N]]` the source's findings rest on; you read it and attribute each observation to the relevant subset |
| motivatedness | step 1 | known agenda / COI — travels to your nodes via `source` |
| trust_score | step 2 | [0,1] data-reliability; your `O`/`H`/`A` inherit it through `source`, never copied onto them |

You ignore `usefulness` / `combined_score` (they served only the curation cut).

## Interface

**Consumes (from step 2):** the `curated: true` source nodes (equivalently, those left directly in `sources/`), opened via their `url`; you process the ~5 in your slice. Each node inherits its source's `trust_score` as data-reliability through the `source` link (never copied); `motivatedness` (a source's known agenda / COI) travels the same link — its data-trust effect is already priced into `trust_score`, its argument-selection effect is handled at steps 5-6. Ignore `usefulness` / `combined_score`.

**Produces for step 4** (cluster hypotheses): the single-source `H` nodes. Step 4 reads `statement` (+ `question`) to drop irrelevant hypotheses, merge near-duplicates across papers, and group them into mutually-exclusive clusters.

**Produces for step 5** (link evidence): the `O` nodes, each with its data provenance attributed (the exact data it rests on — own experiment, external basis, or both — drawn from the source's step-2 `data_basis`). Step 5 builds observation→cluster edges by reading the observations directly (step 3 leaves no `bears_on` hint), and derives each observation's basis set — its `data_basis` override, else its source's — to find correlated observations by shared node identity. An argument about a specific observation reaches its edge on its own: step 5's script reads `affects_observations` as a backlink, so nothing here needs a placement hint.

**Produces for step 6** (arguments): each `A`'s `statement`, `reasoning` body, `affects_observations`, and `affects_hypotheses`. Step 6 assesses each argument's validity from the reasoning itself — so write the reasoning to stand on its own; an argument carrying only `affects_hypotheses` (no observation) feeds step 7's prior, found via `no_observation_arguments.py`.

## Spec

Step 3 **creates** `O` / `H` / `A` nodes and **edits** each processed curated source node (adds the `extracted` list and body `![[embeds]]`; the source's `data_basis` was set at step 2). It mints **no judgment numbers** — data-reliability is inherited from the source, and validity / likelihood / prior are later steps. Mint every id'd node (`O` / `H` / `A` / `D`) by piping its markdown on stdin — `cat <<'EOF' | python3 /home/simonskade/workspace/.claude/skills/flf-epistack/scripts/create_node.py <analysis-dir> --type <type> --title "..."` … `EOF` — with `{{ID}}` in the piped body only and never in `--title`, and the absolute script path so the call works from any working directory; never a hand-picked id — the script takes the next free `PREFIX-N` under a lock, so parallel children never collide (one counter per prefix, gaps are fine).

**Every node you create rests on exactly one source.** You hold ~5 papers, but you extract each in isolation and never merge across them — near-duplicate hypotheses from different papers (even two of your own) are left un-merged here; cross-paper merging is a later job — hypotheses at step 4, and `generally_known` observations at consolidation (below). `source` is singular and permanent; a merge survivor's extra provenance goes into `additional_sources` only when nodes are merged, never while you extract a single paper.

### Shared fields (observation / hypothesis / argument)

| field | req | meaning |
|---|---|---|
| type | MUST | `observation` / `hypothesis` / `argument` |
| id | MUST | `O-N` / `H-N` / `A-N` |
| statement | MUST | ~1-2 sentences; the filename title already names the thing, so `statement` adds the detail. Per-type meaning below |
| source | MUST | exactly one `[[S-N]]`, pointing into a `curated: true` source |
| locator | MUST | section / figure / page / ¶ into that source |
| quote | OPTIONAL | verbatim snippet (worth adding for load-bearing or surprising items) |

Longer prose — methodology, data detail, the argument's reasoning — lives in the **body** (which is embeddable). Data-reliability is the source's `trust_score` (a [0,1] reliability score set in step 2); step-3 nodes inherit it **by reference** through `source` and never copy it onto the node — nothing derived is cached in frontmatter.

### Attributing each observation's data

Step 2 set each source's `data_basis` — the `[[D-N]]`/`[[S-N]]` bases its findings rest on — and minted those `D` nodes (a `data-basis` (`D-N`) node is the shared link target that lets step 5 detect correlated evidence by node identity, not by matching free text). Read that field, and per observation record the exact data it rests on: the source's own experiment (self-link `[[S-N]]`), an external `[[D-N]]`, or both. Reuse an existing base before minting; a needless duplicate hides real correlation, and duplicates parallel batches mint are reconciled by the step-3 consolidator. (Mint any external base step 2 missed.)

### Per type

1. **observation** (node type **"observations and facts"**, folder `observations-and-facts/`) — records something taken to be true or actually observed about *our* world: an empirical finding **or** a general, uncontested fact about the world (a lot of general facts about the world count as observations here). It must say something true (or presumed observed) about our world specifically, not something that holds across all possible realities — so a purely **mathematical** fact is **not** an observation; encode that as an **argument** (a universally-valid inference you can apply) or, if it is a derived conclusion of interest, a **hypothesis**. A finding here follows **~with certainty**; anything genuinely uncertain or contestable is a *hypothesis*, not an observation. (Henceforth this node type is called simply "observation", id `O`.) Two kinds:
   - **paper-derived** (the default; leave `generally_known` absent/false) — a finding / measurement that follows from *this source's data*. The body MAY add data detail (e.g. a small table of the dataset's key properties — not raw data) and MAY `![[embed]]` the source's methodology section so method is written once. `data_basis` — the exact data this finding rests on, drawn from the source's step-2 `data_basis`: the source's own experiment (self-link `[[S-N]]`), an external `[[D-N]]`, or both. Omit it to inherit the source's full `data_basis`; set an explicit subset when the source is mixed and this observation rests on only some of its bases, so step 5 doesn't over-count correlation.
   - **generally_known** (`generally_known: true`, `data_basis: []`) — a firmly-established, uncontested general fact or event about the world that the paper references but that rests on no dataset; evidence-like because its probability differs across the rival hypotheses, so knowing it discriminates between them (e.g. that humans were established on the landmass before the extinction pulse). It carries the paper it appears in as its `source` like any node, but resting on no data it is never correlated (step 5) and same-fact duplicates across papers are merged into one node at consolidation (below). Be sparing.
2. **hypothesis** — `statement` is an **uncertain** candidate answer that predicts observations. `question` (SHOULD) — the sub-question it answers; a useful hint for step-4 clustering, which groups mutually-exclusive answers to one question into a cluster.
3. **argument** — a universally-valid logical or mathematical validity (a calculation counts as one) that **carries no information of its own**: being valid across all realities, it bears on our world only through what it attaches to. `statement` = the overall implication / conclusion it establishes. `reasoning` (MUST, in the **body**) — the inferential content or calculation, free-form but **detailed** (small-stepped inferences welcome), with no required logical structure or premise/conclusion split. It attaches via two OPTIONAL `[[wikilink]]` lists, and **at least one must be non-empty**:
   - `affects_observations` — the `[[O-N]]` observations this argument bears on; step 5's script attaches it to the matching evidence-link edge and step 8 reads it while pricing a likelihood.
   - `affects_hypotheses` — the `[[H-N]]` hypotheses it bears on directly, independently of any observation; step 7 reads these while setting the cluster's prior.

   **Most arguments attach to an observation** (`affects_observations` non-empty). A paper that merely states a fact and connects it to a claim is usually giving you an *observation* (extract the fact as an `O`), not an argument — create an argument only when the connection itself is nontrivial: non-obvious, or carrying important subtleties. An argument attaching **only** to a hypothesis (no observation) is rare — mainly math / theoretical-physics reasoning, where a theorem applies to a hypothesis directly. Extract a paper's observations **and** hypotheses before its arguments so the ids exist; every id you list must be an `O`/`H` extracted from *this* paper — don't invent a cross-paper link.

Extract only observations, hypotheses, and logical / mathematical considerations. **Exclude** opinions, related-work summaries, and authorial recommendations.

### Source note: `extracted` list + embeds

On each processed source node, in **order of appearance in the paper** — this ordered list is itself the paper's structured summary:
1. `extracted` (MUST, frontmatter) — the ordered list of this paper's `O` / `H` / `A` `[[wikilinks]]`; Bases-queryable.
2. body (SHOULD) — `![[embed]]` each extracted node under section headings so the source note renders as the paper's summary. Methodology MAY be written once here as a `## Methodology` section and embedded into the relevant observation bodies.

### Micro-example

Main question "What drove the extinction of Sahul's megafauna around 45-40 ka?", paper `S-1`:
1. `O-14` — `observations-and-facts/O-14 - Youngest reliable ages for 8 of 12 genera fall within ~2 kyr of first human occupation.md`; source `[[S-1 - Re-dated last-appearance ages for Sahul's extinct megafauna]]`; locator "§Results, Fig 2"; `data_basis` `[[D-4 - Continental late-Quaternary age compilation, group R]]` (its ages come from that external compilation, not S-1's own fieldwork); body: small table of the 12 genera + youngest ages, plus `![[S-1 - Re-dated last-appearance ages for Sahul's extinct megafauna#Methodology]]`.
2. `H-3` — `hypotheses/H-3 - Direct predation by arriving humans drove the extinction.md`; source `[[S-1 …]]`; question "What was the dominant driver of the extinction pulse?".
3. `A-101` — `arguments/A-101 - Continental synchrony of the pulse with first arrival favours a human driver.md`; source `[[S-1 …]]`; locator "§Discussion"; `affects_observations: ["[[O-14 …]]"]` — it turns on the synchrony finding, so step 5's script will attach it to O-14's edge; detailed `reasoning` in the body. (An argument bearing directly on a hypothesis instead — e.g. a theorem constraining one member — would carry `affects_hypotheses: ["[[H-N …]]"]` and no observation; rare, mainly in math/theory papers.)
4. On `S-1`: `extracted: ["[[O-14 …]]", "[[H-3 …]]", "[[A-101 …]]", …]` (order of appearance); body embeds each node under `## Results` / `## Discussion`. (`S-1`'s `data_basis` was set at step 2; abbreviated `…` links stand for the full immutable filename.)

### Checks (binary)

1. Every node sits in its type folder, has `type` ∈ {observation, hypothesis, argument} with a unique matching-prefix `id`, and a filename `id - descriptive title.md`; no id collides with a step-1 id.
2. Every node has **exactly one** `source` (into a `curated: true` source) and a non-empty `locator`.
3. Every observation `statement` is a ~certain finding (spot-check: no uncertain / contested claim sits among observations); every `generally_known: true` observation carries `data_basis: []`, and a paper-derived one leaves `generally_known` absent/false.
4. Every argument has a non-empty `reasoning` body, is nontrivial, and carries **≥1** non-empty attachment (`affects_observations` and/or `affects_hypotheses`); no node is an opinion, related-work summary, or recommendation. Every id in `affects_observations` resolves to an `O` node, and every id in `affects_hypotheses` to an `H` node, each extracted from the same paper.
5. No node carries `method`, `kind`, `bears_on`, `premises`, `conclusion`, `topic`, or `section` fields; no clusters, edges, priors, likelihoods, or validity scores exist (later steps own those).
6. Every processed `curated: true` source has a non-empty `extracted` list in which every id resolves to an O/H/A node whose `source` is that source; no `curated: false` source was processed.
7. Every observation `data_basis` override is a subset of its source's `data_basis`; any straggler `D` node step 3 minted sits in `data-bases/` with a unique `D-N`, `basis_type` in enum, and ≥1 inbound link.
8. `generally_known` merge (consolidation): every survivor carries `merged_from` + `additional_sources`; every absorbed duplicate is `state: merged` in `observations-and-facts/merged/` with `merged_into`; no two live `generally_known` observations state the same fact.

## Process

You extract from the ~5 curated papers in your slice, one paper at a time, applying the conventions above to each.

1. **Read the paper properly — this is the deep read.** Steps 1-2 only skimmed; now go end-to-end. Skim the abstract + figures for the thesis, then read Results and Methods closely (observations live there), then Discussion (hypotheses and arguments live there). Extract in order of appearance so the `extracted` list reads as a faithful summary.
2. **The observation/hypothesis line is the crux.** An observation is what the data essentially force — a measurement, a rate, a correlation actually present in the dataset. A hypothesis is any interpretation, causal claim, or extrapolation that could be wrong even if the data are perfect. Test each candidate: *would a rival team analysing the same data still have to grant this?* Yes → observation; if it turns on a contestable inferential step → hypothesis (and that step is usually an `argument`). The standard failure is promoting the authors' preferred interpretation to an observation because the paper asserts it confidently.
3. **Track which data each finding rests on.** Papers routinely mix their own fieldwork with external compilations. Note, per finding, which dataset / instrument produced it — that is what lets you attribute each observation's `data_basis` correctly against the source's step-2 `data_basis`, so step 5 neither misses nor invents correlation.
4. **Capture arguments as reasoning, not slogans.** Write the `reasoning` body densely enough that step 6 can assess validity without reopening the paper — include the actual calculation for a mathematical argument — but don't formalise into premises/conclusion. Skip trivial inferences (a bare fact-plus-connection is an *observation*, not an argument), opinions, and recommendations. Record what the argument bears on: the observations it turns on in `affects_observations`, any hypothesis it bears on directly in `affects_hypotheses` — at least one must be set, and most arguments carry an observation.
5. **Right granularity, one paper at a time.** One node per distinct claim: don't shatter one finding into near-duplicate observations, and don't bundle several findings into one. Extract each of your ~5 papers in isolation — do not merge or cross-reference across them, not even two papers in your own batch; cross-paper merging happens later, never here.
6. **Write statements to stand alone.** A reader who hasn't seen the paper should be able to parse each `statement` and filename title: specific (numbers, taxa, intervals), self-contained, neutral. Give every node a precise `locator`; add a `quote` for anything load-bearing or surprising, for provenance.
7. **Attribute each observation's data.** The source's `data_basis` is set at step 2; per observation, record the exact data it rests on — the source's own experiment (self-link `[[S-N]]`), an external `[[D-N]]`, or both. Reuse an existing base before minting; a needless duplicate silently hides real correlation. (Mint any external base step 2 missed.)
8. **Stay in your lane.** No scores, clusters, cross-paper edges, observation↔hypothesis links, or validity / likelihood / prior numbers — later steps own all of those. Everything you write must be grounded in the single paper it came from.

**Consolidate — merge `generally_known` duplicates, after every extractor has returned.** A separate consolidation child does this (the same one that reconciles duplicate `D` nodes); an extractor does none of it. Two papers referencing the same generally-known fact yield one fact, not independent evidence, so merge near-duplicate `generally_known` observations into a single node with the full step-4 merge bookkeeping: lowest id survives and gains `merged_from` + `additional_sources` + a per-source `locator` list, each absorbed node gets `state: merged` + `merged_into` and moves to `observations-and-facts/merged/`, and any argument `affects_observations` pointing at an absorbed node is repointed to the survivor so its evidence isn't stranded. Paper-derived observations are never merged: independent data is separate evidence, and shared data is handled as correlation at step 5, not by merging.
