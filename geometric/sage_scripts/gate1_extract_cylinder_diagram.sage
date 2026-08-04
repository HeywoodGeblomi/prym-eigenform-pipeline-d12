#!/usr/bin/env sage
# Gate 1: extract CylinderDiagram FROM surface. No hardcoded perm. No projector.
from sage.all import *
import json
from pathlib import Path

w,h,t,e = 1,1,0,-2
lam = -1 + sqrt(3)
T_Ap = matrix(QQ, [[e,0,2*w,2*t],[0,e,0,2*h],[h,-t,0,0],[0,w,0,0]])
p = vector([lam,0,1,0])
export = {"projector_called": False, "gate1_ready": False}
export["native_residual_T_period"] = float((T_Ap*p - lam*p).norm())
print("Native residual", export["native_residual_T_period"])

try:
    from surface_dynamics.all import CylinderDiagram
    export["surface_dynamics"] = "available"
    print("surface_dynamics OK — instantiate cd from EXTRACTED cycles only")
except ImportError as ex:
    export["surface_dynamics"] = str(ex)

try:
    from flatsurf import *
    export["flatsurf"] = "available"
    print("flatsurf OK — build T, call T.cylinder_decomposition(direction=(1,0))")
except ImportError as ex:
    export["flatsurf"] = str(ex)

export["independence_rule"] = "cycles from cd.bot/top_cycle_tuples or flatsurf decomp only"
Path("geometric").mkdir(exist_ok=True)
json.dump(export, open("geometric/flatsurf_independent_export.json","w"), indent=2)
print("Wrote geometric/flatsurf_independent_export.json; gate1_ready=False until extraction")
