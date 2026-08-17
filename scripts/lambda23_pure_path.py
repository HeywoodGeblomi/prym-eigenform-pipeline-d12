#!/usr/bin/env python3
"""
Milestone A/B scaffold: pure dual-Rauzy path (no bounce) for individual Lyapunov balls.

Does NOT claim certified λ₂/λ₃. Reports interval widths under the stated
error model so we can tighten QR and scale the ensemble.

Teichmüller time must use -log(1 - L_l/L_w) (see code/zorich_kz_ball.py).
This scaffold still uses endpoint dt in the float recorder for path shape only;
production certificates must switch to zorich_kz_ball time.

Usage:
  PYTHONPATH=. python scripts/lambda23_pure_path.py [seed] [n_steps]
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

import mpmath as mp
import numpy as np

from code.ball_matrix import Ball, BallMatrix, log_abs_diag, modified_gs_qr
from code.validated_path_ia import (
    TOP0,
    BOT0,
    N,
    dual_exact,
    top_move,
    bot_move,
    normalize_balls,
)


def record_pure_path(n_steps: int, seed: int) -> Tuple[list, np.ndarray, np.ndarray, float]:
    """Pure Rauzy only — no length bounce / artificial restart."""
    rng = np.random.RandomState(seed)
    lengths = rng.dirichlet(np.ones(N))
    top, bot = list(TOP0), list(BOT0)
    path = []
    init_lengths = lengths.copy()
    cocycle = np.eye(N)
    log_sing = np.zeros(N)
    total_t = 0.0
    for step in range(1, n_steps + 1):
        if lengths[top[-1]] > lengths[bot[-1]]:
            which = "top"
            top, bot, M, w, l = top_move(top, bot)
        else:
            which = "bot"
            top, bot, M, w, l = bot_move(top, bot)
        Lw, Ll = float(lengths[w]), float(lengths[l])
        # proper Teichmüller increment when Lw > Ll
        ratio = min(max(Ll / max(Lw, 1e-300), 0.0), 1.0 - 1e-15)
        dt = float(-np.log(max(1.0 - ratio, 1e-300)))
        total_t += dt
        path.append({"which": which, "w": int(w), "l": int(l), "dt": dt, "Lw": Lw, "Ll": Ll})
        lengths = np.abs(M @ lengths)
        lengths /= lengths.sum()
        cocycle = np.linalg.inv(M).T @ cocycle
        if step % 50 == 0:
            q, r = np.linalg.qr(cocycle)
            log_sing += np.log(np.maximum(np.abs(np.diag(r)), 1e-300))
            cocycle = q
    q, r = np.linalg.qr(cocycle)
    log_sing += np.log(np.maximum(np.abs(np.diag(r)), 1e-300))
    lyap = np.sort(log_sing / max(total_t, 1e-15))[::-1]
    return path, init_lengths, lyap, total_t


def validate_pure(
    path,
    init_lengths: np.ndarray,
    length_rad: float = 1e-16,
    qr_eps: float = 1e-14,
    dps: int = 30,
    reorth_every: int = 50,
) -> Dict[str, Any]:
    mp.mp.dps = dps
    lengths = normalize_balls(
        [Ball(mp.mpf(float(x)), mp.mpf(length_rad)) for x in init_lengths]
    )
    top, bot = list(TOP0), list(BOT0)
    cocycle = BallMatrix.identity(N)
    log_sing = [Ball.exact(0) for _ in range(N)]
    total_t = Ball.exact(0)
    min_gap = float("inf")
    n_moves = 0

    for entry in path:
        which, w, l, dt = entry["which"], entry["w"], entry["l"], entry["dt"]
        L_top = lengths[top[-1]]
        L_bot = lengths[bot[-1]]
        if which == "top":
            winner, loser = L_top, L_bot
        else:
            winner, loser = L_bot, L_top
        gap = float(winner.lo() - loser.hi())
        min_gap = min(min_gap, gap)
        if winner.lo() <= loser.hi():
            return {
                "validated": False,
                "reason": f"ambiguous at move {n_moves} gap={gap:.3e}",
                "n_moves": n_moves,
                "min_gap": min_gap,
            }
        D = dual_exact(w, l)
        cocycle = D @ cocycle
        total_t = total_t + Ball.exact(dt)
        rows = [[Ball.exact(1 if i == j else 0) for j in range(N)] for i in range(N)]
        rows[w][l] = Ball.exact(1)
        M = BallMatrix(rows)
        lengths = M.matvec(lengths)
        lengths = [Ball(abs(x.mid), x.rad) for x in lengths]
        lengths = normalize_balls(lengths)
        if which == "top":
            top, bot, _, _, _ = top_move(top, bot)
        else:
            top, bot, _, _, _ = bot_move(top, bot)
        n_moves += 1
        if n_moves % reorth_every == 0:
            Q, R = modified_gs_qr(cocycle)
            logs = log_abs_diag(R)
            for i in range(N):
                logs[i] = Ball(logs[i].mid, logs[i].rad + qr_eps)
                log_sing[i] = log_sing[i] + logs[i]
            cocycle = Q

    Q, R = modified_gs_qr(cocycle)
    logs = log_abs_diag(R)
    for i in range(N):
        logs[i] = Ball(logs[i].mid, logs[i].rad + qr_eps)
        log_sing[i] = log_sing[i] + logs[i]

    Tm = float(total_t.mid) if float(total_t.mid) > 0 else 1.0
    pairs = sorted(
        [
            Ball(
                log_sing[i].mid / Tm,
                log_sing[i].rad / Tm
                + abs(log_sing[i].mid) * float(total_t.rad) / (Tm * Tm + 1e-30),
            )
            for i in range(N)
        ],
        key=lambda b: float(b.mid),
        reverse=True,
    )

    def ball_dict(b: Ball) -> Dict[str, float]:
        return {
            "mid": float(b.mid),
            "rad": float(b.rad),
            "lo": float(b.lo()),
            "hi": float(b.hi()),
        }

    return {
        "validated": True,
        "n_moves": n_moves,
        "min_gap": min_gap,
        "length_rad": length_rad,
        "qr_eps": qr_eps,
        "T": ball_dict(total_t),
        "lyap_sorted": [ball_dict(b) for b in pairs],
        "lambda1_ball": ball_dict(pairs[0]),
        "lambda2_ball": ball_dict(pairs[1]),
        "lambda3_ball": ball_dict(pairs[2]),
        "note": "Experimental individual balls under modified_gs_qr. Not certified.",
        "sum_non_taut_target": 0.6,
    }


def main():
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 728
    n_steps = int(sys.argv[2]) if len(sys.argv) > 2 else 2000
    print(f"pure path seed={seed} steps={n_steps}", flush=True)
    path, init_L, float_lyap, T = record_pure_path(n_steps, seed)
    print(f"float lyap={np.round(float_lyap, 5)} T={T:.3f}", flush=True)

    results = []
    for lr in [1e-18, 1e-16, 1e-14, 1e-12]:
        r = validate_pure(path, init_L, length_rad=lr)
        status = "VALID" if r.get("validated") else "FAIL"
        print(f"  lr={lr:.0e} {status}", end="", flush=True)
        if r.get("validated"):
            print(
                f" min_gap={r['min_gap']:.3e} "
                f"λ1≈{r['lambda1_ball']['mid']:.4f}±{r['lambda1_ball']['rad']:.2e} "
                f"λ2≈{r['lambda2_ball']['mid']:.4f}±{r['lambda2_ball']['rad']:.2e} "
                f"λ3≈{r['lambda3_ball']['mid']:.4f}±{r['lambda3_ball']['rad']:.2e}",
                flush=True,
            )
        else:
            print(f" {r.get('reason')}", flush=True)
        results.append(r)

    out = {
        "seed": seed,
        "n_steps": n_steps,
        "float_lyap": float_lyap.tolist(),
        "T_float": T,
        "attempts": results,
        "promote_ready": False,
        "scope": "Milestone A pure-path dual; individuals experimental until QR radii controlled",
    }
    Path("data").mkdir(exist_ok=True)
    Path("data/lambda23_pure_path.json").write_text(json.dumps(out, indent=2) + "\n")
    print("wrote data/lambda23_pure_path.json", flush=True)


if __name__ == "__main__":
    main()
