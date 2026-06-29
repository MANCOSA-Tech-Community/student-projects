#!/usr/bin/env bash
#
# One-time (and re-runnable) governance setup for the student-projects repo.
#
# Applies the `main` branch ruleset from setup/ruleset.json and creates the
# standard issue labels. Idempotent: safe to run repeatedly — it updates the
# existing ruleset/labels in place rather than creating duplicates.
#
# Requirements:
#   - GitHub CLI (gh) authenticated as the org owner:  gh auth login
#   - Run from anywhere; paths are resolved relative to this script.
#
# Usage:
#   ./setup/setup-governance.sh                  # uses the defaults below
#   ORG=MyOrg REPO=my-repo ./setup/setup-governance.sh
#
set -euo pipefail

ORG="${ORG:-MANCOSA-Tech-Community}"
REPO="${REPO:-student-projects}"
RULESET_NAME="Protect main"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
RULESET_FILE="${SCRIPT_DIR}/ruleset.json"

echo "==> Target repository: ${ORG}/${REPO}"

# --- Sanity checks ----------------------------------------------------------
command -v gh >/dev/null 2>&1 || { echo "error: GitHub CLI (gh) not found."; exit 1; }
gh auth status >/dev/null 2>&1 || { echo "error: run 'gh auth login' first."; exit 1; }
[ -f "${RULESET_FILE}" ] || { echo "error: ${RULESET_FILE} not found."; exit 1; }

# --- Apply the branch ruleset ----------------------------------------------
# Look up an existing ruleset by name so we update rather than duplicate it.
echo "==> Applying '${RULESET_NAME}' ruleset to ${ORG}/${REPO}"
existing_id="$(gh api "repos/${ORG}/${REPO}/rulesets" \
  --jq ".[] | select(.name == \"${RULESET_NAME}\") | .id" 2>/dev/null | head -n1 || true)"

if [ -n "${existing_id}" ]; then
  echo "    updating existing ruleset (id ${existing_id})"
  gh api -X PUT "repos/${ORG}/${REPO}/rulesets/${existing_id}" \
    --input "${RULESET_FILE}" >/dev/null
else
  echo "    creating new ruleset"
  gh api -X POST "repos/${ORG}/${REPO}/rulesets" \
    --input "${RULESET_FILE}" >/dev/null
fi
echo "    ruleset applied (admin role bypasses; everyone else is gated)."

# --- Standard issue labels --------------------------------------------------
# `gh label create --force` creates the label or updates it if it exists.
echo "==> Creating / updating issue labels"
create_label() {
  gh label create "$1" --repo "${ORG}/${REPO}" --color "$2" --description "$3" --force >/dev/null
  echo "    - $1"
}

create_label "new-project"      "0B5D3B" "A pull request or proposal adding a new project"
create_label "improvement"      "9FE870" "An improvement to an existing project"
create_label "needs-review"     "FBCA04" "Waiting on maintainer review"
create_label "changes-requested" "D93F0B" "Author needs to make changes"
create_label "good-first-issue" "7057FF" "Good for newcomers"
create_label "question"         "5E6B63" "Further information is requested"

# --- Manual follow-ups the API can't do for you -----------------------------
cat <<'EOF'

==> Done. Two settings must still be enabled in the GitHub web UI:

    1. Settings -> Pages         : Source = "GitHub Actions"
    2. Settings -> Code security : enable "Secret scanning" + "Push protection"

EOF
