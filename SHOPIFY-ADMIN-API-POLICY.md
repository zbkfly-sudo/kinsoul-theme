# Shopify Admin API 操作规范（Claude 使用限制）

本文档定义 Claude 可以/不可以通过 Shopify Admin API 做什么。**每次调用前 Claude 必须先检查此清单**。

## 🟢 允许（白名单 — 可直接做）

这些是低风险、可回滚、不影响订单/客户/资金的操作。

| 类别 | 具体操作 | API endpoint / Mutation | 理由 |
|---|---|---|---|
| **页面（Pages）** | 创建新 page | `pageCreate` | 可删除回退 |
| | 编辑 page 内容/SEO/template | `pageUpdate` | 可通过版本历史找回 |
| **Metafield 定义** | 新增 metafield definition | `metafieldDefinitionCreate` | 不影响已有数据 |
| | 更新 definition description/name | `metafieldDefinitionUpdate` | 低风险 |
| **Metafield 值** | 设置/更新产品 metafield 值 | `metafieldsSet` | 可重新 set 覆盖 |
| **文件库（Files）** | 上传新文件 | `stagedUploadsCreate` + `fileCreate` | 仅新增不删除 |
| **主题（只读）** | 读取当前 live theme id / 列出 themes | `themes` query | 只读 |
| **只读查询** | 列出产品、页面、订单、客户等 | 任何 `query` 操作 | 只读 |

## 🔴 禁止（黑名单 — 绝不能做，必须让用户手动）

这些是高风险、不可回滚、或会影响真实交易/客户数据的操作。即使 token 有权限，Claude 也不做。

| 类别 | 具体操作 | 为什么禁止 |
|---|---|---|
| **订单** | 任何 order mutation（创建/取消/退款/编辑）| 影响真实交易和资金流 |
| | 订单标签/备注修改 | 影响客服和履约流程 |
| **客户数据** | 删除/合并客户 | 不可逆 + 隐私合规问题 |
| | 修改客户邮箱/地址 | 可能破坏客户登录和发货 |
| | 导出客户数据 | GDPR/CCPA 合规风险 |
| **产品（结构性）** | **删除产品** | 不可逆，破坏所有引用 |
| | 修改产品 handle（URL slug）| 破坏 SEO、外部链接、购物车、书签 |
| | 修改已售产品的 variant ID | 破坏订单历史 |
| | 删除 variant、修改价格、修改库存 | 影响销售和真实收入 |
| **页面/主题** | **删除 page**（非 Claude 创建的）| 可能误删用户的重要内容 |
| | 修改 legal pages（Privacy/Terms/Refund 等）| 法律合规 |
| | **删除 theme 文件 / 卸载 theme** | 用 `publish.sh` 流程，不走 API |
| | 直接改 live theme 的 settings_data.json | 必须走 test theme + preview + publish 流程 |
| **账户/设置** | 账单、shipping rate、tax、支付方式 | 直接影响收入 |
| | 用户权限、staff 管理 | 安全权限 |
| | 域名、DNS、SSL | 影响整站可达性 |
| **折扣码** | 创建/修改公开折扣码 | 影响真实营销和毛利 |
| **库存** | 修改库存数量 | 直接影响 sellable/oversell |
| **App 安装** | 安装/卸载其他 app | 可能改动 theme 或加收费 |
| **Metafield 定义** | **删除已有 metafield definition**（尤其 pinned）| 可能丢失 Admin 配好的数据 |
| **Webhook** | 创建 webhook | 可能被恶意利用 |

## 🟡 受控（灰名单 — 需要显式确认才做）

这些操作本身无害，但因影响面广，**每次必须先告诉用户计划、列出影响、明确问"执行吗？"才做**。

| 操作 | 必须确认的内容 |
|---|---|
| 批量修改 ≥10 个产品 metafield | 列出每个产品的改动预览（dry-run 必选） |
| 删除 Claude 自己创建的 page | 确认 handle、确认没有外部链接指向 |
| 覆盖已有的非空 metafield 值 | 显示旧值 + 新值 |
| 上传 >10 张图片到 Files | 确认这些图片的用途和大小 |
| 修改店铺级 metafield（shop.metafields） | 可能影响全站显示 |

## 📋 每次调用前 Claude 必须做的 4 件事

### 1. 预演（Dry-Run First）
任何 write 操作的脚本**必须**先支持 `--dry-run`，Claude 第一次运行时**必须**用 `--dry-run` 输出操作清单给用户看。

### 2. 最小权限检查
调用前检查本次操作的 API scope 是否超出用户授予的最小必要权限。若超出，停止并告诉用户。

### 3. 可回滚预案
每个 write 操作前记录下：
- 如果出错，怎么回滚？（`pageDelete` / `metafieldsDelete` / 值恢复为旧值等）
- 回滚命令写成具体命令行，不只是文字描述

### 4. 日志（Logging）
write 操作的 API 调用记录到 `scripts/shopify-admin-ops.log`，包含时间戳、操作、对象 ID、用户授权确认。便于审计和回溯。

## 🛑 立即停止的信号

如果遇到以下任一情况，Claude **立即停止**并询问用户：

1. API 返回 rate limit 错误 → 指数退避，不 bypass
2. API 返回未预期的字段（schema 变更）→ 不要猜，先问
3. token 权限不足但操作是必须的 → 不要降级到部分操作
4. 对象 ID 看起来可疑（比如预期一个 product ID 却返回一个 variant ID）
5. 操作结果与预期数量不符（如计划改 6 个产品结果返回了 20 条响应）
6. 用户 .env 里的 token 前缀异常（`shpss_` 非 `shpat_` 等）
7. 店铺域名不是预期的 `qr4xym-qi.myshopify.com`

## 📚 Claude 必须熟悉的 API 快速参考

### 创建页面（允许）
```graphql
mutation pageCreate($page: PageCreateInput!) {
  pageCreate(page: $page) {
    page { id handle title templateSuffix isPublished }
    userErrors { field message code }
  }
}

# Input fields Claude 会用到:
# title (required)        — 页面标题
# handle                  — URL slug（不填则从 title 生成）
# body                    — HTML 内容
# bodySummary             — 摘要
# templateSuffix          — 主题模板后缀（如 "quiz" → page.quiz.json）
# isPublished             — 是否立即发布
# metafields              — 附加 metafield
# publishDate             — 定时发布
# templateSuffix          — 关键字段，连接到 theme template

# NOT 会用的危险字段:
# adminGraphqlApiId / createdAt / updatedAt / onlineStoreUrl — 只读
```

### Metafield 值（允许）
```graphql
mutation metafieldsSet($metafields: [MetafieldsSetInput!]!) {
  metafieldsSet(metafields: $metafields) {
    metafields { id key namespace value type }
    userErrors { field message }
  }
}

# 单次最多 25 条
# ownerId 必须是 GID 格式 (gid://shopify/Product/123)
# value 对 list 类型必须是 JSON 字符串: json.dumps([gid1, gid2])
```

### Metafield 定义（允许）
```graphql
mutation metafieldDefinitionCreate($definition: MetafieldDefinitionInput!) {
  metafieldDefinitionCreate(definition: $definition) {
    createdDefinition { id key namespace type { name } }
    userErrors { field message code }
  }
}

# 常用 type:
# single_line_text_field        — 短文本
# multi_line_text_field         — 长文本
# product_reference             — 单产品引用
# list.product_reference        — 产品引用列表
# number_integer / number_decimal
# boolean
# url
# rich_text_field               — 富文本

# code "TAKEN" 表示已存在 → 跳过而非报错
```

### 只读查询（允许）
```graphql
# 用 handle 查产品 GID:
query { productByHandle(handle: "ember") { id title } }

# 列所有页面:
query { pages(first: 50) { edges { node { id handle title } } } }

# 列产品 metafield:
query { product(id: "gid://shopify/Product/123") {
  metafields(first: 20) { edges { node { namespace key value } } }
}}
```

### 文件上传（允许，受控）
```graphql
# Step 1: 请求上传 URL
mutation stagedUploadsCreate($input: [StagedUploadInput!]!) {
  stagedUploadsCreate(input: $input) {
    stagedTargets { url resourceUrl parameters { name value } }
  }
}

# Step 2: HTTP POST 到 stagedTargets.url (二进制)

# Step 3: 注册到 Files
mutation fileCreate($files: [FileCreateInput!]!) {
  fileCreate(files: $files) {
    files { id preview { image { url } } }
  }
}

# 每次上传 Claude 必须先问用户:
# 1. 文件用途？
# 2. 是否和现有 Files 冲突？
# 3. 上传后 shopify://shop_images/xxx 的引用怎么用？
```

### 禁止调用的 mutation 示例
```
orderCreate / orderCancel / orderRefund        ❌ 订单
customerCreate / customerUpdate / customerDelete ❌ 客户
productCreate / productUpdate / productDelete   ❌ 产品结构（只能改 metafield）
priceRuleCreate / discountCodeCreate            ❌ 折扣
themeDelete / themePublish                       ❌ 主题发布（用 publish.sh）
webhookSubscriptionCreate                        ❌ Webhook
appUninstall                                     ❌ App 管理
```

## 🔐 Token 管理规则

1. **Never log or echo tokens** in chat / commits / PR descriptions
2. Token **必须**从 `.env` 读取，**禁止**硬编码到任何脚本
3. `.env` 必须在 `.gitignore` 里（已是）
4. 如果 Claude 看到 token 格式可疑（前缀错误、长度异常），停止并告诉用户
5. 脚本结束后不保留 token 在内存之外的位置
6. 如果用户说"token 泄漏"，立即建议 Uninstall app → reinstall 生成新 token

## 📝 审计日志格式

每次 write 操作追加一行到 `scripts/shopify-admin-ops.log`：
```
2026-04-17T08:45:12Z | pageCreate       | handle=stone-quiz         | id=gid://shopify/Page/123456  | user_confirmed=true
2026-04-17T08:45:14Z | metafieldsSet    | owner=Product/7839964725334 | key=custom.related_products | count=3 | user_confirmed=true
2026-04-17T08:46:02Z | fileCreate       | filename=lu-founder.jpg   | size=245KB                    | user_confirmed=true
```

## 当前项目（Kinsoul Energy）specific

- **Store**: `qr4xym-qi.myshopify.com`（若域名变化，停止）
- **Live theme**: `147284361302`（P1–P7 redesign 未发布前保持这个）
- **测试 theme**: 每次由 `push-test.sh` 创建，ID 记录在 git tag
- **6 款产品**: Ember / Serenity / Aura / Obsidian / Terra / Soleil（handle 不能改）
- **已创建的 metafield**：
  - `custom.stone_type`（旧）— Claude 只读
  - `custom.stone_story`（旧）— Claude 只读
  - `custom.size_fit` / `shipping_note` / `care_note` / `pearl_type` / `metal_details`（旧）— Claude 只读
  - `custom.related_products`（P2 新增）— Claude 可读写
  - `custom.stone_chip`（P3 新增）— Claude 可读写

---

本文件是 Claude 操作 Shopify Admin API 的**硬契约**，违反视同违反用户授权。创建时间：2026-04-17。
