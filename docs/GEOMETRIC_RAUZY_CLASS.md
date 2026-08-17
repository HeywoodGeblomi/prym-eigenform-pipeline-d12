# Geometric Rauzy class of S(1,-2) — extraction report

**Decision (A)** locked. Extraction from polygon / cylinder data.

## Classes obtained

| Class | Start | |V| | |E| | Strongly connected |
|-------|-------|------|------|--------------------|
| 4-interval (Gate-1 geometric) | top=[3,0,1,2], bot=[0,1,2,3] | **12** | 24 | yes |
| 5-interval Diagram B | top=[4,2,3,0,1], bot=[0,2,1,4,3] | **33** | 66 | yes |
| 3-interval cylinder | top=[0,1,2], bot=[2,1,0] | 3 | 6 | yes |

Sources:
- 4-interval: pure-Python S(1,-2) octagon horizontal return (Gate-1 PASS)
- 5-interval: CylinderDiagram `(0,2)-(4) (1,4)-(2,3) (3)-(0,1)` (LN D=12 / gate1_PASS)
- Lengths 4-int: `[\u03bb, 1\u2212\u03bb, \u03bb, 1]`, \u03bb = \u22121+\u221a3
- Lengths 5-int: `[\u03bb, 1\u2212\u03bb, 1\u2212\u03bb, \u03bb, \u03bb]`

Artifacts:
- `data/geometric_rauzy_class_S12.json` (4-int)
- `data/geometric_rauzy_class_diagram_B.json` (5-int)
- `data/geometric_rauzy_extraction_report.json`

## Mixing under length dynamics

**No.** Deterministic iteration falls into one-sided cycles (dir_changes = 0). Dual monodromy unit-modulus \u2192 suspended spectrum \u2248 0.

## First suspended spectrum

Deterministic pure: collapsed. Measure-resample probe (exploratory): \u03bb\u2082 mean \u2248 0.25, sum23 \u2248 0.28 \u2014 not 3/5, not pure.

`promote_ready: false`

## Blocker

Physical individuals need Rauzy\u2013Veech invariant measure on (combinatorics \u00d7 lengths \u00d7 heights) or Teichm\u00fcller geodesic monodromy on the period lattice of polygonal S(1,-2).

## Next (still path A)

Continuous zippered-rectangle section with heights under Rauzy\u2013Veech measure, or geodesic flow on period coordinates of the octagon.
