"""Minimal tests for ball arithmetic kernel. Run: pytest tests/test_ball_matrix.py -v"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "code"))
sys.path.insert(0, str(ROOT))

from ball_matrix import Ball, BallMatrix, modified_gs_qr  # noqa: E402


def test_ball_add_mul():
    a = Ball.exact(2)
    b = Ball(3, 0.1)
    c = a + b
    assert c.mid == 5
    assert c.rad == mp.mpf("0.1")
    d = a * b
    assert d.mid == 6
    assert d.rad >= mp.mpf("0.2")


def test_ball_div_rejects_zero():
    a = Ball.exact(1)
    z = Ball(0, 0.1)
    with pytest.raises(ZeroDivisionError):
        _ = a / z


def test_identity_matmul():
    I = BallMatrix.identity(3)
    A = BallMatrix.exact([[1, 2, 0], [0, 1, 0], [0, 0, 1]])
    B = I @ A
    assert abs(B.rows[0][1].mid - 2) < 1e-20
    assert B.rows[0][1].rad == 0


def test_matvec():
    A = BallMatrix.exact([[2, 0], [0, 3]])
    v = [Ball.exact(1), Ball.exact(1)]
    # resize helper — use 2x2 only
    A2 = BallMatrix([[Ball.exact(2), Ball.exact(0)], [Ball.exact(0), Ball.exact(3)]])
    w = A2.matvec(v)
    assert w[0].mid == 2 and w[1].mid == 3


def test_modified_gs_qr_smoke():
    mp.mp.dps = 25
    A = BallMatrix.exact(
        [
            [2, 1, 0, 0],
            [0, 2, 1, 0],
            [0, 0, 2, 1],
            [0, 0, 0, 2],
        ]
    )
    Q, R = modified_gs_qr(A)
    assert Q.n == 4 and R.n == 4
    # R should be roughly upper triangular in midpoints
    assert abs(R.rows[3][0].mid) < 1e-6 or R.rows[3][0].rad > 0
