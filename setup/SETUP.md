# Setup instructions for Claude

These instructions are for Claude. The user asked Claude to set up their second brain from this template.

**Assume the user is not technical.** Do the work yourself. Ask only the questions listed below. Explain results in plain words, without git or file-system jargon. Keep updates to one or two sentences.

Supported on macOS and Linux. On Windows, tell the user this template is untested there and stop unless they want to try anyway.

## 1. Put the brain in its home folder

**The default home is `~/second-brain`.** Moving it later breaks the setup, so settle it now.

- **If you are already inside a clone of this template**, and it is somewhere stable such as the home folder or Documents, use it where it is.
- **If it sits somewhere temporary**, such as Downloads or a temp folder, move or re-clone it to `~/second-brain`.
- **If the user has not cloned it yet**, clone it:

  ```bash
  git clone --depth 1 https://github.com/SequoiaLane/second-brain-template ~/second-brain
  ```

- **If `~/second-brain` already exists and is not empty**, ask the user whether to use another folder name.

**The commands below use `~/second-brain`.** Substitute the real folder if it differs.

**If git is missing on macOS**, running `git` opens a system prompt to install developer tools. Tell the user to click Install, wait for it to finish, then say "continue".

## 2. Detach it from the template

**The brain must start its own history.** Otherwise captures would try to send the user's notes to the template's repository.

Check the remote:

```bash
git -C ~/second-brain remote get-url origin
```

If it points at the template, start fresh:

```bash
cd ~/second-brain && rm -rf .git && git init -q
```

If git has no name or email configured, set them for this folder only:

```bash
git -C ~/second-brain config user.name "$(id -F 2>/dev/null || whoami)"
```

```bash
git -C ~/second-brain config user.email "$(whoami)@localhost"
```

Then make the first commit:

```bash
git -C ~/second-brain add -A && git -C ~/second-brain commit -qm "Start my second brain"
```

## 3. Install into Claude Code

**Preview first.**

```bash
python3 ~/second-brain/setup/install.py --dry-run
```

- **If any line says `replace`**, the user already has a skill or hook with that name. Tell them in plain words and ask before continuing. The installer keeps a `.bak` backup of anything it replaces.
- **Otherwise continue without asking.** The user already asked for setup.

Apply:

```bash
python3 ~/second-brain/setup/install.py
```

Tell the user in one sentence what was added: two commands for saving and resuming topics, and a note that lets each new Claude session know the brain exists.

## 4. Check it works

Run the installed hook. It should print text starting with "Second brain:".

```bash
bash ~/.claude/hooks/second-brain-pointer.sh
```

Confirm the settings file is still valid:

```bash
python3 -m json.tool ~/.claude/settings.json > /dev/null && echo ok
```

If either check fails, fix it before going on.

## 5. Offer a backup

**A backup is optional.** Without one, the notes live only on this computer.

Check whether the GitHub command-line tool is installed and signed in:

```bash
gh auth status
```

- **If it is signed in**, ask: "Do you want a private online backup on GitHub? Your notes stay private." On yes:

  ```bash
  cd ~/second-brain && gh repo create second-brain --private --source . --push
  ```

  If the name is taken, ask for another. Always use `--private`.

- **If not**, tell the user the brain works fine without a backup. They can ask Claude later to "back up my second brain to GitHub".

Do not install new tools without asking.

## 6. Hand off

Tell the user, in plain words:

- **Setup is done.** It takes effect in new sessions, so they should start a new one.
- **Saving a topic:** say "capture this" or type `/capture` when they reach a stopping point.
- **Coming back:** start a new session and mention the topic. Claude finds the notes on its own.
- **Seeing open topics:** type `/recall`.
- **Optional:** the folder opens as a vault in Obsidian, a free notes app, for browsing notes.

Then stop. Do not capture this setup conversation.
