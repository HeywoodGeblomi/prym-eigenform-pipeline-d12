# Scripts

## `update_readme_hash.sh`

Rewrites the pinned commit hash in the root `README.md` to the current `HEAD`.

### Basic usage

```bash
./scripts/update_readme_hash.sh
git add README.md
git commit -m "chore: pin README commit hash"
```

### Structured logging

| Variable | Effect |
|----------|--------|
| `DEBUG=1` | Emit DEBUG events (match spans, byte counts, paths) |
| `QUIET=1` | Suppress INFO (ERROR/WARN still shown) |
| `LOG_FORMAT=text` | Human-readable lines (**default**) |
| `LOG_FORMAT=json` | One JSON object per line on stderr |

Examples:

```bash
DEBUG=1 ./scripts/update_readme_hash.sh
LOG_FORMAT=json ./scripts/update_readme_hash.sh
LOG_FORMAT=json DEBUG=1 ./scripts/update_readme_hash.sh 2> hash.log.jsonl
```

JSON fields always include `ts`, `level`, `msg`, `component`, plus event-specific keys
(`hash`, `path`, `exit_code`, `match_count`, …).

### Exit codes

| Code | Meaning |
|------|---------|
| 0 | Success (updated or already current) |
| 1 | Environment / usage error |
| 2 | README I/O error |
| 3 | No commit-hash pattern found |
| 4 | Write verification failed |

The optional GitHub Action `.github/workflows/update-readme-hash.yml` runs the same
step on pushes to `main` and creates a follow-up pin commit when needed.
