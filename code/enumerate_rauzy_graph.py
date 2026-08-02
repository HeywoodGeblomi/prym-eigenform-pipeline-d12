#!/usr/bin/env python3
"""
Enumerate the Prym-symmetric Rauzy graph (linear model) for D=12.

Vertices = integer matrices on H_1^- reachable from the identity by the
four Prym-compatible generators. Writes data/rauzy_graph_d12.json.
"""
import json
from collections import deque
from pathlib import Path

import numpy as np

from rauzy import A_top, A_bot, A_top_sym, A_bot_sym
from rm_projector import lam


def enumerate_graph(max_vertices=64):
    gens = {
        "top": A_top,
        "bot": A_bot,
        "top_sym": A_top_sym,
        "bot_sym": A_bot_sym,
    }
    key = lambda M: tuple(np.round(M.flatten(), 10))
    start = np.eye(4)
    vertices = {key(start): start}
    edges = []
    queue = deque([start])

    while queue and len(vertices) < max_vertices:
        cur = queue.popleft()
        for name, A in gens.items():
            new = A @ cur
            k = key(new)
            edges.append(
                {
                    "from": cur.round(10).tolist(),
                    "to": new.round(10).tolist(),
                    "type": name,
                    "matrix": A.tolist(),
                }
            )
            if k not in vertices:
                vertices[k] = new
                queue.append(new)

    return {
        "description": (
            "Prym-symmetric Rauzy graph (linear model) for the S-shaped "
            "D=12 prototype. Vertices are integer matrices on H_1^- "
            "reachable from the identity by four Prym-compatible generators. "
            "Not the exhaustive zippered-rectangle Rauzy class."
        ),
        "generators": {k: v.tolist() for k, v in gens.items()},
        "vertices": [v.round(10).tolist() for v in vertices.values()],
        "edges": edges,
        "transition_matrices": [v.round(10).tolist() for v in vertices.values()],
        "suspension_data": {
            "initial_heights": [lam, 1.0, 1.0, 1.0],
            "projector": "P_lam = (T - lam_conj*I)/(lam - lam_conj)",
            "note": "Re-project height/period vectors by P_lam after every move.",
        },
        "counts": {
            "vertices": len(vertices),
            "edges": len(edges),
            "generators": len(gens),
        },
    }


if __name__ == "__main__":
    graph = enumerate_graph()
    out = Path(__file__).resolve().parent.parent / "data" / "rauzy_graph_d12.json"
    with open(out, "w") as f:
        json.dump(graph, f, indent=2)
    print(f"Wrote {out}")
    print("Counts:", graph["counts"])
