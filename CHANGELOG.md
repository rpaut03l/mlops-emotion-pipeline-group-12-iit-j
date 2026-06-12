# Changelog

All notable changes to this project are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/);
this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]


### Added
- Report: Archietciure image and updated README.md


### Changed
- Restrict auto-merge to feature/* PRs into develop (excludes drafts, re-checks on push).


### Fixed

---

## [Unreleased]


### Added
- T1: Restrict auto-merge to feature/* PRs into develop (excludes drafts, re-checks on push).
- T2: Prepare data and perform clean up
- T3: Load a public hugging face model and load the correct id2labels
- T4: Train multiple versions on kaggle & Track with W&B
- T5: Push the trained Model to Hugging face hub
- T6: Docker inference image (rohitpatel/mlops-a3-inference)
- T7: Manual inference workflow.


### Changed
- Restrict auto-merge to feature/* PRs into develop (excludes drafts, re-checks on push).


### Fixed

---


## [0.1.0] - 2026-06-09
### Added
- Initial repository scaffold: `README.md`, `.gitignore`, MIT `LICENSE`.
- `develop` branch and `main` branch protection (1 PR review required).
- `CONTRIBUTING.md`, PR template, `CODEOWNERS`, auto-merge + CI workflows.
- Project structure for `src/`, `notebooks/`, `.github/workflows/`.

  

[Unreleased]: https://github.com/rpaut03l/mlops-emotion-pipeline-group-12-iit-j/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/rpaut03l/mlops-emotion-pipeline-group-12-iit-j/releases/tag/v0.1.0

