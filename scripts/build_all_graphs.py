#!/usr/bin/env python3
"""Regenerate every case study's model graph and viewer entry point.

Discovers each analysis folder under content/v1/{analysis-tests,analyses} that
has a `main-report` note, and for each writes:
  - quartz/static/model/graph-<case>.json   the model graph
  - quartz/static/model/<case>/index.html   a redirect into the shared viewer

plus quartz/static/model/manifest.json (the list of available cases) and
graph.json (the bare-URL default).

Run this BEFORE `npx quartz build` — it needs no contentIndex (slugs are
computed directly), so a newly-added analysis needs no bootstrap build and no
code change: finish its pipeline (so it has a main-report) and re-run. Wired as
`npm run graphs`; the deploy recipe in docs/website.md runs it before building.
"""
import json
import pathlib
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
import build_graph  # noqa: E402

MODEL_DIR = REPO / "quartz" / "static" / "model"
ANALYSIS_GLOBS = ["content/v1/analysis-tests/*", "content/v1/analyses/*"]

REDIRECT = """<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>EpiStack model graph — {case}</title>
    <meta http-equiv="refresh" content="0; url=../?a=graph-{case}" />
    <script>
      location.replace("../?a=graph-{case}" + location.hash)
    </script>
  </head>
  <body>
    <a href="../?a=graph-{case}">Open the {case} model graph &rarr;</a>
  </body>
</html>
"""


def has_main_report(d):
    """True if the analysis root holds a main-report note (pipeline finished
    enough to have a final answer to graph)."""
    for f in d.glob("*.md"):  # the main-report sits at the analysis root
        try:
            fm, _ = build_graph.split_frontmatter(f.read_text())
        except Exception:
            continue
        if fm.get("type") == "main-report":
            return True
    return False


def main():
    MODEL_DIR.mkdir(parents=True, exist_ok=True)
    cases = []
    for glob in ANALYSIS_GLOBS:
        for d in sorted(REPO.glob(glob)):
            if not d.is_dir() or not has_main_report(d):
                continue
            case = d.name
            out = f"quartz/static/model/graph-{case}.json"
            try:
                rc = build_graph.main([str(d), "--out", out, "--self-check"])
            except Exception as e:  # self-check assert, parse error, etc.
                print(f"  SKIP {case}: {e}", file=sys.stderr)
                continue
            if rc != 0:
                print(f"  SKIP {case}: exporter returned {rc}", file=sys.stderr)
                continue
            entry = MODEL_DIR / case / "index.html"
            entry.parent.mkdir(parents=True, exist_ok=True)
            entry.write_text(REDIRECT.format(case=case))
            cases.append(case)

    (MODEL_DIR / "manifest.json").write_text(json.dumps(sorted(cases), indent=2))
    if cases:
        default = "eggs1" if "eggs1" in cases else cases[0]
        (MODEL_DIR / "graph.json").write_text(
            (MODEL_DIR / f"graph-{default}.json").read_text()
        )
    print(
        f"\ngenerated {len(cases)} model graph(s): {', '.join(sorted(cases))}",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
