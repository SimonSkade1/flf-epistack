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
3. A **problem log** exists at `projects/create a useful aligning (AI-)macroagents agenda/Participate in FLF competition/analysis-tests/covid1/problem-log.md`. Every child is pointed at it by the notice. That file, `initial_prompt.md`, and `agent-notes/` are the only non-node files in the dir — do NOT treat `problem-log.md` as a graph node, and do not let any check move or delete it.
4. Log the blockers/majors YOU hit too (e.g. a gating Check that keeps failing, a script that errors, a mode file that contradicts itself).
5. At the very end of the run, append a `## Ranked summary` to `problem-log.md`: dedupe the entries and list them ranked by severity (all BLOCKERs first, then MAJORs), each with its step and one-line description. This ranked list is the main deliverable of the test — I read it to decide what to fix before the real N=25/50 runs.

┌─ TEST-RUN NOTICE — copy verbatim into every subagent brief ─────────────┐

This is a **quick test run under time pressure**, not a production analysis. The goal is only to surface **major errors or problems in the pipeline**, not to produce an optimal output. Work **fast**, and don't worry about your output being imperfect or sub-optimal — a rough, correct-enough pass is exactly what's wanted; do not polish or iterate. **Do not log minor imperfections.** If you hit a real problem — a pipeline bug, a broken or ambiguous cross-step interface, missing or contradictory instructions, a script that errors, or anything that blocks or corrupts the run — append ONE entry to the problem log with a severity tag (`BLOCKER` or `MAJOR`) and one line of context (which step, which slice, what happened). The log is at:
`projects/create a useful aligning (AI-)macroagents agenda/Participate in FLF competition/analysis-tests/covid1/problem-log.md`
Append with a single write (e.g. a `>>` shell append) so parallel appends don't clobber each other; never edit or delete other agents' entries. Then keep going if you can.

└──────────────────────────────────────────────────────────────────────────┘

═══════════════════════════════════════════════════════════
CASE (covid origins) — same content as the real run, N reduced for the test
═══════════════════════════════════════════════════════════

Main question (verbatim): "Did SARS-CoV-2 first infect humans through natural zoonotic spillover (e.g. via the wildlife trade / Huanan Seafood Market) or through a research-related incident (a lab leak)?"
curated_target_N: 5
Analysis directory: projects/create a useful aligning (AI-)macroagents agenda/Participate in FLF competition/analysis-tests/covid1

Case framing — from the FLF EpiStack competition page, quoted verbatim as scope/intent (this is the judged case; it is NOT the main question). Competitor-facing sentences omitted where marked.

> In early 2024, a $100,000 judged debate took place between Saar Wilf (founder of Rootclaim) and Peter Miller on the origins of COVID-19. Over 15 hours of structured argument, two smart people marshalled epidemiological data, viral genetics, Bayesian inference, and institutional analysis to reach opposite conclusions. Two expert judges ruled decisively for zoonosis. Six independent Bayesian analyses of the same evidence spanned 23 orders of magnitude.
>
> [...] the debate videos, judge decisions, and comment threads [...] form one of the richest publicly available records of a complex real-world epistemic dispute on an important issue.
>
> And yet all this information is still incredibly difficult to navigate, interrogate, and use to inform one's beliefs.
> - It requires significant background expertise to understand the state of play of the debate and make a considered judgement.
> - The format, a live video debate, may not be the optimal way for a judge to interact with the material.
>
> Further, this intense epistemic effort represents a point in time in a conversation which continues to evolve.
> [competitor-facing framing — "Your job: craft the AI-assisted methodologies…" — omitted]

Starting material (seed sources for step 1; step 1 MUST reach the primary artifacts behind these, not stop at the summaries):
> - Scott Alexander's writeup of the COVID origins debate: https://www.astralcodexten.com/p/practically-a-book-review-rootclaim
> - Judge Will's decision: https://drive.google.com/file/d/1YhmkYB32RpGsXvQTsX4xZ0Yul1wiwh8Z/view | Judge Eric's decision: https://drive.google.com/file/d/1aHlhPd-16EOabzXhiajT5PBm3uVCAG3T/view
> - Michael Weissman's Bayesian analysis: https://michaelweissman.substack.com/p/an-inconvenient-probability-v57
> - Rootclaim's response: https://blog.rootclaim.com/covid-origins-debate-response-to-scott-alexander/
> - Debate videos: https://www.youtube.com/watch?v=Y1vaooTKHCM | https://www.youtube.com/watch?v=KdORmvU8MLI | https://www.youtube.com/watch?v=d1dbfoK8nSE

Scope notes for this run (steering, not binding — carve clusters bottom-up):
1. The top-level split is natural zoonotic spillover (wildlife-trade / market route) vs a research-related origin (accidental infection, sampling, or engineered). Likely sub-questions: geographic/temporal signal of the earliest cases, genomic features (furin cleavage site, RaTG13/BANAL relatedness, restriction-site / lineage-A-vs-B patterns), and market-vs-lab ascertainment bias.
2. This case involves probable deliberate data suppression (withheld early-case line lists, sampling records). Use the source `motivatedness` field, record firmly-established general observations about which data were released vs withheld, and treat absence-of-evidence carefully rather than as clean evidence for either side.
3. Many analyses re-use the same few underlying datasets (early-case geolocations, the market environmental samples, specific genomes) — give each a `data-basis` node so step 5 doesn't count re-analyses as independent.
