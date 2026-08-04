# SageMath + flatsurf / surface-dynamics for Gate 1

**Host note:** This blueprint CI machine (~2 GiB RAM) cannot complete a first-launch sage-flatsurf install (~7 GB download). Run these steps on a developer machine, then commit JSON into `geometric/flatsurf_export/`.

## 1. Recommended: Standalone sage-flatsurf (Linux / macOS)

```bash
curl -fsSL https://github.com/flatsurf/sage-flatsurf/releases/download/0.8.0/sage-flatsurf-0.8.0.unix.tar.gz | tar zxf -
cd sage-flatsurf-0.8.0
./sage          # first run downloads ~7GB via pixi
# or
./jupyterlab
```

Path must contain **no spaces**.

## 2. Conda / Miniforge

```bash
curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
bash Miniforge3-$(uname)-$(uname -m).sh
conda create -n flatsurf sage-flatsurf
conda activate flatsurf
pip install ipyvue-flatsurf flipper realalg veerer   # optional
sage
```

## 3. Existing SageMath (≥ 9.5, preferably 10.x)

```bash
sage -pip install sage-flatsurf
# or: sage -pip install surface-dynamics
```

Debian/Ubuntu system packages:

```bash
source /usr/share/sagemath/bin/sage-env
sage -pip install surface-dynamics --user
```

## 4. Windows

- Preferred: `.exe` from [sage-flatsurf Releases](https://github.com/flatsurf/sage-flatsurf/releases).
- Alternative: WSL2 + Linux steps above.

## Quick verification

```sage
from surface_dynamics.all import *
from flatsurf import *
o = Origami('(1,2)', '(1,3)')
print(o)
print(o.sum_of_lyapunov_exponents())
```

## Gate 1 after install

1. Build S(1,±2) from polygons or a positive-length cylinder presentation.
2. Horizontal transversal → ordered vertical edges.
3. Export permutation + lengths + pairings as JSON under `geometric/flatsurf_export/`.
4. Residual-0 / Prym tests → Gate 1 PASS → Phase 2.

Scripts: `build_S_w1_e2.sage`, `construct_from_cylinders.sage`.
