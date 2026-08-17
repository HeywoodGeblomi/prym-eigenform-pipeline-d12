# Continuous dynamics — zippered-rectangle section & geodesic probe

**Decision locked:** continuous dynamics only. No more discrete graph enumeration.

## What was built

1. **Continuous RV section** — state (\u03c0, \u03bb, h), area 1, heights by dual. Geometric init. Pure runs still one-sided (dirs=0), spectrum collapsed.

2. **Teichm\u00fcller hybrid** (`code/teichmueller_geodesic_kz.py`) — continuous time + origami parabolic twists (6D H\u2081). mean sum23 \u2248 0.09 (target 0.6).

3. **RM hyperbolic on 4D residual-0 plane** — \u03c6 with eigenvalues \u03b5,\u03b5,\u03b5\u207b\u00b9,\u03b5\u207b\u00b9. Lyapunov **only \u00b11**. Non-tautological exponents are not in the 4D RM plane alone.

## Hard conclusion

| Object | Spectrum |
|--------|----------|
| Finite IET Rauzy dual | ~0 |
| Origami parabolic | sum23 \u226a 0.6 |
| RM hyperbolic 4D | only \u00b11 |
| Target | \u03bb\u2081=1, \u03bb\u2082+\u03bb\u2083=3/5 |

KZ of \u03a9E\u2081\u2082 is the **Gauss\u2013Manin / Hodge-bundle cocycle** along the Teichm\u00fcller geodesic — not the Rauzy cocycle of the horizontal IET class alone.

## Required for breakthrough

Full **6D** KZ/Gauss\u2013Manin along g_t on polygonal/origami S(1,-2), including **hyperbolic** Veech monodromy, residual-0/Prym preserved.

Success criterion: sum23 \u2248 3/5 (or pos \u2248 8/5) before any individual claims.

`promote_ready: false`
