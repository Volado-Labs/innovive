#!/usr/bin/env bash
# Reverts /job-application/ (page 3268) to the Contact-Us form GUID.
# Restores the exact _elementor_data captured 2026-08-04 before the HR-form swap.
#
# Auth: export WP_BASIC before running, e.g.
#   export WP_BASIC="$(printf '%s' 'voladoadmin:<app-password-no-spaces>' | base64)"
# The app password lives in ~/workspace/credentials.md, never in this repo.
set -euo pipefail

if [[ -z "${WP_BASIC:-}" ]]; then
  echo "ERROR: set WP_BASIC first (base64 of 'user:app-password'). See header." >&2
  exit 1
fi

BK="$(dirname "$0")/page-3268-2026-08-04-pre-hrformguid.json"
[[ -f "$BK" ]] || { echo "ERROR: backup not found at $BK" >&2; exit 1; }

PAYLOAD=$(mktemp)
trap 'rm -f "$PAYLOAD"' EXIT

python3 - "$BK" "$PAYLOAD" <<'PY'
import json, sys
bk, out = sys.argv[1], sys.argv[2]
d = json.load(open(bk))
ed = d["meta"]["_elementor_data"]
if isinstance(ed, list):
    ed = json.dumps(ed)
json.loads(ed)  # validate before writing
json.dump({"meta": {"_elementor_data": ed}}, open(out, "w"))
PY

curl -s -o /dev/null -w "revert HTTP %{http_code}\n" -X POST \
  -H "Authorization: Basic ${WP_BASIC}" \
  -H "Content-Type: application/json" --data @"$PAYLOAD" \
  "https://innovive.com/wp-json/wp/v2/pages/3268"

sleep 3
echo -n "live GUID now: "
curl -s -L "https://innovive.com/job-application/" | grep -oE 'data-form-id="[a-f0-9-]+"' | head -1
