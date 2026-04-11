# 图片 Alt 文案草稿 — Phase 5

**创建时间：** 2026-04-11
**用途：** 为 17 张模板挑选的图片提供可以直接复制粘贴的英文 alt 文案，加上 6 个 PDP 共 36 张 gallery 图的独立 alt 模式。

> ⚠️ **所有 alt 文案保留英文** —— 因为 kinsoulenergy.com 是英文站，alt 给 Google Image Search 和屏幕阅读器读，必须用英文。中文部分只是说明文字。

> **怎么用：** 每行给一个文件名 + 推荐 alt。在 Shopify Admin → **Content** → **Files** 里搜索文件名 → 点击它 → 在 **Alt text** 字段里粘贴 alt → 保存。

---

## 第一部分：模板挑选的图片（17 张，精确 alt 草稿）

这些图片是通过主题编辑器的 image picker 选的；它们在 Files 库里设置的 alt 是主要来源。Phase 1 已经在 liquid 里加了 fallback chain，所以即使 alt 为空也不会出错 —— 但人写的 alt 永远比兜底好。

### 首页（`templates/index.json`）— 6 张

| # | 文件名 | 所在区块 | 推荐英文 Alt |
|---|---|---|---|
| 1 | `2K_202604040701.jpg` | hero（slot 2 主 hero 图） | `Handmade Kinsoul Energy bracelets — natural pearls and gemstones in soft natural light` |
| 2 | `a462ae552c112aea4711b6de9b734fb0.png` | materials_teaser → mat_1（Natural Pearls 卡片） | `Close-up of natural baroque freshwater pearls used in Kinsoul Energy bracelets` |
| 3 | `ac7c941f089f2cc721d9bd5bece2d52b.png` | materials_teaser → mat_2（Gemstones 卡片） | `Hand-selected natural gemstones — agate, amethyst, citrine — Kinsoul Energy materials` |
| 4 | `5c4f9b5fbbab0abc683d4c388f00d027.png` | materials_teaser → mat_3（Sterling Silver 卡片） | `S925 sterling silver components hand-finished for Kinsoul Energy bracelets` |
| 5 | `Meaning.png` | meaning_teaser（背景图） | `Kinsoul Energy bracelet resting on natural materials — quiet stone meaning` |
| 6 | `8697aeb0aa7a4d4d174e88e88760ac56_8d88733a-40f4-4909-8eb9-cba01d5e905e.jpg` | gifting_service（gift popup 图） | `Kinsoul Energy gift box with handwritten note and signature packaging` |

### About 页（`templates/page.about.json`）— 4 张

| # | 文件名 | 所在区块 | 推荐英文 Alt |
|---|---|---|---|
| 7 | `1.png` | origin（Chapter 1 — The Stone） | `LU holding the natural stone she found in China that became Kinsoul Energy's origin story` |
| 8 | `2.png` | shift（Chapter 2 — The Shift） | `Early Kinsoul Energy bracelets being made by hand in LU's studio` |
| 9 | `3.png` | beginning（Chapter 3 — The Beginning） | `LU at her work table designing the first Kinsoul Energy bracelet collection` |
| 10 | `4.png` | today（Chapter 4 — Today） | `The Kinsoul Energy California studio team — five people making jewelry by hand today` |

> **提示：** 这些章节命名（`origin`, `shift`, `beginning`, `today`）来自同步下来的 page.about.json。如果你后来在 admin 里改了章节标题，按图片在页面上的可见顺序对号入座 —— 4 张图按从上到下的顺序渲染。

### Materials 页（`templates/page.materials.json`）— 7 张

| # | 文件名 | 所在区块 | 推荐英文 Alt |
|---|---|---|---|
| 11 | `a462ae552c112aea4711b6de9b734fb0.png` | materials > pearls（block） | `Natural baroque and freshwater pearls — each shaped uniquely by nature for Kinsoul Energy` |
| 12 | `ac7c941f089f2cc721d9bd5bece2d52b.png` | materials > stones（block） | `Hand-selected natural gemstones — agate, amethyst, quartz — preserved in their natural form` |
| 13 | `logo.jpg` | materials > silver（block） | `S925 sterling silver maker's mark bar engraved for Kinsoul Energy bracelets` |
| 14 | `1.jpg` | craft > step_1（Selected by Hand） | `Hands selecting natural gemstones one at a time at the Kinsoul Energy California studio` |
| 15 | `2.jpg` | craft > step_2（Assembled by Hand） | `A Kinsoul Energy bracelet being strung stone by stone, balanced and composed by hand` |
| 16 | `3.jpg` | craft > step_3（Inspected Before Shipping） | `Final inspection of a finished Kinsoul Energy bracelet before it ships to a customer` |
| 17 | `Overhead_photograph_looking_202604060502.jpg` | variation_note（背景） | `Overhead view of multiple Kinsoul Energy bracelets showing natural variation between handmade pieces` |

---

## 第二部分：每个产品的 Gallery Alt 模式（6 PDP × 每个约 6 张）

产品 gallery 图存在 **Products → 各 → Media** —— 它们不在 templates 里。目前所有 6 张 gallery 图共享同一个 alt 文字（产品标题），Phase 0 已经实测确认这一点。

**每个产品的 6 张 gallery 图通常按这个顺序：**
1. 主图（正面、整条手链）
2. 上手图 / 模特图
3. 细节特写（石头）
4. 细节特写（银吧 / 扣 / 珍珠）
5. 包装 / 礼盒图
6. 反面 / 另一个角度

**模板：** `[Product name] — [angle/detail] in [material descriptor]`

### Ember（`persian-red-agate-pearl-sterling-silver-bracelet`）

| 图片 # | 推荐英文 Alt |
|---|---|
| 1 | `Ember bracelet front view — Persian red agate stones with freshwater pearl silver bars` |
| 2 | `Ember bracelet worn on wrist — bold red agate and pearl detail` |
| 3 | `Ember bracelet close-up — translucent Persian red agate stones in natural light` |
| 4 | `Ember bracelet close-up — freshwater pearl silver bar accents` |
| 5 | `Ember bracelet in Kinsoul Energy gift box with authenticity certificate` |
| 6 | `Ember bracelet alternate angle showing S925 sterling silver maker's mark` |

### Aura（`aura-balance-bracelet-baroque-pearl-crystal-mixed-gemstones`）

| 图片 # | 推荐英文 Alt |
|---|---|
| 1 | `Aura bracelet front view — eight natural gemstones with central baroque pearl` |
| 2 | `Aura bracelet worn on wrist — multi-stone arrangement with baroque pearl detail` |
| 3 | `Aura bracelet close-up — red agate, tiger's eye, lapis lazuli, amazonite stones` |
| 4 | `Aura bracelet close-up — large baroque freshwater pearl at the heart of the design` |
| 5 | `Aura bracelet in Kinsoul Energy gift box — Kinsoul's signature multi-stone piece` |
| 6 | `Aura bracelet alternate angle showing the full eight-gemstone composition` |

### Serenity（`freeform-amethyst-bracelet-with-freshwater-pearls`）

| 图片 # | 推荐英文 Alt |
|---|---|
| 1 | `Serenity bracelet front view — freeform amethyst with freshwater spiral pearls` |
| 2 | `Serenity bracelet worn on wrist — soft purple amethyst with cream pearl accents` |
| 3 | `Serenity bracelet close-up — freeform natural amethyst stones in their organic shape` |
| 4 | `Serenity bracelet close-up — freshwater spiral pearls between amethyst stones` |
| 5 | `Serenity bracelet in Kinsoul Energy gift box with authenticity certificate` |
| 6 | `Serenity bracelet alternate angle showing the full amethyst and pearl arrangement` |

### Obsidian（`mozhu-persian-agate-baroque-pearl-bracelet`）

> **重要：** 这条手链的 URL handle 写的是 "persian-agate"，但实际材质是 **black agate + grey rice pearls + baroque pearls**。alt 文字用真实材质，不要用 handle 里的关键词。

| 图片 # | 推荐英文 Alt |
|---|---|
| 1 | `Obsidian bracelet front view — black agate with grey rice pearls and baroque pearl` |
| 2 | `Obsidian bracelet worn on wrist — deep black agate stones with luminous grey pearls` |
| 3 | `Obsidian bracelet close-up — polished black agate stones in their natural depth` |
| 4 | `Obsidian bracelet close-up — grey rice pearls and central baroque freshwater pearl` |
| 5 | `Obsidian bracelet in Kinsoul Energy gift box with authenticity certificate` |
| 6 | `Obsidian bracelet alternate angle with S925 sterling silver maker's mark detail` |

### Terra（`moqiao-black-agate-rutilated-quartz-pearl-bracelet`）

> **重要：** 这条手链的 URL handle 写的是 "black-agate-rutilated-quartz"，但实际材质是 **Persian banded agate + baroque pearl + antiqued silver spacers**。alt 文字用真实材质，不要用 handle 里的关键词。

| 图片 # | 推荐英文 Alt |
|---|---|
| 1 | `Terra bracelet front view — Persian banded agate with baroque pearl and antique silver` |
| 2 | `Terra bracelet worn on wrist — earthy banded agate stones with baroque pearl detail` |
| 3 | `Terra bracelet close-up — natural banded patterns in Persian agate stones` |
| 4 | `Terra bracelet close-up — baroque freshwater pearl with antiqued silver spacers` |
| 5 | `Terra bracelet in Kinsoul Energy gift box with authenticity certificate` |
| 6 | `Terra bracelet alternate angle showing the full earthy banded agate composition` |

### Soleil（`zining-brazilian-yellow-quartz-clear-quartz-amethyst-bracelet`）

| 图片 # | 推荐英文 Alt |
|---|---|
| 1 | `Soleil bracelet front view — Brazilian citrine, clear quartz points, and amethyst rounds` |
| 2 | `Soleil bracelet worn on wrist — warm yellow citrine and clear quartz detail` |
| 3 | `Soleil bracelet close-up — natural Brazilian citrine stones in golden light` |
| 4 | `Soleil bracelet close-up — clear quartz points and round amethyst stones` |
| 5 | `Soleil bracelet in Kinsoul Energy gift box with authenticity certificate` |
| 6 | `Soleil bracelet alternate angle showing the full citrine and quartz arrangement` |

---

## 第三部分：图片质量与性能优化备注

填完 alt 之后，再考虑这些优化（信息性，不阻塞）：

| 图片 | 当前体积 | 建议 |
|---|---|---|
| `Meaning.png` | 3,412 KB | 重新导出为 80% 质量 JPEG，目标 ~300 KB |
| `a462ae552c112aea4711b6de9b734fb0.png`（pearl thumbnail） | 1,296 KB | 重新导出为 80% JPEG，目标 ~150 KB |
| `ac7c941f089f2cc721d9bd5bece2d52b.png`（gemstone thumbnail） | 1,644 KB | 重新导出为 80% JPEG，目标 ~200 KB |

Phase 1 已经让首屏第一张卡片图 eager-load + `fetchpriority="high"`，所以即使在 1.3 MB 的体积下 LCP 影响也已经被缓解。重压缩是 P3 抛光 —— 只有发布后 PageSpeed Insights 还在标记 LCP 的时候才需要做。

---

## 第四部分：本文档不覆盖的部分

下面这些不在本草稿范围内（另外处理）：

- **Klaviyo 弹窗的图片** —— 在 Klaviyo Forms 编辑器里管理，不在 Shopify
- **Footer logo / favicon** —— 已经在主题设置里全局设好
- **Collection 页的产品卡缩略图** —— 这些来自每个产品的主 media 图片，所以 alt 是从产品 gallery 第一张图继承过来的（第二部分的 image #1 已经覆盖）
- **Header 里的 logo** —— 已经有动态 alt `"{shop.name} Home"`（Phase 0 已验证）

---

**草稿 alt 总数：17 张模板图 + 36 张产品 gallery 图 = 53 条独一无二的 alt 可以直接粘贴使用。**

填完后可以在任意页面的开发者工具 console 里跑这段验证代码：
```js
const imgs = document.querySelectorAll('img');
const empty = Array.from(imgs).filter(i => !i.alt || i.alt.trim() === '');
console.log(`${imgs.length - empty.length}/${imgs.length} alt 覆盖率`, empty.length ? '缺失:' : '全部 ✓', empty.map(i => i.src.split('/').pop()));
```

目标：**每个页面 95%+ 的 alt 覆盖率**（允许 1-2 张装饰性图片合理使用空 alt）。
