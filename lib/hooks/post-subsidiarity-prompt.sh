#!/usr/bin/env bash
# Post-output hook: prompts the user to run a subsidiarity check after any
# legislative draft is produced.
#
# Triggered after the legislative-drafter skill produces a new draft act.
# Subsidiarity (Art. 5(3) TEU) and proportionality (Art. 5(4) TEU) are
# mandatory tests for all EU legislative acts under Protocol No. 2.
# The hook reminds the user to run the check before the draft progresses.
#
# Claude Code hook event: PostToolUse
# Applies to: eu-legislative domain package

input=$(cat)

SUBSIDIARITY_PROMPT="
---
SUBSIDIARITY CHECK REMINDER (Art. 5(3) TEU + Protocol No. 2)

This legislative draft has not yet been checked for subsidiarity and proportionality.
Before this draft proceeds to ISC or Commissioner clearance:

1. Run: /lawyer-secgen  subsidiarity and proportionality check on this draft
   — or —
2. Run: /impact-assessment-analyst  and ensure the IA includes the subsidiarity test

The Commission's obligation to justify EU action under subsidiarity applies to
every legislative initiative. The European Parliament and national parliaments
can raise subsidiarity objections (reasoned opinions) within 8 weeks of publication.

Add [subsidiarity check completed — see IA/SWD YYYY/NNN] once the check is done.
---
"

printf '%s\n%s\n' "$input" "$SUBSIDIARITY_PROMPT"
