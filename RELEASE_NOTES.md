# Release notes

## Computational scaffold for the discriminant-12 Prym prototype

This repository provides verified algebraic and combinatorial tools for the McMullen discriminant-12 S-shaped Prym eigenform prototype, together with a constrained integrator and related diagnostics.

### What is provided

1. **Exact real-multiplication structure.**
   Endomorphism T satisfying T^2-2T-2I=0 with residual 0 (double and 50-digit checks); idempotent rank-2 projector P_lambda; prototype period as exact eigenvector.

2. **Plane-preserving corrected generators.**
   Corrected Rauzy generators that preserve the eigenplane to residual ~10^{-16}.

3. **Geometric construction of S(1,-2).**
   Independent pure-Python octagon construction, cylinder data, and generalised permutation extracted from the horizontal return map, with period residual on the order of machine epsilon without forced re-projection.

4. **Constrained KZ integrator and dual Rauzy evaluation.**
   Code for iterating the cocycle under algebraic constraints, and a dual Rauzy path evaluation whose positive-part sum lies in an interval containing 8/5 under a controlled QR error model (see certified/).

5. **Regression tests** locking the residual-0 algebraic claims.

### What is not claimed

- A new proof of the sum of Lyapunov exponents on H(4)^odd or on Omega E_12(4). That sum is 8/5 by Chen-Moller non-varying (and is consistent with the EKZ formula). This repository records computational consistency with that known value; it does not establish the theorem.
- Formal interval bounds on the individual non-tautological exponents lambda_2 and lambda_3. Floating-point ensemble means remain experimental.
- An exhaustive geometric Rauzy class beyond the presentations used here.

### Citation

Prefer the short computational note in paper/computational_note_d12.tex once posted on arXiv. Until then, cite specific residual-0 algebraic claims and the geometric construction as verified in the tests and artefacts under geometric/.

Do not cite float ensemble spectra as rigorous Lyapunov exponents of Omega E_12.
