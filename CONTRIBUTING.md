# Contributing — Group 12 workflow

Short, strict, and tuned to the rubric (every member needs visible commits + real PR reviews).

## Branch model
- `main` — protected, release-only. Never push directly.
- `develop` — integration branch. CI runs on every push here.
- `feature/<task>-<short>` — one per work item, branched off `develop`.

```bash
git checkout develop && git pull
git checkout -b feature/t2-data-clean
# ...work...
git add -p && git commit -m "T2: clean + dedupe emotion text"
git push -u origin feature/t2-data-clean
gh pr create --base develop --fill
```

## Commit messages (Conventional Commits)
```
<type>(<task>): <summary>
```
Types: `feat`, `fix`, `docs`, `chore`, `refactor`, `test`, `ci`.
Examples: `feat(t4): add V2 run at lr=5e-5`, `docs(readme): add links table`.

## Pull requests
- One PR = one task slice; keep it small and reviewable.
- Fill the PR template; reference the task ("Closes T2 cleaning").
- CI (flake8) must pass.
- **A different teammate must approve** — you cannot approve your own PR.
  (This approval is what earns the T1 "PR review" marks — don't skip it.)
- Update `## [Unreleased]` in `CHANGELOG.md` in the same PR.

## Reviewer checklist
- [ ] Code runs / lint passes
- [ ] No secrets or tokens committed
- [ ] No large data/model files added (only `id2label.json`)
- [ ] CHANGELOG updated
- [ ] PR description explains the *why*

## Who reviews whom (rotate so all 4 have review activity)
| Author | Reviewer |
|---|---|
| Rohit | Amit |
| Amit | Venkata |
| Venkata | Aishwarya |
| Aishwarya | Rohit |
