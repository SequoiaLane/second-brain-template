# How it works

This page is for people who want to understand or customize the setup. You do not need it to use the second brain.

## The pieces

**Two skills and one hook do all the work.** The installer copies them into your user-level Claude folder, `~/.claude`, with your brain's path filled in.

| Piece | Installed to | What it does |
|---|---|---|
| **`/capture` skill** | `~/.claude/skills/capture/` | Distills the conversation into a note, updates INDEX.md, commits, and pushes. |
| **`/recall` skill** | `~/.claude/skills/recall/` | Finds a note, briefs you, and continues the topic. |
| **SessionStart hook** | `~/.claude/hooks/second-brain-pointer.sh` | Tells each new session where the brain is and when to read it. |
| **Settings entries** | `~/.claude/settings.json` | Register the hook and allow git, read, and write in the brain folder without prompts. |

The sources live in this repo:

```
setup/skills/capture/SKILL.md
setup/skills/recall/SKILL.md
setup/hooks/second-brain-pointer.sh
setup/install.py
```

**The installer is safe to re-run.** It skips files that already match, backs up changed files to `.bak`, and never adds duplicate settings entries.

## Why skills work everywhere

**A skill in `~/.claude/skills/` becomes a slash command in all projects.** The folder name is the command name.

**The skill's `description` also triggers it without the slash.** Claude Code loads all skill descriptions at session start. Phrases listed there, such as "capture this", invoke the skill from normal conversation.

**Do not add `context: fork` to the capture skill.** A forked skill runs without the conversation history. The conversation is what capture saves.

## Why the hook matters

**The hook is the only piece that runs in each session without being asked.** Its text tells Claude what the brain is and when to read it. Edit the text in the installed hook to change how sessions use the brain.

**It injects a short pointer to the index.** The index grows with each note. Loading it into all sessions would fill unrelated sessions with off-topic text. A fixed pointer stays small, and Claude reads the index when a topic needs it.

**Its matcher is `*`.** SessionStart fires on startup, resume, `/clear`, and compaction. The wildcard re-injects the pointer after each one.

**It uses a fixed path to the brain.** Hook examples in the docs often use `${CLAUDE_PROJECT_DIR}`. That variable points at the current project, so the hook would only work inside the brain folder.

**It stays silent when the brain is missing.** A settings file synced to another machine does no harm.

**Hooks load when a session starts.** Run `/hooks` in a new session to confirm it is listed.

## Where it works

| Surface | Works? | Why |
|---|---|---|
| **Claude Code on your machine** | Yes | The CLI, desktop Code tab, and IDE extensions all read `~/.claude`. |
| **Claude Code cloud sessions** | No | Cloud sessions do not read your user-level skills or settings. |
| **Cowork** | No, as built | Cowork does not read the CLI's `~/.claude` folder. |
| **claude.ai chat** | No | Chat has no access to your files or git. |

**Cowork can use the brain with extra setup.**

- **Grant the folder.** Attach the brain folder to a Cowork project.
- **Add the instruction.** Paste the hook's text into the project's instructions.
- **Install the skills.** Upload the two skills under Customize, or package them as a plugin. Plugins use the same layout as Claude Code plugins.
- **Unconfirmed: git and hooks.** Docs do not say whether Cowork can run git or push. Docs also do not say whether a plugin's SessionStart output reaches Cowork. Test both before relying on them.

**claude.ai chat has two partial options.**

- **Read only.** Sync the brain's GitHub repo into a claude.ai Project. The sync is a manual snapshot, and chat cannot write back.
- **Read and write.** Run a small MCP server with search, read, and capture tools. Add it as a custom connector.

**Cloud sessions load skills from the repo they clone.** Skills under the repo's `.claude/skills/` folder load there. This only helps when a cloud session runs inside the brain repo.

## How this differs from Claude's built-in memory

**Claude Code's auto-memory and the second brain store different things.** They work well together.

| | Auto-memory | Second brain |
|---|---|---|
| **Holds** | Preferences, corrections, facts about you | The state of thinking on a topic |
| **Written** | Automatically, in small facts | On `/capture`, as a full note |
| **Scope** | Usually one project | All projects |
| **Format** | Short entries in Claude's config folder | Your own folder, readable in Obsidian |

A rule like "always run tests before committing" belongs in memory. A half-finished plan for a pricing model belongs in the brain.

## Manual setup

**Use this if you would rather not let Claude run the installer.**

1. Clone this template to a stable folder, such as `~/second-brain`.
2. Delete its `.git` folder, run `git init`, and commit.
3. Copy the two skill folders from `setup/skills/` into `~/.claude/skills/`.
4. Copy the hook from `setup/hooks/` into `~/.claude/hooks/` and make it executable.
5. Replace `__BRAIN__` in all three copied files with the brain's absolute path.
6. Add the hook to `~/.claude/settings.json`:

   ```json
   {
     "hooks": {
       "SessionStart": [
         {
           "matcher": "*",
           "hooks": [
             { "type": "command", "command": "/Users/you/.claude/hooks/second-brain-pointer.sh" }
           ]
         }
       ]
     }
   }
   ```

7. Optionally, add allow rules so capture runs without prompts. The leading `//` marks an absolute path.

   ```json
   {
     "permissions": {
       "allow": [
         "Bash(git -C /Users/you/second-brain *)",
         "Read(//Users/you/second-brain/**)",
         "Edit(//Users/you/second-brain/**)",
         "Write(//Users/you/second-brain/**)"
       ]
     }
   }
   ```

8. Start a new session and run `/hooks` to confirm.

## Customizing

- **Note format and rules.** Edit `CLAUDE.md` in the brain folder. The skills defer to it.
- **When sessions read the brain.** Edit the text in the installed hook.
- **Capture quality.** Add `model:` and `effort: high` to the capture skill's frontmatter. The override applies only to the capture turn. Leave recall on the session's model, since it hands off to work you chose that model for.

## Design choices

- **Git for storage.** Notes are plain files with full history, and they work with any tool.
- **One note per topic.** Updating in place keeps a single current answer per topic.
- **No asking before commit.** Prompts on each save would discourage saving.
- **Best-effort sync.** A failed push never loses a capture. The next push carries it.
- **No database or search index.** Plain-text search scales to hundreds of notes.
