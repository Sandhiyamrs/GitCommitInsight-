
import json
from pathlib import Path


def generate_report(data, output_dir="output"):
    Path(output_dir).mkdir(exist_ok=True)

    path = Path(output_dir) / "report.json"
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    return path
