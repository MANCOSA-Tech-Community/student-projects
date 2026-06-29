<p align="center">
  <a href="https://mancosa-tech-community.github.io/student-projects/">
    <img src="assets/MANCOSA_Banner.png" alt="MANCOSA Tech Community" width="100%">
  </a>
</p>

<h1 align="center">MANCOSA Tech Community - Student Projects</h1>

<p align="center">
  A student-run showcase of projects built by the MANCOSA tech community.<br>
  Submit your own work or improve someone else's -; all through pull requests.
</p>

<p align="center">
    <a href="https://mancosa-tech-community.github.io/student-projects/"><strong>Visit the live site  </strong></a>
  </p>

<p align="center">
  <a href="https://github.com/MANCOSA-Tech-Community/student-projects/actions/workflows/validate.yml">
    <img src="https://github.com/MANCOSA-Tech-Community/student-projects/actions/workflows/validate.yml/badge.svg" alt="validate">
  </a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-0B5D3B.svg" alt="License: MIT"></a>
  <img src="https://img.shields.io/badge/contributions-welcome-9FE870.svg" alt="Contributions welcome">
  <a href="CODE_OF_CONDUCT.md"><img src="https://img.shields.io/badge/code%20of%20conduct-be%20kind-5E6B63.svg" alt="Code of conduct"></a>
</p>

<p align="center"><sub><strong>Student-run · not an official MANCOSA channel</strong></sub></p>

---
## Explore the projects

<img src="https://github.com/user-attachments/assets/5eec2c69-71ba-4377-b065-227aeb5df579" align="left" width="300" alt="MANCOSA Tech Community showcase on mobile">

### Every student project, in one place

A public, searchable directory of what MANCOSA students and alumni are building - and a real link you can put on your CV.

&nbsp;&nbsp;•&nbsp; **Search & filter** by title, author, or tag<br>
&nbsp;&nbsp;•&nbsp; **Every card links** straight to the source code<br>
&nbsp;&nbsp;•&nbsp; **Merged projects appear automatically** - no manual updates<br>
&nbsp;&nbsp;•&nbsp; **Works on any device**, including mobile (shown here)<br>
&nbsp;&nbsp;•&nbsp; **Free and open** - anyone in the community can contribute

<a href="https://mancosa-tech-community.github.io/student-projects/"><img src="https://img.shields.io/badge/Browse_the_showcase-0B5D3B?style=for-the-badge" alt="Browse the showcase"></a>
<a href="CONTRIBUTING.md"><img src="https://img.shields.io/badge/Submit_your_project-9FE870?style=for-the-badge&logoColor=black" alt="Submit your project"></a>
### What this is

A shared, public home for projects built by MANCOSA students and alumni in tech - data science, machine learning, AI, software development, DevOps, and everything around it.

Every project lives in its own folder. You publish your work, browse and learn from everyone else's, and improve each other's projects the way professional software teams do: **through reviewed pull requests** - the same workflow used in real software jobs. So contributing here isn't just sharing a project; it's hands-on practice with the tools and process employers expect.

<br clear="left">

## Contribute

Two ways in, both through a pull request. Full step-by-step commands are in
**[CONTRIBUTING.md](CONTRIBUTING.md)** -; the short version:

**Submit a new project**
1. Fork this repo.
2. Copy `projects/_template/` to `projects/<your-github-username>--<project-slug>/`.
3. Fill in the `README.md` and `project.json` inside it.
4. Open a pull request. Automated checks run, then it's reviewed and merged.

**Improve an existing project**
1. Open an issue to discuss the change.
2. Fork, edit only that project's folder, open a pull request.

> Before pushing, you can run the same checks locally that CI runs:
> `pip install -r scripts/requirements.txt && python scripts/validate_projects.py`

## How it works

- **One folder per project**, named `<github-username>--<slug>` so two people never collide.
- **No hand-edited project list.** The showcase index is generated automatically from
  each project's `project.json` at build time -; so contributors never fight over a shared file.
- **`main` is protected.** Every change lands via a reviewed PR that passes automated checks.

## Repository structure

```
student-projects/
├── projects/            # one self-contained folder per student project
│   └── _template/       # copy this to start your own
├── schema/              # the project.json contract that CI enforces
├── scripts/             # validation + site-build tooling
├── site/                # the showcase site (built and deployed automatically)
└── .github/             # PR/issue templates, CODEOWNERS, CI workflows
```

## Community guidelines

Be kind, give credit, submit your own work. See **[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)**.
How the project is run and reviewed is documented in **[GOVERNANCE.md](GOVERNANCE.md)**.

## License

Released under the [MIT License](LICENSE). You keep ownership of your work; others can
learn from it.

---

<p align="center"><sub>Built by and for MANCOSA students. Not affiliated with or endorsed by MANCOSA.</sub></p>
