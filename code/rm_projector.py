"""Exact real-multiplication projector for the D=12 Prym prototype."""
import numpy as np

D = 12
e = 2
w = 1
h = 1
lam = 1.0 + np.sqrt(3.0)
lam_conj = 1.0 - np.sqrt(3.0)

T = np.array(
    [
        [2.0, 0.0, 2.0, 0.0],
        [0.0, 2.0, 0.0, 2.0],
        [1.0, 0.0, 0.0, 0.0],
        [0.0, 1.0, 0.0, 0.0],
    ],
    dtype=float,
)

I4 = np.eye(4)
P_lam = (T - lam_conj * I4) / (lam - lam_conj)


def project(v):
    """Project a vector onto the lambda-eigenspace of T."""
    return P_lam @ np.asarray(v, dtype=float)


def residual_minimal_polynomial():
    """||T^2 - e T - 2wh I||; should be 0 for the exact model."""
    return float(np.linalg.norm(T @ T - e * T - 2 * w * h * I4))


def is_eigenvector(v, tol=1e-10):
    """Return True if T v = lam v within tolerance."""
    v = np.asarray(v, dtype=float)
    return float(np.linalg.norm(T @ v - lam * v)) < tol
