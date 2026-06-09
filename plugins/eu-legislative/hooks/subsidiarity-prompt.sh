#!/usr/bin/env bash
# PostToolUse hook (matcher: Skill) — when a drafting skill is invoked, injects
# a reminder that every legislative draft must carry a subsidiarity and
# proportionality check (Art. 5(3)-(4) TEU, Protocol No. 2) before it
# progresses to ISC or Commissioner clearance.
#
# Input: PostToolUse JSON payload on stdin ({tool_name, tool_input, ...}).
# Output: hookSpecificOutput.additionalContext fed back to the model.

set -euo pipefail

input=$(cat)
skill=$(printf '%s' "$input" | jq -r '.tool_input.skill // empty')

case "$skill" in
  legislative-drafter|legislative-proposal|delegated-acts-drafter) ;;
  *) exit 0 ;;
esac

jq -n '{
  hookSpecificOutput: {
    hookEventName: "PostToolUse",
    additionalContext: "[subsidiarity-prompt hook] This draft requires a subsidiarity and proportionality check (Art. 5(3)-(4) TEU, Protocol No. 2) before ISC or Commissioner clearance. Include at least a brief subsidiarity statement in the output, and end the response by reminding the user to run /subsidiarity-checker (or /lawyer-secgen) on the draft — national parliaments can raise reasoned opinions within 8 weeks of publication."
  }
}'
