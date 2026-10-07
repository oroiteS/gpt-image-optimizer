# 信息图 · 数据 · 科研图

> 定位：覆盖"把知识、数据、结构画成一张图"的需求——拆解信息图、科普挂图/知识卡、论文图、架构图、数据可视化与技术爆炸图。写作前先读 2-3 条最相关样例，套用其结构而非照抄内容。

tags: 信息图, 科普挂图, 论文配图, 架构图, 数据可视化, 爆炸图

## 样例

### 【拆解信息图·万能模板】
适用：只给一个主题词（[Subject]）就要一张完整中文拆解信息图，文物/服饰/器物科普展板。固定版式契约 + 占位符模板的示范条目。

```text
Please automatically generate a "museum catalog-style Chinese disassembly infographic" based on the [Subject].

The entire image is required to combine a realistic main visual, structural disassembly, Chinese annotations, material descriptions, pattern meanings, color meanings, and core feature summaries. You need to automatically determine the most appropriate main subject, clothing system, artifact structure, era style, key components, material craftsmanship, color scheme, and layout structure based on the [Subject], and the user does not need to provide any other information.

The overall style should be: national museum exhibition boards, historical clothing catalogs, and cultural/museum thematic infographics, rather than ordinary posters, ancient-style portraits, e-commerce detail pages, or anime illustrations. The background uses paper textures such as off-white, silk white, and light tea color, making the overall look premium, restrained, professional, and collectible.

The layout is fixed as:
- Top: Chinese main title + subtitle + introduction
- Left: Structural disassembly area, with Chinese lead lines annotating key components, accompanied by close-up details
- Upper right: Material / craftsmanship / texture area, displaying real texture samples with descriptions
- Middle right: Pattern / color / meaning area, displaying the main color palette, pattern samples, and cultural explanations
- Bottom: Dressing order / composition flowchart + core feature summary

If the subject is suitable for character display, use a full-body standing posture of a real person as the central subject; if it is more suitable for artifacts or single structures, change it to a central subject disassembly diagram, but the overall form remains a complete Chinese infographic. All text must be in Simplified Chinese, clear, neat, and readable, without garbled characters, typos, English, or pinyin.

Avoid: poster feel, studio portrait feel, e-commerce feel, anime feel, cosplay feel, random annotations, incorrect structures, blurry text, fake materials, excessive decoration.
```

**点评**："模糊需求 → 完整 prompt"的直接范本：用户只给 [Subject]，模板用"固定版式契约（Top/Left/Upper right/Middle right/Bottom）+ 像什么不像什么 + 全中文无乱码 + 排除清单"自动补全主体、结构、布局一切细节。
**来源**：GPT-Image2-Skill（wuyoscar/gpt_image_2_skill） · No.69

### 【百科图鉴知识卡】
适用：把任意 topic 做成竖版科普知识卡/图鉴页，可反复复用的卡片格式。

```text
Generate a high-quality vertical encyclopedia-style infographic for [topic].

This should not be a normal poster or a simple illustration. It should feel like a modular educational infographic that combines the clarity of a field guide, the structure of an encyclopedia page, the polish of a lifestyle knowledge card, and the shareability of a strong social-media explainer.

The image should include:
- a clear and appealing main visual of the topic
- several enlarged detail callouts
- multiple rounded modular information sections
- strong title hierarchy and highlighted key labels
- concise but information-rich educational content
- visual scoring, quick takeaways, or a Top 5 module

Adapt the content sections automatically based on the topic. Useful categories include: basic profile, classification, appearance, habits or ecology, formation mechanism or structure, growth or usage conditions, care or maintenance advice, risks and cautions, suitable users or use cases, pros and cons, and a quick scorecard.

Visual requirements: use a clean light background, soft colors, subtle shadows, refined small icons, rounded information cards, and neat layout. The information density should be high but not crowded, and the final image should feel publishable, collectible, and repeatable as a knowledge-card format rather than an advertisement.

Do not make it look like a commercial promo poster. Emphasize knowledge organization, modular information, and a field-guide presentation.
```

**点评**：给"候选栏目池"让模型按主题自动取舍栏目（basic profile / habitat / risks / Top 5 / scorecard……），并用"像图鉴不像广告"的双重边界控制调性。
**来源**：GPT-Image2-Skill · No.70

### 【Nature 风格论文四联图】
适用：科研论文配图、组会展示，A–D 多面板学术图。

```text
Create a Nature Medicine / Science Translational Medicine style research paper figure, landscape 3:2 (1536×1024), soft literature-science palette, minimal and elegant.

Figure title: "Patient cohort and multimodal biomarker workflow".

Layout: a clean 4-panel academic figure labeled A–D with small bold panel letters.
A. CONSORT-style patient cohort flow diagram: "Screened n=1,248" → "Eligible n=612" → branch into "Training cohort n=428" and "External validation n=184". Include exclusion side boxes: "missing imaging n=81", "insufficient follow-up n=43", "quality-control fail n=32".
B. Multimodal sample-processing flow: icons for "CT imaging", "blood proteomics", "EHR timeline", "outcome labels" flowing into a pale-blue fusion box "feature harmonization".
C. Small Kaplan–Meier survival plot with two clean curves labeled "low-risk" and "high-risk", muted teal vs soft rose, x-axis "Months", y-axis "Event-free survival".
D. Compact table-style performance summary with three rows: "AUROC", "C-index", "Calibration slope" and two columns "Internal" / "External".

Style requirements: white background, light gray axes, thin lines, ample margins, muted teal, dusty blue, soft coral, pale sand, no neon, no dark background, Nature journal figure aesthetics, readable labels, precise arrows, subtle gridlines, no decorative clutter, no fake logos, no watermark.
```

**点评**：A–D 每个面板给出确切的节点、数字、轴标签，末尾统一"Style requirements"段（白底/细线/柔和色/无霓虹/无假 logo）——科研图的可信度全部来自这些具体值。
**来源**：GPT-Image2-Skill · No.76

### 【模型架构图】
适用：神经网络/系统架构图、算法图解，学术论文风。

```text
Landscape 16:9 academic concept figure of the Transformer encoder-decoder architecture, NeurIPS camera-ready style. Two vertical column stacks side-by-side with a dashed divider.

LEFT column header: "ENCODER (×N)". Blocks bottom-to-top: "Input tokens" → "Input Embedding" → "+ Positional Encoding" → dashed "Encoder layer" containing "Multi-Head Self-Attention", "Add & Norm", "Feed-Forward", "Add & Norm", with thin curved residual arrows around each sublayer.

RIGHT column header: "DECODER (×N)". Blocks bottom-to-top: "Output tokens (shifted right)" → "Output Embedding" → "+ Positional Encoding" → dashed "Decoder layer" containing "Masked Multi-Head Self-Attention", "Add & Norm", "Multi-Head Cross-Attention" (horizontal arrow from encoder top labeled "keys, values"), "Add & Norm", "Feed-Forward", "Add & Norm". Above decoder: "Linear", "Softmax", "Output probabilities".

Title: "Transformer: encoder–decoder with multi-head attention". Subtitle: "Vaswani et al., 2017".
```

**点评**：用"自底向上的块序列 + → 箭头 + 括号注明层内容 + 残差环绕箭头"的图解语法（diagram grammar）描述结构，而非形容词堆砌；出处引用作可信度副标题。
**来源**：GPT-Image2-Skill · No.80

### 【数据可视化·小倍数网格】
适用：统计图族海报、编辑级数据可视化（small multiples）。

```text
Produce a clean editorial data visualization poster showing a 4x3 small-multiples grid of monthly climate charts for 12 fictional cities. Use a white background, generous margins, and a restrained palette of navy, rust, sky blue, olive, and charcoal. Each mini-panel should contain a temperature line and precipitation bars with consistent axes and ultra-legible labels. Include a title block with the in-image text "Annual Climate Profiles" and subtitle "12 Cities, 2025". Label panels "Northport", "Solmere", "Aster Bay", "Ridgefall", "Halcyon", "Verdin", "Glass Harbor", "Red Mesa", "Moonfield", "Lake Arden", "Cinder Point", and "Juniper". Use month labels "J F M A M J J A S O N D" and axis labels "Temp °C" and "Rain mm". Add numeric legend values "0", "10", "20", "30", and "100". Keep the composition highly structured, scientifically clear, and visually elegant, with crisp typography, aligned scales, and publication-grade chart rendering.
```

**点评**：图表族先点名（small-multiples grid），再规定"跨面板一致坐标轴"这一小倍数图的灵魂约束，12 个城市名逐个列出避免模型编造。
**来源**：GPT-Image2-Skill · No.108

### 【中文手绘信息图卡片】
适用：小红书/自媒体金句卡、手绘风知识卡片，末尾引号内换文案即可复用。

```text
创作一张手绘风格的信息图卡片，比例为9:16竖版。卡片主题鲜明，背景为带有纸质肌理的米色或米白色，整体设计体现质朴、亲切的手绘美感。

卡片上方以红黑相间、对比鲜明的大号毛笔草书字体突出标题，吸引视觉焦点。文字内容均采用中文草书，整体布局分为2至4个清晰的小节，每节以简短、精炼的中文短语表达核心要点。字体保持草书流畅的韵律感，既清晰可读又富有艺术气息。周边适当留白。

卡片中点缀简单、有趣的手绘插画或图标，例如人物或象征符号，以增强视觉吸引力，引发读者思考与共鸣。整体布局注意视觉平衡，预留足够的空白空间，确保画面简洁明了，易于阅读和理解。
"做 IP 是长期复利
坚持每日更新，肯定会有结果，因为 99% 都坚持不了的！"
```

**点评**：纸质肌理、毛笔草书、红黑配色、"2至4个小节"的数量上限、留白要求全部固定成协议，只需替换末尾引号内的文案——中文写法直接服务文字渲染的最佳样本。
**来源**：awesome-gpt4o-images（jamez-bondos） · @dotey（案例 38）

### 【双语工业科普挂图】
适用：中英双语工程/市政/工业题材科普海报，多语言排版要求高的场景。

```text
Create a horizontal infographic poster explaining the working principles of a wastewater treatment plant. The design style is industrial, modern, and high-contrast, utilizing a color palette of deep red, black, white, and teal/blue for water elements.

**Layout & Text Elements:**
1.  **Top Left/Center (Headline):** Large, bold, distressed red Chinese characters "污水处理厂" (Wastewater Treatment Plant) spanning across the top. Below it, large black bold text "工作原理" (Working Principles). Smaller black text underneath: "从进水、分离、生化反应到净化出水" (From influent, separation, biochemical reaction to purified effluent).
2.  **Left Sidebar:** Vertical layout with small text blocks. Top block: "让每一滴污水重回自然" (Let every drop of sewage return to nature), "水的下一站是更洁净的未来" (Water's next stop is a cleaner future), English text "CLEANER WATER BRIGHTER TOMORROW". Bottom block (red background): "处理改变为了更好的水环境" (Treatment changes for a better water environment), English text "CLEAN CYCLE HEALTHY CITIES".
3.  **Right Side (Background Image):** A large photographic collage showing an aerial view of circular clarifier tanks filled with blue-green water, connected by pipes and walkways. Overlay text on the right: "从污水到清水" (From sewage to clear water), "连接城市与更健康的生活" (Connecting cities with healthier lives), "FOR A CLEANER TOMORROW", "水循环 城市运行 与自然共生" (Water cycle, city operation, symbiosis with nature), "净化 让城市更有生命力" (Purification makes cities more vibrant), "CLEAN WATER STRONGER CITIES".
4.  **Bottom Center (Process Diagram):** A schematic cross-section diagram showing the flow of water through different stages. Arrows indicate direction from left to right. Labels above the sections: "格栅 / 沉砂" (Screening/Grit Chamber), "初沉" (Primary Sedimentation), "生化反应" (Biochemical Reaction - depicted with bubbles), "二沉" (Secondary Sedimentation). Labels at ends: "进水" (Influent) on left, "出水" (Effluent) on right.
5.  **Bottom Right:** Small text block: "更干净的水 更宜居的城市 更可持续的明天" (Cleaner water, more livable cities, more sustainable tomorrow), English text "CLEANER WATER HEALTHIER CITIES A BRIGHTER TOMORROW".
6.  **Center Red Box:** A small red square containing white text: "看不见的工程 支撑看得见的美好生活" (Invisible engineering supports visible good life), English text "INFRASTRUCTURE FOR A HEALTHIER TOMORROW".

**Visual Style Details:**
*   Use a grainy texture overlay on the entire image to give it a printed paper feel.
*   The typography should be heavy sans-serif for Chinese characters.
*   The water in the photos and diagrams should be a distinct teal/cyan color against the grayscale/red/black background.
```

**点评**：逐区块写死 6 处中英双语标语与流程图四个工序标签，并规定"红色粗黑中文标题 + 灰度照片 + 青色水体 + 全图颗粒质感"——固定版式契约 + 逐字文案的双教科书。
**来源**：awesome-gpt-image-2（YouMind-OpenLab） · R42

### 【技术爆炸图·精确计数】
适用：产品/器械分解图、医疗工程可视化，要求部件数与标注数严格可控。

```text
Goal: Create a hyper-realistic futuristic medical engineering visualization of an exploded transparent artificial human heart, presented like a premium bioengineering product render with technical callouts.

Canvas: 4:3 horizontal image, dark laboratory background, glossy black reflective floor, cinematic rim lighting, shallow depth of field, cool blue highlights and warm amber internal glow. The heart floats centered above the floor with a soft reflection beneath it.

Main subject: A transparent biomechanical anatomical heart labeled as {argument name="device concept" default="next-generation bioengineered artificial heart"}. The central heart body is made of clear glass-like biocompatible polymer, with visible internal tubes, valves, microfluidic channels, circuit traces, miniature mechanical pumps, red and blue glowing vascular pathways, and amber illuminated electronic modules. Use realistic refraction, caustics, chrome screws, polished metal rings, and black carbon-fiber structural components.

Exploded layout: Show exactly 13 major separated component groups around the central heart: 1 central transparent heart chamber; 2 left outer clear curved shell; 3 left black carbon-fiber rib panel; 4 left inner transparent curved support layer; 5 upper-left aorta connector ring assembly; 6 upper central transparent aorta and vessel towers; 7 upper-right pulmonary artery connector ring assembly; 8 right-side cylindrical port and interface rings; 9 right black carbon-fiber rib panel; 10 right transparent circuit-interface module with amber glow; 11 right outer clear curved shell; 12 far-right small transparent cap/lens; 13 multiple small floating screws and bolts aligned around the exploded parts. Keep all parts suspended in precise horizontal layers, as if disassembled for inspection.

Technical annotations: Add thin white/gray leader lines and small uppercase sci-fi typography. Include exactly 7 visible callout labels: 1 “AORTA” with subtext “HIGH-FLOW / BIOCOMPATIBLE / POLYMER”; 2 “RIGHT ATRIUM” with subtext “MICRO-FLUIDIC / CHANNELS”; 3 “CARBON-FIBER RIB STRUCTURE” with subtext “ULTRA-LIGHT / HIGH-STRENGTH”; 4 “VENTRICLE” with subtext “BIO-MIMETIC / PUMP CHAMBER”; 5 “PULMONARY ARTERY” with subtext “PRESSURE REGULATING / VALVE”; 6 “BIO-CIRCUIT INTERFACE” with subtext “NEURAL SYNC / WIRELESS POWER / REAL-TIME MONITORING”; 7 “MICRO-FLUID CHANNELS” with subtext “NANO-SCALE / SELF-CLEANING / FLOW OPTIMIZATION”. Place these labels around the heart without covering key details.

Footer text: In the bottom left, small spaced lettering reads {argument name="left footer text" default="HUMANITY\nA STRONGER TOMORROW"}. In the bottom right, add a tiny schematic line icon and text reading {argument name="right footer text" default="BIOENGINEERING\nFOR A HEALTHIER WORLD"}.

Visual style: Ultra-detailed photorealistic 3D render, luxury industrial design, transparent medical device, carbon fiber texture, chrome hardware, glass refraction, glowing red and blue tubes, amber circuit light, high contrast, clean futuristic interface typography, technical diagram aesthetic, 8k quality.

Constraints: No people, no hands, no blood or gore, no cartoon styling, no messy background, no extra large titles. Keep the anatomy recognizable as a human heart while emphasizing transparent futuristic engineering.
```

**点评**："exactly 13 major separated component groups" 逐件编号、"exactly 7 visible callout labels" 连标签副文案都写死，再配 Constraints 禁血腥禁卡通——用计数 + 逐条命名把复杂结构图的随机性压到最低。
**来源**：awesome-gpt-image-2 · R49

## 避坑清单（组装该类 prompt 时逐条对照）

1. **先限模块数再补视觉细节**：开头就写死"4 个模块，每模块 2-4 条短句"这类配额（No. 71、案例 38 的"2至4个小节"），否则 AI 信息图默认文字爆炸。
2. **文案克制**：千万不要把大段正文塞进画面里——"模型不是排版工人"（freestylefly 避坑指南信息图原文），只用短句/短语/标签。
3. **固定版式契约前置**：先写分区结构（Top / Left / Upper right / Middle right / Bottom，或 1-6 编号区块），每个区块指明内容与文字，最后才写视觉风格（No. 69、R42）。
4. **文字逐字给全**：标题、副标题、标签、图例、页脚全部写出原文，并指定字体（粗黑/细衬线/手写）、位置、颜色，一个字都不留给模型自由发挥（F2/R42 写法）。
5. **中文乱码防护**：显式要求"简体中文、清晰可读、无乱码错字、无英文拼音"，avoid 里点各 tiny text / garbled characters / blurry text（No. 69/11）。
6. **精确数量防漂移**：复杂结构用 exactly N 句式锁死部件数/标签数/面板数，并逐条命名每个部件（R49 的 exactly 13 + exactly 7；awesome-gpt-image-2 全库实测统计）。
7. **用"像 A 不像 B"声明调性**：像博物馆展板/图鉴/工程白皮书，不像广告海报/电商详情页/动漫插图（No. 69/10），边界词成对给。
8. **数据必须写实值**：论文图/统计图的节点、样本数、轴标签、图例值逐个给出（n=1,248、"Temp °C"），禁止模型编造数据；小倍数图还要锁"跨面板一致坐标轴"（No. 76/15）。
