# Contributing

Everything here happens through **fork → branch → pull request**. You don't need
write access to this repository, and you don't need any tools beyond git and
Python. This guide assumes you know basic git (clone, branch, commit, push).

There are two paths:

- **[Path 1 — Submit a new project](#path-1--submit-a-new-project)**
- **[Path 2 — Improve an existing project](#path-2--improve-an-existing-project)**

First-time setup is the same for both:

```bash
# 1. Fork this repo on GitHub (click "Fork"), then clone YOUR fork:
git clone https://github.com/<your-username>/student-projects.git
cd student-projects

# 2. Keep a link to the original so you can stay up to date:
git remote add upstream https://github.com/MANCOSA-Tech-Community/student-projects.git
```

---

## Path 1 — Submit a new project

### 1. Create a branch

```bash
git checkout main
git pull upstream main
git checkout -b add/<your-username>-<slug>
```

`<slug>` is a short, lowercase-hyphenated name for the project, e.g. `spam-classifier`.

### 2. Copy the template into your project folder

Your folder **must** be named `<your-github-username>--<slug>` (note the double
hyphen separating username and slug):

```bash
cp -r projects/_template projects/<your-username>--<slug>
```

On Windows PowerShell:

```powershell
Copy-Item -Recurse projects\_template projects\<your-username>--<slug>
```

### 3. Add your work and fill in the two required files

- **`README.md`** — title, author, what it does, tech stack, how to run,
  screenshots, and any notes. Make it something you'd be happy to show an employer.
- **`project.json`** — the metadata that drives the showcase card. It must match
  [`schema/project.schema.json`](schema/project.schema.json). Critically, the
  `github` field must equal your folder's username prefix.

Example `project.json`:

```json
{
  "title": "Spam Classifier",
  "author": "Your Name",
  "github": "<your-username>",
  "year": 2026,
  "category": "AI/ML",
  "tags": ["nlp", "scikit-learn", "classification"],
  "summary": "A short one-liner (max 140 characters) describing the project.",
  "links": {
    "demo": "https://your-demo.example.com",
    "repo": "https://github.com/<your-username>/your-project",
    "video": ""
  }
}
```

**Categories** (pick one): `AI/ML`, `Data Science`, `Web/Mobile`, `Automation`, `Other`.

### 4. Validate locally before pushing

```bash
pip install -r scripts/requirements.txt   # one-time: installs jsonschema
python scripts/validate_projects.py
```

This runs the same checks as CI. Fix anything it reports.

### 5. Commit, push, open the PR

```bash
git add projects/<your-username>--<slug>
git commit -m "Add <your-username>--<slug>"
git push origin add/<your-username>-<slug>
```

Open a pull request from your branch to `MANCOSA-Tech-Community/student-projects:main`.
CI runs automatically; once it's green a maintainer reviews and merges. When it
merges, the showcase site rebuilds and your project appears — **no further action
needed**.

---

## Path 2 — Improve an existing project

We discuss improvements **before** code, out of respect for the original author.

### 1. Open an issue first

Use the **"Improve an existing project"** issue template. Describe what you'd
change and why. Wait for a 👍 from the maintainer (and ideally the original
author) before starting.

### 2. Branch and edit only that project's folder

```bash
git checkout main
git pull upstream main
git checkout -b fix/<short-description>
# edit only files inside projects/<username>--<slug>/
```

Keep your change scoped to a single project folder. Don't touch other projects,
tooling, or docs in the same PR.

### 3. Validate, push, and PR

```bash
python scripts/validate_projects.py
git commit -am "Improve <username>--<slug>: <short description>"
git push origin fix/<short-description>
```

Open the PR and link the issue (e.g. "Closes #123"). CI runs, then the maintainer
reviews and merges.

---

## The rules CI enforces

Your PR will be blocked until all of these pass:

| Check | Requirement |
|-------|-------------|
| Folder name | `<github-username>--<slug>`, lowercase-hyphenated. |
| Required files | Both `README.md` and `project.json` present. |
| Schema | `project.json` validates against `schema/project.schema.json`. |
| Identity | `project.json.github` equals the folder's username prefix. |
| Summary length | `summary` is 140 characters or fewer. |
| File size | No file exceeds **5 MB**. |

### Large data and binaries

Don't commit datasets, model weights, or large media. The 5 MB per-file cap is
enforced in CI. Instead, **link** them from your `README.md` (Google Drive,
Hugging Face, Kaggle, a release asset, etc.) and explain how to obtain them.

### Notebooks

`.ipynb` files are fine if they're under the size cap. **Clear large cell outputs
before committing** — rendered plots and dataframes bloat the file quickly.

### Secrets

Never commit API keys, tokens, passwords, or `.env` files. CI scans for secrets,
and the repository has push protection enabled. If you leak a credential, rotate
it immediately.

---

## Tips for a smooth review

- One project (or one improvement) per pull request.
- Write a clear PR title and description; the template will prompt you.
- Resolve review conversations rather than leaving them open.
- Keep your branch up to date: `git pull upstream main` and merge if asked.

Questions? Open an issue or start a discussion. Welcome aboard. 🚀
