"""
Backward-compatible re-export of Rauzy generators.

 Prefer importing from code.rauzy_generators (matrices) or
 code.enumerate_rauzy_graph (graph construction) for single-responsibility use.
"""
from .rauzy_generators import *  # noqa: F401,F403
