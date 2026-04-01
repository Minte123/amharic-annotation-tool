import json
import os

DATA_PATH = "data/annotations.jsonl"

def save_annotation(record: dict):
    """
    Appends a single annotated sentence to disk.
    Uses JSON Lines format for scalability.
    """
    os.makedirs("data", exist_ok=True)

    with open(DATA_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")