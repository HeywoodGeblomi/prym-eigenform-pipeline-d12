# Benchmarks — prym-eigenform-pipeline-d12

All numbers below are reproducible from the code in this repository.
They document **algebraic and combinatorial status**, not certified
Lyapunov exponents of a geometric Prym eigenform.

## Residual-0 algebra

| Quantity | Value |
|----------|-------|
| `residual_minimal_polynomial(T)` | **0** (exact in double; confirmed at 50-digit precision) |
| Rank of \(P_\lambda\) | **2** |
| \(\|P_\lambda^2 - P_\lambda\|\) | \(< 10^{-15}\) |
| Eigenvector residual \(\|T v - \lambda v\|\) for \(v=(\lambda,0,1,0)\) | \(< 10^{-15}\) |

## Plane-preserving corrected generators

Obtained by the simultaneous projection
\(M_{\mathrm{corr}} = P_\lambda M P_\lambda + (I-P_\lambda) M (I-P_\lambda)\).

| Generator | `preserves_eigenplane` residual | \(\det\) |
|-----------|----------------------------------|----------|
| `A_top_corr` | \(\sim 1.2 \times 10^{-16}\) | \(0.9167\) |
| `A_bot_corr` | \(\sim 1.2 \times 10^{-16}\) | \(0.9167\) |
| `S_corr` | \(\sim 1.0 \times 10^{-16}\) | \(-0.3333\) |

Products of corrected generators remain on the eigenplane
(residual \(\sim 10^{-16}\)).

## Raw (unimodular) generators

Used by the constrained integrator (eigenplane enforced by continuous
re-projection, not by the generators themselves).

| Generator | Unimodular | `preserves_eigenplane` residual |
|-----------|------------|----------------------------------|
| `A_top` | yes (\(\det=1\)) | \(\sim 0.128\) |
| `A_bot` | yes (\(\det=1\)) | \(\sim 0.128\) |
| `S` | yes (\(\det=-1\)) | \(\sim 0.699\) |

## Candidate combinatorial Rauzy class

Derived from the geometrically reconstructed candidate permutation
compatible with the three-cylinder + Prym structure
(see `data/candidate_rauzy_class_d12.json`).

| Quantity | Value |
|----------|-------|
| Starting reduced permutation | \((0\,1\,2\,/\,2\,1\,0)\) |
| Combinatorial permutations | **3** |
| Combinatorial edges | **6** |
| Filtered 4-D monoid size (preserves eigenplane) | **65** |

**Honesty note.** This is the Rauzy class of a *candidate* combinatorial
type, not a certified extraction from the geometric S-shaped surface.

## Provisional integrator (short run)

`run(n_steps=5000, reorth_every=500)` with raw unimodular generators
+ continuous eigenplane re-projection:

| Check | Result |
|-------|--------|
| Spectrum symmetric about zero (\(\lvert\lambda_0+\lambda_3\rvert\)) | \(< 10^{-6}\) (regression-tested) |
| Lengths re-projected onto eigenplane every step | yes |

Longer provisional runs and QR spectra are recorded in
`data/provisional_long_run.json` and must **not** be cited as Lyapunov
exponents of a genuine Prym eigenform.

## Regression suite

```
pytest tests/test_regression.py -v
```

All five tests must pass before any public release:

1. `test_minimal_polynomial`
2. `test_eigenvector`
3. `test_projector`
4. `test_corrected_generators_preserve_eigenplane`
5. `test_short_run_symmetric_spectrum`
