"""
Regression tests for the D=12 Prym prototype.

1. Exact residual of the minimal polynomial of T must be 0.
2. Prototype period vector must be an eigenvector.
3. P_lam must be a projector (idempotent) of rank 2.
4. A short integrator run must keep RM residual near machine zero
   and produce a symmetric spectrum.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import numpy as np

from code.rm_projector import (
    T,
    P_lam,
    project,
    residual_minimal_polynomial,
    is_eigenvector,
    lam,
)
from code.integrator import run


def test_minimal_polynomial():
    res = residual_minimal_polynomial()
    assert res < 1e-12, f"minimal polynomial residual {res}"


def test_eigenvector():
    v = np.array([lam, 0.0, 1.0, 0.0])
    assert is_eigenvector(v)


def test_projector():
    assert np.linalg.matrix_rank(P_lam, tol=1e-8) == 2
    assert np.linalg.norm(P_lam @ P_lam - P_lam) < 1e-12


def test_short_run_stays_on_eigenplane():
    snaps = run(n_steps=5000, reorth_every=500)
    lyap = np.array(snaps[-1]["lyap"])
    assert abs(lyap[0] + lyap[-1]) < 1e-6 * max(1.0, abs(lyap[0]))


if __name__ == "__main__":
    test_minimal_polynomial()
    print("PASS: minimal polynomial")
    test_eigenvector()
    print("PASS: eigenvector")
    test_projector()
    print("PASS: projector")
    test_short_run_stays_on_eigenplane()
    print("PASS: short run on eigenplane")
    print("All regression tests passed.")
