# CylinderDiagram extraction methods (Gate 1)

## Route 1 — surface_dynamics

```sage
from surface_dynamics import *
cd = CylinderDiagram('(0,1)-(0,2) (2)-(1)')  # after geometry supplies cycles
cd.bot_cycle_tuples()
cd.top_cycle_tuples()
cd.separatrix_diagram()
cd.stratum()
```

Cycle tuples are the ordered edge lists for the return map.

## Route 2 — sage-flatsurf

```sage
from flatsurf import *
decomp = T.cylinder_decomposition(direction=(1, 0))
cylinders = T.cylinders(direction=(1, 0))
```

Extract from returned object — do not hardcode.

## Checklist

1. Build TranslationSurface from polygons + gluings only
2. Call cylinder/flow decomposition
3. Read ordered cycles from the object
4. Export JSON
5. Native residual with no projector

Script: `geometric/sage_scripts/gate1_extract_cylinder_diagram.sage`
