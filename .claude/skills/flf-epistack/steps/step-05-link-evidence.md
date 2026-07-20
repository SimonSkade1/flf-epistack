# Step 5 — Link observations to hypothesis-clusters

**Output = the evidence layer**, built by **one child per hypothesis-cluster** (orchestrated by step 0), then a final consolidator. You are one cluster-child: for every observation that *discriminates* between **your** cluster's members, mint one `evidence-link` (`E-N`) edge (observation → cluster) with `create_node.py`. You do **not** touch arguments — an argument about a specific observation already names that observation in `affects_observations` (step 3), so the consolidator's script attaches it to the matching edge for you. The consolidator runs that script, then marks a `link_state` on every observation so nothing is silently unconsidered. Step 5 mints **no numbers** — the layer reads with zero weights present; step 8 later fills each edge's likelihood.

## Relevant context

You link existing nodes; you create only `evidence-link`s. The types you read:

1. **observation** (`O`, step 3) — a finding that follows ~with certainty: paper-derived (`generally_known` absent/false, carrying a `data_basis` override or inheriting its source's) or `generally_known` (`generally_known: true`, `data_basis: []`, so — like any empty-basis observation — never correlated). You read `statement` (+ body) and its basis set.
2. **argument** (`A`, step 3) — a `statement`, a `reasoning` body, and its attachments `affects_observations` (`[[O-N]]`, the observations it is about) and `affects_hypotheses` (`[[H-N]]`), at least one non-empty. You never read these yourself; the consolidator's script uses `affects_observations` to wire each argument onto the edges of the observation it names.
3. **hypothesis** (`H`) — the cluster's members; you read each one's `statement` to run the diagnosticity test. `HC.hypotheses` lists only `active` members, so a `state` caveat is moot.
4. **hypothesis-cluster** (`HC`, step 4) — carries `hypotheses`, an ordered list of active members (ascending id, catch-all residual last), mutually exclusive. This is the `to` of every edge.

## Interface

**Consumes.** From step 4: each `HC`'s id, its ordered `hypotheses` list and member statements. From step 3: `O.statement` + body (the cluster-child). Each observation's basis set — its `data_basis` override else its source's `data_basis` — and `A.affects_observations` are read by the **consolidator's scripts**, not the cluster-child. Step 5 reads **no scores** (not trust, usefulness, or validity — step 6 runs after).

**Owns.** The `evidence-link` type entirely (cluster-children); the `correlation-group` (`CG`) type, each edge's `group` and `arguments` lists, and `link_state` on every `O` (the consolidator, via `attach_argument_backlinks.py` + `build_correlation_groups.py` then by hand). Writes no basis field and nothing on argument or hypothesis nodes; modifies no other upstream field.

**Feeds step 6** (arguments): the edges, so step 6 can find the edge each argument about an observation sits on. Step 5 sets no argument state — the script moves an argument to `arguments/orphan/` only when it has no `affects_hypotheses` and none of its `affects_observations` sits on a live edge.
**Feeds step 8** (likelihoods): each edge (`from`, `to`, `arguments` list, `group`, any `## Why this is evidence`), the `correlation-group` (`CG`) nodes, plus `HC.hypotheses` order. A `group` link means step 8 writes **one joint estimate on that `CG` node for the whole group**, never independent factors.
**Feeds step 7** (priors): the edges themselves — step 7 reads the cluster's evidence-links, may mark some `used_for_prior: true` as prior-relevant, and separately reads the cluster's no-observation arguments via their `affects_hypotheses`.

## Spec

### Artifact and layout

1. One markdown file per node (typed YAML frontmatter + prose body), edited in place.
2. **Obs edges** live in `evidence-links/`, prefix `E`. Filename `E-N - <descriptor>.md`, and the descriptor names the two endpoints the child knows at creation — the `from` observation and the `to` cluster: `E-14 - O-14 × HC-1 — youngest ages cluster in the arrival window.md`. (Arguments are attached later by script, so they are not in the filename.) No `title` field; the filename is the title and is fixed at creation (a SKILL.md convention — renaming breaks inbound links).
3. The edge file is the **single canonical record** of an obs edge; endpoints get no mirrored link fields. The edge body embeds its observation (`![[O-N]]`) so it reads standalone; Obsidian backlinks surface every edge on the `O` and the `HC`.
4. **Orphans move, never deleted.** The consolidator gives an observation that is the `from` of no edge `link_state: orphan` and moves it to `observations-and-facts/orphan/`, keeping its `link_state` and `source` link (provenance); the backlink script likewise moves an argument to `arguments/orphan/` (keeping its `source`) only when it has no `affects_hypotheses` and none of its `affects_observations` sits on a live edge.
5. SHOULD: `evidence-links.base` — a derived adjacency view (one row per edge: `id, from, to, arguments, group`), and optionally `correlation-groups.base` (one row per `CG`: `id, to, members`); the notes stay the source of truth. Skip under time pressure.

### Schema — the `evidence-link` node (obs → cluster; the only edge kind)

| field | req | meaning |
|---|---|---|
| type | MUST | `evidence-link` |
| id | MUST | `E-N`; fixed at creation |
| from | MUST | `[[O-N]]` — the observation |
| to | MUST | `[[HC-N]]` — the hypothesis-cluster |
| arguments | OPTIONAL | `[[[A-N]], …]` — the arguments about this edge's observation. **Written by the consolidator's script, not by you** (from each argument's `affects_observations`); leave it absent when you mint the edge. ≥2 allowed; step 8 composes them |
| group | OPTIONAL | `[[CG-N]]` — the `correlation-group` node holding this edge's joint likelihood, set when its observation shares a data basis with other edges into the same cluster. **Written by `build_correlation_groups.py` at consolidation, not by you**; absent for a lone (uncorrelated) edge |
| used_for_prior | OPTIONAL | `true` if step 7 used this edge for the cluster's prior (step 8 then skips it); **written by step 7, absent here** — step 5 never writes it |

Body: the `![[from]]` embed + an optional `## Why this is evidence` — prose naming which members predict the observation differently and which way, written only where that is not obvious from the observation and the member statements. On a **lone** edge, step 8 later appends a `## Likelihood` section; a **grouped** edge's likelihood lives on its `correlation-group` node instead. Leave the rest of the note to step 8.

### Schema — the `correlation-group` node (`CG`; built by the consolidator)

One node per connected group of correlated edges into a cluster, minted by `build_correlation_groups.py` in `correlation-groups/` (never by a cluster-child). It is the single home of the group's joint likelihood.

| field | req | meaning |
|---|---|---|
| type | MUST | `correlation-group` |
| id | MUST | `CG-N`; assigned by the script |
| to | MUST | `[[HC-N]]` — the cluster all members edge into |
| members | MUST | `[[[E-N]], …]` — the ≥2 evidence-links in the group; their `from` observations are what step 8's joint call names |

Body: a one-line note of what the group is; step 8 writes the single `## Likelihood` block here. The script owns the frontmatter and never rewrites the body, so a re-run preserves step 8's block.

### Schema — fields step 5 writes on existing nodes

| field | req | on | meaning |
|---|---|---|---|
| link_state | MUST (consolidator) | every `O` (survivors; not `merged/` tombstones) | `linked` \| `orphan`. `linked` iff the `O` is the `from` of ≥1 edge, else `orphan` → the file moves to `observations-and-facts/orphan/` (nothing deleted). A cluster-child cannot decide this — an observation is an orphan only if *no* cluster linked it, so the consolidator sets it after every cluster-child returns |

The edge `arguments` and `group` fields are also written at consolidation — by `attach_argument_backlinks.py` and `build_correlation_groups.py` respectively (see Process). Arguments carry no `link_state`; an argument's state is just its folder — the script moves it to `arguments/orphan/` only when it has no `affects_hypotheses` and none of its `affects_observations` sits on a live edge.

**Basis set — read by the consolidator, not the cluster-child.** To group correlated edges, `build_correlation_groups.py` resolves each observation's *basis set*: `basis(O)` = `O.data_basis` if the observation carries that override (a step-3 field), else its source's `data_basis` — each a set of `[[D-N]]`/`[[S-N]]` nodes naming the fallible datasets/actors/instruments the finding rests on. A `generally_known` observation rests on no data (`data_basis: []`) and is therefore never correlated. The cluster-child neither reads nor writes any basis field; correlation is entirely the consolidator's.

### Rules

1. **Edge = discrimination, not topical relatedness.** Create an obs → cluster edge iff ≥2 of the cluster's members make materially different predictions about the observation. An observation "about the topic" that every member predicts equally carries no diagnostic weight — leave it unlinked there.
2. **Paper observations are never merged.** Near-duplicate paper observations from different papers stay separate nodes: if they rest on the same data their basis sets share a node and they get flagged correlated; genuinely independent replications rest on distinct basis nodes and correctly count twice. (`generally_known` observations are the exception — resting on no data, the same fact from two papers is one fact, so step 3's consolidation already merged such duplicates into a single node.)
3. **Correlation is the consolidator's job, not yours.** You compute and write no correlation. After every cluster-child returns, `build_correlation_groups.py` connects edges into the same cluster whose observations share a `data-basis` node — following the whole connected component, since basis-set intersection is not transitive — and materialises each component of ≥2 edges as a `correlation-group` (`CG-N`) node, writing `group: [[CG-N]]` onto each member edge. This is the guard that stops step 8 treating correlated observations as independent likelihood factors — the standard way Bayesian aggregation manufactures false confidence.
4. **One edge per (from, to) pair** — no duplicates. An observation may edge into several clusters. Arguments are not your concern here: the script attaches each argument to every edge whose observation it names, so one argument about one observation lands on that observation's edge into each cluster automatically.

### Micro-example

Main question "What drove the extinction of Sahul's megafauna around 45–40 ka?"; cluster `HC-1` "Dominant driver of the megafauna extinction pulse", members in id order `[H-3 direct predation, H-11 indirect human impact, H-21 climate aridification, H-42 residual]`.

1. `E-14` — file `E-14 - O-14 × HC-1 — youngest ages cluster in the arrival window.md`; from `[[O-14 - Youngest reliable ages for 8 of 12 genera fall within ~2 kyr of first occupation]]` → `[[HC-1 - Dominant driver of the megafauna extinction pulse]]`; body embeds `![[O-14 …]]` under `## Why this is evidence` reading "H-3 predicts the youngest ages pile up inside the arrival window; H-21 predicts they track the aridity maximum instead". You mint it with **no `group` and no `arguments` field** — both are added at consolidation: because `O-14` and `O-22` share basis `D-4`, `build_correlation_groups.py` writes `group: [[CG-1 …]]` onto this edge, and because `A-7 - repeated arrival waves widen the window` names `O-14` in its `affects_observations`, `attach_argument_backlinks.py` writes `arguments: [[[A-7 …]]]`.
2. `E-22` — from `[[O-22 - Three genera have reliable ages more than 5 kyr after the arrival window]]` → `HC-1`; minted with no `group`. Both observations derive the basis set `{[[D-4 - Continental late-Quaternary age compilation, group R]]}` through their shared source (the same continental age compilation), so they intersect on `D-4`.
3. `CG-1` — `type: correlation-group`, `to: [[HC-1 - Dominant driver of the megafauna extinction pulse]]`, `members: [[E-14 …]], [[E-22 …]]`; built by `build_correlation_groups.py` in `correlation-groups/` because `E-14` and `E-22` share basis `D-4`. Step 8 writes the pair's single joint `## Likelihood` block on this node, and the runner reads it here.
4. `O-127` — `link_state: orphan`, moved to `observations-and-facts/orphan/`, `source` intact — present-day dietary ecology, which none of the four drivers separate. The argument `A-31 - No comparable extinction pulse is recorded at earlier glacial terminations` (empty `affects_observations`, so it reaches `HC-1` only through `affects_hypotheses`) is left untouched here — it sits on no edge, but step 7 reads it as one of `HC-1`'s no-observation arguments.

### Checks (binary)

1. Every edge sits in `evidence-links/` with `type: evidence-link`, a unique `E-N` its filename begins with (`E-N - <descriptor>.md`), and `from` `[[O-N]]` + `to` `[[HC-N]]` both resolving; the filename names the `from`/`to` ids (not arguments); no (from, to) pair appears twice.
2. No edge references a `merged` or `dropped` hypothesis; every `to` is an existing `HC`.
3. Spot-check 3 edges against rule 1: for each, ≥2 members of the target cluster predict the observation differently — readable off the observation and the member statements, or off the edge's `## Why this is evidence`.
4. After the consolidator runs: every `O` in `observations-and-facts/` (excluding `merged/`) has `link_state`; `orphan` ⟹ the file sits in `observations-and-facts/orphan/` with `source` intact; `linked` ⟹ `from` of ≥1 edge. Every edge `arguments` entry resolves to an `A` whose `affects_observations` contains that edge's `from`; every argument sits in `arguments/` if it has any `affects_hypotheses` or an `affects_observations` on a live edge, else in `arguments/orphan/`. O/A/H/HC counts unchanged vs the earlier steps (nothing deleted).
5. Re-running `build_correlation_groups.py` is a no-op: every `correlation-group` is exactly one connected component (≥2 edges) of same-cluster edges sharing a `data-basis` node, each such edge's `group` points to its `CG` and every other edge has none, and each `CG`'s `members` are those edges. Basis is always `[[D-N]]`/`[[S-N]]` links (no free-text).
6. No step-5-owned field holds a number, probability, weight, or rank; the layer is complete and readable with none present.
7. The `check_missing_evidence_links.py --cluster HC-N` sweep has been run for the cluster; every `(observation, argument)` pair it surfaced is now an edge or a deliberate non-edge (the observation doesn't discriminate).

## Process

The one judgment that matters here is **diagnosticity**: an observation is evidence on your cluster only where its members would predict it *differently* — plain Bayesianism. Evidence consistent with every member has no diagnostic value, and the job is to find and record where the hypotheses come apart, not to pile up items "consistent with" a favoured answer. Work by discrimination, not by topic.

You own one cluster, and two things to do on it:

1. **Edges.** Walk the observations that plausibly touch your cluster's sub-question — the survivors in `observations-and-facts/`, skipping the `merged/` tombstones step 3's consolidation left (use topic to prune — most observations bear on at most one cluster, some on none). For each candidate, run the diagnosticity test: sketch, qualitatively, `P(observation | member)` down the `hypotheses` list. If ≥2 members differ materially, mint the edge (via `create_node.py`); if they'd all predict it about equally, don't — that observation is non-diagnostic *here* (it may still discriminate another cluster, whose child handles it). Where the discrimination isn't obvious from reading the observation against the member statements, write it into `## Why this is evidence`: name which members predict it differently and which way. No numbers — direction only; step 8 prices it.

2. **Missed-edge sweep.** Before you return, run `python3 .claude/skills/flf-epistack/scripts/check_missing_evidence_links.py <analysis-dir> --cluster HC-N` — a "what might I have missed" pass. It lists `(observation, argument)` pairs where an argument ties the observation to a member of your cluster but no `O → HC` edge exists yet. Add the missing edge where the observation actually discriminates (rule 1); otherwise leave it.

You never place arguments or compute correlation — an argument about an observation reaches its edges from its own `affects_observations` (step 3), and correlated edges are grouped by shared basis node; both are wired mechanically by the consolidator's scripts after every cluster-child returns.

**Consolidate — arguments, correlation, then `link_state`, after every cluster-child has returned.** A separate final child does this; a cluster-child does none of it. In order: (1) run `python3 .claude/skills/flf-epistack/scripts/attach_argument_backlinks.py <analysis-dir>` — it writes each edge's `arguments` list from the arguments' `affects_observations` backlinks and moves an argument to `arguments/orphan/` only when it has no `affects_hypotheses` and none of its `affects_observations` sits on a live edge; (2) run `python3 .claude/skills/flf-epistack/scripts/build_correlation_groups.py <analysis-dir>` — it mints the `correlation-group` (`CG`) nodes over connected components of edges sharing a basis and writes each member edge's `group` (this fixed order after step 1 keeps the edge frontmatter stable across re-runs); (3) set `link_state` on every `O` in `observations-and-facts/` (excluding the `merged/` tombstones) — `linked` iff it is the `from` of some edge, else `orphan` — and move each orphan to `observations-and-facts/orphan/` with its `source` intact. Steps 1-3 are global: an observation is an orphan only if *no* cluster linked it.

Judgment left to you: how finely to slice "materially different", when a discrimination is obvious enough to skip the prose, and how hard to hunt for the cluster an odd observation actually discriminates. Prefer a smaller set of genuinely diagnostic edges with clear reasons over broad topical coverage.
