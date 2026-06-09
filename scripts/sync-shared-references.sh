#!/usr/bin/env bash
#
# sync-shared-references.sh — single-source maintenance for reference files
# needed by more than one plugin.
#
# Plugins install via git-subdir, so each consuming plugin must physically
# contain its own copy (symlinks dangle, see TODO.md). To keep that
# maintainable, every shared file has exactly ONE canonical location; this
# script regenerates the consumer copies from it, stamping each copy with a
# DO-NOT-EDIT header. scripts/validate.sh runs '--check' and fails the build
# if a copy has drifted from its canonical.
#
# Usage:  scripts/sync-shared-references.sh           # regenerate all copies
#         scripts/sync-shared-references.sh --check   # verify only, exit 1 on drift
#
# To share a new reference: add a "canonical|copy" line to SHARED below and run
# this script. Edit only the canonical file, never the copy.
set -uo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

# canonical|consumer-copy  (paths relative to repo root)
SHARED=(
  "plugins/eu-institutional-management/references/staff-regulations-annex-i-2026.md|plugins/eu-careers/references/staff-regulations-annex-i-2026.md"
)

CHECK=0
[[ "${1:-}" == "--check" ]] && CHECK=1

status=0
for pair in "${SHARED[@]}"; do
  canonical="${pair%%|*}"
  copy="${pair##*|}"

  if [[ ! -f "$canonical" ]]; then
    echo "ERROR: canonical file missing: $canonical" >&2
    status=1
    continue
  fi

  header="<!-- SYNCED COPY — do not edit. Canonical: $canonical — edit there, then run scripts/sync-shared-references.sh -->"

  if [[ $CHECK -eq 1 ]]; then
    if [[ ! -f "$copy" ]]; then
      echo "DRIFT: $copy missing (run scripts/sync-shared-references.sh)" >&2
      status=1
    elif ! diff -q <(tail -n +3 "$copy") "$canonical" >/dev/null 2>&1; then
      echo "DRIFT: $copy differs from $canonical (run scripts/sync-shared-references.sh)" >&2
      status=1
    fi
  else
    { printf '%s\n\n' "$header"; cat "$canonical"; } > "$copy"
    echo "synced $copy"
  fi
done

exit $status
