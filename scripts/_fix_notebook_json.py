"""One-off script to fix invalid JSON escape sequences in the Phase 3.5 notebook."""
import re
import json
from pathlib import Path

nb_path = Path("notebooks/phase_3_5_metrics_snapshot.ipynb")
raw = nb_path.read_text(encoding="utf-8")

# Replace \X where X is not a valid JSON escape character.
# Valid: \" \\ \/ \b \f \n \r \t \uXXXX
fixed = re.sub(r'\\(?!["\\/bfnrtu])', r'\\\\', raw)

try:
    json.loads(fixed)
    print("Fixed JSON is valid")
    nb_path.write_text(fixed, encoding="utf-8")
    print("Saved")
except json.JSONDecodeError as e:
    print(f"Still broken at pos {e.pos}: {e.msg}")
    print(repr(fixed[max(0, e.pos - 80):e.pos + 80]))
