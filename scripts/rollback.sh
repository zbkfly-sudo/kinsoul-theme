#!/usr/bin/env bash
# rollback.sh — Republish a previous theme as live (instant rollback).
# Use only when a freshly-published theme breaks something.
#
# Usage:  ./scripts/rollback.sh <previous-theme-id>

set -euo pipefail

cd "$(dirname "$0")/.."

if [[ $# -lt 1 ]]; then
  echo "❌ Usage: $0 <previous-theme-id>"
  echo ""
  echo "Recent theme IDs (from .env history / git log):"
  git log --oneline | grep -E "publish:|baseline:" | head -10
  exit 1
fi

PREV_ID="$1"

if [[ ! -f .env ]]; then
  echo "❌ .env not found."
  exit 1
fi
set -a; source .env; set +a

CURRENT_LIVE="${SHOPIFY_LIVE_THEME_ID}"

echo "🚨 ROLLBACK"
echo "   Current live: #${CURRENT_LIVE}"
echo "   Roll back to: #${PREV_ID}"
echo ""
read -p "Type 'yes' to confirm: " CONFIRM
if [[ "$CONFIRM" != "yes" ]]; then
  echo "Aborted."
  exit 1
fi

shopify theme publish \
  --theme="${PREV_ID}" \
  --store="${SHOPIFY_STORE}" \
  --no-color \
  --force

sed -i "s/^SHOPIFY_LIVE_THEME_ID=.*/SHOPIFY_LIVE_THEME_ID=${PREV_ID}/" .env
git add .env
git commit -m "rollback: live → #${PREV_ID} (was #${CURRENT_LIVE})" || true
git tag -a "rollback-$(date +%Y-%m-%d-%H%M)" -m "Rolled back from #${CURRENT_LIVE} to #${PREV_ID}"

echo ""
echo "✅ Rolled back. Live is now #${PREV_ID}."
