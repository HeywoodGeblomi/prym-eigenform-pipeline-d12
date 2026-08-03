"""High-precision real-multiplication projector using mpmath.
Interface-compatible with the double-precision projector for future swap-in.
"""
import mpmath as mp

mp.mp.dps = 50  # default working precision

D = 12
e = 2
w = 1
h = 1
lam = 1 + mp.sqrt(3)
lam_conj = 1 - mp.sqrt(3)

T = mp.matrix([
    [2, 0, 2, 0],
    [0, 2, 0, 2],
    [1, 0, 0, 0],
    [0, 1, 0, 0],
])

I4 = mp.eye(4)
P_lam = (T - lam_conj * I4) / (lam - lam_conj)

def project(v):
    v = mp.matrix(v)
    return P_lam * v

def residual_minimal_polynomial():
    return float(mp.norm(T * T - e * T - 2 * w * h * I4))

def is_eigenvector(v, tol=mp.mpf('1e-40')):
    v = mp.matrix(v)
    return mp.norm(T * v - lam * v) < tol

if __name__ == "__main__":
    print("HP residual_minimal_polynomial:", residual_minimal_polynomial())
    v = mp.matrix([lam, 0, 1, 0])
    print("HP is_eigenvector:", is_eigenvector(v))
    print("HP rank check via eigenvalues of P_lam:", [float(x) for x in mp.eig(P_lam)[0]])
