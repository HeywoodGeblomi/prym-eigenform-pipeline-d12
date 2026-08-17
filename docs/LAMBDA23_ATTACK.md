# Individual exponents λ₂, λ₃ — technical attack

**Status:** Priority 2 open (user green light 2026-08-17).  
**Goal:** Rigorous enclosures for the individual non-tautological exponents on the D=12 prototype / Diagram B dual paths.  
**Known:** λ₂ + λ₃ = 3/5 (Chen–Möller + EKZ). λ₁ = 1 tautological.  
**Not the goal:** float means, packaging, or “solved” claims before interval control is real.

## Milestone A — Error model & interval infrastructure

### Existing assets
| Module | Role | Limitation |
|--------|------|------------|
| `code/ball_matrix.py` | Ball + BallMatrix + modified Gram–Schmidt | sqrt / QR radii crude; not tight interval QR |
| `code/validated_path_ia.py` | Record float path → replay with length balls | Default `bounce_eps` breaks pure Rauzy; branch validation fails early |
| `code/zorich_kz_ball.py` | Ball Rauzy–Veech dual with proper Teichmüller time | Slow; radii still grow under modified GS |
| `code/integrator_ball.py` | Constrained ball integrator | Linear-model plane clamp (not Diagram B dual) |
| `certified/path_local_monodromy_sum.json` | Path-local sum ∋ 8/5 | Sum only; individuals not certified |

### A1. Pure paths only
- Disable artificial length resampling (`bounce_eps → off`) for all λ₂/λ₃ runs.
- Record combinatorial path (w, ℓ, which, Δt) from pure Rauzy on Diagram B.
- Replay with length balls; **reject** any step where winner.lo() ≤ loser.hi().

### A2. Error budget (must be explicit in every certificate)
| Source | Model | Notes |
|--------|--------|------|
| Rounding (float → ball) | initial `length_rad` | Sweep 1e-18 … 1e-12 |
| Dual matrix | exact `I − E_{ℓ,w}` | integer, rad = 0 |
| Ball mul/add | standard mid-rad | already in `Ball` |
| Modified GS QR | inflate on sqrt and log|R_ii| | **tighten** (A3) |
| Reorthogonalization | every `R` steps | log_sing accumulates with qr_eps |
| Teichmüller time | `-log(1 - L_ℓ/L_w)` | not endpoint length |
| Length normalization | ball division by sum | fail if 0 ∈ sum |

### A3. Interval / ball QR upgrade
1. Keep pure-Python `modified_gs_qr` as baseline; document radius growth.
2. Prefer: bind **Arb** (python-flint) or **mpmath.iv** QR when available.
3. Acceptance test: on exact unimodular products of length ≤ 100, QR residual balls contain 0 and radii do not explode beyond a fixed factor of machine eps × n_steps.

### A4. Residual-0 projector in the loop
- For **Diagram B dual** (5D), do **not** clamp to the 4D linear-model plane.
- Linear-model constrained integrator remains available for residual-0 regression only.

## Milestone B — Controlled path ensemble

1. Pure dual Rauzy ensemble: start with 10–50 seeds × 10³–10⁴ moves (certifiable scale).
2. Each path: validated branch sequence + ball log-singular values → λ̂_i as balls.
3. Extract positive parts; form balls for λ₂, λ₃.
4. Check sum ball for (λ₂+λ₃) contains 3/5 (or positive-sum contains 8/5).
5. Scale up only when A3 radii are controlled.

## Milestone C — First certified statement

Target form (honest):

> On these explicit pure dual-Rauzy paths for Diagram B, under error budget (A2),
> λ₂ ∈ [a, b], λ₃ ∈ [c, d] with rigorous enclosures, and [a,b]+[c,d] contains 3/5.

If widths are large: publish method + widths. That is still progress.

## First experimental readout (reference only)

From certified path-local sum (seed 728, ~1e5 dual moves):

```
spectrum_normalized_mid: [1.0, 0.4817, 0.1238, 0.0, -1.6055]
pos_sum interval: [1.599945, 1.611119] ∋ 8/5
```

Float/mid shape on that path: λ₂ ≈ 0.48, λ₃ ≈ 0.12 (sum ≈ 0.60).  
**Not** certified individual bounds — only the sum interval is certified under the stated QR model.

## Explicit non-goals
- D=14 / personality framing
- Claiming individuals “solved” before interval control is real
- Using bounce / artificial restarts in certified paths

## Entry points
- `scripts/lambda23_pure_path.py` — pure-path dual evaluation scaffold
- `docs/LAMBDA23_ATTACK.md` — this file
- `code/zorich_kz_ball.py` — proper Teichmüller time + dual ball path
- `code/ball_matrix.py` — Ball / modified_gs_qr to tighten
