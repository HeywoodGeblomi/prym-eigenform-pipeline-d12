# prym-eigenform-pipeline-d12 — Computational Release v1.0.0

**PROJECT COMPUTATIONALLY COMPLETE**

```text
Gate 1:  PASS
Track A: FROZEN
Track B: CLOSED
Track C: COMPUTATIONALLY COMPLETE
Track D: REDUCED TO A SINGLE RESEARCH THEOREM
```

Contributor: **Heywood Geblomi**
Repository: https://github.com/HeywoodGeblomi/prym-eigenform-pipeline-d12

---

## Gate 1 — PASS

- CylinderDiagram: `(0,2)-(4) (1,4)-(2,3) (3)-(0,1)`
- Stratum: H₃(4)^odd
- Algebraic lengths: `[λ, 1−λ, 1−λ, λ, λ]` with `λ = −1+√3`
- Widths: `(1, 1, λ)`
- Residual-0: exact 0 (no projector)
- Prototype: `(w,h,t,e)=(1,1,0,−2)`, D=12
- Identification: Lanneau–Nguyen Model A+; S(1,±2) up to SL(2,ℝ)

## Track A — FROZEN

**Exact (theorem-level from origami sum):**
| Identity | Value |
|----------|--------|
| λ₁ | 1 |
| λ₂ + λ₃ | 3/5 |
| Σ positive | 8/5 |

**Empirical 3σ (30 × 500k native KZ, not IA-certified):**
| | Mean | Interval |
|--|------|----------|
| λ₂ | 0.418 | [0.403, 0.433] |
| λ₃ | 0.182 | [0.167, 0.197] |

## Track B — CLOSED

- 4 Model A± cusps in H₃(4)
- Rauzy class H₃(4)^odd: 134 permutations, 268 edges, 30 unique matrices
- Residual-0 edges (homology proxy): 222/268

## Track C — COMPUTATIONALLY COMPLETE

> Across 172 arithmetic surfaces in H₃(4) with nsq = 5…30, the spectral window of Gate 1 is occupied exclusively by the Σ = 8/5 class. No surface from any other class enters that window.

| Class | Count | λ₂ range | λ₃ range |
|-------|-------|----------|----------|
| Σ = 8/5 | 83 | [0.394, 0.434] | [0.164, 0.205] |
| Σ = 9/5 | 89 | [0.600, 0.621] | [0.179, 0.200] |

Intruders into Gate 1 window: **0**. Computational evidence — not a formal proof of D-independence.

## Track D — REDUCED (not proved)

**Target theorem.** Inside the Prym locus of H₃(4)^odd, every Teichmüller curve of residual-0 Model A± type in the spectral class Σ=8/5 has

```text
λ₂ + λ₃ = 3/5
```

independently of the discriminant D.

**Structural reduction completed:**
1. Residual-0 ⇒ all cylinder moduli mᵢ = 1 (λ(D) cancels in height/width)
2. Gate 1 cusp weight: Σ aᵢ² = (6−√3)/12
3. EKZ on Gate 1: κ_{H(4)}=2/5 ⇒ c_area = 18/(5π²)
4. Combinatorial cusps uniform on the class (Track B)
5. **Open:** prove C_cusps / |χ(C_D)| independent of D (intersection theory on ΩE_D(4), parallel to Nguyen arXiv:2602.19901 for (2,2))

Once (5) is proved, EKZ finishes the theorem.

## What may be cited

- Residual-0 algebraic claims (endomorphism T, projector, eigenvector)
- Gate 1 combinatorial identification
- Exact sum identities λ₁=1, λ₂+λ₃=3/5, Σ=8/5
- Track C census statement (as computational evidence)
- Track D reduction to the ratio C_cusps/|χ|

## What must not be cited as theorem

- Individual λ₂, λ₃ as IA-certified enclosures
- Formal D-independence (Track D open gap)
- Candidate linear-model Rauzy data as the geometric class

## License

MIT. Research code; use at your own risk.
