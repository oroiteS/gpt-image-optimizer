# 插画与艺术风格

> 定位：覆盖"氛围与艺术风格优先"的插画需求——水墨、水彩、微缩移轴、复古/VHS 媒介质感、稚拙风等风格化画面。写作前先读 2-3 条最相关样例，套用其结构而非照抄内容。

tags: 插画, 水墨, 水彩, 微缩移轴, 复古VHS, 稚拙风

## 样例

### 【水墨手卷·大师笔法转译示范】
适用：中国古风场景、水墨/工笔题材横卷构图。

```text
Create a horizontal Chinese ink-and-wash handscroll scene of a Song dynasty riverside night market. Use gongbi-level architectural detail combined with loose ink atmosphere: arched stone bridge, lantern boats, teahouse balconies, book stalls, noodle steam, scholars reading under lamps, children chasing paper rabbits, and distant city walls fading into mist. Add small readable Chinese shop signs in brush style: "茶", "书", "面", "灯市". Palette: black ink, warm lantern ochre, muted cinnabar seals, and pale blue-gray moonlight. Composition should read as a continuous scroll with rhythmic clusters of people and negative-space water. Avoid modern objects, anime faces, fake calligraphy clutter, and overly saturated poster lighting.
```

**点评**：**"大师名转译为特征"的示范**——按 freestylefly 防坑指南"提取大师的特征而不是直接写大师名"，本条不写"中国画大师风格"，而是把流派笔法名转译成可执行特征：工笔（gongbi）→ "gongbi-level architectural detail"（界画级建筑细节），写意 → "loose ink atmosphere"（晕染氛围），流派名与视觉特征同时出现；朝代（Song dynasty）明确，且仅四个单字招牌降低文字出错率。
**来源**：GPT-Image2-Skill · No.51

### 【水彩手绘城市地图】
适用：手绘风旅游/美食地图，水彩+复古羊皮纸质感，含大量中文标签。

```text
{
  "type": "illustrated map infographic",
  "style": "{argument name=\"art style\" default=\"watercolor and ink hand-drawn illustration on vintage parchment\"}",
  "title_section": {
    "text": "{argument name=\"city name\" default=\"成都\"} {argument name=\"map title\" default=\"吃货暴走地图\"}",
    "mascot": "cartoon red chili pepper wearing sunglasses and giving a thumbs up"
  },
  "border": "{argument name=\"border decoration\" default=\"vine of green leaves and red chili peppers\"}",
  "layout": {
    "background": "textured beige parchment paper with yellow roads, blue rivers, and green park areas",
    "sections": [
      {
        "title": "landmarks",
        "count": 6,
        "illustrations": ["traditional pavilion", "traditional monastery", "modern skyscraper with climbing panda", "tall TV tower", "traditional gate", "industrial buildings"],
        "labels": ["人民公园", "文殊院", "IFS", "339电视塔", "宽窄巷子", "东郊记忆"]
      },
      {
        "title": "food_spots",
        "count": 12,
        "illustrations": ["mapo tofu", "dumplings in chili oil", "skewers in pot", "sticky rice balls", "egg baking cake", "nine-grid hotpot", "sweet potato noodles", "cold skewers", "spicy mixed dish", "covered tea bowl", "ice jelly dessert", "spicy rabbit heads"],
        "labels": ["1 陈麻婆豆腐", "2 钟水饺", "3 春熙路", "4 宽窄巷子·三大炮", "5 建设路·叶婆婆蛋烘糕", "6 玉林路·小龙坎火锅", "7 香香巷·肥肠粉", "8 武侯祠大街·钵钵鸡", "9 东郊记忆·冒椒火辣", "10 人民公园·鹤鸣茶社", "11 锦里古街·冰粉", "12 双流老妈兔头"]
      },
      {
        "title": "图例",
        "position": "bottom-right",
        "count": 5,
        "items": ["red dot", "green house", "green tree", "blue line", "yellow double line"],
        "labels": ["美食地点", "地标景点", "公园绿地", "河流湖泊", "主要道路"]
      }
    ],
    "centerpiece": "giant panda sitting and eating bamboo",
    "bottom_right_extras": ["vintage compass rose with N, S, E, W", "disclaimer text '温馨提示：吃辣需谨慎，肠胃要保护~' with a red chili pepper icon"]
  }
}
```

**点评**：风格锚是工艺而非画家名——"watercolor and ink hand-drawn illustration on vintage parchment"（水彩+水墨+复古羊皮纸）；JSON `labels` 数组把 6 地标 + 12 美食点的中文名一字不差枚举，图例/指南针/吉祥物/免责小字齐备。
**来源**：awesome-gpt-image-2 · 精选 F2

### 【复古 VHS 监控静帧】
适用：90 年代复古、VHS/监控媒介质感、荒诞叙事静帧。

```text
Create a chaotic security-camera still from a 1990s grocery store. A man in full medieval armor is frozen mid-sprint stealing several rotisserie chickens past the dairy section. Overhead fluorescent lights reflect off the armor. The floor is baby-blue tile. Add a timestamp reading "08/13/96 04:44 AM" and a wall poster saying "NEW! TOASTER STRUDELS!". Make it low-fidelity, absurd, slightly intense, with motion blur, VHS color bleed, surveillance noise, and authentic analog-store lighting.
```

**点评**：一句话核心荒诞 + 媒介细节（监控时间戳/VHS 色偏/噪点/日光灯反射）——时代媒介质感本身就是一组 prompt 词汇，比"复古滤镜"式形容词有效得多。
**来源**：GPT-Image2-Skill · No.30（源自 Reddit）

### 【稚拙风双人打架】
适用：稚拙/素人/儿童画风格的角色互动与情绪表达。

```text
[Character A] and [Character B], neo-naïve painting × outsider art × primitive figurative painting × children's drawing style character translation.

The two characters are composed of a small number of irregular geometric color blocks, retaining only their strongest identity markers: primary color, head silhouette, hairstyle or ears, eyes, representative clothing color blocks, signature accessories.

The two are fighting intensely but comically, bodies pressed close and entangled. Randomly design actions such as face-grabbing, head-pushing, hugging, pulling, slapping, pinning down, or mutual pouncing based on the characters; hand contact is clear, limbs intersect, center of gravity is unbalanced, making the fighting relationship instantly readable.

Childish and inaccurate human anatomy: slender torsos, stiff straight limbs, inaccurate proportions, tilted heads, exaggerated hands and feet, incorrect perspective. Facial features compressed into a few rough color blocks, expressions angry, shocked, baring teeth, screaming, or aggrieved, possessing an absurd comedic feel.

Rough opaque paint flat coloring, dry brush marks, frayed edges, uneven filling, shaky hand-drawn outlines, local underpainting exposure; body and clothing represented directly by flat color blocks.

Warm gray-white or off-white paper background, large areas of blank space. The two characters are located in the center, entangled with each other forming a compact action mass, the picture focuses on expressing the relationship between the characters.

Like a fight moment quickly drawn from memory by an untrained person: primitive, clumsy, direct, absurd, cute.

Vertical format, extremely small "voxcat" signature in the bottom right corner.
```

**点评**：用一整段"风格翻译声明"（稚拙绘画×素人艺术×儿童画）保留角色最强身份记号，再主动要求"解剖不准确、透视错误、手抖轮廓"等缺陷美学锚定风格——"反向要求画错"来锁定笔触的独特思路。
**来源**：awesome-gpt-image-2 · R68

### 【等距微缩天气卡片】
适用：城市微缩场景/移轴立体小景、天气与信息卡片。

```text
以清晰的45°俯视角度，展示一个等距微缩模型场景，内容为[上海东方明珠塔、外滩]等城市特色建筑，天气效果巧妙融入场景中，柔和的多云天气与城市轻柔互动。使用基于物理的真实渲染（PBR）和逼真的光照效果，纯色背景，清晰简洁。画面采用居中构图，凸显出三维模型精准而细腻的美感。在图片上方展示"[上海 多云 20°C]"，并附有多云天气图标。
```

**点评**：微缩/移轴类的四要素公式——视角（45°俯视）、渲染技术（PBR）、构图（居中）、在图文字内容与位置（上方+图标），把日常需求写成工程规格，换城市换天气即成系列。
**来源**：awesome-gpt4o-images · @dotey（案例 82）

## 避坑清单（组装该类 prompt 时逐条对照）

1. **锁定笔触**：不限制笔触通常会得到毫无灵魂的 AI 默认塑料风——写明干笔扫痕/晕染/平涂/纸纹等具体笔触与载体（freestylefly 避坑指南插画原文；R68 的缺陷美学同理）。
2. **慎用大师名**：提取大师的特征（如"梵高的旋转星空笔触"）而不是直接写大师名（freestylefly 避坑指南插画原文）；流派名（工笔/写意/浮世绘/稚拙）同理转译成可执行视觉特征（见水墨手卷样例点评）。
3. **历史古风明确朝代与器物体系**：否则会"穿着和服、拿着清朝折扇在唐朝宫殿里"；并强制排雷 No modern elements，防止古人手里突然多出一杯星巴克（freestylefly 避坑指南历史古风；No. 51 的 Avoid modern objects）。
4. **防动漫脸与伪书法**：古风水墨题材的 avoid 列表要点名 anime faces、fake calligraphy clutter、overly saturated poster lighting 三个高危默认项（No. 51 点评）。
5. **IP 风险**：具名画家/工作室/影片风格商用有版权风险，用"特征转译 + 原创主体"替代（awesome-gpt4o-images 方法论：吉卜力风→手绘水彩动画风）。
6. **在图文字做减法**：招牌/题签只用单字或词组并逐字给出，降低错字率；不要让模型自由生成成段"书法"（No. 51 仅四个单字招牌的点评）。
7. **微缩/移轴四要素齐全**：视角（45°俯视/等距）+ 渲染（PBR/光照）+ 构图（居中）+ 在图文字与位置，缺一项就容易被画成普通场景照（案例 82 点评）。
8. **媒介质感即词汇表**：VHS 色偏、监控噪点、胶片颗粒、套色错位、颜料洇纸——时代与媒介的具体瑕疵词比"复古"一词有效（No. 30 点评）。
