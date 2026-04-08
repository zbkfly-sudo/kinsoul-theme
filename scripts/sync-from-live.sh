#!/usr/bin/env bash
# sync-from-live.sh — Pull content/settings files from the LIVE theme into the working tree.
# This preserves manual edits the user made in the Shopify theme editor (image picks,
# text fields, color scheme changes, section reordering, etc).
#
# What it pulls (content/settings — user-controlled in editor):
#   - templates/         (page templates with section configs and image picks)
#   - config/            (settings_data.json with global theme settings)
#   - sections/*group*.json  (header/footer group configs)
#
# What it does NOT touch (code — repo is source of truth):
#   - sections/*.liquid
#   - snippets/*
#   - assets/*
#   - blocks/*
#   - layout/*
#   - locales/*
#
# Usage:  ./scripts/sync-from-live.sh
# Run this BEFORE making structural code changes that will be pushed.

set -euo pipefail

cd "$(dirname "$0")/.."

if [[ ! -f .env ]]; then
  echo "❌ .env not found."
  exit 1
fi
set -a; source .env; set +a

if [[ -n "$(git status --porcelain)" ]]; then
  echo "❌ Uncommitted changes detected. Commit or stash them before sync:"
  git status --short
  exit 1
fi

echo "📥 Pulling content/settings from live theme #${SHOPIFY_LIVE_THEME_ID} ..."
echo ""

shopify theme pull \
  --theme="${SHOPIFY_LIVE_THEME_ID}" \
  --store="${SHOPIFY_STORE}" \
  --only=templates/ \
  --only=config/ \
  --only=sections/header-group.json \
  --only=sections/footer-group.json \
  --no-color

echo ""
if [[ -n "$(git status --porcelain)" ]]; then
  echo "📝 Changes pulled from live:"
  git status --short
  echo ""
  echo "Review the diff:  git diff"
  echo ""
  echo "If looks good, commit:"
  echo "   git add -A && git commit -m 'sync: pull content from live ($(date +%Y-%m-%d-%H%M))'"
else
  echo "✅ Local already in sync with live. No changes."
fi
