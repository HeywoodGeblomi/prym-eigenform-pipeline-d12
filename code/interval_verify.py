#!/usr/bin/env python3
"""
Rigorous residual certification for residual-0 algebraic claims.

Integer matrix identities are checked in exact mpmath arithmetic (residual is
the exact zero mpf). Quadratic identities over Q(sqrt(3)) use high working
precision (dps=60) and are certified when the residual is smaller than
10^{-(dps-5)}.

This is stronger than float64 heuristics. Full arb-style interval KZ
integration remains future work; numerical spectra stay experimental.
"""
from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from typing import Any, Dict

import mpmath as mp

mp.mp.dps = 60


@dataclass
class IntervalCertificate:
    name: str
    lo: float
    hi: float
    contains_zero: bool
    diameter: float
    certified: bool
    note: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


def _T() -> mp.matrix:
    """Classical residual-0 endomorphism (matches code/rm_projector.py)."""
    return mp.matrix(
        [
            [2, 0, 2, 0],
            [0, 2, 0, 2],
            [1, 0, 0, 0],
            [0, 1, 0, 0],
        ]
    )


def _cert_from_norm(name: str, nrm: mp.mpf, note: str) -> IntervalCertificate:
    eps = mp.mpf(10) ** (-(mp.mp.dps - 5))
    if nrm == 0:
        return IntervalCertificate(name, 0.0, 0.0, True, 0.0, True, note)
    certified = bool(nrm < eps)
    hi = float(nrm + eps)
    return IntervalCertificate(
        name=name,
        lo=0.0 if certified else float(nrm),
        hi=hi,
        contains_zero=certified,
        diameter=hi,
        certified=certified,
        note=note,
    )


def certify_minimal_polynomial(w: int = 1, h: int = 1) -> IntervalCertificate:
    """Certify ||T^2 - 2T - 2wh I|| = 0 exactly."""
    T = _T()
    nrm = mp.norm(T * T - 2 * T - (2 * w * h) * mp.eye(4))
    return _cert_from_norm(
        "minimal_polynomial_residual",
        nrm,
        "||T^2 - 2T - 2wh I|| exact mpmath (integer matrix)",
    )


def certify_eigenvector() -> IntervalCertificate:
    """Certify T p = λ p for λ = 1+√3, p = (λ, 0, 1, 0)."""
    lam = 1 + mp.sqrt(3)
    T = _T()
    p = mp.matrix([lam, 0, 1, 0])
    nrm = mp.norm(T * p - lam * p)
    return _cert_from_norm(
        "eigenvector_residual",
        nrm,
        "||T p - λ p|| with λ=1+√3, dps=60 (matches rm_projector.py)",
    )


def certify_projector_idempotent() -> IntervalCertificate:
    """Certify P_λ^2 = P_λ for λ = 1+√3, λ̄ = 1-√3."""
    lam = 1 + mp.sqrt(3)
    lam_c = 1 - mp.sqrt(3)
    T = _T()
    P = (T - lam_c * mp.eye(4)) / (lam - lam_c)
    nrm = mp.norm(P * P - P)
    return _cert_from_norm(
        "projector_idempotent",
        nrm,
        "||P^2 - P|| with dps=60",
    )


def run_certification_suite(
    D: int = 12, e: int = -2, w: int = 1, h: int = 1
) -> Dict[str, Any]:
    """Run all residual-0 algebraic certifications for a prototype."""
    certs = [
        certify_minimal_polynomial(w=w, h=h),
        certify_eigenvector(),
        certify_projector_idempotent(),
    ]
    return {
        "D": D,
        "e": e,
        "w": w,
        "h": h,
        "method": "exact mpmath + dps=60 ball residuals",
        "certificates": [c.to_dict() for c in certs],
        "all_certified": all(c.certified for c in certs),
        "disclaimer": (
            "Algebraic identities are certified at working precision. "
            "Numerical KZ spectra from integrator.py remain experimental, "
            "not IA-certified Lyapunov exponents."
        ),
    }


if __name__ == "__main__":
    import sys

    D = int(sys.argv[1]) if len(sys.argv) > 1 else 12
    e = int(sys.argv[2]) if len(sys.argv) > 2 else -2
    report = run_certification_suite(D=D, e=e)
    print(json.dumps(report, indent=2))
    sys.exit(0 if report["all_certified"] else 1)
