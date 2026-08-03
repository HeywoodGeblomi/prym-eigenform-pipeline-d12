# prym-eigenform-pipeline-d12

**Research blueprint** for the real-multiplication and Rauzy structure of a linear model of the discriminant-12 S-shaped Prym eigenform prototype.

This repository does **not** contain certified Lyapunov spectra, the exhaustive zippered-rectangle Rauzy class of the published S-shaped surface, or any new theorem. All numerical exponents produced by the current integrator are provisional and must not be cited as Lyapunov exponents of a genuine Prym eigenform.

## Verified algebraic claims

The code and tests establish the following, and only the following:

1. The endomorphism  
   \(T=\begin{pmatrix}2&0&2&0\\0&2&0&2\\1&0&0&0\\0&1&0&0\end{pmatrix}\)  
   satisfies \(T^2-2T-2I=0\) with residual 0 (double and 50-digit precision).
2. The projector \(P_\lambda=(T-\bar\lambda I)/(\lambda-\bar\lambda)\) (\(\lambda=1+\sqrt{3}\)) is idempotent of rank 2.
3. The prototype period vector \((\lambda,0,1,0)\) is an exact eigenvector of \(T\) with eigenvalue \(\lambda\).
4. The integrator keeps every iterate on the real-multiplication eigenplane (residual at machine / high precision).
5. Provisional spectra extracted by QR are symmetric about zero.

Literature prototype parameters (Lanneau–Nguyen): \((w,h,t,e)=(1,1,0,\pm2)\). The signed matrix with \(e=-2\) is equivalent under orientation/basis change; both satisfy the minimal polynomial with residual 0.

## Layout

```
  README.md
  LICENSE
  requirements.txt
  code/
    __init__.py
    rm_projector.py          # exact T, P_λ (double)
    rm_projector_hp.py       # high-precision (mpmath, dps=50)
    rauzy.py                 # Prym-compatible generators (linear model)
    integrator.py            # constrained KZ iteration
    enumerate_rauzy_graph.py
    verify.py                # algebraic predicates (plane, Prym, unimodular)
    avila_viana_checks.py    # pinching / twisting numerical diagnostics
  data/
    prototype_d12.json
    rauzy_graph_d12.json     # 64 vertices, 120 edges (linear model)
    arithmetic_d12.json
    ekz_sum_check.json
    ekz_numerical_eval.json
    provisional_long_run.json
    avila_viana_diagnostics.json
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
# regression tests (must pass)
python3 tests/test_regression.py

# algebraic verification harness (existing generators fail plane, as expected)
python3 -c "from code.verify import full_check; from code.rauzy import A_top, S; print(full_check(A_top, S))"

# high-precision residual check
python3 code/rm_projector_hp.py

# Avila–Viana pinching / twisting diagnostics
python3 -c "
from code.avila_viana_checks import monoid_pinching_score
from code.rauzy import A_top, A_bot, A_top_sym, A_bot_sym
print(monoid_pinching_score([A_top, A_bot, A_top_sym, A_bot_sym]))
"

# regenerate the Rauzy graph (linear model)
cd code && python3 enumerate_rauzy_graph.py && cd ..

# short / long provisional run
python3 -c "
from code.integrator import run
snaps = run(n_steps=20000, reorth_every=1000)
print(snaps[-1])
"
```

## Stage-4 status (2026-08-03)

The Stage-4 checklist remains **open**. The single blocking item is:

> 1. Replace the present generators by the complete Rauzy-class permutation representation of the S-shaped three-torus / zippered-rectangle prototype.

**What is known from the literature**

- Geometric model: \(S(w=1,e=\pm2)\), \(\lambda\times\lambda\) square attached to two \(w\times1\) rectangles.
- Lanneau–Nguyen prototype \((w,h,t,e)=(1,1,0,\pm2)\).
- \(\Omega E_{12}(4)\) (and the corresponding component in the odd \((2,2)\) stratum) is a single connected Teichmüller curve with exactly two cusps.
- Three-cylinder decompositions only.

**What is not available in published machine-readable form**

- The exhaustive set of Rauzy permutations / transition matrices on the 4-dimensional anti-invariant homology that stay inside the Prym involution and the \(\mathcal{O}_{12}\)-eigenplane without forced re-projection.

**Preparatory work completed**

- `code/verify.py` — plane / Prym / unimodular predicates.
- `code/rm_projector_hp.py` — mpmath residual-0 projector.
- `code/avila_viana_checks.py` — numerical pinching (singular-value gaps) and twisting probes inspired by the Avila–Viana simplicity criterion; ready for a genuine monoid.
- Longer provisional trajectory and partial EKZ evaluation recorded in `data/`.

**Next research step required**

Reconstruct the polygonal model → choose a horizontal transversal → extract the initial generalized permutation and suspension data → perform Rauzy induction while enforcing anti-invariant homology and the real-multiplication eigenplane → feed the resulting matrices through `verify.py` and the Avila–Viana diagnostics. Only after a verified generating set exists does the pipeline move to interval arithmetic and certified long runs.

## Limitations (read carefully)

- The Rauzy graph is a **linear model**, not the exhaustive zippered-rectangle Rauzy class.
- Numerical exponents are spectra of this reduced model only.
- No interval arithmetic, no long certified runs, and no Eskin–Kontsevich–Zorich sum check on a genuine spectrum have been performed.

## How to cite / not cite

- **You may cite** the exact algebraic claims that are verified with residual 0 (the endomorphism \(T\), the projector \(P_\lambda\), the prototype eigenvector, and the idempotence of the projector). When doing so, reference this repository and the residual-0 tests.
- **Do not cite** any numerical Lyapunov exponents, provisional spectra, long-run estimates, or similar claims produced by the current integrator. Those numbers belong exclusively to the reduced linear model and are not Lyapunov exponents of a genuine Prym eigenform on \(\Omega E_{12}\).
- The Stage-4 checklist remains open. Until the combinatorial Rauzy class is in place and the algebraic verification, interval-arithmetic, and EKZ checks have been completed, no spectrum from this repository should be treated as rigorous.

Suggested citation form for the algebraic scaffold:

> Exact real-multiplication projector and Prym-symmetric linear-model Rauzy scaffold for the discriminant-12 S-shaped prototype (residual 0), together with Avila–Viana-style pinching/twisting diagnostics. Available at https://github.com/HeywoodGeblomi/prym-eigenform-pipeline-d12.

## Mathematical context

Prym eigenform loci are the only known infinite families of primitive rank-one affine invariant submanifolds in fixed genus 2–5. The open question that motivates this pipeline is whether the individual non-trivial Lyapunov exponents are independent of the discriminant on the two-dimensional components. This repository supplies the exact real-multiplication projector, a concrete Prym-symmetric combinatorial scaffold, algebraic verification tools, and Avila–Viana-style diagnostics for the first discriminant; it does not answer the question.

## License

MIT License. See the file `LICENSE`. Research code provided without warranty; use at your own risk.
