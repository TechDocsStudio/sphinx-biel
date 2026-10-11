"""Regenerate option metadata from a published widget directory (no JS execution)."""
import json
from pathlib import Path
import re
import sys

root = Path(sys.argv[1])
version = json.loads((root / "package.json").read_text())["version"]
source = (root / "dist/collection/components/biel-button/biel-button.js").read_text()
match = re.search(r"static get properties\(\)\s*\{\s*return\s*", source)
if not match:
    raise ValueError("Published collection does not expose button properties")
properties, _ = json.JSONDecoder().raw_decode(source[match.end():])
options = {}
for name, metadata in properties.items():
    key = re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower()
    options[key] = {"property": name, "attribute": metadata.get("attribute"), "type": metadata["type"]}
output = Path(__file__).resolve().parents[1] / "src/sphinx_biel/widget_options.json"
output.write_text(json.dumps({"version": version, "options": options}, indent=2, sort_keys=True) + "\n")
