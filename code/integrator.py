"""
Constrained Kontsevich–Zorich integrator for the D=12 Prym prototype.
Uses the exact RM projector and the minimal Prym-compatible Rauzy generators.

Provisional only — spectra of the reduced linear model, not certified
Lyapunov exponents of a genuine Prym eigenform.
"""
import numpy as np

from .rm_projector import project, T, lam
from .rauzy import choose_move, kz


def run(n_steps=100000, reorth_every=500, seed=0):
    """
    Run constrained KZ iteration.

    Returns a list of snapshots:
      {"step": int, "lyap": [..], "lengths": [..]}
    """
    v0 = np.array([lam, 0.0, 1.0, 0.0])
    assert np.linalg.norm(T @ v0 - lam * v0) < 1e-10

    lengths = np.abs(project(v0)) + 1e-15
    lengths /= lengths.sum()

    cocycle = np.eye(4)
    log_sing = np.zeros(4)
    snapshots = []

    for step in range(1, n_steps + 1):
        A = choose_move(lengths)
        lengths = np.abs(A @ lengths)
        lengths /= lengths.sum()

        shadow = project(lengths * np.array([lam, 1.0, 1.0, 1.0]))
        lengths = np.abs(shadow)
        lengths /= lengths.sum()

        cocycle = kz(A) @ cocycle

        if step % reorth_every == 0:
            q, r = np.linalg.qr(cocycle)
            diag = np.abs(np.diag(r))
            log_sing += np.log(np.maximum(diag, 1e-300))
            cocycle = q
            lyap = np.sort(log_sing / step)[::-1]
            snapshots.append(
                {
                    "step": step,
                    "lyap": lyap.tolist(),
                    "lengths": lengths.tolist(),
                }
            )

    return snapshots
