#!/usr/bin/env python3
"""
CLI: rigorous residual-0 certification for a LN prototype.

Usage:
  python scripts/certify_residual0.py              # Gate-1 D=12
  python scripts/certify_residual0.py 12 -2
  python scripts/certify_residual0.py --D 12

Exit code 0 iff all algebraic residuals are certified at working precision.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from code.interval_verify import run_certification_suite
from code.prototype import GATE1, prototype_from_D


def main() -> int:
    p = argparse.ArgumentParser(description="Residual-0 algebraic certification")
    p.add_argument("D", nargs="?", type=int, default=None, help="discriminant")
    p.add_argument("e", nargs="?", type=int, default=None, help="prototype e")
    p.add_argument("--D", dest="D_opt", type=int, default=None)
    p.add_argument("--json-out", type=str, default=None)
    args = p.parse_args()

    D = args.D_opt or args.D or 12
    if args.e is not None:
        e, w, h = args.e, 1, 1
    else:
        try:
            proto = prototype_from_D(D)
            e, w, h = proto.e, proto.w, proto.h
        except (ValueError, NotImplementedError):
            e, w, h = GATE1.e, GATE1.w, GATE1.h

    report = run_certification_suite(D=D, e=e, w=w, h=h)
    text = json.dumps(report, indent=2)
    print(text)
    if args.json_out:
        Path(args.json_out).write_text(text)
        print(f"Wrote {args.json_out}", file=sys.stderr)

    return 0 if report["all_certified"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
