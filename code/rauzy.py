"""Prym-compatible Rauzy generators for the D=12 linear model.

Raw generators are integer/unimodular (det = +/-1) and are the default
for the constrained integrator (eigenplane enforced by continuous
re-projection).

Corrected generators are the simultaneous projection of each raw
generator onto the lambda-eigenspace and its complement; they satisfy
preserves_eigenplane to residual ~1e-16 and are intended for algebraic
checks and monoid filtering.
"""
import numpy as np

from .rm_projector import P_lam

I4 = np.eye(4)

# ------------------------------------------------------------------
# Raw (unimodular) generators
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

# Outer-exchange conjugates (Prym involution on labels 0 <-> 1)
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

# ------------------------------------------------------------------
# Corrected (plane-preserving) generators
# ------------------------------------------------------------------
def _constrain(A):
    """Simultaneous projection onto lambda-eigenspace and its complement."""
    return P_lam @ A @ P_lam + (I4 - P_lam) @ A @ (I4 - P_lam)

A_top_corr = _constrain(A_top)
A_bot_corr = _constrain(A_bot)
S_corr = _constrain(S)
A_top_sym_corr = _constrain(A_top_sym)
A_bot_sym_corr = _constrain(A_bot_sym)

# Default list used by algebraic filters / monoid generation
GENERATORS_CORR = [A_top_corr, A_bot_corr, S_corr]
GENERATORS_RAW = [A_top, A_bot, S]


def kz(A):
    """Kontsevich-Zorich action on cohomology: (A^{-1})^T."""
    return np.linalg.inv(A).T


def choose_move(lengths, use_corrected=False):
    """Pick top or bot generator from current projective lengths.

    Default uses the raw unimodular generators so that the integrator
    preserves the +/- Lyapunov symmetry.  Pass use_corrected=True to
    obtain the plane-preserving versions for algebraic checks.
    """
    if lengths[0] + lengths[2] > lengths[1] + lengths[3]:
        return A_top_corr if use_corrected else A_top
    return A_bot_corr if use_corrected else A_bot
