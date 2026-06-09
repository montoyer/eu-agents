#!/usr/bin/env bash
# PostToolUse hook (matcher: Skill) — when a drafting skill is invoked, injects
# the legal-basis requirement into context so the draft cannot omit it.
#
# A legislative act without an identified legal basis is void under EU law
# (CJEU C-300/89 Commission v Council — Titanium Dioxide).
#
# Input: PostToolUse JSON payload on stdin ({tool_name, tool_input, ...}).
# Output: hookSpecificOutput.additionalContext fed back to the model.

set -euo pipefail

input=$(cat)
skill=$(printf '%s' "$input" | jq -r '.tool_input.skill // empty')

case "$skill" in
  legislative-drafter|legislative-proposal|delegated-acts-drafter|lawyer-secgen) ;;
  *) exit 0 ;;
esac

jq -n '{
  hookSpecificOutput: {
    hookEventName: "PostToolUse",
    additionalContext: "[legal-basis-check hook] This skill produces legislative text. The draft MUST cite its treaty legal basis as a specific article (e.g. Article 114 TFEU, Article 17(1) TEU) in the citations and explanatory memorandum. An act without a correct legal basis is void and annullable (Art. 263 TFEU; CJEU C-300/89 Titanium Dioxide). If the legal basis cannot yet be determined, tag the draft [review — legal basis not yet determined] instead of guessing."
  }
}'
