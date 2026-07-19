# Step 5 — Link observations and arguments to hypothesis-clusters

**Output = the evidence layer.** For every observation that *discriminates* between a cluster's members, mint one `evidence-link` (`E-N`) edge, observation → cluster. Separately, write onto each active hypothesis an `arguments` list naming the standalone arguments that bear on *that hypothesis's prior* (a prior-shaping argument is not evidence, so it is not an edge). Mark a `link_state` on every observation and every argument so nothing is silently unconsidered. Step 5 mints **no numbers** — the layer reads with zero weights present (criterion 7); step 7 later fills each edge's likelihood, step 8 reads the hypothesis argument-lists.

## Spec

### Artifact and layout

1. One markdown file per node (typed YAML frontmatter + prose body), edited in place.
2. **Obs edges** live in `evidence-links/`, prefix `E`. Filename `E-N - <descriptor>.md`, and the descriptor names **every id the edge touches** — the `from` observation, the `to` cluster, and any attached argument — so a quick-switch jumps straight to any endpoint: `E-14 - O-14 × HC-1 +A-7 — youngest ages cluster in the arrival window.md`. No `title` field; the filename is the title and is fixed at creation (a SKILL.md convention — renaming breaks inbound links).
3. The edge file is the **single canonical record** of an obs edge; endpoints get no mirrored link fields. The edge body embeds its observation (`![[O-N]]`) so it reads standalone; Obsidian backlinks surface every edge on the `O` and the `HC`.
4. **Standalone (prior-shaping) arguments are recorded on the hypothesis, not as an edge** — as an `arguments` list on each active `H`. Step 8 reads those lists.
5. **Orphans move, never deleted.** An observation or argument that links to nothing gets `link_state: orphan` and moves to `observations/orphan/` or `arguments/orphan/`, keeping its `link_state` and its `source` link so it stays reachable from the paper it came from (provenance, criterion 5).
6. SHOULD: `evidence-links.base` — a derived adjacency view (one row per edge: `id, from, to, arguments, correlated_with`); edges stay the source of truth. Skip under time pressure.

### Schema — the `evidence-link` node (obs → cluster; the only edge kind)

| field | req | meaning |
|---|---|---|
| type | MUST | `evidence-link` |
| id | MUST | `E-N`; fixed at creation |
| from | MUST | `[[O-N]]` — the observation |
| to | MUST | `[[HC-N]]` — the hypothesis-cluster |
| arguments | OPTIONAL | `[{id: A-N, role: <one line: what it changes about how this observation bears on these hypotheses>}]`. Omit where the evidence relation is plain — most edges have none. ≥2 allowed; step 7 composes them |
| correlated_with | MUST | sibling edges **into the same cluster** whose observation's basis set intersects this one's (they share ≥1 `[[D-N]]`/`[[S-N]]` node). Mechanically derived; `[]` if none |

Body: the `![[from]]` embed + an optional `## Why this is evidence` — prose naming which members predict the observation differently and which way, written only where that is not obvious from the observation and the member statements. Step 7 later appends its own `## Likelihood` section; leave the rest of the note to it.

### Schema — fields step 5 writes on existing nodes

Context you need (from earlier steps, not repeated elsewhere here): an **observation** (`O`) is a finding that follows ~with certainty from a source's data — either step-1 background (`general: true`, rests on no data) or step-3 paper-derived (`general` absent/false). An **argument** (`A`, from step 3) has a `statement` + a `reasoning` body. A **hypothesis** (`H`) has a `state` — `active` (member of exactly one cluster), `merged`, or `dropped`. A **hypothesis-cluster** (`HC`) carries `hypotheses`: an ordered list of its active members (ascending id, catch-all residual last), which are mutually exclusive.

| field | req | on | meaning |
|---|---|---|---|
| link_state | MUST | every `O` (incl. `general: true`) and every `A` | `linked` \| `orphan`. An `O` is `linked` iff it is the `from` of ≥1 edge. An `A` is `linked` iff it appears in some edge's `arguments` **or** in some `H`'s `arguments` list. Orphan = neither → the file moves to the `orphan/` sub-folder (nothing deleted) |
| arguments | MUST | every `active` `H` | `[[[A-N]], …]` — the standalone arguments that raise or lower this hypothesis's base rate relative to its cluster siblings, independently of any single observation. `[]` if none. **No direction or weight** — step 8 reads the list and reasons from the arguments themselves |

**Basis set — read, never written.** To compute `correlated_with` you need each observation's *basis set*: `basis(O)` = `O.data_basis` if the observation carries that override (a step-3 field), else its source's `data_basis` — each a set of `[[D-N]]`/`[[S-N]]` nodes naming the fallible datasets/actors/instruments the finding rests on. A `general: true` observation rests on no data (`data_basis: []`) and is therefore never correlated. You read this only to derive `correlated_with`; you write no basis field.

### Rules

1. **Edge = discrimination, not topical relatedness.** Create an obs → cluster edge iff ≥2 of the cluster's members make materially different predictions about the observation. An observation "about the topic" that every member predicts equally carries no diagnostic weight — leave it unlinked there.
2. **Observations are never merged.** Near-duplicate observations from different papers stay separate nodes: if they rest on the same data their basis sets share a node and they get flagged correlated; genuinely independent replications rest on distinct basis nodes and correctly count twice.
3. **Correlation is per cluster.** For every basis node with ≥2 edges into the same cluster, each of those edges lists the others in `correlated_with` (set-intersection over basis-node identity, not string equality). Step 7 must not enter a correlated group as independent likelihood factors (criterion 3) — that is the standard way Bayesian aggregation manufactures false confidence.
4. **Two argument placements.** An argument that changes how a *specific observation* bears on the members goes in that edge's `arguments`; one that bears on a hypothesis's prior *independently of any single observation* goes in that `H`'s `arguments` list. The same `A` may do both. Step 3 leaves no placement hint — infer it from `A.statement` + the `reasoning` body.
5. **One edge per (from, to) pair** — no duplicates; multiple arguments live in the one edge's `arguments`. An observation may edge into several clusters. Never reference a `merged` or `dropped` hypothesis in an `H.arguments` list — only `active` H nodes get a list.

### Micro-example

Main question "What drove the extinction of Sahul's megafauna around 45–40 ka?"; cluster `HC-1` "Dominant driver of the megafauna extinction pulse", members in id order `[H-3 direct predation, H-11 indirect human impact, H-21 climate aridification, H-42 residual]`.

1. `E-14` — file `E-14 - O-14 × HC-1 +A-7 — youngest ages cluster in the arrival window.md`; from `[[O-14 - Youngest reliable ages for 8 of 12 genera fall within ~2 kyr of first occupation]]` → `[[HC-1 - Dominant driver of the megafauna extinction pulse]]`; `arguments: [{id: A-7, role: "repeated arrival waves widen the window, raising P(obs|H-3) relative to a single-front reading"}]`; `correlated_with: [[[E-22 - O-22 × HC-1 — late survivors postdate the arrival window]]]`; body embeds `![[O-14 …]]` under `## Why this is evidence` reading "H-3 predicts the youngest ages pile up inside the arrival window; H-21 predicts they track the aridity maximum instead".
2. `E-22` — from `[[O-22 - Three genera have reliable ages more than 5 kyr after the arrival window]]` → `HC-1`; `correlated_with: [[[E-14 …]]]`. Both observations derive the basis set `{[[D-4 - Continental late-Quaternary age compilation, group R]]}` through their shared source (the same continental age compilation), so they intersect on `D-4` and step 7 estimates the pair jointly.
3. `H-21` (active member) — `arguments: [[[A-31 - No comparable extinction pulse is recorded at earlier glacial terminations]]]`, a base-rate argument lowering H-21's prior relative to its siblings, recorded on the hypothesis, not as an edge. `H-3`, `H-11`, `H-42`: `arguments: []`.
4. `O-127` — `link_state: orphan`, moved to `observations/orphan/`, `source` intact — present-day dietary ecology, which none of the four drivers separate. `A-31` is `linked` (it sits in H-21's list).

### Checks (binary)

1. Every edge sits in `evidence-links/` with `type: evidence-link`, a unique `E-N` its filename begins with (`E-N - <descriptor>.md`), and `from` `[[O-N]]` + `to` `[[HC-N]]` both resolving; the filename names the `from`/`to` ids and any argument ids; every `arguments` id resolves to an `A` with a non-empty `role`; no (from, to) pair appears twice.
2. No edge and no `H.arguments` list references a `merged` or `dropped` hypothesis; every `to` is an existing `HC`.
3. Spot-check 3 edges against rule 1: for each, ≥2 members of the target cluster predict the observation differently — readable off the observation and the member statements, or off the edge's `## Why this is evidence`.
4. Every `O` (step-1 and step-3) and every `A` has `link_state`; `orphan` ⟹ the file sits in the `orphan/` sub-folder with `source` intact; `linked` O ⟹ `from` of ≥1 edge; `linked` A ⟹ in ≥1 edge's `arguments` or ≥1 `H.arguments` list. Every `active` `H` has an `arguments` key (list or `[]`). O/A/H/HC counts are unchanged vs the earlier steps (nothing deleted).
5. Every `linked` observation resolves to a basis set; recomputing `correlated_with` per cluster by set-intersection over basis-node identity reproduces exactly what is stored; no free-text basis strings (basis is always `[[D-N]]`/`[[S-N]]` links).
6. No step-5-owned field holds a number, probability, weight, or rank; the layer is complete and readable with none present (criterion 7).

### Interface

**Consumes.** From step 4: each `HC`'s id, its ordered `hypotheses` list and member statements, and each `H`'s `state`/`merged_into`. From step 3: `O.statement` + body, `A.statement` + `reasoning` body, and each observation's basis set (its `data_basis` override else its source's `data_basis`, read only to derive correlation). From step 1: `general: true` observations, linked exactly like paper observations. Step 5 reads **no scores** (not trust, usefulness, or validity — step 6 runs after).

**Owns.** The `evidence-link` type entirely, plus `link_state` on `O`/`A` and the `arguments` list on `active` `H` nodes. Writes no basis field; modifies no other upstream field.

**Feeds step 6** (argument assessment): `link_state: linked` on `A` nodes is its work set (orphans may be skipped). If step 6 merges duplicate arguments it repoints absorbed ids in both edge `arguments` and `H.arguments` lists to the survivor.
**Feeds step 7** (likelihoods): each edge (`from`, `to`, `arguments` roles, `correlated_with`, any `## Why this is evidence`) plus `HC.hypotheses` order. A non-empty `correlated_with` means step 7 makes **one joint estimate for the whole group**, never independent factors (criterion 3).
**Feeds step 8** (priors): each active `H`'s `arguments` list is the set of standalone arguments entering that member's prior.

## Process

The one judgment that matters here is **diagnosticity**: an observation is evidence on a cluster only where the cluster's members would predict it *differently*. This is the core of Heuer's Analysis of Competing Hypotheses — evidence consistent with every hypothesis has no diagnostic value, and the job is to find and record where the hypotheses come apart, not to pile up items "consistent with" a favoured answer. Work by discrimination, not by topic.

A workable order:

1. **Edges, cluster by cluster.** For each cluster, walk the observations that plausibly touch its sub-question (use topic to prune — most observations bear on at most one cluster, some on none). For each candidate, run the diagnosticity test: sketch, qualitatively, `P(observation | member)` down the `hypotheses` list. If ≥2 members differ materially, mint the edge; if they'd all predict it about equally, don't — that observation is non-diagnostic *here* (it may still discriminate another cluster). Where the discrimination isn't obvious from reading the observation against the member statements, write it into `## Why this is evidence`: name which members predict it differently and which way. No numbers — direction only; step 7 prices it.
2. **Be honest about orphans.** An observation that discriminates no cluster's members is an orphan — a normal, expected outcome, not a failure. Do not manufacture a weak edge to avoid an orphan; it inflates the evidence base with non-diagnostic links and, once step 7 runs, false confidence. Equally, don't lazily orphan something genuinely diagnostic because the discrimination took a moment to see.
3. **Place arguments by what they move.** Read each argument's `statement` and `reasoning`. If it changes how a *specific observation* bears on the members — e.g. "this dating method has a bias that widens the arrival window" — attach it to that edge with a one-line `role`. If it shifts a hypothesis's base rate on its own — e.g. "no comparable pulse at earlier glacial terminations" lowering a climate hypothesis's prior — put it on that `H`'s `arguments` list. Some arguments do both. When unsure, ask: does this argument need a particular observation to matter? If yes, it's edge-level; if it stands alone, it's hypothesis-level.
4. **Derive correlation mechanically, then sanity-check it.** After the edges exist, group each cluster's edges by shared basis node and fill `correlated_with`. This is the criterion-3 guard: two observations resting on the same compilation, instrument, or actor are not independent even when they come from different papers and read differently. The trap runs both ways — over-flag and you erase real independent replications (which should count twice); under-flag and you let one dataset speak with two voices. Basis identity is *node* identity (the same `[[D-N]]`/`[[S-N]]`), not similar wording. A `general: true` observation rests on no data and is never correlated.
5. **Mark `link_state` last**, once edges and hypothesis lists are settled, and move every orphan to its sub-folder with its `source` intact.

Judgment left to you: how finely to slice "materially different", when a discrimination is obvious enough to skip the prose, and how hard to hunt for the cluster an odd observation actually discriminates. Prefer a smaller set of genuinely diagnostic edges with clear reasons over broad topical coverage.
