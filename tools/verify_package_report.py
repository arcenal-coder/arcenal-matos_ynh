"""A successful command without a package report is not an installation proof."""
import json
from pathlib import Path
import sys

def failed(value):
    if isinstance(value, dict):
        return any(item == "failure" or failed(item) for item in value.values())
    if isinstance(value, list):
        return any(failed(item) for item in value)
    return False

reports = list(Path(sys.argv[1]).glob("results_*.json"))
if not reports:
    raise SystemExit("Aucun rapport package_check produit.")
for report in reports:
    data = json.loads(report.read_text())
    if failed(data):
        raise SystemExit("Le rapport package_check contient un scénario en échec.")
print("Rapports package_check présents et sans scénario en échec.")
