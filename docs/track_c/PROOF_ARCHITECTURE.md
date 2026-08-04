# Track C — Proof architecture (discriminant independence)

**Status:** CONJECTURAL architecture. **Not a proof.**  
**Contributor:** Heywood Geblomi  
**Date:** 2026-08-04

## Target theorem (statement form)

> **Conjectural Theorem C.** On connected components of the relevant two-dimensional Prym eigenform loci ΩE_D(κ), the non-tautological Lyapunov exponents of the Kontsevich–Zorich cocycle (restricted to the Prym anti-invariant subbundle and the real-multiplication eigenplane) are independent of the discriminant D.

Weaker form:

> **Conjectural Theorem C′.** The non-tautological KZ exponents on ΩE_D(4) (genus-3 Weierstrass Prym) are constant in D on each infinite family with fixed congruence type.

## Why this is not yet proved

Requires: (1) certified base case at D=12 (Gate A), (2) certified geometric Rauzy class (Gate B), (3) deformation/continuity of KZ exponents under variation of D, (4) persistence of pinching/twisting or Zariski-dense monodromy. None of these is available in the current repository.

## Lemma chain (architecture only)

### Block 0 — Algebraic infrastructure (PARTIAL; from v0.2.0-candidate)

| ID | Claim | Status |
|----|-------|--------|
| C0.1 | Minimal polynomial of T residual 0 for O_12 | **Done for D=12** |
| C0.2 | P_λ idempotent rank 2 | **Done for D=12** |
| C0.3 | Plane-preserving generators after simultaneous projection | **Done for linear model** |

### Block 1 — Geometric base case (Phases 1–2; BLOCKED)

| ID | Claim | Status |
|----|-------|--------|
| C1.1 | Geometric S(1,±2) has explicit π_12 | BLOCKED on Phase 1 |
| C1.2 | Rauzy class R(π_12) finite and closed under residual-0 filters | BLOCKED on Gate B |
| C1.3 | R(π_12) realises the two-cusp structure of ΩE_12(4) | BLOCKED |

### Block 2 — Certified spectrum at D=12 (Phase 3; BLOCKED)

| ID | Claim | Status |
|----|-------|--------|
| C2.1 | Interval/exact KZ yields rigorous enclosures λ_i^(12) | BLOCKED |
| C2.2 | EKZ sum holds inside enclosures | BLOCKED |
| C2.3 | Avila–Viana pinching+twisting on positive-measure paths | BLOCKED |

### Block 3 — Deformation / independence (Phase 4; CONJECTURAL)

| ID | Claim | Status |
|----|-------|--------|
| C3.1 | Continuity / local constancy of KZ exponents under Prym+RM deformations | Must be established in this setting |
| C3.2 | Prototype space connected for fixed congruence class of D (Lanneau–Nguyen) | Literature; match to KZ bundle |
| C3.3 | Prym + RM splitting persists algebraically in D | CONJECTURAL as precise lemma |
| C3.4 | Pinching/twisting or Zariski-dense monodromy persists for large D | CONJECTURAL |
| C3.5 | Therefore λ_i(D)=λ_i(12) for non-tautological i | CONJECTURAL conclusion |

## Proof strategy

```
Gate B (class at D=12)
  → Gate A (certified λ_i(12) or simplicity)
    → C3.1 continuity
    → C3.2 connectedness in D
    → C3.3 algebraic persistence of splitting
    → C3.4 persistence of simplicity criteria
    → Theorem C′
```

Alternative: coding-free Furstenberg / Zariski-closure methods (Eskin–Matheus) once monodromy is controlled uniformly in D.

## Non-claims

- This document does **not** prove Theorem C or C′.
- Provisional QR numbers are **not** λ_i(12).
- The candidate Rauzy class is **not** R(π_12).
