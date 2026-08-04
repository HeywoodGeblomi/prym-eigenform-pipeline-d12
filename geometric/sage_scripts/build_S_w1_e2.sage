#!/usr/bin/env sage
"""Build S(w=1,e=±2) export scaffold. Requires SageMath + surface_dynamics/flatsurf.
Run on a Sage-enabled machine; fill pairings/permutation for Gate 1 PASS.
"""
from __future__ import print_function
import json, os
from pathlib import Path

w, e = 1, 2
D = e**2 + 8*w
K.<sqrtD> = QuadraticField(D)
lam = (e + sqrtD) / 2
print("D =", D, "lambda =", lam)

OUT = Path(os.environ.get("PRYM_EXPORT_DIR", "geometric/flatsurf_export"))
OUT.mkdir(parents=True, exist_ok=True)

def try_surface_dynamics():
    try:
        from surface_dynamics.all import *
        print("surface_dynamics imported")
        return {"package": "surface_dynamics", "status": "imported_only"}
    except ImportError:
        print("surface_dynamics not available")
        return None

def try_flatsurf():
    try:
        import flatsurf
        print("flatsurf imported")
        return {"package": "flatsurf", "status": "imported_only"}
    except ImportError:
        print("flatsurf not available")
        return None

def pure_coordinate_model():
    return {
        "w": w, "e": e, "D": D, "lambda_exact": str(lam),
        "construction": "lambda x lambda square + two w x 1 rectangles",
        "horizontal_cylinders": [
            {"name": "long_1", "width": w, "height": 1},
            {"name": "long_2", "width": w, "height": 1},
            {"name": "short", "width": str(lam), "height": str(lam)},
        ],
        "note": "Fill generalized_permutation after polygon glueing in flatsurf/surface_dynamics.",
    }

report = {
    "goal": "horizontal return map for S(1, ±2)",
    "surface_dynamics": try_surface_dynamics(),
    "flatsurf": try_flatsurf(),
    "pure_coordinate_model": pure_coordinate_model(),
    "generalized_permutation": None,
    "side_pairings": None,
    "gate1": "PASS only if generalized_permutation is non-null",
}
with open(OUT / "sage_run_report.json", "w") as f:
    json.dump(report, f, indent=2, default=str)
print("Wrote", OUT / "sage_run_report.json")
raise SystemExit(0 if report["generalized_permutation"] else 1)
