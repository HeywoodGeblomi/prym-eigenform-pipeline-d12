# Scripts

## `update_readme_hash.sh`

Rewrites the pinned commit hash in the root `README.md` to the current `HEAD`.

```bash
# After your content commits:
./scripts/update_readme_hash.sh
git add README.md
git commit -m "chore: pin README commit hash"
```

The optional GitHub Action `.github/workflows/update-readme-hash.yml` runs the same
step on pushes to `main` and creates a follow-up pin commit when needed.
