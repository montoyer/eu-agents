#!/usr/bin/env bash
#
# validate.sh — structural integrity checks for the agents-for-EU repository.
#
# Hard checks (exit 1 on failure):
#   1. Every skill registered in a plugin.json points to a SKILL.md that exists.
#   2. Every SKILL.md contains a DRAFT disclaimer.
#   4. Every command declared in a plugin's hooks/hooks.json resolves to an
#      existing executable file (after ${CLAUDE_PLUGIN_ROOT} substitution).
#   5a. No symlink under plugins/ is dangling.
#
# Soft checks (reported as warnings, do not fail the build):
#   3. Every `references/<file>.md` cited inside a SKILL.md exists in that
#      plugin's references/ directory. (Many legacy citations point to files
#      that were never created; these are surfaced but not fatal.)
#   5b. No symlink under plugins/ resolves outside its own plugin directory.
#      (Such links work in a full clone but dangle when the plugin is
#      installed via a git-subdir marketplace source, which fetches only the
#      plugin's subtree.)
#
# Usage:  scripts/validate.sh            # full repo
#         scripts/validate.sh --strict   # promote soft checks to hard failures
#
set -uo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

STRICT=0
[[ "${1:-}" == "--strict" ]] && STRICT=1

errors=0
warnings=0

red()    { printf '\033[31m%s\033[0m\n' "$1"; }
green()  { printf '\033[32m%s\033[0m\n' "$1"; }
yellow() { printf '\033[33m%s\033[0m\n' "$1"; }

# ---------------------------------------------------------------------------
# Check 1 — every registered skill path exists
# ---------------------------------------------------------------------------
echo "==> Check 1: registered skill paths exist"
for manifest in plugins/*/.claude-plugin/plugin.json; do
  plugin_dir="$(dirname "$(dirname "$manifest")")"
  # extract each skill's "path" value
  while IFS= read -r relpath; do
    [[ -z "$relpath" ]] && continue
    if [[ ! -f "$plugin_dir/$relpath" ]]; then
      red "  MISSING: $manifest declares skill path '$relpath' → $plugin_dir/$relpath not found"
      errors=$((errors + 1))
    fi
  done < <(jq -r '.skills[]?.path // empty' "$manifest" 2>/dev/null)
done

# ---------------------------------------------------------------------------
# Check 2 — every SKILL.md carries a DRAFT disclaimer
# ---------------------------------------------------------------------------
echo "==> Check 2: SKILL.md files carry a DRAFT disclaimer"
while IFS= read -r skill; do
  if ! grep -qiE '\bDRAFT\b' "$skill"; then
    red "  NO DISCLAIMER: $skill has no 'DRAFT' disclaimer"
    errors=$((errors + 1))
  fi
done < <(find plugins -name 'SKILL.md' -type f)

# ---------------------------------------------------------------------------
# Check 3 — cited references/<file>.md exist (soft by default)
# ---------------------------------------------------------------------------
echo "==> Check 3: cited reference files exist (soft)"
while IFS= read -r skill; do
  plugin_dir="$(echo "$skill" | sed -E 's#(plugins/[^/]+)/.*#\1#')"
  # pull every `references/<name>.md` token mentioned in the SKILL
  while IFS= read -r ref; do
    [[ -z "$ref" ]] && continue
    if [[ ! -f "$plugin_dir/$ref" ]]; then
      yellow "  cited-but-missing: $skill → $plugin_dir/$ref"
      warnings=$((warnings + 1))
      [[ $STRICT -eq 1 ]] && errors=$((errors + 1))
    fi
  done < <(grep -ohoE 'references/[A-Za-z0-9._-]+\.md' "$skill" | sort -u)
done < <(find plugins -name 'SKILL.md' -type f)

# ---------------------------------------------------------------------------
# Check 4 — every hook command in hooks/hooks.json exists and is executable
# ---------------------------------------------------------------------------
echo "==> Check 4: declared hook commands exist"
for hooksfile in plugins/*/hooks/hooks.json; do
  [[ -f "$hooksfile" ]] || continue
  plugin_dir="$(dirname "$(dirname "$hooksfile")")"
  while IFS= read -r cmd; do
    [[ -z "$cmd" ]] && continue
    # resolve ${CLAUDE_PLUGIN_ROOT} to the plugin directory, strip quoting
    resolved="${cmd//\$\{CLAUDE_PLUGIN_ROOT\}/$plugin_dir}"
    resolved="${resolved//\"/}"
    # take the command path only (before any arguments)
    resolved="${resolved%% *}"
    if [[ ! -f "$resolved" ]]; then
      red "  MISSING: $hooksfile declares command '$cmd' → $resolved not found"
      errors=$((errors + 1))
    elif [[ ! -x "$resolved" ]]; then
      red "  NOT EXECUTABLE: $resolved (chmod +x needed)"
      errors=$((errors + 1))
    fi
  done < <(jq -r '.hooks // {} | .[]?[]?.hooks[]?.command // empty' "$hooksfile" 2>/dev/null)
done

# ---------------------------------------------------------------------------
# Check 5 — plugin symlinks resolve and stay inside their plugin
# ---------------------------------------------------------------------------
echo "==> Check 5: plugin symlinks resolve (hard) and do not escape their plugin root (soft)"
while IFS= read -r link; do
  plugin_root="$ROOT/$(echo "$link" | cut -d/ -f1-2)"
  target="$(readlink "$link")"
  if [[ ! -e "$link" ]]; then
    red "  DANGLING: $link → $target"
    errors=$((errors + 1))
    continue
  fi
  if [[ "$target" == /* ]]; then
    abs="$target"
  else
    abs="$(dirname "$link")/$target"
  fi
  resolved="$(cd "$(dirname "$abs")" && pwd -P)/$(basename "$abs")"
  if [[ "$resolved" != "$plugin_root/"* ]]; then
    yellow "  escapes-plugin: $link → $target (dangles when installed via git-subdir)"
    warnings=$((warnings + 1))
    [[ $STRICT -eq 1 ]] && errors=$((errors + 1))
  fi
done < <(find plugins -type l)

# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------
echo
echo "----------------------------------------"
if [[ $errors -gt 0 ]]; then
  red "FAILED: $errors error(s), $warnings warning(s)"
  exit 1
fi
if [[ $warnings -gt 0 ]]; then
  yellow "PASSED with $warnings warning(s)"
else
  green "PASSED: all checks clean"
fi
exit 0
