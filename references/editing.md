# 图像编辑与风格迁移

> 覆盖局部改图（不变量写法）、换装换背景、多图合成职责切分、风格迁移（保留原图 vs 重绘两种立场）、材质替换与对比拼贴。写作前先读 2-3 条最相关样例，套用其结构而非照抄内容。

tags: 图像编辑, 局部改图, 风格迁移, 换装换背景, 身份锁, 材质替换

## 样例

### 【局部改图·不变量写法（改气氛不改构图）】
适用：只改季节/天气/光线/氛围，构图、主体与可读性一丝不能动

```text
Make it a winter evening with heavy snowfall, snow dusted on the board and pieces, breath vapor in the air, cold blue-grey lighting, chess position still clearly readable. Preserve the original chess-board composition and landscape aspect ratio exactly; keep the board and pieces aligned and readable.
```

**点评**：两段式契约——先说改什么（冬夜/落雪/呵气/冷光），再用 "Preserve … exactly; keep …" 锁定构图与可读性，50 词内完成一次精准重打光。
**来源**：GPT-Image2-Skill · No. 101（源自 OpenAI Cookbook）

### 【只换装不改人（Preserve/Transform 双清单）】
适用：换服装/配色，脸、发型、表情、姿势印象全部锁死

```text
【OUTFIT CHANGE ONLY】

Use the attached character image as the highest-priority reference.

Create the final image in a vertical 4:5 composition.

Preserve the original character identity and illustration style.
Keep the original face, eyes, hairstyle, hair color, expression, and overall pose impression.

Change only the outfit and matching accessories.

Recompose the image naturally into a 4:5 vertical frame while preserving the original character, expression, pose impression, and overall scene feeling as much as possible.

Keep the character’s face and hand-heart gesture clearly visible in the 4:5 composition.

Do not redesign the scene.
Do not create a completely new pose.
Do not zoom out unnecessarily.
Do not reveal additional body parts just to show outfit details.
If legs or feet are not visible in the original image, do not add them.

OUTFIT:

A cute retro-inspired dress in red, black, and white with a clean polka-dot design.

Black fitted bodice with a large rounded white Peter Pan collar.

Short red puff sleeves with evenly spaced white polka dots and softly gathered cuffs.

High-waisted red skirt with white polka dots and a softly flared A-line silhouette.

Large white fabric bow at the waist.

Optional matching red-and-white polka-dot ribbon hair accessory.

If footwear is visible, use simple matching red shoes.

Clean coordinated costume design.
Consistent polka-dot pattern.
No extra decorations.

Adapt the outfit naturally to the character's existing visible area.
```

**点评**：开头"【OUTFIT CHANGE ONLY】+ highest-priority reference"，Preserve 清单（脸/眼/发型/表情/姿势印象）与 Change 段（仅服装及配套配饰）泾渭分明，再以四条 Do not 把换装副作用全部封死。
**来源**：awesome-gpt-image-2 · R90

### 【换背景创意合成（面部身份锁）】
适用：保留真人面部特征，换场景/换穿搭做创意合成

```text
Use the person in the reference image as the main character, suitable for both male and female subjects. Preserve the exact facial identity, facial structure, age, skin tone, and natural expression. Do not change the person’s identity or create an artificial/plastic-looking face.

Create a 4:5 vertical street-editorial photograph set in a stylish urban café alley with a large black brick wall. On the wall, create a huge black-and-white realistic mural depicting the same person from the reference image, holding a metallic coffee pot and pouring coffee downward.

The real person stands directly below the mural, holding a coffee cup positioned perfectly under the stream of coffee coming from the mural, creating a fun, artistic, interactive, and viral visual effect.

For a female subject:
Wear an oversized white shirt with a relaxed, slightly loose fit, youthful and modern styling, naturally tucked in, paired with jeans or dark-colored trousers and clean sneakers. Avoid a stiff corporate look or tight-fitting clothing.

For a male subject:
Use a modern urban-casual outfit that looks youthful, clean, stylish, and contemporary.

The mural should have a realistic street-art aesthetic, featuring black and white tones with bold orange accents, expressive brush strokes, paint drips, and short graffiti typography such as “BỪNG NĂNG LƯỢNG” or “CÀ PHÊ MỖI NGÀY.”

Use neutral daylight with natural skin tones and no excessive yellow color cast. Camera angle should be slightly low and editorial, showing the subject full-body with a relaxed, natural pose. Do not use a chin-on-hand pose.

Ultra-photorealistic, cinematic depth of field, realistic hands, accurate coffee stream, natural body proportions, authentic skin texture, highly detailed, 8K quality.

Do not copy the exact composition of the reference/sample image. Keep only the core concept of a real person interacting with a giant mural while creating a fresh, original, visually striking composition.
```

**点评**：先声明"以参考图人物为主角、Preserve the exact facial identity、禁止 artificial/plastic-looking face"，再用 "For a female subject: / For a male subject:" 条件分支适配两类用户，最后强调只借概念、不抄构图。
**来源**：awesome-gpt-image-2 · R23

### 【多图合成·双参考图职责切分】
适用：同时上传角色设定图与另一张风格/质量参考图，防止模型抄错对象

```text
Create an extreme close-up portrait of the character in the attached character reference sheet. Treat that sheet as the absolute authority for the character's identity and design: preserve their face, facial proportions, skin tone, hair style/color, eyes, ears or other character features, and any visible clothing/accessories. Do not redesign the character.
The second attached portrait is ONLY a rendering-quality reference. Do not copy that character's identity, face, hair, colors, clothing, accessories, expression, pose, or composition. Use it only as the target for detail density and finish: highly defined facial features, dimensional anime shading, intricate eyes and eyelashes, individually rendered hair strands, subtle skin highlights and warmth, sophisticated lighting, depth, material definition, and extremely polished cinematic anime rendering.
Frame the subject very tightly from approximately the upper chest/clavicle to the tips of their hair/ears, with the face dominating the image. Use an eye-level camera and direct eye contact. Give them a small natural smile with subtle blush. Preserve recognizable anime facial proportions while adding significantly more dimensional definition and fine detail; do not make the face photorealistic.
Use a simple dark atmospheric background and cinematic lighting that complements the character's existing palette. Keep the eyes, face, and nearest hair strands exceptionally sharp, with gentle depth falloff elsewhere.
Do not show the waist, hips, legs, or full body. Do not create a detailed environment. Do not copy the second portrait's scene or character.
Character sheet = WHO the character is. Second portrait = ONLY the LEVEL OF RENDERING QUALITY.
Generate the portrait now.
```

**点评**：一句 "Character sheet = WHO the character is. Second portrait = ONLY the LEVEL OF RENDERING QUALITY." 解决多图输入时身份权威与质量参考混淆的问题——多图合成先分配每张图的职责。
**来源**：awesome-gpt-image-2 · R2

### 【风格迁移·照片与手绘世界融合（保留原图立场）】
适用：照片主体与构图保持写实，局部向下延展成插画世界

```text
Use the uploaded image as the primary reference and transform it into a vertical 3:4 surreal editorial artwork that seamlessly combines photorealistic food/object photography with a whimsical hand-drawn storybook illustration.

Preserve the main subject, composition, colors, textures, and recognizable details of the original photograph. Keep the upper portion highly photorealistic and naturally lit, with realistic materials, shadows, reflections, depth of field, and authentic photographic detail.

Create a seamless visual transition from the photographed subject into an imaginative illustrated world below. Identify the most visually meaningful element in the photograph—such as a liquid, food ingredient, object, pattern, trail, shadow, or texture—and organically extend it downward into the illustration, transforming it into a river, pathway, landscape, trail, or other creative scene.

The illustrated section should appear on a warm off-white textured paper background, using delicate black ink/pencil linework, subtle watercolor and gouache textures, imperfect handmade details, soft muted colors, and a charming vintage storybook aesthetic. Add small environmental details appropriate to the subject, such as tiny people, plants, rocks, objects, or landscape elements.

Include a short handwritten phrase that naturally relates to the concept and the transformation, positioned subtly within the illustrated area. The typography should look genuinely handwritten, imperfect, minimal, and artistic.

The photograph and illustration must feel like one continuous visual story, not two separate images. Avoid a hard horizontal split, borders, frames, arrows, labels, or obvious digital compositing. The photographed element should physically appear to flow, fall, extend, or transform into the illustrated world.

Aesthetic: poetic, whimsical, clever, minimalist, premium editorial magazine art, surreal but believable, tactile paper texture, natural imperfections, sophisticated visual storytelling.

Composition: vertical 3:4, balanced negative space, strong focal point, seamless transition, high detail, realistic photography + delicate hand-drawn illustration, no unnecessary elements.
```

**点评**：让照片中"最有叙事潜力的元素"自然延伸成插画世界，并明令禁止硬分界线、边框、箭头——两张画面必须是一个连续故事而非拼接。
**来源**：awesome-gpt-image-2 · R29

### 【风格迁移·重绘立场（原图只作视觉参考）】
适用：照片转插画/海报等全新画风，成品中不能残留原照片

```text
Create a finished editorial character poster inspired by the uploaded reference image. Preserve the recognizable identity, hairstyle, clothing details, pose, and important visual characteristics of the subject while translating them into a sophisticated flat geometric illustration.

FORMAT LOCK
Vertical 3:4 composition. Edge-to-edge warm off-white paper background. One standalone poster. Clean editorial layout.

CHARACTER
One adult character constructed from a few oversized asymmetric geometric shapes. Slightly exaggerated proportions, small head, elongated capsule-like limbs, simple mitten-style hands, and one oversized object integrated naturally into the pose and silhouette. Preserve the subject's recognizable appearance while simplifying details into graphic shapes.

STYLE
Flat geometric illustration, asymmetric proportions, crisp color blocks, soft airbrushed shading, subtle dark-to-color spray gradients where shapes overlap, fine print grain, delicate stippling mostly inside darker areas, refined contemporary editorial poster aesthetic.

FACE & EXPRESSION
Minimal black cut-paper facial features: simple crescent eyes and minimal mouth. The emotion should be communicated primarily through the character's full-body gesture and silhouette rather than detailed facial expression.

PALETTE
Warm off-white #F3F1EB, near-black ⁠10100F, hot pink #F553D2, warm red #F42726, cobalt ⁠293EA1, emerald ⁠13785D. Keep colors flat and graphic with controlled soft gradients only where forms overlap.

TEXT
Add one short caption in small bold black uppercase sans-serif inside an open paper pocket. Caption: "{argument name="caption text" default="[MAIN_TEXT]"}". No other text, logos, labels, or typography.

CUSTOMIZATION
Character & Object: [WHO + THE OVERSIZED THING]
Gesture & Emotion: [POSE + FEELING]
Shape Idea: [HOW BODY AND OBJECT FORM THE SILHOUETTE]
COMPOSITION
Keep the character and oversized object as the main visual focus. Use generous negative space and a balanced editorial arrangement. The object should visibly affect the overall silhouette and feel integrated into the character's pose.

NEGATIVE PROMPT
No extra text, logos, outlined cartoon style, glossy 3D, realistic skin, photorealism, coarse canvas texture, busy background, extra limbs, distorted anatomy, excessive facial detail, photorealistic shading, random objects, clutter, watermark.
```

**点评**：FORMAT LOCK 声明 "One standalone poster"，HEX 色值锁死调色板，情绪交给全身剪影表达；重绘类务必配上 "Use the photograph only as the visual reference. The original photograph must NOT appear anywhere in the final image."（同库 R32 的标准句式）。
**来源**：awesome-gpt-image-2 · R33

### 【材质替换（JSON 美学定义）】
适用：对参考图整体重新纹理化：玻璃/金属/毛绒/镀铬等材质幻想

```text
对参考图片进行重新纹理化，基于下方的 JSON 美学定义
{
  "style": "photorealistic 3D render",
  "material": "glass with transparent and iridescent effects",
  "surface_texture": "smooth, polished with subtle reflections and refractive effects",
  "lighting": {
    "type": "studio HDRI",
    "intensity": "high",
    "direction": "angled top-left key light and ambient fill",
    "accent_colors": ["blue", "green", "purple"],
    "reflections": true, "refractions": true, "dispersion_effects": true, "bloom": true
  },
  "color_scheme": {
    "primary": "transparent with iridescent blue, green, and purple hues",
    "secondary": "crystal-clear with subtle chromatic shifts",
    "highlights": "soft, glowing accents reflecting rainbow-like effects",
    "rim_light": "soft reflective light around edges"
  },
  "background": { "color": "black", "vignette": true, "texture": "none" },
  "post_processing": { "chromatic_aberration": true, "glow": true, "high_contrast": true, "sharp_details": true }
}
```

**点评**：把材质、灯光、配色、背景、后期拆成布尔与枚举字段的 JSON 控制面板，是图生图精修最可控的写法。
**来源**：awesome-gpt4o-images · 案例 93 · @egeberkina

### 【对比图（双现实拼贴）】
适用：一半图纸一半成片、前后对比、草图 vs 渲染等对比构图

```text
Pick any object and slice it in half vertically, the left side rendered as a detailed technical schematic blueprint with grid lines and annotations, the right side as a polished 3D model render, the center seam flickering and glitching where the two visual realities collide.
```

**点评**：一句话双现实拼贴（左蓝图右渲染、接缝故障感），证明极短 prompt 靠强概念照样出圈。
**来源**：awesome-gpt-image-2-API-and-Prompts · Case 459 · @iamaiistudio

## 避坑清单（组装该类 prompt 时逐条对照）

1. 参考图改写三件套：声明参考图角色（唯一身份来源 / 仅构图模板 / 仅质量参考）Preserve 清单（脸、发型、构图、相机角度、元素数量）Transform 清单（目标风格 + 材质工艺）。
2. 先分清两种立场：拼贴纪念类"保留原图照"（Keep it realistic, do not over-edit）vs 重绘类"原图不得出现"（The original photograph must NOT appear anywhere in the final image）——立场写错成品必跑偏。
3. 身份锁写法：Preserve the exact facial identity / facial structure / skin tone + "Do not change the person's identity" + 禁 artificial/plastic-looking face；涉及身份的编辑至少三件套齐全。
4. 局部改图要封副作用：不重设计场景、不摆新姿势、不乱缩放（Do not zoom out unnecessarily）、原图没露的部位不许补画。
5. 高危编辑用 LOCK 大写条款族：FORMAT LOCK / IDENTITY LOCK / POSE LOCK / REFERENCE LOCK，必要时加 NON-NEGOTIABLE。
6. 修复/增强类只动质量不动内容：Keep details the same, only change the quality and resolution；后续批次直接 "do the same for these attached photos" 复用。
7. 参考图重组与图内文字忠实：undistorted type / artwork preserved exactly（见 GPT-Image2-Skill No. 56 刀版图组装），要什么字就把字引起来。
8. 点名模型坏习惯：photo-of-a-poster（海报套样机）、AI 感配色与颗粒、镜头乱缩放，写进负面清单。
