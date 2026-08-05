# Path 2 — Theorem Target

**Status: OPEN**

## Theorem (target)

Let \(\mathcal{C}_D\) be any Teichmüller curve arising from a residual-0 Model A± Prym eigenform in the spectral class \(\Sigma=8/5\) inside \(H_3(4)^{\mathrm{odd}}\). Then the area Siegel–Veech constant satisfies

\[
c_{\mathrm{area}}(\mathcal{C}_D) = \frac{18}{5\pi^2}
\]

independently of the discriminant \(D\). In particular

\[
\lambda_2 + \lambda_3 = \frac{3}{5}.
\]

## Hypotheses

1. Stratum component: \(H_3(4)^{\mathrm{odd}}\).
2. Combinatorics: Model A± three-cylinder type (Track B diagrams).
3. Algebra: residual-0 real multiplication (period vector in the eigenplane of \(T\)).
4. Spectral class: \(\Sigma = 8/5\).

## Already established (computational campaign)

- Cylinder moduli \(m_i = 1\) for all residual-0 Model A±, all \(D\).
- Gate 1 cusp weight \(\sum a_i^2 = (6-\sqrt{3})/12\).
- Gate 1: \(\sum\lambda_i = 8/5\) \(\Rightarrow\) \(c_{\mathrm{area}} = 18/(5\pi^2)\) by EKZ with \(\kappa_{H(4)}=2/5\).
- Combinatorial cusps uniform on the class.
- Track C: 172 arithmetic surfaces, 0 intruders into the Gate 1 spectral window outside \(\Sigma=8/5\).

## Equivalent formulation

\[
c_{\mathrm{area}}(\mathcal{C}_D) = \frac{3}{\pi^2}\,\frac{C_{\mathrm{cusps}}(D)}{|\chi(\mathcal{C}_D)|}.
\]

The theorem is equivalent to: the ratio \(C_{\mathrm{cusps}}(D)/|\chi(\mathcal{C}_D)|\) is independent of \(D\) (and equals \(6/5\)).

## Parallel to Nguyen

Nguyen (arXiv:2510.23333, arXiv:2602.19901) proves that Siegel–Veech constants on \(\Omega E_D(2,2)^{\mathrm{odd}}\) are independent of \(D\) by expressing both numerator and denominator in terms of intersection numbers / Euler characteristics of boundary components of the Prym locus on the Hilbert modular surface, then observing exact cancellation of the \(D\)-dependent factors.

**First theoretical reduction (Path 2):** carry out the analogous intersection-theoretic computation for \(\Omega E_D(4)\subset H_3(4)^{\mathrm{odd}}\):

1. Express \(C_{\mathrm{cusps}}\) as a linear combination of boundary classes of the residual-0 Model A± locus (cylinder configurations at the cusps, weighted by residual-0 relative areas).
2. Express \(\chi(\mathcal{C}_D)\) from the same boundary classes (or from the known classification of components of \(W_D(4)\) by Lanneau–Nguyen).
3. Show the ratio is constant in \(D\).

Once that ratio is constant, EKZ finishes the theorem.

## First lever

Intersection numbers on the Prym locus / Hilbert modular surface for \(\Omega E_D(4)\), following Nguyen’s strategy for \((2,2)\), using the Model A± residual-0 cusp data already locked in Tracks B and D.
