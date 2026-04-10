# Kinsoul Energy — Full SEO & GEO Audit Report
**Audit Date:** April 10, 2026
**Domain:** kinsoulenergy.com
**Platform:** Shopify (Cloudflare CDN)
**Business:** DTC handmade gemstone & pearl bracelets, $139-$365

---

## Overall Health Scores

| Category | Score | Weight | Weighted |
|---|---|---|---|
| Technical SEO | 61/100 | 22% | 13.4 |
| Content Quality | 58/100 | 23% | 13.3 |
| On-Page SEO | 45/100 | 20% | 9.0 |
| Schema / Structured Data | 62/100 | 10% | 6.2 |
| Performance (CWV) | 55/100 | 10% | 5.5 |
| AI Search Readiness (GEO) | 38/100 | 10% | 3.8 |
| Images | 78/100 | 5% | 3.9 |
| **TOTAL** | | | **55.1 / 100** |

---

## Executive Summary

### Top 5 Critical Issues
1. **6 of 7 pages missing meta descriptions** — Google generates poor auto-snippets
2. **Organization schema has wrong state: TX instead of CA** — factual error in structured data
3. **Zero customer reviews anywhere on site** — devastating for trust, CTR, and AI citation
4. **GEO score 38/100** — no llms.txt, no YouTube, no blog, no external presence
5. **Materials & Craft page is severely thin** (361 words for deepest expertise page)

### Top 5 Quick Wins
1. Add meta descriptions to all pages (Shopify Admin, 30 min)
2. Fix Organization addressRegion TX → CA (code fix, 5 min)
3. Create llms.txt file (code, 30 min)
4. Add explicit AI crawler allow rules to robots.txt (code, 15 min)
5. Fix homepage title: "Kinsoul Energy" → "Handmade Gemstone Bracelets | Kinsoul Energy"

---

## 1. Technical SEO (61/100)

### Critical
- **Meta descriptions missing** on Homepage, About, Contact, Collection, Client Care, Materials (6/7 pages)
- **Product meta description** is 320 chars with embedded non-breaking spaces — truncated poorly

### High
- Missing `sku` in Product schema — blocks Google Shopping rich results
- 28 render-blocking synchronous scripts in `<head>`
- Homepage title "Kinsoul Energy" has no keyword context
- No `aggregateRating` in Product schema (no reviews)

### Medium
- Duplicate H1 on homepage ("Kinsoul Energy" + "Jewelry Born from the Earth")
- Two crawlable collection URLs (`/collections/all` + `/collections/shop-all-bracelets`) — no canonical
- HSTS max-age 91 days (below 1-year standard)
- Hero image has no preload hint and empty alt text
- No IndexNow implementation
- OG description on homepage is just "Kinsoul Energy"

### What's Working Well
- Full SSR rendering — Googlebot indexes everything without JS
- Canonical tags present and correct on all pages
- HTTPS + HTTP/2 + Cloudflare CDN with early hints
- Responsive images with srcset throughout
- All images have width/height (low CLS risk)
- Product schema has shippingDetails + returnPolicy (above average)

---

## 2. Content Quality & E-E-A-T (58/100)

### E-E-A-T Breakdown
| Dimension | Score | Key Gap |
|---|---|---|
| Experience | 48/100 | No customer voices, no studio/team photos |
| Expertise | 60/100 | Technical accuracy present but no sourcing context |
| Authoritativeness | 42/100 | No press, no awards, no industry associations |
| Trustworthiness | 62/100 | Good policies, but no reviews, no address, no founder surname |

### Thin Content Pages
| Page | Words | Minimum | Status |
|---|---|---|---|
| Homepage | 422 | 500 | THIN |
| Materials & Craft | 361 | 800 | **SEVERELY THIN** |
| Client Care | ~264* | 500 | THIN (*likely undercounted) |
| Contact | 138 | 200 | THIN |
| Collection | 74 | 200 | THIN |

### What's Strong (DO NOT BREAK)
- About page narrative voice — genuine differentiator
- Ember product description — rare sensory specificity
- Per-stone care breakdown on Client Care — expert-level
- Return/shipping policy specificity ("72 hours" refund)
- Overall brand voice — consistent and differentiated

---

## 3. Schema / Structured Data (62/100)

### Critical
- **Organization `foundingLocation.addressRegion` = "TX"** — should be "CA" (California)

### High
- **No `aggregateRating`** on Product schema — no star ratings in Google SERP
- **No `CollectionPage` or `ItemList`** on collection pages — misses carousel rich results
- **Missing `sku`** on Product schema

### Medium
- No `AboutPage` type on About page
- No `ContactPage` type on Contact page
- Thin `Person` entity for founder (only "LU", no surname/jobTitle/description)

### Present & Working Well
- Organization + WebSite schema on all pages
- Product schema with Offer, shippingDetails, returnPolicy
- BreadcrumbList on product/collection pages
- SearchAction for Sitelinks Searchbox
- FAQPage on Client Care (kept for AI citation value, no Google rich results for commercial sites)

---

## 4. Sitemap (72/100)

### High
- `/blogs/新闻` in sitemap but returns 404 — empty blog listing
- 3 collection URLs (`frontpage`, `bracelets`, `shop-all-bracelets`) show same products — no canonicals

### Medium
- Homepage has no `lastmod` date
- All products share identical lastmod timestamp (batch update artifact)
- `/pages/data-sharing-opt-out` in sitemap with no SEO value

### Pass
- All 16 URLs return 200
- robots.txt correctly references sitemap
- XML format valid across all sub-sitemaps

---

## 5. GEO / AI Search Readiness (38/100)

### Platform Scores
| Platform | Score | Key Issue |
|---|---|---|
| Google AI Overviews | 35/100 | No blog, no reviews, thin homepage |
| ChatGPT | 30/100 | No llms.txt, no YouTube, no Wikipedia entity |
| Perplexity | 40/100 | Best — Client Care FAQ + product descriptions |
| Bing Copilot | 38/100 | Missing reviews and external mentions |

### Critical Gaps
1. **No llms.txt file** — missed early-mover advantage
2. **No YouTube presence** — highest correlation with AI citations (~0.737)
3. **No blog content** — zero educational/informational content for AI to cite
4. **No customer reviews** — AI can't answer "is this product good?"
5. **No Reddit presence** — high AI citation impact, absent
6. **No external press/mentions** — brand exists only on own site
7. **Homepage headings are decorative** ("A Quiet Meaning") — invisible to AI parsing

### What's Working
- AI crawlers (GPTBot, PerplexityBot, ClaudeBot) allowed by default via robots.txt
- Server-side rendering — full HTML accessible to AI crawlers
- Product descriptions are near-optimal for citation (134-167 word self-contained passages)
- Client Care FAQ blocks are directly structured for LLM consumption

---

## Priority Action Plan

### Phase 1 — Fix Now (This Week)
| # | Action | Impact | Effort |
|---|---|---|---|
| 1 | Add meta descriptions to all 7 pages | Critical | 30 min (Shopify Admin) |
| 2 | Fix Organization addressRegion TX → CA | Critical | 5 min (code) |
| 3 | Fix homepage title → "Handmade Gemstone Bracelets \| Kinsoul Energy" | High | 5 min (Shopify Admin) |
| 4 | Remove duplicate H1 "Kinsoul Energy" from homepage | High | 15 min (code) |
| 5 | Create llms.txt | Medium | 30 min (code) |
| 6 | Add AI crawler allow rules to robots.txt | Medium | 15 min (code) |
| 7 | Add hero image preload + alt text | Medium | 15 min (code) |
| 8 | Fix Collection canonical (all → shop-all-bracelets) | Medium | 15 min (code) |

### Phase 2 — This Month
| # | Action | Impact | Effort |
|---|---|---|---|
| 9 | Add SKU to Product schema | High | 1 hour (code) |
| 10 | Add CollectionPage + ItemList schema | High | 2 hours (code) |
| 11 | Add AboutPage + expanded Person schema | Medium | 1 hour (code) |
| 12 | Add ContactPage schema | Medium | 30 min (code) |
| 13 | Expand Materials & Craft page to 900+ words | Critical | 3 hours (content) |
| 14 | Add sourcing transparency to product descriptions | High | 2 hours (content) |
| 15 | Add physical address to Contact page | Medium | 5 min |
| 16 | Fix blog: either publish content or remove from sitemap | Medium | 1 hour |

### Phase 3 — Next 60 Days
| # | Action | Impact | Effort |
|---|---|---|---|
| 17 | Install review system (Judge.me/Okendo) + collect real reviews | Very High | Ongoing |
| 18 | Create educational blog (6-8 gemstone articles) | Very High | Ongoing |
| 19 | Create YouTube channel (4-6 short videos) | Very High | 2 days filming |
| 20 | Add "Stone Meanings & Properties" standalone page | High | 3 hours |
| 21 | Expand Collection page editorial content (+200 words) | Medium | 1 hour |
| 22 | Add date/freshness signals to content pages | Low | 30 min |
| 23 | Implement IndexNow for Bing/Yandex | Low | 1 hour |

---

## Projected Impact

If all Phase 1-2 actions completed:
- Technical SEO: 61 → ~78
- Content Quality: 58 → ~68
- Schema: 62 → ~85
- **Overall: 55 → ~72**

If all Phase 1-3 actions completed (including reviews, blog, YouTube):
- GEO: 38 → ~65-70
- Content: 58 → ~80
- **Overall: 55 → ~82**
