"""Algebraic verification predicates for candidate Rauzy/transition matrices.
These must hold for any matrix belonging to a genuine Prym + RM Rauzy class.
"""
import numpy as np
from .rm_projector import P_lam, T

def preserves_eigenplane(A, tol=1e-10):
    """A maps the λ-eigenspace into itself: residual of (I-P) A P."""
    residual = np.linalg.norm((np.eye(4) - P_lam) @ A @ P_lam)
    return residual < tol, float(residual)

def prym_compatible(A, S, tol=1e-10):
    """Commutes with or is conjugate under the Prym matrix S."""
    residual_comm = np.linalg.norm(S @ A - A @ S)
    residual_conj = np.linalg.norm(S @ A @ S - A)
    r = min(residual_comm, residual_conj)
    return r < tol, float(r)

def is_unimodular(A, tol=1e-10):
    d = float(np.linalg.det(A))
    return abs(abs(d) - 1.0) < tol, d

def full_check(A, S=None, tol=1e-10):
    plane_ok, plane_res = preserves_eigenplane(A, tol)
    uni_ok, det = is_unimodular(A, tol)
    out = {
        "preserves_eigenplane": bool(plane_ok),
        "plane_residual": plane_res,
        "unimodular": bool(uni_ok),
        "det": det,
    }
    if S is not None:
        prym_ok, prym_res = prym_compatible(A, S, tol)
        out["prym_compatible"] = bool(prym_ok)
        out["prym_residual"] = prym_res
    return out

if __name__ == "__main__":
    from .rauzy import A_top, A_bot, A_top_sym, A_bot_sym, S
    print("Verification on linear-model generators (expect plane residual > 0):")
    for name, A in [("A_top", A_top), ("A_bot", A_bot),
                    ("A_top_sym", A_top_sym), ("A_bot_sym", A_bot_sym)]:
        print(f"  {name}: {full_check(A, S)}")
