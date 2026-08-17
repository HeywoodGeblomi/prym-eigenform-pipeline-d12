# Individual exponents λ₂, λ₃ — technical attack

**Status:** Priority 2 open (user green light 2026-08-17).  
**Goal:** Rigorous enclosures for the individual non-tautological exponents on the D=12 prototype / Diagram B dual paths.  
**Known:** λ₂ + λ₃ = 3/5 (Chen–Möller + EKZ). λ₁ = 1 tautological.  
**Not the goal:** float means, packaging, or “solved” claims before interval control is real.

## Milestone A — Error model & interval infrastructure

### Existing assets
| Module | Role | Limitation |
|--------|------|------------|
| `code/ball_matrix.py` | Ball + BallMatrix + modified Gram–Schmidt | sqrt / QR radii crude |
| `code/zorich_kz_ball.py` | Ball dual + Teichmüller time `-log(1-Lℓ/Lw)` | Slow; bounce optional |
| `certified/path_local_monodromy_sum.json` | Path-local sum ∋ 8/5 | Individuals not certified |

### A1. Pure paths only (for certificates)
No artificial length resampling. Reject ambiguous branches under length balls.

### A2. Error budget
Dual exact integers; ball mul/add; modified GS QR inflation; Teichmüller time `-log(1-Lℓ/Lw)`; length normalization.

### A3. QR upgrade
Tighten pure-Python GS; optional Arb later.

## Engineering readout (2026-08-17)

### Finding 1 — Pure Dirichlet starts trap
Random Dirichlet + pure Rauzy (no bounce), even at 2·10⁴ steps: T ≲ 15, spectrum collapses (λ₂ ≈ λ₃ ≈ 0). Path sits near a cusp.

### Finding 2 — Bounce restores exploration (not pure)
Resample when max length > 0.998: T grows, mids appear, high seed variance. **Not certifiable.**

### Finding 3 — Reference path
Seed-728 path-local (~10⁵ moves, T≈312): normalized mids [1.0, 0.4817, 0.1238, 0, −1.6055]. Sum interval ∋ 8/5 certified under QR model; individuals not.

### Next (Milestone A continued)
1. **Zorich acceleration** on pure paths (consecutive same-direction Rauzy) to escape cusps without bounce.
2. **Typical initial lengths** (Hilbert / approximate Masur–Veech) instead of raw Dirichlet.
3. Tighten QR only after pure paths produce stable mids.

## Milestone B/C
Ensemble of pure validated paths; first honest statement λ₂ ∈ [a,b], λ₃ ∈ [c,d] even if wide.

## Non-goals
D=14 narrative; bounce in certificates; claiming individuals solved early.

## Artifacts
- `data/lambda23_float_ensemble.json` — pure (collapsed)
- `data/lambda23_exploratory_bounce.json` — bounce exploratory
- `scripts/lambda23_float_ensemble.py`
