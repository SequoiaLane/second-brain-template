---
name: recall
description: Pick up a topic from the user's second brain folder. Use when the user says /recall [topic], "pick up where we left off on X", "what did we discuss about X", "what did we decide about X", "what topics do I have open", or wants to continue an earlier train of thought.
---

# Recall from second brain (Cowork)

## Find the brain

The second brain is a folder attached to this project. It contains `INDEX.md`,
`CLAUDE.md`, and a `notes/` folder. Find it among the folders you can access
and call it $BRAIN.

If no such folder is attached, tell the user in plain words: "Your second
brain folder isn't attached to this project. Add the second-brain folder to
the project, then ask me again." Then stop.

## Steps

1. **Find the note(s).**
   - Topic given: search $BRAIN/INDEX.md first, then search $BRAIN/notes/ and
     $BRAIN/inbox/ by filename and content, case-insensitively.
   - No topic: list INDEX.md entries marked `open` or `parked` and ask which.
2. **Load context.** Read the note in full, plus relevant `[[wikilinked]]`
   notes one hop out.
3. **Brief, then continue.** Summarize current thinking, decisions already made
   (don't re-litigate them), open questions, and next steps. Then pick up the
   thread.
4. **Close the loop.** If the conversation advances the topic, offer to
   capture it at a natural stopping point.

If nothing matches, say so and list the nearest INDEX.md entries. Never
fabricate prior context.
