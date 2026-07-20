Run the full FLF EpiStack pipeline (flf-epistack step 0) on the case below.

(This file IS the run's initial prompt — read it as the source of truth. It is already written verbatim; do not overwrite it with the chat message that launched the run.)

═══════════════════════════════════════════════════════════
⚡ QUICK TEST RUN — READ FIRST (orchestrator)
═══════════════════════════════════════════════════════════

I (Simon) am under time pressure. This is a **fast shakedown run to test whether there are any major errors or problems in the pipeline** — NOT a production analysis and NOT an attempt at an optimal knowledge base. Optimize for finishing quickly and surfacing real pipeline problems, not for output quality.

`curated_target_N` is deliberately small (10) to keep this cheap. Still run all 10 steps end-to-end, so every stage and every cross-step interface executes at least once — the point is to exercise the whole pipeline once and see what breaks.

Orchestrator, you must:
1. Work fast and keep every step lean. Use the minimum children each step needs. Don't polish, don't re-run steps for quality — only re-run a step if its gating **Check** actually fails.
2. **Copy the TEST-RUN NOTICE block below verbatim into every subagent brief you write** (append it to each child's brief). It applies to you too.
3. A **problem log** exists at `projects/create a useful aligning (AI-)macroagents agenda/Participate in FLF competition/analysis-tests/eggs1/problem-log.md`. Every child is pointed at it by the notice. That file, `initial_prompt.md`, and `agent-notes/` are the only non-node files in the dir — do NOT treat `problem-log.md` as a graph node, and do not let any check move or delete it.
4. Log the blockers/majors YOU hit too (e.g. a gating Check that keeps failing, a script that errors, a mode file that contradicts itself).
5. At the very end of the run, append a `## Ranked summary` to `problem-log.md`: dedupe the entries and list them ranked by severity (all BLOCKERs first, then MAJORs), each with its step and one-line description. This ranked list is the main deliverable of the test — I read it to decide what to fix before the real N=25/50 runs.

┌─ TEST-RUN NOTICE — copy verbatim into every subagent brief ─────────────┐

This is a **quick test run under time pressure**, not a production analysis. The goal is only to surface **major errors or problems in the pipeline**, not to produce an optimal output. Work **fast**, and don't worry about your output being imperfect or sub-optimal — a rough, correct-enough pass is exactly what's wanted; do not polish or iterate. **Do not log minor imperfections.** If you hit a real problem — a pipeline bug, a broken or ambiguous cross-step interface, missing or contradictory instructions, a script that errors, or anything that blocks or corrupts the run — append ONE entry to the problem log with a severity tag (`BLOCKER` or `MAJOR`) and one line of context (which step, which slice, what happened). The log is at:
`projects/create a useful aligning (AI-)macroagents agenda/Participate in FLF competition/analysis-tests/eggs1/problem-log.md`
Append with a single write (e.g. a `>>` shell append) so parallel appends don't clobber each other; never edit or delete other agents' entries. Then keep going if you can.

└──────────────────────────────────────────────────────────────────────────┘

═══════════════════════════════════════════════════════════
CASE (eggs) — same content as the real run, N reduced for the test
═══════════════════════════════════════════════════════════

Main question (verbatim): "Is habitual egg consumption net beneficial, harmful, or neutral for human health — overall, for whom, and at what level of intake?"
curated_target_N: 10
Analysis directory: projects/create a useful aligning (AI-)macroagents agenda/Participate in FLF competition/analysis-tests/eggs1

Case framing — from the FLF EpiStack competition page, quoted verbatim as scope/intent (NOT the main question). This is the entire brief FLF gives; there is no starting-material list.

> Are eggs good to eat? Bad to eat? Great in moderation? How can we tell? Does it vary across people, and what predicts this? What else should we be paying attention to here?
> This vague and open-ended topic, though mundane, is representative of a huge number of everyday questions — and hopefully also a microcosm of many more impactful debates. Sometimes getting resolution on what are the important things to answer and what are the appropriate ways of knowing is (more than) half of the challenge.

Scope notes for this run (steering, not binding):
1. FLF says resolving WHAT to ask and WHAT COUNTS AS KNOWING is more than half the challenge — treat surfacing the right sub-questions as a first-class output. Candidate (non-binding) sub-questions to seed step 1: effect on blood LDL/ApoB (dietary-cholesterol response), effect on CVD events, effect on all-cause mortality, effect specifically in people with type-2 diabetes, dose-response above ~1 egg/day, and inter-individual variation (hyper- vs hypo-responders).
2. N is set higher (10) than the other test cases because the base spans mechanistic, RCT (mostly surrogate-endpoint), and observational/epidemiological designs. Balance step-1 sourcing across those designs and across pro/anti findings, and be strict about correlated evidence: many cohort papers re-analyse the same few underlying cohorts (NHS, PURE, EPIC, etc.) — give each cohort its own data-basis node.
3. Keep surrogate endpoints (LDL) and hard endpoints (events, mortality) in separate clusters. A real effect on a surrogate alongside a null effect on mortality is itself a key finding, not a contradiction to sand off.
