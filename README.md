# prym-eigenform-pipeline-d12

**Research blueprint** (v0.2.0-candidate) for the real-multiplication and Rauzy structure of a linear model of the discriminant-12 S-shaped Prym eigenform prototype, plus geometrically derived **candidate** combinatorial data.

This repository does **not** contain certified Lyapunov spectra, the exhaustive zippered-rectangle Rauzy class of the published S-shaped surface, or any new theorem. All numerical exponents produced by the current integrator are provisional and must not be cited as Lyapunov exponents of a genuine Prym eigenform.

See [RELEASE_NOTES.md](RELEASE_NOTES.md) and [benchmarks.md](benchmarks.md).

## Verified algebraic claims

The code and tests establish the following, and only the following:

1. The endomorphism  
   \(T=\begin{pmatrix}2&0&2&0\\0&2&0&2\\1&0&0&0\\0&1&0&0\end{pmatrix}\)  
   satisfies \(T^2-2T-2I=0\) with residual 0 (double and 50-digit precision).
2. The projector \(P_\lambda=(T-\bar\lambda I)/(\lambda-\bar\lambda)\) (\(\lambda=1+\sqrt{3}\)) is idempotent of rank 2.
3. The prototype period vector \((\lambda,0,1,0)\) is an exact eigenvector of \(T\) with eigenvalue \(\lambda\).
4. **Corrected generators** `A_top_corr`, `A_bot_corr`, `S_corr` strictly preserve the eigenplane (residual \(\sim10^{-16}\)).
5. The constrained integrator (raw unimodular generators + continuous eigenplane re-projection) produces provisional QR spectra symmetric about zero.

Literature prototype parameters (Lanneau–Nguyen): \((w,h,t,e)=(1,1,0,\pm2)\).

## Layout

```
  README.md
  RELEASE_NOTES.md           # v0.2.0-candidate summary
  benchmarks.md              # residual-0 and class-size numbers
  LICENSE
  requirements.txt
  code/
    __init__.py
    rm_projector.py          # exact T, P_λ (double)
    rm_projector_hp.py       # high-precision (mpmath, dps=50)
    rauzy.py                 # raw + corrected (plane-preserving) generators
    integrator.py            # constrained KZ iteration
    enumerate_rauzy_graph.py
    verify.py                # algebraic predicates (plane, Prym, unimodular)
    avila_viana_checks.py    # pinching / twisting numerical diagnostics
  data/
    prototype_d12.json
    candidate_rauzy_class_d12.json   # candidate combinatorial class (3 perms, 6 edges)
    rauzy_graph_d12.json     # linear-model graph (64 verts, 120 edges)
    arithmetic_d12.json
    ekz_sum_check.json
    ekz_numerical_eval.json
    provisional_long_run.json
    avila_viana_diagnostics.json
  tests/
    test_regression.py       # 5 tests; must all pass
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
# regression tests (must be 5 passed)
python3 -m pytest tests/test_regression.py -v

# high-precision residual check
python3 code/rm_projector_hp.py

# corrected generators: eigenplane residual ~1e-16
python3 -c "
from code.verify import preserves_eigenplane
from code.rauzy import A_top_corr, A_bot_corr, S_corr
for n,M in [('A_top_corr',A_top_corr),('A_bot_corr',A_bot_corr),('S_corr',S_corr)]:
    print(n, preserves_eigenplane(M))
"

# short provisional run
python3 -c "
from code.integrator import run
snaps = run(n_steps=5000, reorth_every=500)
print(snaps[-1])
"
```

See `benchmarks.md` for residual and class-size numbers.

## Stage-4 status (2026-08-04)

| Step | Status |
|------|--------|
| 1. Polygonal model + side identifications + \(\rho\) | Advanced (geometric derivation) |
| 2. Horizontal transversal | Done |
| 3. Initial generalized permutation + lengths | **Candidate** written down |
| 4. Rauzy induction under residual-0 filter | Executed on the **candidate** |
| 5. Enumerate + algebraic filter | Candidate: 3 perms / 6 edges; 4-D monoid size 65 |
| 6. Publish permutations + matrices | `data/candidate_rauzy_class_d12.json` |

The combinatorial data above is a **geometrically derived candidate**, not a certified extraction from the published S-shaped surface. The geometric Rauzy class remains uncertified until confirmed by an independent polygonal construction or labelled-figure transcription.

**What is known from the literature**

- Geometric model: \(S(w=1,e=\pm2)\), \(\lambda\times\lambda\) square attached to two \(w\times1\) rectangles.
- Lanneau–Nguyen prototype \((w,h,t,e)=(1,1,0,\pm2)\).
- \(\Omega E_{12}(4)\) is a single connected Teichmüller curve with exactly two cusps.
- Three-cylinder decompositions only.

**What is not available in published machine-readable form**

- The exhaustive set of Rauzy permutations / transition matrices of the geometric surface that stay inside the Prym involution and the \(\mathcal{O}_{12}\)-eigenplane without forced re-projection.

## Limitations (read carefully)

- The linear-model Rauzy graph (64/120) is **not** the exhaustive zippered-rectangle Rauzy class.
- The candidate class in `data/candidate_rauzy_class_d12.json` is **not** claimed to be the geometric class.
- Numerical exponents are spectra of the reduced model only.
- No interval arithmetic, no long certified runs, and no Eskin–Kontsevich–Zorich sum check on a genuine spectrum have been performed.

## How to cite / not cite

- **You may cite** the residual-0 algebraic claims (endomorphism \(T\), projector \(P_\lambda\), eigenvector, idempotence, corrected-generator residuals).
- **Do not cite** any numerical Lyapunov exponents, provisional spectra, or the candidate Rauzy class as certified results about a genuine Prym eigenform on \(\Omega E_{12}\).

Suggested citation form:

> Exact real-multiplication projector, plane-preserving generator corrections, and geometrically derived candidate Rauzy data for the discriminant-12 S-shaped prototype (residual 0). Available at https://github.com/HeywoodGeblomi/prym-eigenform-pipeline-d12.

## Mathematical context

Prym eigenform loci are the only known infinite families of primitive rank-one affine invariant submanifolds in fixed genus 2–5. The open question that motivates this pipeline is whether the individual non-trivial Lyapunov exponents are independent of the discriminant on the two-dimensional components. This repository supplies the exact real-multiplication projector, plane-preserving generator corrections, a candidate combinatorial scaffold, algebraic verification tools, and Avila–Viana-style diagnostics for the first discriminant; it does not answer the question.

## License

MIT License. See the file `LICENSE`. Research code provided without warranty; use at your own risk.
