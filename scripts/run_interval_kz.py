#!/usr/bin/env python3
"""
Smoke runner for ball-arithmetic KZ enclosures.

Usage (from repo root, after copying packet files into place):

  python scripts/run_interval_kz.py --steps 500 --dps 30
  python scripts/run_interval_kz.py --steps 2000 --dps 40 --json-out data/interval_kz_smoke.json

Exit codes:
  0 = run completed (check promote_ready in JSON)
  1 = numerical failure (zero in denominator, etc.)
  2 = usage / import error
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


def main() -> int:
    p = argparse.ArgumentParser(description="Ball-arithmetic KZ smoke run")
    p.add_argument("--steps", type=int, default=500)
    p.add_argument("--reorth", type=int, default=50)
    p.add_argument("--dps", type=int, default=30)
    p.add_argument("--json-out", type=str, default=None)
    args = p.parse_args()

    try:
        from code.integrator_ball import run_ball
    except ImportError:
        # packet-local import when run from ENGINEER_PACKET/
        sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "code"))
        try:
            from integrator_ball import run_ball  # type: ignore
        except ImportError as e:
            print(f"Import failed: {e}", file=sys.stderr)
            print(
                "Copy code/ball_matrix.py and code/integrator_ball.py into the repo first.",
                file=sys.stderr,
            )
            return 2

    report = run_ball(n_steps=args.steps, reorth_every=args.reorth, dps=args.dps)
    text = json.dumps(report, indent=2)
    print(text)
    if args.json_out:
        out = Path(args.json_out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text)
        print(f"Wrote {out}", file=sys.stderr)

    if not report.get("ok"):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
