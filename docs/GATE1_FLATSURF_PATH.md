# Why the previous sage script did NOT close Gate 1

1. **Hardcoded permutation** — independence requires extraction from TranslationSurface.
2. **Matrix / λ mismatch** — use T_Ap (e=-2) with λ=-1+√3.
3. **Gluings / API** must produce a valid closed surface.
4. **This host cannot run sage-flatsurf** — export must be produced locally.

Corrected script: `geometric/sage_scripts/gate1_flatsurf_export.sage`

Gate 1 OPEN until real export JSON with extracted perm + residual ~1e-16 without projector.
