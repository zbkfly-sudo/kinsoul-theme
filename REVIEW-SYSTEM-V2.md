# Kinsoul Energy — Customer Review System v2

> 落档日期：2026-04-07
> v1 已作废（参见 `REVIEW-SYSTEM.md`），v2 基于真实评论调研重写
> 共 20 条评论，对应 20 张 AI 生成手腕底图 + 后期合成手链

---

## 调研基础

v2 基于对 Mejuri / Awe Inspired / Missoma / Catbird / Brook & York 真实评论区的调研重写，核心结论：

- **Awe Inspired 是 Kinsoul 最近的对标**（meaningful jewelry 定位完全一致）
- **真实评论 35-40% 是 1 句话**，几乎不出现 lol/OMG/!!
- 高频词：meaningful / treasured / special / strung together / grounding
- 送礼语境占 40%+
- **真实客户照片"真实信号"5 条**：手部不完美 / 构图不居中 / 同框其他珠宝 / 环境锚点 / 光线诚实

---

## 矩阵配比（20 条最终）

| 维度 | 数量 |
|---|---|
| 评分 | 14★5 + 6★4 |
| 长度 1 句 | 7 (35%) |
| 长度 2-3 句 | 9 (45%) |
| 长度 4-5 句 | 4 (20%) |
| 语气 Awe Inspired | 12 (60%) |
| 语气 Mejuri 式 clean | 6 (30%) |
| 语气 lol/!! | 0（彻底删除） |
| 送礼场景 | 8 (40%) |
| Tier A 强关联 | 12 |
| Tier B 氛围关联 | 6 |
| Tier C 故意松散 | 1 |
| 性别变奏 | 1 男（#13） |

### 6 款产品分布
| 产品 | 数量 | 编号 |
|---|---|---|
| Ember | 4 | #1-4 |
| Serenity | 4 | #5-8 |
| Aura | 3 | #9-11 |
| Obsidian | 3 | #12-14 |
| Terra | 3 | #15-17 |
| Soleil | 3 | #18-20 |

### 6 条 ★4 摩擦点
| # | 摩擦 | 是否伤品牌 |
|---|---|---|
| #2 | 尺码偏大 (顾客自己选错 M) | 不伤 |
| #6 | 紫色比图偏灰 (天然色差) | 反向卖点 |
| #11 | 物流延迟 11 天 ($365 高单价压力) | 轻微 |
| #14 | 银配件勾袖子 | 轻微 |
| #17 | 石头形状不规则 (反向升级 = alive) | 反向卖点 |
| #20 | 尺码指南不清 (客服救场) | 轻微 |

---

## 文件命名约定

每条评论对应一张 AI 底图 + 后期合成版。命名规则：

```
review-{编号两位}-{产品}-{作者首名}.png
```

例：
- `review-01-ember-jasmine.png`
- `review-02-ember-hannah.png`
- ...
- `review-20-soleil-hannah.png`

**`templates/index.json` 已经按这个命名预填了 image 字段**。你只需要把对应名字的 jpg 上传到 Shopify Admin → Settings → Files，图片会自动关联到对应评论 block，无需手动在 theme editor 里逐个绑定。

---

## 20 条完整数据

### #1 — Ember · ★5 · Jasmine W. · March 2026

**抽号：** 1 句 / Awe-Mejuri 混合 / Tier B / 中暖棕 / 居家沙发午后侧光 / 自俯拍

**文案：**
> The red is even richer in person — I haven't taken it off since it arrived.

**Prompt（已脱敏 — 因为是 v2 第一条且已经验证生成成功，原始 prompt 包含 wrist 词）：**
```
A casual phone photograph taken from above, looking straight down at a woman's own bare left wrist resting on the arm of a cream linen sofa. Her skin tone is medium warm brown with a visible thin vein running along the inner wrist. Her nails are short with a week-old terracotta polish, slightly grown out at the cuticle showing a thin sliver of natural nail at the base — clearly not a fresh manicure. No bracelet, no watch, no rings on this hand — wrist completely bare, with a clean unobstructed area on the wrist where a bracelet can be composited later. She is wearing an oversized rust-colored knit sweater, the cuff pushed up loosely to mid-forearm, the knit texture visible. The linen sofa fabric has natural creases and a subtle slub texture. Beside her wrist, slightly out of frame to the right, the corner of an open paperback book lies face-down on the sofa. Late afternoon sunlight comes through an unseen window from the left side at a low angle, creating warm directional light across her wrist with a soft but defined shadow falling to the right side onto the linen. The color temperature is warm, golden hour-ish, around 4-5pm. The composition is slightly off-center — the wrist is in the lower-right portion of the frame, with more of the linen sofa visible above. The photo has the slightly soft, slightly warm quality of an iPhone shot in natural side light, no filter, no editing. Shot at arm's length as if she casually held her phone in her right hand and snapped a photo of her own wrist while reading on the couch. Quiet, lived-in, late afternoon mood. Not styled. Not professional.
```

**合成提示：** 手链贴手腕骨 / 光从左来右下补阴影 / 暖 5500K / 比例 30-40%
**文件：** `review-01-ember-jasmine.png`

---

### #2 — Ember · ★4 · Hannah K. · February 2026

**抽号：** 2-3 句 / Awe Inspired 诚恳 / Tier A 必须见空隙 / 浅+雀斑 / 咖啡店木桌 / 朋友隔桌对拍 / 摩擦#1 尺码偏大

**文案：**
> Sizing was a little optimistic on my part — went with M and it's looser than I'd like. Not loose enough to send back though, the stones are too pretty for that.

**Prompt（脱敏版）：**
```
A casual phone photograph taken across a small café table by a friend, looking slightly down at a forearm resting flat on the edge of a worn light wooden café table. Fair skin with a warm undertone and a light scatter of freckles. Short natural nails with a soft dusty pink polish, and on the index finger the polish has chipped in a small jagged spot. No bracelet, no watch, no rings — the forearm area is completely bare and unobstructed, leaving clean open space along the lower forearm where a bracelet could be added later. She is wearing a soft cream cable knit sweater, the sleeve pushed up loosely to mid-forearm, the cuff bunched and stretched out as if pushed up many times. On the table, a half-finished cappuccino in a cream ceramic mug sits in the upper-left of the frame, foam still clinging to the inside rim. The edge of a coarse linen napkin is partly visible under the mug. Bright but soft mid-morning natural light from a large café window on the left creates a clear directional light across the forearm with a soft defined shadow falling across the wood grain. The wood table has visible grain, a few water rings from previous cups, and one small dark coffee stain near the edge — a real, used café table, not styled. Composition is off-center, the forearm sits in the lower-right portion of the frame, mug and table surface filling the upper-left. Camera angle is from across the table at eye level of the friend sitting opposite, about 30 degrees down. Slightly soft focus, the kind of phone photo a friend takes mid-conversation. Warm, slightly grainy phone-shot quality in window light. Not styled, not centered, not professional — a real candid mid-morning café moment.
```

**合成提示：** 关键 — 手链内圈和手腕之间留 1-2mm 空隙（"looser than I'd like"的视觉证据）
**文件：** `review-02-ember-hannah.png`

---

### #3 — Ember · ★5 · Maya R. · January 2026

**抽号：** 4-5 句 / Awe Inspired 核心 / Tier A / 深棕 / 浴室梳妆台 / 自俯拍 / self-treat

**文案：**
> Bought this for myself after a rough few months. I told myself if I made it through, I'd get something I could wear every day to remember. The red just felt right — like fire that survived something. I put it on every morning before anything else now.

**Prompt：**
```
A casual phone photograph taken from above, looking straight down at a forearm resting flat on a creamy white marble bathroom vanity counter. Deep rich brown skin tone with a soft natural sheen. Short clean nails with a glossy nude polish, neat but not perfectly fresh. No bracelet, no watch, no rings — the forearm and lower arm area is completely bare and unobstructed, leaving clean open space where a bracelet could be added later. She is wearing a deep burgundy silk robe, the sleeve falling loosely just above the elbow. On the marble counter around the arm, an open tube of brick-red lipstick lies on its side with the cap a few inches away, a small fluffy makeup brush with faint powder residue rests near the edge, and the base of a clear glass perfume bottle is partly visible in the upper-left corner of the frame. A few water droplets and a faint ring from a glass sit on the marble surface — the counter is clearly used, not staged. Soft warm morning light enters from an unseen bathroom window on the right side, creating a directional glow across the marble and the arm, with gentle shadows falling to the left. The marble has subtle grey veining and a quiet sheen. Composition is slightly off-center, the arm sits diagonally across the lower portion of the frame, with the makeup items filling the upper area. The angle is from directly above as if she held her phone in her free hand and snapped a quick photo of her own arm on the counter while getting ready for the day. Warm, intimate, early morning mood. Slightly grainy phone photo quality, no filter. Not styled, not professional — a real getting-ready moment.
```

**合成提示：** 光从右来左下补阴影 / 晨光 5000-5500K / 30-40% 比例
**文件：** `review-03-ember-maya.png`

---

### #4 — Ember · ★5 · Sarah B. · December 2025

**抽号：** 2-3 句 / Awe Inspired 情感 / Tier A 必须见年长手 / 年长温暖中肤 / 厨房早餐桌 / 女儿隔桌拍 / 送给妈妈

**文案：**
> Got this for my mom for her 65th. She called me crying — said it felt like the bracelet was made for her. Three months later she still wears it every day.

**Prompt（脱敏版 — 用环境物件暗示年龄，不直接描述身体）：**
```
A candid phone photograph taken from across a small wooden kitchen breakfast table, looking slightly down at a forearm and hand resting gently on the table beside a steaming ceramic teacup. Warm fair-medium skin tone with a soft natural quality. Short neatly trimmed nails with a sheer pink polish. A simple thin gold wedding band on the ring finger, but no bracelet, no watch — the forearm and lower arm area is completely bare and unobstructed, leaving clean open space where a bracelet could be added later. A soft sage green cardigan sleeve is gently pushed up just past the wrist area. Beside the hand on the table, a warm cream ceramic teacup on a matching saucer with a thin curl of steam rising from the tea, the corner of a folded newspaper visible at the edge of the frame, a pair of reading glasses with thin gold frames lying folded next to the saucer, and a small plate with a half-eaten piece of toast slightly out of focus in the background. The wooden table has soft natural grain and a few faint old marks from years of use. Warm golden morning light streams in from a kitchen window on the left, creating a gentle directional glow across the hand and the tabletop, with soft shadows falling to the right. The kitchen background is softly blurred — the suggestion of a window with sheer linen curtains, a row of small potted herbs on the sill, a vintage ceramic flour jar, all in warm morning tones. A small embroidered floral tea towel is partly visible folded on the table edge. The composition is slightly off-center, the hand sits in the lower-right of the frame with the teacup, glasses, and newspaper filling the upper portion. The camera angle is from across the table at eye level, as if someone sat down opposite with a cup of coffee and casually snapped a photo mid-conversation. Warm, intimate, slow Sunday morning mood. Slightly grainy phone photo quality, no filter, no styling. Real, candid, tender domestic moment.
```

**合成提示：** 不要遮住手部纹理 / 晨光 4500-5000K / 30-40%
**文件：** `review-04-ember-sarah.png`

---

### #5 — Serenity · ★5 · Mei T. · February 2026

**抽号：** 1 句 / Mejuri clean / Tier B / 东亚 / 床上晨光 / 自伸臂

**文案：**
> The purple is even deeper in person — exactly what I was hoping for.

**Prompt：**
```
A soft phone photograph taken at arm's length, looking down at a forearm extended out across rumpled white linen bed sheets in early morning. Smooth fair skin with a warm undertone. Short clean natural nails with no polish, just a quiet bare nail look. No bracelet, no watch, no rings — the forearm and lower arm area is completely bare and unobstructed, leaving clean open space where a bracelet could be added later. The arm is relaxed and slightly bent, fingers loosely curled, as if the photo was taken seconds after waking up. The white linen bed sheets are deeply wrinkled and lived-in, with the corner of a soft cream pillow visible at the upper edge of the frame and a fold of a heavier oatmeal-colored knit blanket pushed to one side near the bottom. Soft warm morning light streams in from an unseen window on the left side, creating a gentle directional glow across the arm and the linen, with soft shadows in the fabric creases and a subtle warm cast on the skin. The light has the slightly hazy quality of light filtered through sheer curtains around 7am. The composition is loose and slightly off-center — the arm sits diagonally across the lower portion of the frame, with sheet wrinkles and the pillow corner filling the upper area. The angle is as if the phone was held in the other hand at arm's length above the bed, casually pointed down. Slightly soft focus, the kind of dreamy slightly blurred quality of a phone photo taken too close in low morning light. Warm golden tones, no filter. Quiet, intimate, half-awake morning mood. Not styled, not professional — a real lazy morning moment in bed.
```

**合成提示：** 紫石头朝光源使色调更深 / 晨光 4500-5000K / 30-40%
**文件：** `review-05-serenity-mei.png`

---

### #6 — Serenity · ★4 · Elena F. · January 2026

**抽号：** 2-3 句 / Awe Inspired 反向升级 / Tier A / 中橄榄 / 户外阴天散步 / 侧面手腕垂落 / 摩擦#3 紫色偏灰

**文案：**
> Have to be honest — the purple is more grey-toned in person than the photos suggested. It threw me off at first, but in real daylight I actually love it more. Feels less candy and more like a real stone.

**Prompt：**
```
A casual phone photograph taken from a side angle at waist level, showing a forearm hanging naturally at the side of the body while walking outdoors on an overcast city afternoon. Medium olive skin tone with a soft warm undertone. Short natural nails with a quiet dusty mauve polish, slightly grown out at the cuticle. No bracelet, no watch, no rings — the forearm and lower arm area is completely bare and unobstructed, leaving clean open space where a bracelet could be added later. The arm is relaxed and gently swinging, fingers loose, captured in a natural mid-step moment. A dark charcoal grey wool coat with the sleeve ending just above the wrist area is the upper part of the frame, and below the arm a glimpse of deep indigo straight-leg jeans is partly visible. The background is a softly blurred urban sidewalk on a cloudy afternoon — the suggestion of grey concrete pavement, the muted edge of a brick building wall, a few bare tree branches in the upper distance, all in cool desaturated tones. The lighting is the flat soft even quality of a fully overcast sky — no harsh shadows, no warm golden tones, just clean honest cool daylight that reveals true colors accurately. The color temperature is cool, around 6500K, the kind of light that doesn't lie. The composition is intentionally off-center, the forearm sits in the right side of the frame with the urban background filling the left. The angle is from the side at waist level as if a friend walking next to her quickly snapped a photo of her arm mid-stride. Slightly motion-blurred at the edges from the casual capture, the kind of phone photo taken without stopping to pose. Cool, contemplative, urban afternoon mood. Slightly desaturated, no filter, no warmth pushed in post. Real, candid, unposed walking moment.
```

**合成提示：** 冷光保持真实紫色不要修暖 / 阴影柔不要重 / 30-40%
**文件：** `review-06-serenity-elena.png`

---

### #7 — Serenity · ★5 · Naomi A. · February 2026

**抽号：** 4-5 句 / Awe×Mejuri 行为驱动 / Tier A / 深棕 / 车里 + 拆包 / 自俯拍 / unboxing 变体

**文案：**
> I genuinely could not wait to get home. Opened the package in my car the second I got back. The way the purple catches the light is even better than I'd hoped. Already wore it out the same night.

**Prompt：**
```
A casual phone photograph taken from above, looking down at a lap in the driver's seat of a car parked in a daytime parking lot. Deep rich brown skin tone with a warm glow. A forearm and hand resting on the lap, the lower arm completely bare and unobstructed, leaving clean open space where a bracelet could be added later. Short clean nails with a glossy nude polish. No bracelet, no watch, no rings — wrist area completely empty for compositing. A camel wool coat sleeve is pushed up loosely past the wrist, with a soft cream cashmere sweater layer visible underneath. On the lap, a small open jewelry package — a soft natural linen drawstring pouch laid open beside a folded square of cream tissue paper with subtle texture, and a small card with handwritten-style serif text resting on top of the tissue. The package looks freshly opened, the contents arranged in a slightly spontaneous way as if just unwrapped seconds ago. The lower portion of the frame shows the edge of a black leather steering wheel with subtle stitching, and the bottom of the windshield revealing soft afternoon daylight outside — the suggestion of a parking lot with blurred trees and sky in the distance. Bright but soft natural daylight pours through the windshield from the front, creating a clean even glow across the lap, the package, and the arm. Some warm reflected light bounces off the camel coat. The car interior is in soft shadow at the edges of the frame, but the lap area is bright and clear. The composition is intentionally off-center — the package and forearm sit in the upper-left, the steering wheel edge and windshield in the lower right. The angle is from above as if she pulled out her phone with one hand and snapped a quick photo of the moment she opened the package in the car. Bright, excited, can't-wait afternoon mood. Slightly grainy phone photo quality, no filter. Real, candid, unposed unboxing-in-car moment.
```

**合成提示：** 特殊 — 手链 P 在棉纸/亚麻袋上而非戴在手腕 / 日光 5500K
**文件：** `review-07-serenity-naomi.png`

---

### #8 — Serenity · ★5 · Claire D. · March 2026

**抽号：** 1 句 / Mejuri clean / Tier A / 浅色 / Brunch 餐桌 / 朋友隔桌对拍

**文案：**
> Three of my friends asked where it was from at brunch — that says it all.

**Prompt：**
```
A casual phone photograph taken from across a brunch table by a friend sitting opposite, looking slightly down at a forearm and hand resting near the base of a tall glass on a marble brunch table. Fair skin with a warm undertone, smooth and clean. Short clean nails with a soft blush polish, freshly done but not perfect. No bracelet, no watch, no rings — the forearm and lower arm area is completely bare and unobstructed, leaving clean open space where a bracelet could be added later. The hand rests gently beside a tall fluted glass holding a half-finished mimosa, the orange liquid catching the warm light, condensation visible on the glass. A soft cream silk blouse sleeve falls just past the wrist area, slightly draped and natural. On the marble table around the hand, a small white plate with the remains of avocado toast partly visible, a half-eaten croissant on a wooden board to the side, a small stoneware coffee cup with a saucer in the upper-left of the frame, and the corner of a linen napkin softly bunched near the plate. The marble table has subtle grey veining and a faint warm sheen, with a few crumbs and a coffee ring suggesting the meal has been going on for a while. Bright soft natural light pours in from a large brunch spot window on the left, creating a warm directional glow across the table and the forearm, with soft shadows in the marble. The background is softly blurred, suggesting a bright airy brunch restaurant — the warm out-of-focus shapes of other tables, plants, and morning sun. The composition is slightly off-center, the hand and mimosa glass sit in the lower-right portion of the frame with the table spread filling the upper-left. The angle is from across the table at a slight downward tilt, about 25 degrees, as if her friend across the table casually picked up her phone mid-conversation and snapped a photo. Slightly soft focus in the background. Warm, social, late-morning Sunday brunch mood. Slightly grainy phone photo quality, no filter, no styling. Real, candid, mid-conversation moment.
```

**合成提示：** 餐厅暖光 4500-5000K / mimosa 橙色反射保留 / 30-40%
**文件：** `review-08-serenity-claire.png`

---

### #9 — Aura · ★5 · Rachel M. · January 2026

**抽号：** 2-3 句 / Awe Inspired 核心 / Tier A / 中暖+晒痕 / 户外露台午后阳光 / 自伸臂 / 10 周年丈夫送 + 婚戒叠戴

**文案：**
> My husband gave this to me for our 10-year anniversary. He said the rainbow of stones reminded him of all the years strung together. I haven't taken it off in two months.

**Prompt：**
```
A casual phone photograph taken at arm's length, looking down at a forearm extended outward along the wooden armrest of an outdoor patio chair on a bright summer afternoon. Medium warm tan skin tone with a light scatter of natural sun freckles on the forearm, the kind of skin that's been outside a few times this season. Short clean nails with a soft warm peach polish. A delicate thin gold wedding band on the ring finger, simple and worn-in, catching a small glint of sunlight — but no bracelet, no watch — the forearm and lower arm area is completely bare and unobstructed, leaving clean open space where a bracelet could be added later. A soft sleeveless white linen top is partly visible at the upper edge of the frame, the strap thin and delicate. The wooden patio armrest has a warm honey-toned grain, slightly weathered from sun exposure, with a faint ring mark from a past glass. Bright direct afternoon sunlight pours down from the upper-right at a steep angle, creating clear warm highlights across the forearm and the wood, with a defined sharp shadow falling to the left of the arm onto the armrest. The light is the strong, slightly overexposed quality of mid-afternoon summer sun. The background is a softly blurred backyard or garden patio — the suggestion of green leaves, dappled light through trees, and a hint of a hammock or another patio chair in the warm distance. The composition is slightly off-center, the forearm sits diagonally across the frame from lower-left to upper-right, with greenery and warm light filling the upper portion. The angle is at arm's length as if she casually extended her arm out into the sun and held up her phone with the other hand to snap a quick photo. Slightly overexposed in the brightest highlights — typical of a phone shot in direct sun. Warm, golden, summery, content mood. No filter, no styling — a real lazy afternoon moment outside.
```

**合成提示：** 强阳光左下硬阴影 / 每颗石头要有高光点 / 5000-5500K / 保留过曝
**文件：** `review-09-aura-rachel.png`

---

### #10 — Aura · ★5 · Margaret H. · December 2025

**抽号：** 2-3 句 / Awe Inspired / Tier A / 年长冷浅 / 窗边阅读角午后软光 / 自俯拍 / 母亲节女儿送

**文案：**
> My daughter gave me this for Mother's Day last year. I was worried it would be too flashy at my age, but the way the stones sit together feels almost classical. I get compliments from women half my age.

**Prompt：**
```
A quiet phone photograph taken from above, looking straight down at a forearm and hand resting gently on the open pages of a hardcover novel held in the lap. Cool fair skin tone with a soft natural quality. Short clean nails with a sheer pearly polish, neat and well-cared-for. A delicate slim platinum wedding band on the ring finger and a small antique-looking opal ring on the pinky, but no bracelet, no watch — the forearm and lower arm area is completely bare and unobstructed, leaving clean open space where a bracelet could be added later. A soft dusty lavender cashmere cardigan sleeve falls just past the wrist area, the knit fine and well-worn, the kind of cardigan that has been a favorite for years. The hardcover novel underneath is open to the middle of a chapter, the cream pages slightly aged, the typeset old-fashioned serif. A pair of thin tortoiseshell reading glasses with delicate gold temples lies folded on the corner of the book, partly visible at the upper edge of the frame. Beside the book, the soft edge of a moss green wool throw blanket is visible across the lap. Soft warm afternoon light pours in from a tall window on the left side, filtered slightly through sheer linen curtains, creating a gentle directional glow across the forearm, the book pages, and the cardigan, with quiet soft shadows falling to the right. The light has the slow honeyed quality of a winter afternoon around 3pm. The background is softly blurred — the suggestion of a window with bare tree branches outside, a small side table with a teacup and a vase of dried lavender, all in muted warm tones. The composition is slightly off-center, the forearm and book sit in the lower-right portion of the frame, with the throw blanket and side table filling the upper-left. The angle is from directly above as if she gently held her phone in her free hand and snapped a photo of her own arm resting on her book during a quiet afternoon read. Warm, intimate, peaceful, slow afternoon mood. Slightly grainy phone photo quality, no filter, no styling. Real, candid, quiet domestic moment.
```

**合成提示：** 软窗光透纱帘 / 不要遮书页字 / 4000-4500K / 婚戒 opal 不抢戏
**文件：** `review-10-aura-margaret.png`

---

### #11 — Aura · ★4 · Anya P. · February 2026

**抽号：** 4-5 句 / Awe 诚实成年版 / Tier A / 中等中性 / 窗边书桌 + 拆包 / macro 特写 / 摩擦#4 物流 11 天

**文案：**
> Took 11 days to arrive which felt like forever for a $365 bracelet. I almost cancelled twice. Then I opened the box and got it. The stones are all slightly different shapes — not uniform, very alive. Worth the wait, but I think the brand should be honest about lead times upfront.

**Prompt：**
```
A close-up phone photograph taken at very near range, looking down at a forearm and hand resting on a light wooden home desk surface beside an opened jewelry package, the camera held only a few inches away from the wrist area for an intimate macro feel. Medium neutral skin tone with a soft natural quality. Short clean nails with a dusty taupe polish, slightly worn at the tips. No bracelet, no watch, no rings on this hand — the forearm and lower arm area is completely bare and unobstructed, leaving clean open space where a bracelet could be added later. A soft heather grey waffle-knit sweater sleeve is pushed up loosely past the wrist area. On the desk beside the arm, a freshly opened jewelry package — a soft natural linen drawstring pouch laid open to one side, a folded square of cream tissue paper unfolded with subtle texture, and a small handwritten-style serif card resting nearby. The package looks just-opened, with the contents arranged in a slightly spontaneous casual way. The light wooden desk has visible warm grain, a few faint pen marks, and a small ceramic mug with a cooling herbal tea in the upper-left of the frame. Soft warm late afternoon light pours in from a tall window on the left side, creating a clear directional glow across the forearm, the package, and the desk surface, with gentle soft shadows falling to the right. The window itself is partly visible at the upper-left edge of the frame, the light filtered through sheer white curtains. The composition is intentionally tight and slightly off-center, the wrist area filling most of the lower-right portion of the frame in soft macro focus, with the package and desk filling the rest. The angle is from very close above, as if she leaned in with her phone in her free hand to capture the wrist and the package together in one tight frame, the kind of slightly too-close shot a phone takes when you can't quite get the focus right. Slight soft focus around the edges of the frame from the close range. Warm, intimate, post-arrival mood. No filter, no styling — a real just-arrived afternoon moment at home.
```

**合成提示：** macro 特写比例可放大到 40-50% / 选可见多颗石头形状差异的角度 / 边缘失焦保留
**文件：** `review-11-aura-anya.png`

---

### #12 — Obsidian · ★5 · Imani K. · January 2026

**抽号：** 2-3 句 / Mejuri clean confident / Tier A / 深棕 / 卧室全黑造型镜子 / 镜子自拍

**文案：**
> Wore it out the same night I got it. The black stones with everything black is a whole look.

**Prompt：**
```
A casual mirror selfie phone photograph taken in a softly lit bedroom, framed from upper chest down to upper thigh, showing a torso turned slightly toward a full-length mirror with one hand resting on the hip and the other holding the phone at chest level. Deep rich brown skin tone with a soft natural sheen on the forearms. Short clean nails with a glossy black polish. The hand resting on the hip has a delicate slim silver ring on the index finger but no bracelet, no watch — the forearm and lower arm area on the hip-resting hand is completely bare and unobstructed, leaving clean open space where a bracelet could be added later. The outfit is entirely black: a soft black ribbed long-sleeve turtleneck top, fitted but not tight, paired with high-waisted black wide-leg trousers, the sleeves of the turtleneck pushed up loosely past the wrist area on both arms. The phone in the other hand is a slim black smartphone, partially visible at chest level in the reflection, slightly obscuring part of the upper face area which is naturally cropped out of frame by the casual angle. The mirror is a tall full-length frame with a thin matte black metal border. The bedroom background visible in the mirror is softly cluttered and lived-in — a partly made bed with a charcoal grey duvet and one slightly askew pillow, an open closet door at the edge with a few hangers visible, a small wooden side table with a half-burnt black candle and a stack of books, all in muted dark warm tones. Soft warm bedroom lighting from a single lamp on the side table creates gentle directional light across the torso and arms, with soft warm shadows in the folds of the turtleneck. The lighting is intimate, low-key, evening getting-ready vibe, around 7pm. The composition is casually framed — the body sits slightly off-center in the mirror, with the cluttered bedroom background filling the surrounding space. Slightly grainy phone photo quality typical of low-light indoor shots, no filter, no styling. Confident, sleek, going-out-tonight mood. Real, candid, unposed mirror selfie moment.
```

**合成提示：** 暖室内灯 3500-4000K / 黑石头要有高光点不要死黑 / 不要修脸
**文件：** `review-12-obsidian-imani.png`

---

### #13 — Obsidian · ★5 · Lara M. · February 2026

**抽号：** 2-3 句 / Awe Inspired / Tier A 必须男手 / 男性浅暖 / 男性工作间 / 自俯拍 / 男友礼物 (性别变奏)

**文案：**
> Bought this for my boyfriend's birthday. He doesn't usually wear jewelry but he hasn't taken this off. Says the weight feels grounding.

**Prompt：**
```
A casual phone photograph taken from above, looking straight down at a man's bare forearm and hand resting on a worn wooden workbench in a small home workshop or garage corner. Fair-medium warm skin tone with the natural texture of a working hand — visible knuckles, a small faint old scratch near the wrist area, light fine arm hair on the forearm. Short clean practical nails, unmanicured, slightly utilitarian. No bracelet, no watch, no rings — the forearm and lower arm area is completely bare and unobstructed, leaving clean open space where a bracelet could be added later. A faded charcoal grey heavyweight cotton t-shirt sleeve is partly visible at the upper edge of the frame, the cotton softened from many washes. The wooden workbench underneath has deep visible grain, a few old paint marks, several pencil notations, and a faint coffee ring — clearly used, clearly real. Around the arm on the bench, a few honest workshop objects: a small folding pocket knife resting closed, a worn leather notebook with a cracked spine, a simple ceramic mug with cooling black coffee in the upper-left of the frame, and the edge of a small wood plane tool partly visible at the right edge. Soft warm directional light from a single bare window on the left side, the kind of late morning light filtering into a workshop space, creating a clear gentle glow across the forearm and the workbench with defined soft shadows falling to the right. The light has a slightly dusty quality from the workshop atmosphere. The background is a softly blurred suggestion of a workshop wall with hanging tools and a small shelf with jars, all in warm muted brown and grey tones. The composition is slightly off-center, the forearm sits diagonally across the lower portion of the frame from upper-left to lower-right, with the workshop objects filling the surrounding space. The angle is from directly above as if he held his phone in his free hand and casually snapped a photo of his own forearm on the workbench mid-project. Warm, grounded, masculine, lived-in workshop mood. Slightly grainy phone photo quality, no filter, no styling. Real, candid, unposed working moment.
```

**合成提示：** 男手宽 → 比例缩到 25-30% / 让手链像 EDC 不像装饰 / 不要修工作感
**文件：** `review-13-obsidian-lara.png`

---

### #14 — Obsidian · ★4 · Beth O. · January 2026

**抽号：** 2-3 句 / Mejuri clean 诚实 / Tier A / 浅暖 / 办公桌 + Apple Watch 叠戴 / 自俯拍 / 摩擦#5 银配件勾袖

**文案：**
> Wears really well — I've been putting it on every morning for work. The only thing is the silver detail catches on my sweater sleeves sometimes. Not enough to stop wearing it though, just something to know.

**Prompt：**
```
A casual phone photograph taken from above, looking straight down at a forearm and hand resting near the trackpad of an open silver laptop on a light wooden home office desk. Fair skin with a warm undertone, the kind of skin that doesn't get much sun in winter. Short clean nails with a quiet bare buff polish, neat but practical. A modern smartwatch with a soft taupe leather band sits on the wrist closer to the elbow, the watch face dark and small — but the area of the forearm between the watch and the hand is completely bare and unobstructed, leaving clean open space where a bracelet could be added later. A soft camel cashmere sweater sleeve is pushed up loosely past the watch area, the cashmere slightly pilled near the cuff from many wears. On the desk around the laptop, a small open spiral notebook with a few lines of handwritten notes in blue ink, a black ballpoint pen lying diagonally across the page, a half-finished mug of black coffee with a faint cooling ring on the desk surface, and a small green succulent in a terracotta pot in the upper-left corner of the frame. The wooden desk has visible warm grain and a few faint old marks from years of work. Soft mid-morning natural light enters from a window on the left side, creating a clear gentle glow across the desk, the laptop, and the forearm, with soft shadows falling to the right. The light has the clean even quality of an unhurried Tuesday morning around 9:30am. The composition is slightly off-center, the forearm and laptop trackpad sit in the lower-right portion of the frame, with the notebook, coffee mug, and succulent filling the upper-left. The angle is from directly above as if she paused mid-email and casually held her phone above her own arm to snap a quick photo. Warm, focused, productive Tuesday morning mood. Slightly grainy phone photo quality, no filter, no styling. Real, candid, mid-work-session moment.
```

**合成提示：** 手链在手表和手掌之间不重叠 / 银配件留高光 / 5000K / 保留袖口起球
**文件：** `review-14-obsidian-beth.png`

---

### #15 — Terra · ★5 · Helena S. · February 2026

**抽号：** 1 句 / Awe Inspired 浓缩 / Tier A / 中暖 / 厨房台面拆姐妹邮件 / 自俯拍 / 姐妹无缘由邮寄

**文案：**
> My sister mailed this to me out of the blue — I opened the box standing in my kitchen and immediately cried.

**Prompt：**
```
A casual phone photograph taken from above, looking straight down at a forearm and hand resting on a creamy white quartz kitchen counter beside a freshly opened cardboard mailer envelope. Medium warm skin tone with a soft natural glow. Short clean nails with a quiet warm taupe polish, slightly worn at the tips. No bracelet, no watch, no rings — the forearm and lower arm area is completely bare and unobstructed, leaving clean open space where a bracelet could be added later. A soft oatmeal-colored cotton sweatshirt sleeve is pushed up loosely past the wrist area, the cotton softened from many washes, the cuff slightly stretched. On the counter beside the hand, a small kraft brown cardboard mailer envelope torn open along one side, the packing tape pulled back, with a soft natural linen drawstring pouch and a folded square of cream tissue paper partly emerging from the opening. A small handwritten serif card rests on the tissue paper. Around the package on the counter, a half-finished mug of black coffee in a warm earth-toned ceramic cup, a small plate with the crumbs of a half-eaten piece of toast, and the corner of a folded morning newspaper at the upper edge of the frame. A small ceramic vase with a single sprig of dried eucalyptus sits in the upper-left corner. The quartz counter surface has subtle warm veining and a few faint old water marks — clearly used, clearly real. Soft warm morning light enters from a kitchen window on the left side, creating a gentle directional glow across the counter, the package, and the forearm, with soft shadows falling to the right. The light has the quiet honeyed quality of a slow weekday morning around 8am. The composition is slightly off-center, the forearm and the opened mailer sit in the lower-right portion of the frame, with the breakfast items filling the upper-left. The angle is from directly above as if she stood at the counter holding her phone in her free hand and snapped a photo of the moment she opened the unexpected package. Warm, intimate, emotional morning mood. Slightly grainy phone photo quality, no filter, no styling. Real, candid, just-opened-a-surprise-from-someone-I-love moment.
```

**合成提示：** 双层包装外 kraft 内 Kinsoul / 4500-5000K / 不要让手链抢戏
**文件：** `review-15-terra-helena.png`

---

### #16 — Terra · ★5 · Carla R. · March 2026

**抽号：** 1 句 / Mejuri×Awe 短诗 / Tier A / 中暖晒痕 / 沙滩 / 自伸臂 / 度假

**文案：**
> Took it to Mexico last week — looks like every shell I picked up off the sand.

**Prompt：**
```
A casual phone photograph taken at arm's length, looking down at a forearm extended outward across warm golden beach sand on a bright sunny vacation afternoon. Medium warm skin tone with a fresh light tan from a few days at the beach, the kind of glow you get on day three of a trip. Short clean nails with chipped soft coral polish — clearly the polish has been in salt water and sand for several days, with small jagged worn spots near the tips. No bracelet, no watch, no rings — the forearm and lower arm area is completely bare and unobstructed, leaving clean open space where a bracelet could be added later. The arm is relaxed and gently spread on the sand, fingers loosely curled, a few grains of sand visible on the back of the hand and along the forearm. The sand underneath is warm golden-beige with the natural texture of small grain patterns and a few tiny shells partly buried near the fingers — pinkish, white, and cream colored small shells, the kind you collect on a walk. In the very softly blurred upper background, the edge of bright turquoise ocean water is partly visible meeting a thin line of white foam and a clear sky, all in slightly over-bright vacation tones. Direct overhead afternoon sunlight pours down at a steep angle, creating clear warm highlights across the forearm and the sand, with sharp short shadows in the sand grain texture and a defined shadow falling beneath the fingers. The light has the strong, slightly hazy quality of tropical mid-afternoon sun. The composition is loose and slightly off-center — the forearm sits diagonally across the lower-right portion of the frame, with sand and a hint of ocean filling the upper-left. The angle is at arm's length as if she casually extended her arm out across the sand and held up her phone with the other hand to snap a quick vacation photo. Slightly overexposed in the bright highlights — typical of a phone shot in direct tropical sun. Warm, golden, salty, vacation mood. No filter, no styling — a real lazy beach moment on day three of a trip.
```

**合成提示：** 正下方短阴影 / 5000-5500K / 让石头有清晰轮廓不融入沙色 / 保留过曝
**文件：** `review-16-terra-carla.png`

---

### #17 — Terra · ★4 · Sofia L. · January 2026

**抽号：** 2-3 句 / Mejuri 反向升级 / Tier B / 中橄榄 / 厨房做饭 / 自俯拍 / 摩擦#6 石头不规则

**文案：**
> Each stone is a different shape and a different shade. I noticed it the second I unwrapped it and almost felt disappointed. A week in, it's the thing I love most about it.

**Prompt：**
```
A casual phone photograph taken from above, looking straight down at a forearm and hand resting near the edge of a worn wooden cutting board on a creamy stone kitchen counter, mid-cooking. Medium olive skin tone with a soft warm undertone. Short clean nails with a natural buff polish, slightly worn. No bracelet, no watch, no rings — the forearm and lower arm area is completely bare and unobstructed, leaving clean open space where a bracelet could be added later. A soft sage linen button-down shirt sleeve is rolled up loosely past the wrist area, the linen slightly wrinkled from the morning. On the cutting board beside the hand, a small pile of freshly chopped flat-leaf parsley with a few stray leaves scattered around it, a halved lemon with the cut side up showing the bright pulp, and a small wooden-handled paring knife resting at an angle. The cutting board is well-used with deep knife marks and a few faint dark stains from years of cooking. Around the cutting board on the counter, a small ceramic bowl with sea salt flakes, a half-full mason jar of olive oil with a pour spout, and the corner of a worn cookbook open to a recipe page in the upper-left of the frame. The stone counter has subtle warm veining and a few faint old water marks. Soft warm late morning light enters from a kitchen window on the left side, creating a gentle directional glow across the counter, the cutting board, and the forearm, with soft shadows falling to the right. The light has the slow honeyed quality of an unhurried weekend cooking session around 11am. The composition is slightly off-center, the forearm and the cutting board sit in the lower-right portion of the frame, with the cookbook and other ingredients filling the upper-left. The angle is from directly above as if she paused mid-chop and casually held her phone in her free hand to snap a quick photo of her own arm beside the board. Warm, intimate, slow weekend cooking mood. Slightly grainy phone photo quality, no filter, no styling. Real, candid, mid-recipe moment.
```

**合成提示：** 选多颗石头形状差异角度 / 4500K / 不要修切板污渍
**文件：** `review-17-terra-sofia.png`

---

### #18 — Soleil · ★5 · Yuna K. · February 2026

**抽号：** 4-5 句 / Awe Inspired 跨代叙事 / Tier B / 东亚年轻 / 校园斑驳阳光 / 侧面手腕垂落 / 妈妈毕业礼物

**文案：**
> My mom gave this to me when I graduated last spring. She said yellow was the color of the sweater she wore the day she got into the university she'd dreamed of. I didn't know that until she told me. I think about it every time the light catches the stones.

**Prompt：**
```
A casual phone photograph taken from a side angle at waist level, showing a forearm hanging naturally at the side of the body while walking along a sun-dappled outdoor path on a bright spring afternoon. East Asian skin tone, smooth and even with a soft fresh quality. Short clean natural nails with no polish, just a quiet bare nail look. No bracelet, no watch, no rings — the forearm and lower arm area is completely bare and unobstructed, leaving clean open space where a bracelet could be added later. The arm is relaxed and gently swinging mid-stride, fingers loose, captured in a natural mid-step moment. A soft faded denim jacket sleeve with a subtle worn cuff is the upper part of the frame, with a thin cotton white t-shirt layer just visible underneath at the wrist. Below the arm, a glimpse of soft worn-in light blue jeans is partly visible. The background is a softly blurred outdoor path on a sunny afternoon — the suggestion of warm grey paving stones, the muted edges of green spring leaves overhead, dappled sunlight breaking through tree branches, and the warm distant blur of a sunny campus or park in the background, all in fresh spring tones. Bright direct afternoon sunlight breaks through the leaves overhead in shifting patches, creating warm dappled highlights across the forearm and the path, with soft moving shadows from the leaves. The light has the bright hopeful quality of late spring around 2pm. The color temperature is warm and clean, slightly golden. The composition is intentionally off-center, the forearm sits in the lower-right of the frame with the dappled sunlit path filling the rest. The angle is from the side at waist level as if a friend walking next to her quickly snapped a photo of her arm mid-stride. Slightly motion-blurred at the edges from the casual capture, the kind of phone photo taken without stopping to pose. Bright, hopeful, warm, spring-afternoon mood. Slightly grainy phone photo quality, no filter, no styling. Real, candid, unposed walking moment.
```

**合成提示：** 斑驳光手链上要有 1-2 个亮点 / 5000-5500K / 金石头被点亮的瞬间感
**文件：** `review-18-soleil-yuna.png`

---

### #19 — Soleil · ★5 · Adaeze N. · March 2026

**抽号：** 1 句 / Awe Inspired 浓缩 + 友谊 / Tier B / 深棕 / 浴室晨间镜子 / 镜子自拍 / 闺蜜 brunch 礼物

**文案：**
> My best friend put this on my wrist at brunch and refused to let me give it back.

**Prompt：**
```
A casual mirror selfie phone photograph taken in a softly lit bathroom in the early morning, framed from upper chest down to mid-thigh, showing a body turned slightly toward a wall-mounted bathroom mirror with one hand resting near the hip and the other holding the phone at chest level. Deep rich brown skin tone with a soft natural morning glow, slightly damp at the edges. Short clean nails with a soft warm cream polish. The hand resting near the hip has a small delicate gold chain ring on the index finger but no bracelet, no watch — the forearm and lower arm area on the hip-resting hand is completely bare and unobstructed, leaving clean open space where a bracelet could be added later. The outfit is a soft cream waffle-knit cotton robe loosely tied at the waist, sleeves falling just past the elbow, modest and cozy, with a thin white cotton cami visible at the chest area underneath. The phone in the other hand is a small cream-cased smartphone, partially visible at chest level in the reflection, slightly obscuring the upper face area which is naturally cropped out of frame by the casual angle. Hair is half-dry, soft natural texture, hanging loose. The bathroom mirror is a simple round frame with a thin matte gold border. The bathroom background visible in the mirror is softly lived-in — a small white floating shelf with a half-used tube of toothpaste, a small ceramic cup holding a toothbrush, a glass jar of cotton rounds, and a small terracotta pot with a trailing plant, all in warm muted tones. A soft cream linen hand towel hangs slightly askew from a hook to the side. Bright soft natural morning light pours in from an unseen window above, creating a gentle directional glow across the body, the robe, and the bathroom counter, with a fresh airy clean quality. The light has the optimistic morning quality of around 8am. The composition is casually framed — the body sits slightly off-center in the mirror, with the cluttered bathroom background filling the surrounding space. Slightly soft focus from the bathroom humidity in the air. Bright, fresh, optimistic morning getting-ready mood. Slightly grainy phone photo quality, no filter, no styling. Real, candid, unposed bathroom morning mirror moment.
```

**合成提示：** 5000K 偏冷于 #12 / 金石头自然发光 / 半干头发不修
**文件：** `review-19-soleil-adaeze.png`

---

### #20 — Soleil · ★4 · Hannah W. · January 2026

**抽号：** 1 句 / Awe×Mejuri 诚实 / **Tier C 故意松散** / 浅色 / 办公室午休普通桌 / 朋友隔桌对拍 / 摩擦#2 尺码指南不清 + 配偶送

**文案：**
> My husband got it for me but the size chart confused us at first — Kinsoul's team made the swap really easy though.

**Prompt：**
```
A casual phone photograph taken from across a small office breakroom table by a coworker sitting opposite, looking slightly down at a forearm and hand resting flat on a basic light grey laminate table during a weekday lunch break. Fair skin with a soft cool undertone, slightly pale from indoor office life. Short clean nails with no polish, just bare and practical. No bracelet, no watch, no rings — the forearm and lower arm area is completely bare and unobstructed, leaving clean open space where a bracelet could be added later. A simple navy blue cotton button-down shirt sleeve is rolled up loosely past the wrist area, the cotton slightly wrinkled from a half day of work. On the table near the hand, a half-eaten turkey sandwich on whole wheat bread sits on a piece of crinkled brown deli paper, a small plastic cup of black coffee with a lid removed, a crumpled paper napkin, and a small bag of plain potato chips half-open, with a few stray chip crumbs on the table. The corner of a manila folder with some stuck-on post-it notes is partly visible at the upper edge of the frame. The laminate table has a few faint old water marks and a small ink stain near the edge — the kind of breakroom table that has seen years of lunches. The lighting is the slightly flat mixed quality of typical office space — overhead fluorescent light combined with cool natural light from a distant window on the right side, creating soft even illumination with minimal directional shadow. The color temperature is slightly cool and neutral, around 5500K, the kind of unremarkable indoor lighting that doesn't try to flatter anyone. The background is softly blurred, suggesting a generic office breakroom — the muted shapes of a vending machine corner, a wall clock, and a window showing a grey office building across the street. The composition is mildly off-center but not dramatically — the forearm sits roughly centered with the lunch items spread around it, the kind of casual composition you get when a coworker just snapped a quick photo without thinking about framing. The angle is from across the table at about 25 degrees down. The photo is unremarkable in every way — flat lighting, ordinary food, ordinary table, ordinary clothes. Neutral, mundane, mid-week midday mood. Slightly grainy phone photo quality, no filter, no styling. The kind of photo someone takes while half-listening to a coworker. Real, ordinary, unstaged, completely uncurated.
```

**合成提示：** 5500K 偏冷不要修暖 / 金石头克制不闪 / 不要美化任何东西 / 乏味就是真实
**文件：** `review-20-soleil-hannah.png`

---

## 图片上传工作流（重要）

`templates/index.json` 已经把 20 条评论按 `review_01` ~ `review_20` 的 block key 写好，每个 block 的 `image` 字段预填了 `shopify://shop_images/review-XX-product-name.png`。

**你只需要做一件事：**

1. 在本地（PS 合成完毕的图）按上面 20 条对应的"文件"字段命名图片
2. 打开 Shopify Admin → **Settings → Files**
3. 点击 **Upload files**，**一次性把 20 张 jpg 全部拖进去**
4. 上传完成后**不需要做任何手动绑定** —— Shopify 会通过文件名自动匹配 `index.json` 里的引用

**核心原则：文件名必须 100% 一致**，包括小写、连字符、`.png` 扩展名。

如果你之后想换某条评论的图：
- 同名覆盖上传 → 自动替换
- 或者改 `index.json` 里那条 block 的 image 字段值

如果某张图还没上传，前端只会显示空 placeholder（已在 section 代码里处理），不会报错。

---

## v2 文件清单

- `REVIEW-SYSTEM.md` (v1，作废，保留作历史)
- `REVIEW-SYSTEM-V2.md` (本文件)
- `templates/index.json` (已写入 20 条 block)
- `sections/kinsoul-social-proof.liquid` (无需修改)
- 20 张图片：`review-01-ember-jasmine.png` ... `review-20-soleil-hannah.png`
