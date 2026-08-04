# Release Notes — v0.2.0-candidate

**Date:** 2026-08-04  
**Status:** Research blueprint with candidate combinatorial Rauzy data  
**(not a certified spectrum package)**

**Contributor:** [Heywood Geblomi](https://github.com/HeywoodGeblomi)

**Repository:** https://github.com/HeywoodGeblomi/prym-eigenform-pipeline-d12

## What this release contains

- Exact real-multiplication endomorphism \(T\) with residual **0** (double and 50-digit precision).
- Rank-2 projector \(P_\lambda\) onto the \(\lambda=1+\sqrt{3}\) eigenplane (idempotent).
- Corrected generators `A_top_corr`, `A_bot_corr`, `S_corr` (eigenplane residual \(\sim10^{-16}\)).
- Raw unimodular generators for the constrained integrator (eigenplane enforced by continuous re-projection).
- Candidate combinatorial Rauzy class: **3 permutations, 6 edges**.
- Residual-0-filtered 4-D monoid: **65 matrices**.
- `benchmarks.md` with residual and class-size numbers.
- Regression suite: **5/5 tests**.
- Hash-pin automation (`scripts/update_readme_hash.sh`) with structured logging.

## What this release does not contain

- Certified geometric Rauzy class of the published S-shaped surface.
- Certified Lyapunov spectra of a genuine Prym eigenform.
- Interval-arithmetic long runs or a completed EKZ sum check on a genuine spectrum.
- Any new theorem.

Provisional numerical exponents must **not** be cited as Lyapunov exponents of a surface in \(\Omega E_{12}\).

## Stage-4 status

| Step | Status |
|------|--------|
| 1. Polygonal model + side identifications + \(\rho\) | Advanced (geometric derivation) |
| 2. Horizontal transversal | Done |
| 3. Initial generalized permutation + lengths | Candidate written down |
| 4. Rauzy induction under residual-0 filter | Executed on the **candidate** |
| 5. Enumerate + algebraic filter | Candidate: 3 perms / 6 edges; monoid size 65 |
| 6. Publish permutations + matrices | `data/candidate_rauzy_class_d12.json` |

The combinatorial data is a geometrically derived **candidate**, not a certified extraction from the published S-shaped surface.

## Citation policy

- You **may** cite residual-0 algebraic claims and corrected-generator residuals.
- You **must not** cite provisional spectra or the candidate class as certified geometric results.

Suggested form:

> Exact real-multiplication projector, plane-preserving generator corrections, and geometrically derived candidate Rauzy data for the discriminant-12 S-shaped prototype (residual 0). Heywood Geblomi. https://github.com/HeywoodGeblomi/prym-eigenform-pipeline-d12

## License

MIT. See `LICENSE`.

## Changelog since v0.1.0

- Plane-preserving corrected generators.
- Candidate edge pairings and generalized permutation from geometry.
- Rauzy induction on the candidate; published class + monoid.
- `benchmarks.md`.
- Integrator default: raw unimodular generators + continuous projection.
- Regression suite expanded to 5 tests (all passing).
- README hash-pin script + structured logging + optional GitHub Action.
