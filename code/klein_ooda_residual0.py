"""Klein-bottle Möbius-OODA + residual-0 RM projector.
COMPUTATIONAL ANALOGY ONLY. Does NOT close Gate 1.
"""
from typing import List, Any
import numpy as np

lam = 1.0 + np.sqrt(3.0)
lam_conj = 1.0 - np.sqrt(3.0)
T = np.array([[2.,0,2,0],[0,2,0,2],[1,0,0,0],[0,1,0,0]], dtype=float)
I4 = np.eye(4)
P_lam = (T - lam_conj * I4) / (lam - lam_conj)

def project(v):
    return P_lam @ np.asarray(v, dtype=float)

def residual_minimal_polynomial():
    return float(np.linalg.norm(T @ T - 2.0 * T - 2.0 * I4))

class KleinState:
    def __init__(self, tape, init_vec=None):
        self.tape = list(tape)
        self.control_parity = 0
        self.data_parity = 0
        if init_vec is None:
            init_vec = np.array([lam, 0.0, 1.0, 0.0])
        self.homology = project(init_vec)
    def twist_control(self):
        self.control_parity ^= 1
        self.data_parity ^= 1
    def twist_data(self):
        self.data_parity ^= 1
        self.control_parity ^= 1
    def project_homology(self):
        self.homology = project(self.homology)
        s = np.abs(self.homology).sum()
        if s > 0:
            self.homology = np.abs(self.homology) / s

def observe(tape, idx, data_parity):
    n = len(tape)
    neighbour = idx + (1 if data_parity == 0 else -1)
    if not (0 <= neighbour < n):
        return (tape[idx], None)
    return (tape[idx], tape[neighbour])

def orient(obs, data_parity):
    a, b = obs
    if b is None:
        return (a, None)
    return (a, b) if data_parity == 0 else (b, a)

def decide(ori):
    a, b = ori
    if b is None:
        return False
    return a > b

def act(tape, idx, data_parity, invert=False):
    step = 1 if data_parity == 0 else -1
    neighbour = idx + step
    if 0 <= neighbour < len(tape):
        tape[idx], tape[neighbour] = tape[neighbour], tape[idx]

def klein_ooda_sort(tape, max_cycles=6):
    state = KleinState(tape)
    n = len(state.tape)
    if n < 2:
        return state.tape, state
    for cycle in range(max_cycles):
        start, end, step = (0, n, 1) if state.control_parity == 0 else (n - 1, -1, -1)
        for i in range(start, end, step):
            j = i
            while True:
                obs = observe(state.tape, j, state.data_parity)
                ori = orient(obs, state.data_parity)
                if not decide(ori):
                    break
                act(state.tape, j, state.data_parity, invert=(state.data_parity == 1))
                state.project_homology()
                j += step
                if not (0 <= j < n):
                    break
        state.twist_control()
        state.project_homology()
        if cycle % 2 == 1:
            state.twist_data()
            state.project_homology()
    return state.tape, state

if __name__ == "__main__":
    print("residual_minimal_polynomial =", residual_minimal_polynomial())
    data = [7, 3, 9, 1, 5, 2, 8, 4, 6]
    print("before:", data)
    result, st = klein_ooda_sort(data, max_cycles=8)
    print("after :", result)
    r = float(np.linalg.norm(T @ st.homology - lam * st.homology))
    print("final ||T h - lam h|| =", r)
    print("NOTE: computational analogy only — does not close Gate 1.")
