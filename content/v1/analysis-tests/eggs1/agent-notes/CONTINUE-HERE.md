# CONTINUE-HERE — orchestrator resume note (eggs1 test run)

> **RUN COMPLETE (2026-07-20).** All 10 steps finished and gated; the ranked summary is written at the bottom of `problem-log.md` (2 BLOCKERs, 14 MAJORs). Final artifacts: `main report - Is habitual egg consumption...md` at the analysis root and three `Analysis of HC-N - ...md` cluster reviews in `hypothesis-clusters/`. Nothing below needs doing — the rest of this file is retained as the record of what was planned and why.

**You are the flf-epistack step-0 orchestrator, RESUMING a run already in progress.** Steps 0–4b are done and gated (4b verified against Checks 2–4,6 on 2026-07-20: 13 actives, each in exactly one of HC-1/HC-2/HC-3, backlinks match, one residual last per cluster, no numbers; strain already logged as MAJOR). Read this whole file, then continue from **step 5** through step 10 and the final ranked summary. Do **not** redo earlier steps or overwrite existing nodes.

First actions on resume:
1. Read `.claude/skills/flf-epistack/steps/step-00-orchestrate.md` (your role) and this run's source of truth `initial_prompt.md` (verbatim — do NOT overwrite it).
2. Skim this note's "Current state" and "Remaining plan". Verify state on disk with the check commands before trusting it.

---

## Run parameters (from initial_prompt.md)

- **Main question (verbatim):** "Is habitual egg consumption net beneficial, harmful, or neutral for human health — overall, for whom, and at what level of intake?"
- **curated_target_N = 10.**
- **Analysis dir:** `projects/create a useful aligning (AI-)macroagents agenda/Participate in FLF competition/analysis-tests/eggs1`
- **This is a FAST TEST RUN (shakedown), not a production analysis.** Optimize for finishing quickly and surfacing pipeline problems, not output quality. Use the minimum children each step needs. Only re-run a step if its gating Check actually fails.

## Operating rules for the rest of the run (IMPORTANT — carry these into every child)

1. **Agent types:** spawn judgment-heavy children as `epistack-high`, mechanical children as `epistack-med` (these exist as custom agent types with baked-in reasoning effort + speed discipline). Do NOT set a `model` override — let the agent type govern. All fan-out is yours; children never spawn children.
2. **Strong speed cap in every brief.** Prepend this to each child brief: "⚡ HARD SPEED CAP (from Simon): Work FAST, few tool calls, NO web unless truly unavoidable — work from the node files already on disk. Don't polish or re-verify. Target the minimum tool calls." The web-heavy re-reads (steps 1–2) were the ~850s/child cost; steps 5–10 are local reasoning and should be fast.
3. **Copy the TEST-RUN NOTICE (bottom of this file) verbatim into every child brief**, appended at the end. It applies to you too.
4. **create_node.py gotchas** (state these in every brief that mints nodes): (a) it needs the full node markdown, with a `{{ID}}` placeholder, piped on **stdin** (the mode-file one-line example omits this); (b) run it from vault root `/home/simonskade/workspace` OR pass the analysis-dir as an **absolute** path — a bare relative path fails from other cwds. Never hand-pick an id.
5. **Gate every step** with its mode-file Checks before starting the next; on failure spawn a fixer child, then re-check. Move-never-delete: retired nodes go to sub-folders, not deletion.
6. **Problem log** at `<dir>/problem-log.md`: children append BLOCKER/MAJOR only, single `>>` writes. It, `initial_prompt.md`, and everything under `agent-notes/` (incl. this file) are the only non-node files — no check may move/delete them.

---

## Current state (done + gated: steps 0, 1, 2, 3, 4a)

Verify with:
```
cd "<dir>"
ls sources/*.md | wc -l                 # 10 curated
ls sources/non-curated/*.md | wc -l      # 10 non-curated
ls data-bases/*.md | wc -l               # 10 live D (D-9 merged→D-4 in data-bases/merged/)
ls observations-and-facts/*.md | wc -l   # 20 live O (O-15 merged→O-3 in .../merged/)
ls hypotheses/*.md | wc -l               # 10 active H
ls arguments/*.md | wc -l                # 6 A
```

- **Curated sources (10):** S-1, S-5, S-8, S-9, S-11, S-12, S-13, S-14, S-16, S-19. (Non-curated S-2,S-3,S-4,S-6,S-7,S-10,S-15,S-17,S-18,S-20 in `sources/non-curated/`.)
- **Data-bases (10 live):** D-1 NHS, D-2 NHSII, D-3 HPFS, D-4 PHS, D-5 WHS, D-6 pooled-US (ARIC/CARDIA/Framingham/Jackson/MESA), D-7 PURE, D-8 China Kadoorie, D-10 EPIC, D-11 NIPPON DATA80. D-9 (dup PHS) merged→D-4.
- **Observations (20 live):** O-1..O-21 minus O-15 (merged→O-3). Generally-known survivor: O-3 (egg cholesterol content, data_basis []). D-backed obs carry data_basis overrides: O-4,O-5→D-8; O-6,O-7,O-8→D-4; O-9,O-10→D-10; O-19→D-1/D-2/D-3; O-20,O-21→D-7. Self-basis obs (inherit source): O-1,O-2 (S-12); O-13,O-14 (S-1); O-16,O-17 (S-5); O-18 (S-8); O-11,O-12 (S-19).
- **Hypotheses (10 active):** H-1 egg raises atherogenic lipids→CVD (S-12, surrogate); H-2 moderate intake protective for CVD (S-13, hard); H-3 high intake raises mortality esp. diabetics (S-14, hard); H-4 essentially neutral for IHD / inverse=reverse-causation (S-16, hard); H-5 poor bioavailability→weak effect (S-19, surrogate); H-6 2 eggs/day safe in T2D (S-1, heterogeneity); H-7 stable hypo-responder subset (S-5, heterogeneity); H-8 real but saturating lipid effect (S-8, surrogate); H-9 moderate intake not associated with CVD (S-9, hard-null); H-10 globally neutral (S-11, broad null). **4a made no merges/drops** (all discriminable) — so the H-merge bookkeeping path is untested (fine; step-3 generally-known merge exercised the same convention).
- **Arguments (6):** A-1 blinded crossover isolates egg as cause → affects O-1 (S-12); A-2 mortality-without-events→residual confounding → O-6,O-7 (S-14); A-3 attenuation on excluding first 4y→reverse causation → O-9,O-10,H-4 (S-16); A-4 dose-response strengthens causal reading → O-4,H-2 (S-13); A-5 population-average misleading for subgroups → O-16,O-17,H-7 (S-5); A-6 concavity→linear extrapolation overstates harm → O-18,H-8 (S-8). (Verify each A's exact `affects_*` in the files before relying on it.)

---

## Remaining plan (steps 4b → 10)

### Step 4b — cluster (NEXT). One child, `epistack-high`, single (needs whole active set in view).
Brief it to read `steps/step-04-structure-hypotheses.md` (4b part only; take 4a's active set as given, do NO merging). Carve the 10 actives into ~3 mutually-exclusive `HC` clusters. **Case steering:** keep surrogate-endpoint H (H-1, H-5, H-8) separate from hard-endpoint H (H-2, H-3, H-4, H-9, H-10); heterogeneity (H-6, H-7) its own cluster. Each HC: `hypotheses` (≥2, ascending id, residual last), `exclusivity`, `exhaustive_by_construction` (key present), `independence`, `depends_on` (key present, ideally empty). Add exactly one residual per non-exhaustive cluster (mint via create_node.py, `origin: step-4-residual`, statement names the escape). Set each active H's `cluster` backlink. Write `agent-notes/structure.md` (inventory + counts + generated date).
**Known tension to watch (ask child to flag in its return):** H-4/H-9/H-10 all assert ~null direction, so as separate members of one hard-endpoint cluster their mutual exclusivity is strained. This is useful pipeline signal — if it can't be carved cleanly without merging, that points to a gap in the 4a-merge/4b-cluster division of labour (log MAJOR if real).
**Gate (step-4 Checks 2–4, 6):** every HC in `hypothesis-clusters/`, unique HC-N matching filename, ≥2 active members ascending-id/residual-last, non-empty exclusivity+independence, `depends_on`+`exhaustive_by_construction` keys present; exactly one `residual: true` last per non-exhaustive cluster; every active H in exactly one HC with matching `cluster` backlink, no H in two clusters; no step-4 field holds a number.

### Step 5 — link evidence. One child per HC (`epistack-high`, parallel), then one consolidator (`epistack-med`).
Per-cluster children read `steps/step-05-link-evidence.md`; each owns one HC and mints `evidence-link` (E) edges from every observation that DISCRIMINATES its cluster's members (obs→HC, per-member breakdown indexed by HC.hypotheses order). They do NOT touch arguments or correlation. Slices disjoint by construction.
Then ONE consolidator (after all cluster-children) runs, in order:
```
python3 .claude/skills/flf-epistack/scripts/attach_argument_backlinks.py "<dir>"
python3 .claude/skills/flf-epistack/scripts/build_correlation_groups.py "<dir>"
```
then sets `link_state` on every O (linked iff it's the `from` of some edge, else orphan→`observations-and-facts/orphan/`).
**Expected correlation groups** (obs sharing a data basis): {O-6,O-7,O-8}=D-4; {O-4,O-5}=D-8; {O-9,O-10}=D-10; {O-20,O-21}=D-7; plus each source's self-basis obs pair. build_correlation_groups mints CG nodes over these — sanity-check they appear.
**Gate:** `python3 .claude/skills/flf-epistack/scripts/check_missing_evidence_links.py "<dir>" --cluster all` (reports only) — spawn a fixer for any real (observation,argument) gap before proceeding.

### Step 6 — assess arguments. One child per batch of ≤20 args (`epistack-high`, parallel).
`python3 .claude/skills/flf-epistack/scripts/batch_arguments.py "<dir>"` (reports only) → batches. Only 6 args, so likely ONE batch = one child. It reads `steps/step-06-arguments.md`, assesses each arg's validity, writes `status`/`reason_if_not_false` (and for a `corrected` arg an edited `statement` + `## Original`) on its own args only. Gate step-6 Checks before step 7.

### Step 7 — priors. One child per HC (`epistack-high`, parallel; small).
Each reads `steps/step-07-priors.md`, slice = one HC. Consult the cluster's evidence-links + its no-observation args:
```
python3 .claude/skills/flf-epistack/scripts/no_observation_arguments.py "<dir>" --cluster HC-N
```
Select prior-relevant links (base rates), write one `## Prior` block pricing that cluster's members, mark each used edge `used_for_prior: true` (so step 8 won't double-count).

### Step 8 — likelihoods. One child per unit (`epistack-high`, parallel).
`python3 .claude/skills/flf-epistack/scripts/batch_likelihoods.py "<dir>"` (reports only) → units, each either one `CG-N` (joint) or a batch of ≤3 lone edges; `used_for_prior` edges are excluded and listed as "already accounted for". Pass each unit's edge ids (`assess`) + write target (`block_on`: the CG node, or each edge note) into the brief. CG unit → one joint `## Likelihood` block on the CG node; independent batch → one `## Likelihood` block per edge note. No consolidator.

### After step 8, before step 9 — run the model (gate):
```
python3 .claude/skills/flf-epistack/runner/run.py "<dir>"
```
Prints `HC-N  prior [...]  posterior [...]` per cluster. Catches wrong-length vectors, a cluster missing a prior/likelihood, or banned tokens. Fix before step 9.

### Step 9 — cluster reviews. One child per HC (`epistack-high`, parallel).
Each reads `steps/step-09-cluster-review.md`, writes the human-readable review beside its HC: `hypothesis-clusters/Analysis of HC-N - {rest of HC-N's title}.md` (no id).

### Step 10 — final report. One child (`epistack-high`).
Reads `steps/step-10-final-report.md`, reads the cluster reviews + posteriors, writes the single `main report - {core research question}.md` at the analysis root.

### FINAL — ranked summary (your job, orchestrator):
Append `## Ranked summary` to `problem-log.md`: dedupe all entries, list BLOCKERs first then MAJORs, each with step + one-line description. **This ranked list is the main deliverable of the test run** — Simon reads it to decide what to fix before the real N=25/50 runs.

---

## Problem log state so far (all MAJOR, no BLOCKERs yet)

Already logged in `problem-log.md`:
1. MAJOR — `create_node.py` snippet uses relative paths with no stated cwd; fails when run from the analysis dir. (step 1)
2. MAJOR — briefs asked to tag each source surrogate-vs-hard endpoint, but no `endpoint_type` field exists in the source schema (added ad-hoc, inconsistent across pool). (step 1)
3. MAJOR — data-basis granularity undefined for pooled multi-cohort studies (scope-note says "each cohort its own node" but S-7/S-9 treated as single pooled basis); choice changes step-5 independence counting. (step 2a)
4. MAJOR — my orchestrator brief mislabeled S-14's basis as "PHS/WHS"; S-14 is PHS-only (WHS is S-4). Scorer caught it and minted PHS-only, else a false step-5 correlation edge. (step 2a)
5. MAJOR — `create_node.py` stdin requirement (piped markdown + `{{ID}}`) absent from mode-file invocation examples; multiple agents' first mint call failed. (step 3 + recurring)

Watch for more at 4b (exclusivity strain) and step 5 (correlation-group correctness).

---

## TEST-RUN NOTICE — copy verbatim into every subagent brief

```
┌─ TEST-RUN NOTICE — copy verbatim into every subagent brief ─────────────┐

This is a **quick test run under time pressure**, not a production analysis. The goal is only to surface **major errors or problems in the pipeline**, not to produce an optimal output. Work **fast**, and don't worry about your output being imperfect or sub-optimal — a rough, correct-enough pass is exactly what's wanted; do not polish or iterate. **Do not log minor imperfections.** If you hit a real problem — a pipeline bug, a broken or ambiguous cross-step interface, missing or contradictory instructions, a script that errors, or anything that blocks or corrupts the run — append ONE entry to the problem log with a severity tag (`BLOCKER` or `MAJOR`) and one line of context (which step, which slice, what happened). The log is at:
`projects/create a useful aligning (AI-)macroagents agenda/Participate in FLF competition/analysis-tests/eggs1/problem-log.md`
Append with a single write (e.g. a `>>` shell append) so parallel appends don't clobber each other; never edit or delete other agents' entries. Then keep going if you can.

└──────────────────────────────────────────────────────────────────────────┘
```
