# Image Alt Text Drafts — Phase 5

**Created:** 2026-04-11
**Purpose:** Ready-to-paste alt text for the 17 template-managed images, plus per-product gallery alt patterns for the 6 PDPs.

> **How to use:** Each row gives a filename and a recommended alt text. In Shopify Admin → **Content** → **Files**, search for the filename, click it, paste the alt into the **Alt text** field, save. Done.

---

## Section 1: Template-Managed Images (17 files, exact alt drafts)

These images are picked via the theme editor's image picker; the alt set on the file in Files library is the primary source. Phase 1 added liquid fallback chains so even an empty alt won't break — but a hand-written alt is always better for image SEO.

### Homepage (`templates/index.json`) — 6 images

| # | Filename | Section | Recommended Alt |
|---|---|---|---|
| 1 | `2K_202604040701.jpg` | hero (slot 2 — main hero image) | `Handmade Kinsoul Energy bracelets — natural pearls and gemstones in soft natural light` |
| 2 | `a462ae552c112aea4711b6de9b734fb0.png` | materials_teaser → mat_1 (Natural Pearls card) | `Close-up of natural baroque freshwater pearls used in Kinsoul Energy bracelets` |
| 3 | `ac7c941f089f2cc721d9bd5bece2d52b.png` | materials_teaser → mat_2 (Gemstones card) | `Hand-selected natural gemstones — agate, amethyst, citrine — Kinsoul Energy materials` |
| 4 | `5c4f9b5fbbab0abc683d4c388f00d027.png` | materials_teaser → mat_3 (Sterling Silver card) | `S925 sterling silver components hand-finished for Kinsoul Energy bracelets` |
| 5 | `Meaning.png` | meaning_teaser (background image) | `Kinsoul Energy bracelet resting on natural materials — quiet stone meaning` |
| 6 | `8697aeb0aa7a4d4d174e88e88760ac56_8d88733a-40f4-4909-8eb9-cba01d5e905e.jpg` | gifting_service (gift popup image) | `Kinsoul Energy gift box with handwritten note and signature packaging` |

### About page (`templates/page.about.json`) — 4 images

| # | Filename | Section | Recommended Alt |
|---|---|---|---|
| 7 | `1.png` | origin (Chapter 1 — The Stone) | `LU holding the natural stone she found in China that became Kinsoul Energy's origin story` |
| 8 | `2.png` | shift (Chapter 2 — The Shift) | `Early Kinsoul Energy bracelets being made by hand in LU's studio` |
| 9 | `3.png` | beginning (Chapter 3 — The Beginning) | `LU at her work table designing the first Kinsoul Energy bracelet collection` |
| 10 | `4.png` | today (Chapter 4 — Today) | `The Kinsoul Energy California studio team — five people making jewelry by hand today` |

> **Note:** The current chapter section names (`origin`, `shift`, `beginning`, `today`) are from the synced page.about.json. If your About page chapters are titled differently in admin (you may have edited them), pick the alt that matches the visible chapter on your page. The 4 images render in order top-to-bottom.

### Materials page (`templates/page.materials.json`) — 7 images

| # | Filename | Section | Recommended Alt |
|---|---|---|---|
| 11 | `a462ae552c112aea4711b6de9b734fb0.png` | materials > pearls (block) | `Natural baroque and freshwater pearls — each shaped uniquely by nature for Kinsoul Energy` |
| 12 | `ac7c941f089f2cc721d9bd5bece2d52b.png` | materials > stones (block) | `Hand-selected natural gemstones — agate, amethyst, quartz — preserved in their natural form` |
| 13 | `logo.jpg` | materials > silver (block) | `S925 sterling silver maker's mark bar engraved for Kinsoul Energy bracelets` |
| 14 | `1.jpg` | craft > step_1 (Selected by Hand) | `Hands selecting natural gemstones one at a time at the Kinsoul Energy California studio` |
| 15 | `2.jpg` | craft > step_2 (Assembled by Hand) | `A Kinsoul Energy bracelet being strung stone by stone, balanced and composed by hand` |
| 16 | `3.jpg` | craft > step_3 (Inspected Before Shipping) | `Final inspection of a finished Kinsoul Energy bracelet before it ships to a customer` |
| 17 | `Overhead_photograph_looking_202604060502.jpg` | variation_note (background) | `Overhead view of multiple Kinsoul Energy bracelets showing natural variation between handmade pieces` |

---

## Section 2: Per-Product Gallery Alt Patterns (6 PDPs × ~6 images each)

The product gallery images live in **Products → [each product] → Media** — they're not in the templates. Currently all 6 gallery images on each PDP share the same alt text (the product title), which Phase 0 confirmed.

**For each product, the 6 gallery images typically follow this order:**
1. Main hero shot (front, full bracelet)
2. Wrist-on / model shot
3. Detail close-up (stones)
4. Detail close-up (silver bar / clasp / pearl)
5. Packaging / gift box shot
6. Reverse / alternate angle

**Use this template:** `[Product name] — [angle/detail] in [material descriptor]`

### Ember (`persian-red-agate-pearl-sterling-silver-bracelet`)

| Image # | Recommended Alt |
|---|---|
| 1 | `Ember bracelet front view — Persian red agate stones with freshwater pearl silver bars` |
| 2 | `Ember bracelet worn on wrist — bold red agate and pearl detail` |
| 3 | `Ember bracelet close-up — translucent Persian red agate stones in natural light` |
| 4 | `Ember bracelet close-up — freshwater pearl silver bar accents` |
| 5 | `Ember bracelet in Kinsoul Energy gift box with authenticity certificate` |
| 6 | `Ember bracelet alternate angle showing S925 sterling silver maker's mark` |

### Aura (`aura-balance-bracelet-baroque-pearl-crystal-mixed-gemstones`)

| Image # | Recommended Alt |
|---|---|
| 1 | `Aura bracelet front view — eight natural gemstones with central baroque pearl` |
| 2 | `Aura bracelet worn on wrist — multi-stone arrangement with baroque pearl detail` |
| 3 | `Aura bracelet close-up — red agate, tiger's eye, lapis lazuli, amazonite stones` |
| 4 | `Aura bracelet close-up — large baroque freshwater pearl at the heart of the design` |
| 5 | `Aura bracelet in Kinsoul Energy gift box — Kinsoul's signature multi-stone piece` |
| 6 | `Aura bracelet alternate angle showing the full eight-gemstone composition` |

### Serenity (`freeform-amethyst-bracelet-with-freshwater-pearls`)

| Image # | Recommended Alt |
|---|---|
| 1 | `Serenity bracelet front view — freeform amethyst with freshwater spiral pearls` |
| 2 | `Serenity bracelet worn on wrist — soft purple amethyst with cream pearl accents` |
| 3 | `Serenity bracelet close-up — freeform natural amethyst stones in their organic shape` |
| 4 | `Serenity bracelet close-up — freshwater spiral pearls between amethyst stones` |
| 5 | `Serenity bracelet in Kinsoul Energy gift box with authenticity certificate` |
| 6 | `Serenity bracelet alternate angle showing the full amethyst and pearl arrangement` |

### Obsidian (`mozhu-persian-agate-baroque-pearl-bracelet`)

> **Important:** This bracelet's URL handle says "persian-agate" but the actual stones are **black agate + grey rice pearls + baroque pearls**. Use the actual materials in alt text, not the handle.

| Image # | Recommended Alt |
|---|---|
| 1 | `Obsidian bracelet front view — black agate with grey rice pearls and baroque pearl` |
| 2 | `Obsidian bracelet worn on wrist — deep black agate stones with luminous grey pearls` |
| 3 | `Obsidian bracelet close-up — polished black agate stones in their natural depth` |
| 4 | `Obsidian bracelet close-up — grey rice pearls and central baroque freshwater pearl` |
| 5 | `Obsidian bracelet in Kinsoul Energy gift box with authenticity certificate` |
| 6 | `Obsidian bracelet alternate angle with S925 sterling silver maker's mark detail` |

### Terra (`moqiao-black-agate-rutilated-quartz-pearl-bracelet`)

> **Important:** This bracelet's URL handle says "black-agate-rutilated-quartz" but the actual stones are **Persian banded agate + baroque pearl + antiqued silver spacers**. Use the actual materials in alt text, not the handle.

| Image # | Recommended Alt |
|---|---|
| 1 | `Terra bracelet front view — Persian banded agate with baroque pearl and antique silver` |
| 2 | `Terra bracelet worn on wrist — earthy banded agate stones with baroque pearl detail` |
| 3 | `Terra bracelet close-up — natural banded patterns in Persian agate stones` |
| 4 | `Terra bracelet close-up — baroque freshwater pearl with antiqued silver spacers` |
| 5 | `Terra bracelet in Kinsoul Energy gift box with authenticity certificate` |
| 6 | `Terra bracelet alternate angle showing the full earthy banded agate composition` |

### Soleil (`zining-brazilian-yellow-quartz-clear-quartz-amethyst-bracelet`)

| Image # | Recommended Alt |
|---|---|
| 1 | `Soleil bracelet front view — Brazilian citrine, clear quartz points, and amethyst rounds` |
| 2 | `Soleil bracelet worn on wrist — warm yellow citrine and clear quartz detail` |
| 3 | `Soleil bracelet close-up — natural Brazilian citrine stones in golden light` |
| 4 | `Soleil bracelet close-up — clear quartz points and round amethyst stones` |
| 5 | `Soleil bracelet in Kinsoul Energy gift box with authenticity certificate` |
| 6 | `Soleil bracelet alternate angle showing the full citrine and quartz arrangement` |

---

## Section 3: Image Quality & Optimization Notes

After alt text is filled, also consider these optimizations (informational, not blocking):

| Image | Current size | Recommendation |
|---|---|---|
| `Meaning.png` | 3,412 KB | Re-export as JPEG @ 80% quality, ~300 KB target |
| `a462ae552c112aea4711b6de9b734fb0.png` (pearl thumbnail) | 1,296 KB | Re-export as JPEG @ 80%, ~150 KB target |
| `ac7c941f089f2cc721d9bd5bece2d52b.png` (gemstone thumbnail) | 1,644 KB | Re-export as JPEG @ 80%, ~200 KB target |

Phase 1 already made the first card eager-load with `fetchpriority="high"`, so even at the current 1.3 MB the LCP impact is minimized. The re-compression is a P3 polish — only do it if PageSpeed Insights still flags LCP after publishing.

---

## Section 4: What This Doesn't Cover

Out of scope for this draft (handled separately):

- **Klaviyo popup image** — managed in Klaviyo Forms editor, not Shopify
- **Footer logo / favicon** — already set globally via theme settings
- **Product card thumbnail images on collection page** — these come from each product's main media image, so the alt is inherited from the **first** media item in each product's gallery (which Section 2 above covers as image #1)
- **Logo in header** — already has dynamic alt `"{shop.name} Home"` (verified Phase 0)

---

**Total alt text drafts: 17 template files + 36 product gallery images = 53 unique alts ready to paste.**

When done, run this verification in DevTools console on any page:
```js
const imgs = document.querySelectorAll('img');
const empty = Array.from(imgs).filter(i => !i.alt || i.alt.trim() === '');
console.log(`${imgs.length - empty.length}/${imgs.length} alt coverage`, empty.length ? 'missing:' : 'all set ✓', empty.map(i => i.src.split('/').pop()));
```

Target: **95%+ coverage** on every page (allowing for 1-2 decorative images that legitimately use empty alt).
