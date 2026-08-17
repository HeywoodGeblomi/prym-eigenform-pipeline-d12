# Full-rank period lattice from polygonal S(1,-2) — status

## Mathematical fact (locked)

Periods of absolute cycles against a **single** abelian differential \u03c9 always span at most a **2-dimensional** real subspace of \u2102 \u2245 \u211d\u00b2. Period rank 2 is a **theorem**, not a coordinate bug of the origami frame.

## What was built from the polygon

| Object | Rank / value |
|--------|----------------|
| Period matrix against \u03c9 (6 cycles \u00d7 2) | **2** (theorem) |
| Intersection form \u03a9 on 6 cylinder cores | **6** (full) |
| Prym anti-invariant projector rank | **4** |
| Naive derivative \u03c6 = diag(\u03b5\u00b3, \u03b5\u207b\u00b9\u00b3) Lyapunov | only \u00b11 |

Artifacts: `data/fullrank_period_lattice.json`

## Consequence for the gate

Rebuilding the period lattice cannot increase period-rank above 2 for a single \u03c9. Non-tautological KZ expansion requires either:

1. **Combinatorial monodromy that mixes** horizontal and vertical cycles (affine diffeomorphism action beyond pure derivative), or
2. The **full Hodge bundle** H^{1,0} (3 holomorphic forms in genus 3), not periods of \u03c9 alone.

\u03c6\u208a from cylinder multi-twists is symplectic with \u03c1 = 2+\u221a3 but acts as only \u00b11 on the present frames. Path-local dual Rauzy on Diagram B remains the only probe that produced a sum interval containing 8/5 (exploratory, with bounce).

## Success criterion (unchanged)

Recover sum23 \u2248 3/5 under control before any individual claims. `promote_ready: false`
