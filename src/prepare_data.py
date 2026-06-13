"""
T2 — Data Preparation & Normalisation
======================================
Loads the `dair-ai/emotion` dataset (split config, 6-class), inspects it,
applies text cleaning, encodes labels, and writes the committed `id2label.json`.

The label order is taken directly from the dataset's built-in ClassLabel, so it
matches the model trained on Kaggle and the committed mapping:
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
_URL_RE = re.compile(r"http\S+|www\.\S+")
_WS_RE = re.compile(r"\s+")


def clean_text(text: str) -> str:
    """Lowercase, strip URLs, collapse whitespace."""
    text = text.lower()
    text = _URL_RE.sub(" ", text)
    text = _WS_RE.sub(" ", text)
    return text.strip()


def _dedupe(dataset):
    """Drop exact-duplicate (text, label) rows. Returns filtered dataset."""
    seen = set()
    keep = []
    for i, row in enumerate(dataset):
        key = (row["text"], row["label"])
        if key not in seen:
            seen.add(key)
            keep.append(i)
    return dataset.select(keep)


# --- main pipeline ---------------------------------------------------------
def prepare(save: bool = True, write_mapping: bool = True):
    """Load, inspect, clean, encode, and (optionally) persist the dataset.

    Returns the cleaned DatasetDict and the id2label mapping.
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
    print("\ntrain class distribution:")
    for cid in sorted(counts):
        print(f"  {cid} {id2label[cid]:<9} {counts[cid]:>6}")
    top, bottom = max(counts.values()), min(counts.values())
    print(f"imbalance ratio (max/min): {top / bottom:.1f}x  "
          f"-> note: 'joy'/'sadness' dominate; 'surprise'/'love' are minority.")

    # --- clean (lowercase, strip URLs, collapse whitespace) + dedupe ------
    print("\nCleaning text and de-duplicating...")
    cleaned = {}
    for part in ds:
        before = len(ds[part])
        part_ds = ds[part].map(
            lambda ex: {"text": clean_text(ex["text"])},
            desc=f"clean[{part}]",
        )
        part_ds = _dedupe(part_ds)
        cleaned[part] = part_ds
        print(f"  {part:>10}: {before} -> {len(part_ds)} after dedupe")

    # labels are already encoded as ints (0-5) by the ClassLabel feature.
    # id2label is the single source of truth, in the same order as training.

    # --- persist ----------------------------------------------------------
    if write_mapping:
        with open(ID2LABEL_PATH, "w") as f:
            # keys as strings to match the committed JSON / HF config format
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
