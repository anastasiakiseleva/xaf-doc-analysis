"""Fix ALL invalid JSON escape sequences by parsing the JSON tokens properly."""
import json
import re
from pathlib import Path

nb_path = Path("notebooks/phase_3_5_metrics_snapshot.ipynb")
raw = nb_path.read_text(encoding="utf-8")

errors = []
pos = 0
text = raw
while True:
    try:
        json.loads(text)
        break
    except json.JSONDecodeError as e:
        errors.append(e.pos)
        # Replace the single bad backslash at e.pos with double backslash
        text = text[:e.pos] + "\\\\" + text[e.pos + 1:]

print(f"Fixed {len(errors)} escape errors at positions: {errors}")

try:
    json.loads(text)
    print("Resulting JSON is valid")
    nb_path.write_text(text, encoding="utf-8")
    print("Saved")
except json.JSONDecodeError as e:
    print(f"Could not fully fix: {e}")
