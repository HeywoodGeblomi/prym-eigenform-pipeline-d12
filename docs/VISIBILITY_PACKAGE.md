# Making the D=12 scaffold usable

Goal: present residual-0 algebra, geometric construction, dual Rauzy evaluation, and related tools so specialists can check and reuse them. No campaign framing.

## Entry ticket

A short computational note on arXiv (math.DS / math.GT) is the primary public artefact. Draft: paper/computational_note_d12.tex.

The note states accurately:
- what is new (exact RM projector, plane-preserving generators, residual-0 checks, geometric construction, constrained integrator, path-local dual evaluation under a stated model);
- what is not (the sum of Lyapunov exponents on the locus — that is Chen-Moller).

## Repo hygiene

- README and RELEASE_NOTES state rigorous vs provisional claims without sprint language.
- certified/ holds narrow documented claims only.
- CONTRIBUTORS.md does not claim authorship of Chen-Moller.

## Public communication

After arXiv is live, a brief technical post with the arXiv link is appropriate. Prefer dry language. Tag sparingly, if at all. Do not describe the work as proving the sum of Lyapunov exponents.

## What not to do

- Do not use release titles such as v1.1.0-theorem.
- Do not describe Path 2 / the sum as a theorem proved in this repository.
- Do not cite float ensemble means as formal bounds on individual exponents.
