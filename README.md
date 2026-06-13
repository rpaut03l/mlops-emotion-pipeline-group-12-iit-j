# 🎭 mlops-emotion-pipeline-group-12-iit-j

> **End-to-end MLOps pipeline** — fine-tuning `distilbert-base-uncased` on the `dair-ai/emotion` dataset (6-class text classification), with Kaggle GPU training, Weights & Biases tracking, Hugging Face model hosting, Docker inference, and GitHub Actions CI/CD.

[![CI](https://github.com/rpaut03l/mlops-emotion-pipeline-group-12-iit-j/actions/workflows/ci.yaml/badge.svg?branch=develop)](https://github.com/rpaut03l/mlops-emotion-pipeline-group-12-iit-j/actions/workflows/ci.yaml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/)
[![Model: DistilBERT](https://img.shields.io/badge/model-distilbert--base--uncased-orange.svg)](https://huggingface.co/distilbert-base-uncased)
[![Dataset: dair-ai/emotion](https://img.shields.io/badge/dataset-dair--ai%2Femotion-ff69b4.svg)](https://huggingface.co/datasets/dair-ai/emotion)

**Course:** MLOps · M.Tech AI Program · IIT Jodhpur · **Group 12**

---

## 📑 Table of Contents
- [Architecture](#-architecture)
- [Tech Stack](#-tech-stack)
- [Live Links](#-live-links)
- [Team & Ownership](#-team--ownership)
- [Task Breakdown & Marks](#-task-breakdown--marks)
- [Contribution Log](#-contribution-log)
- [Repository Structure](#-repository-structure)
- [Quickstart](#-quickstart)
- [Secrets](#-secrets)
- [Branching & PR Workflow](#-branching--pr-workflow)
- [Versioning & Changelog](#-versioning--changelog)

---

## 🏗 Architecture

![alt text](./HLD_UML.svg)


## 🧰 Tech Stack

| Layer | Tool |
|---|---|
| Model | `distilbert-base-uncased` (Hugging Face Transformers) |
| Dataset | `dair-ai/emotion` — `split` config (20k) |
| Training | Kaggle Notebook, GPU T4, HF `Trainer` API |
| Experiment tracking | Weights & Biases |
| Model registry | Hugging Face Hub (public) |
| Packaging | Docker (slim Python 3.11) |
| CI/CD | GitHub Actions |

## 🔗 Live Links

| Component | Link | Status |
|---|---|---|
| GitHub Repo | https://github.com/rpaut03l/mlops-emotion-pipeline-group-12-iit-j | ✅ public |
| Kaggle Notebook (V1 + V2) | https://www.kaggle.com/code/shyamg25ait2134/notebook012c22c8bb | ✅ public |
| Hugging Face Model | https://huggingface.co/G25AIT2134/distilbert-emotion | ✅ public |
| Docker Image | https://hub.docker.com/r/rohitpatel/mlops-a3-inference | ✅ public |
| W&B Dashboard | https://wandb.ai/g25ait2134-iitj/mlops-emotion-distilbert/workspace?nw=nwuserg25ait2134 | ✅ public |

> ⚠️ Every link must open in an **incognito window** at submission time. Private/broken = 0 for that component.

## 👥 Team & Ownership

| Member | GitHub Handle | Role | Owns |
|---|---|---|---|
| Rohit Patel (G25AIT2089) | [@rpaut03l](https://github.com/rpaut03l) | Admin / Owner | T1, T6, T7 |
| Yekkirala Venkata Radhe Shyam (G25AIT2134) | [@g25ait2134-tech](https://github.com/g25ait2134-tech) · [@vrsyvby](https://github.com/vrsyvby) | Collaborator (Write) | T4, T5 |
| Amit Singh (G25AIT2007) | [@Amitstreet](https://github.com/Amitstreet) | Collaborator (Write) | T2, T8 |
| Aishwarya Mishra (G25AIT2137) | [@g25ait2137-ops](https://github.com/g25ait2137-ops) | Collaborator (Write) | T3, Report |


## ✅ Task Breakdown & Marks

| # | Task | Owner | Marks |
|---|---|---|---|
| T1 | Set up GitHub repository (branch protection, collaborators) | Rohit | 10 |
| T2 | Data preparation & normalisation | Amit | 15 |
| T3 | Select & load model from Hugging Face | Aishwarya | 10 |
| T4 | Train 2 versions on Kaggle + W&B tracking | Venkata | 25 |
| T5 | Push trained model to Hugging Face Hub | Venkata | 5 |
| T6 | Create Dockerfile (inference container) | Rohit | 10 |
| T7 | GitHub Actions — CI + Inference workflows | Rohit | 15 |
| T8 | W&B experiments dashboard | Amit | 5 |
| T9 | Report PDF (4–5 pages) | Aishwarya | 5 |
| T10 | HLD, LLD, drift, fairness simulation | Venkata |
| | **TOTAL** | | **100** |

### Detailed do-items
<details>
<summary><b>T1 — GitHub Repo (10) · Rohit</b></summary>

- [x] Create **public** repo with `README.md`, `.gitignore`, `LICENSE` — **2**
- [x] Add `develop` branch; protect `main` (≥1 PR review to merge) — **3**
- [x] Admin (Rohit) + 3 Collaborators with **Write** — **3**
- [x] Screenshot Collaborators settings page → report — **2**
</details>

<details>
<summary><b>T2 — Data Prep & Normalisation (15) · Amit</b></summary>

- [x] Inspect raw data: 16k/2k/2k, 6 classes, note class imbalance — **3**
- [x] Clean: lowercase, strip URLs, collapse whitespace, dedupe — **6**
- [x] Encode labels + save `id2label.json` — **3**
- [x] Save dataset locally; commit **only** the mapping file — **3**
</details>

<details>
<summary><b>T3 — Select & Load Model (10) · Aishwarya</b></summary>

- [x] Load `distilbert-base-uncased` tokenizer — **3**
- [x] Load model with `num_labels=6` from `id2label` — **3**
- [x] 100–150 word justification citing the HF model card → report — **4**
</details>

<details>
<summary><b>T4 — Train 2 Versions + W&B (25) · Venkata</b></summary>

- [x] Store `WANDB_API_KEY` + `HF_TOKEN` in Kaggle Secrets — **3**
- [x] V1 `lr=2e-5` / V2 `lr=5e-5` (one hyperparameter changed) — **7**
- [x] Log train loss, val loss, accuracy, F1, all hyperparams — **7**
- [x] Screenshot W&B with both runs → report — **5**
</details>

<details>
<summary><b>T5 — Push to Hugging Face (5) · Venkata</b></summary>

- [x] Push weights + tokenizer to public HF repo — **3**
- [x] Log HF URL to `wandb.run.summary` — **2**
- [x] (gate) HF repo Public — Actions inference pulls from here
</details>

<details>
<summary><b>T6 — Dockerfile (10) · Rohit</b></summary>

- [x] Slim Python base + inference deps only — **3**
- [x] `ARG HF_MODEL_NAME` with sensible default — **2**
- [x] Build + test locally end-to-end — **3**
- [x] Push to public registry; URL → report — **2**
</details>

<details>
<summary><b>T7 — GitHub Actions (15) · Rohit</b></summary>

- [x] CI workflow (`ci.yaml`) — lint on push→`develop` — **5**
- [x] Inference workflow (`inference.yml`) — manual `workflow_dispatch` — **7**
- [x] `HF_TOKEN` in GitHub Secrets; no committed tokens — **3**
- [x] Trigger inference → success screenshot → report
</details>

<details>
<summary><b>T8 — W&B Dashboard (5) · Amit</b></summary>

- [x] Both runs visible · project Public · comparison table (Accuracy, F1, Loss) · paste URL → report
</details>

## 📒 Contribution Log

Keep this updated as work lands — it feeds the "individual contributions" section of the report.

| Date | Member | What | PR |
|---|---|---|---|
| 2026-06-09 | Rohit | Repo init, branch protection, scaffold | #1 |
| 2026-06-11| Amit| Created workflow to pull kaggle notebook with initial data preparation and cleanup| #10|
| 2026-06-09| Aishwarya| Experimented with distilbert uncased public model, id2label, tokenizer| #6|
| 2026-06-11| Venkata| Added notebook to capture wandb metrics, pushed trained model to hugging face, simulated drift, fairness| #20|
| 2026-06-11| Rohit| Added Docker yml and inference yml, py files| #22|
| 2026-06-12| Aishwarya| architecture diagram and readme file updates| #23|

## 🗂 Repository Structure

```
.
├── .github/
│   ├── workflows/
│   │   ├── amit.yml                 # syncs Kaggle notebook into the repo
│   │   ├── ci.yaml                  # T7.1: lint on push→develop
│   │   ├── inference.yml            # T7.2: manual inference (workflow_dispatch)
│   │   ├── auto-merge.yml           # native auto-merge on approved PRs
│   │   └── pull_request_template.md # PR template
│   └── CODEOWNERS                   # auto-requests reviewers per path
├── notebooks/
│   ├── notebook012c22c8bb.ipynb     # T4/T5 training (V1+V2) + T10 drift & fairness analysis
│   └── train_kaggle.ipynb           # T4/T5: train V1+V2, push best to HF
├── src/
│   └── inference.py                 # Docker + Actions entrypoint
├── Dockerfile                       # T6
├── HLD_UML.svg                      # rendered high-level design diagram
├── LLD_UML.svg                      # rendered low-level design diagram
├── hld.puml                         # PlantUML source — HLD
├── lld.puml                         # PlantUML source — LLD
├── id2label.json                    # committed label map (6 emotions)
├── requirements.txt
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE                          # MIT
└── README.md
```

## 🚀 Quickstart

```bash
# 1. Data prep (T2) — local
pip install -r requirements.txt datasets
python src/prepare_data.py            # uses load_dataset("dair-ai/emotion","split")

# 2. Training (T4/T5) — Kaggle GPU T4
#    Upload notebooks/train_kaggle.ipynb, add Kaggle Secrets, run V1 then V2,
#    push best model to a PUBLIC Hugging Face repo.

# 3. Build + test inference image (T6)
docker build --build-arg HF_MODEL_NAME=G25AIT2134/distilbert-emotion \
             -t mlops-a3-inference:latest .
# Model is public, so HF_TOKEN is optional. To pass one, inherit from the shell
# (export HF_TOKEN=... first) rather than typing the secret on the command line:
docker run --rm -e INPUT_TEXT='i feel so happy today' mlops-a3-inference:latest   # -> joy

# 4. Push image
docker push <dockerhub-user>/mlops-a3-inference:latest
```

## 🔐 Secrets

| Secret | Where | Used by |
|---|---|---|
| `WANDB_API_KEY` | Kaggle → Add-ons → Secrets | Training (T4) |
| `HF_TOKEN` | Kaggle Secrets **and** GitHub → Settings → Secrets → Actions | Training push (T5), inference workflow (T7) |

> Never commit tokens. `.gitignore` already excludes `.env`, `*.key`, `kaggle.json`.

## 🌿 Branching & PR Workflow

`main` is protected (≥1 review required). Nobody pushes to `main` directly.

```
main      ●──────────────●────────────●     (protected, release branch)
           \            / \          /
develop     ●──●──●──●──●   ●──●──●──●        (integration branch, CI runs here)
                 \                /
feature/<task>    ●──●──●──●──●──●            (one short-lived branch per work item)
```

1. Branch off `develop`: `git checkout develop && git pull && git checkout -b feature/t2-data-prep`
2. Commit + push, then open a PR **into `develop`**.
3. CODEOWNERS auto-requests a reviewer; a **different teammate** approves.
4. Merge to `develop` (auto-merge will do this once approved + CI green).
5. Periodically open a PR `develop → main` (requires 1 approval) for releases.

### Code / PR review rules
- One PR = one task slice. Keep them small.
- You **cannot approve your own PR** — pick a teammate (this is what earns the "PR review" marks).
- CI (flake8) must be green before merge.
- Use the PR template; link the task (e.g. "Closes T2 cleaning").

## 🏷 Versioning & Changelog

We use [Semantic Versioning](https://semver.org/) `MAJOR.MINOR.PATCH` and [Keep a Changelog](https://keepachangelog.com/).

| Bump | When |
|---|---|
| MAJOR | breaking change to the pipeline contract |
| MINOR | new capability (e.g. V2 model, new workflow) |
| PATCH | fixes, doc tweaks |

Tag a release after merging to `main`:
```bash
git checkout main && git pull
git tag -a v0.1.0 -m "Scaffold + repo setup"
git push origin v0.1.0
gh release create v0.1.0 --title "v0.1.0" --notes-from-tag
```

See [CHANGELOG.md](./CHANGELOG.md). Update the `## [Unreleased]` section in the same PR as your change.
