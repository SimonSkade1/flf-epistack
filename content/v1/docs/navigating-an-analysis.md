---
title: "How to navigate an analysis"
---

*Written after the submission deadline.* This page was added afterwards as a reading guide for the published runs; it is not part of the submitted entry, changes nothing in any analysis, and replaces three unfinished draft pages that stood here. The entry itself is [[submission|the submission document]], and the method is published step by step at [[v1/pipeline/index|the pipeline]] — this page is about reading the output, not producing it.

One run is used throughout: `analysis-tests/black-holes1`, which asks [[main report - Was the risk that LHC collisions destroy the Earth truly put to rest and what does that conclusion hinge on|whether the risk that LHC collisions destroy the Earth was truly put to rest, and what that conclusion hinges on]]. Every number, id and filename below was re-checked against that run's files and against `run.py` while writing.

## 1 — What you are looking at

An analysis is one directory of markdown notes. Each note is one typed node, each frontmatter wikilink is one typed edge, so the directory *is* a directed typed graph. black-holes1 holds 83 markdown files, 72 of them graph nodes: 5 curated sources and 18 non-curated, 2 data-bases, 6 linked observations and 4 orphaned, 10 hypotheses, 4 clusters plus 4 cluster reviews, 9 evidence links, 2 correlation groups, 7 arguments, and the main report. The other 11 are the run's input and its own logs.

The structural fact to hold onto before clicking anything: **no conclusion is stored anywhere in the graph.** No posterior, prior or likelihood sits in frontmatter. What the notes store are inputs — one prior over each cluster's members, one likelihood per piece of evidence — written as small python blocks inside the notes. The answer is recomputed from those on demand. So "check this number" and "change this number and see what happens" are the same operation, and no cached figure can silently go stale behind an edit.

## 2 — The folders are the node types

| prefix | type | lives in | what it is |
|---|---|---|---|
| `S-N` | source | `sources/`, dropped ones in `sources/non-curated/` | one paper or dataset; carries `trust_score` and `usefulness` |
| `D-N` | data-basis | `data-bases/` | a dataset, instrument or premise that several findings share |
| `O-N` | observation | `observations-and-facts/`, non-discriminating ones in `observations-and-facts/orphan/` | a finding that follows ~with certainty from a source's data |
| `H-N` | hypothesis | `hypotheses/` | a candidate answer; `residual: true` marks the "something not listed here" member |
| `HC-N` | hypothesis-cluster | `hypothesis-clusters/` | one sub-question and its mutually-exclusive answers; carries the `## Prior` block |
| `Analysis of HC-N` | cluster-review | `hypothesis-clusters/` | the prose review of one cluster: what moved it, what it may miss, what would help |
| `E-N` | evidence-link | `evidence-links/` | one observation → one cluster edge; carries a `## Likelihood` block unless it belongs to a group |
| `CG-N` | correlation-group | `correlation-groups/` | one *joint* `## Likelihood` for several edges resting on the same data-basis |
| `A-N` | argument | `arguments/` | an inference or calculation, judged for validity alone: `approved` / `corrected` / `rejected` |
| `main report - …` | main-report | the run's root | the answer to the main question |

Three conventions make the folder listing itself informative:

1. **Nothing is deleted, only moved.** A source that lost the curation cut, an observation that discriminated no cluster, a merged or dropped hypothesis — each keeps its content and its links in a sub-folder, with the reason recorded. `sources/non-curated/` is where you look to find out what the run decided *not* to use.
2. **The reviews sit beside the clusters they review.** `Analysis of HC-1 - …` and `HC-1 - …` are the same sub-question in two registers: prose and numbers.
3. **The remaining files are not graph nodes.** `initial_prompt.md` is the run's input (the question, the scope, `curated_target_N`); `problem-log.md` and `agent-notes/` are the run's record of its own faults and decisions, appended by the agents as they went.

## 3 — Top-down: from the answer to the data it rests on

The intended reading direction is downwards. Each step below is a real note in black-holes1.

1. **The report.** [[main report - Was the risk that LHC collisions destroy the Earth truly put to rest and what does that conclusion hinge on|The main report]] answers the question and then lists its own entry points. Its verdict is a conjunction of three conditional clusters — a hole probably never forms (HC-3), if it forms it evaporates (HC-2), if it fails to evaporate and is trapped it is still harmless (HC-1) — and its actual finding is about pedigree rather than probability: nearly every empirical likelihood in the run routes through one paper.
2. **The cluster review.** [[Analysis of HC-1 - Fate of a stable LHC black hole trapped in Earth|Analysis of HC-1]] takes the cluster the question really turns on and says in prose what moved it, what it cannot express, and what would help. Read it before the cluster; it is where the model's own limits are stated, including the admission that the two evidence items are "closer to one item than two".
3. **The cluster.** [[HC-1 - Fate of a stable LHC black hole trapped in Earth|HC-1]] holds three mutually-exclusive members in a frozen order — [[H-1 - Stable LHC black holes trapped in Earth would accrete it catastrophically within the solar lifetime|H-1 catastrophic]], [[H-2 - Stable LHC black holes pose no macroscopic risk to Earth within the solar lifetime|H-2 harmless]], [[H-6 - Stable LHC black holes have some fate or impact not listed here|H-6 residual]] — plus its `## Prior` block. Every probability vector printed for HC-1 is in that order. The prior is deliberately evidence-blind: `w_no_risk = 1.0` as anchor, `frac_log_range_fast = 0.35` (the fraction of the plausible log-timescale range falling below the 5 Gyr cutoff) giving `w_danger`, and `w_residual = 0.2` argued in its own right rather than taken as `1 − sum(others)`. That normalises to `[0.3097, 0.5752, 0.115]`.
4. **The evidence.** Two blocks update HC-1: [[CG-1 - HC-1 joint over O-2+O-3+O-4|CG-1]], one joint likelihood over three observations, and the lone edge [[E-1 - O-1 × HC-1 — old low-field white dwarfs observed intact|E-1]]. Both set the danger member at 0.1 against a 1.0 anchor on H-2, and both cap `t` at 0.74.
5. **The edge and its observation.** [[E-3 - O-3 × HC-1 — super-LHC cosmic-ray exposure of Earth, WDs and NSs|E-3]] states in prose why [[O-3 - Cosmic rays far above LHC-equivalent energy continuously bombard Earth, white dwarfs and neutron stars|O-3]] discriminates — under H-1, nature already ran vastly more super-LHC collisions on these bodies, so their survival is surprising; under H-2 the same exposure is harmless. E-3 carries no python: it has a `group` field pointing at CG-1, where its number lives.
6. **The data basis.** O-3's `data_basis` names [[D-1 - Cosmic-ray survival premise - high-energy cosmic rays have bombarded astronomical bodies over Gyr without catastrophe|D-1]], the shared premise that ultra-high-energy cosmic rays have struck astronomical bodies for Gyr without catastrophe. Its `known_biases` field names the common-mode failure explicitly: cosmic-ray-produced states are relativistic and escape, while collider-produced ones can be slow and trapped. If that mapping fails, everything resting on D-1 fails together.
7. **The source.** O-3's `source` is [[S-1 - Astrophysical implications of hypothetical stable TeV-scale black holes|S-1]] (Giddings–Mangano 2008), `trust_score: 0.74`, docked for model-dependent accretion assumptions and for a CERN co-author's institutional stake in a no-risk conclusion. That 0.74 is the cap on `t` in both blocks named in item 4, which is how a judgment about a *paper* becomes a bound on how far its data may move a posterior.
8. **The repair the chain depends on.** E-1 and E-3 both list [[A-1 - Relativistic-escape loophole in the Earth cosmic-ray argument is closed by white-dwarf and neutron-star stopping power|A-1]] (`approved`) in `arguments`: it closes the loophole in the naive cosmic-ray argument, that cosmic-ray-produced holes are relativistic and simply escape, by way of white-dwarf and neutron-star stopping power. Pulling the other way, CG-1's likelihood comment invokes [[A-6 - Observer selection makes naive survival-based risk bounds uninformative|A-6]] (`corrected`) to dock O-4: Earth's and the Sun's own survival cannot bound a catastrophe rate at all, since we could not have observed the branch where it fired, though distant independently observed bodies keep most of their force. Between them the weight ends up on white dwarfs and neutron stars rather than on "we are still here" — and you can read that conclusion off the argument nodes rather than having to take it on faith.

Going the other way works too. Every node's **backlinks** panel is its inbound edge set: open S-1 and you see the observations extracted from it; open D-1 and you see everything that would fail with it.

## 4 — The one idea to take away: correlated evidence is counted once

This is the pipeline's central claim, and CG-1 is the concrete instance.

O-2 (intact Gyr-old neutron stars), O-3 (the cosmic-ray exposure record) and O-4 (Earth and Sun surviving 4.5 Gyr) all name D-1 in their `data_basis`. Step 5 therefore joins their three edges — E-2, E-3, E-4 — into one connected component, and step 8 writes **one** `## Likelihood` block for the whole pattern on [[CG-1 - HC-1 joint over O-2+O-3+O-4|CG-1]]: a single `evidence("HC-1", ["O-2", "O-3", "O-4"], …)` call stating P(all three | member) jointly, at `lik = [0.10, 1.0, 0.55]`, `t = 0.74`.

The alternative — three separate factors of ~0.1 against the danger member — is the standard way Bayesian aggregation manufactures false confidence. Here the three "reassurances" are one witness: the same premise seen from three angles. The folk version of the safety case (O-4: Earth and the Sun are still here after 4.5 Gyr of bombardment) sits *inside* that group rather than beside it as extra support, which is exactly what a source-tally gets wrong. Counting the three as independent updates would have compounded the same odds factor three times over instead of once, for free.

The mechanism is mechanical, not rhetorical, and you can watch it decide: [[O-1 - White dwarfs of about one solar mass with Gyr ages and low magnetic fields are observed intact|O-1]], the white-dwarf datum, lists a *different* basis in `data_basis` — [[S-10 - Spectropolarimetric survey of hydrogen-rich white dwarf stars|S-10]], the spectropolarimetric survey the catalogued white dwarfs come from — so its edge E-1 stayed outside CG-1 and got its own block. That is why HC-1 shows "2 evidence block(s)" over four edges.

Then the honest half, which [[Analysis of HC-1 - Fate of a stable LHC black hole trapped in Earth|the cluster review]] states against itself: CG-1 and E-1 still both rest on S-1's stopping-power and accretion machinery. The correlation group catches a shared *data basis*; it does not catch a shared *analysis*. If A-1's kinematics or A-2's density scaling fails, both blocks fail together — so the split into two edges overstates independence, and the review says so rather than letting the arithmetic imply otherwise.

## 5 — How the numbers compose

Two kinds of python block exist, and nothing else runs.

1. A **`## Prior`** block on each `HC-N` builds one strictly-positive relative weight per member out of named variables, each carrying its reasoning in the comment beside it, and ends in `prior(hc, w)`. The runner normalises.
2. A **`## Likelihood`** block on each `E-N` (or once per `CG-N`) states P(observation | member) for every member, anchored at 1.0 on the member under which the observation is unsurprising, and ends in `evidence(hc, obs, lik, t)`. `t ∈ [0, 1]` is how far the data's reliability lets this evidence carry you off the prior, capped by the source's `trust_score`.

`pipeline/runner/run.py` reads every note in the directory, extracts these blocks, and for each cluster multiplies each member `i` by `t·lik[i] + (1−t)·marg`, where `marg` is the prior-weighted average likelihood. Equivalently, `posterior = t·(posterior at t=1) + (1−t)·prior`. Two consequences worth knowing while reading: `t = 0` means the evidence does nothing, and because the mixture anchors on the prior rather than on the running posterior, a cluster's edges commute — the order the runner happens to read files in cannot change an answer.

HC-1 in full, at prior `[0.3097, 0.5752, 0.115]`:

```
CG-1: marg = 0.6695 → factors [0.2481, 0.9141, 0.5811]
E-1:  marg = 0.6752 → factors [0.2496, 0.9156, 0.6196]
```

Multiply through and renormalise and you get `[0.0354, 0.8882, 0.0764]` — reproducible on a pocket calculator from the two likelihood vectors and the two `t` values, both of which you can read straight off the notes. In odds terms the two blocks together cut H-1 against H-2 by 13.5×, not the 100× that two likelihood ratios of 0.1 would give unattenuated; the 0.74 trust cap absorbs the difference.

Determinism is enforced rather than hoped for: blocks are arithmetic over named variables plus the two registrar calls, with `import`, `open`, `eval`, `exec` and dunder access rejected, and no randomness, clock or I/O available. The same notes always give the same numbers.

## 6 — Re-pricing any number yourself

Run the whole model. It needs only python 3 and the repository:

```
python3 pipeline/runner/run.py content/v1/analysis-tests/black-holes1
HC-1  prior [0.3097, 0.5752, 0.115]  posterior [0.0354, 0.8882, 0.0764]  (2 evidence block(s))
HC-2  prior [0.891, 0.109]  posterior [0.9561, 0.0439]  (2 evidence block(s))
HC-3  prior [0.03, 0.94, 0.03]  posterior [0.03, 0.94, 0.03]  (0 evidence block(s))
HC-4  prior [0.504, 0.496]  posterior [0.7615, 0.2385]  (1 evidence block(s))
```

One line per cluster, members in `HC.hypotheses` order. HC-3 having zero evidence blocks is not a bug: its single edge was consumed inside the prior, which the block records.

Now disagree with something. `--set BLOCK:var=value` rewrites one named variable and recomposes everything downstream of it. The interesting target here is the single-source dependency the report itself flags — S-1's 0.74 trust caps both `CG-1:t_survival` and `E-1:t_wd`, so those two flags price the entire empirical layer of this cluster at once:

```
python3 pipeline/runner/run.py content/v1/analysis-tests/black-holes1 --set CG-1:t_survival=0.3 --set E-1:t_wd=0.3
HC-1  prior [0.3097, 0.5752, 0.115]  posterior [0.1663, 0.7318, 0.1019]  (2 evidence block(s))

python3 pipeline/runner/run.py content/v1/analysis-tests/black-holes1 --set CG-1:t_survival=0.0 --set E-1:t_wd=0.0
HC-1  prior [0.3097, 0.5752, 0.115]  posterior [0.3097, 0.5752, 0.115]  (2 evidence block(s))

python3 pipeline/runner/run.py content/v1/analysis-tests/black-holes1 --set CG-1:t_survival=1.0 --set E-1:t_wd=1.0
HC-1  prior [0.3097, 0.5752, 0.115]  posterior [0.005, 0.9334, 0.0616]  (2 evidence block(s))
```

Reading those three: distrusting Giddings–Mangano down to 0.3 multiplies the danger member by 4.7, from 0.0354 to 0.1663. Distrusting it entirely returns the prior *exactly*, which is the check that the whole empirical contribution really does flow through that one paper and is not leaking in somewhere unlabelled. Trusting it completely gives 0.0050 — so the full span of defensible opinion about one source's reliability is a factor 33 in the headline danger figure.

The same handle works on priors. `--set HC-1:frac_log_range_fast=0.6` moves the run's most-admitted guess from 0.35 to 0.6 and takes the posterior danger mass from 0.0354 to 0.0669 — roughly linear, exactly as the cluster review predicts. That is the intended use of the whole artifact: locate the one step you disagree with, re-price it, and see what it was worth.

## 7 — Moving around

1. **Backlinks** (right rail) are the inbound edge set of whatever you are reading. On a source they are its extractions; on a data-basis they are its dependants.
2. **The graph** colours nodes by their `type:` field, and hovering a node shows its own title plus the titles of everything it links to, so a neighbourhood is readable without clicking. `Ctrl`/`Cmd`+`G` opens the full-screen graph, which adds per-type filter chips with counts: hide `source` and `other` and what remains is the reasoning skeleton — observations, hypotheses, clusters, edges, arguments.
3. **In-text links are tinted by the folder their target lives in**, so you can see what kind of thing a link leads to before following it. One gap to not over-read: a cluster-review lives beside the cluster it reviews, in `hypothesis-clusters/`, so its links carry the cluster colour rather than its own. The graph reads the `type:` field directly and colours reviews correctly.

<ul class="node-legend">
<li class="node-source">source</li>
<li class="node-data-basis">data-basis</li>
<li class="node-observation">observation</li>
<li class="node-hypothesis">hypothesis</li>
<li class="node-hypothesis-cluster">hypothesis-cluster</li>
<li class="node-evidence-link">evidence-link</li>
<li class="node-argument">argument</li>
<li class="node-cluster-review">cluster-review</li>
<li class="node-main-report">main-report</li>
</ul>

## 8 — Read these as a demonstration of method, not as answers

The published runs are low-N shakedown runs. black-holes1 ran at `curated_target_N = 5`: 23 sources were scored, 18 cleared the trust baseline of 0.6, and the top 5 were curated. Everything above is real and recomputes, and it is still a thin evidence base. Three specific things to keep in view while reading it:

1. **The curation cut shapes the answer more than any likelihood does.** S-1, the paper the whole empirical layer routes through, finished only 7th of 23 by `combined_score` (0.59) and was swapped in over the 5th-ranked source because a script flagged that D-1 — the cosmic-ray premise the question turns on — would otherwise have had no curated source at all. In the other direction, Plaga's metastable-black-hole paper (`S-16`, `trust_score: 0.40`, `usefulness: 4.0`, `combined_score: −0.80`), the strongest published challenge to exactly the accretion machinery this cluster rests on, sat below the trust floor and never entered the graph. The LSAG report, the document that publicly put the risk to rest, cleared the floor but finished 18th of 23 (0.10, trust 0.63 as a synthesis), so the run reconstructs its case from its primary inputs instead. All of them are in `sources/non-curated/`, with the full ranking in `agent-notes/curation.md`.
2. **What is missing is visible but not priced.** Strangelets and vacuum decay are named in the question and never became clusters at N=5. [[O-9 - Hawking radiation has never been experimentally observed from any black hole|O-9]] sits in `observations-and-facts/orphan/`: the graph's most safety-relevant negative fact touched no likelihood, because the evaporation argument was taken on trust rather than traced. Orphan status means "discriminated nothing", not "consistent with everything" — the pipeline refuses to count a non-discriminating observation as support.
3. **The residual is a real competitor, not a remainder.** H-6 ends at 0.0764 on an argued weight of 0.2 and likelihoods of 0.55 and 0.6 — and the review concedes that sub-catastrophic fates would look observationally identical to full safety in every observation used here, so the evidence cannot separate them. That is the model reporting the shape of its own blind spot.

The defects the three runs exposed are collected in [[APPENDIX - known failure modes|the known-failure-modes appendix]] — 3 BLOCKERs and 33 MAJORs, each logged by an agent inside the run that hit it, including one defect claim a run later retracted. Reading that first is a reasonable way to calibrate how much to believe of anything else here.
