# prym-eigenform-pipeline-d12

**Computational scaffold** for the discriminant-12 McMullen S-shaped Prym eigenform prototype.

This repository provides an exact residual-0 real-multiplication projector, plane-preserving Rauzy generators, an independent geometric construction of $S(1,-2)$, a constrained KZ integrator, and dual Rauzy evaluation code. Regression tests lock the algebraic claims.

The sum of positive Lyapunov exponents on $H(4)^{\mathrm{odd}}$ (and on $\Omega E_{12}(4)$) is $8/5$ by Chen–Möller. The individual non-tautological exponents on the Weierstrass Prym loci $\Omega E_D(4)$ (including $D=12$) are $\lambda_2=2/5$ and $\lambda_3=1/5$, due to Möller and to Eskin–Kontsevich–Zorich (Eskin–Matheus arXiv:1210.2157 §3.2). This repository does **not** claim those theorems. Path-local dual Rauzy evaluation on an explicit Diagram B path produces a positive-sum interval containing $8/5$ under a controlled QR error model (path-local consistency only).

See [docs/SPECTRUM_ATTRIBUTION.md](docs/SPECTRUM_ATTRIBUTION.md), [docs/PATH_LOCAL_CERTIFICATE.md](docs/PATH_LOCAL_CERTIFICATE.md), and the draft note [paper/computational_note_d12.tex](paper/computational_note_d12.tex).

## Verified algebraic claims

1. Residual-0 real-multiplication endomorphism $T$ and projector $P_\lambda$.
2. Plane-preserving corrected Rauzy generators.
3. Pure-Python geometric construction of $S(1,-2)$ with residual-0 period vector.
4. Path-local dual Rauzy certificate (seed 728) whose pos-sum interval contains $8/5$ under a controlled QR model — **path-local only**.

## How to cite / not cite

**You may cite** residual-0 algebra, geometric construction of $S(1,-2)$, and the path-local sum enclosure as path-local.

**Do not cite** this repo as the source of $\lambda_2=2/5$ or $\lambda_3=1/5$ (those are Möller / EKZ / Eskin–Matheus), nor path-local mids as global individual exponents, nor this repo as the source of the sum $8/5$ (Chen–Möller).

## Status

`promote_ready` remains false for any global *computational* claim of the individuals. No further engineering cycles on recovering global $\lambda_2,\lambda_3$ computationally — that gate is closed by the literature.

## License

MIT License. See LICENSE.
