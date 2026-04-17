# Shopify 中文界面词汇表

**用途**：Claude 给 Kinsoul 项目 UI 路径时**必须用中文标签**，不能自作聪明给英文。这份表从用户的实际截图里提取，确保和用户看到的界面一一对应。

**维护原则**：
- 只记录**用户截图里真实看到过的**中文标签
- 不确定的标签标记 `❓ 未验证`
- 每次遇到新界面名称追加到这里

---

## 左侧主导航（Shopify Admin）

| 中文标签 | 英文 | 图标/位置 |
|---|---|---|
| 主页 | Home | 最上面 |
| 订单 | Orders | |
| 产品 | Products | |
| 客户 | Customers | |
| 市场营销 | Marketing | |
| 折扣 | Discounts | |
| 内容 | Content | |
| Markets | Markets | （保留英文）|
| 财务 | Finances | |
| 分析 | Analytics | |
| 销售渠道 > 在线商店 | Sales channels > Online Store | 侧栏中部 |
| 销售渠道 > Facebook & Instagram | | |
| 应用 > Kinsoul Admin Ops | Apps > Custom App | 侧栏下部 |
| 设置 | Settings | **左下角齿轮图标** |

## 在线商店（Online Store）子菜单

| 中文 | 英文 |
|---|---|
| 模板 | Themes |
| 当前使用 / 当前模板 | Current theme |
| 其他模板 | Theme library（草稿列表）|
| 自定义 | Customize（进主题编辑器）|
| 编辑代码 | Edit code |
| 发布 | Publish |
| 预览 | Preview |
| 重命名 | Rename |

## Shopify Dev Dashboard（Custom App 配置）

| 中文 | 英文 | 说明 |
|---|---|---|
| 设置 | Settings | app 内的 tab |
| 凭据 | Credentials | |
| 客户端 ID | Client ID | 开头 32 位 hex |
| 加密密钥 / API 密钥 | Client Secret / API Secret | 前缀 `shpss_` |
| Admin API access token | Admin API access token | **通常保留英文**；前缀 `shpat_` 或 `shpca_` 或纯 hex |
| 管理 Admin API 权限范围 | Admin API access scopes | 勾选 write_products / write_content 等 |
| 安装应用 | Install app | |
| 卸载应用 | Uninstall app | |

## 管理页面（Pages）

| 中文 | 英文 |
|---|---|
| 在线商店 > 页面 | Online Store > Pages |
| 添加页面 | Add page |
| 模板（Theme template）| Theme template | 页面右侧栏选择 page.quiz 等 |
| 标题 | Title |
| 内容 | Content |
| URL 和句柄 | URL and handle | "句柄" = handle |
| 搜索引擎列表预览 | Search engine listing preview | SEO 元数据区 |
| 页面标题（SEO）| Page title |
| 元说明 | Meta description |
| 可见性 | Visibility |
| 可见 / 隐藏 | Visible / Hidden |

## Metafield / 自定义数据

| 中文 | 英文 |
|---|---|
| 设置 > 自定义数据 | Settings > Custom data |
| 产品 | Products |
| 添加定义 | Add definition |
| 命名空间 | Namespace |
| 键 | Key |
| 类型 | Type |
| 单行文本 | Single line text |
| 产品引用（列表）| Product reference (list) |
| 数值 | Number |
| 日期 | Date |
| 固定到产品页 | Pin to Admin pages | （显示在产品编辑页侧栏）|

## 主题编辑器（Customize）

| 中文 | 英文 |
|---|---|
| 章节 / 区块 | Sections / Blocks |
| 添加章节 / 添加区块 | Add section / Add block |
| 设置 | Settings |
| 颜色方案 | Color scheme |
| 保存 | Save |
| 预览主题 | Preview theme |

## 应用安装与 App Store

| 中文 | 英文 |
|---|---|
| 应用和销售渠道 | Apps and sales channels |
| 开发应用 / 构建应用 | Develop apps / Build apps | （新版 Dev Dashboard 改名了）|
| 已安装 | Installed |
| 查看 Shopify 应用商店 | Visit Shopify App Store |

## 订单（我们项目不改这些，仅为避免混淆）

| 中文 | 英文 | 操作 |
|---|---|---|
| 订单 | Orders | Claude 不碰 |
| 客户 | Customers | Claude 不碰 |
| 退款 | Refund | Claude 不碰 |

---

## ❓ 遇到新词时的处理

1. Claude 遇到不确定的中文标签 → **请用户截图发一下**，不要猜
2. 抄进这份表 + 标注是从哪个截图/页面看到的
3. 下次同样场景直接引用
4. WebFetch 官方中文 docs 被 403 的话，备用来源：https://community.shopify.com/c/ 中文版

---

**最后更新**：2026-04-17  
**来源**：用户在 Kinsoul 项目中分享的 Dev Dashboard / Admin / Themes 页面截图
