import os
import sys
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

MODEL = os.environ.get("HF_MODEL_NAME", "G25AIT2134/distilbert-emotion")
TEXT = os.environ.get("INPUT_TEXT", "i feel so happy today")
TOKEN = os.environ.get("HF_TOKEN") or None  # public model - not needed


def main():
    print(f"Loading model: {MODEL}")
    tok = AutoTokenizer.from_pretrained(MODEL, token=TOKEN)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL, token=TOKEN)
    model.eval()
    inputs = tok(TEXT, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        logits = model(**inputs).logits
    pid = int(logits.argmax(-1))
    print(f"INPUT : {TEXT}")
    print(f"PRED  : {model.config.id2label.get(pid, pid)}  (class {pid})")


if __name__ == "__main__":
    sys.exit(main())
