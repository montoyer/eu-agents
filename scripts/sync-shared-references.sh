#!/usr/bin/env bash
#
# sync-shared-references.sh — single-source maintenance for files needed by
# more than one plugin, or by a plugin and the repo root.
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
# To share a new file: add a "canonical|copy" line to SHARED below. To share a
# whole folder: add a "canonical-dir|copy-dir" line to SHARED_DIRS. Then run
# this script. Edit only the canonical, never the copy.
set -uo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

# canonical|consumer-copy  (paths relative to repo root)
SHARED=(
  "plugins/eu-institutional-management/references/staff-regulations-annex-i-2026.md|plugins/eu-careers/references/staff-regulations-annex-i-2026.md"
  "plugins/eu-legislative/references/eu-charter.md|plugins/eu-competition/references/eu-charter.md"
  "plugins/eu-legislative/references/tfeu-teu-consolidated.md|plugins/eu-competition/references/tfeu-teu-consolidated.md"
  "plugins/eu-legislative/references/tfeu-teu-consolidated.md|plugins/eu-grants-enforcement/references/tfeu-teu-consolidated.md"
)

# canonical-dir|consumer-dir  (every *.md and *.yml is mirrored except files
# whose name starts with "_", such as templates; copies with no canonical are
# removed)
SHARED_DIRS=(
  "knowledge|plugins/eu-simulation/knowledge"
)

CHECK=0
[[ "${1:-}" == "--check" ]] && CHECK=1

status=0

sync_one() {
  local canonical="$1" copy="$2"

  if [[ ! -f "$canonical" ]]; then
    echo "ERROR: canonical file missing: $canonical" >&2
    status=1
    return
  fi

  local note="SYNCED COPY — do not edit. Canonical: $canonical — edit there, then run scripts/sync-shared-references.sh"
  local header="<!-- $note -->"
  [[ "$canonical" == *.yml ]] && header="# $note"

  if [[ $CHECK -eq 1 ]]; then
    if [[ ! -f "$copy" ]]; then
      echo "DRIFT: $copy missing (run scripts/sync-shared-references.sh)" >&2
      status=1
    elif ! diff -q <(tail -n +3 "$copy") "$canonical" >/dev/null 2>&1; then
      echo "DRIFT: $copy differs from $canonical (run scripts/sync-shared-references.sh)" >&2
      status=1
    fi
  else
    mkdir -p "$(dirname "$copy")"
    { printf '%s\n\n' "$header"; cat "$canonical"; } > "$copy"
    echo "synced $copy"
  fi
}

for pair in "${SHARED[@]}"; do
  sync_one "${pair%%|*}" "${pair##*|}"
done

for pair in "${SHARED_DIRS[@]}"; do
  src="${pair%%|*}"
  dst="${pair##*|}"

  if [[ ! -d "$src" ]]; then
    echo "ERROR: canonical folder missing: $src" >&2
    status=1
    continue
  fi

  while IFS= read -r canonical; do
    sync_one "$canonical" "$dst/${canonical#"$src"/}"
  done < <(find "$src" -type f \( -name '*.md' -o -name '*.yml' \) ! -name '_*' | sort)

  # Copies whose canonical was deleted or renamed
  [[ -d "$dst" ]] || continue
  while IFS= read -r copy; do
    canonical="$src/${copy#"$dst"/}"
    if [[ ! -f "$canonical" || "$(basename "$canonical")" == _* ]]; then
      if [[ $CHECK -eq 1 ]]; then
        echo "DRIFT: $copy has no canonical in $src (run scripts/sync-shared-references.sh)" >&2
        status=1
      else
        rm "$copy"
        echo "removed $copy"
      fi
    fi
  done < <(find "$dst" -type f | sort)
done

exit $status
