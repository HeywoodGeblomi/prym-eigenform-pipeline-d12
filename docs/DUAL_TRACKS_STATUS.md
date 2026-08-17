# Dual tracks status

## Track 2 — Path-local (deliverable)

Existing seed-728 Diagram B certificate (`data/path_local_certificate.json`):

| Quantity | Value |
|----------|-------|
| Spectrum mids | [1.0, **0.4817**, **0.1238**, 0, -1.61] |
| pos_sum interval | **[1.5999, 1.6111]** ∋ 8/5 |
| sum23 mid | 0.6055 |
| Scope | PATH-LOCAL only |
| promote_ready | false |

Individuals under the same QR model (path-local):
- λ2 mid ≈ 0.4817
- λ3 mid ≈ 0.1238
- Explicitly **not** global exponents

## Track 1 — Mixing monodromy (breakthrough attempt)

Formal Dehn multi-twists on the 6D intersection form of cylinder cores:

- Best words achieve sum23 ≈ **0.599** and pos ≈ **1.599**
- But the spectrum is **[1, 0.599, 0, 0, -0.599, -1]** — **λ3 = 0** (degenerate)
- No symplectic Dehn word found with both λ2 > 0.05 and λ3 > 0.05 near sum 0.6
- Algebraic mixing recovers a Forni-like zero, not the physical non-degenerate ΩE₁₂ spectrum

## Gate status

- Track 2: controlled path-local sum ∋ 8/5 **exists**; individuals path-local only
- Track 1: mixing exists algebraically but is **degenerate** (λ3=0)
- Full non-degenerate global sum still open
- `promote_ready: false`
