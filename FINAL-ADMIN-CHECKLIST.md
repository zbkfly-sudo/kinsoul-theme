# 🎯 Kinsoul 全站重设计 — 最终 Admin 操作清单

**测试 Theme**：`fix-2026-04-17-0122-p7-cart-final`（ID **147445907542**）  
**Live Theme**：`147284361302`（未更新）  
**预览链接**：https://qr4xym-qi.myshopify.com/?preview_theme_id=147445907542

这份清单合并了 P1–P7 所有需要在 Shopify Admin 完成的非代码操作。**全部做完 + 预览确认无误后，用 `./scripts/publish.sh 147445907542 "redesign-p1-to-p7"` 发布。**

---

## 🚨 必做（关键解锁功能）

### 1. Klaviyo 弹窗触发 ✅ 已做
（你已确认改成 exit-intent / 45s+70% 滚动，跳过）

### 2. 创建 3 个新页面（P5 解锁 Quiz / Compare / Gifting Guide）

详情见 `ADMIN-TASKS-P5-PAGES.md`。操作约 10 分钟：

| Page Title | URL Handle | Theme Template |
|---|---|---|
| Stone Quiz | `stone-quiz` | `page.quiz` |
| Compare Bracelets | `compare` | `page.compare` |
| Gifting Guide | `gifting-guide` | `page.gifting-guide` |

**如果不创建这些页面**：首页 Quiz 入口、Collection/Gifting Guide 的交叉链接都会 404。

### 3. 配置 6 款产品的 related_products metafield（P2 解锁 Complete Your Look）

详情见 `ADMIN-TASKS-P2-RELATED.md`。操作约 15 分钟：

`Settings → Custom data → Products → Add definition`
- Namespace: `custom`
- Key: `related_products`
- Type: **Product reference (List)**

然后给每款产品填 3 个推荐（配对表见 `ADMIN-TASKS-P2-RELATED.md`）。

**如果不配置**：PDP 的 "Complete Your Look" 区会是空白。

---

## 🎨 增强（提升视觉品质）

### 4. Founder 区上传 LU 工作照（P3 增强）

首页 Founder Lockup 区目前是占位 SVG（平面设计图标）。上传真实照片替换：

- 主题编辑器 → 首页 → 滚到 "Our Founder" 区
- 点 "Founder image" → 上传 LU 工作台或工作室照片
- Save

建议素材：About 页 Chapter 3（`shop_images/3.png`）或 Chapter 5（`shop_images/4.png`）可以复用。

### 5. 为 6 款产品填 `custom.stone_chip` metafield（P3 增强）

产品卡左上角的石头标签目前从 `stone_type` 自动推导，结果偏长（如 "Persian Red Agate"、"Persian Banded Agate"）。可选：填一个更短的 `stone_chip` 字段：

| 产品 | 推荐 chip 文本 |
|---|---|
| Ember | `Red Agate` |
| Serenity | `Amethyst` |
| Aura | `Multi-stone` |
| Obsidian | `Black Agate` |
| Terra | `Banded Agate` |
| Soleil | `Citrine` |

操作：`Settings → Custom data → Products → Add definition`，namespace `custom`，key `stone_chip`，type `Single line text`。然后给每款填值。

### 6. 更改首页次 CTA 链接到 Stone Quiz（配合 #2 解锁后）

Stone Quiz 页创建后，建议把首页 hero 次 CTA 从 "Explore Materials" 改回 "Find Your Stone" 指向 `/pages/stone-quiz`：

- 主题编辑器 → 首页 → Hero 区 → 次按钮
- Label：`Find Your Stone`
- Link：`/pages/stone-quiz`

---

## 🔒 可选（后续优化）

### 7. Judge.me 评价系统（Phase 8+ 推迟）

当品牌积累到 ≥10 条真实客户反馈后再装。现有 "What's in the Box" + "Quick Answers" + "Made by 5 people" Trust Signals 已顶替评价空缺。

### 8. 产品主图换成 close-up（Phase 8+ 推迟）

现在 6 款产品主图都是同一模特的手腕照，辨识度靠石头 chip + 名字 + 价格撑着。后续拍摄/生成独立产品 close-up 图替换主图位。

### 9. Klaviyo Welcome Flow 发首单折扣码

- Klaviyo → Flows → 新建 `Welcome - first subscribe`
- Trigger: 加入 Newsletter list
- 发 email with `10% off` 或 `$20 off $200+` 折扣码

---

## 📋 全站重设计改了什么（速览）

| Phase | 核心内容 |
|---|---|
| P1 | Hero 加价格锚点 / PDP 手风琴默认开 Materials+Size / PDP 移动端首屏压缩 / Klaviyo 触发改（你已做） |
| P2 | PDP 新增 "What's in the Box" 4 卡 + "Quick Answers" 4 问答 / Founder's Note 替代星评 |
| P3 | 首页新增 Best Seller Bar / Trust Signals / 产品卡石头 chip / Founder 重构为图+文 |
| P4 | Collection 移动端 2 列 + "Still deciding" 3 卡 CTA |
| P5 | 新增 Stone Quiz / Compare / Gifting Guide 3 个页面 |
| P6 | About 4 章加产品 CTA / Materials 3 材料卡加 Shop 链 / Materials 新增 9 块 Stone Index |
| P7 | Cart 运费进度条（$200 阈值） |

## ✅ 验证通过的改动

- 8 个核心页面全部 200 OK
- 每页唯一 H1
- Schema 完整（Organization / Product / FAQPage / AboutPage / ContactPage / CollectionPage / WebPage+HowTo）
- PDP：sticky ATC / Founder Note / What's in Box / Quick Answers / 手风琴默认展开全部验证
- Cart 运费进度条：$168 显示差 $32 / $396 显示 "Free shipping unlocked" 双状态验证

## ❌ 尚未验证（需要 Admin 动作解锁后）

- Stone Quiz 页面交互流程（完成 #2 解锁）
- Compare 页表格视觉（完成 #2 解锁）
- Gifting Guide 页布局（完成 #2 解锁）
- Complete Your Look 显示手工推荐产品（完成 #3 解锁）

---

## 🚀 发布流程

**建议顺序**：

1. 做完 #1–#3（必做）
2. 访问预览 `https://qr4xym-qi.myshopify.com/?preview_theme_id=147445907542`
3. 检查新建的 3 个页面
4. 移动端 + 桌面检查所有核心流程
5. 做完 #4–#6（增强）
6. 最后检查一遍
7. `./scripts/publish.sh 147445907542 "redesign-p1-to-p7"`

**发布后**：
- Live theme ID 自动更新到 `.env`
- 旧 live theme 保留作 rollback 用
- Git tag `published-YYYY-MM-DD-HHMM-redesign-p1-to-p7`

**回滚**（如出问题）：
```
./scripts/rollback.sh 147284361302
```
（147284361302 是当前 live theme ID，发布后会被替换）

---

创建时间：2026-04-17  
P1–P7 累计 commit 数：36  
涉及文件：12 新建 + 15 修改（详见 git log）
