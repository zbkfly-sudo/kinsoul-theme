# Kinsoul Energy — SEO 工作状态与路线图

> 最后更新：2026-04-07
> 域名：kinsoulenergy.com
> 域名注册：2025-09
> 上线日期：2026-04 初（几天前）
> 法律实体：LuKai Trading LLC（Texas, US）

---

## 一、Google 工具接通状态

| 工具 | 状态 | 备注 |
|---|---|---|
| **Google Search Console** | ✅ 已注册（2025-09）| 用 GA4 验证 |
| **Google Analytics 4** | ✅ 已接入 | Shopify "Google & YouTube" 应用一键集成 |
| **Sitemap 提交** | ✅ 已提交 sitemap.xml | 子 sitemap（products / pages / collections / blogs）待手动补提交 |
| **GA4 ↔ GSC 互联** | ⏸️ 待做 | Settings → Associations |
| **邮件通知** | ⏸️ 待做 | GSC preferences |
| **Bing Webmaster** | ⏳ 未做 | 欧美双引擎 SEO 时再做 |

---

## 二、已完成的 SEO 工作

### ✅ Schema.org 结构化数据（极致版）

**5 个 Schema 类型全部部署，覆盖所有页面类型：**

| Schema 类型 | 文件 | 作用范围 |
|---|---|---|
| **Organization**（14 字段完整版）| `snippets/kinsoul-schema-organization.liquid` | 全站 |
| **WebSite + SearchAction** | 同上（合并在 @graph 里）| 全站 |
| **BreadcrumbList**（动态根据页面类型）| `snippets/kinsoul-schema-breadcrumb.liquid` | 产品/集合/页面/博客 |
| **Product**（含退货 + 运费 + 材料 metafield）| `snippets/kinsoul-schema-product.liquid` | 产品页（含 featured product） |
| **FAQPage**（6 条 Q&A）| `snippets/kinsoul-schema-faq.liquid` | 仅 Client Care 页 |

**Organization Schema 包含的字段：**
- name, alternateName, legalName
- url, logo（带 width/height）, image
- description, slogan
- email, founder（LU）, foundingDate（2018）
- foundingLocation（Texas, US）
- knowsLanguage, knowsAbout, areaServed
- currenciesAccepted, paymentAccepted
- contactPoint, sameAs（Instagram）

**Product Schema 极致字段（关键差异化）：**
- ✅ `hasMerchantReturnPolicy` —— Google 显示 "30-day returns" 徽章
- ✅ `shippingDetails`（3 条规则：免运/标准/国际）—— Google 显示 "Free shipping" 徽章
- ✅ `additionalProperty`（5 个 metafield 字段）：
  - Stone Type
  - Pearl Type
  - Metal Details
  - Size & Fit
  - Stone Story
- ✅ `manufacturer`、`brand`（双重引用 Organization）
- ✅ `countryOfOrigin: US`
- ✅ `itemCondition: NewCondition`
- ✅ `audience: Adults`
- ✅ `keywords`、`priceValidUntil`（自动 +1 年）
- ✅ 多张产品图（最多 6 张）
- ❌ **不含 aggregateRating / review**（评论合法性问题悬置）

### ✅ Meta 标签增强

**修改了 `snippets/meta-tags.liquid`：**

| 改动 | 详情 |
|---|---|
| 删除空 theme-color | 改由 `kinsoul-head-meta.liquid` 设为 `#7B6B5D` |
| 修复 og:image 协议错误 | `http:` → `https:` |
| 新增 og:locale | `en_US` |
| 新增 og:image:alt | 动态读取 page title |
| 新增 og:see_also | Instagram URL |
| 新增 product:brand | "Kinsoul Energy" |
| 新增 product:availability | 动态判断库存 |
| 新增 product:condition | "new" |
| 新增 product:retailer_item_id | SKU |
| 新增 twitter:image | 显式声明（不依赖 og fallback） |
| 新增 twitter:image:alt | 动态读取 page title |

### ✅ Head Meta 性能 + UX 增强

**新建 `snippets/kinsoul-head-meta.liquid`：**

- ✅ `theme-color: #7B6B5D`（手机 Safari 状态栏品牌色）
- ✅ `msapplication-TileColor`（Windows 磁贴色）
- ✅ `color-scheme: light`
- ✅ `apple-touch-icon`（180x180 iOS 主屏图标）
- ✅ `format-detection: telephone=no, address=no, email=no`
- ✅ `robots: index, follow, max-image-preview:large, max-snippet:-1`
- ✅ `author / publisher: Kinsoul Energy`
- ✅ `preconnect: cdn.shopify.com, fonts.shopifycdn.com`
- ✅ `dns-prefetch: google-analytics.com, googletagmanager.com, shop.app`

### ✅ 客评 section alt 文本

`sections/kinsoul-social-proof.liquid` 的 image_tag 加了动态 alt：
```
Customer review - {author} - {product_name}
```

---

## 三、修改 / 影响的所有文件清单

### 新建（5 个 snippets）
- `snippets/kinsoul-schema-organization.liquid`
- `snippets/kinsoul-schema-breadcrumb.liquid`
- `snippets/kinsoul-schema-product.liquid`
- `snippets/kinsoul-schema-faq.liquid`
- `snippets/kinsoul-head-meta.liquid`

### 修改（6 个核心文件）
- `layout/theme.liquid` —— head 里 render 5 个新 snippets，FAQ 仅在 Client Care 页加载
- `sections/header.liquid` —— 删除原极简版 Organization Schema
- `sections/product-information.liquid` —— 替换 Shopify 自动 Schema
- `sections/featured-product.liquid` —— 同上
- `sections/featured-product-information.liquid` —— 同上
- `snippets/meta-tags.liquid` —— 增强 OG/Twitter

---

## 四、验证状态

### ✅ 已通过验证

| 工具 | 测试 URL | 结果 |
|---|---|---|
| Google Rich Results Test | `pages/client-care` | ✅ BreadcrumbList + FAQPage 通过 |
| Schema.org Validator | `pages/client-care` | ✅ 全部 schema 正常 |

> 注：Organization 和 WebSite Schema 不在 Rich Results Test 中显示（工具限制），但 Schema.org Validator 验证通过。

### ⏸️ 待验证

- 产品页（任一）的 Product Schema 完整 rich snippet 测试
- Facebook Sharing Debugger 预览
- Twitter Card Validator 预览

---

## 五、Velora 主题保留的原生 SEO 能力

**这些 Velora 主题已经做好的，我们没动：**

| 项目 | 状态 |
|---|---|
| Article Schema（博客）| ✅ 自动生成 |
| Canonical URL | ✅ 自动生成 |
| 页面 title 智能拼接 | ✅ 已有 |
| Meta description fallback | ✅ 已有 |
| Open Graph 基础字段 | ✅ 已有（被我们增强） |
| Sitemap.xml | ✅ Shopify 默认 |
| HTTPS | ✅ Shopify 默认 |
| 移动端 viewport | ✅ 已有 |

---

## 六、未来 SEO 工作路线图

### 🔥 阶段 A：纯代码 SEO（我可以独立完成）

按推荐执行顺序：

| 顺序 | 任务 | 时间 | 影响 | 状态 |
|---|---|---|---|---|
| 1 | **图片懒加载 + LCP 优化** | 1h | ⭐⭐⭐⭐⭐ | ⏳ 待做 |
| 2 | **字体加载策略**（font-display swap, preload） | 30min | ⭐⭐⭐⭐ | ⏳ 待做 |
| 3 | **CSS 性能优化**（critical CSS 拆分） | 1.5h | ⭐⭐⭐⭐ | ⏳ 待做 |
| 4 | **图片 alt 批量审查**（除产品图外的所有图） | 1h | ⭐⭐⭐⭐ | ⏳ 待做 |
| 5 | **CollectionPage / ItemList Schema**（集合页） | 30min | ⭐⭐⭐ | ⏳ 待做 |
| 6 | **AboutPage / ContactPage Schema** | 20min | ⭐⭐⭐ | ⏳ 待做 |
| 7 | **H1/H2 层级审查**（8 个 kinsoul-* section） | 1.5h | ⭐⭐⭐ | ⏳ 待做 |
| 8 | **内链结构优化**（站内权重传递） | 1.5h | ⭐⭐⭐ | ⏳ 待做 |
| 9 | **首页 Hero SEO 强化**（不改视觉） | 30min | ⭐⭐⭐ | ⏳ 待做 |
| 10 | **404 页面 SEO 优化** | 1h | ⭐⭐ | ⏳ 待做 |
| 11 | **Resource Hints 进阶**（preload / prerender） | 1h | ⭐⭐ | ⏳ 待做 |
| 12 | **Robots.txt 增强** | 30min | ⭐⭐ | ⏳ 待做 |
| 13 | **URL trailing slash 一致性** | 30min | ⭐⭐ | ⏳ 待做 |
| 14 | **HTML 语义 ARIA landmarks** | 30min | ⭐⭐ | ⏳ 待做 |
| 15 | **HTML lang 属性优化** | 15min | ⭐ | ⏳ 待做 |

**阶段 A 总时间：~12 小时**

### 🟡 阶段 B：需要你在 Shopify 后台 / Google 工具操作

| 任务 | 谁做 | 时间 | 状态 |
|---|---|---|---|
| GA4 ↔ GSC 互联 | 你 | 5 min | ⏳ |
| GSC 邮件通知设置 | 你 | 2 min | ⏳ |
| GSC 4 个子 sitemap 手动补提交 | 你 | 5 min | ⏳ |
| GSC URL Inspection 强制索引 12 个核心页 | 你 | 15 min | ⏳ |
| GSC 现有数据巡检 | 你 + 我 | 10 min | ⏸️ 暂停 |
| 6 个产品的自定义 SEO title / description | 你（在 Shopify Admin）| 1h | ⏳ |
| 5 个核心页面的自定义 SEO title / description | 你 | 30 min | ⏳ |
| 6 个产品的 URL slug 优化 | 你 | 15 min | ⏳ |
| 6 个产品图的 alt 文本逐张填写 | 你 | 30 min | ⏳ |
| 6 款产品 metafield 数据填充（已部分完成）| 你 | 1-2h | 🔄 50% |
| 写第 1 篇博客文章 | 你 | 看你写多少 | ⏳ |

### 🟢 阶段 C：内容 SEO（半年长期工程）

| 任务 | 影响 | 时间投入 |
|---|---|---|
| **博客内容引擎**（每月 2-4 篇） | 长期 ROI 最高 | 持续 |
| **媒体 PR**（小众珠宝媒体 / 生活方式博客） | 高质量外链 | 持续 |
| **HARO**（Help A Reporter Out 注册回答） | 高权重外链 | 持续 |
| **Pinterest 内容矩阵**（珠宝品牌的真正流量入口） | 直接转化流量 | 持续 |
| **Instagram 配合**（不直接 SEO 但联动） | 品牌词搜索量 | 持续 |
| **真实客户评论积累**（解决合法性后）| 信任 + Schema rating | 持续 |

### ⏳ 阶段 D：未来扩展（按需做）

| 任务 | 触发条件 | 状态 |
|---|---|---|
| 多语言 hreflang | 上欧洲多语言版本 | ⏳ |
| Bing Webmaster Tools | 欧美双引擎策略 | ⏳ |
| Yandex Webmaster | 进入俄罗斯市场 | ❌ |
| Schema rating / review | 解决评论合法性 + 有 verified 评论 | ⏸️ |
| Google Merchant Center 优化 | 跑 Google Shopping 广告 | ⏳ |
| 第三方评论 app（Loox/Judge.me）| 积累 verified 评论 | ⏳ |

---

## 七、SEO 见效时间预期

| 时间 | 你能看到的变化 |
|---|---|
| **24-72h**（已上线）| Google 重新抓取，新 schema 入库 |
| **1 周** | GSC Enhancements 报告显示 schema 状态 |
| **1-2 周** | 产品页搜索结果出现 rich snippets（价格 + 库存）|
| **2-4 周** | 退货 / 运费徽章出现；品牌搜索 Knowledge Panel 雏形 |
| **4-8 周** | 完整 Knowledge Panel + Sitelinks 搜索框；FAQ 答案展开 |
| **3-6 个月** | 长尾关键词开始有真实点击；博客文章逐步起效 |
| **6-12 个月** | SEO 流量成为可观渠道（前提：有内容引擎 + 外链建设） |

---

## 八、参考信息

### 关键 URL
- 网站首页：https://kinsoulenergy.com/
- Google Search Console：https://search.google.com/search-console
- Google Analytics 4：https://analytics.google.com
- Google Rich Results Test：https://search.google.com/test/rich-results
- Schema.org Validator：https://validator.schema.org/

### 品牌核心信息（用于 Schema / Meta）
- 品牌名：Kinsoul Energy
- 法律实体：LuKai Trading LLC
- 注册地：Texas, US
- 创立年份：2018
- 创始人：LU
- 邮箱：hello@kinsoulenergy.com
- Instagram：https://www.instagram.com/kinsoulenergy/
- Slogan：Jewelry Born from the Earth
- 描述：Handmade bracelets crafted from 100% natural pearls and hand-selected gemstones — meaningful jewelry designed to be worn every day.

### 技术堆栈
- 平台：Shopify
- 主题：Velora（已深度定制）
- 域名年龄：7 个月（2025-09 起）
- 上线时间：2026-04（几天前）

---

## 九、待解决的悬置问题

| 问题 | 状态 | 影响 |
|---|---|---|
| 评论合法性 | 用户表示已处理 | 直接影响 aggregateRating Schema 是否能加 |
| GSC 数据巡检 | 暂停 | 影响数据驱动的 SEO 决策 |
| 第三方评论 app 选型 | 未决定 | 决定 verified 评论积累方式 |

---

## 十、下次继续 SEO 工作时的快速恢复指南

如果你想从某一项继续，告诉我"继续 SEO 阶段 A 第 X 项"或者直接说项目名，我能立刻接上工作。

最有可能的下一步：
- **#2 图片懒加载 + LCP 优化** —— 影响最大，纯代码工作
- **GSC 配置补全**（GA4 互联 + 邮件通知 + 子 sitemap）—— 5 分钟你做
- **首页 Hero SEO 强化** —— 30 分钟纯代码

---

*此文档随 SEO 工作进度更新。每完成一项，把状态从 ⏳ 改为 ✅。*
