#!/usr/bin/env bash
# publish.sh — Publish a previously-pushed test theme as the new live theme.
# Tags the corresponding git commit as "published-<timestamp>-<desc>".
# Updates SHOPIFY_LIVE_THEME_ID in .env to the new live ID.
#
# Usage:  ./scripts/publish.sh <theme-id> "short-description"
# Example: ./scripts/publish.sh 147200000000 "pdp-reviews-fix"

set -euo pipefail

cd "$(dirname "$0")/.."

if [[ $# -lt 2 ]]; then
  echo "❌ Usage: $0 <theme-id> \"short-description\""
  exit 1
fi

NEW_THEME_ID="$1"
DESC="$2"
DESC_SLUG="$(echo "$DESC" | tr ' ' '-' | tr -cd 'a-zA-Z0-9-')"
STAMP="$(date +%Y-%m-%d-%H%M)"

if [[ ! -f .env ]]; then
  echo "❌ .env not found."
  exit 1
fi
set -a; source .env; set +a

OLD_LIVE_ID="${SHOPIFY_LIVE_THEME_ID}"

echo "⚠️  About to PUBLISH theme #${NEW_THEME_ID} as the new live theme."
echo "   Current live: #${OLD_LIVE_ID}"
echo "   New live:     #${NEW_THEME_ID}"
echo ""
read -p "Type 'yes' to confirm: " CONFIRM
if [[ "$CONFIRM" != "yes" ]]; then
  echo "Aborted."
  exit 1
fi

# Final safety snapshot before swap
echo ""
echo "📥 Final snapshot of current live before swap..."
./scripts/snapshot-live.sh "pre-publish-${DESC_SLUG}"
git add baselines/
git diff --cached --quiet || git commit -m "baseline: pre-publish ${DESC_SLUG} ($(date +%Y-%m-%d))"

# Publish via CLI
echo ""
echo "🚀 Publishing #${NEW_THEME_ID} ..."
shopify theme publish \
  --theme="${NEW_THEME_ID}" \
  --store="${SHOPIFY_STORE}" \
  --no-color \
  --force

# Update .env with new live ID
sed -i "s/^SHOPIFY_LIVE_THEME_ID=.*/SHOPIFY_LIVE_THEME_ID=${NEW_THEME_ID}/" .env

# Tag git
git tag -a "published-${STAMP}-${DESC_SLUG}" -m "Published to Shopify live as #${NEW_THEME_ID} (replaced #${OLD_LIVE_ID})"
git add .env
git commit -m "publish: ${DESC_SLUG} → live theme #${NEW_THEME_ID}"

echo ""
echo "✅ Published. Live is now #${NEW_THEME_ID}."
echo ""
echo "🔙 ROLLBACK (if anything goes wrong):"
echo "   ./scripts/rollback.sh ${OLD_LIVE_ID}"
echo ""
echo "Or in Shopify Admin: Online Store → Themes → find #${OLD_LIVE_ID} → Publish"
