#!/usr/bin/env sage
"""Sketch: construct translation surface from cylinder/polygon data for Gate 1.
Run inside sage-flatsurf. Fill real S(1,±2) data before claiming PASS.
"""
from __future__ import print_function
import json
from pathlib import Path

w, e = 1, 2
D = e**2 + 8 * w
K.<sqrtD> = QuadraticField(D)
lam = (e + sqrtD) / 2
print("D =", D, "lambda =", lam)

OUT = Path("geometric/flatsurf_export")
OUT.mkdir(parents=True, exist_ok=True)

def try_flatsurf_polygons():
    try:
        from flatsurf import Polygon, similarity_surfaces
    except Exception as exc:
        print("flatsurf unavailable:", exc)
        return None
    print("flatsurf imported — fill explicit S(1,±2) vertices before Gate 1 PASS")
    return {"status": "template_only", "package": "flatsurf"}

def try_cylinder_diagram():
    try:
        from surface_dynamics.all import CylinderDiagram
    except Exception as exc:
        print("surface_dynamics unavailable:", exc)
        return None
    print("surface_dynamics imported — supply true CylinderDiagram for D=12")
    return {"status": "template_only", "package": "surface_dynamics"}

report = {
    "goal": "Gate 1 export: generalized permutation for S(1,±2)",
    "D": D, "lambda": str(lam), "w": w, "e": e,
    "flatsurf": try_flatsurf_polygons(),
    "surface_dynamics": try_cylinder_diagram(),
    "generalized_permutation": None,
    "lengths_exact": None,
    "side_pairings": None,
    "note": "Do not write hypothesis (0 1 2 / 2 1 0) unless independently recovered.",
}
path = OUT / "construction_report.json"
with open(path, "w") as f:
    json.dump(report, f, indent=2, default=str)
print("Wrote", path)
raise SystemExit(0 if report["generalized_permutation"] else 1)
