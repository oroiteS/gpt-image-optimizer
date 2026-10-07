# 建筑与空间

> 覆盖建筑外观（微缩/城市尺度）、室内设计与图纸渲染、草图转渲染、等距剖面。写作前先读 2-3 条最相关样例，套用其结构而非照抄内容。

tags: 建筑外观, 室内设计, 草图转渲染, 等距剖面, 建筑可视化

## 样例

### 【草图转真实渲染（布局锚点+防幻觉）】
适用：手绘草图/布局稿转真实感房间、空间宣传图

```text
Create a real-life room promotional image to market my room to potential tenants. The theme is room layout: a large floor-to-ceiling window on the left with excellent sunlight and lighting. Beside the window is a cat bed with a {argument name="pet" default="orange cat"} lying on it. Inside the bedroom is a large desk with daily items like a computer, keyboard, mouse, and phone. A young Chinese male is sitting on an ergonomic chair operating the computer. To the right of the desk is a single bed. The overall spatial relationship follows the sketch. Lighting and textures should look like a bedroom photo taken with a phone. Hard requirements: all items drawn in the sketch must appear, including the sun outside the window. Problems to avoid: do not include any elements or phenomena that contradict real daily life. Other proportions and room details are up to you to ensure a natural, realistic, and unforced effect.
```

**点评**："空间关系 follows the sketch" + 硬性要求：草图上画过的东西（连窗外的太阳）必须全部出现 + 避免任何违背日常生活的元素——把草图当布局约束、用硬性条款防幻觉。
**来源**：awesome-gpt-image-2 · R106（Raycast 参数化）

### 【平面图转 3D 室内渲染（一保留一放开）】
适用：建筑平面图/户型图添加家具、材质做超写实室内渲染

```text
对这张建筑平面进行超写实 3D 渲染：不得改变墙体位置，保持所有线条与平面图一致，但添加家具、饰面、材质与纵深。
```

**点评**：编辑类黄金句式——"不得改变 X，保持 Y 一致，但添加 Z"，一保留一放开的权限划分适用于所有图纸类图生图。
**来源**：awesome-gpt4o-images · gpt-image-1 官方案例 20（版权属 OpenAI，公开分发时建议重写）

### 【等距剖面改写（参考图作布局锚点）】
适用：把街区/建筑参考图改写成等距剖面立体模型

```text
Use the reference image as the layout anchor for a richly detailed isometric two-block cafe district at blue hour. Keep the street footprint, corner cafe, neighboring bookstore, bakery and fountain plaza recognizable. Transform it into a three-storey architectural cutaway diorama with coherent 30-degree isometric geometry.

Open the front-facing walls to reveal the cafe espresso bar and upstairs jazz lounge; bookshelves, reading nooks and a spiral staircase in the bookstore; pastry cases and a working oven in the bakery. Add a rooftop glass greenhouse, tiny terraces, copper plumbing, tiled stairs, balconies, hanging plants and warm lights visible through rain-speckled windows. At street level show wet cobbles, bicycles, the coffee cart, varied miniature pedestrians and reflections around the fountain. Every floor, doorway and staircase should connect plausibly.

Use warm amber interiors against deep teal evening shadows, tactile brick, glazed tiles, glass and brushed brass. Preserve crisp detail throughout the scene, with a clean dark navy background and room around the floating diorama. Give the scene depth through cutaway rooms and layered architecture. Use restrained, readable storefront lettering: "NIGHT OWL CAFE", "OPEN BOOKS", and "DAWN BAKERY". Keep the composition square and visually balanced.
```

**点评**："Use the reference image as the layout anchor" + "Keep … recognizable" 先定义参考图角色，再用 "Every floor, doorway and staircase should connect plausibly" 约束剖面空间自洽。
**来源**：GPT-Image2-Skill · No. 54（附改写案例）

### 【建筑外观·45° 等距微缩模型】
适用：城市地标/建筑群微缩沙盘、天气卡片、立体模型感展示

```text
以清晰的45°俯视角度，展示一个等距微缩模型场景，内容为[上海东方明珠塔、外滩]等城市特色建筑，天气效果巧妙融入场景中，柔和的多云天气与城市轻柔互动。使用基于物理的真实渲染（PBR）和逼真的光照效果，纯色背景，清晰简洁。画面采用居中构图，凸显出三维模型精准而细腻的美感。在图片上方展示"[上海 多云 20°C]"，并附有多云天气图标。
```

**点评**：视角（45° 俯视）、渲染技术（PBR）、构图（居中）、文字内容与位置四要素齐全，把日常需求写成工程规格。
**来源**：awesome-gpt4o-images · 案例 82 · @dotey

### 【城市剖面信息图（天空到地底）】
适用：城市/园区/基础设施的等距剖面科普图、工程图

```text
Vertical 9:16 isometric cutaway infographic "城市生命系统图谱 / Urban Metabolism Atlas". Smart city from sky to bedrock: skyscrapers, streets, subway, utility tunnels, water/sewage/gas/heating pipes, fiber, data center, flood tanks, aquifers, geothermal wells, bedrock. Color-coded flows for power/water/data/traffic/waste. 12 numbered panels bilingual CN/EN: 能源/水循环/交通/数据/垃圾/建筑/公共服务/ 物流/气候韧性/生态/地质/治理看板. 24h timeline at bottom. Style: engineering white paper + scientific atlas, light paper bg, crisp lines, 8K. No cyberpunk, no gibberish text, must show both above AND below ground.
```

**点评**：比例前置、内容枚举（12 个编号面板双语清单）、风格两句、负面三条收尾，576 字符控制一张极复杂剖面信息图；"must show both above AND below ground" 是空间完整性的硬验收。
**来源**：freestylefly-awesome-gpt-image-2 · 案例层（No. 63)

## 避坑清单（组装该类 prompt 时逐条对照）

1. 控制透视：Eye-level perspective 压住变形；等距类锁定角度（如 coherent 30-degree isometric geometry），一张图只用一个透视系统。
2. 冷暖对比是高级感作弊码：室外冷光 + 室内暖光。
3. 图纸类先划权限：空间关系/墙体位置保持一致（一保留），家具、饰面、材质、光影放开添加（一放开）。
4. 防幻觉硬条款：草图上画过的元素必须全部出现（Hard requirements 逐条列）；禁止出现任何违背日常生活的元素或现象。
5. 剖面图空间自洽：每层楼、门、楼梯要 connect plausibly；地上地下都要交代（must show both above AND below ground）。
6. 场景叙事要有动词："正在崩塌""刚点燃火把"，别画成风景明信片；用 Low angle shot / Dutch angle 加戏剧冲突。
7. 微缩/沙盘类用 PBR + 纯色背景 + 居中构图；靠材质物理行为（折射、焦散、反射、双光源位）代替 8K、masterpiece 式质量形容词。
