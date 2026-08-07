"""
Midpoint–radius ball matrices over mpmath.

A ball is (mid, rad) with rad >= 0 meaning the set { x : |x - mid| <= rad }.
Matrix balls use entrywise radii (conservative; not the tightest spectral norm).

This is the pure-Python path. Swap mid/rad storage for arb/flint later without
changing integrator_ball.py call sites.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List, Sequence, Tuple

import mpmath as mp


def _as_mpf(x) -> mp.mpf:
    return mp.mpf(x)


@dataclass
class Ball:
    mid: mp.mpf
    rad: mp.mpf  # >= 0

    def __post_init__(self):
        self.mid = _as_mpf(self.mid)
        self.rad = abs(_as_mpf(self.rad))

    @classmethod
    def exact(cls, x) -> "Ball":
        return cls(_as_mpf(x), mp.mpf(0))

    @classmethod
    def from_interval(cls, lo, hi) -> "Ball":
        lo, hi = _as_mpf(lo), _as_mpf(hi)
        mid = (lo + hi) / 2
        rad = (hi - lo) / 2
        return cls(mid, abs(rad))

    def lo(self) -> mp.mpf:
        return self.mid - self.rad

    def hi(self) -> mp.mpf:
        return self.mid + self.rad

    def __add__(self, other: "Ball") -> "Ball":
        return Ball(self.mid + other.mid, self.rad + other.rad)

    def __sub__(self, other: "Ball") -> "Ball":
        return Ball(self.mid - other.mid, self.rad + other.rad)

    def __mul__(self, other: "Ball") -> "Ball":
        # | (m1+e1)(m2+e2) - m1 m2 | <= |m1|r2 + |m2|r1 + r1 r2
        m1, r1 = self.mid, self.rad
        m2, r2 = other.mid, other.rad
        return Ball(m1 * m2, abs(m1) * r2 + abs(m2) * r1 + r1 * r2)

    def __truediv__(self, other: "Ball") -> "Ball":
        # require 0 not in other
        if other.lo() <= 0 <= other.hi():
            raise ZeroDivisionError("ball divisor contains 0")
        m, r = other.mid, other.rad
        denom = abs(m) - r
        if denom <= 0:
            raise ZeroDivisionError("ball divisor contains 0")
        inv_mid = 1 / m
        inv_rad = r / (abs(m) * denom)
        return self * Ball(inv_mid, inv_rad)

    def abs_bound(self) -> mp.mpf:
        return abs(self.mid) + self.rad

    def contains_zero(self) -> bool:
        return self.lo() <= 0 <= self.hi()

    def __repr__(self) -> str:
        return f"Ball({self.mid}, ±{self.rad})"


class BallMatrix:
    """n x n ball matrix stored as list of lists of Ball."""

    def __init__(self, rows: Sequence[Sequence[Ball]]):
        self.rows = [[b if isinstance(b, Ball) else Ball.exact(b) for b in row] for row in rows]
        self.n = len(self.rows)
        if any(len(r) != self.n for r in self.rows):
            raise ValueError("only square matrices supported in this sprint")

    @classmethod
    def exact(cls, data: Sequence[Sequence[float]]) -> "BallMatrix":
        return cls([[Ball.exact(x) for x in row] for row in data])

    @classmethod
    def identity(cls, n: int) -> "BallMatrix":
        rows = []
        for i in range(n):
            rows.append([Ball.exact(1 if i == j else 0) for j in range(n)])
        return cls(rows)

    def __matmul__(self, other: "BallMatrix") -> "BallMatrix":
        n = self.n
        out = []
        for i in range(n):
            row = []
            for j in range(n):
                acc = Ball.exact(0)
                for k in range(n):
                    acc = acc + (self.rows[i][k] * other.rows[k][j])
                row.append(acc)
            out.append(row)
        return BallMatrix(out)

    def matvec(self, v: Sequence[Ball]) -> List[Ball]:
        out = []
        for i in range(self.n):
            acc = Ball.exact(0)
            for j in range(self.n):
                acc = acc + (self.rows[i][j] * v[j])
            out.append(acc)
        return out

    def transpose(self) -> "BallMatrix":
        n = self.n
        return BallMatrix([[self.rows[j][i] for j in range(n)] for i in range(n)])

    def frobenius_rad(self) -> mp.mpf:
        s = mp.mpf(0)
        for row in self.rows:
            for b in row:
                s += b.rad * b.rad
        return mp.sqrt(s)

    def mid_matrix_mp(self) -> mp.matrix:
        M = mp.matrix(self.n)
        for i in range(self.n):
            for j in range(self.n):
                M[i, j] = self.rows[i][j].mid
        return M

    def copy(self) -> "BallMatrix":
        return BallMatrix([[Ball(b.mid, b.rad) for b in row] for row in self.rows])


def modified_gs_qr(A: BallMatrix) -> Tuple[BallMatrix, BallMatrix]:
    """
    Modified Gram–Schmidt with radius inflation.

    Returns (Q, R) as BallMatrices such that A ≈ Q R entrywise in the ball sense.
    Not a fully tight interval QR; radii grow. Good enough for smoke enclosures;
    tighten later with arb.
    """
    n = A.n
    V = [[Ball(A.rows[i][j].mid, A.rows[i][j].rad) for i in range(n)] for j in range(n)]
    # V[j] is column j as list of n balls
    Qcols: List[List[Ball]] = []
    R = [[Ball.exact(0) for _ in range(n)] for _ in range(n)]

    for j in range(n):
        v = V[j]
        for i in range(j):
            # r_ij = q_i · v
            rij = Ball.exact(0)
            for k in range(n):
                rij = rij + (Qcols[i][k] * v[k])
            R[i][j] = rij
            # v = v - r_ij * q_i
            for k in range(n):
                v[k] = v[k] - (rij * Qcols[i][k])
        # r_jj = ||v||
        norm_sq = Ball.exact(0)
        for k in range(n):
            norm_sq = norm_sq + (v[k] * v[k])
        # sqrt ball
        if norm_sq.lo() < 0:
            # inflate to keep nonnegative
            norm_sq = Ball(norm_sq.mid, abs(norm_sq.mid) + norm_sq.rad)
        rjj_mid = mp.sqrt(abs(norm_sq.mid))
        # crude radius for sqrt
        rjj_rad = norm_sq.rad / (2 * max(rjj_mid, mp.mpf("1e-30")))
        rjj = Ball(rjj_mid, rjj_rad)
        R[j][j] = rjj
        if rjj.contains_zero():
            # column collapse — mark unit vector fallback with large radius
            q = [Ball.exact(1 if k == j else 0) for k in range(n)]
            for k in range(n):
                q[k] = Ball(q[k].mid, mp.mpf("1e-3"))
        else:
            q = [vk / rjj for vk in v]
        Qcols.append(q)

    Q = BallMatrix([[Qcols[j][i] for j in range(n)] for i in range(n)])
    Rmat = BallMatrix(R)
    return Q, Rmat


def log_abs_diag(R: BallMatrix) -> List[Ball]:
    """log|R_ii| as balls."""
    out = []
    for i in range(R.n):
        d = R.rows[i][i]
        ab = Ball(abs(d.mid), d.rad)
        if ab.lo() <= 0:
            # failed enclosure
            out.append(Ball(mp.log(max(abs(d.mid), mp.mpf("1e-300"))), mp.mpf(10)))
            continue
        # log(m ± r) ⊂ log(m) ± r/lo
        mid = mp.log(ab.mid)
        rad = ab.rad / ab.lo()
        out.append(Ball(mid, rad))
    return out
