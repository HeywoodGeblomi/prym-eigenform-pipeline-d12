# Phase 1 — Geometric completion (INITIATED)

**Goal:** Replace the linear-model / candidate combinatorial input by the geometric S(w=1,e=±2) surface of Lanneau–Nguyen, with side pairings and Prym involution ρ, then read off the initial generalized permutation.

## Known from the literature

- Prototype parameters: (w,h,t,e)=(1,1,0,±2).
- Discriminant D=e²+8w=12 for the standard S-model in ΩE_D(4).
- ΩE_12(4) is a single connected Teichmüller curve with exactly two cusps (Lanneau–Nguyen).
- Complete periodicity results apply to Prym eigenforms in this family.
- Model A± three-cylinder decompositions are the relevant combinatorial type.

## Required geometric data (BLOCKED until transcribed or constructed)

| Item | Status |
|------|--------|
| Edge-labelled polygonal model with translation pairings | **Missing** as machine-readable data |
| Explicit action of ρ on edges / homology | **Missing** in open labelled form |
| Ordered vertical edges crossed by a horizontal transversal | **Missing** (candidate only) |
| Suspension heights / zippered-rectangle data | **Missing** |

## Method (do not fabricate)

1. Published high-resolution figure of S(1,±2) **or** construct in sage-flatsurf / surface_dynamics.
2. Label edges; write pairing list; choose transversal compatible with three-cylinder decomposition.
3. Read off generalized permutation and length vector.
4. Test against residual-0 projector and Prym predicates in code/verify.py.
5. **Gate 1:** accept only if exact residual-0 and Prym compatibility hold.

## Relation to candidate data

data/candidate_rauzy_class_d12.json is a geometrically *motivated hypothesis*, not Gate 1 output. Phase 2 must not treat it as the certified class.

## Immediate checklist

- [ ] Obtain labelled figure or flatsurf construction
- [ ] Write geometric/side_pairings.json
- [ ] Write geometric/initial_permutation.json
- [ ] Run residual-0 + Prym tests in exact arithmetic
- [ ] Record Gate 1 pass/fail in docs/EXECUTION_LOG.md
