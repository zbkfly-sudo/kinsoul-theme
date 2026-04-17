# P5 新页面 — Admin 操作清单

**上下文**：P5 新增了 3 个页面（Stone Quiz / Compare / Gifting Guide）。代码层的 template 文件已提交（`templates/page.quiz.json` 等），但 **Shopify 页面本身还需要在 Admin 手动创建** 并绑定对应 template。

## 需要创建的 3 个页面

| Page Title | URL Handle（自动/手填） | Template（选择这个） |
|---|---|---|
| Stone Quiz | `stone-quiz` | `page.quiz` |
| Compare Bracelets | `compare` | `page.compare` |
| Gifting Guide | `gifting-guide` | `page.gifting-guide` |

## 操作步骤

对每个页面重复：

1. Shopify Admin → **Online Store → Pages → Add page**
2. **Title**：填上表 `Page Title`
3. **Content**：可以留空（section 已经有默认文案）；也可以在顶部加一句简短介绍
4. **Search engine listing preview**（右侧 "Search engine listing" 区）：
   - Page title：可用默认（或自定义 SEO 标题）
   - Meta description：写一段具体描述，约 150-160 字符
   - URL and handle：确认 handle 是上表的值（**重要** —— 代码里的链接都是这些）
5. **Online store → Theme template**（右侧栏）：点下拉选 `page.quiz` / `page.compare` / `page.gifting-guide`
6. **Visibility**：Visible
7. **Save**

## 每个页面的 SEO 元数据建议

### Stone Quiz
- Page title: `Find Your Stone — 3-Question Bracelet Quiz | Kinsoul Energy`
- Meta description: `Not sure which Kinsoul bracelet is right for you? Answer 3 short questions about feeling, budget, and occasion — we'll match you to the piece that fits.`

### Compare Bracelets
- Page title: `Compare All 6 Bracelets — Kinsoul Energy`
- Meta description: `Side-by-side comparison of every Kinsoul bracelet: stone, pearl, metal, price, and best worn. Pick the one that fits your wrist and your day.`

### Gifting Guide
- Page title: `Gifting Guide — Kinsoul Bracelets by Occasion & Budget`
- Meta description: `Handmade gemstone + pearl bracelets for birthdays, anniversaries, holidays, and self-gifting. Each piece arrives gift-ready. Under $200 to $365.`

## 验证方式

1. 访问 `https://www.kinsoulenergy.com/pages/stone-quiz` → 应渲染 quiz 问卷（不是 404）
2. 访问 `https://www.kinsoulenergy.com/pages/compare` → 应渲染对比表
3. 访问 `https://www.kinsoulenergy.com/pages/gifting-guide` → 应渲染送礼指南
4. 首页的 hero 次 CTA、Collection 页的 "Take the quiz →" 链接、PDP 的 Gifting 相关链接 应都能跳对

## 可选：把 Quiz 放在首页 Hero 次 CTA

P1 把首页 hero 次 CTA 设为 `Explore Materials` → `/pages/materials-craft`。现在 Quiz 页面上线后，可以考虑改回 `Find Your Stone` → `/pages/stone-quiz`。

改法（在主题编辑器里）：
1. Admin → Online Store → Themes → Customize
2. 首页 hero 区 → 找到 "Find Your Stone" / "Explore Materials" 按钮
3. 改 Label 为 `Find Your Stone`，Link 填 `/pages/stone-quiz`
4. Save

（等你把 Quiz 页面创建好再改。）

---

文件创建时间：2026-04-17
