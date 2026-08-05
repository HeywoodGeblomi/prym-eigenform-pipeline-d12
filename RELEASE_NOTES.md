# prym-eigenform-pipeline-d12 — Campaign Complete

**Tag target: `v1.1.0-theorem`**

```text
Gate 1:  PASS
Track A: FROZEN
Track B: CLOSED
Track C: COMPUTATIONALLY COMPLETE
Path 2:  CLOSED — THEOREM PROVED
```

Contributor: **Heywood Geblomi**
Repository: https://github.com/HeywoodGeblomi/prym-eigenform-pipeline-d12

---

## Theorem (proved)

Every Teichmüller curve in $H_3(4)^{\mathrm{odd}}$ (in particular every residual-0 Model A± Prym curve of any admissible discriminant $D$) satisfies

$$
c_{\mathrm{area}} = \frac{18}{5\pi^2},\qquad \lambda_2+\lambda_3=\frac{3}{5}.
$$

**Proof.** Chen–Möller (Geom. Topol. 16, 2012; arXiv:1104.3932) establish that the sum of Lyapunov exponents is non-varying and equal to $8/5$ on the entire odd component of $H(4)$. The Eskin–Kontsevich–Zorich formula then forces the constant Siegel–Veech value above. See `docs/PATH2_THEOREM_PROVED.md`.

---

## Campaign record

### Gate 1 — PASS
- CylinderDiagram: `(0,2)-(4) (1,4)-(2,3) (3)-(0,1)`
- Stratum: $H_3(4)^{\mathrm{odd}}$
- Algebraic lengths: $[\lambda, 1-\lambda, 1-\lambda, \lambda, \lambda]$, $\lambda=-1+\sqrt{3}$
- Residual-0: exact 0
- Prototype: $(w,h,t,e)=(1,1,0,-2)$, $D=12$

### Track A — FROZEN
Exact: $\lambda_1=1$, $\lambda_2+\lambda_3=3/5$, $\Sigma=8/5$.
Empirical 3σ (not IA-certified): $\lambda_2\in[0.403,0.433]$, $\lambda_3\in[0.167,0.197]$.

### Track B — CLOSED
4 Model A± cusps · Rauzy class 134 · residual-0 edges 222/268.

### Track C — COMPUTATIONALLY COMPLETE
172 arithmetic surfaces (nsq 5…30): Gate 1 spectral window occupied exclusively by the $\Sigma=8/5$ class; zero intruders.

### Path 2 — THEOREM PROVED
Chen–Möller non-varying + EKZ. The five intersection numbers are superfluous for the sum. Individual $\lambda_2,\lambda_3$ remain open.

---

## What may be cited

- Residual-0 algebraic claims
- Gate 1 combinatorial identification
- Exact sum identities (now theorem-level for the whole odd component)
- Track C census (computational evidence)
- Path 2 theorem (as corollary of Chen–Möller + EKZ)

## What remains open

- Individual exponents $\lambda_2$, $\lambda_3$ (separation within the sum $3/5$)
- Interval-arithmetic certified enclosures

## License

MIT. Research code; use at your own risk.

## Credit

**Heywood Geblomi** — project lead of the computational and structural campaign; contributor to the final theorem.
