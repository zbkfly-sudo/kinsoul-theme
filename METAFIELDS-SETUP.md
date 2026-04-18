# Kinsoul Energy — Metafield 设置清单

在 Shopify 后台「设置 → 自定义数据 → 产品」中创建以下字段：

## 必须创建的 Metafield

| 命名空间.键名 | 名称 | 类型 | 说明 |
|---|---|---|---|
| custom.stone_type | Stone Type | 单行文本 | 石头类型，如 "Persian Red Agate" |
| custom.pearl_type | Pearl Type | 单行文本 | 珍珠类型，如 "Baroque Freshwater Pearl" |
| custom.metal_details | Metal Details | 单行文本 | 金属细节，如 "S925 Sterling Silver" |
| custom.size_fit | Size & Fit | 多行文本 | 尺寸和佩戴说明 |
| custom.shipping_note | Shipping Note | 多行文本 | 自定义运费说明（留空则使用默认文案） |
| custom.care_note | Care Note | 多行文本 | 自定义护理说明（留空则使用默认文案） |
| custom.stone_story | Stone Story | 多行文本 | 石头象征寓意说明 |

> **字段名核对说明：** 上表 7 个字段已与 `templates/product.json` 代码中的引用 100% 对齐，可直接在 Shopify 后台「设置 → 自定义数据 → 产品」按这套命名创建。Shipping Note 和 Care Note 留空时前端会自动显示通用默认文案。

## 每个产品的建议填写内容

### PS2508016 — Persian Red Agate Bracelet ($228)
- stone_type: Persian Red Agate
- pearl_type: Freshwater Pearl Silver Bars
- metal_details: S925 Sterling Silver bars (20-30mm)
- size_fit: Agate stones 17-20mm. Available in 14.5cm, 15cm, 16cm circumference.
- stone_story: Red agate is associated with confidence, vitality, and grounding energy. In many traditions, it's believed to bring stability and courage.

### PS2508034 — Obsidian Bracelet ($208)
- stone_type: Black Agate, Tourmalinated Quartz
- pearl_type: Grey Freshwater Rice Pearls (8mm) + Baroque Pearl centerpiece
- metal_details: S925 Sterling Silver logo tag (California silversmith workshop)
- size_fit: Available in S / M / L / XL (6.1" / 6.7" / 7.3" / 7.9").
- stone_story: Black agate is a stone of protection and inner strength. Paired with tourmalinated quartz, known for inner resolve and quiet strength.

### PS2508037 — Mozhu Bracelet ($264)
- stone_type: Persian Banded Agate
- pearl_type: Large Baroque Freshwater Pearl
- metal_details: S925 Sterling Silver spacers with antique finish
- size_fit: Available in 14.5cm, 15cm, 16cm circumference.
- stone_story: Banded agate is prized for its layered, earth-toned patterns — a symbol of balance and harmony.

### PS2508080 — Freeform Amethyst Bracelet ($168)
- stone_type: Freeform Amethyst, Amethyst Rounds
- pearl_type: Freshwater Threaded Pearls (8.3-9.2mm)
- metal_details: S925 Sterling Silver logo tag
- size_fit: Available in 14.5cm, 15cm, 16cm circumference.
- stone_story: Amethyst is one of the most beloved stones in jewelry — traditionally associated with calm, clarity, and intuition.

### PS2508125 — Soleil Bracelet ($139)
- stone_type: Brazilian Citrine, Clear Quartz Tips, Amethyst Rounds
- pearl_type: Freshwater Round Pearls (Zhuji, China)
- metal_details: S925 Sterling Silver logo tag (California silversmith workshop)
- size_fit: Amethyst rounds 5-5.5mm. Available in S / M / L / XL (6.1" / 6.7" / 7.3" / 7.9").
- stone_story: Citrine is often called the "stone of abundance" — associated with warmth, optimism, and creative energy.

### PS2508174 — Aura Balance Bracelet ($365)
- stone_type: 8 natural stones selected from a curated palette of 12 (Tiger's Eye, Lapis Lazuli, Amethyst, Citrine, Amazonite, Clear Quartz, Tourmalinated Quartz, Red Agate, Prehnite, Grey Agate, Blue Apatite, Agate Accent Beads)
- pearl_type: Large Baroque Saltwater Pearl (Australia)
- metal_details: S925 Sterling Silver logo tag + maker's mark bar (California silversmith workshop)
- size_fit: Available in S / M / L / XL (6.1" / 6.7" / 7.3" / 7.9").
- stone_story: A curated spectrum of stones — each hand-selected from our palette of twelve. No two Auras share the same combination.
