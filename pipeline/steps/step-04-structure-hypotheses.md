# Step 4 — Structure hypotheses

Step 3 handed over a pile of `hypothesis` (`H`) nodes: each has a `statement` (one claim), a `question` (the sub-question the paper posed it against — a clustering hint), exactly one `source` (`[[S-N]]`) and one `locator` string. Step 3 ran a fresh subagent per paper and did **no** cross-paper deduplication, so the same hypothesis usually arrives several times in different words. Step 4 turns that pile into the **structured hypothesis layer**: `hypothesis-cluster` (`HC`) nodes — each a sub-question plus its mutually-exclusive answers — and a disposition on every `H`. Nothing is deleted. Step 4 mints **no numbers**: the whole layer must read with zero weights present (criterion 7); priors and likelihoods come at steps 7-8.

## Spec

### Output

1. **Create `hypothesis-clusters/`** holding the `HC-N` nodes, plus any new `H` nodes you mint — residual catch-alls and constructed complements — continuing the shared `H-N` counter (tombstoned ids are never reused).
2. **Edit existing `H` nodes** with the disposition fields below, giving each exactly one `state`: `active` (member of one cluster, stays in `hypotheses/`), `merged` (a near-duplicate absorbed into a survivor — moved to `hypotheses/merged/`), or `dropped` (irrelevant to the run's `main_question` — moved to `hypotheses/dropped/`). No `H` file is ever deleted, only moved.
3. **Write `structuring-manifest.md`** (a plain file, not a graph node): `main_question` verbatim; the **cluster inventory** — `[[HC-N]]` + its sub-question, one line each, which is the KB's top-level map; counts (H in / active / merged / dropped / clusters); a `generated` timestamp.

Same layout as earlier steps: one markdown file per node (typed frontmatter + prose body), filename beginning with the id (`HC-1 - Dominant driver of the extinction pulse.md`).

### hypothesis-cluster node

The filename's descriptive part names the dimension the members answer (a noun phrase — "Dominant driver of the extinction pulse"); the precise sub-question, when one clean sentence exists, goes in `question`.

| field | req | meaning |
|---|---|---|
| type | MUST | `hypothesis-cluster` |
| id | MUST | `HC-N`, fixed at creation |
| hypotheses | MUST | `[[H-N]]` list, ≥2, all `active`, distinct, none also in another cluster. This is the **canonical** membership (each member's `cluster` field is the derived backlink). Order by **ascending id, residual last** — this frozen order is the vector index steps 7-8 address members by, so never reorder it afterwards |
| exclusivity | MUST | one line: why at most one member can be true |
| exhaustive_by_construction | MUST — key present even if `false` | bool. `true` only if the members logically cover the answer space; then the **body** MUST justify it and name what a failure of the *analysis* would look like and which member it would favour. `false` ⇒ a residual member is required |
| independence | MUST | one line: why this cluster's prior factorizes from the other clusters (knowing one answer doesn't shift another's base rate) |
| depends_on | MUST — key present even if empty | `[HC-N: one-line note]` for cross-cluster dependences you chose to leave un-merged. **Ideally empty** — a non-empty entry flags that this pair is only approximately independent. Steps 8-10 read it |
| question | OPTIONAL | the precise sub-question the members answer, one sentence ending `?`, when one cleanly exists |
| relevance | OPTIONAL | one line: how the answer bears on `main_question` |

Body: embed the members (`![[H-N …]]`) in `hypotheses` order so the cluster reads in one view, then the justification prose (exclusivity, exhaustiveness, carving).

### disposition fields written on each `H`

| field | req | meaning |
|---|---|---|
| state | MUST | `active` \| `merged` \| `dropped`; exactly one |
| cluster | MUST if `active` | `[[HC-N]]`; the derived backlink, MUST match that cluster's `hypotheses` |
| merged_into | MUST if `merged` | `[[H-N]]` of the survivor (itself `active`) — resolves in **one hop, never a chain**; if the survivor is later absorbed, rewrite this to the newer survivor. The node's other fields stay untouched, so its original per-paper wording remains auditable |
| merged_from | MUST on a survivor | the absorbed ids |
| additional_sources | MUST on a survivor (absent otherwise) | the absorbed hypotheses' `[[S-N]]` sources. The survivor's own `source` is never rewritten — this is the one place an `H` rests on >1 source |
| locator | MUST on a survivor | one `"S-N: <where>"` entry per source across `source` + `additional_sources` (step 3 wrote a single string; a survivor's becomes this list) |
| generalization_note | MUST if a merge widened the statement | one line: what was widened, which distinction was given up |
| drop_reason | MUST if `dropped` | one line: why it discriminates nothing relevant to `main_question` |
| residual | MUST on a catch-all member | `true`; exactly one per non-exhaustive cluster, listed last. Its `statement` reads "the answer is something not listed here", never as one more named answer |
| origin | MUST if not from a paper | `step-4-residual` \| `step-4-constructed` — the only `H` nodes allowed an empty `source` |

Merge mechanics (survivor = lowest id, absorbed nodes tombstoned via `merged_into` and moved to `hypotheses/merged/`, survivor keeps its own `source` and gains the absorbed ones in `additional_sources` with a per-source `locator`) follow the shared merge-bookkeeping convention; the fields above are how it lands on `H` nodes.

### Rules

1. **Merging near-duplicates is the central job.** Merge two `H` nodes only when their cores are the same **and no curated observation in scope would come out differently under them**; if some observation would discriminate them, they are distinct members — keep both. Widening a survivor's `statement` to cover what it absorbed is fine with a `generalization_note`; the absorbed node keeps its own wording, so a merge can be read back and undone.
2. **Exclusivity + exhaustiveness make the cluster a probability space.** Members pairwise exclusive, and with the residual exactly one is true — that is what lets step-8 priors normalize within the cluster and step-7 posteriors be well-defined. Give every non-exhaustive cluster exactly one residual, listed last, whose `statement` names the escape ("some driver other than the above, e.g. disease"), never a bare "other".
3. **Independence lets each cluster be scored alone.** `independence` asserts the joint prior factorizes: `P(h_i ∧ g_j) ≈ P(h_i)·P(g_j)`. It does *not* mean clusters share no evidence — one observation can discriminate in several. Default for two dependent clusters: **keep them separate and record the dependence in `depends_on`.** Fold them into a single cluster of *combination* members only when the dependence is significant **and** the combined cluster stays **under ~10 members** — combinations multiply out fast, and each member costs a prior plus a likelihood per observation. Never carve two clusters that are alternative partitions of the *same* sub-question: that double-counts the evidence (criterion 3), and no `depends_on` note repairs it.
4. **Carve bottom-up, at comparable grain.** Let cluster boundaries fall out of the concrete hypotheses and the observations that separate them, rather than imposing a top-down taxonomy of the debate. Non-residual members should trace to ≥1 curated source; a logically-needed member no paper stated (typically a complement) is allowed with `origin: step-4-constructed` + a one-line reason. Keep members at similar specificity — an over-narrow member competing with a broad one distorts step-8 priors.

### Micro-example

Main question "What drove the extinction of Sahul's megafauna around 45–40 ka?".

1. **`HC-1`** — `hypothesis-clusters/HC-1 - Dominant driver of the extinction pulse.md`; `question` "What was the dominant driver of the Sahul megafauna extinction pulse (~45–40 ka)?"; `hypotheses` `["[[H-3 - Direct predation by arriving humans drove the extinction]]", "[[H-11 - Indirect human impact through burning and habitat transformation drove the extinction]]", "[[H-21 - Climate-driven aridification drove the extinction]]", "[[H-42 - Some driver not listed above dominated]]"]` (ascending id, residual last); `exclusivity` "each names a different dominant driver of one pulse; at most one dominated"; `exhaustive_by_construction: false`; `independence` "the driver question and the arrival-chronology question factorize — neither answer constrains the other's base rate"; `depends_on` `["HC-2: arrival chronology mildly shifts P(the pulse is arrival-keyed); judged small — revisit at step 10"]`.
2. **`H-3` (survivor)** absorbs `H-127` "Hunting of juveniles drove the extinction" — same core, no in-scope observation separates them, so merge. `H-3` keeps `source` `[[S-1 - …]]`, gains `additional_sources` `[[[S-6 - …]]]`, `locator` `["S-1: §Results", "S-6: §3.2"]`, `merged_from` `[[H-127 …]]`, `generalization_note` "widened 'hunting of juveniles' → 'direct predation'; no in-scope observation separates them". `H-127` → `state: merged`, `merged_into: [[H-3 …]]`, other fields untouched, moved to `hypotheses/merged/`.
3. **`H-11` was NOT merged** into `H-3`, although it too turns on human arrival: observation `O-22` discriminates them — ages surviving ~5 kyr past the arrival window fit a slow habitat squeeze, not a rapid kill-off. Discriminable ⇒ distinct members.
4. **`H-42` (residual, last)** — `statement` "the answer is something not listed here, e.g. a disease or trophic cascade no one in this literature has proposed"; empty `source`; `origin: step-4-residual`.
5. **`H-133` dropped** — `drop_reason` "concerns the taxonomy of one extinct genus only; discriminates no cluster's members"; moved to `hypotheses/dropped/`.

### Checks (binary)

1. Every `H` has exactly one `state`. `merged` ⇒ `merged_into` resolves in one hop to an `active` `H`; `dropped` ⇒ non-empty `drop_reason`; both sit in the matching sub-folder. Total `H` file count ≥ the step-3 count (nothing deleted).
2. Every `HC` sits in `hypothesis-clusters/` with a unique `HC-N` its filename begins with, ≥2 distinct `active` members ordered ascending-id / residual-last, non-empty `exclusivity` and `independence`, and the `depends_on` and `exhaustive_by_construction` keys present.
3. Each `HC` has exactly one `residual: true` member listed last — or `exhaustive_by_construction: true` with a body justification naming an analysis-failure mode and the member it favours.
4. Every `active` `H` appears in exactly one `HC`'s `hypotheses`, its `cluster` backlink names that `HC`, and no `H` id is in two clusters.
5. Every survivor has `merged_from`, its original single `source` unchanged, `additional_sources` = exactly the absorbed sources (disjoint from `source`), one `locator` entry per source, and a `generalization_note` iff it was widened. Every non-residual `active` `H` lacking a `source` carries `origin: step-4-constructed` + reason.
6. No step-4-owned field holds a number, probability, weight, or rank.

### Interface

1. **Consumes (step 3):** `H` nodes (`statement`, `question`, `source`, `locator`) and `main_question` from the step-1 manifest (`manifest.md`). You MAY read `observation` (`O`) statements to test discriminability before merging; you create no edges (that is step 5) and ignore `argument` (`A`) nodes.
2. **Owns:** the `HC` nodes entirely, and on `H` nodes the disposition fields above (`state`, `cluster`, `merged_into`, `merged_from`, `additional_sources`, `generalization_note`, `drop_reason`, `residual`, `origin`). On a merge survivor you also touch two step-3 fields — `statement` (widening) and `locator` (→ list); `source` is never rewritten. Write nothing on `O`, `A`, `S`.
3. **Feeds step 5** (link evidence): `HC` nodes are the targets of observation edges — the edge unit is (observation, `HC-N`) with a per-member breakdown indexed by `HC.hypotheses` order. Step 5 resolves any `merged`/`dropped` `H` via `merged_into` (one hop) before linking.
4. **Feeds steps 7-8** (likelihoods, priors): `HC.hypotheses` in its frozen order is the vector every prior and likelihood is indexed against; the residual (`hypotheses[-1]`, absent iff `exhaustive_by_construction: true`) is what makes the prior sum to 1 honestly. `independence` licenses per-cluster scoring; `depends_on` marks where that is approximate; `merged_from` counts papers, not evidence — never read it as weight.

## Process

1. **Load the field.** Read every `active` `H` (its `statement`, `question`, `source`) and the curated `observation` statements. Expect heavy duplication — a fresh step-3 subagent read each paper, so the same hypothesis recurs in different words, and reconciling that is most of the work.
2. **Find the sub-questions bottom-up.** Group hypotheses by the dimension they answer. The `question` field is a hint, but trust the `statement`s over the labels, and resist importing a tidy textbook taxonomy of the debate — let each cluster's boundary fall out of what the hypotheses actually claim and what the observations can pull apart. A good cluster is one sub-question whose answers the evidence discriminates. The frame is MECE (mutually exclusive, collectively exhaustive): zero overlap between members, zero gaps in the space.
3. **Merge on the discriminability test — the crux.** For each near-duplicate pair ask: does any curated observation in scope come out differently under the two? If no, they are one member — merge (lowest id survives; widen with a `generalization_note` if needed). If yes, they are distinct members — keep both. This is the analysis-of-competing-hypotheses move: evidence that can't tell two hypotheses apart is no reason to hold them apart. Over-merging silently destroys resolution that steps 5-7 would have used; under-merging inflates the space and skews priors. When genuinely unsure, keep them separate — a later step can't un-merge, whereas separate members simply compete.
4. **Make each cluster a clean probability space.** State in one line why at most one member holds; if two could co-hold, the carving is wrong (or you want a combination cluster). Then either argue `exhaustive_by_construction` — naming the analysis-failure that would break it — or add exactly one residual so "the members, or none of them" covers the space. Keep members at comparable grain.
5. **Handle cross-cluster dependence by default-separate.** Two clusters are independent when the answer to one doesn't shift the other's base rate. Where they interact, prefer separate clusters plus a `depends_on` note over a combination cluster; build combinations only when the dependence really bites and the product stays under ~10 members. Hunt for the trap: two clusters that are secretly the same sub-question sliced two ways double-count the evidence, and no note fixes that — merge or re-carve them.
6. **Drop only the genuinely off-topic.** A hypothesis that bears on nothing in the `main_question` moves to `dropped` with a one-line reason. "Bears only weakly" is a reason to keep it and let priors handle it, not to drop; be conservative.
7. **Add constructed members sparingly.** If a cluster's logic implies an answer no paper stated — often the "neither/complement" case — add it with `origin: step-4-constructed`. Don't manufacture members to look thorough; each one is paid for again in every later step.
8. **Write the manifest as the map, and freeze the order.** `structuring-manifest.md`'s cluster inventory is the KB's top-level entry point — a reader should see the whole question's decomposition at a glance (criterion 10). Fix each cluster's member order now (ascending id, residual last); every later step addresses members by position, so treat the order as a committed interface. Keep the whole layer number-free (criterion 7) — the moment you want to write "this one's more likely," stop; that is steps 7-8.
