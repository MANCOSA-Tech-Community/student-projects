#!/usr/bin/env python3
"""Validate every project folder in the repository.

Run by CI on each pull request, and locally by contributors before pushing:

    python scripts/validate_projects.py

Checks, for every folder under ``projects/`` (the ``_template`` folder is checked
for structure and schema but exempt from the naming and identity checks):

  1. Folder name matches ``<github-username>--<slug>`` (lowercase, hyphenated).
  2. Both ``README.md`` and ``project.json`` are present.
  3. ``project.json`` parses and validates against ``schema/project.schema.json``.
  4. ``project.json``'s ``github`` equals the folder's username prefix.
  5. No file under ``projects/`` exceeds the size cap (5 MB).

Exits 0 if everything passes, 1 otherwise. Every failure is printed with the
offending path so contributors can fix it without guessing.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

try:
    from jsonschema import Draft202012Validator
except ImportError:  # pragma: no cover - environment guard
    sys.exit(
        "error: the 'jsonschema' package is required.\n"
        "       install it with:  pip install jsonschema"
    )

REPO_ROOT = Path(__file__).resolve().parent.parent
PROJECTS_DIR = REPO_ROOT / "projects"
SCHEMA_PATH = REPO_ROOT / "schema" / "project.schema.json"

TEMPLATE_NAME = "_template"
REQUIRED_FILES = ("README.md", "project.json")
MAX_BYTES = 5 * 1024 * 1024  # 5 MB per-file cap

# <username>--<slug>: each part is lowercase alphanumeric with internal hyphens.
FOLDER_RE = re.compile(
    r"^[a-z0-9](?:[a-z0-9-]*[a-z0-9])?--[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$"
)


def human_size(num_bytes: int) -> str:
    mb = num_bytes / (1024 * 1024)
    return f"{mb:.2f} MB"


def load_schema_validator() -> Draft202012Validator:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema)


def validate_project(folder: Path, validator: Draft202012Validator) -> list[str]:
    """Return a list of error strings for one project folder (empty == OK)."""
    errors: list[str] = []
    name = folder.name
    is_template = name == TEMPLATE_NAME

    # 1. Folder naming (template is exempt).
    if not is_template and not FOLDER_RE.match(name):
        errors.append(
            f"{name}: folder name must be '<github-username>--<slug>' "
            f"(lowercase letters, digits, hyphens; e.g. 'jdoe--weather-app')."
        )

    # 2. Required files.
    for required in REQUIRED_FILES:
        if not (folder / required).is_file():
            errors.append(f"{name}: missing required file '{required}'.")

    project_json = folder / "project.json"
    if not project_json.is_file():
        return errors  # can't validate schema without the file

    # 3. project.json parses + validates against the schema.
    try:
        data = json.loads(project_json.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"{name}/project.json: invalid JSON ({exc}).")
        return errors

    schema_errors = sorted(validator.iter_errors(data), key=lambda e: list(e.path))
    for err in schema_errors:
        location = "/".join(str(p) for p in err.path) or "(root)"
        errors.append(f"{name}/project.json: {location}: {err.message}")

    # 4. github field must equal the folder's username prefix (template exempt).
    if not is_template and "--" in name:
        prefix = name.split("--", 1)[0]
        github = data.get("github")
        if isinstance(github, str) and github.lower() != prefix.lower():
            errors.append(
                f"{name}/project.json: 'github' is '{github}' but the folder "
                f"prefix is '{prefix}' - they must match."
            )

    return errors


def check_file_sizes() -> list[str]:
    """Flag any file under projects/ that exceeds the size cap."""
    errors: list[str] = []
    for path in PROJECTS_DIR.rglob("*"):
        if path.is_file():
            size = path.stat().st_size
            if size > MAX_BYTES:
                rel = path.relative_to(REPO_ROOT).as_posix()
                errors.append(
                    f"{rel}: {human_size(size)} exceeds the "
                    f"{human_size(MAX_BYTES)} limit — link large data instead."
                )
    return errors


def main() -> int:
    if not PROJECTS_DIR.is_dir():
        print(f"error: projects directory not found at {PROJECTS_DIR}", file=sys.stderr)
        return 1
    if not SCHEMA_PATH.is_file():
        print(f"error: schema not found at {SCHEMA_PATH}", file=sys.stderr)
        return 1

    validator = load_schema_validator()

    folders = sorted(p for p in PROJECTS_DIR.iterdir() if p.is_dir())
    errors: list[str] = []
    checked = 0

    for folder in folders:
        folder_errors = validate_project(folder, validator)
        errors.extend(folder_errors)
        if folder.name != TEMPLATE_NAME:
            checked += 1

    errors.extend(check_file_sizes())

    if errors:
        print(f"FAILED - {len(errors)} problem(s) found:\n", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        print(
            "\nFix the issues above and re-run: python scripts/validate_projects.py",
            file=sys.stderr,
        )
        return 1

    print(f"OK - {checked} project(s) validated, no problems found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
