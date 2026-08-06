#!/usr/bin/env python3
"""Apply Volado house paragraph spacing to an existing Google Doc.

Targeted fix, not a rebuild: the doc already has correct named styles, tables
and bullets from the HTML conversion. Rebuilding via the vault's build_doc()
would destroy the tables, which it does not handle. So this only sets
spaceAbove/spaceBelow on top-level body paragraphs.

Table cell paragraphs are deliberately left alone; Docs already applies cell
padding and adding spacing there makes tables tall and loose.

Spacing scale from wiki/concepts/google-docs-api-editing.md.
"""
import json
import subprocess
import sys
import time

DOC_ID = sys.argv[1] if len(sys.argv) > 1 else None
if not DOC_ID:
    sys.exit("usage: fix_doc_spacing.py <documentId>")

# (spaceAbove, spaceBelow) in PT
SPACING = {
    "HEADING_1": (24, 8),
    "HEADING_2": (20, 6),
    "HEADING_3": (14, 4),
    "HEADING_4": (12, 4),
    "SUBTITLE": (4, 14),
    "NORMAL_TEXT": (6, 6),
}
BULLET = (3, 3)


def gws(*args, stdin_json=None):
    r = subprocess.run(["gws", *args], capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"gws failed: {r.stderr[:400]}")
    return r.stdout


doc = json.loads(gws("docs", "documents", "get",
                     "--params", json.dumps({"documentId": DOC_ID})))

reqs = []
for el in doc["body"]["content"]:
    para = el.get("paragraph")
    if not para:
        continue  # tables, section breaks, TOC
    style = para.get("paragraphStyle", {}).get("namedStyleType", "NORMAL_TEXT")
    # A bulleted paragraph carries a `bullet` key; keep list items tight.
    above, below = BULLET if "bullet" in para else SPACING.get(style, (6, 6))
    reqs.append({
        "updateParagraphStyle": {
            "range": {"startIndex": el["startIndex"], "endIndex": el["endIndex"]},
            "paragraphStyle": {
                "spaceAbove": {"magnitude": above, "unit": "PT"},
                "spaceBelow": {"magnitude": below, "unit": "PT"},
            },
            "fields": "spaceAbove,spaceBelow",
        }
    })

print(f"paragraphs to restyle: {len(reqs)}")

# Batches capped at 50; the API 429s above that.
for i in range(0, len(reqs), 50):
    chunk = reqs[i:i + 50]
    gws("docs", "documents", "batchUpdate",
        "--params", json.dumps({"documentId": DOC_ID}),
        "--json", json.dumps({"requests": chunk}))
    print(f"  applied {i + len(chunk)}/{len(reqs)}")
    if i + 50 < len(reqs):
        time.sleep(0.5)

print("done")
