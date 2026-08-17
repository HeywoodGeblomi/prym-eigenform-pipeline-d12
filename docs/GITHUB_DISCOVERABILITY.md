# GitHub discoverability + Zenodo DOI (manual steps)

These actions require the repo owner's UI (or API scopes we do not have for metadata/releases).

## 1. About box (2 minutes)

Open: https://github.com/HeywoodGeblomi/prym-eigenform-pipeline-d12  
Click the gear icon next to **About**.

**Description** (paste):
```
Computational scaffold for the discriminant-12 Prym eigenform: residual-0 RM projector, geometric construction of S(1,-2), dual Rauzy evaluation
```

**Topics** (add one by one):
```
teichmuller-dynamics
lyapunov-exponents
kontsevich-zorich
prym-eigenforms
translation-surfaces
rauzy-veech
```

Save.

## 2. New sober release (for Zenodo)

Do **not** promote the old `v1.1.0-theorem` tag. Create a new release from current `main`.

1. https://github.com/HeywoodGeblomi/prym-eigenform-pipeline-d12/releases/new
2. Tag: `v0.3.0-scaffold` (create new tag on `main`)
3. Release title: `Computational scaffold for the D=12 Prym prototype`
4. Body (paste):

```
Verified residual-0 real-multiplication projector, plane-preserving generators, geometric construction of S(1,-2), constrained KZ integrator, and dual Rauzy path evaluation.

See README and certified/ for scope. Individual non-tautological Lyapunov exponents remain experimental. The sum 8/5 on H(4)^odd is due to Chen-Moller; this release does not claim that theorem.

Computational note draft: paper/computational_note_d12.tex
```

5. Publish release.

Optional: mark the old `v1.1.0-theorem` release as **draft** or delete it if you want campaign language off the Releases page.

## 3. Zenodo DOI

1. Log in at https://zenodo.org with GitHub
2. GitHub → Settings → Applications → Zenodo → grant access to this repo (or enable in Zenodo → GitHub)
3. On Zenodo, flip the switch for `prym-eigenform-pipeline-d12`
4. Create/publish the GitHub release above if not done — Zenodo mints a DOI on the release
5. Copy the DOI into README citation and CITATION.cff when you have it

## 4. After DOI exists

Update README “How to cite” with the Zenodo DOI and keep arXiv for when endorsement arrives.
