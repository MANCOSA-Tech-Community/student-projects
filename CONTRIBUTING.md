# Contributing

Welcome! This guide shows you exactly how to add your project or improve someone
else's. **Everything happens through a pull request (PR)** that gets reviewed before
it goes live - the same way professional software teams work.

There are **two ways** to add a project:
- **Option 1 - with Git** (recommended; teaches a real skill).
- **Option 2 - in your browser** (no installs, no command line).

Pick whichever you're comfortable with. Both end in the same place: a PR we review and merge.

---

## One-time setup

- A free [GitHub account](https://github.com/signup).
- For Option 1: [Git installed](https://git-scm.com/downloads).
- New to forking and pull requests? Read GitHub's 2-minute primer:
  [Fork a repo](https://docs.github.com/en/get-started/quickstart/fork-a-repo).

---

## Option 1 - Add a project with Git

We'll use a real example all the way through. **Imagine your GitHub username is
`janedev` and you built a to-do app.** Just swap in your own username and project
name as you go.

### 1. Fork this repo
Click **Fork** (top-right of the repo page). You now have your own copy at
`github.com/janedev/student-projects`.

### 2. Clone YOUR fork to your computer
```bash
git clone https://github.com/janedev/student-projects.git
cd student-projects
```

### 3. Create a branch for your work
```bash
git checkout -b add/janedev-todo-app
```

### 4. Make your project folder from the template
Your folder **must** be named `<your-username>--<project-slug>` (lowercase, hyphens).

```bash
# Mac / Linux / Git Bash:
cp -r projects/_template projects/janedev--todo-app
```
```powershell
# Windows PowerShell:
Copy-Item -Recurse projects/_template projects/janedev--todo-app
```

### 5. Add your work and fill in the two required files
Put your code (or a link to it) inside `projects/janedev--todo-app/`, then edit:

- **`README.md`** - what it is, the tech you used, how to run it.
- **`project.json`** - the details that put your project on the showcase. Filled-in example:

```json
{
  "title": "To-Do App",
  "author": "Jane Doe",
  "github": "janedev",
  "year": 2026,
  "category": "Web/Mobile",
  "tags": ["react", "javascript", "local-storage"],
  "summary": "A simple to-do list web app with dark mode and offline support.",
  "links": {
    "demo": "https://janedev.github.io/todo-app/",
    "repo": "https://github.com/janedev/todo-app",
    "video": ""
  }
}
```
> `category` must be one of: **AI/ML**, **Data Science**, **Web/Mobile**, **Automation**, **Other**.
> `github` must match your folder prefix (`janedev`). `summary` is max 140 characters.
> Leave any link you don't have as `""`.

### 6. Check it yourself before pushing (optional but smart)
This runs the **exact same checks** our CI will run, so you catch problems early:
```bash
pip install -r scripts/requirements.txt
python scripts/validate_projects.py
```
You want to see `OK - N project(s) validated, no problems found.`

### 7. Commit and push
```bash
git add projects/janedev--todo-app
git commit -m "Add janedev--todo-app"
git push origin add/janedev-todo-app
```

### 8. Open the pull request
Go to your fork on GitHub - it'll show a **"Compare & pull request"** button. Click it,
write one line about your project, and submit.

### 9. What happens next
- Automated checks run on your PR (folder name, required files, the rules below).
- A maintainer reviews it and may ask for small changes.
- Once approved and merged, **your project automatically appears on the
  [live showcase](https://mancosa-tech-community.github.io/student-projects/)**. 🎉

> First time contributing? You may see "checks haven't run yet" until a maintainer
> clicks **Approve and run workflows** - that's a normal GitHub security step for new
> contributors. After your first PR, checks run automatically.

---

## Option 2 - Add a project in your browser (no Git)

You can do the whole thing on github.com:

1. Click **Fork** to get your own copy.
2. In your fork, click **Add file → Create new file**.
3. In the filename box, type the full path including the folder, e.g.
   `projects/janedev--todo-app/project.json`, then paste the JSON from Option 1, Step 5.
4. Repeat to add `README.md` (and use **Add file → Upload files** to drag in your code).
5. At the bottom, choose **"Create a new branch and start a pull request"**, then
   **Propose changes** → **Create pull request**.

Same review, same checks, same result - just no terminal.

---

## The rules (what the checks enforce)

Your PR must satisfy all of these, or the automated check will fail with a clear message:

- Folder is named `yourusername--project-slug` (lowercase letters, numbers, hyphens).
- The folder contains both `README.md` and `project.json`.
- `project.json` is valid and its `github` field matches your folder prefix.
- `summary` is 140 characters or fewer; `category` is one of the five allowed values.
- No single file is larger than 5 MB - **link** large datasets/models, don't commit them.
- No passwords, API keys, or secrets anywhere in your files.
- It's your own work (or you clearly credit anything you used).

---

## Improve someone else's project

1. **Open an issue first** to describe the improvement and agree on it.
2. Fork, branch (`git checkout -b fix/short-description`), and edit **only that
   project's folder**.
3. Open a PR. The project's author and a maintainer will review it.

---

## Need help?

Open an [issue](../../issues) and ask - that's exactly what the community is for.
No question is too basic.