import json
from pathlib import Path

def offload_profiles() -> dict:
    file_path = Path(__file__).parent / "config.json"

    if not file_path.is_file():
        return {}

    with open(file_path, "r") as f:
        return json.load(f)

NEW_PROFILES = offload_profiles()
