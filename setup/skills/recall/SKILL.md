---
name: recall
description: Pick up a topic from the user's second brain (__BRAIN__). Use when the user says /recall [topic], "pick up where we left off on X", "what did we discuss about X", "what did we decide about X", "what topics do I have open", or wants to continue an earlier train of thought.
---

# Recall from second brain

Load prior context from `__BRAIN__` ($BRAIN) and continue the thread.

## Steps

1. **Sync** (best effort): `git -C $BRAIN pull --rebase` if a remote exists.
   If it fails, use the local copy.
2. **Find the note(s).**
   - Topic given: search $BRAIN/INDEX.md first, then search $BRAIN/notes/ and
     $BRAIN/inbox/ by filename and content, case-insensitively.
   - No topic: list INDEX.md entries marked `open` or `parked` and ask which.
3. **Load context.** Read the note in full, plus relevant `[[wikilinked]]`
   notes one hop out. The `project:` field says where related work lives.
4. **Brief, then continue.** Summarize current thinking, decisions already made
   (don't re-litigate them), open questions, and next steps. Then pick up the
   thread.
5. **Close the loop.** If the conversation advances the topic, offer /capture
   at a natural stopping point.

If nothing matches, say so and list the nearest INDEX.md entries. Never
fabricate prior context.
