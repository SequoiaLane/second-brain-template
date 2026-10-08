#!/bin/bash
# SessionStart hook: tell Claude the second brain exists, without loading it.
# Its output is added to the start of each Claude Code session.
# Edit the text below to change how sessions use the brain.

BRAIN="__BRAIN__"

# Stay silent if the brain isn't on this machine.
[ -f "$BRAIN/INDEX.md" ] || exit 0

cat <<EOF
Second brain: $BRAIN holds distilled notes from the user's past Claude
conversations: decisions, open threads, and reasoning worth resuming.
INDEX.md there lists each topic on one line. Full notes live in notes/.

Read $BRAIN/INDEX.md when the current work may already have prior thinking
behind it, or when the user refers to an earlier discussion. Don't read it for
tasks that clearly stand alone. The /recall skill does this lookup properly,
and /capture saves new thinking back. When a conversation reaches a natural
stopping point on a topic worth keeping, offer /capture.
EOF
