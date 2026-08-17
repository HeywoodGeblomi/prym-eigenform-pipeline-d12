# Track 1 — Non-degenerate mixing (formal)

## Result

Random search over Dehn multi-twist words on the 6D intersection form found **non-degenerate** spectra:

| Quantity | Best |
|----------|------|
| λ₂ | **0.2989** |
| λ₃ | **0.2989** |
| sum23 | **0.5978** (target 0.6) |
| pos_sum | **1.5978** (target 1.6) |
| Both > 0.1 | **yes** |
| Degenerate (λ₃=0) | **no** |

Word: `(3,1)(4,2)(2,4)(0,3)(3,5)(0,5)(1,4)(5,2)(3,5)` (Dehn powers about cylinder cores).

## Caveat

This is **formal algebraic** monodromy on the intersection form of abstract cylinder cores. It is **not** yet identified with a geometric affine diffeomorphism of polygonal S(1,-2). Path-local seed-728 gives a different split (0.48 / 0.12).

## Next

Identify a geometric affine map of S(1,-2) whose induced action on H₁ matches (or is conjugate to) a non-degenerate word, then integrate Gauss–Manin along that geodesic.

`promote_ready: false`
