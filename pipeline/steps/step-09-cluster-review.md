# Step 9 — Per-cluster review of the analysis

Write one human-readable review per hypothesis-cluster: the qualitative layer over the computed model, and step 10's source for "what would change my mind" and "limits" (the analysis's explicit gaps).

## Spec

**Orientation.** Steps 1-8 leave a computed model. Each hypothesis-cluster (`HC-N`) is a set of mutually-exclusive member hypotheses (`H-N`) answering one sub-question — usually including a `residual` member ("none of the listed answers") so the set is exhaustive — and the runner turns the cluster's prior and likelihood `python` blocks into a **posterior**: a probability vector over those members, in `HC.hypotheses` order (`python3 runner/run.py <analysis-dir>` prints `HC-N  prior [...]  posterior [...]` per cluster). Step 9 steps back from the arithmetic and writes, per cluster, one short document a human reads: what the analysis concluded and why, then the things the block form cannot hold — where the carving or reasoning may be structurally wrong, what information would sharpen it and whether that is gettable, and where the evidence is confusing or contradictory.

**Two boundaries.**

1. **Each review stays inside its own cluster.** Synthesising across clusters and pricing the main question is step 10's job; done in both places you get two answers that drift.
2. **Step 9 changes nothing the model reads** — no number, no field on an existing node, no `python` edit, no generated file. A defect it names is fixed by re-running the step that owns it (a wrong likelihood → step 8, a wrong prior → step 7, a mis-carve → step 4). The reviews are a new, read-only layer.

### Artifact

One review per active cluster (every `HC-N` file in `hypothesis-clusters/`), living **beside its cluster** in `hypothesis-clusters/`, named `Analysis of HC-N - {rest of HC-N's title}.md` — e.g. `HC-1 - Dominant driver of the megafauna extinction pulse.md` gets `Analysis of HC-1 - Dominant driver of the megafauna extinction pulse.md`. It is not an id'd graph node: no `CR-` prefix, no separate folder. The body is the four parts below and is the whole artifact — no index, no register, no script.

**Create the file with a shell heredoc, not the `Write` tool.** When step 9 runs as a subagent (the normal case — one child per cluster), `Write` refuses this file with "Subagents should return findings as text, not write report files", because a prose `.md` looks to the harness like a report the child should have returned instead. That refusal is spurious here: the review *is* this step's deliverable, not a status write-up. A child that accepts the error produces **no artifact at all** and the run silently completes a cluster short. So write it as:

```
cat > "<analysis-dir>/hypothesis-clusters/Analysis of HC-N - {rest of title}.md" << 'EOF'
---
type: cluster-review
...
EOF
```

Quote the delimiter (`<< 'EOF'`) so backticks, `$` and python in the body are not interpolated. Verify with `wc -w` on the path afterwards.

| field | req | meaning |
|---|---|---|
| `type` | MUST | `cluster-review` (no `id` — the file is not an id'd node; it is located by its `Analysis of HC-N …` name beside the cluster) |
| `cluster` | MUST | one `[[HC-N …]]` wikilink — the cluster this reviews, 1:1 |

### The document — four parts, all MUST, all prose

Use the four names as the body's section headers.

1. **What the analysis says** — the cluster's question, its members, where the prior started and where the posterior landed, and which observations and arguments did the updating work. Quote the model's numbers; mint none. A reader who will not open a `python` block should finish this part knowing what the cluster concluded and on what.
2. **What the model may not capture** — the structural doubts the blocks cannot express: whether the members are carved right, are really mutually exclusive, or plausibly miss one; where a variable is a proxy for something it doesn't quite measure; where a reference class was picked for availability rather than fit; where the reasoning may simply be wrong; which counterarguments were probably never presented because the sources that would make them are motivated. Model uncertainty gets argued here, not scored.
3. **What would help** — the information that would most sharpen this cluster, each labelled *exists, unread* · *exists, inaccessible* · *does not exist* · *unclear*, ordered by how much it would change the picture.
4. **Confusions and contradictions** — where two pieces of evidence point opposite ways and the analysis papered over it, where the literature disagrees irreducibly, where you cannot tell what is going on. Part 2 says *the model may be built wrong*; part 4 says *I cannot tell what is true here*. If you can name the fix, it belongs in 2 or 3.

**Optionally — external consensus (MAY, its own short section).** What the field currently believes about this cluster's question, set beside where the posterior landed, with any divergence flagged: an analysis that lands far from the mainstream is either seeing something or missing something, and saying which is the point. Write it only *after* the four parts are done — consulting the consensus first anchors the whole review to it — and let it enter no number and no frontmatter field.

### Rules

1. **Name the node where there is one** (SHOULD) as a full wikilink, not a bare id, so its backlinks gain a "this was questioned" view. **Deliberately not a MUST:** the doubts this step exists to collect are often exactly the ones with no node to name — that the framing is wrong, that the field's incentives shaped what got published at all, that a whole class of evidence was never gathered. Forcing those to anchor to whatever id sits nearest either distorts or loses them, and losing them is this step's failure mode. Say it plainly instead.
2. **Stay inside the cluster** (MUST). No claim about the main question, no ranking against other clusters, no verdict.
3. **Length follows weight.** A cluster the answer turns on earns 400-800 words; a peripheral one earns three honest sentences.
4. **Quote the model's numbers, mark your own** (MUST). A number attributed to the analysis is the model's — a block's own value, or a run of it. Your own rough magnitudes are allowed and are often the point ("perhaps a third of the relevant excavation reports were never digitised" is a real thing to know and lives nowhere in the model), but write them as your estimate and let them enter no computation. A number worth putting *into* the analysis is a step-7/8 block edit, i.e. a re-run.
5. **Say so when a defect is being shipped unfixed** (SHOULD) — a named weakness is worth more to step 10 than a smoothed-over one.
6. **Ask whether the true answer is on the list at all** — as a standing question in part 2, not only when a number trips a threshold. A mutually-exclusive member set can still be collectively wrong; this is where out-of-model / unknown-unknowns mass gets argued rather than sanded off. Argue it from outside the members' shared framing, and say whether an unlisted answer would be more, less or equally consequential than the listed ones — an unlisted answer can be worse than every listed one, and then a small probability is not a small risk. It is *most* worth asking where the arithmetic looks comfortable and so nobody thinks to; it is unmissable where a posterior entry sits within ~1e-3 of 0 or 1, past which the arithmetic has stopped being the binding uncertainty at all.

### Micro-example (compressed, numbers illustrative)

The review of `HC-1` "What was the dominant driver of the Sahul megafauna extinction pulse (~45–40 ka)?" — file `Analysis of HC-1 - Dominant driver of the megafauna extinction pulse.md` — members `H-3` direct predation · `H-11` indirect human impact · `H-21` climate aridification · `H-42` residual.

```yaml
---
type: cluster-review
cluster: "[[HC-1 - Dominant driver of the megafauna extinction pulse]]"
---
```

#### What the analysis says

The prior favoured a human driver but left climate a real share. One correlated observation pair does all the updating, estimated jointly because both rest on the same age compilation; it pulls toward indirect human impact. Climate is where the prior does the most work relative to the evidence: [[A-31 - No comparable extinction pulse at earlier glacial terminations]] cut its weight before any observation was read.

#### What the model may not capture

`H-3` and `H-11` split one branch on a judgment with no reference class, which the two posterior entries hide. Their asserted exclusivity is doubtful if arrival and aridity interacted — the blocks cannot say "partly both". [[A-31 …]] was trusted without its inference traced, and absence-of-record is weak evidence where the earlier terminations have far worse dating — the largest unchecked step in this cluster. Could the driver be one nobody listed (e.g. disease)? The residual holds only a small share, but nothing outside the human/climate framing was actually weighed.

#### What would help

The age compilation's full screening protocol, with the ages it excluded — *exists, inaccessible*. A trace of [[A-31 …]]'s inference against the earlier-termination record — *exists, unread*. Whether `H-3` and `H-11` are separable at all — *does not exist*.

#### Confusions and contradictions

One observation reads as slow-habitat-squeeze evidence, another as a rapid-kill signal, and both rest on the same compilation. Judging them jointly is right, but the single joint likelihood states P(both | H) and so cannot show *which half* of the pattern each member fits. Unfixed at submission, deliberately; the honest fix is prose in the block's comment, not a second estimate.

### Checks (binary)

1. One review per active cluster; each `cluster` resolves to a distinct existing cluster.
2. All four parts present and non-empty in every review.
3. Every wikilink resolves, and every point that *is* about a specific node names it (points about the cluster as a whole, the framing, or the literature need no id).
4. Every part-3 label is one of the four; no review names the main question or another cluster's verdict; every number attributed to the analysis is reproduced by the model, and every other number is marked as the reviewer's own.
5. The runner's posteriors are byte-identical before and after step 9.

### Interface

**Consumes (read-only).** The cluster's prior/likelihood blocks and the posteriors they produce, plus the per-hypothesis prose beside them (what would have to be true, the reference class, what the number doesn't cover, confidence versus the other members) — this is part 2's raw material. For finding weaknesses also read: motivated and non-curated sources; arguments accepted as sound without their inference traced; observations that failed to discriminate (orphaned) and correlated-observation groups; the cluster's dropped members, its residual, and whether it was built exhaustive; and any external consensus the sources make legible, for the optional section above (it enters no number).

**Produces for step 10.** The reviews. Step 10 synthesises across clusters, prices the main question, links deciding clusters' reviews among its ≤10 entry points, and owns KB-wide issues that belong to no single cluster (source selection, the run's exclusions, overall scope). It summarises and cites each review rather than re-deriving it. Step 9 supplies no sensitivity number, no headline, no threshold, and none is owed.

**Owns.** The per-cluster review file and nothing else — no field on any existing node, no generated file, no script.

## Process

1. **Read the computation before doubting it.** Open the cluster: its members and their prose, the prior and likelihood blocks, and the posterior the runner prints. Then read the nodes the blocks lean on — the observations and arguments named as variables, their evidence-links and sources. You are reviewing one specific calculation; know exactly what it did first.
2. **Write part 1 as translation, not summary.** Say what the cluster concluded in words a reader who won't open `python` can hold: where the prior sat, where the posterior landed, and the one or two items that moved it. Find the movers by looking at which likelihoods deviate most from flat and which prior adjustments were largest — naming them makes the drivers visible, and they are what parts 2-4 should mostly interrogate.
3. **Run parts 2 and 4 as adversarial self-review** — assume the model is wrong and find where. Borrow whatever helps, skip the rest:
	1. *Key-assumptions check:* list the few assumptions the posterior rests on and ask which, if false, flips it — the members are exclusive, the reference class fits, the trusted argument's inference holds, the reliability discount stands in for a screening protocol nobody read.
	2. *Premortem:* imagine this cluster's answer turned out wrong and write the most likely story of how. It usually names a structural fault — a mis-carve, a proxy variable, a motivated-source blind spot — that belongs in part 2.
	3. *Is the answer on the list?* A mutually-exclusive member set can still be collectively wrong. Argue this from outside the members' shared framing; ask it even — especially — when the arithmetic looks settled. The residual member nominally holds this probability, but its value is a guess, so keep the question live regardless of what the block assigns (rule 6).
	4. *Motivated sources cut twice:* they lower data-trust and bias which arguments got presented at all, so the real gap is often the counterargument no source in the set had an incentive to make. Read the non-curated and motivated sources for what the curated set omits.
4. **Keep part 4 for genuine irreducible conflict** — two well-supported observations pointing opposite ways, a literature that won't converge, a pattern you can't read. Don't manufacture contradictions to fill the section, and don't paper over real ones to keep part 1 clean; anything with a nameable fix is a part-2 or part-3 item instead.
5. **Calibrate and stay honest.** Spend words where being wrong costs most (rule 3). Mark every number you introduce as your own estimate (rule 4). Name defects you're shipping unfixed (rule 5). If the review convinces you a number or field is wrong, that is a re-run of the owning step, not an edit here — record the doubt and move on. Optionally, once the four parts are written, set the field's current consensus beside the posterior and flag any divergence — after, never before, so it does not anchor the review.

Failure modes: re-scoring instead of reviewing (a new probability belongs in a block, not in prose); anchoring every doubt to a node id when the doubts that matter most have none (rule 1); drifting into step 10 (no cross-cluster ranking, no main-question claim, no verdict — rule 2).
