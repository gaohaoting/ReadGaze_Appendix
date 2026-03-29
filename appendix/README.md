# Supplementary materials (UIST 2026)

This repository contains **optional** supplementary materials for peer review: algorithm validation documentation and a reproducibility script layout. The main paper is intended to be self-contained; reviewers are not required to use this repository to evaluate the contribution.

## Contents

| Path | Description |
|------|-------------|
| `supplementary/sanity_check_report_en.md` | Extended sanity-check report (algorithm validation summary). |
| `scripts/sanity_check.py` | Python script to reproduce validation analyses when session data are provided. |
| `sample_data/README.md` | Expected on-disk layout for session CSVs (no raw data shipped here). |
| `POLICY_CHECKLIST.md` | UIST 2026 compliance checklist for authors. |

## Reproducing analyses

1. Install **Python 3.10+** (stdlib only; no pip packages required).
2. Place de-identified session folders under `scripts/Datasets/` as described in `sample_data/README.md`.
3. Run:

```bash
cd scripts && python3 sanity_check.py
```

If `Datasets/` is empty or missing, the script runs and reports zero sessions (no crash).

## Anonymized link for submission

Do **not** cite a personal GitHub URL in the anonymized paper. After uploading this `appendix/` tree to GitHub, create an anonymous mirror at [anonymous.4open.science](https://anonymous.4open.science/) and cite **only** that URL.

## PCS upload

Zip **only** this `appendix/` directory (or the repository if it contains solely this folder) and upload as supplementary material by the materials deadline (see `POLICY_CHECKLIST.md`). Maintainer notes for zipping live outside the tracked tree in this repo layout.
