# Individual exponents λ₂, λ₃ — technical attack

**Status:** Priority 2 open.  
**Known:** λ₂+λ₃=3/5 (Chen–Möller+EKZ). Individuals open.

## Engineering readout

### Pure Zorich acceleration (failed to mix)
On Diagram B and on the geometric 4-interval permutation, Zorich stacking from balanced / geometric / Dirichlet inits gives **dir_changes = 0**. Spectrum collapses (λ₂≈λ₃≈0). Acceleration alone does not escape the one-sided Rauzy chamber under projective length updates.

### Path-class ensemble (bounce, exploratory — not pure)
Bounce when max length > 0.998 (same style as sum-certificate paths):

| quantity | value |
|--|--|
| λ₂ mean (15 seeds × 8·10⁴ steps) | ≈ 0.40 (std ≈ 0.25) |
| λ₃ mean | ≈ 0.03 (std ≈ 0.09) |
| sum23 mean | ≈ 0.45 (target 0.6) |
| seed 728 this run | λ₂≈0.68, λ₃≈0.16 |
| seed 728 certificate ref | λ₂≈0.48, λ₃≈0.12 |

QR-model radii ~1e-7; **seed-to-seed mid variance dominates**. Not certified.

### Blocker for pure individual certificates
Need one of:
1. Suspension / zippered-rectangle Teichmüller flow (continuous heights+lengths).
2. Path-local individuals only on explicit recorded paths (same scope as sum cert).
3. A combinatorially mixing Rauzy component.

Bounce stays experimental only. `promote_ready: false`.

## Artifacts
- `data/lambda23_zorich_inits.json`
- `data/lambda23_path_class_ensemble.json`
- `data/lambda23_exploratory_bounce.json`
- `scripts/lambda23_zorich_pure.py`
