---
name: capture
description: Save the current conversation to the user's second brain (__BRAIN__) so the topic can be picked up later in a new session. Use when the user says /capture, "capture this", "save this", "save this to my second brain", "remember where we are", or wants to keep the discussion before stopping.
---

# Capture to second brain

Distill the current conversation into a note in `__BRAIN__` ($BRAIN).
Read $BRAIN/CLAUDE.md for the note format. It wins if anything here disagrees.

## Steps

1. **Sync** (best effort): `git -C $BRAIN pull --rebase`. Skip silently if
   there is no remote. If a pull fails, proceed and mention it at the end.
2. **Identify the topic(s).** Usually one note. Split only for unrelated threads.
3. **Find or create the note.** Check $BRAIN/INDEX.md and search $BRAIN/notes/.
   If a note exists, update it in place: merge new thinking, prune superseded
   content, bump `updated`, adjust `status`. Otherwise create a new file with
   a descriptive kebab-case name.
4. **Write the distillation.** It must stand alone for a reader with no access
   to this conversation. Include specifics: names, numbers, file paths, options
   rejected and why. Do not transcribe dialogue. Set `project:` to the current
   working directory if it is not the brain itself. Add `[[wikilinks]]` to
   related notes.
5. **Update INDEX.md** in the same change. Update the existing line if any.
6. **Commit** without asking:
   `git -C $BRAIN add -A && git -C $BRAIN commit -m "capture: <topic>"`.
   Then `git -C $BRAIN push` if a remote exists. A failed push must not fail
   the capture.
7. **Report** in one or two plain sentences: the note's title, whether it was
   new or updated, and whether the backup push worked. The user may not be
   technical, so avoid git jargon.
