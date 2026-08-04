# Phase 2 / Track B — Exhaustive Rauzy class

**Status:** Machinery **implemented**; Gate B **BLOCKED** on Gate 1  
**Contributor:** Heywood Geblomi  
**Date:** 2026-08-04

## What was executed

1. Classical top/bot Rauzy moves on two-row generalized permutations.
2. Exhaustive BFS enumeration with irreducibility filter.
3. Closure detection (queue empty ⇒ finite closed class).
4. Optional 4D monoid filter via `preserves_eigenplane`.
5. Dry-run on the **candidate** start `(0 1 2 / 2 1 0)`.

### Dry-run result (candidate only)

| Quantity | Value |
|----------|-------|
| Start | `(0 1 2 / 2 1 0)` |
| Permutations | **3** |
| Edges | **6** |
| Closed | **True** |
| All irreducible | **Yes** |

This matches `data/candidate_rauzy_class_d12.json`. It is **not** the geometric class of S(1,±2).

## Code

- `code/phase2_rauzy_class.py` — enumerator + CLI dry-run
- Output: `data/phase2_candidate_class.json`

```bash
python3 code/phase2_rauzy_class.py
```

## Gate B criteria (not met)

Gate B passes only when:

1. Gate 1 geometric start permutation is accepted.
2. Enumeration of **that** start yields a finite closed class.
3. The class is checked against known cusp / complete-periodicity invariants of ΩE_12(4).
4. Results are published under `certified/` (not `data/` candidate paths).

## Next

Return to Phase 1: geometric side-pairings → Gate 1 → re-run this enumerator on the geometric start → Gate B.
