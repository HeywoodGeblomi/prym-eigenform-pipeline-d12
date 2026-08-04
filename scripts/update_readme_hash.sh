#!/usr/bin/env bash
# Update the pinned commit hash in README.md to the current HEAD.
#
# Usage:
#   ./scripts/update_readme_hash.sh
#   DEBUG=1 ./scripts/update_readme_hash.sh    # verbose logging
#   QUIET=1 ./scripts/update_readme_hash.sh    # suppress INFO lines
#
# Environment:
#   DEBUG=1   enable debug logs on stderr
#   QUIET=1   suppress non-error informational messages
#
# Exit codes:
#   0  success (hash updated, or already current / nothing to do)
#   1  usage / environment error
#   2  README missing or unreadable/unwritable
#   3  no recognizable commit-hash pattern and could not insert one
#   4  write verification failed

set -euo pipefail

DEBUG="${DEBUG:-0}"
QUIET="${QUIET:-0}"

ts() { date -u +"%Y-%m-%dT%H:%M:%SZ"; }

log() {
  if [[ "${QUIET}" != "1" ]]; then
    echo "[$(ts)] INFO  $*" >&2
  fi
}

dbg() {
  if [[ "${DEBUG}" == "1" ]]; then
    echo "[$(ts)] DEBUG $*" >&2
  fi
}

die() {
  local code="$1"
  shift
  echo "[$(ts)] ERROR $*" >&2
  dbg "exiting with code ${code}"
  exit "${code}"
}

need_cmd() {
  dbg "checking for command: $1"
  command -v "$1" >/dev/null 2>&1 || die 1 "required command not found: $1"
}

need_cmd git
need_cmd python3
dbg "tools ok (git=$(command -v git), python3=$(command -v python3))"

ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || die 1 "not inside a git repository"
dbg "repository root: ${ROOT}"
cd "${ROOT}" || die 1 "cannot cd to repository root: ${ROOT}"

BRANCH="$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo "?")"
dbg "current branch: ${BRANCH}"
if [[ "${BRANCH}" == "HEAD" ]]; then
  echo "[$(ts)] WARN  detached HEAD" >&2
fi

HASH="$(git rev-parse HEAD 2>/dev/null)" || die 1 "git rev-parse HEAD failed"
dbg "HEAD raw: ${HASH}"
if [[ ! "${HASH}" =~ ^[0-9a-f]{40}$ ]]; then
  die 1 "HEAD does not look like a full SHA-1: '${HASH}'"
fi
log "pinning README to ${HASH:0:8}… (${HASH})"

README="README.md"
dbg "README path: ${ROOT}/${README}"
if [[ ! -f "${README}" ]]; then
  die 2 "${README} not found in ${ROOT}"
fi
if [[ ! -r "${README}" ]]; then
  die 2 "${README} is not readable"
fi
if [[ ! -w "${README}" ]]; then
  die 2 "${README} is not writable"
fi
dbg "README size: $(wc -c < "${README}" | tr -d ' ') bytes"

set +e
python3 - "${HASH}" "${README}" "${DEBUG}" <<'PY'
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

def ts():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

def log(msg):
    print(f"[{ts()}] INFO  {msg}", file=sys.stderr)

def dbg(msg, enabled):
    if enabled:
        print(f"[{ts()}] DEBUG {msg}", file=sys.stderr)

def err(msg):
    print(f"[{ts()}] ERROR {msg}", file=sys.stderr)

if len(sys.argv) != 4:
    err("internal usage: python3 - HASH README DEBUG")
    sys.exit(1)

new_hash, readme_path, debug_flag = sys.argv[1], sys.argv[2], sys.argv[3]
debug = debug_flag == "1"
dbg(f"python helper start hash={new_hash[:8]}… readme={readme_path}", debug)

if not re.fullmatch(r"[0-9a-f]{40}", new_hash):
    err(f"invalid hash passed to python: {new_hash!r}")
    sys.exit(1)

path = Path(readme_path)
try:
    text = path.read_text(encoding="utf-8")
except OSError as exc:
    err(f"cannot read {readme_path}: {exc}")
    sys.exit(2)

dbg(f"read {len(text)} characters from {readme_path}", debug)

if not text.strip():
    err(f"{readme_path} is empty")
    sys.exit(2)

pattern = re.compile(r"(commit\s+`)[0-9a-f]{7,40}(`)", re.IGNORECASE)
matches = list(pattern.finditer(text))
dbg(f"found {len(matches)} existing commit-pin match(es)", debug)
for i, m in enumerate(matches):
    dbg(f"  match[{i}] span={m.span()} text={m.group(0)!r}", debug)

if matches:
    text2, n = pattern.subn(r"\g<1>" + new_hash + r"\2", text)
    if n == 0:
        err("pattern matched but substitution made no changes")
        sys.exit(3)
    action = f"updated {n} existing pin(s)"
    dbg(f"substitution count n={n}", debug)
else:
    needle = "**Research blueprint** (v0.2.0-candidate)"
    dbg(f"no existing pins; looking for version badge {needle!r}", debug)
    if needle in text and f"commit `{new_hash}`" not in text:
        text2 = text.replace(
            needle,
            f"**Research blueprint** (v0.2.0-candidate, commit `{new_hash}`)",
            1,
        )
        action = "inserted new pin next to version badge"
    elif f"commit `{new_hash}`" in text:
        log(f"README.md already pinned to {new_hash[:8]}… ({new_hash})")
        sys.exit(0)
    else:
        err(
            "no commit-hash pattern found and could not insert one "
            f"(expected a 'commit `…`' pin or the version badge {needle!r})"
        )
        sys.exit(3)

if text2 == text:
    log(f"README.md already pinned to {new_hash[:8]}… ({new_hash})")
    sys.exit(0)

dbg(f"writing {len(text2)} characters to {readme_path}", debug)
try:
    path.write_text(text2, encoding="utf-8")
except OSError as exc:
    err(f"cannot write {readme_path}: {exc}")
    sys.exit(2)

try:
    verify = path.read_text(encoding="utf-8")
except OSError as exc:
    err(f"write verification read failed: {exc}")
    sys.exit(4)

dbg(f"verify read {len(verify)} characters", debug)
if new_hash not in verify:
    err("write verification failed \u2014 new hash not present in README")
    sys.exit(4)

post = list(pattern.finditer(verify))
dbg(f"post-write pin count: {len(post)}", debug)

log(f"README.md pinned to {new_hash[:8]}… ({new_hash}) [{action}]")
sys.exit(0)
PY
py_rc=$?
set -e

dbg "python helper exit code: ${py_rc}"

case "${py_rc}" in
  0)
    dbg "success"
    exit 0
    ;;
  1) die 1 "python helper failed (invalid arguments or hash)" ;;
  2) die 2 "README read/write error" ;;
  3) die 3 "no recognizable commit-hash pattern in README" ;;
  4) die 4 "write verification failed" ;;
  *) die 1 "python helper exited with unexpected code ${py_rc}" ;;
esac
