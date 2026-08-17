# prym-eigenform-pipeline-d12

**Computational scaffold** for the discriminant-12 McMullen S-shaped Prym eigenform prototype.

This repository provides an exact residual-0 real-multiplication projector, plane-preserving Rauzy generators, an independent geometric construction of $S(1,-2)$, a constrained KZ integrator, and dual Rauzy evaluation code. Regression tests lock the algebraic claims.

The sum of positive Lyapunov exponents on $H(4)^{\\mathrm{odd}}$ (and on $\\Omega E_{12}(4)$) is $8/5$ by Chen–Möller. This work records computational consistency with that known value on explicit paths; it does not prove the theorem. Individual non-tautological exponents remain experimental.

See [RELEASE_NOTES.md](RELEASE_NOTES.md), [certified/CERTIFICATE.md](certified/CERTIFICATE.md), and the draft note [paper/computational_note_d12.tex](paper/computational_note_d12.tex).

## Verified algebraic claims

The code and tests establish the following, and only the following:

1. The endomorphism  
   $T=\\begin{pmatrix}2&0&2&0\\\\0&2&0&2\\\\1&0&0&0\\\\0&1&0&0\\end{pmatrix}$  
   satisfies $T^2-2T-2I=0$ with residual 0 (double and 50-digit precision).
2. The projector $P_\\lambda=(T-\\bar\\lambda I)/(\\lambda-\\bar\\lambda)$ ($\\lambda=1+\\sqrt{3}$) is idempotent of rank 2.
3. The prototype period vector $(\\lambda,0,1,0)$ is an exact eigenvector of $T$ with eigenvalue $\\lambda$.
4. **Corrected generators** `A_top_corr`, `A_bot_corr`, `S_corr` strictly preserve the eigenplane (residual $\\sim10^{-16}$).
5. The constrained integrator (raw unimodular generators + continuous eigenplane re-projection) produces provisional QR spectra symmetric about zero.

Literature prototype parameters (Lanneau–Nguyen): $(w,h,t,e)=(1,1,0,\\pm2)$.

## Layout

```
  README.md
  RELEASE_NOTES.md
  benchmarks.md
  LICENSE
  requirements.txt
  code/
    rm_projector.py, rm_projector_hp.py
    rauzy.py, integrator.py
    enumerate_rauzy_graph.py, verify.py
    avila_viana_checks.py
  data/
    prototype and candidate combinatorial artefacts
  geometric/
    S(1,-2) construction and Gate 1 extraction
  certified/
    narrow documented computational claims (see CERTIFICATE.md)
  paper/
    computational_note_d12.tex (draft arXiv note)
  tests/
    test_regression.py
```

## Requirements

- Python 3.10+
- NumPy
- mpmath (high-precision projector and diagnostics)

```bash
pip install -r requirements.txt
```

## How to run

```bash
python3 -m pytest tests/test_regression.py -v
python3 code/rm_projector_hp.py
```

## Limitations

- The linear-model Rauzy graph is not the exhaustive zippered-rectangle Rauzy class.
- Numerical individual exponents are experimental.
- Path-local dual Rauzy evaluation and Hilbert uniqueness data under `certified/` are scoped; see CERTIFICATE.md.
- This repository does not prove the sum $8/5$ on the locus; that is Chen–Möller.

## How to cite / not cite

**You may cite** residual-0 algebraic claims, the geometric construction of $S(1,-2)$, and the dual Rauzy evaluation tools under the scopes documented in `certified/`.

**Do not cite** float ensemble means as rigorous bounds on individual Lyapunov exponents, or this repository as the source of the sum $8/5$.

## License

MIT License. See LICENSE.
