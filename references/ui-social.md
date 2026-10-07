# UI·社交媒体·截图

> 定位：一句话说明覆盖什么需求。写作前先读 2-3 条最相关样例，套用其结构而非照抄内容。
> 本文件覆盖：App UI、网页/AR 界面、直播间、社媒内容截图（X/抖音/小红书/朋友圈）、YouTube 封面、社媒帖图。

tags: UI 截图, 直播间, 社交媒体, App 界面, YouTube 封面, 小红书

## 样例

### 【App UI·产品规格化】
适用：虚构 App 的高保真手机界面截图

```text
Design a polished mobile finance app UI mockup for a fictional neobank called AURAE, shown on a 1290x2796 smartphone screen, front-facing, with a soft off-white background and subtle shadow. Use a calm palette of deep navy, mint green, warm gray, and white. Create a complete home screen with crisp typography, clean spacing, rounded cards, and precise icon alignment. Include a top header with the in-image text "AURAE", "Good morning, Lina", and "Total balance $12,480.36". Add three summary chips labeled "Income +$4,200", "Spent -$1,830", and "Saved 32%". Show a weekly spending bar chart labeled "Mon Tue Wed Thu Fri Sat Sun" and a recent transactions list with "Metro Pass $18.50", "Green Bowl $14.20", and "Rent $1,240.00". Include a bottom nav with "Home", "Cards", "Budget", and "Profile". Prioritize crisp UI hierarchy, realistic mobile app styling, sharp labels, and production-quality mockup presentation.
```

**点评**：UI 类的本质是"把每个控件当文字标注出来"——虚构产品名 AURAE 防品牌泄漏 + 精确画布尺寸 + 余额/账单/星期轴逐个给出。
**来源**：GPT-Image2-Skill · No. 103

### 【App/网页 UI 模板】
适用：模糊 UI 需求的最小完备填空骨架

```text
为[产品类型]生成一张[平台，如 iOS/Android/Web]界面图。
核心功能：[功能点A]、[功能点B]、[功能点C]。
视觉风格：[极简/科技/拟物]，主色[颜色]，强调色[颜色]。
布局：[顶部导航/双栏/卡片流]，信息层级清晰，留白充足。
输出：高保真UI截图，文字清晰可读，比例[9:16/16:9]。
```

**点评**：六行覆盖"任务-功能-风格-布局-输出约束"的最小完备集，是"模糊需求 → 完整 prompt"填空骨架的教科书。
**来源**：freestylefly-awesome-gpt-image-2 · templates.md 模板层

### 【AR 界面叠加·实拍融合】
适用：真实场景 + 悬浮科技 UI 的示意图（一组三连）

```text
Dessert (AR shopping UI)

POV shot inside a modern supermarket aisle, hands holding a small gourmet dessert with cream and berries, futuristic augmented reality (AR) interface overlay showing calories, sugar, fats, freshness score, expiry date, and recipe suggestions, soft depth of field, cinematic lighting, ultra-realistic, 4K, tech-inspired UI, clean glassmorphism design

⸻

2. Apple (AR nutrition UI)

First-person view in a grocery store holding a fresh red apple, augmented reality interface displaying calories, vitamin C, fiber, freshness bar, and recipe ideas, minimal futuristic UI panels floating around the object, bright supermarket lighting, shallow depth of field, hyper-realistic, modern tech aesthetic, 4K

⸻

3. Orange Soda Bottle (AR data UI)

POV shot of hands holding an orange soda bottle in a supermarket aisle, futuristic AR overlay showing calories, sugar content, caffeine level, freshness score, expiry date, and drink recipes, sleek holographic interface, glassmorphism UI, vibrant colors, cinematic lighting, ultra-detailed, photorealistic, 4K
```

**点评**：界面内容逐项点名（卡路里/糖分/新鲜度/到期日），风格锚定 glassmorphism，POV + 浅景深让画面像真实抓拍而非设计稿渲染。
**来源**：ai-image-prompts-skill · ID 12812

### 【直播间带货 UI·全要素复刻】
适用：抖音式电商直播界面截图，弹幕/礼物/商品卡全要素

```text
{
  "type": "live stream UI mockup",
  "subject": {
    "description": "portrait of {argument name=\"host name\" default=\"Elon Musk\"}, smiling, wearing a black t-shirt with a white technical schematic graphic",
    "background": "left side shows a screen with '{argument name=\"left background logo\" default=\"SPACEX\"}' text, right side shows a red '{argument name=\"right background logo\" default=\"Tesla T logo\"}' and a dark car"
  },
  "ui_overlay": {
    "top_header": {
      "host_info": "avatar, name '{argument name=\"host name\" default=\"Elon Musk\"}', subtext '55.6万本场点赞', red '关注' button",
      "rank_badge": "gold coin icon with '全站第1名'",
      "viewer_stats": "3 top viewer avatars with '12.3w', '8.6w', '5.7w', total '68.7万', 'X' close button",
      "right_links": "'更多直播 >', '礼物展馆 0/24' with blue '经典' tag"
    },
    "mid_left_gifts": {
      "count": 2,
      "items": [
        "avatar '科技爱好者', '送小心心', heart icon x 1314",
        "avatar '星辰大海', '送火箭', rocket icon x 666"
      ]
    },
    "bottom_left_chat": {
      "system_message": "level 37 badge '宇宙漫游者 加入了直播间'",
      "message_count": 7,
      "messages": [
        "小火箭: 马斯克！未来可期！🚀",
        "future: 特斯拉Model 2什么时候出？",
        "星空梦想家: SpaceX今年能上火星吗？",
        "AI探索者: Neuralink进展如何？",
        "帅气的网友: 马总好！",
        "Mars: 第一次来你的直播，超激动！",
        "用户123: 讲讲AI吧，会取代人类吗？"
      ]
    },
    "bottom_right_product_card": {
      "hot_tag": "orange '热卖 x 1888'",
      "image": "Tesla Cybertruck",
      "title": "{argument name=\"product name\" default=\"特斯拉Cybertruck 电动皮卡\"}",
      "price": "{argument name=\"product price\" default=\"¥ 1,618,000\"}",
      "button": "red '抢' button",
      "floating_animation": "translucent hearts floating up the right edge"
    },
    "bottom_bar": {
      "input_field": "'说点什么...'",
      "icons": ["smiley face", "three dots", "shopping cart", "gift box", "share"]
    }
  }
}
```

**点评**：平台特征复刻的完整度天花板——把 UI 拆成 header/礼物栏/聊天区/商品卡/底栏五区，连 7 条弹幕文案、徽章等级、'关注/抢'按钮颜色都逐条给出。
**来源**：awesome-gpt-image-2 · F4

### 【社媒截图模板·平台特征复刻】
适用：高仿 X/抖音/小红书/朋友圈等内容截图

```text
生成一张[平台，如 X/抖音/小红书/微信朋友圈]内容截图，[深色/浅色]模式。
整体比例：[9:16 / 3:4 / 1:1]，手机截图风格。

核心内容：
- 账号信息：[头像描述 / 用户名 / 认证标识]
- 正文内容：[具体文本内容，包含指定中文]
- 互动数据：[点赞/评论/转发/收藏数量]

界面元素：
- 顶部：[状态栏/导航栏/搜索栏]
- 底部：[操作栏/Tab栏/输入框]
- 附加：[浮窗/弹幕/礼物特效/购物车卡片]

约束：文字必须准确显示指定的中文，禁止乱码和占位文本，比例固定。
输出：高仿社交平台截图，文字清晰可读。
```

**点评**：截图三层清单（核心内容 + 界面元素顶/底/附加）+ 硬性锁定"文字必须准确显示指定中文"，直击生图模型乱码痛点；平台特征（X 蓝勾、抖音音乐碟片、小红书双列瀑布流）按坑点清单补进对应槽位。
**来源**：freestylefly-awesome-gpt-image-2 · templates.md 模板层

### 【YouTube 封面·key visual 公式】
适用：视频封面级强叙事冲击图

```text
Ultra-realistic cinematic 4K image of a {argument name="locomotive" default="colossal vintage steam locomotive racing across an enormous collapsing railway bridge"} above a violent ocean during a {argument name="weather" default="supernatural-looking but physically grounded thunderstorm"}. The train is captured at the exact moment a massive wave crashes against the bridge far below, while lightning illuminates the entire scene. Hundreds of rain droplets freeze sharply in the foreground, reflecting tiny fragments of light. The locomotive is incredibly detailed: weathered black steel, polished brass components, glowing furnace light, realistic steam escaping from valves, wet metallic surfaces, spinning wheels throwing water and sparks against the rails.

The environment is breathtaking and immense: towering dark cliffs disappearing into storm clouds, a distant lighthouse barely visible through heavy rain, enormous waves exploding against rocks, dramatic clouds spiraling across the sky, mist flowing beneath the bridge, broken sections of railway disappearing into the distance. A {argument name="mystery detail" default="lone passenger silhouette is visible through one warmly illuminated train window"}, creating mystery and emotional storytelling.

Composition uses an extreme low-angle perspective from beside the railway tracks, making the locomotive feel enormous and powerful. Strong leading lines from the rails pull the eye directly toward the train. Lightning provides dramatic backlighting and creates a brilliant rim around the locomotive and steam. Warm interior light contrasts naturally against the cold storm atmosphere. Photorealistic materials, physically accurate reflections, realistic rain behavior, atmospheric perspective, volumetric mist, cinematic depth of field, subtle motion blur on the wheels while the locomotive remains razor sharp, HDR lighting, natural film grain, incredible micro-details, realistic scale, professional Hollywood cinematography, 35mm anamorphic lens aesthetic, high dynamic range, breathtaking visual storytelling, crystal-clear 4K Ultra HD, no text, no logo, no watermark, no artificial-looking CGI, no cartoon style.

The key visual: gigantic train + collapsing bridge + ocean storm + lightning + tiny human silhouette = scale, danger, mystery, and cinematic storytelling in one frame.
```

**点评**：结尾"The key visual: A + B + C = scale, danger, mystery"公式化收束是封面图的独门技巧；三个叙事槽位让它成为可换皮封面模板。
**来源**：ai-image-prompts-skill · ID 33922

### 【社媒帖图·复古拼贴】
适用：社交平台发图的随拍感双框拼贴

```text
{

  "type": "retro fashion photo collage",

  "aspect_ratio": "1:1",

  "composition": "two overlapping photographic frames with different zoom levels",

  "subject": "young freckled woman, long messy wavy dark-brown hair, soft bangs, spontaneous playful mood",

  "outfit": "oversized black and off-white rugby pullover with lime panels, loose khaki bermuda cargos, olive socks, brown chunky sneakers, orange graphic baseball cap, colorful clip accessories",

  "action": "holding a waffle cone while squeezing whipped cream onto it; second frame captures her licking the cream with an amused expression",

  "setting": "simple warm-gray studio floor and backdrop",

  "lighting": "soft overhead diffused light with gentle shadows",

  "style": "90s-inspired Japanese youth editorial, candid snapshot aesthetic, muted colors, subtle analog grain, imperfect natural poses",

  "negative": "perfect commercial photography, plastic skin, cinematic lighting, anatomy errors, extra fingers, malformed hands, duplicate objects, face distortion, clothing glitches, text, watermark, logos"

}
```

**点评**：10 个键讲清完整画面；negative 里写 "perfect commercial photography"——把"太完美"列为避免项，才出得了胶片随拍感。
**来源**：ai-image-prompts-skill · ID 35454

### 【社媒手账·照片+手绘拼贴】
适用：旅行照片转手账风社媒帖（需上传照片）

```text
Transform the uploaded photo into a premium travel-memory scrapbook poster.

Keep the original photo as the main visual reference and preserve the important subjects, objects, environment, composition, colors, and recognizable details accurately. Do not change the identity or structure of the main subject.

Create a vertical 3:4 editorial scrapbook layout divided horizontally into two equal sections:

TOP 50%:
Place the original photograph prominently, enhanced with warm, natural, slightly cinematic color grading. Keep it realistic, detailed, and photographic. Do not over-edit or make it look artificial.

BOTTOM 50%:
Create a beautiful hand-drawn illustrated journal page inspired directly by the photograph. Extract 6–9 of the most recognizable visual elements from the original image and turn each into a small individual colored-pencil / ink / watercolor-style sketch arranged in a clean 3×3 scrapbook grid.

Use:
- textured warm ivory/off-white paper background
- subtle paper grain
- hand-drawn pencil and ink outlines
- loose colored-pencil and watercolor shading
- slightly imperfect handmade strokes
- soft muted but cheerful colors
- tiny doodles such as stars, hearts, leaves, sparkles, waves and arrows
- thin, delicate hand-drawn grid dividers
- cozy travel-journal aesthetic
- sophisticated editorial composition
- authentic handmade imperfections

Add a handwritten title at the top of the illustrated section, customized to the photo's theme, such as "{argument name="location" default="[LOCATION]"} Memories", "{argument name="theme" default="[THEME]"} Moments", "Sweet Moments", "Blue Sky Memories", etc.

Under each illustrated element, add a short handwritten label describing it, for example:
“street lamp”, “soft clouds”, “colorful lights”, “tea”, “old walls”, “sweet treat”, “green moments”, etc.

At the very bottom, add a small handwritten sentimental caption related to the photo, such as:
“a perfect day to remember ♡”
or
“same place, different feelings ♡”

The final result should feel like a luxury travel scrapbook / visual diary page created by hand, combining a real photograph with charming illustrated memories.

IMPORTANT:
- One original photo + one illustrated memory section
- Clean 50/50 horizontal division
- Vertical 3:4 composition
- Preserve the original photo realistically
- Illustrations must clearly originate from objects in the uploaded photo
- No photorealistic illustrations
- No 3D rendering
- No excessive graphic-design effects
- No borders around individual illustrations
- No random objects unrelated to the photo
- Keep typography minimal, elegant, and handwritten
- Make the entire page cohesive, warm, nostalgic, artistic, and premium
```

**点评**："上 50% 保原照片 + 下 50% 提取 6-9 个元素重绘 3×3 手账格"，先给足正向风格清单，再用 IMPORTANT 一口气列 11 条禁令——正负约束配对最工整的一条。
**来源**：awesome-gpt-image-2 · R28

### 【小红书封面·设计规范式】
适用：小红书等平台的高点击封面图

```text
画图：画一个小红书封面。
要求：
有足够的吸引力吸引用户点击；
字体醒目，选择有个性的字体；
文字大小按重要度分级，体现文案的逻辑结构；
标题是普通文字的至少2倍；
文字段落之间留白。
只对要强调的文字用醒目色吸引用户注意；
背景使用吸引眼球的图案（包括不限于纸张，记事本，微信聊天窗口，选择一种）
使用合适的图标或图片增加视觉层次，但要减少干扰。

文案：重磅！ChatGPT又变强了！
多任务处理更牛✨
编程能力更强💪
创造力爆表🎨
快来试试！

图像9:16比例
```

**点评**：与其说是 prompt 不如说是"封面设计规范"——字号分级（标题≥2 倍）、留白、强调色唯一全写成需求文档，文案带 emoji 逐行注入。
**来源**：awesome-gpt4o-images · 案例 22 · @balconychy

## 避坑清单（组装该类 prompt 时逐条对照）

1. **明确"平台+比例+布局"，拒绝模糊指令**：手机截图比例（9:16/3:4/1:1）写在前头；车机等特殊屏幕（21:9）比例必须写在最前面。
2. **强制文字锁定**："必须准确显示指定的中文，禁止乱码和占位文本"；界面文字逐控件给出（余额/账单/星期轴/按钮文案/输入框占位符）。
3. **截图必须区分平台特征**：X 蓝勾、抖音音乐碟片、小红书双列瀑布流、朋友圈点赞线——特征元素不写出来就不像那个平台。
4. **直播先定类型**：带货 vs 才艺布局差异大；按屏幕四角分区枚举 UI 叠加层，并用"界面元素不遮挡主播面部"这类可判定约束防止多层元素打架。
5. **虚构品牌/人名防泄漏**：AURAE / Moss Radio 式自造名 + 显式给出全部虚构产品信息（余额、账单、价格），防止模型带入真实品牌 logo。
6. **UI 要素当在图文字标注**：把每个 chip/nav/图表轴当文字逐个点名——UI 类 prompt 的本质是元素清单，不是"画一个好看的界面"。
7. **实拍融合用 POV + 浅景深**：风格锚定具体流派（glassmorphism），防止像设计稿渲染；随拍感在 negative 里写 "perfect commercial photography"（把"太完美"列为避免项）。
8. **改图/拼贴类正负约束配对**：先定义参考图角色（保身份、保构图），再给正向风格清单，最后用 IMPORTANT/约束列表禁掉越界（插图必须源自照片、no 3D、no random objects）。
