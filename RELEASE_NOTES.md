# Release Notes — prym-eigenform-pipeline-d12

## v0.1.0 — Research Blueprint (2026-08-03)

Initial public release of a research pipeline for the real-multiplication structure of the discriminant-12 S-shaped Prym eigenform prototype.

### What this release provides

- Exact real-multiplication endomorphism \(T\) satisfying \(T^2 - 2T - 2I = 0\) (residual 0 in double and 50-digit precision).
- Rank-2 projector \(P_\lambda\) onto the \(\lambda = 1+\sqrt{3}\) eigenplane (idempotent, residual 0).
- Prototype period vector verified as an exact eigenvector.
- Prym-compatible linear-model Rauzy generators and a 64-vertex / 120-edge graph.
- Constrained Kontsevich–Zorich integrator that stays on the eigenplane.
- Algebraic verification predicates (`preserves_eigenplane`, `prym_compatible`, `is_unimodular`).
- Avila–Viana-style numerical pinching and twisting diagnostics ready for any future plane-preserving monoid.
- High-precision (mpmath) projector and regression tests that pass.
- Explicit documentation of the open Stage-4 combinatorial gate.

### What this release does **not** provide

- Certified Lyapunov spectra of any genuine Prym eigenform.
- The exhaustive zippered-rectangle Rauzy class of the published S-shaped surface.
- Interval-arithmetic long runs or a completed Eskin–Kontsevich–Zorich sum check on a genuine spectrum.
- Any new theorem.

### Citation policy

- You **may** cite the residual-0 algebraic claims (the matrix \(T\), the projector \(P_\lambda\), the eigenvector property) and the combinatorial description of the linear-model scaffold.
- You **must not** cite any numerical Lyapunov exponents, provisional spectra, or pinching scores as results about genuine Prym eigenforms or the locus \(\Omega E_{12}\).

### Next research step

Replace the linear-model generators by the complete Rauzy-class permutation representation of the S-shaped three-torus / zippered-rectangle prototype, then feed the resulting matrices through the existing verification and diagnostic harnesses.

### License

MIT License — see `LICENSE`.

### Files of interest

| Path | Purpose |
|------|---------|
| `code/rm_projector.py` / `rm_projector_hp.py` | Exact and high-precision real-multiplication projector |
| `code/verify.py` | Algebraic predicates for candidate transition matrices |
| `code/avila_viana_checks.py` | Pinching / twisting numerical diagnostics |
| `code/integrator.py` | Constrained KZ iteration |
| `data/rauzy_graph_d12.json` | Linear-model Rauzy graph (64 verts, 120 edges) |
| `tests/test_regression.py` | Regression suite (must pass) |

Thank you for reading the limitations carefully.
