#!/usr/bin/env bash
# Update the pinned commit hash in README.md to the current HEAD.
#
# Usage (from repo root, after committing other changes):
#   ./scripts/update_readme_hash.sh
# Then commit the README change if the hash moved.
#
# Exit codes:
#   0  success (hash updated, or already current / nothing to do)
#   1  usage / environment error (not a git repo, missing tools, etc.)
#   2  README missing or unreadable/unwritable
#   3  no recognizable commit-hash pattern and could not insert one
#   4  write verification failed

set -euo pipefail

die() {
  local code="$1"
  shift
  echo "error: $*" >&2
  exit "${code}"
}

need_cmd() {
  command -v "$1" >/dev/null 2>&1 || die 1 "required command not found: $1"
}

need_cmd git
need_cmd python3

ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || die 1 "not inside a git repository"
cd "${ROOT}" || die 1 "cannot cd to repository root: ${ROOT}"

if ! git rev-parse --abbrev-ref HEAD >/dev/null 2>&1; then
  echo "warning: could not resolve current branch name" >&2
fi

HASH="$(git rev-parse HEAD 2>/dev/null)" || die 1 "git rev-parse HEAD failed"
if [[ ! "${HASH}" =~ ^[0-9a-f]{40}$ ]]; then
  die 1 "HEAD does not look like a full SHA-1: '${HASH}'"
fi

README="README.md"
if [[ ! -f "${README}" ]]; then
  die 2 "${README} not found in ${ROOT}"
fi
if [[ ! -r "${README}" ]]; then
  die 2 "${README} is not readable"
fi
if [[ ! -w "${README}" ]]; then
  die 2 "${README} is not writable"
fi

set +e
python3 - "${HASH}" "${README}" <<'PY'
import re
import sys
from pathlib import Path

if len(sys.argv) != 3:
    print("error: internal usage: python3 - HASH README", file=sys.stderr)
    sys.exit(1)

new_hash, readme_path = sys.argv[1], sys.argv[2]
if not re.fullmatch(r"[0-9a-f]{40}", new_hash):
    print(f"error: invalid hash passed to python: {new_hash!r}", file=sys.stderr)
    sys.exit(1)

path = Path(readme_path)
try:
    text = path.read_text(encoding="utf-8")
except OSError as exc:
    print(f"error: cannot read {readme_path}: {exc}", file=sys.stderr)
    sys.exit(2)

if not text.strip():
    print(f"error: {readme_path} is empty", file=sys.stderr)
    sys.exit(2)

pattern = re.compile(r"(commit\s+`)[0-9a-f]{7,40}(`)", re.IGNORECASE)
matches = list(pattern.finditer(text))

if matches:
    text2, n = pattern.subn(r"\g<1>" + new_hash + r"\2", text)
    if n == 0:
        print("error: pattern matched but substitution made no changes", file=sys.stderr)
        sys.exit(3)
    action = f"updated {n} existing pin(s)"
else:
    needle = "**Research blueprint** (v0.2.0-candidate)"
    if needle in text and f"commit `{new_hash}`" not in text:
        text2 = text.replace(
            needle,
            f"**Research blueprint** (v0.2.0-candidate, commit `{new_hash}`)",
            1,
        )
        action = "inserted new pin next to version badge"
    elif f"commit `{new_hash}`" in text:
        print(f"README.md already pinned to {new_hash[:8]}\u2026 ({new_hash})")
        sys.exit(0)
    else:
        print(
            "error: no commit-hash pattern found and could not insert one "
            f"(expected a 'commit `\u2026`' pin or the version badge {needle!r})",
            file=sys.stderr,
        )
        sys.exit(3)

if text2 == text:
    print(f"README.md already pinned to {new_hash[:8]}\u2026 ({new_hash})")
    sys.exit(0)

try:
    path.write_text(text2, encoding="utf-8")
except OSError as exc:
    print(f"error: cannot write {readme_path}: {exc}", file=sys.stderr)
    sys.exit(2)

try:
    verify = path.read_text(encoding="utf-8")
except OSError as exc:
    print(f"error: write verification read failed: {exc}", file=sys.stderr)
    sys.exit(4)

if new_hash not in verify:
    print("error: write verification failed \u2014 new hash not present in README", file=sys.stderr)
    sys.exit(4)

print(f"README.md pinned to {new_hash[:8]}\u2026 ({new_hash}) [{action}]")
sys.exit(0)
PY
py_rc=$?
set -e

case "${py_rc}" in
  0) exit 0 ;;
  1) die 1 "python helper failed (invalid arguments or hash)" ;;
  2) die 2 "README read/write error" ;;
  3) die 3 "no recognizable commit-hash pattern in README" ;;
  4) die 4 "write verification failed" ;;
  *) die 1 "python helper exited with unexpected code ${py_rc}" ;;
esac
