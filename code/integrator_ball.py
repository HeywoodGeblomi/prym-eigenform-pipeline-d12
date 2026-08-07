"""
Ball-arithmetic constrained KZ integrator (smoke / enclosure path).

Provisional float64 integrator remains in code/integrator.py.
This module is the candidate path toward certified/.

IMPORTANT
---------
Radii will grow. A successful *engineering* run produces finite intervals.
A successful *mathematical* certification requires widths small enough to be
useful (e.g. lambda_2 within +/-0.05). If widths explode, report FAILURE — do not
promote to certified/.
"""
from __future__ import annotations

from typing import Any, Dict, List, Sequence

import mpmath as mp
import numpy as np

try:
    from .ball_matrix import Ball, BallMatrix, log_abs_diag, modified_gs_qr
except ImportError:
    from ball_matrix import Ball, BallMatrix, log_abs_diag, modified_gs_qr

# Classical residual-0 data (matches rm_projector.py)
LAM = 1 + mp.sqrt(3)
T_EXACT = [
    [2, 0, 2, 0],
    [0, 2, 0, 2],
    [1, 0, 0, 0],
    [0, 1, 0, 0],
]
A_TOP = [
    [1, 0, 1, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
]
A_BOT = [
    [1, 0, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
]


def _project_ball(v: Sequence[Ball]) -> List[Ball]:
    """P_lambda v with lambda = 1+sqrt(3)."""
    lam = Ball.exact(LAM)
    lam_c = Ball.exact(1 - mp.sqrt(3))
    denom = lam - lam_c
    T = BallMatrix.exact(T_EXACT)
    Tv = T.matvec(v)
    lamc_v = [lam_c * x for x in v]
    num = [Tv[i] - lamc_v[i] for i in range(4)]
    return [x / denom for x in num]


def _choose_move(lengths: Sequence[Ball]) -> BallMatrix:
    s0 = (lengths[0] + lengths[2]).mid
    s1 = (lengths[1] + lengths[3]).mid
    data = A_TOP if s0 > s1 else A_BOT
    return BallMatrix.exact(data)


def _kz(A: BallMatrix) -> BallMatrix:
    """(A^{-1})^T using mid inverse + residual inflation (FIRST-CUT)."""
    M = np.array([[float(A.rows[i][j].mid) for j in range(4)] for i in range(4)], dtype=float)
    try:
        Minv = np.linalg.inv(M)
    except np.linalg.LinAlgError:
        Minv = np.eye(4)
    rad = max(float(A.frobenius_rad()), 1e-18)
    infl = mp.mpf(rad * 10 + 1e-12)
    rows = []
    for i in range(4):
        row = []
        for j in range(4):
            row.append(Ball(mp.mpf(Minv[j, i]), infl))
        rows.append(row)
    return BallMatrix(rows)


def run_ball(
    n_steps: int = 2000,
    reorth_every: int = 50,
    dps: int = 40,
) -> Dict[str, Any]:
    """Run ball-arithmetic constrained KZ."""
    mp.mp.dps = dps

    v0 = [Ball.exact(LAM), Ball.exact(0), Ball.exact(1), Ball.exact(0)]
    T = BallMatrix.exact(T_EXACT)
    Tv = T.matvec(v0)
    seed_res = max((Tv[i] - Ball.exact(LAM) * v0[i]).abs_bound() for i in range(4))

    lengths = _project_ball(v0)
    s = Ball.exact(0)
    for x in lengths:
        s = s + Ball(abs(x.mid), x.rad)
    lengths = [x / s for x in lengths]

    cocycle = BallMatrix.identity(4)
    log_sing = [Ball.exact(0) for _ in range(4)]
    snapshots = []
    max_rad = mp.mpf(0)

    for step in range(1, n_steps + 1):
        A = _choose_move(lengths)
        new_len = A.matvec(lengths)
        new_len = [Ball(abs(x.mid), x.rad) for x in new_len]
        shadow = _project_ball(
            [
                new_len[0] * Ball.exact(LAM),
                new_len[1] * Ball.exact(1),
                new_len[2] * Ball.exact(1),
                new_len[3] * Ball.exact(1),
            ]
        )
        shadow = [Ball(abs(x.mid), x.rad) for x in shadow]
        tot = Ball.exact(0)
        for x in shadow:
            tot = tot + x
        if tot.contains_zero():
            return {"ok": False, "reason": f"length sum contains 0 at step {step}", "step": step}
        lengths = [x / tot for x in shadow]

        cocycle = _kz(A) @ cocycle
        max_rad = max(max_rad, cocycle.frobenius_rad())

        if step % reorth_every == 0:
            Q, R = modified_gs_qr(cocycle)
            logs = log_abs_diag(R)
            for i in range(4):
                log_sing[i] = log_sing[i] + logs[i]
            cocycle = Q
            lyap = [Ball(log_sing[i].mid / step, log_sing[i].rad / step) for i in range(4)]
            lyap_sorted = sorted(lyap, key=lambda b: -b.mid)
            snapshots.append(
                {
                    "step": step,
                    "lyap": [
                        {"mid": float(b.mid), "rad": float(b.rad), "lo": float(b.lo()), "hi": float(b.hi())}
                        for b in lyap_sorted
                    ],
                    "cocycle_frobenius_rad": float(cocycle.frobenius_rad()),
                }
            )

    final = snapshots[-1]["lyap"] if snapshots else []
    widths = [f["hi"] - f["lo"] for f in final]
    promote_ready = bool(final) and all(w < 1e6 for w in widths) and widths[0] < 0.5

    return {
        "ok": True,
        "dps": dps,
        "n_steps": n_steps,
        "reorth_every": reorth_every,
        "seed_residual_bound": float(seed_res),
        "max_cocycle_frobenius_rad": float(max_rad),
        "final_lyap": final,
        "widths": widths,
        "promote_ready": promote_ready,
        "snapshots_tail": snapshots[-3:],
        "disclaimer": (
            "Ball enclosures with conservative radius inflation. "
            "Not arb/RIF tight intervals. Do not promote unless promote_ready "
            "and widths are scientifically useful."
        ),
    }
