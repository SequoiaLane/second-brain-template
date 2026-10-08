#!/usr/bin/env python3
"""Install this second brain into the user's Claude Code setup.

Copies the /capture and /recall skills and the SessionStart pointer hook into
the user's Claude folder, with this repo's path filled in. Then merges the hook
and permission rules into the user's settings.json.

Safe to re-run: unchanged files are left alone, changed files are backed up
to <file>.bak before being replaced, and settings entries are never duplicated.

Usage:
    python3 setup/install.py --dry-run   # show what would change
    python3 setup/install.py             # apply
"""

import argparse
import json
import os
import shlex
import shutil
import stat
import sys
from pathlib import Path

PLACEHOLDER = "__BRAIN__"
HOOK_NAME = "second-brain-pointer.sh"


def render(src: Path, brain: Path) -> str:
    return src.read_text().replace(PLACEHOLDER, str(brain))


def plan_file(dest: Path, content: str) -> str:
    if not dest.exists():
        return "create"
    if dest.read_text() == content:
        return "unchanged"
    return "replace"


def write_file(dest: Path, content: str, executable: bool = False) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists():
        shutil.copy2(dest, dest.with_name(dest.name + ".bak"))
    dest.write_text(content)
    if executable:
        dest.chmod(dest.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)


def merge_settings(settings: dict, hook_cmd: str, brain: Path) -> list:
    """Mutate settings in place. Return a list of human-readable changes."""
    changes = []

    hooks = settings.setdefault("hooks", {})
    session_start = hooks.setdefault("SessionStart", [])
    registered = any(
        h.get("command") == hook_cmd
        for group in session_start
        for h in group.get("hooks", [])
    )
    if not registered:
        session_start.append(
            {"matcher": "*", "hooks": [{"type": "command", "command": hook_cmd}]}
        )
        changes.append("register the SessionStart hook")

    # Leading // marks an absolute path in permission rules.
    abs_rule = "/" + str(brain) + "/**"
    wanted = [
        f"Bash(git -C {brain} *)",
        f"Read({abs_rule})",
        f"Edit({abs_rule})",
        f"Write({abs_rule})",
    ]
    allow = settings.setdefault("permissions", {}).setdefault("allow", [])
    for rule in wanted:
        if rule not in allow:
            allow.append(rule)
            changes.append(f"allow {rule}")

    return changes


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument(
        "--claude-dir",
        default=os.environ.get("CLAUDE_CONFIG_DIR", str(Path.home() / ".claude")),
    )
    args = parser.parse_args()

    setup_dir = Path(__file__).resolve().parent
    brain = setup_dir.parent
    claude = Path(args.claude_dir).expanduser()

    if not (brain / "INDEX.md").exists():
        print(f"error: {brain} does not look like a second brain (no INDEX.md)")
        return 1

    hook_dest = claude / "hooks" / HOOK_NAME
    files = [
        (setup_dir / "skills/capture/SKILL.md", claude / "skills/capture/SKILL.md", False),
        (setup_dir / "skills/recall/SKILL.md", claude / "skills/recall/SKILL.md", False),
        (setup_dir / "hooks" / HOOK_NAME, hook_dest, True),
    ]

    settings_path = claude / "settings.json"
    if settings_path.exists():
        try:
            settings = json.loads(settings_path.read_text() or "{}")
        except json.JSONDecodeError as e:
            print(f"error: {settings_path} is not valid JSON ({e}). Fix it and re-run.")
            return 1
    else:
        settings = {}

    print(f"Second brain: {brain}")
    print(f"Claude folder: {claude}\n")

    for src, dest, executable in files:
        content = render(src, brain)
        action = plan_file(dest, content)
        print(f"  {action:9} {dest}")
        if action == "replace":
            print(f"            (existing file differs; backup goes to {dest.name}.bak)")
        if not args.dry_run and action != "unchanged":
            write_file(dest, content, executable)

    changes = merge_settings(settings, shlex.quote(str(hook_dest)), brain)
    if changes:
        print(f"  update    {settings_path}")
        for c in changes:
            print(f"            - {c}")
        if not args.dry_run:
            write_file(settings_path, json.dumps(settings, indent=2) + "\n")
    else:
        print(f"  unchanged {settings_path}")

    print("\nDry run: nothing was changed." if args.dry_run else "\nDone.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
