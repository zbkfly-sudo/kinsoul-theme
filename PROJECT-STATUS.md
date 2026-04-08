# Kinsoul Energy — Shopify 主题重设计 项目状态

> 最后更新：2026-04-06

## 一、项目概述

Kinsoul Energy 珠宝品牌的 Shopify 主题全面重设计。围绕 6 款手链（Ember / Serenity / Aura / Obsidian / Terra / Soleil），重塑首页、品牌故事、材料、护理、联系、客评、包装等全链路体验。

**品牌调性：** 温暖、教育型、真实无伪装、强调天然而非完美。

---

## 二、文档清单

| 文档 | 作用 |
|---|---|
| `AI-IMAGE-PROMPTS.md` | 16 套 Midjourney V8 生图提示词（首页 Hero / Materials / About / 模特 / 包装） |
| `PACKAGING-DESIGN-BRIEF.md` | 包装系统设计：天地盖礼盒、内衬、寓意卡、护理卡、收纳袋、邮寄防护 |
| `PACKAGING-IMAGE-PROMPTS.md` | 7 套 Google Nano Banana 2 包装场景生图提示词 |
| `STONE-MEANING-CARDS.md` | 6 款手链寓意卡文案 + 排版规范（字体、纸张、色彩） |
| `PRODUCT-CARE-NOTES.md` | 6 款手链定制护理指南，匹配各石材特性 |
| `METAFIELDS-SETUP.md` | Shopify metafield 字段清单（6 必建 + 4 可选）+ 6 款产品填写建议 |
| `REVIEW-SYSTEM.md` | 20 条客评文案 + 配套手腕生图 prompt + 多样性配比表 |

---

## 三、主题结构

```
shopify-theme-redesign/
├── sections/        51 个（含 8 个 kinsoul-* 定制板块）
├── snippets/        145 个
├── templates/       15 个（首页/About/Materials/ClientCare/Contact/Product 等已定制）
├── blocks/          2 个
├── config/          settings_schema.json (53KB) + settings_data.json
├── assets/          180+ 文件（kinsoul-custom.css 2274 行 / 50+ JS / SVG 图标）
└── layout/          theme.liquid + password.liquid
```

### Kinsoul 定制 Sections
- `kinsoul-about-story.liquid` — About 故事章节
- `kinsoul-craft-process.liquid` — Materials 工艺 3 步
- `kinsoul-materials-teaser.liquid` — 三大材料卡片
- `kinsoul-meaning-teaser.liquid` — 寓意背景介绍
- `kinsoul-social-proof.liquid` — 客评轮播（图文 + 星级 + 自动播放 + 触屏滑动）
- `kinsoul-gifting-service.liquid` — 礼物服务
- `kinsoul-newsletter.liquid` — 邮件订阅
- `kinsoul-trust-strip.liquid` — 信任带状条

---

## 四、各模块完成度

### ✅ 已完成（80–95%）

| 模块 | 完成度 | 说明 |
|---|---|---|
| 首页 Hero | 95% | "Jewelry Born from the Earth" + 双 CTA + 渐变遮罩 |
| About 故事页 | 90% | 4 章故事结构、图文反转布局、引用样式 |
| Materials 页 | 85% | 三大材料卡 + 工艺 3 步 + 天然差异说明 |
| Client Care 中心 | 90% | 4 大模块（购前/运费/退货/护理）+ FAQ + 材料知识库 |
| Contact 页 | 90% | 表单（topic/order number 等字段）+ 快速问题导航 + 信息侧栏 |
| Product 页 | 80% | 媒体库 + 详情 + 推荐 + 护理手风琴框架 |
| 客评轮播 Section | 100% | 代码完整：图文布局、星级、箭头、圆点、自动播放、触屏 |
| 客评 20 条文案 | 100% | REVIEW-SYSTEM.md 全部撰写完毕 |
| Metafield 架构 | 100% | 字段定义完成（数据填充未做） |
| 自定义 CSS 体系 | 100% | kinsoul-custom.css 2274 行，色彩/字体/响应式齐备 |

### 🔄 进行中

| 模块 | 完成度 | 待办 |
|---|---|---|
| 客评系统上线 | 20% | 首页只挂了 3 条 preset 占位 block，无图；需替换为 20 条真实数据 + 上传图片 |
| 评论图片生成 | 0% | 20 张手腕底图待用 Nano Banana 2 生成，再合成产品手链 |
| 包装设计细节 | 60% | 7 套包装图待生成 |
| 产品 metafield 数据 | 50% | 6 款产品逐个填写 stone/pearl/metal 字段 |
| 护理卡 / 寓意卡印刷文件 | 40% | 排版定稿 → 出印刷文件 |
| 商品页评论区 | 0% | product.json 尚未挂载客评 section |

### ⏳ 未开始

- Midjourney 16 套产品 + lifestyle 图生成
- Nano Banana 2 7 套包装场景图生成
- 包装第一版打样
- 品牌故事录音 / 视频（可选）

---

## 五、客评系统现状（重点）

**文案** ✅ 20 条全部就绪（REVIEW-SYSTEM.md）
**Section 代码** ✅ kinsoul-social-proof.liquid 完整可用
**首页挂载** 🔄 仅 3 条 preset 占位，全部无图，作者非真实数据
**商品页挂载** ❌ 未挂载
**图片素材** ❌ 0/20 已生成

**评分分布：** 14 ★★★★★ + 6 ★★★★
**产品覆盖：** Ember 4 / Serenity 4 / Aura 3 / Obsidian 3 / Terra 3 / Soleil 3
**肤色覆盖：** 浅 6 / 中 6 / 深 4 / 亚 2 / 年长 2

### 客评系统下一步
1. **批量生成 20 张手腕底图**（Nano Banana 2，手腕完全为空）
2. **后期合成产品手链上手图**
3. **将 20 条数据写入 templates/index.json**（替换 3 条占位 + 关联图片）
4. **决定商品页方案**：是否扩展 section 支持按产品筛选评论后挂到 product.json

---

## 六、后续优先级

### 紧急（本周）
1. 客评系统 20 张图片生成 + 合成
2. Midjourney 16 套产品/lifestyle 图
3. Nano Banana 2 7 套包装图
4. product.json 护理手风琴关联 metafield

### 重要（本月）
1. 6 款产品 metafield 数据填充
2. 护理卡 & 寓意卡印刷文件输出
3. 包装第一版打样
4. 全页面发布前测试

### 优化（2-3 周后）
1. 首页热力图分析 + CTA 转化优化
2. 客评轮播 A/B 测试
3. Unboxing 视频制作

---

## 七、已知技术债

- `page.client-care.json`（17KB）过于庞大，可拆分为多个 custom-liquid sections
- `kinsoul-custom.css` 与 section 内 stylesheet 存在样式重复
- `puraperla-custom.css` 是旧品牌遗留，可清理
- 客评 section 当前未支持按产品筛选（商品页落地需要扩展）
