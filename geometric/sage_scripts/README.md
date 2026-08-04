# Sage / flatsurf scripts for Gate 1

## Environment requirement

`surface_dynamics` and `sage-flatsurf` **require SageMath**. They do not install into plain CPython.

This host has ~2 GiB RAM and no SageMath — full Sage cannot be installed here.

## What to run on a Sage-enabled machine

```bash
sage geometric/sage_scripts/build_S_w1_e2.sage
```

Expected for Gate 1 PASS:

1. Polygon vertices for S(1,±2)
2. Side pairings
3. Horizontal transversal → ordered vertical edges
4. Generalized permutation + lengths
5. JSON under `geometric/flatsurf_export/`

## Status on this host

| Check | Result |
|-------|--------|
| pip install surface-dynamics | FAIL (needs SageMath) |
| pip install flatsurf / sage-flatsurf | FAIL |
| System RAM | ~2 GiB |
| Gate 1 | **OPEN** |
