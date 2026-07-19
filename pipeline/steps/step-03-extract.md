# Step 3 — Extract observations, hypotheses, and arguments from a paper

Step 3 fills in the paper-derived body of the graph. **Spawn one fresh subagent per curated source**; each reads its one paper end-to-end and extracts that paper's `observation` / `hypothesis` / `argument` nodes (each resting on exactly that one source), then writes an ordered `extracted` link list back onto the source node. No scoring, no cross-paper merging, no clustering, no observation↔hypothesis edges — those are later steps (4-8). Model: fable subagents.

## Spec

Step 3 **creates** `O` / `H` / `A` nodes and **edits** each processed curated source node (adds the `extracted` list, body `![[embeds]]`, and resolves its `data_basis`). It mints **no judgment numbers** — data-reliability is inherited from the source, and validity / likelihood / prior are later steps. `O` nodes continue the same `O-N` counter the step-1 background observations already used (one integer counter per prefix; new ids just keep climbing, gaps are fine).

Because each subagent sees only its own paper, **every node it creates rests on exactly one source** — near-duplicate hypotheses from different papers are left un-merged here (step 4 merges across papers). `source` is singular and permanent; a merge survivor's extra provenance goes into `additional_sources` at steps 4/6, never here.

### Shared fields (observation / hypothesis / argument)

| field | req | meaning |
|---|---|---|
| type | MUST | `observation` / `hypothesis` / `argument` |
| id | MUST | `O-N` / `H-N` / `A-N` |
| statement | MUST | ~1-2 sentences; the filename title already names the thing, so `statement` adds the detail. Per-type meaning below |
| source | MUST | exactly one `[[S-N]]`, pointing into a `curated: true` source |
| locator | MUST | section / figure / page / ¶ into that source |
| quote | OPTIONAL | verbatim snippet (worth adding for load-bearing or surprising items) |

Longer prose — methodology, data detail, the argument's reasoning — lives in the **body** (which is embeddable). Data-reliability is the source's `trust_score` (a [0,1] reliability score set in step 2); step-3 nodes inherit it **by reference** through `source` and never copy it onto the node (criterion 7: nothing derived is cached in frontmatter).

### Data-basis nodes and resolving `data_basis`

A `data-basis` (`D-N`) node is a minimal stand-in for one shared fallible thing that several findings can rest on — a dataset, a reporting actor, an instrument, an analysis pipeline. Its whole job is to be a **shared link target**: two observations that rest on the same thing link the *same* `D` node, so step 5 detects correlated evidence by node identity, not by matching free text. Fields: `type: data-basis`, `id: D-N`, `basis_type` (enum: dataset / actor / instrument / pipeline), `url` (value or `unknown`); the body SHOULD carry a one-line `known_biases` — the failure mode that would move everything resting on this basis together.

Step 1 records each source's `data_basis` but may leave it `unknown` when it couldn't cheaply see the methods. **Your subagent reads the methods properly, so it MUST resolve `unknown`** into a real value — no curated source may still read `unknown` after step 3. The value is one of:
1. a list of `[[D-N]]` / `[[S-N]]` naming the fallible bases the paper's findings rest on — a **self-link `[[S-N]]`** (the paper itself) means it collected its own data; or
2. `[]` — a theory / pure-argument piece resting on no data.

Mint a new `D` node in `data-bases/` for any shared basis this paper rests on that has no node yet; **reuse the existing node** (via Obsidian autocomplete) whenever the thing is already represented, since correlation detection depends on the shared identity. Mint rule: is it a citable artifact you could extract observations from? Yes → it's an `S`; no → a `D`.

### Per type

1. **observation** — `statement` is a finding / measurement that follows **~with certainty** from the source's data; anything genuinely uncertain or contestable is a *hypothesis*, not an observation. Leave `general` absent (or `false`) — that marks it paper-derived, versus the step-1 background observations that carry `general: true`. The body MAY add data detail (e.g. a small table of the dataset's key properties — not raw data) and MAY `![[embed]]` the source's methodology section so method is written once. `data_basis` (SHOULD, only when the source is mixed) — a subset list of the source's `data_basis` naming just the bases *this* observation rests on; omit it and the observation inherits the source's full `data_basis`. Set it only when the source has >1 basis and this observation rests on some but not all (e.g. an external compilation vs the paper's own fieldwork), so step 5 doesn't over-count correlation.
2. **hypothesis** — `statement` is an **uncertain** candidate answer that predicts observations. `question` (SHOULD) — the sub-question it answers; a useful hint for step-4 clustering, which groups mutually-exclusive answers to one question into a cluster.
3. **argument** — capture only **nontrivial** arguments (a mathematical calculation counts as one). `statement` = the overall implication / conclusion it establishes. `reasoning` (MUST, in the **body**) — the inferential content or calculation, free-form but **detailed** (small-stepped inferences welcome), with no required logical structure or premise/conclusion split. That is the whole node.

Extract only observations, hypotheses, and logical / mathematical considerations. **Exclude** opinions, related-work summaries, and authorial recommendations.

### Source note: `extracted` list + embeds

On each processed source node, in **order of appearance in the paper** — this ordered list is itself the paper's structured summary:
1. `extracted` (MUST, frontmatter) — the ordered list of this paper's `O` / `H` / `A` `[[wikilinks]]`; Bases-queryable.
2. body (SHOULD) — `![[embed]]` each extracted node under section headings so the source note renders as the paper's summary. Methodology MAY be written once here as a `## Methodology` section and embedded into the relevant observation bodies.

### Micro-example

Main question "What drove the extinction of Sahul's megafauna around 45-40 ka?", paper `S-1`:
1. `O-14` — `observations/O-14 - Youngest reliable ages for 8 of 12 genera fall within ~2 kyr of first human occupation.md`; source `[[S-1 - Re-dated last-appearance ages for Sahul's extinct megafauna]]`; locator "§Results, Fig 2"; body: small table of the 12 genera + youngest ages, plus `![[S-1 - Re-dated last-appearance ages for Sahul's extinct megafauna#Methodology]]`.
2. `H-3` — `hypotheses/H-3 - Direct predation by arriving humans drove the extinction.md`; source `[[S-1 …]]`; question "What was the dominant driver of the extinction pulse?".
3. `A-101` — `arguments/A-101 - Continental synchrony of the pulse with first arrival favours a human driver.md`; source `[[S-1 …]]`; locator "§Discussion"; detailed `reasoning` in the body.
4. On `S-1`: `extracted: ["[[O-14 …]]", "[[H-3 …]]", "[[A-101 …]]", …]` (order of appearance); `data_basis` resolved from `unknown` to `["[[D-4 - Continental late-Quaternary age compilation, group R]]"]` (its ages come from that compilation, not its own fieldwork); body embeds each node under `## Results` / `## Discussion`. (Abbreviated `…` links stand for the full immutable filename.)

### Checks (binary)

1. Every node sits in its type folder, has `type` ∈ {observation, hypothesis, argument} with a unique matching-prefix `id`, and a filename `id - descriptive title.md`; no id collides with a step-1 id.
2. Every node has **exactly one** `source` (into a `curated: true` source) and a non-empty `locator`.
3. Every observation `statement` is a ~certain finding (spot-check: no uncertain / contested claim sits among observations); no paper observation has `general: true`.
4. Every argument has a non-empty `reasoning` body and is nontrivial; no node is an opinion, related-work summary, or recommendation.
5. No node carries `method`, `kind`, `bears_on`, `premises`, `conclusion`, `topic`, or `section` fields; no clusters, edges, priors, likelihoods, or validity scores exist (later steps own those).
6. Every processed `curated: true` source has a non-empty `extracted` list in which every id resolves to an O/H/A node whose `source` is that source; no `curated: false` source was processed.
7. No processed source still reads `data_basis: unknown`; every `data_basis` entry resolves to an existing `D` or `S` node; any new `D` node sits in `data-bases/` with a unique `D-N`, `basis_type` in enum, and ≥1 inbound link; every observation `data_basis` override is a subset of its source's `data_basis`.

### Interface

**Consumes (from step 2):** the `curated: true` source nodes (equivalently, those left directly in `sources/`), opened via their `url`; process exactly this set, one subagent each. Each node inherits its source's `trust_score` as data-reliability through the `source` link (never copied); `motivatedness` (a source's known agenda / COI) travels the same link — its data-trust effect is already priced into `trust_score`, its argument-selection effect is handled at steps 5-6. Ignore `usefulness` / `combined_score`.

**Produces for step 4** (cluster hypotheses): the single-source `H` nodes. Step 4 reads `statement` (+ `question`) to drop irrelevant hypotheses, merge near-duplicates across papers, and group them into mutually-exclusive clusters.

**Produces for step 5** (link evidence): the `O` and `A` nodes plus a resolved `data_basis` on every curated source (and any per-observation overrides). Step 5 builds observation→cluster edges and argument links by reading the nodes directly (step 3 leaves no `bears_on` hint), and derives each observation's basis set — its `data_basis` override, else its source's — to find correlated observations by shared node identity.

**Produces for step 6** (argument validity): each `A`'s `statement` + `reasoning` body; step 6 judges an argument's complexity from the reasoning itself, so write the reasoning to stand on its own.

## Process

You (the step-3 coordinator) spawn one fresh fable subagent per curated source and pass it the conventions above. Points 1-7 and 9 are how each subagent extracts its one paper; point 8 is your job across them.

1. **Read the paper properly — this is the deep read.** Steps 1-2 only skimmed; now go end-to-end. Skim the abstract + figures for the thesis, then read Results and Methods closely (observations live there), then Discussion (hypotheses and arguments live there). Extract in order of appearance so the `extracted` list reads as a faithful summary.
2. **The observation/hypothesis line is the crux.** An observation is what the data essentially force — a measurement, a rate, a correlation actually present in the dataset. A hypothesis is any interpretation, causal claim, or extrapolation that could be wrong even if the data are perfect. Test each candidate: *would a rival team analysing the same data still have to grant this?* Yes → observation; if it turns on a contestable inferential step → hypothesis (and that step is usually an `argument`). The standard failure is promoting the authors' preferred interpretation to an observation because the paper asserts it confidently.
3. **Track which data each finding rests on.** Papers routinely mix their own fieldwork with external compilations. Note, per finding, which dataset / instrument produced it — that is what lets you resolve the source's `data_basis` and set per-observation overrides correctly, so step 5 neither misses nor invents correlation.
4. **Capture arguments as reasoning, not slogans.** Write the `reasoning` body densely enough that step 6 can assess validity without reopening the paper — include the actual calculation for a mathematical argument — but don't formalise into premises/conclusion. Skip trivial one-step inferences, opinions, and recommendations.
5. **Right granularity, within this paper only.** One node per distinct claim: don't shatter one finding into near-duplicate observations, and don't bundle several findings into one. Do not look at other papers or try to merge across them — cross-paper merging is step 4's job, and your single-paper view is what guarantees you can't accidentally do it here.
6. **Write statements to stand alone.** A reader who hasn't seen the paper should be able to parse each `statement` and filename title: specific (numbers, taxa, intervals), self-contained, neutral. Give every node a precise `locator`; add a `quote` for anything load-bearing or surprising (criterion 5, provenance).
7. **Resolve `data_basis` deliberately.** You are now reading the methods, so decide for the source: own data (self-link `[[S-N]]`), external base(s) (link or mint `D` / `S` nodes), or none (`[]`, a theory piece). Before minting a `D` node, check `data-bases/` for an existing node for the same thing and reuse it — correlation detection depends on shared identity, so a needless duplicate silently hides real correlation.
8. **Avoid id / `D`-node collisions across papers.** Simplest: process papers **sequentially**, so each subagent sees the ids and `D` nodes already minted and continues / reuses them cleanly. If you parallelise for speed, give each subagent a disjoint id block for its new `O` / `H` / `A` / `D` nodes and run a quick pass afterwards to merge any duplicate `D` nodes (two papers minting a node for the same dataset). Ids are permanent, so a collision is expensive to unwind.
9. **Stay in your lane.** No scores, clusters, cross-paper edges, observation↔hypothesis links, or validity / likelihood / prior numbers — later steps own all of those. Everything you write must be grounded in this one paper.
