#!/usr/bin/env bash
# Pre-output hook: warns if a legislative draft output contains no Treaty article citation.
#
# Triggered before finalising any output from legislative-drafter or lawyer-secgen.
# A legislative act without an identified legal basis is void under EU law
# (CJEU C-300/89 Commission v Council — Titanium Dioxide).
#
# Claude Code hook event: PreToolUse
# Applies to: eu-legislative domain package

input=$(cat)

# Check for presence of a TFEU or TEU article reference.
# Acceptable patterns: "Article 114 TFEU", "Art. 114 TFEU", "Article 114(1) TFEU",
# "Article 17 TEU", "Art. 17(1) TEU"
if echo "$input" | grep -qiE "(article|art\.)\s+[0-9]+([\(][0-9]+[\)])?\s+(TFEU|TEU)"; then
  # Legal basis found — pass through
  echo "$input"
  exit 0
else
  # No legal basis detected — prepend a warning
  WARNING="[pre-legal-basis-check] WARNING: No Treaty article (TFEU/TEU) detected in this
legislative draft. All legislative acts must cite their legal basis before adoption.
Failure to identify the correct legal basis is a ground for annulment (Art. 263 TFEU).
Add the legal basis now or tag the draft [review — legal basis not yet determined].

---
"
  printf '%s\n%s\n' "$WARNING" "$input"
  exit 0
fi
