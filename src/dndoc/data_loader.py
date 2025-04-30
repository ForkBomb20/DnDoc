import json
from pathlib import Path

CHARACTER_FILE = Path("data/dan_quixote.json")

def load_character():
    if CHARACTER_FILE.exists():
        with open(CHARACTER_FILE, "r") as f:
            return json.load(f)
    return {}  # default empty character if not found

def save_character(data):
    CHARACTER_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(CHARACTER_FILE, "w") as f:
        json.dump(data, f, indent=4)
