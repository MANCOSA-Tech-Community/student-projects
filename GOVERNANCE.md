# Governance

This document describes how the MANCOSA Tech Community student-projects
repository is run: who decides what, how pull requests are reviewed, and how the
model can evolve as the community grows.

## Roles

| Role | Who | Rights |
|------|-----|--------|
| **Maintainer / Admin** | The founder (`@shiviancodes`) | Sole admin. Reviews, approves, and merges every PR. Owns repository settings and the ruleset. |
| **Contributor** | Everyone else | No write access. Contributes exclusively via fork → pull request. |

This is a deliberate **single-maintainer model**. There is one admin and one
approver. It keeps full editorial control with the founder while the community is
small, and it requires no paid GitHub features.

## How pull requests are reviewed

1. A contributor opens a PR from their fork.
2. **CI (`validate`) runs automatically** - folder naming, required files, schema
   validation, the `github`-matches-prefix check, and the 5 MB file-size gate. The
   PR cannot merge until this check passes.
3. **CODEOWNERS** routes every PR to the maintainer for review automatically.
4. The maintainer reviews for quality, scope, and conduct, then requests changes
   or approves.
5. All review conversations must be resolved before merge.
6. The maintainer merges. On merge to `main`, the showcase site rebuilds and
   deploys automatically - nothing is committed back to the repository.

For **improvements to an existing project**, contributors open an issue first so
the change can be discussed with the maintainer and, ideally, the original author
before any code is written.

## Branch protection (the `main` ruleset)

`main` is protected by a repository ruleset, applied via
[`setup/setup-governance.sh`](setup/setup-governance.sh) and version-controlled in
[`setup/ruleset.json`](setup/ruleset.json). It requires:

- A pull request before merging.
- **1** approving review (the maintainer).
- Review from **CODEOWNERS**.
- The **`validate`** status check to pass.
- The branch to be up to date before merging.
- All conversations to be resolved.
- No force-pushes and no branch deletion.

### Why the admin can bypass

There is only one maintainer, so there is no second person to provide the required
approving review on the maintainer's *own* commits. To resolve this without
weakening the rules for anyone else, the ruleset grants a **bypass to the
"Repository admin" role** (a role-based bypass, not a named-user exception). This
lets the maintainer merge their own changes while **every contributor remains
fully gated** by review and CI. As soon as a second maintainer exists, the bypass
can be removed and normal two-person review applies - with no restructuring.

## Becoming a maintainer

The model is intentionally easy to grow into. If you'd like to help maintain the
project:

1. Build a track record - submit good projects and helpful, well-scoped
   improvements to others' work.
2. Open an issue titled "Maintainer proposal: \<your-username\>" describing what
   you'd help with (reviews, triage, tooling, docs).
3. The current maintainer evaluates and, if it's a fit, adds you to a maintainers
   team with review rights and updates `CODEOWNERS` and the ruleset accordingly.

There are no hidden requirements. The bar is trust, reliability, and alignment
with the Code of Conduct.

## One-time setup (performed by the admin)

These steps are run once, after the repository is created. They're scripted where
possible:

1. Create the **free organization** `MANCOSA-Tech-Community`.
2. Create the **public** repository `student-projects` and push this scaffold.
3. Run [`setup/setup-governance.sh`](setup/setup-governance.sh) to apply the
   ruleset and create issue labels.
4. **Settings → Pages →** deploy from **GitHub Actions**.
5. **Settings → Code security →** enable **secret scanning** and **push
   protection**.

## Changing this document

Governance changes are made by the maintainer via pull request so they're
transparent and recorded in history. Substantive changes should be announced to
the community (an issue or discussion) before they take effect.
