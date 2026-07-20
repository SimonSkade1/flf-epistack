# Orchestrator continuation note — covid1 N=5 test run

> ## ✅ RUN COMPLETE — steps 1–10 all done and gated.
> Nothing left to continue. Final model: `HC-1 prior [0.3695, 0.1132, 0.5173] → posterior [0.4952, 0.0809, 0.4238]` over [H-1 market spillover, H-5 WIV research incident, H-6 residual].
> Deliverables: `main report - Did SARS-CoV-2 first infect humans…md` at the analysis root, `hypothesis-clusters/Analysis of HC-1 …md`, and — the thing Simon reads — the **`## Ranked summary` at the bottom of `problem-log.md`** (1 BLOCKER fixed, 9 MAJORs, plus 4 analysis-quality findings).
> One fix was made **outside** the analysis dir: `.claude/skills/flf-epistack/runner/run.py` gained `code_only()` to stop the banned-token scan reading comments (BLOCKER #1). `runner/test_run.py` still passes all 9 self-checks.
> The section below is the historical mid-run state; it is retained only for provenance.

**You are the flf-epistack step-0 orchestrator resuming a run already in progress. Do NOT restart.** Read this whole note, then `.claude/skills/flf-epistack/steps/step-00-orchestrate.md`, then continue from the NEXT section.

> ⚠️ **VERIFY BEFORE YOU SPAWN.** This note has already been stale once (it said "NEXT: Step 3" when step 3 was complete on disk; following it literally would have re-minted a duplicate node set, since `create_node.py` takes next-free ids and cannot detect that a paper was already extracted — logged as MAJOR in `problem-log.md`). **Always inventory the directory first** (`ls` the node folders, check for the artifacts the NEXT step is supposed to produce) and trust on-disk state over this note.

The run's verbatim prompt is `initial_prompt.md` (do NOT overwrite it). This is a deliberately fast **N=5 shakedown to surface pipeline bugs**, not a production analysis.

Analysis directory (quote it everywhere — spaces + parens):
`projects/create a useful aligning (AI-)macroagents agenda/Participate in FLF competition/analysis-tests/covid1`
Absolute root: `/home/simonskade/workspace/` + the above. cwd = vault root.
Main question (verbatim): "Did SARS-CoV-2 first infect humans through natural zoonotic spillover (e.g. via the wildlife trade / Huanan Seafood Market) or through a research-related incident (a lab leak)?"
`curated_target_N` = 5.

## Standing rules (carry into every remaining step)

1. **Minimum children per step** (at N=5 most steps are 1–2). Don't polish; only re-run a step if its gating **Check** actually fails.
2. **Effort routing via custom subagent types:** judgment-heavy children → `subagent_type: epistack-high`; mechanical children (consolidators, script-runners, fixers) → `epistack-med`. (If unavailable, fall back to `model: sonnet`; the Agent tool is `additionalProperties:false` so it has **no** `effort` param — routing must go through subagent_type or model.)
3. **Put a SPEED CAP block in every brief** (template below). Steps 3–10 are local-only, so cap web at 0 and read files in bulk (one shell `cat`/python loop, not many Reads).
4. **Copy the TEST-RUN NOTICE verbatim into every child brief** (template below).
5. **Gate each step's binary Checks before the next.** Prefer a Python gate script. On failure: either fix directly if it's a small mechanical edit, or spawn an `epistack-med` fixer; then re-check.
6. **Bash cwd persists between calls** — do NOT blindly re-`cd` (it errors). Prefer absolute paths. **Never `for f in $(find ...)` over these filenames — they contain spaces**; use Python or `-print0 | while IFS= read -r -d ''`.
7. **Non-node files** are ONLY: `initial_prompt.md`, `problem-log.md`, everything under `agent-notes/`. Never treat `problem-log.md` as a graph node.
8. **Problem log** at `…/covid1/problem-log.md`: append (never edit others') BLOCKER/MAJOR entries. Children are pointed at it via the notice.
9. **After step 8, before step 9:** run `python3 .claude/skills/flf-epistack/runner/run.py "<analysis-dir>"` to compose priors×likelihoods into per-cluster posteriors. Steps 9–10 read its output.
10. **FINAL deliverable — do not forget:** at the very end, append a `## Ranked summary` to `problem-log.md`: dedupe all entries, BLOCKERs first then MAJORs, each with step + one-line description. This is what Simon reads.
11. **Keep this note current** after each step you gate — that's the fix for the staleness bug above.

## Done & gated (do NOT redo)

- **Step 1 ✓ (gate PASS):** 17 sources `S-1…S-17`. Orientation notes in `agent-notes/orientation/`.
- **Step 2 ✓ (gate PASS):** all 17 scored; baseline **0.5**; **5 curated** — **S-2, S-4, S-11, S-12, S-15**; 12 moved to `sources/non-curated/`. Data-bases **D-1, D-2, D-3** live; D-4 merged into D-1. See `agent-notes/curation.md`.
- **Step 3 ✓ (gate PASS, all 8 checks):** 12 observations `O-1…O-12`, 5 hypotheses `H-1…H-5`, 5 arguments `A-1…A-5`; every curated source carries an ordered `extracted:` list. **Consolidator deliberately skipped** — zero `generally_known` observations and zero straggler `D` nodes minted, so both of its jobs were no-ops.
- **Step 4 ✓ (gate PASS, checks 1–6):**
  - **4a:** H-2 → merged into **H-1**; H-4 → merged into **H-3**; nothing dropped. Survivor bookkeeping (`merged_from` / `additional_sources` / per-source `locator` / `generalization_note`) verified.
  - **4b:** carved **one** cluster, **HC-1** "Route of the first human SARS-CoV-2 infection", members in frozen order **[H-1, H-5, H-6]** (H-6 = residual, `origin: step-4-residual`). It **rejected** a second "evolutionary origin" cluster as the rule-3 double-counting trap, and **dropped H-3** as background compatible with every member. `agent-notes/structure.md` written.
  - **Orchestrator fix applied:** dropping survivor H-3 stranded H-4 (`merged_into` → a dropped node, breaking check 1). H-4 re-dispositioned to `dropped` with its 4a merge preserved in `former_merged_into` + `merge_note`; `structure.md` counts corrected. Logged MAJOR.

### Current graph state
- **Active hypotheses:** H-1, H-5, H-6 (all in HC-1). Dropped: H-3, H-4. Merged: H-2.
- **Observations:** O-1…O-12, all live in `observations-and-facts/`, no tombstones.
- **Arguments:** A-1…A-5. Attachments: A-1→O-2, A-2→O-5, A-3→O-6, A-4→O-9, A-5→O-11 **and** H-5 (the only argument with a non-empty `affects_hypotheses`, so it is HC-1's no-observation-argument feed at step 7).

**Watch-outs:** (a) the 5 curated sources rest on 5 *distinct* data bases (D-2, S-4, S-11, S-12, S-15), so a correlation group at step 5/8 will only form if a *single* source yields ≥2 linked observations sharing a basis — S-2 (O-1/O-2/O-3 → D-2) and S-12 (O-8/O-9/O-10 → S-12) are the only candidates. If no CG forms, note it but it may be the design working. (b) The lab-leak side rests on S-15 alone (a *rejected proposal*, not evidence an escape occurred), so expect a zoonosis-leaning posterior; fine for a shakedown.

## NEXT: Step 5 (in progress) → 6→10

**Step 5 cluster-child for HC-1 was spawned and is running** (`epistack-high`); it mints `evidence-link` (E) edges from discriminating observations only. When it returns:

1. **Gate nothing yet** — first spawn the **step-5 consolidator** (`epistack-med`), which runs, in this exact order:
   1. `python3 .claude/skills/flf-epistack/scripts/attach_argument_backlinks.py "<dir>"`
   2. `python3 .claude/skills/flf-epistack/scripts/build_correlation_groups.py "<dir>"`
   3. by hand: set `link_state` (`linked`/`orphan`) on every O in `observations-and-facts/` and move orphans to `observations-and-facts/orphan/` with `source` intact.
2. Then **gate step-5 Checks 1–7** (in the mode file). Check 5 = re-running `build_correlation_groups.py` is a no-op.

Then:
- **Step 6** (`step-06-arguments.md`): run `batch_arguments.py "<dir>"` → 1 child per batch (`epistack-high`) writes `status`/`reason_if_not_false` on its own args. Only 5 arguments → 1 batch. Gate.
- **Step 7** (`step-07-priors.md`): 1 child for HC-1 (`epistack-high`); consult cluster edges + `no_observation_arguments.py "<dir>" --cluster HC-1` (expect A-5); select prior-relevant links, write a `## Prior` block over [H-1, H-5, H-6], mark used edges `used_for_prior: true`. Gate.
- **Step 8** (`step-08-likelihoods.md`): run `batch_likelihoods.py "<dir>"` → 1 child per unit (`epistack-high`); write `## Likelihood` block(s). Units disjoint. Then **run `runner/run.py "<dir>"`** — the step-8→9 gate.
- **Step 9** (`step-09-cluster-review.md`): 1 child (`epistack-high`) writes `hypothesis-clusters/Analysis of HC-1 - {title}.md`.
- **Step 10** (`step-10-final-report.md`): 1 child (`epistack-high`) writes `main report - {question}.md` at the analysis root.
- **Then append `## Ranked summary` to problem-log.md** (rule 10).

## Templates to reuse

### SPEED CAP block (adapt the numbers per step)
```
╔═ SPEED CAP (fast test — HARD limits) ═╗
Single pass, no polish/iterate. Read files in bulk (one shell command), not many Reads. Web fetches: [0 / ≤N]. Hard cap ~[N] tool calls total. Rough-but-correct beats thorough.
╚═══════════════════════════════════════╝
```

### TEST-RUN NOTICE (copy verbatim into EVERY child brief)
```
┌─ TEST-RUN NOTICE — copy verbatim into every subagent brief ─────────────┐

This is a **quick test run under time pressure**, not a production analysis. The goal is only to surface **major errors or problems in the pipeline**, not to produce an optimal output. Work **fast**, and don't worry about your output being imperfect or sub-optimal — a rough, correct-enough pass is exactly what's wanted; do not polish or iterate. **Do not log minor imperfections.** If you hit a real problem — a pipeline bug, a broken or ambiguous cross-step interface, missing or contradictory instructions, a script that errors, or anything that blocks or corrupts the run — append ONE entry to the problem log with a severity tag (`BLOCKER` or `MAJOR`) and one line of context (which step, which slice, what happened). The log is at:
`projects/create a useful aligning (AI-)macroagents agenda/Participate in FLF competition/analysis-tests/covid1/problem-log.md`
Append with a single write (e.g. a `>>` shell append) so parallel appends don't clobber each other; never edit or delete other agents' entries. Then keep going if you can.

└──────────────────────────────────────────────────────────────────────────┘
```
