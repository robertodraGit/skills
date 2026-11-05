#!/usr/bin/env python3
"""Group developer changes into a raw list for user-facing release notes.

Input: a CHANGELOG section (release-please / conventional-changelog format) or a git range.
Output: markdown grouped into User-facing and Internal buckets, with commit links and hashes
stripped. The agent rewrites the user-facing bullets in plain language (references/05-release-notes.md).

Usage:
    python3 changelog-to-notes.py --changelog CHANGELOG.md --version 3.4.1
    python3 changelog-to-notes.py --git v3.3.0..HEAD
Stdlib only.
"""
import argparse
import re
import subprocess
import sys

USER_TYPES = {"feat": "New", "fix": "Fixed", "perf": "Faster", "revert": "Fixed"}
INTERNAL_TYPES = {"chore", "ci", "docs", "test", "tests", "refactor", "build", "style", "deps"}
HEADING_TO_TYPE = {
    "features": "feat",
    "bug fixes": "fix",
    "performance improvements": "perf",
    "reverts": "revert",
    "miscellaneous chores": "chore",
    "documentation": "docs",
    "code refactoring": "refactor",
    "tests": "test",
    "build system": "build",
    "continuous integration": "ci",
}


def clean(text):
    text = re.sub(r"\s*\(\[[0-9a-f]{7,40}\]\([^)]*\)\)", "", text)  # (hash link)
    text = re.sub(r"\s*\([0-9a-f]{7,40}\)$", "", text)
    text = re.sub(r"\s*\(#\d+\)$", "", text)
    return text.strip()


def split_scope(text):
    m = re.match(r"^\*\*([^*]+):\*\*\s*(.+)$", text)
    if m:
        return m.group(1), m.group(2)
    m = re.match(r"^([a-z]+)(?:\(([^)]+)\))?!?:\s*(.+)$", text)
    if m:
        return (m.group(2) or ""), m.group(3)
    return "", text


def from_changelog(path, version):
    lines = open(path, encoding="utf-8").read().split("\n")
    start = None
    for i, line in enumerate(lines):
        if re.match(r"^##\s+\[?v?" + re.escape(version) + r"\]?", line):
            start = i + 1
            break
    if start is None:
        sys.exit(f"version {version} not found in {path}")
    items, current = [], "feat"
    for line in lines[start:]:
        if re.match(r"^##\s+\[?v?\d", line):
            break
        h = re.match(r"^###\s+(.+)$", line)
        if h:
            current = HEADING_TO_TYPE.get(h.group(1).strip().lower(), "chore")
            continue
        b = re.match(r"^[*-]\s+(.+)$", line)
        if b:
            scope, text = split_scope(clean(b.group(1)))
            items.append((current, scope, text))
    return items


def from_git(rng):
    out = subprocess.run(["git", "log", "--no-merges", "--pretty=%s", rng], capture_output=True, text=True, check=True).stdout
    items = []
    for subject in out.splitlines():
        m = re.match(r"^([a-z]+)(?:\(([^)]+)\))?!?:\s*(.+)$", subject.strip())
        if m:
            items.append((m.group(1), m.group(2) or "", clean(m.group(3))))
        else:
            items.append(("other", "", clean(subject)))
    return items


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--changelog")
    ap.add_argument("--version")
    ap.add_argument("--git", help="git revision range, e.g. v3.3.0..HEAD")
    args = ap.parse_args()
    if args.changelog and args.version:
        items = from_changelog(args.changelog, args.version)
    elif args.git:
        items = from_git(args.git)
    else:
        ap.error("pass --changelog and --version, or --git RANGE")

    user = {}
    internal = []
    for typ, scope, text in items:
        if typ in USER_TYPES:
            user.setdefault(USER_TYPES[typ], []).append((scope, text))
        else:
            internal.append((typ, scope, text))

    print("# Raw material for release notes\n")
    print("Rewrite the user-facing bullets in plain language; drop anything the user cannot see or feel.\n")
    print("## User-facing candidates\n")
    if not user:
        print("_none: if the release has user-visible changes, the commit messages do not show them; ask the user._\n")
    for bucket in ("New", "Faster", "Fixed"):
        if bucket in user:
            print(f"### {bucket}")
            for scope, text in user[bucket]:
                print(f"- {text}" + (f"  _(area: {scope})_" if scope else ""))
            print()
    print("## Internal (usually omitted)\n")
    for typ, scope, text in internal:
        print(f"- {typ}{'(' + scope + ')' if scope else ''}: {text}")
    print()


if __name__ == "__main__":
    main()
