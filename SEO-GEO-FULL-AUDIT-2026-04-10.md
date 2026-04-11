# Kinsoul Energy SEO & GEO Full Audit Report

**Date:** 2026-04-10
**Auditor:** Claude (11-Phase Automated Audit)
**Domain:** kinsoulenergy.com / www.kinsoulenergy.com
**Previous Audit:** 2026-04-10 baseline (55.1/100)

---

## Executive Summary

| Dimension | Score | Previous | Change |
|-----------|-------|----------|--------|
| **Technical SEO** | 62/100 | 61 | +1 |
| **On-Page SEO** | 38/100 | 45 | -7 |
| **Content Quality (E-E-A-T)** | 64/100 | 58 | +6 |
| **Schema Markup** | 78/100 | 62 | +16 |
| **GEO / AI Visibility** | 56/100 | 38 | +18 |
| **Backlink Profile** | 5/100 | N/A | new |
| **Sitemap** | 82/100 | N/A | new |
| **Keyword Readiness** | 35/100 | N/A | new |
| **OVERALL** | **52.5/100** | 55.1 | -2.6 |

**Why the overall dropped despite improvements:** The On-Page SEO score dropped significantly due to the discovery of **11 H1 tags on the homepage** and **missing meta descriptions on 6/7 pages** — problems that existed before but were now properly measured. Schema and GEO saw real improvement (+16 and +18 respectively). The backlink profile (5/100) is a new measurement that drags down the composite.

---

## P0 Critical Issues (Fix Immediately)

### 1. Homepage has 11 H1 tags (should be 1)
- **Impact:** Severe SEO confusion — Google cannot determine page topic
- **Cause:** Multiple sections use `type_preset: "h1"` in template settings
- **Found:** Phase 2 WebFetch extraction
- **Fix:** Code — change all section headings to H2 except "Jewelry Born from the Earth"
- **Files:** `templates/index.json` — update heading presets for each section

### 2. About page has 3 H1 tags (should be 1)
- **Impact:** Heading hierarchy broken
- **Found:** Phase 2 WebFetch extraction
- **Fix:** Code — keep only "Our Story" or the first H1, demote others to H2
- **Files:** `templates/page.about.json`

### 3. Meta descriptions missing on 6/7 pages
- **Impact:** Google generates random snippets, CTR loss
- **Pages missing:** Homepage, About, Materials, Client Care, Collection, Product
- **Only Contact has one:** "Questions about a piece, a gift, or your order?..."
- **Fix:** Shopify Admin — add meta descriptions (copy in SEO-META-DESCRIPTIONS.md)

### 4. llms.txt returns 404
- **Impact:** AI crawlers cannot find brand guidelines
- **Cause:** File exists in theme assets but not deployed at root `/llms.txt`
- **Found:** Phase 5 GEO audit
- **Fix:** Verify Shopify deployment — the file may need to be at `/llms.txt` not `/assets/llms.txt`

### 5. Terra/Obsidian prices swapped in Shopify Admin
- **Impact:** Wrong prices in Schema, collection, and product pages
- **Found:** Phase 4 Schema validation
- **Detail:** Terra shows $208 (should be $264), Obsidian shows $264 (should be $208)
- **Fix:** Shopify Admin — correct product prices

### 6. Homepage: 34 images with ZERO alt text
- **Impact:** Accessibility failure + missed image SEO
- **Found:** Phase 2 WebFetch extraction
- **Fix:** Shopify Admin — add alt text to all images via media library

---

## P1 High Priority Issues

### 7. Product page images (6+) have no alt text
- **Fix:** Shopify Admin — add descriptive alt to all product images

### 8. Materials page: 6 images with no alt text
- **Fix:** Shopify Admin image settings

### 9. About page: 14/16 images missing alt text
- **Fix:** Shopify Admin image settings

### 10. Backlink profile is effectively zero
- **Total backlinks:** 14 (all nofollow, all from spam domains)
- **Referring domains:** 10 (spam score 47-50 on 9/10)
- **Zero dofollow links, zero keyword anchors**
- **Fix:** Long-term link building strategy (see recommendations)

### 11. No AI crawler declarations in robots.txt
- **Fix:** Add explicit Allow for GPTBot, ClaudeBot, PerplexityBot, OAI-SearchBot

### 12. No FAQPage schema on Product pages
- **Impact:** Missing Bing Copilot product cards and Google AIO shopping results
- **Fix:** Code — add FAQ schema to product template

### 13. Collection page lacks editorial introduction
- **74 words** of indexable content
- **Fix:** Add 150-200 word editorial paragraph above product grid

### 14. Materials page WebPage name has duplicate brand suffix
- `"Materials & Craft — ... | Kinsoul Energy | Kinsoul Energy"`
- **Fix:** Code — `kinsoul-schema-materials.liquid`

### 15. BreadcrumbList names use full page titles (too long)
- Should use short names: "Materials & Craft" not the full title tag
- **Fix:** Code — `kinsoul-schema-breadcrumb.liquid`

---

## P2 Medium Priority Issues

### 16. AboutPage schema missing `description` field
### 17. Client Care page: 11/19 images missing alt text
### 18. Collection has 3 potentially duplicate handles: `/collections/all`, `/collections/bracelets`, `/collections/shop-all-bracelets`
### 19. `/pages/data-sharing-opt-out` in sitemap but should be noindex
### 20. `/blogs/新闻` (Chinese URL) is empty blog placeholder in sitemap
### 21. No customer reviews — zero social proof across all pages
### 22. Collection may display phantom star ratings from deleted review system
### 23. Logo alt text translation error: "Translation missing: en.Kinsoul Energy accessibility.home"
### 24. No blog content — blog template exists but zero posts
### 25. Care instruction H3s on Client Care not in question format (limits FAQ schema eligibility)

---

## P3 Low Priority / Long-term

### 26. No YouTube presence (0.737 correlation with AI citations)
### 27. No Reddit/Wikipedia/press mentions
### 28. HowTo schema on Materials page is deprecated for rich results (but valuable for AI)
### 29. No IndexNow implementation
### 30. Homepage word count borderline (~1850 but inflated by navigation text)
### 31. changefreq in sitemap (Shopify default, cannot fix, ignored by Google)
### 32. www vs non-www: confirm GSC property matches canonical (non-www)

---

## Detailed Phase Results

### Phase 2: On-Page SEO by Page

| Page | Title | Meta Desc | H1 Count | Images Total/Alt | Words |
|------|-------|-----------|----------|-----------------|-------|
| Homepage | "Handmade Gemstone & Pearl Bracelets \| Kinsoul Energy" | MISSING | **11** | 34/0 | ~1850 |
| About | "Our Story — How a Stone in China..." | MISSING | **3** | 16/2 | ~1050 |
| Materials | "Materials & Craft — Natural Pearls..." | MISSING | 1 | 6/0 | ~3000 |
| Client Care | "Client Care — Shipping, Returns..." | MISSING | 1 | 19/8 | ~1850 |
| Contact | "Contact Us — We Read Every Message..." | EXISTS | 1 | 4/4 | ~580 |
| Collection | "Shop All Bracelets – Kinsoul Energy" | MISSING | 1 | 6/6 | ~850 |
| Product Ember | "Ember \| Red Agate & Pearl Silver Bar..." | MISSING | ? | 6/0 | ~450 |

### Phase 3: E-E-A-T Scores

| Page | Experience | Expertise | Authority | Trust | Total |
|------|-----------|-----------|-----------|-------|-------|
| Homepage | 14/20 | 15/25 | 10/25 | 19/30 | 58/100 |
| About | 18/20 | 16/25 | 8/25 | 21/30 | 63/100 |
| Materials | 17/20 | 19/25 | 10/25 | 22/30 | 68/100 |
| Client Care | 12/20 | 15/25 | 7/25 | 22/30 | 56/100 |
| Contact | 10/20 | 8/25 | 7/25 | 24/30 | 49/100 |
| Collection | 8/20 | 8/25 | 10/25 | 16/30 | 42/100 |
| Product Ember | 17/20 | 19/25 | 12/25 | 22/30 | 70/100 |
| **Average** | | | | | **64/100** |

### Phase 4: Schema Validation

| Page | Schemas Found | Status | Issues |
|------|--------------|--------|--------|
| Homepage | Organization + WebSite | PASS | addressRegion=CA correct |
| About | +BreadcrumbList +AboutPage | PASS | Missing description field |
| Materials | +BreadcrumbList +WebPage +HowTo | PASS | Name has double brand suffix; FAQPage inline in section |
| Client Care | +BreadcrumbList +FAQPage(8 Q&A) | PASS | Hardcoded FAQ (sync risk) |
| Contact | +BreadcrumbList +ContactPage | PASS | Clean |
| Collection | +BreadcrumbList +CollectionPage +ItemList(6) | PASS | Terra/Obsidian prices swapped |
| Product | +BreadcrumbList +Product(shipping+returns) | PASS | No aggregateRating, no FAQPage |

**Schema Score: 78/100**

### Phase 5: GEO by Page

| Page | GEO Score | Best For |
|------|----------|---------|
| Materials | 76 | Google AIO, Perplexity (statistics + FAQ) |
| Client Care | 68 | Bing Copilot (FAQPage schema) |
| About | 61 | Entity queries (founder, brand origin) |
| Homepage | 54 | Brand entity signals |
| Product Ember | 52 | Product schema (needs FAQ) |
| Contact | 45 | Minimal GEO value |
| Collection | 41 | Needs editorial content |

**GEO Score: 56/100**

### Phase 8: Backlink Profile

| Metric | Value |
|--------|-------|
| Total backlinks | 14 |
| Referring domains | 10 |
| Dofollow links | 0 |
| Nofollow links | 14 (100%) |
| Domain spam score | 47/100 |
| Referring IPs | 3 |
| Anchor diversity | 0% (only "kinsoulenergy.com") |
| Quality domains | 0 |

**Backlink Score: 5/100** (effectively no backlink profile)

### Phase 10: Sitemap

| Check | Result |
|-------|--------|
| XML valid | PASS |
| Core URLs present | PASS (13/13) |
| All return 200 | PASS |
| robots.txt reference | PASS |
| Duplicate collections | WARNING (3 collection handles) |
| Thin/utility pages | WARNING (data-sharing-opt-out, 新闻 blog) |

**Sitemap Score: 82/100**

### Phase 7: Keyword Opportunities

**Best opportunity keywords (KD < 30):**
- persian red agate bracelet (KD 8)
- red agate bracelet (KD 22)
- gemstone bracelet gift (KD 20)
- sterling silver gemstone bracelet (KD 28)
- baroque pearl bracelet (KD 30)

**Avoid (KD > 55):**
- crystal bracelet (KD 65)
- pearl bracelet (KD 68)
- handmade bracelet (KD 60)

---

## Immediate Action Plan (This Week)

### Code Fixes (push-test required)
1. Fix homepage H1 tags: keep only 1, demote rest to H2
2. Fix About page H1 tags: keep only 1
3. Fix Materials schema double brand name
4. Fix BreadcrumbList to use short names
5. Add AboutPage description field
6. Add FAQPage schema to product template
7. Add AI crawler Allow rules to robots.txt (via Shopify theme)
8. Verify llms.txt deployment path

### Shopify Admin (no code needed)
1. Add meta descriptions to 6 pages (copy in SEO-META-DESCRIPTIONS.md)
2. Fix Terra/Obsidian prices
3. Add alt text to ALL images (priority: homepage 34, product 6, materials 6, about 14)
4. Verify/remove phantom star ratings on collection
5. Fix logo translation key
6. Add collection editorial description (150-200 words)

### 30-Day Plan
- Create 3 blog posts targeting low-KD keywords
- Deploy llms.txt correctly
- Add FAQ schema to all 6 product pages
- Start collecting real customer reviews

### 60-Day Plan
- Create YouTube channel (3-5 short videos)
- Establish Reddit presence
- Build 10+ quality backlinks
- Create Gift Guide page
- Expand Client Care care instructions

---

---

## Phase 9: Image SEO Audit

### Summary by Page

| Page | Total Images | Alt Coverage | Critical Issues |
|------|-------------|-------------|-----------------|
| Homepage | 35 | 77% (27/35) | Hero image alt MISSING (not empty — attribute absent), 3 massive PNGs (up to 3.4MB), 8 empty alt |
| Materials | 16 | 56% (9/16) | 3 above-fold images lazy-loaded (bad for LCP), 7 empty alt, 2 PNGs over 1MB |
| Product Ember | 34 | 94% (32/34) | All 6 gallery images share IDENTICAL alt text, 5 images >200KB, main image 699KB |

### Critical Image Issues

**1. Hero image has no alt attribute at all (Homepage)**
- File: 2K_202604040701.jpg (3840px, 354KB)
- Has correct `loading="eager"` and `fetchpriority="high"` — good
- But alt attribute is completely absent — Google Image Search cannot index it
- Fix: Add descriptive alt text in Shopify Admin

**2. Materials page: 3 above-fold images are lazy-loaded**
- Natural Pearls, Gemstones, Sterling Silver card images = `loading="lazy"`
- These are in the initial viewport and should be `loading="eager"`
- Combined with their massive file sizes (1.3MB + 1.6MB PNG), this severely hurts LCP
- Fix: Code — change loading attribute in kinsoul-materials-deep.liquid or template

**3. Three PNGs are massively oversized**
- Meaning.png: **3,412 KB** (WebP would be 346KB — 10x saving)
- Pearl thumbnail: **1,296 KB** (WebP 113KB)
- Gemstone thumbnail: **1,644 KB** (WebP 218KB)
- Shopify CDN auto-serves WebP to browsers, but crawlers get raw PNG
- Fix: Re-upload as JPEG or add `&format=webp` to srcset URLs

**4. All 6 product gallery images share identical alt text**
- Every image: "Ember | Red Agate & Pearl Silver Bar Bracelet"
- Each shows a different angle — should have unique descriptive alt
- Severely limits Google Image Search visibility
- Fix: Shopify Admin — edit each image's alt individually

**5. Product image logo1_f003d68c...jpg is 699KB**
- At 1600px, should be under 200KB
- Fix: Re-export/compress before re-uploading

**6. No `<link rel="preload">` for LCP images on any page**
- Neither homepage hero nor materials first images have head preload hints
- Fix: Code — add preload link tags in theme.liquid or section files

### What's Working Well
- Responsive srcset on 33/35 homepage images and 33/34 product images
- Width/height attributes on ALL images (no CLS risk)
- Hero fetchpriority="high" + loading="eager" correctly set
- Product JSON-LD includes all 6 gallery image URLs
- Shopify CDN serves WebP via content negotiation (Vary: Accept confirmed)

---

*Report generated by 11-phase automated SEO/GEO audit. All scores are relative assessments based on industry benchmarks for DTC e-commerce in the $100-$400 jewelry category.*
