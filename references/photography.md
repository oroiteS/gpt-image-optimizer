# 摄影与照片级写实

> 定位：覆盖街拍、抓拍、夜景、纪实、黑白艺术、建筑室内等一切"要像拍出来的照片"的需求。写作前先读 2-3 条最相关样例，套用其结构而非照抄内容。

tags: 摄影写实, 照片感, 街拍纪实, 夜景, 抓拍, 建筑室内

## 样例

### 【RAW iPhone 地铁站抓拍】
适用：抓拍感、纪实瞬间、"随手拍出来"的真实感，极简 prompt 起点

```text
Create a completely RAW quality, unprocessed, unedited image with full iPhone camera quality. A subway station in USA, a momentary blur. The subway is in motion. In front of the subway, there is an elderly woman and man.
```

**点评**：全场最短的上榜样例——"RAW/未处理/iPhone 画质 + 一处动态模糊 + 平凡人物"这一捕捉语境本身就是最强的照片真实感杠杆。
**来源**：GPT-Image2-Skill · No. 63

### 【街头意外瞬间写实模板】
适用：街头小事故、日常瞬间纪实，中文变量填空模板

```text
生成一张竖版手机纪实照片，主题是[意外事件/日常瞬间]发生在[街头/室外地点]。
主体：[物品/人物动作/现场痕迹]，必须呈现真实的材质状态，例如[液体扩散/冰块散落/纸张褶皱/灰尘颗粒]。
环境：[地面材质/墙面/街景元素]，保留自然杂乱和生活痕迹。
光线：[正午强光/阴天散射光/夜间路灯]，阴影要符合真实方向，可加入[人物影子/路牌影子/树影]。
镜头：手持手机视角，略微俯拍或低角度，构图自然，像随手拍到的现场。
画面质感：raw unedited photo look，自然色彩，真实纹理，高细节。
负面约束：不要插画、动漫、CGI、棚拍光、过度干净、过度构图、假液体、漂浮物、品牌文字、水印、海报设计感。
输出：一张可信的日常纪实摄影图。
```

**点评**：反其道行之的"真实感模板"——用负面约束主动排掉 AI 的"过度干净、过度构图、棚拍光"本能，是"把不完美写具体"的典范。
**来源**：freestylefly-awesome-gpt-image-2 · 模板层No. 76

### 【泼洒抹茶街头手机照】
适用：街头静物事故、液体洒落场景，正面与 Negative Prompt 显式分离写法

```text
A realistic vertical smartphone photo of a spilled green iced drink on outdoor stone pavement, a transparent disposable plastic cup lying on its side inside the green puddle, clear plastic lid nearby, scattered ice cubes floating in the drink, small foam bubbles on the surface, green liquid naturally spreading across rough square floor tiles, strong midday sunlight, harsh realistic shadows, a dark human shadow silhouette cast across the ground and partially over the spill, accidental street moment, urban documentary photography, handheld phone camera perspective, slightly top-down angle, natural colors, realistic pavement texture, raw unedited photo look, high detail, authentic everyday scene, 9:16 vertical composition

Negative Prompt:
cartoon, illustration, anime, CGI, 3D render, fantasy style, studio lighting, overly perfect composition, overly clean floor, fake liquid, unrealistic reflections, plastic-looking liquid, oversaturated green, blurry, low resolution, distorted cup, melted plastic, extra cups, duplicated objects, readable brand logo, messy text, watermark, poster design, dramatic artificial lighting, excessive sharpening, over-processed, unrealistic shadow, floating ice, deformed perspective
```

**点评**：把"真实感"完全交给 29 条 Negative Prompt 反向定义，正负面分离写法可控性最高，负面清单可直接移植到任何街头纪实题材。
**来源**：freestylefly-awesome-gpt-image-2 · 案例层No. 10（例 376） · @Shinning1010

### 【便利店霓虹夜景胶片】
适用：夜景街拍、霓虹灯环境人像、35mm 胶片质感

```text
35mm film photography with harsh convenience store fluorescent lighting mixed with colorful neon signs from outside, authentic film grain, high contrast, slight color cast, cinematic street editorial style, intimate medium shot, early 20s sexy Chinese female idol with ultra-realistic delicate refined Chinese features, seductive almond-shaped fox eyes with natural double eyelids, high nose bridge, small sharp V-shaped jawline, flawless porcelain skin with cool ivory undertone and visible specular highlights from fluorescent light, subtle skin texture and micro pores, natural dewy makeup with soft flush on cheeks, glossy natural pink lips slightly parted, subtle natural freckles across nose and cheeks, long dark brown hair in a messy high ponytail with many loose strands falling around face and neck, wearing an oversized white button-up shirt as the only top, unbuttoned at the top with deep cleavage and loosely tied at the waist, paired with a tiny black pleated mini skirt, barefoot in simple white slides, seductive casual leaning pose against the glass door of a 24-hour convenience store at late night, body slightly arched, one leg bent with foot resting against the door frame, the other leg straight, one hand holding a bottle of iced drink, the other hand lightly pulling the hem of her mini skirt, intensely seductive playful yet slightly vulnerable gaze straight at the viewer with soft doe eyes full of quiet temptation and teasing smile, bright cold fluorescent store light from inside mixed with pink and blue neon glow from outside signs, realistic reflections on glass door, blurred convenience store interior with shelves and snacks in background, authentic 35mm film color grading with harsh lighting and neon accents, extremely sharp yet soft skin rendering, natural hair strands, realistic fabric wrinkles and drape on the oversized shirt and mini skirt, no plastic skin, no digital over-sharpening, no airbrushing, no blemishes, no moles, no oily skin, no watermark, no text, authentic late-night convenience store atmosphere
```

**点评**：从瞳孔形状到环境光源的全量外观描写 + 35mm 胶片质感 + 尾部一长串 no 负面，"堆细节"流派写夜景街拍人像的代表。
**来源**：awesome-gpt-image-2-API-and-Prompts · Case 52 · @BubbleBrain

### 【涩谷雨夜街头 Lookbook】
适用：夜景时尚街拍、潮牌穿搭、雨夜霓虹环境

```text
Full-body lookbook photography of a model standing in the center of a rain-slicked Shibuya crossing at twilight. The model wears an oversized, multi-pocketed technical puffer jacket in 'Electric Cobalt' with reflective silver detailing, paired with wide-leg cargo trousers in matte black and chunky platform sneakers. The composition is a sharp medium-wide shot using a 35mm lens, capturing the vibrant neon signs of the background blurred into a soft bokeh of pinks and cyans. Lighting is dramatic and directional, sourced from the surrounding digital billboards, creating high-contrast highlights on the jacket's texture. The mood is urban and fast-paced, with a subtle film grain characteristic of Portra 400. The image features a clean vertical layout suitable for a fashion magazine, with the text 'NEO-URBAN' subtly embossed in the corner in a minimalist sans-serif font. No brand logos are visible.
```

**点评**：服装色名带引号（'Electric Cobalt'）、胶片型号（Portra 400）、光源来自环境广告牌——时尚街拍的真实感来自这些具体的行业词汇。
**来源**：GPT-Image2-Skill · No. 130

### 【黑白艺术人像摄影】
适用：黑白肖像、艺术编辑感、负空间情绪人像

```text
高分辨率的黑白肖像艺术作品，采用编辑类和艺术摄影风格。背景呈现柔和渐变效果，从中灰过渡到近乎纯白，营造出层次感与寂静氛围。细腻的胶片颗粒质感为画面增添了一种可触摸的、模拟摄影般的柔和质地，让人联想到经典的黑白摄影。

画面右侧，一个模糊却惊艳的哈利波特面容从阴影中隐约浮现，并非传统的摆拍，而像是被捕捉于思索或呼吸之间的瞬间。他的脸部只露出一部分：也许是一个眼睛、一块颧骨，还有唇角的轮廓，唤起神秘、亲密与优雅之感。他的五官精致而深刻，散发出忧郁与诗意之美，却不显矫饰。

一束温柔的定向光，柔和地漫射开来，轻抚他的面颊曲线，或在眼中闪现光点——这是画面的情感核心。其余部分以大量负空间占据，刻意保持简洁，使画面自由呼吸。画面中没有文字、没有标志——只有光影与情绪交织。

整体氛围抽象却深具人性，仿佛一瞥即逝的目光，或半梦半醒间的记忆：亲密、永恒、令人怅然的美。
```

**点评**：中文长 prompt 的文学性天花板——四段式（整体风格/主体/光线与负空间/氛围收束），"一个眼睛、一块颧骨、唇角轮廓"把局部构图写成诗，结尾顺带完成负向约束。
**来源**：awesome-gpt4o-images · 案例 99 · @ZHO_ZHO_ZHO

### 【怀旧闪光灯快照】
适用：年代感室内抓拍、直闪快照质感、怀旧氛围

```text
超写实的 3D 渲染画面，重现了2008年《命令与征服：红色警戒3》中娜塔莎的角色设计，完全依照原版建模。场景设定在一个昏暗杂乱的2008年代卧室里，角色正坐在地毯上，面对一台正在播放《命令与征服：红色警戒3》的老式电视和游戏机手柄。

整个房间充满了2008年代的怀旧氛围：零食包装袋、汽水罐、海报以及纠缠在一起的电线。娜塔莎·沃尔科娃在画面中被抓拍到转头的一瞬，回眸看向镜头，她那标志性的空灵美丽面容上带着一抹纯真的微笑。她的上半身微微扭转，动态自然，仿佛刚刚被闪光灯惊到而做出的反应。

闪光灯轻微地过曝了她的脸和衣服，使她的轮廓在昏暗的房间中更加突出。整张照片显得原始而自然，强烈的明暗对比在她身后投下深邃的阴影，画面充满触感，带有一种真实的2008年胶片快照的模拟质感。
```

**点评**：年代考据（2008 年的零食袋/电线）+ 相机事件（闪光灯过曝）双技巧叠加，"把一次闪光写进 prompt"是快照感的秘密。
**来源**：awesome-gpt4o-images · 案例 67 · @ZHO_ZHO_ZHO

### 【平面图转建筑室内渲染】
适用：建筑平面图可视化、室内设计效果图、图生图改写

```text
对这张建筑平面进行超写实 3D 渲染：不得改变墙体位置，保持所有线条与平面图一致，但添加家具、饰面、材质与纵深。
```

**点评**：改图任务的"先锁什么不能变（墙体/线条），再写添什么（家具/饰面/材质/纵深）"一句式契约，建筑室内类改写的最小可用模板。
**来源**：awesome-gpt4o-images · gpt-image-1 官方案例 20

### 【草图转真实卧室】
适用：手绘草图转实拍效果图、租房/地产宣传图、布局约束类改写

```text
Create a real-life room promotional image to market my room to potential tenants. The theme is room layout: a large floor-to-ceiling window on the left with excellent sunlight and lighting. Beside the window is a cat bed with a {argument name="pet" default="orange cat"} lying on it. Inside the bedroom is a large desk with daily items like a computer, keyboard, mouse, and phone. A young Chinese male is sitting on an ergonomic chair operating the computer. To the right of the desk is a single bed. The overall spatial relationship follows the sketch. Lighting and textures should look like a bedroom photo taken with a phone. Hard requirements: all items drawn in the sketch must appear, including the sun outside the window. Problems to avoid: do not include any elements or phenomena that contradict real daily life. Other proportions and room details are up to you to ensure a natural, realistic, and unforced effect.
```

**点评**："空间关系 follows the sketch + 硬性要求：草图上画过的东西（连窗外的太阳）必须全部出现 + 避免任何违背日常生活的元素"——把草图当布局约束、用硬性条款防幻觉。
**来源**：awesome-gpt-image-2 · R106

## 避坑清单（组装该类 prompt 时逐条对照）

1. **加点瑕疵**：skin pores、雀斑、film grain 主动写进正向——"AI 画的人太完美了，反而像假人"。（freestylefly 避坑指南摄影）
2. **用参数说话**：`f/1.4` 代替"浅景深"，`50mm` 代替"半身照"，`Portra 400` 代替"胶片感"——大模型吃这套；确定不了参数就只写视觉效果（"广角存在感、空间压缩"）。（freestylefly 避坑指南摄影 + GPT-Image2-Skill 防幻觉红线）
3. **把"不完美"写具体**："粗糙石砖、散落冰块、自然阴影、轻微手持感"比一句"真实"稳定得多。（freestylefly 避坑指南摄影）
4. **负面清单主动排掉 AI 本能**：棚拍光、过度干净、过度构图、CGI、假液体、海报设计感——真实感一半靠 negative 定义。（freestylefly No. 76/22 点评）
5. **建筑室内控透视**：Eye-level perspective 压住广角变形；室外冷光 + 室内暖光的冷暖对比是"空间高级感的作弊码"。（freestylefly 避坑指南建筑）
6. **抓拍/UGC 用精确点数锁元素**：`exactly one basket, two background shoppers...` 防人多手杂，并点名 no glamour lighting、不完美构图。（awesome-gpt-image-2 R109 点评）
7. **场景要有"正在发生"**：写"地铁正在进站、液体正在扩散"，否则画成风景明信片；戏剧冲突用 Low angle / Dutch angle 镜头语言加。（freestylefly 避坑指南场景叙事）
8. **改图类先锁后加**：平面图/草图转实拍，第一句写"不得改变什么"（墙体、布局、物品清单），第二句才写"添加什么"；硬性要求逐条列出防幻觉。（官方案例 20 与 R106 的共同结构）
