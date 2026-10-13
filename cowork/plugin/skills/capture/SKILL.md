---
name: capture
description: Save the current conversation to the user's second brain folder so the topic can be picked up later. Use when the user says /capture, "capture this", "save this", "save this to my second brain", "remember where we are", or wants to keep the discussion before stopping.
---

# Capture to second brain (Cowork)

## Find the brain

The second brain is a folder attached to this project. It contains `INDEX.md`,
`CLAUDE.md`, and a `notes/` folder. Find it among the folders you can access
and call it $BRAIN. Its path here may differ from its path on the user's Mac.
That is expected.

If no such folder is attached, tell the user in plain words: "Your second
brain folder isn't attached to this project. Add the second-brain folder to
the project, then ask me again." Then stop.

Read $BRAIN/CLAUDE.md for the note format. It wins if anything here disagrees.

## Steps

1. **Identify the topic(s).** Usually one note. Split only for unrelated threads.
2. **Find or create the note.** Check $BRAIN/INDEX.md and search $BRAIN/notes/.
   If a note exists, update it in place: merge new thinking, prune superseded
   content, bump `updated`, adjust `status`. Otherwise create a new file with
   a descriptive kebab-case name.
3. **Write the distillation.** It must stand alone for a reader with no access
   to this conversation. Include specifics: names, numbers, links, options
   rejected and why. Do not transcribe dialogue. Add `[[wikilinks]]` to
   related notes.
4. **Update INDEX.md** in the same change. Update the existing line if any.
5. **Commit if you can** (best effort):
   `git -C $BRAIN add -A && git -C $BRAIN commit -m "capture: <topic>"`.
   Do not push. If git is missing or fails, leave the files as written. The
   next capture from Claude Code on the user's computer commits and backs
   them up. Never let a git problem fail the capture.
6. **Report** in one or two plain sentences: the note's title and whether it
   was new or updated. Avoid git jargon.
