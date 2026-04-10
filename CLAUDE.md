# CLAUDE.md — Kinsoul Energy Theme

> **Every session must read this file first.** This is the single source of truth for project rules, brand context, development workflow, and tool usage. No other file is required to start working.

---

## 1. Project & Brand

### 1.1 Repository

- **Path:** `/home/binkai/projects/shopify-theme-redesign/`
- **GitHub:** `zbkfly-sudo/kinsoul-theme` (private)
- **Live store:** `qr4xym-qi.myshopify.com` (domain: `www.kinsoulenergy.com`)
- **Live theme ID:** stored in `.env` as `SHOPIFY_LIVE_THEME_ID` (always read from `.env`, never hard-code)
- **CLI auth:** Theme Access token in `.env` as `SHOPIFY_CLI_THEME_TOKEN`. Never paste tokens into chat, code, or commits.
- **Theme base:** Velora (heavily customized with 11 kinsoul-* sections)

### 1.2 Brand Identity

| | |
|---|---|
| **Brand** | Kinsoul Energy — DTC handmade gemstone & pearl bracelets |
| **Philosophy** | "Natural over perfect" — celebrating natural imperfection |
| **Founder** | LU, designer, started in 2018 after finding a stone during a trip in China |
| **Team** | 5 people, small studio in California |
| **Price range** | $139–$365 |
| **Language** | Communicate in Chinese; code and copy in English |
| **Voice** | Quiet, grounded, specific. No superlatives, no hype, no pseudo-mysticism |
| **Colors** | Warm ivory `#F9F6F1`, accent brown `#7B6B5D`, deep charcoal `#2C2C2C` |
| **Email** | hello@kinsoulenergy.com |
| **Instagram** | instagram.com/kinsoulenergy/ |

### 1.3 Product Line (6 Bracelets)

| Product | Handle | Core Materials | Price |
|---|---|---|---|
| **Ember** | `persian-red-agate-pearl-sterling-silver-bracelet` | Persian red agate + freshwater pearl silver bars | $228 |
| **Serenity** | `freeform-amethyst-bracelet-with-freshwater-pearls` | Freeform amethyst + freshwater pearls | $168 |
| **Aura** | `aura-balance-bracelet-baroque-pearl-crystal-mixed-gemstones` | 8 gemstones + baroque pearl (most complex) | $365 |
| **Obsidian** | `mozhu-persian-agate-baroque-pearl-bracelet` | Black agate + rutilated quartz + grey rice pearls | $208 |
| **Terra** | `moqiao-black-agate-rutilated-quartz-pearl-bracelet` | Persian banded agate + baroque pearl + antique silver | $264 |
| **Soleil** | `zining-brazilian-yellow-quartz-clear-quartz-amethyst-bracelet` | Brazilian citrine + clear quartz + amethyst | $139 |

**Universal construction:** Elastic cord (no clasp), S925 sterling silver maker's mark bar, 4 sizes (S/M/L/XL).

> **Warning:** Obsidian and Terra have URL handles that don't match their actual materials (historical naming error corrected in Admin 2026-04-08, but handles preserved for SEO). Never infer materials from handles.

### 1.4 Page Map

| Page | Handle | Template | Content | Words |
|---|---|---|---|---|
| Homepage | `/` | index.json | Hero + trust strip + product carousel + materials teaser + meaning + founder + gifting + newsletter | ~422 |
| About | `/pages/about` | page.about.json | 4-chapter founder story + brand name origin + belief statement | ~800 |
| Materials | `/pages/materials-craft` | page.materials.json | 3 material deep-dives + 9-stone index + 3-step craft + 4 quality promises + 7 FAQ + variation note | ~1700 |
| Client Care | `/pages/client-care` | page.client-care.json | Authenticity + sizing + shipping + returns + care + contact CTA | ~264 |
| Contact | `/pages/contact` | page.contact.json | 5 quick-link cards + form (7 topics) + sidebar | ~138 |
| Collection | `/collections/shop-all-bracelets` | collection.json | Dynamic title + description + product grid | ~74 |
| Product (PDP) | `/products/[handle]` | product.json | Media gallery + details + variant selector + metafield accordion | dynamic |

### 1.5 Schema Coverage

| Schema Type | Snippet File | Pages | Status |
|---|---|---|---|
| Organization + WebSite | kinsoul-schema-organization.liquid | All | ✅ |
| BreadcrumbList | kinsoul-schema-breadcrumb.liquid | All (except homepage) | ✅ |
| Product (with shipping + returns) | kinsoul-schema-product.liquid | PDP | ✅ |
| FAQPage (client care) | kinsoul-schema-faq.liquid | Client Care | ✅ |
| FAQPage (materials) | inline in kinsoul-materials-faq.liquid | Materials | ✅ |
| CollectionPage + ItemList | kinsoul-schema-collection.liquid | Collections | ✅ |
| AboutPage | kinsoul-schema-about.liquid | About | ✅ |
| ContactPage | kinsoul-schema-contact.liquid | Contact | ✅ |
| WebPage + HowTo | kinsoul-schema-materials.liquid | Materials | ✅ |

### 1.6 Custom Sections (11 kinsoul-* sections)

| Section | Purpose | Used On |
|---|---|---|
| kinsoul-about-story | Narrative chapter with alternating image/text | About (x4) |
| kinsoul-craft-process | 3-step process with images | Materials |
| kinsoul-gifting-service | 4-card service grid | Homepage |
| kinsoul-materials-deep | 3 material profiles with sourcing + product links | Materials |
| kinsoul-materials-faq | 7-question FAQ accordion + FAQPage schema | Materials |
| kinsoul-materials-teaser | 3-card material intro | Homepage |
| kinsoul-meaning-teaser | Full-width hero + CTA | Homepage, Materials |
| kinsoul-newsletter | Email signup | Homepage |
| kinsoul-quality-promise | 4 trust signal cards | Materials |
| kinsoul-stone-guide | 9-stone index grid | Materials |
| kinsoul-trust-strip | 5-icon trust bar | Homepage |

---

## 2. The Four Laws (Deployment Safety)

### Law 1 — Never push directly to the live theme.
- `shopify theme push --theme=$SHOPIFY_LIVE_THEME_ID` is **forbidden**.
- Always push to a **new unpublished test theme** via `./scripts/push-test.sh`.
- The user previews and approves. Then `./scripts/publish.sh` swaps it in.

### Law 2 — Always commit before push.
- Working tree must be clean before any push. `push-test.sh` enforces this.
- Never stash-and-push; pushed code must match a real git commit.

### Law 3 — Always snapshot live before changing live.
- Helper scripts auto-snapshot into `baselines/<timestamp>-<label>/`.
- If bypassing scripts, run `./scripts/snapshot-live.sh <label>` first.

### Law 4 — Every published version is a git tag.
- Published: `published-YYYY-MM-DD-HHMM-<desc>`
- Test: `test-YYYY-MM-DD-HHMM-<desc>`

---

## 3. Development Workflow

### 3.1 Standard Sequence

```
1. git status                              # confirm clean
2. <edit files>
3. git add <specific files>
4. git commit -m "type: description"
5. ./scripts/push-test.sh "short-slug"     # pushes unpublished test theme
6. Verify with Playwright (see Section 4)
7. Give user preview URL
8. DO NOT publish until user explicitly says so
```

### 3.2 Commit Conventions

Format: `type: description`

Types: `feat` / `fix` / `refactor` / `docs` / `infra` / `baseline` / `publish` / `rollback`

### 3.3 Before Changing Code

- Read the target files first. Understand existing patterns.
- Check if a relevant `kinsoul-*` section/snippet already exists (Section 1.6).
- Don't create new files unless necessary — prefer editing existing ones.
- Don't push a new theme when only .md / script / config files changed (Section 8.2).

### 3.4 When to Use Shopify Admin Instead of Code

These are Admin-side, not code fixes:
- Product descriptions, metafields, SEO titles/descriptions
- App-injected content (subscriptions, reviews apps)
- Payment method visibility
- Email popups (Klaviyo/Privy)

Tell the user **exactly where in Admin to click**.

---

## 4. Testing Standards

### 4.1 Verification Checklist (after every push-test, before telling user)

- [ ] Page loads without Liquid errors (Console 0 errors)
- [ ] New content renders correctly, no layout breakage
- [ ] Internal links are clickable and go to correct pages
- [ ] Schema types are complete (Playwright evaluate check)
- [ ] Only one H1 tag on the page
- [ ] Mobile layout not broken (if UI changes involved)

### 4.2 Verification Tool Priority

1. **Playwright** (`browser_navigate` + `browser_evaluate`) — primary verification tool
2. **`/seo-page`** — for SEO-related changes
3. **`/seo-schema`** — for schema changes
4. **WebFetch** — backup, can only see live (not preview themes)

### 4.3 When to Do Before/After Comparison

| Change Type | Compare |
|---|---|
| Content expansion | Word count, H-tag count, internal link count |
| Schema changes | Schema type list before vs after |
| SEO optimization | `/seo-page` scores before vs after |

---

## 5. Documentation Standards

### 5.1 Document Hierarchy

| Layer | Purpose | Examples |
|---|---|---|
| **CLAUDE.md** | Single entry point — rules, brand, workflow, tools | This file |
| **Reference docs** | Specialized data too large for CLAUDE.md | PRODUCT-DESCRIPTIONS.md, PACKAGING-DESIGN-BRIEF.md |
| **Memory system** | Cross-session user/feedback/project memory | ~/.claude/projects/.../memory/ |
| **Git history** | Progress tracking, change history | `git log`, commit messages, tags |

### 5.2 Rules

- New rules and lessons learned → write directly into CLAUDE.md
- Don't create new root-level .md files unless they contain specialized reference data
- CLAUDE.md Section 9 (File Index) must always match actual files
- Don't put in project root: temp plans, session notes, progress trackers, completed work logs

### 5.3 Document Lifecycle

- **Create** only when there's a clear, ongoing reference need
- **Update** when content changes — never leave stale info
- **Delete** when task is done and info is captured in CLAUDE.md / memory / git

---

## 6. Tools & Plugins

### 6.1 Principles

- **Use installed tools.** Don't manually redo what a tool can do.
- **Tools inform decisions.** Don't blindly follow every suggestion.
- **New tools get documented.** When user installs a new plugin: evaluate capabilities → define triggers → add to this section → update affected workflows.

### 6.2 Installed Tools

#### SEO Suite

| Tool | What It Does | When to Use |
|---|---|---|
| `/seo-page` | Single-page deep SEO analysis | Before + after any content/meta/schema change |
| `/seo-content` | E-E-A-T, readability, thin content detection | Before + after content expansion |
| `/seo-schema` | Schema detection, validation, generation | Any schema change |
| `/seo-geo` | AI search visibility (GEO) analysis | Content optimization — assess AI citability |
| `/seo-dataforseo` | Keyword volume, difficulty, intent | New content planning (**keyword selection must have data**) |
| `/seo-plan` | SEO strategy planning | Before major SEO initiatives |
| `/seo-technical` | Technical SEO audit (crawl, index, CWV) | Canonical/robots/rendering issues |
| `/seo-audit` | Full-site crawl audit | Quarterly or after major redesign |
| `/seo-images` | Image alt text, size, format audit | After bulk image uploads |
| `/seo-sitemap` | Sitemap validation/generation | After URL structure changes |

#### Development

| Tool | What It Does | When to Use |
|---|---|---|
| `/code-review` | Code review a PR | Before merging major changes |
| `/frontend-design` | UI/UX design + implementation | New pages or components |
| Playwright | Browser automation + page verification | After every push-test |

#### Content & Research

| Tool | What It Does | When to Use |
|---|---|---|
| WebSearch | Web research for facts and data | When content needs authoritative data |
| WebFetch | Fetch and analyze web page content | Competitor analysis, live page checks |
| `/ultraplan` | Remote planning with web UI | Complex tasks needing independent planning |

### 6.3 New Tool Onboarding

When user installs a new plugin/MCP tool:
1. Understand its capabilities
2. Identify overlap with existing workflows
3. Define usage triggers and scenarios
4. Add to Section 6.2 table
5. If it changes an existing workflow, update that section too

---

## 7. SEO Workflow

**Trigger:** Changes to content, schema, meta tags, page structure, or new pages. Skip for pure CSS/UI/performance changes.

### Phase 1: Diagnose (before coding)

```
/seo-page <target URL>          → on-page score, missing elements
/seo-content <target URL>       → E-E-A-T score, readability, depth
/seo-schema <target URL>        → existing schema, missing types
/seo-geo <target URL>           → AI citation readiness
/seo-dataforseo                 → keyword volumes (for new content)
```

**Output:** Problem list + quantified baseline scores.

### Phase 2: Design

Based on diagnostic data, design the optimization. `/seo-plan` can assist. Plan must include:
- Target keywords (with search volume data — no guessing)
- Content structure (heading hierarchy, word count target, internal link plan)
- Schema types to add/modify
- GEO optimization points (citable passages, statistics, authoritative sources)

### Phase 3: Implement

Code the changes. Use `/seo-schema` to generate JSON-LD when needed.

### Phase 4: Verify (after push-test)

Re-run diagnostic tools on the **preview URL**:

```
/seo-page <preview URL>         → confirm all scores improved
/seo-schema <preview URL>       → validate schema, no errors
/seo-content <preview URL>      → confirm E-E-A-T improvement
```

**Output:** Before/After comparison table.

### Notes

- Ignore HowTo and FAQ **Rich Results** suggestions from tools (deprecated/restricted by Google for commercial sites). But FAQPage schema is still valuable for AI citation — add it.
- Keyword selection **must** have `/seo-dataforseo` volume data. No gut-feel keyword choices.
- Record Before/After data in the commit message.

---

## 8. Lessons Learned (Real Cases)

### 8.1 Verify symptoms before fixing

Third-party reports produce false positives. Before fixing anything:
1. Reproduce the symptom yourself (incognito browser or DevTools)
2. Check if the element is hidden (`visually-hidden`, `aria-hidden`, `display:none`)
3. If hidden → the report is wrong, don't "fix" it

**Case:** April 2026 report flagged "subscription consent text" as P0. It was inside `<small class="hidden" aria-hidden="true">` — Shopify's standard pre-rendered element. The "fix" would have been noise.

### 8.2 Don't push when you can publish an existing test theme

If only .md / script / .gitignore files changed since the last verified test theme, publish the existing theme directly. Don't waste a push.

### 8.3 Ground-truth from photos, never from names

Material claims must trace to product photos or owner confirmation. Never infer materials from product names or URL handles.

**Case:** "Obsidian" and "Terra" were mapped to the wrong physical products for weeks. Six layers of documentation inherited the error because each copied from the previous — none verified against the actual photos.

### 8.4 Admin-side problems need Admin-side solutions

Don't code around issues that belong in Shopify Admin (apps, payment settings, product data, metafields). Tell the user exactly where to click.

---

## 9. File Index

### Theme Code
`assets/` `blocks/` `config/` `layout/` `locales/` `sections/` `snippets/` `templates/`

### Reference Documents

| File | Purpose |
|---|---|
| `PRODUCT-DESCRIPTIONS.md` | 6 product PDP copy (v2, corrected) |
| `STONE-MEANING-CARDS.md` | Printed card designs + typography specs |
| `PRODUCT-CARE-NOTES.md` | Per-material care metafield copy |
| `METAFIELDS-SETUP.md` | 7 metafield definitions + fill guidance |
| `AI-IMAGE-PROMPTS.md` | 16 image generation prompts (Midjourney + Nano Banana) |
| `PACKAGING-DESIGN-BRIEF.md` | Box/card/pouch physical specs |
| `PACKAGING-IMAGE-PROMPTS.md` | 7 packaging scene prompts |
| `SEO-GEO-AUDIT-2026-04-10.md` | SEO baseline audit (55.1/100 overall) |
| `SEO-META-DESCRIPTIONS.md` | Title/meta copy for all pages |

### Operations
- `.env` — secrets (gitignored)
- `scripts/` — push-test.sh, publish.sh, rollback.sh, snapshot-live.sh, sync-from-live.sh
- `baselines/` — rollback snapshots (gitignored)

---

## 10. New Session Checklist

```
1. Read this file (CLAUDE.md)
2. git log --oneline -10               → recent changes
3. source .env                          → confirm env vars loaded
4. If SEO work → /seo-page <url>       → get baseline
5. If content work → /seo-content <url> → get E-E-A-T score
6. If unsure about project state → check memory system
```

---

**This file is the contract.** If unsure, re-read before touching anything.
