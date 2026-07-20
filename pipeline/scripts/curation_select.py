"""Rank scored `source` nodes and report how skewed the prospective cut is.

Step 2 scores sources in parallel slices, then one selector makes the cut. The
cut has two parts a script can do better than prose: the arithmetic
(`combined_score = usefulness * (trust_score - baseline)`, sorted) and the
check that the top N is not a monoculture — forty re-analyses of one dataset
rank well individually and rise and fall together, which is exactly how a
Bayesian aggregation manufactures false confidence.

This script only reports. It never edits a node and never moves a file: the
selector reads the ranking and the skew flags, decides, and applies the
decision by hand so the reasoning stays in `curation_reason` where a reader
can see it.

Usage:
    python3 curation_select.py <analysis-dir> --target-n 8
    python3 curation_select.py <analysis-dir> --target-n 8 --baseline 0.7
"""

import argparse
import collections
import pathlib
import re
import sys

# A category value holding more than this share of the top N is flagged as
# over-represented; a value with at least MIN_SHUT_OUT sources in the pool but
# none in the top N is flagged as shut out.
SKEW_SHARE = 0.4
MIN_SHUT_OUT = 3

DIMENSIONS = ("field", "angle", "data_basis")


def parse_frontmatter(text):
    """Minimal YAML-subset reader: `key: value` and `- item` lists, top level only."""
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    fields, key = {}, None
    for line in text[3:end].splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        item = re.match(r"\s*-\s+(.*)", line)
        if item and key:
            # `key:` with an empty value followed by `- item` lines is a list.
            if not isinstance(fields.get(key), list):
                fields[key] = []
            fields[key].append(item.group(1).strip())
            continue
        m = re.match(r"([A-Za-z_][\w-]*)\s*:\s*(.*)", line)
        if m:
            key, value = m.group(1), m.group(2).strip()
            if value.startswith("[") and value.endswith("]"):
                inner = value[1:-1].strip()
                fields[key] = [v.strip() for v in inner.split(",") if v.strip()]
            else:
                fields[key] = value
    return fields


def as_float(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def clean_value(value):
    """Strip quotes and wikilink brackets; a link keeps only its id."""
    value = str(value).strip().strip("'\"").strip()
    value = re.sub(r"^\[\[|\]\]$", "", value).strip("'\"").strip()
    return value.split(" - ")[0].strip()


def values_of(source, dimension):
    """Category values a source occupies on one dimension (may be several)."""
    raw = source.get(dimension)
    if raw is None or raw == "" or raw == "unknown" or raw == []:
        return ["unknown"]
    if isinstance(raw, list):
        cleaned = [clean_value(v) for v in raw]
        return [c for c in cleaned if c] or ["unknown"]
    return [clean_value(raw)]


def load_sources(root):
    scored, unscored = [], []
    for path in sorted((root / "sources").rglob("*.md")):
        fields = parse_frontmatter(path.read_text())
        if fields.get("type") != "source":
            continue
        fields["_path"] = path
        fields["_id"] = fields.get("id", path.name.split(" - ")[0])
        trust, use = as_float(fields.get("trust_score")), as_float(fields.get("usefulness"))
        if trust is None or use is None:
            unscored.append(fields)
        else:
            fields["_trust"], fields["_use"] = trust, use
            scored.append(fields)
    return scored, unscored


def report_skew(top, pool, dimension):
    """Flag values over-represented in the cut, and values shut out of it."""
    top_counts = collections.Counter(v for s in top for v in values_of(s, dimension))
    pool_counts = collections.Counter(v for s in pool for v in values_of(s, dimension))
    lines, flags = [], []
    for value, count in top_counts.most_common():
        share = count / len(top)
        marker = "  <-- over-represented" if share > SKEW_SHARE and value != "unknown" else ""
        if marker:
            flags.append(value)
        lines.append("    %-32s %2d/%d of cut, %d in pool%s"
                     % (value[:32], count, len(top), pool_counts[value], marker))
    for value, count in pool_counts.most_common():
        if value not in top_counts and count >= MIN_SHUT_OUT and value != "unknown":
            flags.append(value)
            lines.append("    %-32s  0/%d of cut, %d in pool  <-- shut out"
                         % (value[:32], len(top), count))
    return lines, flags


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("analysis_dir")
    ap.add_argument("--target-n", type=int, required=True, help="curated_target_N")
    ap.add_argument("--baseline", type=float, default=0.8, help="trust baseline (default 0.8)")
    args = ap.parse_args()

    root = pathlib.Path(args.analysis_dir)
    if not (root / "sources").is_dir():
        sys.exit("no sources/ folder under %s" % root)

    scored, unscored = load_sources(root)
    if not scored:
        sys.exit("no scored sources found — has 2a run?")

    for s in scored:
        s["_combined"] = s["_use"] * (s["_trust"] - args.baseline)
    scored.sort(key=lambda s: s["_combined"], reverse=True)

    eligible = [s for s in scored
                if s["_combined"] > 0
                and str(s.get("refuted", "")).lower() not in ("true", "yes")
                and not s.get("duplicate_of")]
    top = eligible[:args.target_n]

    print("baseline %.2f | %d scored | %d clear the baseline | cut = top %d"
          % (args.baseline, len(scored), len(eligible), args.target_n))

    print("\nRANKING  (* = in the prospective cut)")
    print("    %-6s %7s %6s %5s  %s" % ("id", "comb", "trust", "use", "title"))
    for s in scored:
        mark = "*" if s in top else " "
        excl = ""
        if s["_combined"] <= 0:
            excl = "  [below baseline]"
        elif str(s.get("refuted", "")).lower() in ("true", "yes"):
            excl = "  [refuted]"
        elif s.get("duplicate_of"):
            excl = "  [duplicate]"
        print("  %s %-6s %7.2f %6.2f %5.1f  %s%s"
              % (mark, s["_id"], s["_combined"], s["_trust"], s["_use"],
                 s["_path"].stem.split(" - ", 1)[-1][:52], excl))

    print("\nREPRESENTATION OF THE CUT")
    all_flags = []
    for dimension in DIMENSIONS:
        lines, flags = report_skew(top, eligible, dimension)
        all_flags += flags
        print("  %s:" % dimension)
        print("\n".join(lines) if lines else "    (nothing recorded)")

    if all_flags:
        print("\nSWAP CANDIDATES  (next best outside the cut, for rebalancing)")
        for s in eligible[args.target_n:args.target_n + 8]:
            tags = ", ".join("%s=%s" % (d, "/".join(values_of(s, d))) for d in DIMENSIONS)
            print("    %-6s %7.2f  %s" % (s["_id"], s["_combined"], tags))
        print("\n  The cut is skewed on: %s." % ", ".join(sorted(set(all_flags))))
        print("  Trading a marginal ranking point for an independent method or dataset is")
        print("  usually worth it; log every departure from rank in curation_reason.")
    else:
        print("\n  No strong skew detected in the prospective cut.")

    if unscored:
        print("\nUNSCORED  (a 2a slice missed these — resolve before cutting)")
        for s in unscored:
            print("    %s  %s" % (s["_id"], s["_path"].name))


if __name__ == "__main__":
    main()
