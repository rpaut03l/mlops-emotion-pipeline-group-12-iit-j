"""
T2 — Data Preparation & Normalisation
======================================
Loads the `dair-ai/emotion` dataset (split config, 6-class), inspects it,
applies the cleaning decisions documented in the report, encodes labels, and
writes the committed `id2label.json`.

Cleaning decisions (see report Section 5) — kept deliberately minimal because
the dataset is already clean:
  * Whitespace strip + collapse only.
  * NO manual lowercasing — `distilbert-base-uncased` lowercases in its
    tokenizer, so doing it here would be redundant.
  * Exact-duplicate removal on TEXT (31 rows in train, ~0.19%).
  * Cross-split de-leak: texts present in train that also appear in
    validation or test are dropped from train only; validation/test stay
    untouched as unbiased benchmarks.

Label order comes from the dataset's built-in ClassLabel, matching the model
trained on Kaggle and the committed mapping:
    0:sadness 1:joy 2:love 3:anger 4:fear 5:surprise

Run locally:
    pip install -r requirements.txt datasets
    python src/prepare_data.py

Importable too:
    from src.prepare_data import clean_text, prepare
"""

import os
import re
import json
import argparse
from collections import Counter

from datasets import load_dataset

# --- paths -----------------------------------------------------------------
HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(HERE)
ID2LABEL_PATH = os.path.join(REPO_ROOT, "id2label.json")
CLEAN_DIR = os.path.join(REPO_ROOT, "data", "clean")  # gitignored; local only

# --- cleaning --------------------------------------------------------------
_WS_RE = re.compile(r"\s+")


def clean_text(text: str) -> str:
    """Strip and collapse whitespace. No lowercasing (tokenizer handles that)."""
    return _WS_RE.sub(" ", text).strip()


def _dedupe_on_text(dataset):
    """Drop empty/whitespace-only texts, then rows whose TEXT was already seen."""
    seen = set()
    keep = []
    for i, row in enumerate(dataset):
        text = row["text"]
        if text == "":            # drop empty/whitespace-only (post-strip)
            continue
        if text not in seen:
            seen.add(text)
            keep.append(i)
    return dataset.select(keep)


def _deleak(train_ds, eval_texts):
    """Drop train rows whose text appears in the eval set (validation ∪ test)."""
    keep = [i for i, row in enumerate(train_ds) if row["text"] not in eval_texts]
    removed = len(train_ds) - len(keep)
    return train_ds.select(keep), removed


# --- main pipeline ---------------------------------------------------------
def prepare(save: bool = True, write_mapping: bool = True):
    """Load, inspect, clean, de-leak, encode, and (optionally) persist.

    Returns the cleaned dict of splits and the id2label mapping.
    """
    print("Loading dair-ai/emotion (split config)...")
    ds = load_dataset("dair-ai/emotion", "split")

    # --- inspect: sizes + class distribution + imbalance note -------------
    label_feature = ds["train"].features["label"]
    id2label = {i: name for i, name in enumerate(label_feature.names)}

    print("\n=== Inspection ===")
    for part in ("train", "validation", "test"):
        if part in ds:
            print(f"{part:>10}: {len(ds[part]):>6} rows")
    print(f"classes ({label_feature.num_classes}): {label_feature.names}")

    counts = Counter(ds["train"]["label"])
    total = sum(counts.values())
    print("\ntrain class distribution:")
    for cid in sorted(counts):
        pct = 100 * counts[cid] / total
        print(f"  {cid} {id2label[cid]:<9} {counts[cid]:>6}  ({pct:4.1f}%)")
    top, bottom = max(counts.values()), min(counts.values())
    print(f"imbalance ratio (max/min): {top / bottom:.1f}x  "
          f"-> note: joy/sadness dominate; love/surprise are minority.")

    # report-style quality checks
    n_dup_train = len(ds["train"]) - len(set(ds["train"]["text"]))
    print(f"\nexact-duplicate texts in train: {n_dup_train}")

    # --- clean (strip/collapse whitespace, NO lowercasing) ----------------
    print("\nCleaning text (whitespace only) and de-duplicating on text...")
    cleaned = {}
    for part in ds:
        before = len(ds[part])
        part_ds = ds[part].map(
            lambda ex: {"text": clean_text(ex["text"])},
            desc=f"clean[{part}]",
        )
        part_ds = _dedupe_on_text(part_ds)
        cleaned[part] = part_ds
        print(f"  {part:>10}: {before} -> {len(part_ds)} after dedupe")

    # --- cross-split de-leak: train rows that also appear in val/test -----
    if "train" in cleaned and ("validation" in cleaned or "test" in cleaned):
        eval_texts = set()
        for part in ("validation", "test"):
            if part in cleaned:
                eval_texts |= set(cleaned[part]["text"])
        before = len(cleaned["train"])
        cleaned["train"], removed = _deleak(cleaned["train"], eval_texts)
        print(f"\nde-leak: dropped {removed} train rows also present in "
              f"validation/test ({before} -> {len(cleaned['train'])}); "
              f"validation/test untouched")

    # labels are already encoded as ints (0-5) by the ClassLabel feature.
    # id2label is the single source of truth, in the same order as training.

    # --- persist ----------------------------------------------------------
    if write_mapping:
        with open(ID2LABEL_PATH, "w") as f:
            json.dump({str(k): v for k, v in id2label.items()}, f, indent=2)
        print(f"\nWrote label map -> {ID2LABEL_PATH}")

    if save:
        os.makedirs(CLEAN_DIR, exist_ok=True)
        for part, part_ds in cleaned.items():
            out = os.path.join(CLEAN_DIR, f"{part}.parquet")
            part_ds.to_parquet(out)
        print(f"Saved cleaned splits -> {CLEAN_DIR}/ (local only, gitignored)")
        print("Reminder: commit ONLY id2label.json, not the dataset.")

    return cleaned, id2label


def main():
    ap = argparse.ArgumentParser(description="T2 data prep & normalisation")
    ap.add_argument("--no-save", action="store_true",
                    help="skip writing cleaned parquet files")
    ap.add_argument("--no-mapping", action="store_true",
                    help="skip writing id2label.json")
    args = ap.parse_args()
    prepare(save=not args.no_save, write_mapping=not args.no_mapping)


if __name__ == "__main__":
    main()
