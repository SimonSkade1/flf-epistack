"""Batch `argument` nodes for step-6 validity-assessment children.

Step 6 assesses every argument's validity, fanned out over batches. The
orchestrator runs this to get the batches it hands to children. It only reads
and reports -- it never edits or moves a file; the children own all edits.

Every `type: argument` node directly under `arguments/` is batched; the
sub-folders `orphan/` and `dropped/` hold retired arguments and are skipped by
the non-recursive scan.

Usage:
    python3 batch_arguments.py <analysis-dir> [--batch-size 20]
"""

import argparse
import json
import pathlib
import re
import sys


def parse_frontmatter(text):
    """Minimal YAML-subset reader: `key: value` and `- item` lists, top level only."""
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    fm = {}
    key = None
    for line in text[3:end].splitlines():
        if not line.strip():
            continue
        m = re.match(r"^(\w[\w-]*):\s*(.*)$", line)
        if m:
            key, val = m.group(1), m.group(2).strip()
            if val in ("", "[]", "~", "null"):
                fm[key] = []
            elif val.startswith("[") and val.endswith("]"):
                inner = val[1:-1].strip()
                fm[key] = [x.strip().strip("\"'") for x in inner.split(",")] if inner else []
            else:
                fm[key] = val.strip("\"'")
        elif line.lstrip().startswith("- ") and key is not None:
            if not isinstance(fm.get(key), list):
                fm[key] = []
            fm[key].append(line.lstrip()[2:].strip().strip("\"'"))
    return fm


def arg_id(name):
    m = re.match(r"^(A-\d+)", name)
    return m.group(1) if m else name


def collect(root):
    argdir = root / "arguments"
    if not argdir.is_dir():
        sys.exit("no arguments/ folder under %s" % root)
    rows = []
    for path in sorted(argdir.glob("*.md")):  # non-recursive: skips orphan/, dropped/
        fm = parse_frontmatter(path.read_text(encoding="utf-8"))
        if fm.get("type") != "argument":
            continue
        rows.append(path)
    return rows


def batched(rows, size):
    return [rows[i:i + size] for i in range(0, len(rows), size)]


def main():
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("analysis_dir", type=pathlib.Path)
    ap.add_argument("--batch-size", type=int, default=20)
    args = ap.parse_args()

    rows = collect(args.analysis_dir)
    batches = batched(rows, args.batch_size)

    print("%d argument(s) -> %d batch(es) of <=%d\n"
          % (len(rows), len(batches), args.batch_size))
    for i, batch in enumerate(batches, 1):
        ids = [arg_id(p.name) for p in batch]
        print("Batch %d (%d): %s" % (i, len(batch), ", ".join(ids)))

    # machine-readable: list of batches, each a list of paths relative to analysis-dir
    rel = [[str(p.relative_to(args.analysis_dir)) for p in batch] for batch in batches]
    print("\nJSON:")
    print(json.dumps(rel))


if __name__ == "__main__":
    main()
