# Kinsoul Energy — Materials & Craft Page SEO Expansion Plan

**Date:** April 10, 2026
**Branch:** `claude/seo-materials-craft-page-CQE7q`
**Status:** Implemented & Pushed

---

## 1. Background & Diagnosis

### Why This Page Matters

The Materials & Craft page is Kinsoul Energy's **deepest expertise showcase** — the #1 place to demonstrate E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness) to both Google and AI search engines. For a DTC handmade jewelry brand selling $139–$365 bracelets, material transparency and craft storytelling are direct conversion drivers.

### Pre-Optimization State

| Metric | Before | Problem |
|---|---|---|
| **Total word count** | ~361 words | SEO audit flagged as **SEVERELY THIN** (minimum 800+) |
| **Structured data** | 0 types | No WebPage / HowTo / FAQPage schema |
| **Meta description** | Missing | Google auto-generates poor snippets |
| **Internal links** | 1 (CTA → /collections/all) | No cross-links to product pages |
| **E-E-A-T signals** | Weak | No sourcing details, no certifications, no expert voice |
| **FAQ** | None | Missing rich results and AI citation opportunities |
| **Long-tail keywords** | ~2 | "baroque pearl jewelry", "natural gemstone bracelet handmade", etc. absent |

### Content Breakdown (Before)

| Section | Words | Issue |
|---|---|---|
| Intro | ~30 | Too short, no brand background |
| Materials Cards (3×) | ~130 | Each material gets only ~43 words |
| Craft Process (3 steps) | ~180 | Decent but lacks depth |
| Variation Note | ~40 | Conclusion-only, no specific examples |

### SEO Audit Context (April 10, 2026)

- Overall site score: **55.1 / 100**
- Content Quality score: **58 / 100**
- Materials page called out as **Critical action item #13** in Phase 2
- GEO (AI Search Readiness) score: **38 / 100** — thin content is a major factor

---

## 2. Optimization Goals

| Dimension | Target |
|---|---|
| Word count | 361 → **1,400–1,600 words** |
| Structured data | Add **WebPage + HowTo + FAQPage** (3 new schema types) |
| Internal links | 1 → **15+ cross-links** to product pages |
| Long-tail keyword coverage | Cover **12+ high-value search terms** |
| E-E-A-T | Strengthen sourcing transparency, craft expertise, quality promises |
| Rich results eligibility | FAQ snippets (6 Q&A) + HowTo snippet (3 steps) |

---

## 3. New Page Architecture

### Before (4 sections, ~361 words)

```
1. Intro (hero text)
2. Materials Cards (3 thin cards)
3. Craft Process (3 steps)
4. Variation Note (hero + CTA)
```

### After (7 sections, ~1,500 words)

```
┌─────────────────────────────────────────────┐
│  1. INTRO  (expanded)                       │
│     Brand background + material philosophy  │
│     ~100 words                              │
├─────────────────────────────────────────────┤
│  2. MATERIALS DEEP DIVE  ★ NEW             │
│     3 full material profiles with images,   │
│     rich text, and product cross-links      │
│     ~500 words                              │
├─────────────────────────────────────────────┤
│  3. STONE GUIDE  ★ NEW                     │
│     9-stone index grid with traditions      │
│     and product mapping                     │
│     ~100 words                              │
├─────────────────────────────────────────────┤
│  4. CRAFT PROCESS  (expanded)              │
│     3-step workflow, richer descriptions    │
│     ~300 words                              │
├─────────────────────────────────────────────┤
│  5. QUALITY PROMISE  ★ NEW                 │
│     4 trust signal cards                    │
│     ~120 words                              │
├─────────────────────────────────────────────┤
│  6. MATERIALS FAQ  ★ NEW                   │
│     6 Q&A accordion + FAQPage schema        │
│     ~300 words                              │
├─────────────────────────────────────────────┤
│  7. VARIATION NOTE  (expanded)             │
│     Specific examples + stronger CTA        │
│     ~60 words                               │
└─────────────────────────────────────────────┘
```

---

## 4. Section-by-Section Design

### 4.1 Intro — Expanded Brand Context

**Before:** One sentence ("Every material we use is chosen for its natural beauty and authenticity. We don't hide imperfections — we celebrate them.")

**After:** Full paragraph establishing brand credentials:
- Founded 2018, California studio, 5-person team
- "Natural over perfect" philosophy
- Specific material mentions (baroque pearl, amethyst, agate)
- Differentiation from mass-produced jewelry

**Target keywords:** *handmade gemstone bracelets, natural pearl jewelry, California jewelry studio*

---

### 4.2 Materials Deep Dive — ★ New Section

Replaces the 3 thin material cards with 3 full-length material profiles using an alternating image/text layout (same visual language as the Craft Process section).

#### Natural Pearls (~170 words)
- Types used: baroque pearls, freshwater pearls, rice pearls, pearl silver bars
- Why baroque pearls (natural irregular shape = authenticity marker)
- How pearl luster develops naturally (layer by layer inside a mollusk)
- Care tip: pearls thrive when worn close to skin
- **"Found In" product links** → Ember, Serenity, Aura, Obsidian, Terra
- **Target keywords:** *baroque pearl bracelet, freshwater pearl jewelry handmade*

#### Hand-Selected Gemstones (~200 words)
- Full stone inventory: amethyst, Persian red agate, black agate, Persian banded agate, Brazilian citrine, clear quartz, rutilated quartz, tiger's eye, lapis lazuli, amazonite, red jasper
- Hand-cut + minimally polished philosophy
- Specific examples of natural variation (amethyst color range, agate banding, rutilated quartz inclusions)
- Cultural traditions shared honestly (not pseudo-science)
- **"Found In" product links** → all 6 bracelets
- **Target keywords:** *natural gemstone jewelry, hand-cut amethyst bracelet, Persian red agate*

#### S925 Sterling Silver (~130 words)
- S925 grade specification (92.5% pure silver)
- Hand-finishing process
- Components: maker's mark bar, spacers (some with antique finish)
- Natural patina as a feature, not a defect
- Daily wear durability
- **"Found In" product links** → Ember, Aura, Terra
- **Target keywords:** *S925 sterling silver bracelet, hand-finished silver jewelry*

**Section template:** `sections/kinsoul-materials-deep.liquid`
- Alternating image/text layout (2nd profile reverses)
- Each profile has anchor ID for deep linking (`#material-pearls`, `#material-gemstones`, `#material-silver`)
- Product links rendered as small pill-style tags
- Responsive: stacks to single column on mobile

---

### 4.3 Stone Guide — ★ New Section

A quick-reference grid mapping each stone to its tradition and the products it appears in.

| Stone | Tradition | Found In |
|---|---|---|
| Amethyst | Calm, clarity, intuition | Serenity, Soleil, Aura |
| Persian Red Agate | Confidence, vitality, grounding | Ember, Aura |
| Black Agate | Protection, inner resolve | Obsidian, Aura |
| Persian Banded Agate | Stability, earth connection | Terra |
| Brazilian Citrine | Abundance, optimism, creative energy | Soleil |
| Rutilated Quartz | Clarity, focus, illumination | Obsidian |
| Clear Quartz | Clarity, amplification | Soleil, Aura |
| Tiger's Eye | Courage, personal power | Aura |
| Lapis Lazuli | Wisdom, truth, self-awareness | Aura |

**Section template:** `sections/kinsoul-stone-guide.liquid`
- 3-column grid (desktop), 2-column (tablet), 1-column (mobile)
- 1px grid gap creates a clean table-like appearance
- Hover effect on individual cells
- **SEO value:** Targets long-tail queries like "what is banded agate jewelry", "amethyst bracelet meaning"

---

### 4.4 Craft Process — Expanded

Retains the existing 3-step structure but expands each step by ~30 words with more specific details:

| Step | Added Detail |
|---|---|
| 01: Selected by Hand | Founder personally selects materials; evaluates translucency, texture, stone-pearl interaction |
| 02: Assembled One Piece | Color temperature balance (warm vs. cool tones); weight distribution testing; "no assembly line" |
| 03: Checked Before It Leaves | Elastic cord tension verification; paired with meaning card; signature gift box packaging |

Also updated the header description to mention "small team of five."

**Template:** Uses existing `sections/kinsoul-craft-process.liquid` (no code changes needed)

---

### 4.5 Quality Promise — ★ New Section

Four trust-signal cards in a horizontal grid:

| Card | Title | Description |
|---|---|---|
| ◇ | 100% Natural Stones & Pearls | Never synthetic, never lab-created, never coated |
| ◆ | Gemstone Meaning Card | Letterpress-printed on 350gsm cotton paper |
| ○ | Replacement Cord Included | Free spare elastic cord with every order |
| □ | Signature Gift Packaging | Cotton-linen box, microsuede lining, cotton pouch |

**Section template:** `sections/kinsoul-quality-promise.liquid`
- 4-column grid (desktop), 2-column (tablet), 1-column (mobile)
- Subtle border + hover shadow
- Centers on trust and tangible value

---

### 4.6 Materials FAQ — ★ New Section

Six high-frequency questions in an accordion (details/summary) layout:

| # | Question | Key Content |
|---|---|---|
| Q1 | Are your stones and pearls real? | 100% natural, certificate with every piece |
| Q2 | Why does my bracelet look different from the photo? | Natural variation = authenticity, specific stone examples |
| Q3 | What is a baroque pearl? | Definition, why valued, used in Kinsoul bracelets |
| Q4 | How should I care for my gemstone bracelet? | Pearl care, sunlight avoidance, silver polishing, link to Client Care |
| Q5 | Will the sterling silver tarnish? | Natural patina, intentional antique finish, easy restoration |
| Q6 | What cord do you use? Will it break? | Elastic stretch cord, tension-tested, free replacement included |

**Section template:** `sections/kinsoul-materials-faq.liquid`
- Native `<details>` / `<summary>` elements (no JS dependency)
- Chevron icon rotates on open
- **Inline FAQPage schema** (JSON-LD) rendered directly in the section
- CTA at bottom → "Visit Our Client Care Page"

---

### 4.7 Variation Note — Expanded

**Before (40 words):** Generic statement about natural materials varying.

**After (~60 words):** Adds specific, vivid examples:
- "Your amethyst may lean more lavender or more violet"
- "Your baroque pearl will have its own shape"
- "The banding inside your agate is a geological fingerprint that took millions of years to form"
- CTA updated: "Shop the Collection" → `/collections/shop-all-bracelets`

---

## 5. Structured Data Implementation

### 5.1 WebPage Schema

**File:** `snippets/kinsoul-schema-materials.liquid`
**Rendered when:** `page.handle == 'materials-craft'` or `page.handle == 'materials'`

```json
{
  "@type": "WebPage",
  "name": "Materials & Craft | Kinsoul Energy",
  "description": "Learn about the natural baroque pearls, hand-selected gemstones, and S925 sterling silver...",
  "specialty": "Handmade Natural Gemstone & Pearl Jewelry Craftsmanship",
  "mainEntity": [
    { "@type": "Thing", "name": "Natural Baroque & Freshwater Pearls" },
    { "@type": "Thing", "name": "Hand-Selected Natural Gemstones" },
    { "@type": "Thing", "name": "S925 Sterling Silver" }
  ]
}
```

### 5.2 HowTo Schema

Maps directly to the 3-step Craft Process section:

```json
{
  "@type": "HowTo",
  "name": "How Kinsoul Energy Bracelets Are Handmade",
  "step": [
    { "name": "Selected by Hand", "text": "..." },
    { "name": "Assembled One Piece at a Time", "text": "..." },
    { "name": "Inspected Before It Leaves", "text": "..." }
  ],
  "tool": ["Natural gemstones", "Baroque and freshwater pearls", "S925 sterling silver components", "Elastic stretch cord"]
}
```

### 5.3 FAQPage Schema

Embedded inline in `kinsoul-materials-faq.liquid` (not a separate snippet) — renders only when FAQ blocks are present:

```json
{
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Are your stones and pearls real?", "acceptedAnswer": { "@type": "Answer", "text": "..." } },
    // ... 5 more Q&As
  ]
}
```

### 5.4 theme.liquid Integration

Added conditional rendering after the contact schema block:

```liquid
{%- if page.handle == 'materials-craft' or page.handle == 'materials' -%}
  {%- render 'kinsoul-schema-materials' -%}
{%- endif -%}
```

---

## 6. Target Keyword Matrix

| Keyword | Search Intent | Location on Page |
|---|---|---|
| handmade gemstone bracelet | Commercial | Intro, Craft Process |
| natural pearl jewelry | Commercial | Pearls profile, Stone Guide |
| baroque pearl bracelet | Informational/Commercial | Pearls profile, FAQ Q3 |
| S925 sterling silver bracelet | Commercial | Silver profile |
| hand-cut amethyst jewelry | Informational/Commercial | Gemstones profile, Stone Guide |
| Persian red agate bracelet | Informational/Commercial | Gemstones profile, Stone Guide |
| natural gemstone jewelry care | Informational | FAQ Q4, link to Client Care |
| handmade jewelry California | Local/Commercial | Intro, Craft Process |
| what is baroque pearl | Informational | FAQ Q3 |
| gemstone bracelet materials | Informational | Deep Dive (all profiles) |
| banded agate meaning | Informational | Stone Guide, Gemstones profile |
| are gemstone bracelets real | Informational | FAQ Q1 |

---

## 7. Internal Linking Map

```
Materials & Craft Page
│
├── Pearls Profile ──→ Ember (product page)
│                  ──→ Serenity (product page)
│                  ──→ Aura (product page)
│                  ──→ Obsidian (product page)
│                  ──→ Terra (product page)
│
├── Gemstones Profile ──→ Ember
│                     ──→ Serenity
│                     ──→ Aura
│                     ──→ Obsidian
│                     ──→ Terra
│
├── Silver Profile ──→ Ember
│                  ──→ Aura
│                  ──→ Terra
│
├── FAQ Q4 ──→ Client Care Page (/pages/client-care)
│
├── FAQ CTA ──→ Client Care Page (/pages/client-care)
│
└── Variation Note CTA ──→ Collection (/collections/shop-all-bracelets)
```

**Total internal links: 15+** (up from 1)

---

## 8. Files Changed

### New Files (5)

| File | Purpose | Lines |
|---|---|---|
| `sections/kinsoul-materials-deep.liquid` | 3 material profiles with alternating layout + product links | ~230 |
| `sections/kinsoul-stone-guide.liquid` | 9-stone index grid with traditions | ~170 |
| `sections/kinsoul-quality-promise.liquid` | 4 trust signal cards | ~160 |
| `sections/kinsoul-materials-faq.liquid` | 6 Q&A accordion + inline FAQPage schema | ~190 |
| `snippets/kinsoul-schema-materials.liquid` | WebPage + HowTo JSON-LD schema | ~80 |

### Modified Files (2)

| File | Change |
|---|---|
| `templates/page.materials.json` | Restructured from 4 to 7 sections; all content expanded and rewritten |
| `layout/theme.liquid` | Added conditional render for `kinsoul-schema-materials` snippet |

---

## 9. Projected SEO Impact

| Metric | Before | After | Change |
|---|---|---|---|
| Page word count | 361 | ~1,500 | +315% |
| Structured data types | 0 | 3 | WebPage + HowTo + FAQPage |
| Internal links | 1 | 15+ | +1,400% |
| FAQ rich result eligibility | No | Yes (6 Q&A) | New |
| HowTo rich result eligibility | No | Yes (3 steps) | New |
| Long-tail keyword coverage | ~2 | 12+ | +500% |
| E-E-A-T content depth | ~48/100 | ~75/100 (est.) | +56% |
| Site-wide SEO score contribution | — | +4–6 points | ~55 → ~60 |

---

## 10. Remaining Actions (Not in This Implementation)

These items complement the Materials & Craft page but are outside the scope of this code change:

| # | Action | Where |
|---|---|---|
| 1 | Add meta description for Materials page | Shopify Admin → Pages → Materials → SEO |
| 2 | Add meta title: "Materials & Craft — Natural Pearls, Gemstones & Silver | Kinsoul Energy" | Shopify Admin |
| 3 | Upload high-quality material close-up photos for the 3 Deep Dive profiles | Shopify Admin → Files |
| 4 | Verify page handle matches schema conditional (`materials-craft` or `materials`) | Shopify Admin → Pages |
| 5 | Test rich results after deployment | Google Rich Results Test tool |
| 6 | Submit updated page URL to Google Search Console for re-indexing | Google Search Console |

---

## 11. Design Principles Followed

1. **Brand voice consistency** — All new copy matches the existing Kinsoul tone: warm, specific, honest, non-pretentious. No superlatives, no pseudo-mysticism.
2. **CLAUDE.md Rule 7.7** — No material claims were inferred from product names. All stone/pearl descriptions trace to existing verified content (STONE-MEANING-CARDS.md, PRODUCT-CARE-NOTES.md, and product template data).
3. **Visual consistency** — All new sections use the same CSS variable system, font families, spacing conventions, and animation patterns as existing kinsoul-* sections.
4. **Mobile-first responsive** — Every new section gracefully collapses to single-column on mobile with adjusted padding and aspect ratios.
5. **No JS dependencies** — FAQ uses native `<details>`/`<summary>`. Animations use existing `data-kinsoul-reveal` and `data-kinsoul-stagger` patterns.
6. **Schema best practices** — FAQPage schema is inline in the section (renders only when blocks exist). WebPage + HowTo schema is in a separate snippet for clean separation.
