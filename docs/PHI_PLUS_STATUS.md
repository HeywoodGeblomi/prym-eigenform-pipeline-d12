# Hyperbolic Veech element \u03c6\u208a \u2014 status

## Built
- \u03c6\u208a as word in origami cylinder multi-twists: H\u2080\u00b3 V\u2080\u00b2 (and other words)
- 6\u00d76 monodromy on H\u2081, **symplectic** (det=1, \u03a9-preserving)
- Spectral radius = **2+\u221a3** (fundamental unit of Q(\u221a3))
- Artifact: `data/phi_plus_monodromy.json`, `code/hyperbolic_veech_phi.py`

## Lyapunov of this monodromy
Normalized by log(\u03c1):

```
[1, 0, 0, 0, 0, -1]
pos_sum = 1.0   (target 1.6)
sum23   = 0.0   (target 0.6)
```

## Interpretation
This \u03c6\u208a generates the **tautological** hyperbolic action of the Teichm\u00fcller geodesic corresponding to the RM unit. On the present origami frame, the Prym complement appears with multiplier 1 (zero Lyapunov). Non-tautological \u03bb\u2082, \u03bb\u2083 are **not** carried by this monodromy matrix alone.

## Gate status
- Hyperbolic element: **constructed** (symplectic, correct unit)
- Sum recovery: **not achieved**
- `promote_ready: false`

## Next (still this gate)
Need the Hodge-norm / Gauss\u2013Manin realization of the KZ cocycle along g_t in which the Prym complement is **not** fixed by \u03c6\u208a, or a different presentation of H\u2081 where non-tautological expansion is visible. Cylinder-twist words in the current frame are insufficient for the sum.
