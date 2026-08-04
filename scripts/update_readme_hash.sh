#!/usr/bin/env bash
# Update the pinned commit hash in README.md to the current HEAD.
# Usage (from repo root, after committing other changes):
#   ./scripts/update_readme_hash.sh
# Then commit the README change if the hash moved.
set -euo pipefail

ROOT="$(git rev-parse --show-toplevel 2>/dev/null || true)"
if [[ -z "${ROOT}" ]]; then
  echo "error: not inside a git repository" >&2
  exit 1
fi
cd "${ROOT}"

HASH="$(git rev-parse HEAD)"
SHORT="${HASH:0:8}"
README="README.md"

if [[ ! -f "${README}" ]]; then
  echo "error: ${README} not found" >&2
  exit 1
fi

python3 - << PY
from pathlib import Path
import re

readme = Path("README.md")
text = readme.read_text()
new_hash = "${HASH}"

# Replace full or short hashes in backtick commit pins
text2 = re.sub(
    r"(commit\s+\`)[0-9a-f]{7,40}(\`)",
    r"\g<1>" + new_hash + r"\2",
    text,
    flags=re.IGNORECASE,
)

if text2 == text:
    if "commit \`" not in text:
        text2 = text.replace(
            "**Research blueprint** (v0.2.0-candidate)",
            f"**Research blueprint** (v0.2.0-candidate, commit \`{new_hash}\`)",
            1,
        )
    else:
        print("no commit-hash pattern found to update")
        raise SystemExit(0)

readme.write_text(text2)
print(f"README.md pinned to {new_hash[:8]}\u2026 ({new_hash})")
PY
