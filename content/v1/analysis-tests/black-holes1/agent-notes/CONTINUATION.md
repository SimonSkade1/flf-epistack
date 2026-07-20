# Continuation note — resume step-0 orchestration from after step 5

You are the step-0 orchestrator of the flf-epistack pipeline, resuming a paused test run. Steps 1–5 are DONE — do not redo or re-check them beyond the one pending gate below. Read in this order: (1) this file, (2) `../initial_prompt.md` (run's source of truth: main question verbatim, curated_target_N=5, TEST-RUN NOTICE block, ranked-summary duty), (3) `orchestrator-log.md` (full history, entries 1–19). Skim `.claude/skills/flf-epistack/SKILL.md` for conventions; read each step's mode file section only as needed for gating.

Main question (verbatim): "Was the risk that LHC collisions destroy the Earth (via stable micro black holes or other proposed mechanisms) truly put to rest, and what does that conclusion hinge on?"
Analysis directory: `projects/create a useful aligning (AI-)macroagents agenda/Participate in FLF competition/analysis-tests/black-holes1` (quote it — spaces; cwd = vault root `/home/simonskade/workspace`).

## Graph state (all ids minted so far — never reuse)

1. sources/: S-1..S-23; curated = S-1 (Giddings–Mangano), S-5 (Auger), S-13 (ADD), S-14 (Hawking), S-23 (Tegmark–Bostrom); other 18 in sources/non-curated/. Baseline 0.6, curation note agent-notes/curation.md.
2. data-bases/: D-1 (cosmic-ray survival premise), D-2 (planet-formation-time distribution).
3. observations-and-facts/: O-1..O-10; linked O-1/2/3/4/8/10; orphans O-5/6/7/9 in orphan/.
4. hypotheses/: H-1..H-10 all active (H-6..H-10 constructed/residual by 4b). Cluster map agent-notes/structure.md.
5. hypothesis-clusters/: HC-1 fate/danger (H-1,H-2,H-6res), HC-2 evaporation (H-4,H-7), HC-3 TeV gravity (H-3,H-8,H-9res), HC-4 exogenous bound (H-5,H-10).
6. arguments/: A-1..A-7 (all attached; 0 orphaned).
7. evidence-links/: E-1..E-4→HC-1, E-5→HC-3, E-6→HC-4, E-7..E-9→HC-2; `arguments` fields written by script.
8. correlation-groups/: CG-1 (HC-1: E-2,E-3,E-4), CG-2 (HC-2: E-8,E-9). Lone edges: E-1, E-5, E-6, E-7.
9. check_missing_evidence_links.py --cluster all: clean.

## Resume sequence

1. **Gate step 5** (yourself, mechanically — Checks at end of steps/step-05-link-evidence.md). Especially: E-1 and E-6 had hand-inserted `id:` fields after a create_node.py error — verify id/filename/from/to consistency on all 9 edges; no (from,to) duplicates; CG members/group fields mutually consistent. On failure spawn a fixer child, else proceed.
2. **Step 6**: run `python3 .claude/skills/flf-epistack/scripts/batch_arguments.py "<analysis-dir>"` (reports only). 7 top-level args → expect 1 batch → 1 child (epistack-high) assessing validity per steps/step-06-arguments.md (status / reason_if_not_false; corrected → edited statement + `## Original`). Gate step-6 Checks before step 7.
3. **Step 7**: 1 small child per cluster ×4, parallel (epistack-high). Each: steps/step-07-priors.md, one HC; consult connected evidence-links + `python3 .../scripts/no_observation_arguments.py "<analysis-dir>" --cluster HC-N`; write one `## Prior` block pricing the members; mark prior-used edges `used_for_prior: true`.
4. **Step 8**: run `python3 .../scripts/batch_likelihoods.py "<analysis-dir>"` → units (CG-1, CG-2 joint; lone edges in ≤3-batches; used_for_prior edges excluded — pass each unit's `assess` ids and `block_on` target from the script's JSON into the brief). 1 child per unit, parallel (epistack-high). CG unit → one joint `## Likelihood` block on the CG node; lone batch → one block per edge note.
5. **Gate**: `python3 .claude/skills/flf-epistack/runner/run.py "<analysis-dir>"` must print `HC-N prior [...] posterior [...]` for all 4 clusters. Fix (fixer child) until it runs clean.
6. **Step 9**: 1 child per cluster ×4, parallel (epistack-med, steps/step-09-cluster-review.md) → `Analysis of HC-N - {rest of title}.md` beside each HC. Remind them: the run's value is naming what the verdict hinges on (weakest links), per initial_prompt scope note.
7. **Step 10**: 1 child (epistack-high, steps/step-10-final-report.md) → `main report - {core research question}.md` at analysis root, reading the 4 reviews + run.py posteriors.
8. **Ranked summary**: dedupe problem-log.md entries, append `## Ranked summary` — BLOCKERs first then MAJORs, each with step + one line. This is Simon's main deliverable. Log your own blockers/majors too. Known entries so far (~7): 1a fabricated LSAG byline; sibling-dir collision risk; 1c output spec missing from mode file; wikilink-format ambiguity; no cross-paper argument-attachment slot (step 3); create_node.py stdin/{{ID}} contract undocumented (logged twice — dedupe); 2b curation.md line-count vs spec (minor, 2b report only).
9. Report to Simon: posteriors, ranked problems, wall-clock.

## Rules for every child brief (unchanged from the run so far)

10. Template per step-00: mode-file line, analysis dir (+ quote-the-path warning), main question verbatim, slice, budget, mint command (`python3 .claude/skills/flf-epistack/scripts/create_node.py "<analysis-dir>" --type <type> --title "..."` — NOTE: it reads node markdown on stdin with an `{{ID}}` placeholder; SAY SO in briefs, two children already tripped on it), "Never hand-pick an id, and do not spawn subagents", return spec (≤10 lines).
11. Append BOTH blocks below verbatim to every brief.
12. Full-filename wikilinks without .md everywhere (e.g. `[[HC-1 - <full title>]]`), never bare `[[X-N]]`.
13. Warn every child: sibling dir `.../Participate in FLF competition/analyses/black-holes/` is a different earlier run — never read/copy it. `problem-log.md`, `initial_prompt.md`, `agent-notes/` are not graph nodes.
14. Models/effort: no model overrides remain (opus phase was steps 1a/1c/2a/2b, done); use agent types epistack-high (judgment) / epistack-med (mechanical) — they carry effort settings + speed discipline.
15. Gate each step's binary Checks (mechanically where possible, yourself) before the next step; fixer child only on real failure.

## Block 1 — TEST-RUN NOTICE (copy verbatim into every brief)

┌─ TEST-RUN NOTICE — copy verbatim into every subagent brief ─────────────┐

This is a **quick test run under time pressure**, not a production analysis. The goal is only to surface **major errors or problems in the pipeline**, not to produce an optimal output. Work **fast**, and don't worry about your output being imperfect or sub-optimal — a rough, correct-enough pass is exactly what's wanted; do not polish or iterate. **Do not log minor imperfections.** If you hit a real problem — a pipeline bug, a broken or ambiguous cross-step interface, missing or contradictory instructions, a script that errors, or anything that blocks or corrupts the run — append ONE entry to the problem log with a severity tag (`BLOCKER` or `MAJOR`) and one line of context (which step, which slice, what happened). The log is at:
`projects/create a useful aligning (AI-)macroagents agenda/Participate in FLF competition/analysis-tests/black-holes1/problem-log.md`
Append with a single write (e.g. a `>>` shell append) so parallel appends don't clobber each other; never edit or delete other agents' entries. Then keep going if you can.

└──────────────────────────────────────────────────────────────────────────┘

## Block 2 — SPEED CAP (copy verbatim into every brief; set the cap number per task: ~12 mechanical, ~20 judgment, ~30 heavy)

┌─ SPEED CAP (orchestrator; Simon says the run is too slow) ──────────────┐
1. HARD CAP: ≤{N} tool calls total; batch independent calls.
2. Single pass. NO end-of-task self-validation sweep, no re-reading files you wrote — the orchestrator gates.
3. No web fetches. Trust what's on the nodes.
4. Terse output; return ≤10 lines.
5. If a call is 60/40, take the 60 and move on — no written deliberation.
└──────────────────────────────────────────────────────────────────────────┘
