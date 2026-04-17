# P2 Complete Your Look — Admin 手工配置

**上下文**：PDP 底部 "Complete Your Look" 区依赖 Shopify 的 `recommendation_type: "related"` 自动推荐（用购买历史数据）。对于 6 款产品的小 SKU 品牌、早期订单量不够，自动推荐会显示为空。必须手工配相关产品。

## 推荐配对（基于价格相近 + 风格互补）

| 主产品 | 推荐 1 | 推荐 2 | 推荐 3 | 理由 |
|---|---|---|---|---|
| **Ember** ($228) | Obsidian ($208) | Terra ($264) | Aura ($365) | 同类中高端 agate + pearl 层叠佩戴 |
| **Serenity** ($168) | Soleil ($139) | Ember ($228) | Aura ($365) | 入门价位互补，步进加购 |
| **Aura** ($365) | Ember ($228) | Terra ($264) | Obsidian ($208) | 顶配搭配高端款，多石头叠戴 |
| **Obsidian** ($208) | Ember ($228) | Terra ($264) | Aura ($365) | 同色系深色调合集 |
| **Terra** ($264) | Ember ($228) | Obsidian ($208) | Aura ($365) | Agate 家族成员互补 |
| **Soleil** ($139) | Serenity ($168) | Ember ($228) | Aura ($365) | 入门价叠加购，渐进价格梯度 |

## 配置步骤（Shopify Admin → Products）

对 6 款产品，每款重复以下操作：

1. Admin → **Products** → 点击产品（如 Ember）
2. 右侧 **Metafields** → 找到 / 创建 `custom.related_products`
   - 如果这个 metafield 没有：先在 **Settings → Custom data → Products** 添加：
     - Namespace: `custom`
     - Key: `related_products`
     - Type: **Product reference (List)**
     - Description: "Manual related products for Complete Your Look section"
3. 在字段里**按顺序添加** 3 个产品（参考上表）
4. **Save**

## 代码层如何使用这个 metafield

当前 `templates/product.json` 的 `product_recommendations_qggXJq` 用的是 Shopify 原生 `recommendation_type: "related"`，它会：
- 优先用 `product.metafields.custom.related_products`（如果存在）
- 否则回退到 Shopify 自动算法

所以**只要在 Admin 里填了 metafield**，PDP 底部立刻显示手工推荐，不需要改代码。

## 验证方式

1. 配完 Ember 的 3 个推荐产品后
2. 用隐身浏览器访问 `https://www.kinsoulenergy.com/products/persian-red-agate-pearl-sterling-silver-bracelet`
3. 滚到底部 "Complete Your Look"
4. 应看到 Obsidian + Terra + Aura 三张卡，不是空白

## 附：如果 `custom.related_products` 无效

Velora 的 `product-recommendations` section 默认读 Shopify API `/recommendations/products.json` — 这个 API 会返回：
- 先用 metafield 如果配置了
- 再用基于碰撞 / 协同过滤算法

如果 metafield 没生效，可能需要在 `sections/product-recommendations.liquid` 加显式 override：
```liquid
{%- if product.metafields.custom.related_products != blank -%}
  {%- for p in product.metafields.custom.related_products.value -%}
    {% render 'product-card', product: p %}
  {%- endfor -%}
{%- else -%}
  {% comment %} fallback to auto recommendations {% endcomment %}
{%- endif -%}
```

P3 或 P4 如果 metafield 路径走不通，我会改代码兜底。先试 metafield。

---

文件创建时间：2026-04-17
预计配置时间：6 款 × 2 分钟 = 约 15 分钟
