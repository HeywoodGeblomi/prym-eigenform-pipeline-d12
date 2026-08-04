#!/usr/bin/env bash
# Update the pinned commit hash in README.md to the current HEAD.
#
# Usage:
#   ./scripts/update_readme_hash.sh
#   DEBUG=1 ./scripts/update_readme_hash.sh
#   LOG_FORMAT=json ./scripts/update_readme_hash.sh
#
# Environment:
#   DEBUG=1          emit DEBUG-level events
#   QUIET=1          suppress INFO (ERROR/WARN still shown)
#   LOG_FORMAT=text  human-readable lines (default)
#   LOG_FORMAT=json  one JSON object per line (structured)
#
# Exit codes: 0 success, 1 env error, 2 README I/O, 3 no pattern, 4 verify failed

set -euo pipefail

DEBUG="${DEBUG:-0}"
QUIET="${QUIET:-0}"
LOG_FORMAT="${LOG_FORMAT:-text}"

ts() { date -u +"%Y-%m-%dT%H:%M:%SZ"; }

_log_emit() {
  local level="$1"; shift
  local msg="$1"; shift || true
  if [[ "${LOG_FORMAT}" == "json" ]]; then
    python3 -c '
import json,sys
level,msg,ts=sys.argv[1],sys.argv[2],sys.argv[3]
fields={"ts":ts,"level":level,"msg":msg,"component":"update_readme_hash"}
for pair in sys.argv[4:]:
    if "=" in pair:
        k,v=pair.split("=",1); fields[k]=v
print(json.dumps(fields,ensure_ascii=False))
' "${level}" "${msg}" "$(ts)" "$@" >&2
  else
    local extra=""
    [[ "$#" -gt 0 ]] && extra=" $*"
    echo "[$(ts)] ${level}  ${msg}${extra}" >&2
  fi
}

log_info()  { [[ "${QUIET}" != "1" ]] && _log_emit "INFO" "$@" || true; }
log_debug() { [[ "${DEBUG}" == "1" ]] && _log_emit "DEBUG" "$@" || true; }
log_warn()  { _log_emit "WARN" "$@"; }
log_error() { _log_emit "ERROR" "$@"; }

die() {
  local code="$1"; shift
  log_error "$*" "exit_code=${code}"
  exit "${code}"
}

need_cmd() {
  log_debug "checking command" "cmd=$1"
  command -v "$1" >/dev/null 2>&1 || die 1 "required command not found: $1" "cmd=$1"
}

need_cmd git
need_cmd python3
log_debug "tools available" "git=$(command -v git)" "python3=$(command -v python3)"

ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || die 1 "not inside a git repository"
log_debug "repository root resolved" "root=${ROOT}"
cd "${ROOT}" || die 1 "cannot cd to repository root" "root=${ROOT}"

BRANCH="$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo "?")"
log_debug "branch resolved" "branch=${BRANCH}"
[[ "${BRANCH}" == "HEAD" ]] && log_warn "detached HEAD"

HASH="$(git rev-parse HEAD 2>/dev/null)" || die 1 "git rev-parse HEAD failed"
[[ "${HASH}" =~ ^[0-9a-f]{40}$ ]] || die 1 "HEAD does not look like a full SHA-1" "hash=${HASH}"
log_info "pinning README" "hash=${HASH}" "short=${HASH:0:8}"

README="README.md"
[[ -f "${README}" ]] || die 2 "README not found" "path=${ROOT}/${README}"
[[ -r "${README}" ]] || die 2 "README not readable" "path=${README}"
[[ -w "${README}" ]] || die 2 "README not writable" "path=${README}"
log_debug "README ready" "path=${README}" "bytes=$(wc -c < "${README}" | tr -d ' ')"

set +e
python3 - "${HASH}" "${README}" "${DEBUG}" "${LOG_FORMAT}" <<'PY'
import json, re, sys
from datetime import datetime, timezone
from pathlib import Path

def ts():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

def emit(level, msg, fmt, **fields):
    if fmt == "json":
        rec = {"ts": ts(), "level": level, "msg": msg, "component": "update_readme_hash.python"}
        rec.update(fields)
        print(json.dumps(rec, ensure_ascii=False), file=sys.stderr)
    else:
        extra = " ".join(f"{k}={v}" for k, v in fields.items())
        print(f"[{ts()}] {level:5} {msg}" + (f" {extra}" if extra else ""), file=sys.stderr)

if len(sys.argv) != 5:
    emit("ERROR", "internal usage: python3 - HASH README DEBUG LOG_FORMAT", "text")
    sys.exit(1)

new_hash, readme_path, debug_flag, log_format = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
debug = debug_flag == "1"

def info(msg, **f): emit("INFO", msg, log_format, **f)
def dbg(msg, **f):
    if debug: emit("DEBUG", msg, log_format, **f)
def err(msg, **f): emit("ERROR", msg, log_format, **f)

dbg("python helper start", hash=new_hash[:8], readme=readme_path)
if not re.fullmatch(r"[0-9a-f]{40}", new_hash):
    err("invalid hash", hash=repr(new_hash)); sys.exit(1)

path = Path(readme_path)
try:
    text = path.read_text(encoding="utf-8")
except OSError as exc:
    err("cannot read README", path=readme_path, error=str(exc)); sys.exit(2)

dbg("readme loaded", chars=len(text))
if not text.strip():
    err("README is empty", path=readme_path); sys.exit(2)

pattern = re.compile(r"(commit\s+`)[0-9a-f]{7,40}(`)", re.IGNORECASE)
matches = list(pattern.finditer(text))
dbg("pin scan complete", match_count=len(matches))
for i, m in enumerate(matches):
    dbg("pin match", index=i, span=str(m.span()), text=m.group(0))

if matches:
    text2, n = pattern.subn(r"\g<1>" + new_hash + r"\2", text)
    if n == 0:
        err("pattern matched but substitution made no changes"); sys.exit(3)
    action = f"updated {n} existing pin(s)"
    dbg("substitution done", count=n)
else:
    needle = "**Research blueprint** (v0.2.0-candidate)"
    if needle in text and f"commit `{new_hash}`" not in text:
        text2 = text.replace(needle, f"**Research blueprint** (v0.2.0-candidate, commit `{new_hash}`)", 1)
        action = "inserted new pin next to version badge"
    elif f"commit `{new_hash}`" in text:
        info("README already pinned", hash=new_hash, short=new_hash[:8]); sys.exit(0)
    else:
        err("no commit-hash pattern found and could not insert one"); sys.exit(3)

if text2 == text:
    info("README already pinned", hash=new_hash, short=new_hash[:8]); sys.exit(0)

dbg("writing README", chars=len(text2))
try:
    path.write_text(text2, encoding="utf-8")
except OSError as exc:
    err("cannot write README", error=str(exc)); sys.exit(2)

try:
    verify = path.read_text(encoding="utf-8")
except OSError as exc:
    err("write verification read failed", error=str(exc)); sys.exit(4)

if new_hash not in verify:
    err("write verification failed - new hash not present"); sys.exit(4)

dbg("post-write pin count", count=len(list(pattern.finditer(verify))))
info("README pinned", hash=new_hash, short=new_hash[:8], action=action)
sys.exit(0)
PY
py_rc=$?
set -e
log_debug "python helper finished" "exit_code=${py_rc}"

case "${py_rc}" in
  0) log_debug "success"; exit 0 ;;
  1) die 1 "python helper failed (invalid arguments or hash)" "exit_code=1" ;;
  2) die 2 "README read/write error" "exit_code=2" ;;
  3) die 3 "no recognizable commit-hash pattern in README" "exit_code=3" ;;
  4) die 4 "write verification failed" "exit_code=4" ;;
  *) die 1 "python helper exited with unexpected code" "exit_code=${py_rc}" ;;
esac
