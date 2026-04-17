# P1 Klaviyo 弹窗触发改 — Admin 操作清单

**上下文**：目前 kinsoulenergy.com 首次访问 **3 秒内 Klaviyo 弹窗全屏阻挡所有交互**，新客户第一个动作被迫变成"关闭弹窗"。这是单个最大转化杀手。代码层改不了，必须在 Klaviyo 后台改。

## 目标触发规则

| 设备 | 触发条件 | 原因 |
|---|---|---|
| **桌面** | 访客停留 **30s** **且** 滚动深度 ≥ **60%**，或 exit-intent（鼠标移至浏览器 tab 区） | 访客表现出浏览兴趣后再请注册，不阻断初次探索 |
| **移动** | 访客停留 **45s** **且** 滚动深度 ≥ **70%** | 移动端不能用 exit-intent（没鼠标事件），用更保守的停留+滚动阈值 |

## 操作步骤

1. 登录 Klaviyo → 左侧 **Signup Forms**
2. 找到 kinsoulenergy 的"Join Our Kinsoul Family"弹窗（当前弹 3s 触发的那个）
3. 点 **Edit** → **Behavior** 或 **Display rules** 标签
4. **当前设置**（要改掉）：`Show form after 3 seconds on page`
5. **改为**：

### 桌面规则（create new rule for desktop）
- Device: **Desktop / Tablet**
- Trigger: **Exit intent** (primary)
- Fallback trigger: `User has been on page for 30 seconds` **AND** `Scroll depth ≥ 60%`

### 移动规则（create new rule for mobile）
- Device: **Mobile**
- Trigger: `User has been on page for 45 seconds` **AND** `Scroll depth ≥ 70%`

6. **频次控制**：
   - `Don't show if dismissed in the last 14 days`（避免反复打扰）
   - `Don't show to users who already subscribed`（登录/已订阅跳过）

7. 点 **Publish changes** 生效

## 验证方式

1. 用隐身模式访问 `https://www.kinsoulenergy.com/`
2. **桌面**：不滚动 30s 后弹窗**不应**出现；滚到 60% 后应出现；或把鼠标移到上方浏览器 tab 区应出现
3. **移动**（iPhone 或 DevTools mobile 模式）：不滚动 45s 后**不应**出现；滚到 70% 后应出现

## Newsletter 诱饵（可选，建议同步改）

首页 Newsletter 区块文案已微调，但邮件首单奖励目前没配置。建议：

1. Klaviyo → **Flows** → 创建新 flow：`Welcome series - first-time subscribers`
2. Trigger: `List membership change` → 加入 Newsletter list
3. Action: 发送 email with `10% off first order` 或 `$20 off orders over $200` 折扣码
4. 折扣码由 Shopify Admin → Discounts 预生成一批，或用 Klaviyo 动态生成

---

文件创建时间：2026-04-17
下次审核：P2 发布前确认以上全部完成
