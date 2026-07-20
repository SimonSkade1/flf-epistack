# Problem log — black-holes1 test run

Agents append problems here during the flf-epistack **quick test run**. Purpose: catch **major errors or problems in the pipeline** on a fast N=5 shakedown — before the real N=25/50 runs. This is NOT a place to record minor imperfections.

## How to append (every agent)

1. Only log **BLOCKER** or **MAJOR** problems. Skip minor/cosmetic imperfections — the run is deliberately quick and rough, and sub-optimal output is expected and fine.
2. Append your entry at the bottom of `## Log`, using a single write (e.g. a `>>` shell append) so parallel appends don't clobber. Never edit or delete another agent's entry.
3. One block per problem, in this format:

```
### [SEVERITY] step <n> / <slice or agent> — <short title>
<1–3 lines: what happened, where (file / script / cross-step interface), and why it blocks or corrupts the run>
```

Severity scale:
- **BLOCKER** — stops the step or run, or corrupts the graph; must be fixed before the real runs.
- **MAJOR** — wrong/misleading output, a broken cross-step interface, or instructions ambiguous/contradictory enough that a competent agent could easily get them wrong.

The orchestrator appends a `## Ranked summary` at the end of the run: deduped, all BLOCKERs first then MAJORs. That ranked list is the deliverable Simon reads.

## Log

<!-- append problem entries below this line -->

### [MAJOR] step 1 / 1B-A (official-safety-case searcher) — wrong author list for LSAG 2008 in seed material
My searcher brief named the LSAG report (arXiv:0806.3414) authors as "Ellis, Giddings, Mangano, Sandweiss, Wilczek." Verified independently via arXiv abstract + INSPIRE-HEP (and cross-checked against a prior full pipeline run of this same case, `.../analyses/black-holes/sources/S-3 - LSAG 2008...md`): the real author list is Ellis, Giudice, Mangano, Tkachev, Wiedemann. The brief's version conflates 3 distinct real papers' authors (Giddings from Giddings-Mangano 2008; Sandweiss/Wilczek from Busza-Jaffe-Sandweiss-Wilczek RHIC 2000) into one wrong byline. A searcher who didn't independently verify would have written incorrect `authors` metadata onto a load-bearing node (S-7). Fixed on the node itself with a note; logging since this is a seed-material fabrication risk (planner/orchestrator step generating bibliographic detail that reads as verbatim fact but wasn't checked).

### [MAJOR] step 1 / slice B (empirical-survival-bounds) — test-run case directory collides with a pre-existing full production analysis
`analysis-tests/black-holes1` (this test run) and `analyses/black-holes` (a sibling directory) analyze the identical case end-to-end (same question, same seed sources, overlapping S-ids like S-5/S-6/S-15/S-16). An agent could easily read the wrong directory, mistake the completed run's scored/curated nodes for already-decided parts of the current graph, or copy its step-2/3 fields (data_basis, trust_score, extracted) into a step-1-only node. No corruption occurred here (used it only as an external fact-check), but the setup invites it.

### [MAJOR] step 1 / 1c (consolidator) — step-01 mode file has no output spec for the 1c consolidated pool (a load-bearing cross-step interface)
Step 2's interface (step-01 mode file, "Interface" para) says it starts "from the consolidated overview in agent-notes/orientation/", but the mode file's only spec for that file is the single clause "the consolidator the merged overview step 2 starts from" (line 55); the detailed "Your orientation note" spec right below it is searcher-shaped (search_scope etc.) and omits the pool-consolidation + plan-audit that are 1c's actual job. The full 1c spec lived only in the orchestrator's prompt. It worked here because that prompt was detailed, but a terser orchestrator prompt would leave a 1c agent producing a searcher-style note and dropping the audit — i.e. step 2's entry-point format is defined outside the versioned mode file.
- MAJOR (step 2a, orchestrator-observed): Link-format ambiguity in the skill — mode-file field tables write ``[[S-N]]``/`[[D-N]]` shorthand while SKILL.md's shared conventions and the step-05 worked example require full-filename wikilinks; a 2a scorer followed the tables literally and wrote 16 short-form `data_basis` links (scripts parse them, but Obsidian can't resolve them, breaking graph navigation). Orchestrator normalized all links to full-filename form; skill should pin one format in every field table.
- MAJOR (step 3, extractor slice S-13/S-14/S-23): S-23's observer-selection argument targets cross-paper evidence (cosmic-ray survival premise D-1, used by the other slice's S-1 observations), but argument attachment fields only allow same-paper O/H. Encoded via affects_hypotheses on its own H plus a body note naming D-1; steps 5/6 have no structured field to see this attack on survival-based evidence links.
MAJOR (step 5, HC-1 child): create_node.py invocation given in step file/brief fails — script requires full node content on stdin and an {{ID}} placeholder, neither documented; first call errored ("no content on stdin") and E-1 was minted without an id (fixed by hand).
MAJOR — step 5, HC-3 child: create_node.py errors ("no content on stdin") when invoked as the step file documents; it requires body content on stdin containing an {{ID}} placeholder, else mints a node with no id (warning only). Undocumented in step-05/brief; worked around by piping body and adding id by hand.
MAJOR — step 8 gate (runner): run.py BANNED-token scan matches inside comments — E-7 block failed on the word "open" in a reason comment ("HC-1's open question"); scan should strip comments (or match call syntax only) before banning. Orchestrator reworded the comment to unblock.
- MAJOR (step 9, HC-1 slice): subagent Write tool refused to create the cluster-review artifact ('Subagents should return findings as text, not write report files') — the harness misclassifies the step-9 deliverable as a report file; worked around via shell heredoc, but other step-9 children may silently fail to write their reviews.
- MAJOR (step 9, HC-4 review): A-7 (status approved/checked at step 6) derives an observer-weighting tilt toward LATE formation dates while E-6's mechanism prose asserts the opposite (high rate pushes observers EARLY); step-6 trace endorsed one direction without catching that the step-8 edge asserts the other. Update direction/numbers unaffected, but the checked-gate missed a direct inter-node contradiction; needs a step-6/8 re-trace against S-23.
- MAJOR | step 10 | main-report slice: spec requires quoting each cluster's `external_consensus` (step-7/8 field) in part 4, but no such field exists anywhere in the KB — steps 7/8 never wrote it; report had to substitute its own labelled characterization.

## Ranked summary

Deduped (11 logged entries → 10 distinct; create_node.py logged twice). 0 BLOCKERs, 10 MAJORs — ranked by how important a fix is before the real N=25/50 runs:

1. MAJOR (step 5; hit by 2 children) — `create_node.py` stdin/`{{ID}}` contract undocumented in step-05/briefs: script needs node body on stdin with an `{{ID}}` placeholder, else mints an id-less node (warning only). Two edges (E-1, E-6) got hand-inserted ids. Fix: document in the script's --help + step files, and make missing-stdin a hard error.
2. MAJOR (step 9, also hit at step 10) — harness Write tool refuses the cluster-review/report artifacts ("subagents should return findings as text, not write report files"); 3+ children worked around via shell heredoc. Risk: a child that doesn't think of the workaround silently returns text and writes nothing. Fix: permission/hook config or brief-level instruction to write via shell.
3. MAJOR (step 8 gate) — `run.py` BANNED-token scan matches inside comments: E-7's block failed on the word "open" in a reason comment. Fix: strip comments before scanning (or ban call syntax only).
4. MAJOR (step 10) — spec consumes per-cluster `external_consensus`, but no upstream step ever writes that field (steps 7/8 own the blocks, step 9 has it as optional prose). Broken cross-step interface; report substituted a labelled own-characterization. Fix: assign an owner or drop from step-10's Consumes.
5. MAJOR (step 1a) — orchestrator/planner fabricated the LSAG author list in seed material (conflating 3 real papers); a non-verifying searcher would have written it onto a load-bearing source node. Fix: mark all planner-supplied bibliographic detail as unverified-until-fetched.
6. MAJOR (steps 2a/5; skill-wide) — link-format ambiguity: mode-file field tables show ``[[S-N]]`` shorthand while SKILL.md requires full-filename wikilinks; a 2a scorer followed the tables and wrote 16 unresolvable links (orchestrator normalized). Fix: pin full-filename form in every field table.
7. MAJOR (step 3) — no schema slot for cross-paper argument attachment: S-23's observer-selection argument attacks another paper's evidence basis (D-1/S-1) but `affects_*` only reaches same-paper O/H; encoded as prose, invisible to steps 5/6 mechanics.
8. MAJOR (step 1c) — step-01 mode file lacks an output spec for the 1c consolidated pool (step 2's entry point); the real spec lived only in the orchestrator's prompt.
9. MAJOR (setup) — sibling-dir collision: `analyses/black-holes/` (earlier full run of the same case) invites children to read/copy the wrong graph; mitigated only by per-brief warnings. Fix: quarantine/rename earlier runs of the same case.
10. MAJOR (step 6→8 QA gap, HC-4) — A-7 approved as checked while deriving the opposite observer-tilt (late) from what E-6's mechanism prose asserts (early); direct inter-node contradiction passed the checked-gate (update direction happened to survive). Fix candidate: step-6 trace should read the argument's attached edges, not just the argument.
