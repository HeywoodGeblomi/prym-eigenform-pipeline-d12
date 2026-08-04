#!/usr/bin/env sage
# Gate 1 independent flatsurf export — D=12 Model A+
# EXTRACT permutation from surface; do NOT hardcode.
# Residual-0 with T_Ap (e=-2), lambda=-1+sqrt(3); NO projector.
from sage.all import *
import json
from pathlib import Path

w, h, t, e = 1, 1, 0, -2
lam = -1 + sqrt(3)
T_Ap = matrix(QQ, [[e,0,2*w,2*t],[0,e,0,2*h],[h,-t,0,0],[0,w,0,0]])
I4 = identity_matrix(QQ, 4)
print("minpoly residual", (T_Ap**2 - e*T_Ap - 2*w*h*I4).norm())

export = {"source": "sage-flatsurf", "projector_called": False, "gate1_ready": False}
export["independence_rule"] = "top/bot MUST be extracted from surface, not hardcoded"

p = vector([lam, 0, 1, 0])
export["period_vector"] = [float(lam), 0.0, 1.0, 0.0]
export["native_residual_T_period"] = float((T_Ap * p - lam * p).norm())
print("Native ||Tp - λp|| =", export["native_residual_T_period"])
print("Build TranslationSurface, EXTRACT return map, write flatsurf_independent_export.json")
print("Set gate1_ready=True only after extraction + residual ~1e-16")

Path("geometric").mkdir(exist_ok=True)
with open("geometric/flatsurf_independent_export.json", "w") as f:
    json.dump(export, f, indent=2)
