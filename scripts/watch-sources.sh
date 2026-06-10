#!/usr/bin/env bash
#
# watch-sources.sh — detect when the official sources behind references/*.md
# files have changed, so the curated summaries can be reviewed.
#
# Manifest:  scripts/source-watch.json   (what to watch, and which reference
#                                          file to review when it fires)
# Baseline:  scripts/source-watch.baseline.json  (committed; last known state)
#
# Check types:
#   celex — original legal acts are immutable, so the change signal is a NEW
#           amending / correcting / consolidating act appearing in the
#           Publications Office graph. Counts inbound cdm relations via the
#           public SPARQL endpoint (no WAF, unlike eur-lex.europa.eu).
#   hash  — for living documents (PDFs, web pages): sha256 of the downloaded
#           content; HTML is normalized (scripts/styles stripped) first to
#           ignore per-request tokens.
#
# Usage:  scripts/watch-sources.sh            # check against baseline
#         scripts/watch-sources.sh --update   # accept current state as baseline
#
# Exit codes: 0 all unchanged · 1 changes detected · 2 errors only
# Run monthly via .github/workflows/source-watch.yml or manually.
set -uo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
MANIFEST="$ROOT/scripts/source-watch.json"
BASELINE="$ROOT/scripts/source-watch.baseline.json"
SPARQL="http://publications.europa.eu/webapi/rdf/sparql"
UA="Mozilla/5.0 (compatible; agents-for-EU source-watch)"

UPDATE=0
[[ "${1:-}" == "--update" ]] && UPDATE=1

red()    { printf '\033[31m%s\033[0m\n' "$1"; }
green()  { printf '\033[32m%s\033[0m\n' "$1"; }
yellow() { printf '\033[33m%s\033[0m\n' "$1"; }

current_celex() { # $1 = celex id -> count of inbound amend/correct/consolidate relations
  local celex="$1"
  # parentheses must be percent-encoded inside the URI
  local enc="${celex//\(/%28}"; enc="${enc//)/%29}"
  local q="PREFIX cdm: <http://publications.europa.eu/ontology/cdm#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
SELECT (COUNT(DISTINCT ?a) AS ?n) WHERE {
  ?w owl:sameAs <http://publications.europa.eu/resource/celex/$enc> .
  { ?a cdm:resource_legal_amends_resource_legal ?w }
  UNION { ?a cdm:resource_legal_corrects_resource_legal ?w }
  UNION { ?a cdm:act_consolidated_consolidates_resource_legal ?w }
  UNION { ?a cdm:resource_legal_repeals_resource_legal ?w }
}"
  curl -sf --max-time 60 -G "$SPARQL" --data-urlencode "query=$q" \
       -H "Accept: text/csv" | tail -1 | tr -d '"\r'
}

current_hash() { # $1 = url -> sha256 of (normalized) content
  local url="$1" tmp
  tmp="$(mktemp)"
  if ! curl -sfL --max-time 300 -A "$UA" -o "$tmp" "$url"; then
    rm -f "$tmp"; return 1
  fi
  if file "$tmp" | grep -qi 'html\|text'; then
    python3 - "$tmp" <<'EOF'
import re, sys, hashlib
d = open(sys.argv[1], encoding='utf-8', errors='replace').read()
d = re.sub(r'<script.*?</script>', '', d, flags=re.S)
d = re.sub(r'<style.*?</style>', '', d, flags=re.S)
d = re.sub(r'\s+', ' ', d)
print(hashlib.sha256(d.encode()).hexdigest())
EOF
  else
    shasum -a 256 "$tmp" | cut -d' ' -f1
  fi
  rm -f "$tmp"
}

changed=0; errors=0; checked=0
new_baseline='{}'
old_baseline='{}'
[[ -f "$BASELINE" ]] && old_baseline="$(cat "$BASELINE")"

n=$(jq '.sources | length' "$MANIFEST")
for ((i=0; i<n; i++)); do
  id=$(jq -r ".sources[$i].id" "$MANIFEST")
  type=$(jq -r ".sources[$i].type" "$MANIFEST")
  backs=$(jq -r ".sources[$i].backs" "$MANIFEST")

  if [[ "$type" == "celex" ]]; then
    celex=$(jq -r ".sources[$i].celex" "$MANIFEST")
    value="$(current_celex "$celex")" || value=""
  else
    url=$(jq -r ".sources[$i].url" "$MANIFEST")
    value="$(current_hash "$url")" || value=""
  fi

  if [[ -z "$value" ]]; then
    red "  ERROR    $id — could not retrieve current state"
    errors=$((errors + 1)); continue
  fi
  checked=$((checked + 1))
  new_baseline=$(jq --arg id "$id" --arg v "$value" \
    '. + {($id): {"value": $v, "checked": (now | strftime("%Y-%m-%d"))}}' <<<"$new_baseline")

  old=$(jq -r --arg id "$id" '.[$id].value // empty' <<<"$old_baseline")
  if [[ -z "$old" ]]; then
    yellow "  NEW      $id — no baseline yet (value: ${value:0:16}…)"
    changed=$((changed + 1))
  elif [[ "$old" != "$value" ]]; then
    red "  CHANGED  $id  ($old → ${value:0:16}…)"
    red "           review: $backs"
    changed=$((changed + 1))
  else
    green "  OK       $id"
  fi
done

echo "----------------------------------------"
if [[ $UPDATE -eq 1 ]]; then
  jq . <<<"$new_baseline" > "$BASELINE"
  green "Baseline updated: $checked source(s) recorded in scripts/source-watch.baseline.json"
  exit 0
fi
if [[ $changed -gt 0 ]]; then
  red "CHANGED: $changed source(s) differ from baseline — review the listed references, then run scripts/watch-sources.sh --update"
  exit 1
fi
if [[ $errors -gt 0 ]]; then
  yellow "ERRORS: $errors source(s) unreachable, $((checked)) OK"
  exit 2
fi
green "All $checked sources unchanged"
exit 0
