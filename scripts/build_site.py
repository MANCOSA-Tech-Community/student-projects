#!/usr/bin/env python3
"""Generate the showcase index and assemble the static site.

Run at deploy time (and locally to preview):

    python scripts/build_site.py

Steps:
  1. Scan every ``projects/*/project.json`` (skipping ``_template``).
  2. Emit ``index.json`` at the repo root (git-ignored; never committed).
  3. Copy ``site/template/`` into ``_site/`` and drop ``index.json`` in beside it.

The site is a pure static bundle: ``_site/index.html`` fetches ``index.json`` at
runtime. Nothing here is committed back to the repository — the deploy workflow
publishes ``_site/`` directly to GitHub Pages.

Stdlib only.
"""

from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PROJECTS_DIR = REPO_ROOT / "projects"
TEMPLATE_DIR = REPO_ROOT / "site" / "template"
ASSETS_DIR = REPO_ROOT / "assets"
INDEX_PATH = REPO_ROOT / "index.json"
SITE_DIR = REPO_ROOT / "_site"

# Files copied from assets/ into the site root so they resolve on the deployed
# Pages site: the banner backs the Open Graph preview; the two logos back the
# hero mark (transparent) and the favicon / apple-touch-icon (green tile).
SITE_ASSETS = [
    "MANCOSA_Banner.png",
    "mancosa_icon_trans.png",
    "mancosa_icon.png",
]

TEMPLATE_NAME = "_template"
# GitHub blob/tree URL prefix so each card can link to its source folder.
REPO_TREE_URL = (
    "https://github.com/MANCOSA-Tech-Community/student-projects/tree/main/projects"
)


def collect_projects() -> list[dict]:
    projects: list[dict] = []
    for folder in sorted(PROJECTS_DIR.iterdir()):
        if not folder.is_dir() or folder.name == TEMPLATE_NAME:
            continue
        project_json = folder / "project.json"
        if not project_json.is_file():
            print(f"warning: skipping {folder.name} (no project.json)", file=sys.stderr)
            continue
        data = json.loads(project_json.read_text(encoding="utf-8"))
        # Enrich with derived fields the front-end needs.
        data["path"] = folder.name
        data["source"] = f"{REPO_TREE_URL}/{folder.name}"
        projects.append(data)
    return projects


def build_index(projects: list[dict]) -> dict:
    # Newest first, then alphabetical by title.
    ordered = sorted(
        projects,
        key=lambda p: (-int(p.get("year", 0)), str(p.get("title", "")).lower()),
    )
    categories = sorted({p["category"] for p in ordered if p.get("category")})
    return {
        "generated": True,
        "count": len(ordered),
        "categories": categories,
        "projects": ordered,
    }


def assemble_site(index: dict) -> None:
    if not TEMPLATE_DIR.is_dir():
        sys.exit(f"error: site template not found at {TEMPLATE_DIR}")
    if SITE_DIR.exists():
        shutil.rmtree(SITE_DIR)
    shutil.copytree(TEMPLATE_DIR, SITE_DIR)
    (SITE_DIR / "index.json").write_text(
        json.dumps(index, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    # assets/ is the single source of truth — copy each shipped asset into the
    # site root. Warn (don't fail) on a missing file so a build still completes.
    for name in SITE_ASSETS:
        asset = ASSETS_DIR / name
        if asset.is_file():
            shutil.copy2(asset, SITE_DIR / name)
        else:
            print(f"warning: asset not found at {asset}", file=sys.stderr)


def main() -> int:
    if not PROJECTS_DIR.is_dir():
        print(f"error: projects directory not found at {PROJECTS_DIR}", file=sys.stderr)
        return 1

    projects = collect_projects()
    index = build_index(projects)

    # Root index.json (git-ignored) — handy for local inspection.
    INDEX_PATH.write_text(
        json.dumps(index, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    assemble_site(index)

    print(
        f"Built site: {index['count']} project(s) -> {SITE_DIR.relative_to(REPO_ROOT)}/ "
        f"(index.json + {len(list(TEMPLATE_DIR.iterdir()))} template file(s))."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
