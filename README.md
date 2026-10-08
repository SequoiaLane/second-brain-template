# Second Brain for Claude

**A second brain lets you close a Claude session and pick the topic up later.** Claude saves where your thinking stands into a note. In a new session, Claude finds that note on its own and continues.

Setup takes about five minutes. Claude does the work.

## Why use it

**Many people keep a Claude session open for days on one topic.** The context lives only in that session. Closing it means explaining everything again.

The second brain saves that context to a note. Your routine becomes:

1. **Work** on a topic with Claude.
2. **Say "capture this"** when you reach a stopping point.
3. **Close** the session.
4. **Come back later** in a new session and mention the topic. Claude reads your notes and continues.

**What you get:**

- **Fewer open sessions.** You no longer keep windows open to hold onto context.
- **Better starts.** A new session begins from a short summary instead of pages of old back-and-forth.
- **Notes that last.** They survive restarts and computer changes, and you can read them yourself.
- **Connected topics.** Notes link to each other, so Claude can trace a decision back to where it started.

## Set it up

**You need Claude Code.** That is the Code tab in the Claude desktop app, or the `claude` command in a terminal. This works on Mac and Linux.

**1. Start a new Claude Code session.** Any folder is fine.

**2. Paste this message:**

```
Set up a second brain for me from https://github.com/SequoiaLane/second-brain-template by following the instructions in its setup/SETUP.md file.
```

**3. Approve what Claude asks to do.** Claude downloads the template and installs two commands. It also tells future sessions where your notes live. It may offer a private backup on GitHub, which is optional.

**4. Start a new session when Claude says it is done.** The setup takes effect in new sessions.

## Use it

| You want to | Do this |
|---|---|
| **Save a topic** | Say "capture this" or type `/capture` |
| **Continue a topic** | Mention it in a new session, such as "let's keep going on the kitchen budget" |
| **See your open topics** | Type `/recall` |
| **Update a topic** | Capture again. Claude updates the same note. |
| **Read your notes** | Open your `second-brain` folder. Each topic is a text file in `notes/`. |

**You will rarely need `/recall`.** Each new session knows the second brain exists. When you mention a topic with notes behind it, Claude reads them without being asked.

**Tip: capture at natural stopping points.** Good moments are the end of a planning discussion, before switching tasks, or before closing for the day.

## Optional: browse in Obsidian

[Obsidian](https://obsidian.md) is a free notes app. Open your `second-brain` folder as a vault to browse notes and see how topics link together. Nothing depends on it.

## Where it works

**It works in Claude Code on the computer where you set it up.** That includes the desktop app's Code tab and the terminal, in any folder.

**It does not work in regular Claude chat, Cowork, or cloud sessions yet.** Those cannot reach the notes on your computer. See [how it works](docs/how-it-works.md) for workarounds.

## Common questions

**Is my data private?** Notes stay on your computer. If you chose a GitHub backup, it is a private repository only you can see.

**Can I use it on two computers?** Yes, if you set up the GitHub backup. On the second computer, ask Claude: "Clone my second-brain repo from GitHub into ~/second-brain and run its setup."

**Something stopped working.** Start Claude Code in your `second-brain` folder and type `/brain-setup`. It repairs the installation.

**How do I remove it?** Ask Claude: "Remove the second brain skills and hook from my Claude Code settings." Your notes folder stays until you delete it.
