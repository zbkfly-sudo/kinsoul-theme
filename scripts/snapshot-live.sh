#!/usr/bin/env bash
# snapshot-live.sh — Pull the current [live] Shopify theme into ./baselines/<timestamp>/
# Use this BEFORE any push, and ANY TIME you want a rollback point.
#
# Usage:  ./scripts/snapshot-live.sh [optional-label]
# Example: ./scripts/snapshot-live.sh pre-pdp-reviews-fix

set -euo pipefail

cd "$(dirname "$0")/.."
ROOT="$(pwd)"

# Load .env
if [[ ! -f .env ]]; then
  echo "❌ .env not found. Copy .env.example to .env and fill in values."
  exit 1
fi
set -a; source .env; set +a

LABEL="${1:-snapshot}"
STAMP="$(date +%Y-%m-%d-%H%M)"
DEST="baselines/${STAMP}-${LABEL}"

if [[ -d "$DEST" ]]; then
  echo "❌ Destination already exists: $DEST"
  exit 1
fi

mkdir -p "$DEST"
cd "$DEST"

echo "📥 Pulling live theme #${SHOPIFY_LIVE_THEME_ID} from ${SHOPIFY_STORE} ..."
shopify theme pull \
  --theme="${SHOPIFY_LIVE_THEME_ID}" \
  --store="${SHOPIFY_STORE}" \
  --no-color

cd "$ROOT"

echo ""
echo "✅ Snapshot complete: $DEST"
echo "   Size: $(du -sh "$DEST" | cut -f1)"
echo ""
echo "Commit it to git for permanent record:"
echo "   git add $DEST && git commit -m 'baseline: ${LABEL} ($(date +%Y-%m-%d))'"
