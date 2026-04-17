# 🎯 Kinsoul 全站重设计 — 最终状态

**最终 Test Theme**：`fix-2026-04-17-0223-p7-final-admin-wrapup`（ID **147446693974**）  
**Live Theme**（未更新）：`147284361302`  
**预览链接**：https://qr4xym-qi.myshopify.com/?preview_theme_id=147446693974

---

## ✅ 已全部完成（包括 API 自动化的所有 Admin 操作）

### 代码 + 测试 theme（P1–P7）
- [x] P1 · Kill 最大漏损（Hero 价格锚点 / PDP 手风琴默认开 / 移动首屏压缩）
- [x] P2 · PDP 信任+信息密度（What's in the Box / Quick Answers / Founder's Note）
- [x] P3 · Homepage 转化架构（Trust Signals / Best Seller Bar / Stone Chip / Founder 重构）
- [x] P4 · Collection 页（2 列移动 / Still Deciding CTA）
- [x] P5 · 3 个新页面（Stone Quiz / Compare / Gifting Guide）
- [x] P6 · About + Materials 购物化（章末产品锚点 / Stone Index 9 卡 / material 卡加链）
- [x] P7 · Cart 运费进度条（$200 阈值双状态）

### Shopify Admin 自动化（通过 Custom App + API）
- [x] 创建 3 个 Shopify Page（Stone Quiz / Compare Bracelets / Gifting Guide），绑定对应 theme template
- [x] 定义 `custom.related_products` metafield（list.product_reference）
- [x] 定义 `custom.stone_chip` metafield（single_line_text_field）
- [x] 为 6 款产品填 `stone_chip` 值（Red Agate / Amethyst / Multi-stone / Black Agate / Banded Agate / Citrine）
- [x] 为 6 款产品填 `related_products` 配对值（按 P2 配对表）
- [x] Hero 次 CTA 改回 "Find Your Stone" → `/pages/stone-quiz`
- [x] Founder Lockup 图设为 `shopify://shop_images/about.png`
- [x] PDP Complete Your Look 改为读 `custom.related_products` metafield（精准控制，非 ML 推荐）

### Playwright 验证
- [x] `/pages/stone-quiz` 渲染 + 3 题交互流程 + 推荐引擎打分正确（Warmth+$200-300+Everyday → Ember 主推）
- [x] `/pages/compare` 6 列对比表 + 每列 Shop 链接
- [x] `/pages/gifting-guide` 4 场合卡 + 3 预算层
- [x] PDP Ember Complete Your Look 显示 Obsidian/Terra/Aura（精准匹配配对表）
- [x] PDP Serenity Complete Your Look 显示 Soleil/Ember/Aura（精准）
- [x] PDP Aura Complete Your Look 显示 Ember/Terra/Obsidian（精准）
- [x] Collection 6 卡片全部 stone chip 显示正确
- [x] Cart 运费进度条双状态（<$200 显示差额 / >=$200 显示 Unlocked）
- [x] 所有 schema 保留（Organization / WebSite / Breadcrumb / Product / FAQPage / AboutPage / ContactPage / CollectionPage / WebPage+HowTo）
- [x] 每页唯一 H1
- [x] Hero 次 CTA 点击跳 Quiz

---

## 🔒 唯一剩余的用户侧任务

### Klaviyo H1 修复（见 `ADMIN-TASKS-2026-04-11.md` 第 13 行）

Klaviyo 弹窗的标题 "Join Our Kinsoul Family" 包的是 `<h1>` 标签，导致**每个页面都有 2 个 H1**（SEO 问题）。

**操作**（你自己在 Klaviyo 做，API 无法做）：
1. 登录 Klaviyo → Sign-up Forms
2. 找当前活跃的 popup form
3. Edit → 点 "Join Our Kinsoul Family" 标题块
4. 改 heading 从 **H1** 到 **H2** 或 **Paragraph**
5. Save + Publish

---

## 🎨 可选增强（不影响发布）

### 收紧 Admin API token 权限

目前给 Custom App 勾了 80+ 个 scope，远超实际需要的 3 个。建议：

1. Dev Dashboard → Kinsoul Admin Ops → Configuration → Admin API access scopes
2. **只勾**：`write_products` / `write_content` / `write_files`（以及对应 read）
3. **取消勾选**其它所有（orders/customers/discounts/payments/...）
4. Save → 回 WSL 跑 `python3 scripts/shopify-exchange-token.py` 换新 token

### Phase 8+ 推迟
- Judge.me 评价系统（等攒 ≥10 条真实评价）
- 产品主图换 close-up（需要拍摄新素材）
- Klaviyo Welcome 首单折扣 flow

---

## 🚀 发布流程

### 步骤

1. **你去预览** → 链接 https://qr4xym-qi.myshopify.com/?preview_theme_id=147446693974
2. 过一遍桌面 + 移动（重点：Quiz 交互、Cart 进度条、PDP Complete Your Look、首页 CTA）
3. Klaviyo H1 修掉（可选，但建议发布前做）
4. 发布：
   ```bash
   ./scripts/publish.sh 147446693974 "redesign-p1-to-p7-complete"
   ```

### 回滚预案

如发布后发现问题：
```bash
./scripts/rollback.sh 147284361302  # 回到当前 live theme
```

发布会自动：
- 更新 `.env` 里的 `SHOPIFY_LIVE_THEME_ID`
- 打 git tag `published-YYYY-MM-DD-HHMM-redesign-p1-to-p7-complete`
- snapshot 当前 live 进 `baselines/`

---

## 📊 完成情况总结

| 指标 | 数字 |
|---|---|
| 代码 commit 数 | 40+ |
| 新建/改动文件 | 15 新建 section + 18 修改 |
| 新建页面 | 3 |
| Metafield 定义 | 2 |
| Metafield 值 | 12（6 产品 × 2 字段） |
| 自动化脚本 | 3（exchange-token / admin-setup / list-files） |
| Playwright 验证轮次 | 12+ |
| 验证通过项 | 全部 |

更新时间：2026-04-17 02:30
