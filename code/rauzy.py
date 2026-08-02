"""Prym-compatible Rauzy generators (minimal set) for D=12."""
import numpy as np

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


def kz(A):
    """Kontsevich–Zorich action on cohomology: (A^{-1})^T."""
    return np.linalg.inv(A).T


def choose_move(lengths):
    """Pick top or bot generator from current projective lengths."""
    if lengths[0] + lengths[2] > lengths[1] + lengths[3]:
        return A_top
    return A_bot
