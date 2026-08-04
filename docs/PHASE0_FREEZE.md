# Phase 0 — Freeze of the provisional scaffold

**Date:** 2026-08-04  
**Contributor:** Heywood Geblomi

## Decision

The public tree at `v0.2.0-candidate` is frozen as the last **provisional** release:

- residual-0 projector T, P_λ
- plane-preserving corrected generators (linear model)
- candidate (non-geometric) Rauzy class
- uncertified QR spectra

## Rules going forward

1. No claim of certified spectra or geometric Rauzy class may appear under the `v0.2.0-candidate` tag.
2. All geometric / certified work lives under `geometric/` and `certified/`.
3. Gate failures block promotion of downstream claims.
4. Track C statements are marked CONJECTURAL until Gates A and B close.

## Recommended git tag

```bash
git tag -a v0.2.0-candidate -m "Freeze: provisional residual-0 scaffold; not certified"
git push origin v0.2.0-candidate
```

## Assets retained as lemmas for later phases

| Lemma | Status |
|-------|--------|
| L0.1 T²−2T−2I=0 residual 0 | **Machine-checked** (double + dps=50) |
| L0.2 P_λ idempotent rank 2 | **Machine-checked** |
| L0.3 Prototype vector is λ-eigenvector | **Machine-checked** |
| L0.4 Corrected generators preserve eigenplane to ~1e-16 | **Machine-checked** (float); exact form pending Phase 3 |
