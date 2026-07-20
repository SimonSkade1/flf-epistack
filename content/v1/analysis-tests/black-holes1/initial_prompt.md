Run the full FLF EpiStack pipeline (flf-epistack step 0) on the case below.

(This file IS the run's initial prompt — read it as the source of truth. It is already written verbatim; do not overwrite it with the chat message that launched the run.)

═══════════════════════════════════════════════════════════
⚡ QUICK TEST RUN — READ FIRST (orchestrator)
═══════════════════════════════════════════════════════════

I (Simon) am under time pressure. This is a **fast shakedown run to test whether there are any major errors or problems in the pipeline** — NOT a production analysis and NOT an attempt at an optimal knowledge base. Optimize for finishing quickly and surfacing real pipeline problems, not for output quality.

`curated_target_N` is deliberately small (5) to keep this cheap. Still run all 10 steps end-to-end, so every stage and every cross-step interface executes at least once — the point is to exercise the whole pipeline once and see what breaks.

Orchestrator, you must:
1. Work fast and keep every step lean. Use the minimum children each step needs (at N=5 most steps are 1–2 children). Don't polish, don't re-run steps for quality — only re-run a step if its gating **Check** actually fails.
2. **Copy the TEST-RUN NOTICE block below verbatim into every subagent brief you write** (append it to each child's brief). It applies to you too.
3. A **problem log** exists at `projects/create a useful aligning (AI-)macroagents agenda/Participate in FLF competition/analysis-tests/black-holes1/problem-log.md`. Every child is pointed at it by the notice. That file, `initial_prompt.md`, and `agent-notes/` are the only non-node files in the dir — do NOT treat `problem-log.md` as a graph node, and do not let any check move or delete it.
4. Log the blockers/majors YOU hit too (e.g. a gating Check that keeps failing, a script that errors, a mode file that contradicts itself).
5. At the very end of the run, append a `## Ranked summary` to `problem-log.md`: dedupe the entries and list them ranked by severity (all BLOCKERs first, then MAJORs), each with its step and one-line description. This ranked list is the main deliverable of the test — I read it to decide what to fix before the real N=25/50 runs.

┌─ TEST-RUN NOTICE — copy verbatim into every subagent brief ─────────────┐

This is a **quick test run under time pressure**, not a production analysis. The goal is only to surface **major errors or problems in the pipeline**, not to produce an optimal output. Work **fast**, and don't worry about your output being imperfect or sub-optimal — a rough, correct-enough pass is exactly what's wanted; do not polish or iterate. **Do not log minor imperfections.** If you hit a real problem — a pipeline bug, a broken or ambiguous cross-step interface, missing or contradictory instructions, a script that errors, or anything that blocks or corrupts the run — append ONE entry to the problem log with a severity tag (`BLOCKER` or `MAJOR`) and one line of context (which step, which slice, what happened). The log is at:
`projects/create a useful aligning (AI-)macroagents agenda/Participate in FLF competition/analysis-tests/black-holes1/problem-log.md`
Append with a single write (e.g. a `>>` shell append) so parallel appends don't clobber each other; never edit or delete other agents' entries. Then keep going if you can.

└──────────────────────────────────────────────────────────────────────────┘

═══════════════════════════════════════════════════════════
CASE (LHC black-holes) — same content as the real run, N reduced for the test
═══════════════════════════════════════════════════════════

Main question (verbatim): "Was the risk that LHC collisions destroy the Earth (via stable micro black holes or other proposed mechanisms) truly put to rest, and what does that conclusion hinge on?"
curated_target_N: 5
Analysis directory: projects/create a useful aligning (AI-)macroagents agenda/Participate in FLF competition/analysis-tests/black-holes1

Case framing — from the FLF EpiStack competition page, quoted verbatim as scope/intent (NOT the main question):

> CERN, home of the world's largest particle accelerator, the Large Hadron Collider (LHC), has a frequently asked question: Will CERN generate a black hole?
> What??
> As in some previous science experiments, noting that novel circumstances might produce unprecedented outcomes, some participants had apocalyptic concerns. How were these put to rest? (Were they truly? What does that hinge on?)
> Unlike COVID, this is (we hope!) essentially a closed case, and uncontested. It nevertheless rests on a huge body of accumulated and interacting knowledge which enabled scientists (and the officials and public supporting them) to move forward with confidence.
> The key challenge here may be in probing this argument for its dependencies and key considerations, and perhaps noting the weakest or most speculative points — all in an accessible way.

Starting material (the only sources FLF links; step 1 must snowball out to the primary safety analyses):
> - CERN FAQ: https://home.cern/resources/faqs/will-cern-generate-black-hole
> - 1946 Konopinski–Marvin–Teller LA-602 atmospheric-ignition paper (methodological analogue for a-priori catastrophe bounds): https://blog.nuclearsecrecy.com/wp-content/uploads/2018/06/1946-LA-602-Konopinski-Marvin-Teller-Ignition-fo-the-Atmsophere.pdf

Scope notes for this run (steering, not binding):
1. This is a near-closed case, and the main question itself asks "what does the conclusion hinge on" — so the value is a graph that shows exactly what the ~zero-risk verdict DEPENDS ON and names the weakest / most speculative links, not a surprising bottom line. Make sure step 6 (arguments) and step 9/10 ("what it hangs on", "what would help") capture the load-bearing premises rather than just restating the safe conclusion.
2. Likely clusters: micro-black-hole stability & accretion rate, strangelet conversion, vacuum decay, plus a residual "some other new-physics catastrophe". The cosmic-ray empirical-bound argument (astrophysical objects survive natural collisions at higher energies) routes through several of these — watch for correlated evidence and give the shared cosmic-ray premise a single data-basis / argument identity.
3. Reach the primary safety analyses: the LSAG report, Giddings–Mangano (2008), the earlier RHIC safety reviews (Busza et al.), and the Hawking-radiation / production-cross-section literature. Score theoretical papers on argument validity (step 6b), not on data-replication baselines.
