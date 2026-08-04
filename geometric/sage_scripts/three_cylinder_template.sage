#!/usr/bin/env sage
# Three-cylinder template for D=12. Prototype LOCKED: (1,1,0,-2), lambda=-1+sqrt(3).
# CylinderDiagram string is TEMPLATE only — replace before Gate 1 PASS.
from surface_dynamics.all import *
from sage.all import *

w, h, t, e = 1, 1, 0, -2
D = e**2 + 8*w*h
K.<sqrt3> = NumberField(x**2 - 3, embedding=AA(3).sqrt())
lam = -1 + sqrt3
print("D =", D, "lambda =", lam)

c = CylinderDiagram('(0,1)-(0,2) (2,3)-(1,3) (4)-(4)')  # TEMPLATE
print("[TEMPLATE]", c, c.stratum())

T_Ap = matrix(QQ, 4, 4, [[e,0,2*w,2*t],[0,e,0,2*h],[h,-t,0,0],[0,w,0,0]])
R = T_Ap**2 - e*T_Ap - 2*w*h*identity_matrix(QQ,4)
print("T residual:", R.list())
print("Gate 1 OPEN until true diagram + permutation exported.")
