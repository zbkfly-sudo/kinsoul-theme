# 管理后台任务清单 — Phase 5（Kinsoul SEO/GEO 全面修复）

**创建时间：** 2026-04-11
**数据来源：** `BASELINE-2026-04-11.md`（Playwright 实测的真实站点状态）
**适用人：** LU（Kinsoul 创始人） —— 这些任务必须在 **Shopify Admin / Klaviyo Forms / Google Search Console** 完成，**不能在代码层修复**。

> **最重要的提醒：** 标记 **🎯 P0** 的项目正在阻塞 Phase 1 + Phase 3 + Phase 4 代码修复的全部生效。**越早完成 P0，发布到 live 的代码改动才能体现完整价值。** 测试主题已经发布到 live，Theme ID `147284361302`。

---

## 🎯 P0 — 严重（今天必须做）

### 1. 修 Klaviyo 邮件弹窗里的 `<h1>`（影响全站 7 个页面）

**为什么必须修：** Phase 0 用 Playwright 实测发现，Klaviyo 邮件弹窗注入的 "Join Our Kinsoul Family" 标题被包在一个 **`<h1>` 语义标签**里。这意味着每一个页面（首页 / About / Materials / Client Care / Contact / Collection / 每一个 PDP）都多了一个第二 H1。**主题代码无法修复这个问题** —— 因为 Klaviyo 是通过运行时外部脚本注入这段 HTML 的。

**操作路径：**
1. 登录 **Klaviyo**：https://www.klaviyo.com/
2. **Sign-up Forms** → 找到当前在 kinsoulenergy.com 上活跃的弹窗（HTML class 是 `klaviyo-form klaviyo-form-version-cid_1`）
3. **Edit Form** → 点击标题块 "Join Our Kinsoul Family"
4. 在富文本工具栏里把样式从 **H1** 改成 **H2**（或者改成 **Paragraph**，这样它根本不算标题）
5. **Save** + **Publish**

**验证方法：** 在隐身窗口打开 kinsoulenergy.com → 开发者工具 Console → 运行 `document.querySelectorAll('h1').length` —— 应该从 2 降到 1（每个页面）。

**替代方案（更彻底）：** 如果这个弹窗本来就没在收订阅，**直接在 Klaviyo 把它停用** —— 一举去掉 1 个 H1 + 一个 ~50KB 的外部 JS 文件（提速）。

---

### 2. 修 Terra / Obsidian 产品价格互换

**为什么必须修：** 这两个产品在 admin 后台的变体价格被反了。Phase 0 实测确认：

| 产品（URL handle） | Schema 价格（admin 变体） | 应该是（按 CLAUDE.md） |
|---|---|---|
| `mozhu-persian-agate-baroque-pearl-bracelet`（Obsidian） | $264 ❌ | **$208** |
| `moqiao-black-agate-rutilated-quartz-pearl-bracelet`（Terra） | $208 ❌ | **$264** |

**操作路径：**
1. Shopify Admin → **Products**
2. 打开 **"Obsidian | Black Agate & Grey Pearl Bracelet"** → variants 部分 → 把所有变体价格从 $264 改为 **$208**
3. 打开 **"Terra | Banded Agate & Baroque Pearl Bracelet"** → variants 部分 → 把所有变体价格从 $208 改为 **$264**
4. 两个都点 **Save**

**验证方法：** 重新加载每个 PDP → 开发者工具 → 运行 `document.querySelector('script[type="application/ld+json"]')` 看 `offers.price` 字段是否符合 CLAUDE.md。

**附加检查：** 改完后看一下两个 PDP 主图区的可见价格。Phase 0 时我用通用选择器抓到 $228，但那可能是 related-product card 上的别人价格。请你 **人眼确认 Obsidian 和 Terra 主标题下面的价格是 $208 / $264** 而不是其他数字。

---

### 3. 缩短 Materials 页 SEO title

**为什么必须修：** 当前 admin 里的 SEO title 太长（88 个字符），Shopify 自动截断后又自动拼接 " – Kinsoul Energy"，结果在浏览器 tab 和 Google 搜索结果里显示成 `"Materials & Craft — Natural Pearls, Gemstones & Sterling Silver | Kins – Kinsoul Energy"` —— 注意结尾那个**断尾的 "Kins"**。

**操作路径：**
1. Shopify Admin → **Online Store** → **Pages** → **Materials & Craft**
2. 滚到 **Search engine listing** → 点 **Edit website SEO**
3. 把 **Page title** 改成下面三个候选之一（都在 60 字符以内）：
   - `Materials & Craft — Natural Pearls & Gemstones | Kinsoul`
   - `Materials & Craft — Hand-Selected Stones & Pearls`
   - `Natural Pearls, Gemstones & S925 Silver — Kinsoul Craft`
4. **Save**

**验证方法：** 重新加载 `/pages/materials-craft` → `document.title` 不应该再含 "Kins"。

---

## ⚠️ P1 — 高优（本周做完）

### 4. 填 17 张模板图片的 alt 文字

**文案来源：** 看 `IMAGE-ALT-DRAFT-2026-04-11-zh.md` —— 已经为每个文件名写好可直接复制的英文 alt 文案。

**为什么必须填：** Phase 1 已经在 liquid section 里加了防御式 alt fallback —— 即便你什么都不做，alt 也会回退到 section/block 的标题文字。但是 **产品照片和 hero 图值得人写的 alt** 来给图片 SEO 和无障碍体验加分。`IMAGE-ALT-DRAFT` 已经覆盖了 17 张模板挑选的图片。其余图片来自产品 gallery（admin）、Files 库和 Klaviyo（不在主题代码范围内）。

**操作路径：**
1. Shopify Admin → **Content** → **Files**
2. 对照 IMAGE-ALT-DRAFT 里的每一个文件名，用搜索框找到那个文件
3. 点击文件 → 右侧面板的 **Alt text** 字段 → 粘贴推荐的英文 alt
4. 点击外部 / **Save**

> ⚠️ 注意：alt 文案保留英文，因为站点是英文站，alt 给 Google Image Search 和屏幕阅读器读，必须用英文。

---

### 5. 填 6 个 PDP × 6 张 gallery 图片的独立 alt 文字

**为什么必须填：** Phase 0 实测 PDP Ember 发现 6 张 gallery 图**全部共享同一个 alt 文字**（都是 `"Ember | Red Agate & Pearl Silver Bar Bracelet"`）。每张 gallery 图是不同的拍摄角度（正面 / 上手 / 细节 / 包装），应该有独立的描述性 alt 给 Google Image Search 用。

**操作路径：**
1. Shopify Admin → **Products** → 打开 6 个产品中的每一个
2. **Media** 部分 → 点击每张图 → **Edit alt text**
3. 用 `IMAGE-ALT-DRAFT-2026-04-11-zh.md` 里 "每个产品 Gallery Alt 模式" 部分的文案

---

### 6. 填 About 页的正文（让 AboutPage schema 的 description 字段不再为空）

**为什么必须填：** Phase 0 实测 `/pages/about` 上的 AboutPage JSON-LD —— 它的 `description` 字段是**空的**。Liquid snippet 是有条件渲染的，因为 admin 里的 `page.content` 字段为空所以跳过了。可见的页面内容是写在 `custom_liquid` 区块里，不是 body 字段。

**操作路径：**
1. Shopify Admin → **Online Store** → **Pages** → **About**
2. 在 **Content** 富文本编辑器（body 字段，不是 section 编辑器），粘贴这段干净的文本版本：

```
Kinsoul Energy is a California jewelry studio founded in 2018 by LU, a designer who began making bracelets after finding a stone on the ground during a trip in China. What started as a single bracelet became a small studio of five people working by hand. Every piece is made one at a time, from hand-selected gemstones, baroque pearls, and S925 sterling silver. We believe in the quiet authority of natural materials — pieces that don't need to be perfect to feel right.
```

3. **Save**

> ⚠️ 这段英文文案不要翻译成中文 —— AboutPage schema 是给 Google 和 AI 搜索引擎读的，必须英文。

**验证方法：** 重新加载 `/pages/about` → 检查 JSON-LD → AboutPage 对象现在应该有 `description` 字段。

---

### 7. Phase 3 依赖任务：创建 `llms-txt` 页面

**为什么必须做：** Phase 3 在主题里加了 `templates/page.llms-txt.liquid`（一个无 layout 的页面模板）。它只是一个"接收方" —— 必须由 admin 创建一个真正使用这个模板的页面。

**操作路径：**
1. Shopify Admin → **Online Store** → **Pages** → **Add page**
2. **Title:** `llms.txt — Kinsoul Energy`
3. 右侧 **Page** 模板下拉框 → 选 **`llms-txt`**（这是新主题发布后才会出现的选项）
4. **Content:** 点 **Show HTML**（`<>` 图标）切换到源码模式，然后**把 `assets/llms.txt` 整个文件的内容粘贴进来**（60 行，开头是 `# Kinsoul Energy`）
5. **Visibility:** Visible
6. **Save**

完成后这个页面会在 `/pages/llms-txt` 上线。

---

### 8. Phase 3 依赖任务：创建 URL 重定向 `/llms.txt` → `/pages/llms-txt`

**为什么必须做：** AI 爬虫会探测规范的短 URL `/llms.txt`。我们刚才在 `/pages/llms-txt` 创建了页面。这个重定向把两者桥接起来，让爬虫能找到文件。

**操作路径：**
1. Shopify Admin → **Online Store** → **Navigation** → 滚到底部 → **URL redirects** → **Create URL redirect**
2. **Redirect from:** `/llms.txt`
3. **Redirect to:** `/pages/llms-txt`
4. **Save redirect**

**验证方法（发布主题之后）：**
```bash
curl -sL https://kinsoulenergy.com/llms.txt | head -3
# 应该输出 "# Kinsoul Energy" + 一行简短描述
```

---

### 9. Collection 规范 URL 重定向（3 个 handle 合并到 1 个规范）

**为什么必须做：** Phase 0 实测确认 `/collections/all`、`/collections/bracelets` 和 `/collections/shop-all-bracelets` **三个 URL 都返回 200**，而且产品列表完全一样。这会稀释 PageRank 并产生重复内容风险。CLAUDE.md 已经规定规范 URL 是 `shop-all-bracelets`。

**决策（已经在计划阶段确认 — 决策 2 选 B）：** **加 301 重定向，不删除底层 collection**（保留任何已建立的外部链接）。

**操作路径：**
1. Shopify Admin → **Online Store** → **Navigation** → **URL redirects** → **Create URL redirect**
2. 添加这两条重定向：

| Redirect from | Redirect to |
|---|---|
| `/collections/all` | `/collections/shop-all-bracelets` |
| `/collections/bracelets` | `/collections/shop-all-bracelets` |

3. 每条都点 **Save**

**验证方法：**
```bash
curl -sI https://kinsoulenergy.com/collections/all | grep -i "^location"
# 应该输出: location: /collections/shop-all-bracelets
```

---

## 📋 P2 — 中等优先（本 sprint 内做）

### 10. 删除空的 `/blogs/新闻` 中文博客

**为什么：** Sitemap 审计发现这个空博客占位符。可被索引但毫无价值。要么删了要么改名成有用的。

**操作路径：**
1. Shopify Admin → **Online Store** → **Blog posts** → **Manage blogs**
2. 找到 handle 为 **`新闻`** 的博客
3. 如果一篇文章都没有 → **Delete blog**
4. 如果以后想要博客 → 把 handle 改成 `journal` 或 `notes`（英文 handle 利于 SEO）

---

### 11. 把 `/pages/data-sharing-opt-out` 设为 noindex

**为什么：** Sitemap 包含这个工具页面。它是 CCPA 合规要求，但不应该被索引。

**操作路径：**
1. Shopify Admin → **Online Store** → **Pages** → **Data sharing opt out**
2. 滚到 **Search engine listing** → 点 **Edit website SEO**
3. Shopify 没有 UI 上的 noindex 开关。变通方案：在页面正文 HTML 模式里加一个 meta 标签：
   ```html
   <meta name="robots" content="noindex, nofollow">
   ```
   （切到编辑器的 HTML 模式，加在最顶部）
4. **Save**

**替代方案（更干净）：** 跳过这一项 —— Shopify 可能默认就给这种合规页面加了 noindex。验证方法：`curl -sL https://kinsoulenergy.com/pages/data-sharing-opt-out | grep "robots"`。

---

### 12. 验证 Google Search Console 属性是 non-www

**为什么：** 全站规范 URL 都用 apex 域名（`https://kinsoulenergy.com`，不是 `https://www.kinsoulenergy.com`）。Search Console 必须跟踪同一个 property 才能拿到准确数据。

**操作路径：**
1. 登录 https://search.google.com/search-console
2. 点左上角 property 下拉
3. 确认当前活跃 property 是 **`https://kinsoulenergy.com/`**（不是 `www.`）
4. 如果两个都存在，apex 那个是事实来源
5. 如果只有 `www` 那个 → **Add property** → **URL prefix** → `https://kinsoulenergy.com/` → 验证 ownership（DNS 或 Shopify 自动验证）

---

### 13. JavaScript Console 报错排查

**为什么：** Phase 0 实测多个页面有 JS console 报错（首页 18，Materials 17，Contact 14，Ember 22，Terra 27）。不阻塞 SEO 但说明确实有 bug。

**操作路径：**
1. 在 Chrome 打开 `https://kinsoulenergy.com/products/moqiao-black-agate-rutilated-quartz-pearl-bracelet`（Terra —— 报错最多，27 个）
2. F12 → **Console** 标签
3. 截图或复制错误信息
4. 发给我 —— 我会在另一个会话里排查（很可能是 Velora 主题的 JS 问题、第三方脚本冲突或缺少资源）

**这不属于 Phase 1-4 的范围。**

---

## 📚 P3 — 低优 / 信息性

### 14. 发布之后：重新验证 robots.txt + llms.txt

`./scripts/publish.sh 147283378262 "phase1-3-foundation"` 跑完之后：
```bash
curl -sL https://kinsoulenergy.com/robots.txt | grep -E "GPTBot|ClaudeBot|PerplexityBot"
# 应该看到 11 个 AI 爬虫的 Allow 规则

curl -sL https://kinsoulenergy.com/llms.txt | head -5
# 应该返回 page content（在 admin 任务 #7 + #8 完成后）
```

### 15. Phase 4 落地之后：创建 `custom.faq_json` metafield

这是 Phase 4（Product FAQPage schema）的未来依赖。Phase 4 落地后我会写具体的操作路径。**目前的 Phase 4 实现已经不需要这个 metafield**（用现有的 `custom.stone_type` / `custom.stone_story` 衍生），所以这条可以暂时忽略。

### 16. Materials 页大 PNG 图重新压缩（如果性能仍差）

Materials 页有三张图在 Phase 0 审计时是 1.3-3.4 MB 的 PNG：
- `Meaning.png` (3.4 MB)
- `a462ae552c112aea4711b6de9b734fb0.png` (1.3 MB pearl thumbnail)
- `ac7c941f089f2cc721d9bd5bece2d52b.png` (1.6 MB gemstone thumbnail)

Phase 1 已经让第一张卡片图 eager-load + `fetchpriority="high"`，所以即使在 1.3 MB 的体积下 LCP 影响也已经被缓解。重新压缩是 P3 抛光 —— 只有发布后 PageSpeed Insights 仍然标记 LCP 才需要做：把这三张图重新导出为 JPEG（80% 质量，目标 < 300 KB），重新上传到 Files。

---

## ✅ 总检查表

复制到你的任务管理器：

- [ ] **P0-1** Klaviyo 弹窗 H1 → H2
- [ ] **P0-2** Terra / Obsidian 价格互换
- [ ] **P0-3** Materials SEO title 缩短
- [ ] **P1-4** 填 17 张模板图 alt（用 IMAGE-ALT-DRAFT-2026-04-11-zh.md）
- [ ] **P1-5** 填 6 PDP × 6 张 gallery 图 alt（每张独立）
- [ ] **P1-6** 填 About 页正文
- [ ] **P1-7** 创建 page handle `llms-txt`，模板后缀选 `llms-txt`
- [ ] **P1-8** 创建 URL 重定向 `/llms.txt` → `/pages/llms-txt`
- [ ] **P1-9** 添加 2 条 collection URL 重定向
- [ ] **P2-10** 删除或重命名空的 `/blogs/新闻`
- [ ] **P2-11** 把 `/pages/data-sharing-opt-out` 设为 noindex（如果需要）
- [ ] **P2-12** 验证 GSC property = non-www
- [ ] **P2-13** Console JS 报错排查（截图发给 Claude）
- [ ] **P3-14** 发布后：验证 robots.txt + llms.txt
- [ ] **P3-15** Phase 4 未来：创建 `custom.faq_json` metafield（已不需要，可忽略）
- [ ] **P3-16** Materials 大 PNG 重压缩（如果 LCP 仍差）

---

## 何时通知 Claude 跑 Final phase

至少完成 **P0-1, P0-2, P0-3** 之后告诉我「**做完了，跑 Final**」，我会立刻跑：

1. Playwright 全站 13 个 URL 重测（7 主页面 + 6 PDP）
2. `/seo-page` `/seo-content` `/seo-geo` `/seo-schema` 全套工具组
3. 生成新审计报告 `SEO-GEO-FULL-AUDIT-2026-04-XX.md`
4. 与 Phase 0 baseline 做 before/after 对比表
5. 写 `CLAUDE.md Section 8.5 防回归规则`

如果 P1-7、P1-8 也做完了，验证报告里能加上"llms.txt 200 + 内容齐全"这一项。

---

**任何任务有疑问？** 直接 ping 我，我帮你解释或调整。
