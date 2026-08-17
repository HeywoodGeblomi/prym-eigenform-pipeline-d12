# Individual exponents λ₂, λ₃ — technical attack

**Status:** Priority 2 open. Known: λ₂+λ₃=3/5. Individuals open.

## Option 1 — Suspension / zippered-rectangle (scaffold live)

Module: `code/suspension_flow.py`

- State: lengths λ, heights h, area λ·h = 1, Gate-1 Rauzy vertex
- Return time: `-log(1 - λ_ℓ/λ_w)`
- Height + KZ cocycle: dual `(M^{-1})^T`

### Finding
On the current Gate-1 4-interval class, dynamics fall into **one-sided cycles** (e.g. bot 0→1→3→0). Dual monodromy has eigenvalues on the **unit circle** → Lyapunov spectrum ≈ 0. Suspension bookkeeping is correct; **combinatorial mixing is missing**.

### Implication
Architecture is ready. Physical λ₂, λ₃ need the **true geometric monodromy** of S(1,-2) (complete mixing Rauzy class or homology from cylinder/origami presentation).

## Prior findings
- Pure discrete Rauzy / Zorich: dir_changes=0, spectrum collapsed
- Bounce path-class: exploratory mids, high variance, not pure
- Seed-728 path-local sum cert: still best sum signal; individuals not certified

`promote_ready: false`
