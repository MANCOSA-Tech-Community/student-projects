# MANCOSA Tech Community — Student Projects

[![Validate](https://github.com/MANCOSA-Tech-Community/student-projects/actions/workflows/validate.yml/badge.svg)](https://github.com/MANCOSA-Tech-Community/student-projects/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-0B5D3B.svg)](LICENSE)

A student-run showcase of projects built by the MANCOSA tech community. Students
publish their own work and improve each other's — entirely through git pull
requests. Every accepted project appears on the public showcase site, generated
automatically from this repository.

**🌐 Live showcase:** https://mancosa-tech-community.github.io/student-projects/

> **Student-run, not an official MANCOSA channel.** This is a community project
> maintained by students. It is not operated or endorsed by MANCOSA.

---

## How it works

Each project lives in its own self-contained folder under `projects/`, named
`<github-username>--<project-slug>/`. There is **no central list to edit** — the
showcase index is generated from the project folders at build time. That single
decision is what lets dozens of people contribute at once without their pull
requests colliding on the same file.

```
projects/
├── _template/                     # copy this to start a new project
└── shiviancodes--spam-classifier/ # one folder per project
    ├── README.md                  # human-readable write-up
    └── project.json               # machine-readable metadata
```

Every pull request is automatically validated (folder naming, required files,
metadata schema, file-size limits) before a maintainer reviews it.

## Contribute

Two ways to get involved — both are plain git, no special tools:

1. **Add your own project** — fork, copy the template, fill it in, open a PR.
2. **Improve an existing project** — open an issue to discuss, then fork and PR.

Full step-by-step commands are in **[CONTRIBUTING.md](CONTRIBUTING.md)**. You can
validate your work locally before pushing:

```bash
python scripts/validate_projects.py
```

## Project contract (the short version)

- Folder: `projects/<your-github-username>--<slug>/` (slug is lowercase-hyphenated).
- Required files: `README.md` and `project.json`.
- `project.json` must match [`schema/project.schema.json`](schema/project.schema.json);
  its `github` field must equal your folder's username prefix.
- No file over **5 MB**. Link large datasets and model weights — don't commit them.

## Repository layout

| Path | Purpose |
|------|---------|
| `projects/` | Self-contained project folders — the only place you add files. |
| `schema/` | The JSON Schema every `project.json` must satisfy. |
| `scripts/` | Validation (CI) and site-build tooling. |
| `site/` | Framework-free showcase template (rendered at deploy). |
| `setup/` | One-time admin setup (ruleset + governance script). |
| `.github/` | Issue/PR templates, CODEOWNERS, CI workflows. |

## Governance

A single maintainer reviews, approves, and merges all pull requests. See
**[GOVERNANCE.md](GOVERNANCE.md)** for the review process and how to propose
becoming a future maintainer. All participation is covered by our
**[Code of Conduct](CODE_OF_CONDUCT.md)**.

## License

Repository tooling and documentation are released under the [MIT License](LICENSE).
Each project remains the work of its author; check a project's own README for any
additional terms.
