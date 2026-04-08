#!/usr/bin/env bash
# push-test.sh — Push the current working directory to a NEW unpublished test theme.
# Enforces: clean git, snapshot of live first, named with timestamp + description.
# NEVER pushes to the live theme.
#
# Usage:  ./scripts/push-test.sh "short-description"
# Example: ./scripts/push-test.sh "pdp-reviews-fix"

set -euo pipefail

cd "$(dirname "$0")/.."
ROOT="$(pwd)"

# ---------- Preflight ----------
if [[ $# -lt 1 ]]; then
  echo "❌ Usage: $0 \"short-description\""
  exit 1
fi

DESC="$1"
DESC_SLUG="$(echo "$DESC" | tr ' ' '-' | tr -cd 'a-zA-Z0-9-')"
STAMP="$(date +%Y-%m-%d-%H%M)"
THEME_NAME="fix-${STAMP}-${DESC_SLUG}"

# Load .env
if [[ ! -f .env ]]; then
  echo "❌ .env not found."
  exit 1
fi
set -a; source .env; set +a

# Require clean git working tree (no uncommitted changes)
if [[ -n "$(git status --porcelain)" ]]; then
  echo "❌ Uncommitted changes detected. Commit them first:"
  git status --short
  exit 1
fi

CURRENT_COMMIT="$(git rev-parse --short HEAD)"
echo "📌 Current git commit: ${CURRENT_COMMIT}"

# ---------- Sync content/settings from live first ----------
# Pulls templates/, config/, header/footer groups from live so user's manual
# image bindings + theme editor edits are preserved on the new test theme.
echo ""
echo "🔄 Syncing content/settings from live before push..."
shopify theme pull \
  --theme="${SHOPIFY_LIVE_THEME_ID}" \
  --store="${SHOPIFY_STORE}" \
  --only="templates/*.json" \
  --only="config/*.json" \
  --only="sections/header-group.json" \
  --only="sections/footer-group.json" \
  --no-color

if [[ -n "$(git status --porcelain)" ]]; then
  echo ""
  echo "⚠️  Live content differs from local. Pulled changes:"
  git status --short
  echo ""
  echo "❌ Stopping. Review the diff and decide:"
  echo "   - If your local structural changes need to be RE-APPLIED on top of live's content,"
  echo "     re-apply them manually, then commit and run this script again."
  echo "   - If you want to discard local changes and use live's version, just commit the pull"
  echo "     and run this script again."
  echo ""
  echo "   git diff                # see what changed"
  echo "   git add -A && git commit -m 'sync: pull content from live'"
  exit 1
fi

# ---------- Snapshot live first ----------
echo ""
echo "📥 Snapshotting current live theme as safety baseline..."
./scripts/snapshot-live.sh "pre-${DESC_SLUG}"

# Auto-commit the baseline
git add baselines/
if [[ -n "$(git diff --cached --name-only)" ]]; then
  git commit -m "baseline: pre-${DESC_SLUG} ($(date +%Y-%m-%d))"
fi

# ---------- Push as new unpublished theme ----------
echo ""
echo "🚀 Pushing working tree as new unpublished theme: ${THEME_NAME}"
echo ""

shopify theme push \
  --unpublished \
  --theme="${THEME_NAME}" \
  --store="${SHOPIFY_STORE}" \
  --no-color \
  --json > /tmp/push-result.json

THEME_ID="$(grep -o '"id":[0-9]*' /tmp/push-result.json | head -1 | cut -d: -f2)"

# Tag the git commit with the theme name for traceability
git tag -a "test-${STAMP}-${DESC_SLUG}" -m "Pushed to Shopify as test theme '${THEME_NAME}' (#${THEME_ID})"

echo ""
echo "✅ Push complete."
echo ""
echo "   Theme name: ${THEME_NAME}"
echo "   Theme ID:   ${THEME_ID}"
echo "   Git tag:    test-${STAMP}-${DESC_SLUG}"
echo ""
echo "   Preview:    https://${SHOPIFY_STORE}/?preview_theme_id=${THEME_ID}"
echo "   Editor:     https://${SHOPIFY_STORE}/admin/themes/${THEME_ID}/editor"
echo ""
echo "👉 NEXT STEP:"
echo "   1. Open the preview URL above and verify everything works"
echo "   2. If broken: do NOT publish. Fix locally, commit, run this script again."
echo "   3. If good:   ./scripts/publish.sh ${THEME_ID} \"${DESC_SLUG}\""
