# Second Brain

This folder is the user's second brain: distilled notes from conversations with Claude, so any topic can be picked up later without starting over.

It is also an Obsidian vault. Everything here must remain plain markdown.

## Structure

```
INDEX.md    # the map: one line per note, always current
notes/      # one file per topic
inbox/      # quick, unorganized captures awaiting promotion to notes/
setup/      # installer files, not notes
```

## Note format

Filenames are descriptive kebab-case, such as `kitchen-remodel-budget.md`. Never date-based names like `note-2026-08-06.md`.

```markdown
---
status: open        # open | parked | resolved
created: 2026-08-06
updated: 2026-08-06
project: /path/to/folder   # optional: where the conversation happened
tags: []
---

# Title

## Context
Why this topic exists.

## Current thinking
Where the reasoning stands now. Written for a reader with no access to the
original conversation. Include names, numbers, links, and trade-offs.

## Decisions
- What was decided, with brief rationale.

## Open questions
- What remains unresolved.

## Next steps
- [ ] Concrete actions.

## Related
- [[other-note]]
```

Leave out empty sections rather than writing placeholders.

## Conventions

- **Distill, don't transcribe.** A good note lets a fresh session resume in one read.
- **One note per topic, updated over time.** Search INDEX.md and notes/ before creating a new file.
- **Wikilinks** (`[[note-name]]`) connect related notes. Link liberally.
- **INDEX.md** is updated in the same commit as any note change. Format: `- [Title](notes/file.md) — one-line hook (status)`.
- **No plugin dependencies.** Obsidian plugins must never be required to read a note.

## Saving

Never ask before committing here. Saving should take no effort.

- Before reading: `git pull --rebase` if a remote exists (best effort).
- After any note change: commit with a short message naming the topic, then `git push` if a remote exists. A failed push must not fail the save.
