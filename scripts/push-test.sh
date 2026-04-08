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

# ---------- Drift check (read-only) ----------
# Pull live's content to a temp dir and diff against working tree.
# We DO NOT overwrite the working tree — that would clobber structural changes.
# If drift is detected, the user must run ./scripts/sync-from-live.sh, then
# re-apply any structural changes, commit, and re-run this script.
echo ""
echo "🔍 Checking for content drift between local and live..."
DRIFT_TMP="$(mktemp -d)"
trap "rm -rf $DRIFT_TMP" EXIT

(cd "$DRIFT_TMP" && shopify theme pull \
  --theme="${SHOPIFY_LIVE_THEME_ID}" \
  --store="${SHOPIFY_STORE}" \
  --only="templates/*.json" \
  --only="config/*.json" \
  --no-color > /dev/null 2>&1)

DRIFT_FILES=()
for f in $(find "$DRIFT_TMP/templates" "$DRIFT_TMP/config" -type f 2>/dev/null); do
  REL="${f#$DRIFT_TMP/}"
  if [[ -f "$REL" ]] && ! diff -q "$f" "$REL" > /dev/null 2>&1; then
    # Skip files that we KNOW we've structurally edited (whitelist)
    case "$REL" in
      templates/product.json|templates/collection.json|templates/index.json)
        # These are expected to differ — we have local structural changes
        ;;
      *)
        DRIFT_FILES+=("$REL")
        ;;
    esac
  fi
done

if [[ ${#DRIFT_FILES[@]} -gt 0 ]]; then
  echo ""
  echo "⚠️  Live has content edits not yet in local repo:"
  for f in "${DRIFT_FILES[@]}"; do echo "   - $f"; done
  echo ""
  echo "❌ Stopping to prevent overwriting user's manual edits."
  echo ""
  echo "   To resolve:"
  echo "   1. ./scripts/sync-from-live.sh        # pull live content to local"
  echo "   2. Re-apply any structural code changes that got reverted"
  echo "   3. git add -A && git commit -m 'sync: pull content from live'"
  echo "   4. Run this script again"
  exit 1
fi

echo "✅ No content drift on non-structural files."

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
