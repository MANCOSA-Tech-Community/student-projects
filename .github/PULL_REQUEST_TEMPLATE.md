<!--
Thanks for contributing to the MANCOSA Tech Community!
Fill in the sections below and tick every box before requesting review.
-->

## What kind of PR is this?

- [ ] **New project** (adds a new `projects/<username>--<slug>/` folder)
- [ ] **Improvement** to an existing project (links the issue below)

## Summary

<!-- One or two sentences describing the change. -->

Related issue (required for improvements): Closes #

## Contributor checklist

- [ ] My folder is named `<my-github-username>--<slug>` (lowercase, hyphenated).
- [ ] The folder contains both `README.md` and `project.json`.
- [ ] `project.json` validates against `schema/project.schema.json` and its
      `github` field matches my folder's username prefix.
- [ ] `summary` in `project.json` is 140 characters or fewer.
- [ ] No file in this PR exceeds **5 MB**; large datasets/weights are **linked**, not committed.
- [ ] No secrets, API keys, tokens, or `.env` files are included.
- [ ] I ran `python scripts/validate_projects.py` locally and it passed.
- [ ] This PR changes only one project folder.
