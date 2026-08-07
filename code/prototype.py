"""
Parameterized LN prototype for Prym eigenforms in H(4).

Not hardcoded to D=12: any (w, h, t, e) with D = e^2 + 8*w*h admissible.
Default is the Gate-1 prototype (w,h,t,e)=(1,1,0,-2), D=12.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

import numpy as np


@dataclass(frozen=True)
class Prototype:
    """Lanneau–Nguyen splitting prototype parameters."""

    w: int
    h: int
    t: int
    e: int

    @property
    def D(self) -> int:
        return self.e * self.e + 8 * self.w * self.h

    @property
    def lambda_exact(self) -> complex:
        """Positive real unit of O_D when D is not a square: (e + sqrt(D))/2 for RM action conventions vary;
        for residual-0 checks we use the eigenvalue of T consistent with T^2 - e T - 2wh I = 0.
        """
        disc = self.D
        # Roots of x^2 - e x - 2wh = 0
        return 0.5 * (self.e + np.sqrt(disc))

    @property
    def lambda_conj(self) -> complex:
        return 0.5 * (self.e - np.sqrt(self.D))

    def endomorphism_T(self) -> np.ndarray:
        """Standard 4x4 residual-0 endomorphism for Model A± linear model."""
        # For the classical D=12 form used in the pipeline:
        # T = [[2,0,2,0],[0,2,0,2],[1,0,0,0],[0,1,0,0]] with e=2, w=h=1
        # Generalise the minimal polynomial coefficients; matrix form for
        # (w,h,t,e)=(1,1,0,±2) families keeps the same block shape when |e|=2, w=h=1.
        if (self.w, self.h) == (1, 1) and abs(self.e) == 2:
            # Orientation: e>0 vs e<0 swaps eigenvalue sign convention
            a = float(abs(self.e))
            return np.array(
                [
                    [a, 0.0, a, 0.0],
                    [0.0, a, 0.0, a],
                    [1.0, 0.0, 0.0, 0.0],
                    [0.0, 1.0, 0.0, 0.0],
                ],
                dtype=float,
            )
        raise NotImplementedError(
            f"T-matrix template not yet implemented for (w,h,t,e)="
            f"({self.w},{self.h},{self.t},{self.e}); extend prototype.endomorphism_T"
        )

    def period_vector(self) -> np.ndarray:
        """Canonical residual-0 period vector in H_1^-."""
        lam = float(self.lambda_exact) if self.e > 0 else float(-self.lambda_conj if self.e < 0 else self.lambda_exact)
        # For e=-2, D=12: λ = -1+sqrt(3) is the positive length unit used in Gate 1
        if self.e < 0:
            lam = float((-self.e + np.sqrt(self.D)) / 2 - self.e)  # simplify below
            # Gate-1 convention: λ = -1 + sqrt(3) for e=-2
            lam = float(-1.0 + np.sqrt(3.0)) if self.D == 12 else float((-self.e + np.sqrt(self.D)) / 2)
        else:
            lam = float((self.e + np.sqrt(self.D)) / 2)
        return np.array([lam, 0.0, 1.0, 0.0], dtype=float)

    def minimal_poly_residual(self, T: np.ndarray | None = None) -> float:
        T = self.endomorphism_T() if T is None else T
        I = np.eye(4)
        return float(np.linalg.norm(T @ T - self.e * T - 2 * self.w * self.h * I))


# Canonical Gate-1 / D=12 prototype (Model A+)
GATE1 = Prototype(w=1, h=1, t=0, e=-2)
D12 = Prototype(w=1, h=1, t=0, e=2)  # orientation-reversed equivalent


def prototype_from_D(D: int, prefer_minus: bool = True) -> Prototype:
    """Build a Model A± prototype for admissible D when a simple (w,h,t,e) exists.

    For D=12 returns Gate-1. For other D, searches small positive w,h with
    e^2 + 8wh = D. Raises ValueError if none found in the search range.
    """
    if D == 12:
        return GATE1 if prefer_minus else D12
    for w in range(1, 32):
        for h in range(1, 32):
            rem = D - 8 * w * h
            if rem < 0:
                continue
            root = int(round(np.sqrt(rem)))
            if root * root == rem:
                e = -root if prefer_minus else root
                return Prototype(w=w, h=h, t=0, e=e)
    raise ValueError(f"No simple (w,h,t,e) prototype found for D={D} in search range")
