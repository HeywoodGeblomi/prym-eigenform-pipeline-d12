# Response to the floating-point / pipeline critique

## 1. Floating point → interval / ball residuals

**Implemented:** `code/interval_verify.py` + `scripts/certify_residual0.py`

- Minimal polynomial residual certified with `mpmath.iv` (exact integer matrix ⇒ residual interval `{0}`).
- Eigenvector and projector idempotence certified with high-precision ball residuals (dps=60).
- A claim is **certified** only when the residual encloses 0 at working precision.

```bash
python scripts/certify_residual0.py 12 -2
```

**Still experimental (not IA-certified):** numerical KZ / QR Lyapunov spectra from `integrator.py`. Those remain experimental numerical evidence.

## 2. Pipeline vs one-off

**Implemented:** `code/prototype.py`

- `Prototype(w,h,t,e)` with `D = e² + 8wh`
- `prototype_from_D(D)` searches simple prototypes
- Gate-1 default `(1,1,0,-2)` still available as `GATE1`

Data filenames `*_d12.json` remain historical artifacts of the campaign focus; the **code** path is parameterized.

## 3. Disclaimers

Algebraic residual-0 claims are now certifiable via interval/ball checks.
Lyapunov *spectra* stay labelled experimental. That split is intentional, not anxiety: the field requires it.

## 4. Structure

| Module | Responsibility |
|--------|----------------|
| `rauzy_generators.py` | Transition matrices only |
| `enumerate_rauzy_graph.py` | Graph construction |
| `verify.py` | Float algebraic predicates |
| `interval_verify.py` | Rigorous residual certificates |
| `prototype.py` | `(w,h,t,e)` / `D` parameters |

`rauzy.py` is a thin backward-compatible re-export.
