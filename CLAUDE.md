# CLAUDE.md — Kinsoul Energy Theme · Strict Operating Rules

> **Read this file first in every session that touches this repo.**
> These rules are non-negotiable. They exist because production = a real store with real customers, and a single bad push can break checkout, lose orders, and destroy trust in 30 seconds.

---

## 1. What this repo is

- **Path:** `/home/binkai/projects/shopify-theme-redesign/`
- **Purpose:** Source-of-truth for the Kinsoul Energy Shopify theme.
- **Live store:** `qr4xym-qi.myshopify.com` (custom domain: `www.kinsoulenergy.com`)
- **Live theme ID:** stored in `.env` as `SHOPIFY_LIVE_THEME_ID` (always read from `.env`, never hard-code).
- **CLI auth:** Theme Access token in `.env` as `SHOPIFY_CLI_THEME_TOKEN`. The `.env` file is gitignored. Never paste token contents into chat, code, or commits.

---

## 2. Hard rules (THE FOUR LAWS)

### Law 1 — Never push directly to the live theme.
- ❌ `shopify theme push --theme=$SHOPIFY_LIVE_THEME_ID` is **forbidden**.
- ✅ Always push to a **new unpublished test theme** via `./scripts/push-test.sh`.
- The user previews and approves. Then `./scripts/publish.sh` swaps it in.

### Law 2 — Always commit before push.
- The repo's working tree must be **clean** (`git status` shows nothing) before any push.
- `push-test.sh` enforces this and will refuse to run otherwise.
- If you have local changes, commit them first with a descriptive message. **Never** stash-and-push; the pushed code must match a real git commit.

### Law 3 — Always snapshot live before changing live.
- Before any push *and* before any publish, the helper scripts pull the current `[live]` theme into `baselines/<timestamp>-<label>/` and commit it.
- These baselines are the **instant rollback artifact**. Never delete them. Never `.gitignore` them.
- If you somehow need to push without the helper script (you almost never should), you MUST run `./scripts/snapshot-live.sh <label>` first.

### Law 4 — Every published version is a git tag.
- After `publish.sh` runs, the corresponding git commit is tagged `published-YYYY-MM-DD-HHMM-<desc>`.
- Test pushes are tagged `test-YYYY-MM-DD-HHMM-<desc>`.
- This means: from any moment in time, you can reproduce exactly what was on Shopify.

---

## 3. Standard workflow (the only workflow)

### Making changes
```
1. cd /home/binkai/projects/shopify-theme-redesign
2. git status                          # confirm clean
3. <edit files locally>
4. git add <files>
5. git commit -m "feat/fix/refactor: <what changed and why>"
```

### Pushing changes for the user to preview
```
6. ./scripts/push-test.sh "short-description"
```
This will:
- Verify git is clean (refuse if not)
- Snapshot current live → `baselines/<timestamp>-pre-<desc>/`
- Auto-commit the baseline
- Push working tree as a new unpublished theme `fix-<timestamp>-<desc>`
- Tag the git commit `test-<timestamp>-<desc>`
- Print the preview URL

### After the user previews and approves
```
7. ./scripts/publish.sh <theme-id-from-step-6> "short-description"
```
This will:
- Confirm with user (`yes` prompt)
- Final snapshot of the about-to-be-replaced live theme
- Publish the new theme as live
- Update `.env` with new live theme ID
- Tag the git commit `published-<timestamp>-<desc>`

### If something breaks after publish
```
8. ./scripts/rollback.sh <previous-live-theme-id>
```
The previous live ID is in the most recent `publish:` commit message and in `.env` history.

---

## 4. Naming conventions

| Thing | Format | Example |
|---|---|---|
| Branch | `main` only (single-branch trunk) | `main` |
| Commit message | `type: description` | `fix: PDP Liquid error from missing schema snippet` |
| Test theme | `fix-YYYY-MM-DD-HHMM-<slug>` | `fix-2026-04-07-2330-pdp-reviews` |
| Baseline dir | `baselines/YYYY-MM-DD-HHMM-<label>/` | `baselines/2026-04-07-1450-pre-fix-live/` |
| Test git tag | `test-YYYY-MM-DD-HHMM-<slug>` | `test-2026-04-07-2330-pdp-reviews` |
| Published git tag | `published-YYYY-MM-DD-HHMM-<slug>` | `published-2026-04-07-2350-pdp-reviews` |

Commit type prefixes: `feat`, `fix`, `refactor`, `docs`, `infra`, `baseline`, `publish`, `rollback`, `wip`.

---

## 5. Files & directories

```
shopify-theme-redesign/
├── CLAUDE.md                   ← THIS FILE — operating rules
├── .env                        ← secrets (gitignored)
├── .env.example                ← template (committed)
├── .gitignore
├── PROJECT-STATUS.md           ← high-level project status
├── SEO-STATUS.md               ← SEO work status
├── REVIEW-SYSTEM-V2.md         ← homepage + PDP review data
├── ... (other docs)
│
├── assets/                     ← Shopify theme: CSS, JS, images
├── blocks/                     ← Shopify theme: block definitions
├── config/                     ← Shopify theme: settings_schema.json, settings_data.json
├── layout/                     ← Shopify theme: theme.liquid
├── locales/                    ← Shopify theme: translations
├── sections/                   ← Shopify theme: section definitions (incl. all kinsoul-* sections)
├── snippets/                   ← Shopify theme: snippets (incl. all kinsoul-* snippets)
├── templates/                  ← Shopify theme: page templates (JSON)
│
├── baselines/                  ← Git-tracked snapshots of past live themes
│   └── YYYY-MM-DD-HHMM-<label>/   ← each is a full theme dump
│
└── scripts/                    ← Workflow helper scripts
    ├── snapshot-live.sh        ← pull current live → baselines/
    ├── push-test.sh            ← commit-check + snapshot + push as test theme
    ├── publish.sh              ← snapshot + publish + git tag
    └── rollback.sh             ← republish a previous theme
```

---

## 6. What MUST never happen

| Forbidden | Why |
|---|---|
| `shopify theme push --theme=$LIVE_ID` | Direct overwrite of live, no rollback path |
| `shopify theme push --allow-live` | Same as above |
| `git push --force` to a remote (if added) | Loses history |
| Editing files directly in Shopify Admin → Edit code | Creates drift between repo and live; the next push will overwrite the user's manual change |
| Committing `.env` | Leaks the Theme Access token |
| Deleting `baselines/` | Loses rollback capability |
| Skipping `git commit` before `push-test.sh` | Decouples Shopify state from git history |
| Pushing without first running `snapshot-live.sh` (if helper bypassed) | No rollback artifact |

---

## 7. When the user says "fix X and push it"

Default sequence:
1. Read the relevant files.
2. Make the smallest change that fixes the problem.
3. `git add` only the files you changed.
4. `git commit -m "fix: <one line>"`.
5. `./scripts/push-test.sh "<slug>"`.
6. Give the user the preview URL and tell them: *"Verify this. If good, run `./scripts/publish.sh <id> <slug>` or tell me to."*
7. **Do NOT publish until the user explicitly says so.** Publishing changes what real customers see.

---

## 8. When working with the Shopify Admin instead of code

Some problems aren't code:
- Apps that inject content (e.g., subscription consent text on PDP — this is an App, not the theme)
- Payment method visibility (Bancontact, Shop Pay Installments — Settings → Payments)
- Email popups (Klaviyo / Privy app install)
- Product descriptions (Shopify product data, not theme code)
- Metafields (Shopify product data, not theme code unless we're scaffolding)

For these: tell the user **exactly where in Admin to click** and what to change. Do not try to "code around" an Admin-side issue.

---

## 9. Recovering from a bad state

| Symptom | Action |
|---|---|
| Local code is wrong, want to revert | `git checkout <file>` or `git reset --hard <commit>` |
| Live theme broken right after publish | `./scripts/rollback.sh <previous-live-id>` |
| Need to see what was on live N days ago | Check `baselines/` directory or `git log` for `baseline:` commits |
| Need to know what code was published last Tuesday | `git tag -l 'published-2026-04-01-*'` then `git show <tag>` |
| `.env` deleted | Recreate from `.env.example`; the user must regenerate the Theme Access token from Apps → Theme Access |
| Working tree is a mess | `git stash`, then triage. Never stash and push. |

---

## 10. Project context (quick brief for new sessions)

- **Brand:** Kinsoul Energy — DTC handmade gemstone & pearl bracelets, $139–$365 AOV
- **Owner:** Chinese-speaking; communicate in Chinese, code/copy in English
- **Stage:** Pre-launch / early traction. Diagnostic report (April 2026) found P0 bugs:
  - P0-1 ✅ Fixed in repo: missing `kinsoul-schema-organization.liquid` snippet → Liquid error
  - P0-2 ⚠️ Admin-side: subscription consent text injected by an App on PDP
  - P0-3 ✅ Fixed in repo: PDP had no review module — added `sections/kinsoul-product-reviews.liquid`
- See `PROJECT-STATUS.md` and `SEO-STATUS.md` for full context.

---

**Remember:** this file is the contract. If a future Claude session is unsure, it should re-read CLAUDE.md before touching anything. Violating these rules has cost the user real money in the past.
