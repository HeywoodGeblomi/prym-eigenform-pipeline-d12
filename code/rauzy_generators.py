"""
Rauzy / KZ generators for the residual-0 linear model.

Single responsibility: define raw and plane-constrained transition matrices.
Graph enumeration lives in enumerate_rauzy_graph.py.
Verification lives in verify.py / interval_verify.py.
"""
from __future__ import annotations

import numpy as np

from .rm_projector import P_lam, I4

# ------------------------------------------------------------------
# Raw unimodular generators (linear model)
# ------------------------------------------------------------------
A_top = np.array(
    [
        [1.0, 0.0, 1.0, 0.0],
        [0.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0],
    ],
    dtype=float,
)
A_bot = np.array(
    [
        [1.0, 0.0, 0.0, 0.0],
        [0.0, 1.0, 0.0, 1.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0],
    ],
    dtype=float,
)
# Label exchange (Prym involution on labels 0 <-> 1)
S = np.array(
    [
        [0.0, 1.0, 0.0, 0.0],
        [1.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0],
    ],
    dtype=float,
)
A_top_sym = S @ A_top @ S
A_bot_sym = S @ A_bot @ S


def constrain(A: np.ndarray) -> np.ndarray:
    """Simultaneous projection onto lambda-eigenspace and its complement."""
    return P_lam @ A @ P_lam + (I4 - P_lam) @ A @ (I4 - P_lam)


A_top_corr = constrain(A_top)
A_bot_corr = constrain(A_bot)
S_corr = constrain(S)
A_top_sym_corr = constrain(A_top_sym)
A_bot_sym_corr = constrain(A_bot_sym)

GENERATORS_CORR = [A_top_corr, A_bot_corr, S_corr]
GENERATORS_RAW = [A_top, A_bot, S]


def kz(A: np.ndarray) -> np.ndarray:
    """Kontsevich–Zorich action on cohomology: (A^{-1})^T."""
    return np.linalg.inv(A).T


def choose_move(lengths, use_corrected: bool = False):
    """Pick top or bot generator from current projective lengths."""
    if lengths[0] + lengths[2] > lengths[1] + lengths[3]:
        return A_top_corr if use_corrected else A_top
    return A_bot_corr if use_corrected else A_bot
