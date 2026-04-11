# Admin Tasks — Phase 5 (Kinsoul SEO/GEO Comprehensive Fix)

**Created:** 2026-04-11
**Source:** BASELINE-2026-04-11.md (Playwright real-state measurement)
**Audience:** LU (Kinsoul founder) — these tasks must be done in **Shopify Admin / Klaviyo Forms / GSC**, not in code.

> **Most important note:** Items marked **🎯 P0** are blocking the full benefit of the Phase 1 + Phase 3 code fixes already in test theme `147283378262`. The earlier you finish them, the sooner the test theme can be published with full impact.

---

## 🎯 P0 — Critical (Do Today)

### 1. Fix the Klaviyo email popup `<h1>` (affects ALL 7 pages)

**Why:** Phase 0 measurement found that the "Join Our Kinsoul Family" heading injected by the Klaviyo email popup is wrapped in a semantic `<h1>` tag. This is a 2nd `<h1>` on every single page of the site (homepage, about, materials, client-care, contact, collection, every PDP). Theme code cannot fix this — Klaviyo injects the form HTML at runtime via external script.

**Click path:**
1. Sign in to **Klaviyo** (https://www.klaviyo.com/)
2. **Sign-up Forms** → find your active popup form (the one rendering on kinsoulenergy.com — it's `klaviyo-form klaviyo-form-version-cid_1`)
3. **Edit Form** → click the heading block "Join Our Kinsoul Family"
4. In the rich-text toolbar, change the heading style from **H1** to **H2** (or **Paragraph** if you don't want it counted as a heading at all)
5. **Save** + **Publish**

**Verification:** Reload kinsoulenergy.com in incognito → DevTools → run `document.querySelectorAll('h1').length` — should drop from 2 to 1 on every page.

**Alternative:** If you don't actively use this popup for conversions, the cleanest fix is to **deactivate the form entirely** in Klaviyo. Removes 1 H1 + 1 ~50KB external JS file across the whole site.

---

### 2. Fix Terra / Obsidian product price swap

**Why:** The two products' admin variant prices are swapped. Phase 0 verified:

| Product (URL handle) | Schema price (admin variant) | Should be (per CLAUDE.md) |
|---|---|---|
| `mozhu-persian-agate-baroque-pearl-bracelet` (Obsidian) | $264 ❌ | $208 |
| `moqiao-black-agate-rutilated-quartz-pearl-bracelet` (Terra) | $208 ❌ | $264 |

**Click path:**
1. Shopify Admin → **Products**
2. Open **"Obsidian | Black Agate & Grey Pearl Bracelet"** → variants section → change all variant prices from $264 to **$208**
3. Open **"Terra | Banded Agate & Baroque Pearl Bracelet"** → variants section → change all variant prices from $208 to **$264**
4. **Save** both

**Verification:** Reload each PDP → DevTools → `document.querySelector('script[type="application/ld+json"]')` and confirm `offers.price` matches CLAUDE.md.

**Bonus check:** Look at the visible UI price on each PDP after saving. Phase 0 caught $228 from a related-product card via a generic selector — please confirm the **main hero price** on the Obsidian and Terra PDPs is correct, not just the schema.

---

### 3. Shorten Materials page SEO title

**Why:** Current admin SEO title is so long (88 chars) that Shopify auto-truncates and appends " – Kinsoul Energy", resulting in `"Materials & Craft — Natural Pearls, Gemstones & Sterling Silver | Kins – Kinsoul Energy"` — note the dangling **"Kins"** in browser tabs and Google SERPs.

**Click path:**
1. Shopify Admin → **Online Store** → **Pages** → **Materials & Craft**
2. Scroll to **Search engine listing** → **Edit website SEO**
3. Change the **Page title** to one of these (all under 60 chars):
   - `Materials & Craft — Natural Pearls & Gemstones | Kinsoul`
   - `Materials & Craft — Hand-Selected Stones & Pearls`
   - `Natural Pearls, Gemstones & S925 Silver — Kinsoul Craft`
4. **Save**

**Verification:** Reload `/pages/materials-craft` → `document.title` should not contain "Kins".

---

## ⚠️ P1 — High Priority (Do This Week)

### 4. Fill image alt text for 17 template-managed images

**Source:** See `IMAGE-ALT-DRAFT-2026-04-11.md` for ready-to-paste alt text per filename.

**Why:** Phase 1 added defensive alt fallback chains in liquid sections — so even if you do nothing, alt text will fall back to section/block titles. But **product photos and hero images deserve hand-written alt text** for image SEO and accessibility. The drafts in IMAGE-ALT-DRAFT-2026-04-11.md cover the 17 template-picked images. The remaining images come from product gallery (admin), Files library, and Klaviyo (out of theme scope).

**Click path:**
1. Shopify Admin → **Content** → **Files**
2. For each filename in IMAGE-ALT-DRAFT-2026-04-11.md, find the file (use the search box)
3. Click the file → in the right panel, **Alt text** field → paste the recommended alt
4. Click out / **Save**

---

### 5. Fill product gallery alt text (6 PDPs × ~6 images each)

**Why:** Phase 0 measured PDP Ember and found all 6 gallery images share the **same alt text** (`"Ember | Red Agate & Pearl Silver Bar Bracelet"`). Each gallery image is a different angle (front, wrist-on, detail, packaging) and should have a unique descriptive alt for Google Image Search.

**Click path:**
1. Shopify Admin → **Products** → open each of the 6 products
2. **Media** section → click each image → **Edit alt text**
3. Use the suggested alt patterns from `IMAGE-ALT-DRAFT-2026-04-11.md` (see "Per-Product Gallery Alt Patterns" section)

---

### 6. Fill About page content (so AboutPage schema description renders)

**Why:** Phase 0 measured the AboutPage JSON-LD on `/pages/about` — its `description` field is **empty**. The liquid snippet conditionally skips it because admin `page.content` is blank. The visible page content lives in `custom_liquid` blocks, not the body field.

**Click path:**
1. Shopify Admin → **Online Store** → **Pages** → **About**
2. In the **Content** rich-text editor (the body field, not the section editor), paste a clean text version of the visible story:

```
Kinsoul Energy is a California jewelry studio founded in 2018 by LU, a designer who began making bracelets after finding a stone on the ground during a trip in China. What started as a single bracelet became a small studio of five people working by hand. Every piece is made one at a time, from hand-selected gemstones, baroque pearls, and S925 sterling silver. We believe in the quiet authority of natural materials — pieces that don't need to be perfect to feel right.
```

3. **Save**

**Verification:** Reload `/pages/about` → check JSON-LD → AboutPage object should now contain a `description` field.

---

### 7. Phase 3 dependency: Create the `llms-txt` page

**Why:** Phase 3 added `templates/page.llms-txt.liquid` (a layout-less page template). It's a "receiver" — admin must create the actual page that uses it.

**Click path:**
1. Shopify Admin → **Online Store** → **Pages** → **Add page**
2. **Title:** `llms.txt — Kinsoul Energy`
3. **Page** template suffix dropdown (right sidebar) → select **`llms-txt`**
4. **Content:** Click the **Show HTML** button (`<>` icon) to switch to source mode, then **paste the entire contents** of `assets/llms.txt` (60 lines, starts with `# Kinsoul Energy`)
5. **Visibility:** Visible
6. **Save**

The page will be live at `/pages/llms-txt`.

---

### 8. Phase 3 dependency: Create URL redirect `/llms.txt` → `/pages/llms-txt`

**Why:** AI crawlers probe the canonical short URL `/llms.txt`. We just created the page at `/pages/llms-txt`. This redirect bridges the two so crawlers find the file.

**Click path:**
1. Shopify Admin → **Online Store** → **Navigation** → scroll down → **URL redirects** → **Create URL redirect**
2. **Redirect from:** `/llms.txt`
3. **Redirect to:** `/pages/llms-txt`
4. **Save redirect**

**Verification (after publishing the test theme):**
```bash
curl -sL https://kinsoulenergy.com/llms.txt | head -3
# Should print "# Kinsoul Energy" + a short tagline
```

---

### 9. Collection canonical URL redirects (3 handles → 1 canonical)

**Why:** Phase 0 confirmed `/collections/all`, `/collections/bracelets`, and `/collections/shop-all-bracelets` **all return 200** with the same product list. This dilutes PageRank and creates duplicate-content risk. The CLAUDE.md canonical is `shop-all-bracelets`.

**Decision (already approved — Plan Decision 2 = B):** **Add 301 redirects, do NOT delete the underlying collections** (preserves any external links the legacy handles may have).

**Click path:**
1. Shopify Admin → **Online Store** → **Navigation** → **URL redirects** → **Create URL redirect**
2. Add these two redirects:

| Redirect from | Redirect to |
|---|---|
| `/collections/all` | `/collections/shop-all-bracelets` |
| `/collections/bracelets` | `/collections/shop-all-bracelets` |

3. **Save** each

**Verification:**
```bash
curl -sI https://kinsoulenergy.com/collections/all | grep -i "^location"
# Should print: location: /collections/shop-all-bracelets
```

---

## 📋 P2 — Medium Priority (Do This Sprint)

### 10. Delete the empty `/blogs/新闻` Chinese blog

**Why:** Sitemap audit found this empty blog placeholder. Indexable but worthless. Either delete or rename to something useful.

**Click path:**
1. Shopify Admin → **Online Store** → **Blog posts** → **Manage blogs**
2. Find the blog with handle **`新闻`** (Chinese for "News")
3. If no posts → **Delete blog**
4. If you want a blog later → rename handle to `journal` or `notes` (English handle for SEO)

---

### 11. Set `/pages/data-sharing-opt-out` to noindex

**Why:** Sitemap contains this utility page. It's required for CCPA compliance but should not be indexed.

**Click path:**
1. Shopify Admin → **Online Store** → **Pages** → **Data sharing opt out**
2. Scroll to **Search engine listing** → **Edit website SEO**
3. Add to **Page title**: keep as is, but check the page settings — Shopify doesn't have a UI noindex toggle. Workaround: use a meta tag in the page body content:
   ```html
   <meta name="robots" content="noindex, nofollow">
   ```
   (Switch to HTML mode in the editor and add at the very top.)
4. **Save**

**Alternative (cleaner):** Skip if Shopify auto-handles this — the page may already be noindex'd by Shopify default for compliance pages. Verify with `curl -sL https://kinsoulenergy.com/pages/data-sharing-opt-out | grep "robots"`.

---

### 12. Verify GSC property is non-www

**Why:** Canonical URLs across the site use the apex domain (`https://kinsoulenergy.com`, not `https://www.kinsoulenergy.com`). Search Console must be tracking the same property to get accurate data.

**Click path:**
1. Sign in to https://search.google.com/search-console
2. Click the property dropdown (top-left)
3. Confirm the active property is **`https://kinsoulenergy.com/`** (not `www.`)
4. If both exist, the apex one is the source of truth
5. If only the `www` one exists → **Add property** → **URL prefix** → `https://kinsoulenergy.com/` → verify ownership (DNS or Shopify auto-verify)

---

### 13. Console JS errors triage

**Why:** Phase 0 measurement showed multiple pages with JS console errors (homepage 18, materials 17, contact 14, Ember 22, Terra 27). Not blocking SEO but indicates real bugs.

**Click path:**
1. Open `https://kinsoulenergy.com/products/moqiao-black-agate-rutilated-quartz-pearl-bracelet` (Terra — worst with 27 errors) in Chrome
2. F12 → **Console** tab
3. Screenshot or copy the error messages
4. Send to me — I'll triage in a separate session (likely a Velora theme JS issue, third-party script conflict, or missing asset)

**Not a Phase 1-4 deliverable.**

---

## 📚 P3 — Low Priority / Informational

### 14. After publishing: re-verify robots.txt + llms.txt

Once `./scripts/publish.sh 147283378262 "phase1-3-seo-foundation"` runs:
```bash
curl -sL https://kinsoulenergy.com/robots.txt | grep -E "GPTBot|ClaudeBot|PerplexityBot"
# Should show the 11 AI crawler Allow rules

curl -sL https://kinsoulenergy.com/llms.txt | head -5
# Should serve the page content (after admin tasks #7 + #8 done)
```

### 15. After Phase 4 ships: create `custom.faq_json` metafield

This is a future dependency for Phase 4 (Product FAQPage schema). I'll write the click path when Phase 4 lands.

### 16. Materials page large PNG re-compression (if performance still poor)

Three images on Materials page were 1.3-3.4 MB PNGs in the Phase 0 audit:
- `Meaning.png` (3.4 MB)
- `a462ae552c112aea4711b6de9b734fb0.png` (1.3 MB pearl thumbnail)
- `ac7c941f089f2cc721d9bd5bece2d52b.png` (1.6 MB gemstone thumbnail)

If LCP doesn't recover after Phase 1's eager-loading fix, re-export these as high-quality JPEG (target < 300 KB each) and re-upload via Files. Phase 1's fix is necessary but not sufficient for these huge files.

---

## ✅ Summary Checklist

Copy this into your task manager:

- [ ] **P0-1** Klaviyo popup H1 → H2
- [ ] **P0-2** Terra / Obsidian price swap
- [ ] **P0-3** Materials SEO title shorten
- [ ] **P1-4** Fill 17 template image alt (use IMAGE-ALT-DRAFT-2026-04-11.md)
- [ ] **P1-5** Fill 6 PDPs × 6 gallery image alt (per-image)
- [ ] **P1-6** Fill About page body content
- [ ] **P1-7** Create page handle `llms-txt` with template suffix `llms-txt`
- [ ] **P1-8** Create URL redirect `/llms.txt` → `/pages/llms-txt`
- [ ] **P1-9** Add 2 collection URL redirects
- [ ] **P2-10** Delete or rename empty `/blogs/新闻`
- [ ] **P2-11** Set `/pages/data-sharing-opt-out` to noindex (if needed)
- [ ] **P2-12** Verify GSC property = non-www
- [ ] **P2-13** Console JS errors triage (send screenshots to Claude)
- [ ] **P3-14** After publish: verify robots.txt + llms.txt curl
- [ ] **P3-15** Phase 4 future: create `custom.faq_json` metafield (waiting on Claude)
- [ ] **P3-16** Materials big PNG re-compression (if LCP still poor)

---

## When to publish the test theme

After **at least P0-1, P0-2, P0-3** are done (no more dependency on admin), tell me to run:
```bash
./scripts/publish.sh 147283378262 "phase1-3-seo-foundation"
```

And I'll do it. This makes the Phase 1 + Phase 3 code changes go live.

Tasks **P1-7, P1-8, P1-9** depend on the theme being published (or at least: `templates/page.llms-txt.liquid` must exist on the active theme for the page template dropdown to show "llms-txt"). So publish first, then do P1-7 onward.

---

**Questions on any task?** Ping me — I'll explain or adjust.
