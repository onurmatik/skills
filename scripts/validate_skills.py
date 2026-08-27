#!/usr/bin/env python3
"""Validate the portable structure of every public skill in this repository."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
PRIVATE_PATH_PATTERN = re.compile(r"(?:/Users/|file://|github\.com/onurmatik/menu-fit)", re.IGNORECASE)


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        raise ValueError("missing opening YAML frontmatter delimiter")

    try:
        closing = lines.index("---", 1)
    except ValueError as error:
        raise ValueError("missing closing YAML frontmatter delimiter") from error

    values: dict[str, str] = {}
    for line in lines[1:closing]:
        if not line or line.startswith((" ", "\t", "#")) or ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"\'')
    return values


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    entrypoint = skill_dir / "SKILL.md"
    if not entrypoint.is_file():
        return [f"{skill_dir}: missing SKILL.md"]

    try:
        frontmatter = parse_frontmatter(entrypoint)
    except ValueError as error:
        return [f"{entrypoint}: {error}"]

    if frontmatter.get("name") != skill_dir.name:
        errors.append(
            f"{entrypoint}: frontmatter name must equal folder name {skill_dir.name!r}"
        )
    if not frontmatter.get("description"):
        errors.append(f"{entrypoint}: missing description")

    text = entrypoint.read_text(encoding="utf-8")
    if PRIVATE_PATH_PATTERN.search(text):
        errors.append(f"{entrypoint}: contains a local or private installation source")
    for target in LINK_PATTERN.findall(text):
        if target.startswith(("http://", "https://", "#")):
            continue
        resolved = (skill_dir / target).resolve()
        if not resolved.is_relative_to(skill_dir.resolve()) or not resolved.exists():
            errors.append(f"{entrypoint}: unresolved relative link {target!r}")

    openai_yaml = skill_dir / "agents" / "openai.yaml"
    if openai_yaml.exists():
        metadata = openai_yaml.read_text(encoding="utf-8")
        if f"${skill_dir.name}" not in metadata:
            errors.append(
                f"{openai_yaml}: default prompt must mention ${skill_dir.name}"
            )

    install = skill_dir / "INSTALL.md"
    if not install.is_file():
        errors.append(f"{skill_dir}: missing INSTALL.md")
    elif PRIVATE_PATH_PATTERN.search(install.read_text(encoding="utf-8")):
        errors.append(f"{install}: contains a local or private installation source")

    return errors


def main() -> int:
    if not SKILLS_DIR.is_dir():
        print("skills directory is missing", file=sys.stderr)
        return 1

    skill_dirs = sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir())
    if not skill_dirs:
        print("no skills found", file=sys.stderr)
        return 1

    errors = [error for path in skill_dirs for error in validate_skill(path)]
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1

    print(f"Validated {len(skill_dirs)} skill(s): {', '.join(p.name for p in skill_dirs)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
