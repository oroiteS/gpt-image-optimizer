# 产品与电商

> 定位：覆盖电商主图、产品棚拍、食物摄影、概念广告、结构化 JSON 渲染与 UGC 场景化带货图。写作前先读 2-3 条最相关样例，套用其结构而非照抄内容。

tags: 产品图, 电商主图, 棚拍, 食物摄影, JSON渲染, UGC场景

## 样例

### 【万能产品棚拍·极简模板】
适用：任何产品的兜底棚拍主图，Raycast 参数化填空

```text
Professional advertising product photo of "{argument name="product" default="[PRODUCT NAME]"}", studio shot on a {argument name="background" default="neutral background [light beige / blue gradient]"}, soft diffused lighting, subtle shadows, product centered in frame, three-quarter angle view, high detail on material texture, clean modern aesthetic in the style of premium brand campaigns, 4K resolution, 1:1 aspect ratio
```

**点评**：仅 40 余词却覆盖产品名、背景、柔光、阴影、居中、3/4 角度、材质细节、高级品牌感、4K、1:1 十要素——"最小可用模板"的极限压缩，适合做兜底产品图模板。
**来源**：awesome-gpt-image-2 · R115

### 【微缩工地护肤品广告·概念主图】
适用：概念隐喻型主图，把"匠心/工艺"卖点变成叙事场景

```text
A hyper-realistic miniature diorama product advertisement featuring an oversized luxury skincare pump bottle labeled "LUXEVEIL Skin Science - Radiance Nourishing Body Lotion" in cream/beige with a polished gold pump top, placed on a circular platform. Tiny figurine construction workers dressed in yellow coveralls and white hard hats swarm around the bottle climbing scaffolding, painting the bottle with rollers, operating a tower crane, working near industrial tanks and pipework, and unloading a miniature flatbed truck. The scene includes metal scaffolding structures, industrial silos, orange traffic cones, wooden barricades, and storage barrels. The overall color palette is warm beige, cream, gold, and mustard yellow. Studio photography style with soft diffused lighting, no shadows, clean beige background. The concept metaphorically shows workers "crafting" or "building" the perfect lotion. Tilt-shift miniature aesthetic, ultra-detailed, commercial product photography, 8K resolution, photorealistic CGI render.
```

**点评**：用"微缩工人建造巨型瓶子"的隐喻把『工艺/匠心』卖点变成叙事场景，色板、布光、tilt-shift 一句不落，概念型电商主图的样板。
**来源**：awesome-gpt-image-2-API-and-Prompts · Case 1 · @Strength04_X

### 【巧克力威化产品渲染·JSON 配置式】
适用：多系统互相作用的复杂产品渲染（环境/材质/物理/粒子/流体），JSON 规格书写法

```text
/* PRODUCT_RENDER_CONFIG: Chocolate Wafer Hazelnut Edition
   VERSION: 2.0.1
   AESTHETIC: Premium Commercial Food Photography */

{
  "ENVIRONMENT": {
    "Background": "Gradient(Dark_Warm_Brown)",
    "Atmospheric_FX": ["Floating_Particles", "Depth_Blur", "Cinematic_Bokeh"],
    "Lighting": { "Type": "Directional_Studio_Warmer", "Highlights": "Specular_Glossy_Reflections", "Shadow_Softness": "High" }
  },
  "CORE_ASSETS": {
    "Primary_Subject": "Wafer_Rolls",
    "Physics": "Zero_Gravity_Diagonal_X_Composition",
    "Material_Properties": {
      "Outer": "Milk_Chocolate_Coating",
      "Surface_Texture": "Irregular_Nut_Clusters_Embedded",
      "Interior_Cross_Section": { "Structure": "Crispy_Hollow_Wafer", "Core": "Silky_Chocolate_Cream_Filling" }
    }
  },
  "PARTICLE_SYSTEMS": [
    { "Object": "Chocolate_Blocks", "Detail": "Rectangular_Embossed_Letter_B", "State": "Floating" },
    { "Object": "Hazelnuts", "State": "Halved_and_Fragmented", "Distribution": "Random_Orbit" }
  ],
  "FLUID_DYNAMICS": { "Element": "Chocolate_Splash", "Behavior": "Dynamic_Backdrop_Flow", "Viscosity": "Thick_Glossy" },
  "RENDER_OUTPUT": { "Resolution": "8K_UHD", "Aspect_Ratio": "3:4", "Quality_Flags": ["Hyper_Realistic", "Sharp_Foreground", "Indulgent_Mood"] }
}
```

**点评**：当画面有多个相互作用的系统（环境/材质/物理/粒子/流体）时，JSON schema 比散文更可控，VERSION/AESTHETIC 头注释让 prompt 像一份可迭代的规格书。
**来源**：GPT-Image2-Skill · No. 57

### 【冰淇淋成分标注 JSON 主图】
适用：需要成分标注/callout 箭头的电商主图，结构化 JSON 写法

```text
{
  "resolution": "8K",
  "aspect_ratio": "3:4",
  "image_type": "photorealistic commercial product render",
  "scene_description": {
    "main_subject": "A vertically centered ice cream bar mounted on a wooden stick",
    "orientation": "upright, front-facing, slightly elevated perspective",
    "composition": "single product centered with surrounding ingredient labels and curved arrows"
  },
  "background": {
    "color": "warm golden-yellow gradient",
    "texture": "smooth, matte, evenly illuminated",
    "lighting_falloff": "subtle vignette, darker towards edges"
  },
  "lighting": {
    "type": "studio lighting",
    "key_light": "soft frontal light emphasizing chocolate gloss",
    "fill_light": "balanced fill preserving texture detail",
    "specular_highlights": "visible on melted chocolate coating",
    "shadows": "soft shadow beneath the stick"
  },
  "ice_cream_bar": {
    "shape": "rounded rectangular bar",
    "surface": "smooth with visible embedded inclusions",
    "layers": [
      {
        "layer_position": "top coating",
        "material": "milk chocolate",
        "state": "melted and dripping",
        "texture": "glossy, thick, fluid",
        "details": [
          "multiple chocolate drips flowing downward",
          "irregular almond pieces embedded in coating",
          "rounded drip edges pulled by gravity"
        ]
      },
      {
        "layer_position": "left interior",
        "material": "chocolate ice cream",
        "texture": "dense, creamy",
        "details": [
          "small dark brownie chunks evenly dispersed",
          "matte finish contrasting outer chocolate"
        ]
      },
      {
        "layer_position": "right interior",
        "material": "vanilla ice cream",
        "texture": "smooth and creamy",
        "details": [
          "visible caramel pieces",
          "light beige caramel chunks with rounded edges"
        ]
      }
    ]
  },
  "stick": {
    "material": "light natural wood",
    "texture": "smooth with subtle grain",
    "shape": "rounded edges, flat profile",
    "visibility": "fully visible below ice cream bar"
  },
  "ingredient_callouts": {
    "style": {
      "arrows": "curved, thick, dark brown",
      "text_color": "dark brown",
      "font_style": "clean sans-serif",
      "layout": "balanced around product"
    },
    "labels": [
      {
        "text": "Chocolate with almonds",
        "position": "top-left",
        "visual_aid": ["whole almonds", "small chocolate squares"]
      },
      {
        "text": "Chocolate ice cream with brownies",
        "position": "left-middle",
        "visual_aid": ["brownie chunks"]
      },
      {
        "text": "Chocolate ice cream with brownies",
        "position": "right-middle",
        "visual_aid": ["brownie chunks"]
      },
      {
        "text": "Vanilla ice cream with caramel pieces",
        "position": "bottom-right",
        "visual_aid": ["caramel cubes", "white vanilla pieces"]
      }
    ]
  },
  "color_palette": {
    "primary_colors": ["milk chocolate brown", "golden yellow", "cream white"],
    "secondary_colors": ["dark brownie brown", "light caramel orange", "almond beige"]
  },
  "render_quality": {
    "sharpness": "extreme micro-detail visibility",
    "texture_fidelity": "high realism",
    "noise": "none",
    "depth_of_field": "moderate, product fully in focus"
  },
  "style_tags": [
    "luxury dessert advertising",
    "hyper-realistic food photography",
    "commercial product render",
    "clean studio composition"
  ]
}
```

**点评**：直接用 JSON 描述产品分层/灯光/标注箭头，labels 数组逐条给"文字+位置+辅助视觉"，是需要精确标注的电商主图极致示范。
**来源**：awesome-gpt-image-2-API-and-Prompts · Case 14 · @iamaiistudio

### 【香水瓶微缩景观·光学物理】
适用：高端质感产品图，用材质物理行为代替质量形容词

```text
A giant, rounded, light green transparent glass perfume bottle, containing a miniature mossy valley, bonsai trees, rocks, and small waterfalls sealed inside. Placed in a brutalist raw concrete space covered by water; cold daylight enters through architectural openings from the upper left, while warm sunset light forms a rim light from the back right. The glass exhibits real refraction, caustics, tiny water droplets, and highlight distortion; the water surface creates natural reflections. Low-angle product photography, subject positioned slightly to the right, large negative space, realistic optical depth of field, high-end fragrance advertising quality, no text, no logo, no plastic CGI look.
```

**点评**：不堆 "8K、masterpiece"，而是写"真实折射、焦散、细小水珠、高光畸变、水面自然反射 + 冷日光/暖落日双光源位"——材质物理行为才是高级感的真正来源。
**来源**：awesome-gpt-image-2 · R99

### 【分层沙拉罐+手写配料表】
适用：食物摄影、透明容器分层产品、图内手写文字

```text
Create a photorealistic lifestyle food photography scene featuring four clear glass meal-prep jars arranged on a clean light-colored kitchen countertop. Each jar has a natural bamboo wooden lid with a white sealing ring.

The jars contain beautifully layered Mexican-inspired chicken salads, with clearly separated colorful layers from bottom to top: diced cucumber, cherry tomatoes, red onion, red bell pepper, sweet corn, black beans, crumbled Cotija cheese, fresh chopped romaine lettuce, and shredded cooked chicken. Keep every ingredient fresh, vibrant, crisp, and visibly distinct through the transparent glass.

Place two jars in the foreground and two slightly behind them for depth and composition. Warm modern kitchen background with subtle wooden cabinets, soft natural daylight coming from a window, shallow depth of field, realistic reflections on the glass, soft shadows, premium food photography, natural colors, high detail, realistic textures, 4K, editorial meal-prep aesthetic.

On the right side, include a neat handwritten-style ingredient list reading:
“Shredded Chicken
Romaine
Cojita
Black beans
Corn
Red pepper
Red onion
Cherry tomatoes
Cucumber”

Vertical composition, realistic proportions, clean and appetizing presentation, professional commercial food photography.
```

**点评**：要求"从下到上逐层可见且颜色分明"（黄瓜丁→…→鸡肉丝）并把右侧手写体配料表逐行写死——食物摄影"层次可读性 + 图内文字"双难点的组合解法。
**来源**：awesome-gpt-image-2 · R100

### 【超市抓拍 UGC 带货图】
适用：场景化电商、买家秀/门店社媒风格、反棚拍真实感

```text
Create a realistic vertical smartphone photo of a candid grocery-store shopping moment in a Korean supermarket. A young woman with {argument name="hair color" default="dark brown shoulder-length hair"} is crouching low beside the cereal and granola aisle, wearing a {argument name="hat color" default="red"} baseball cap pulled low over her face, a slightly loose white ribbed long-sleeve henley top, light blue wide-leg jeans, white sneakers with beige soles, and a slim black shoulder bag. She is turned in side profile looking to the right, with her left arm extended toward a black plastic shopping basket on the floor; the basket contains visible groceries and has the white “emart” logo on the side. The scene contains exactly one main shopper, one black basket, two background shoppers, one shopping cart in the background, one prominent overhead aisle sign with the number 6 and Korean category text, one visible price sign reading “2,980,” and long shelves packed with cereal, granola, snack, and packaged food bags with Korean labels. Use a natural consumer-phone snapshot style, slightly imperfect framing, realistic indoor fluorescent lighting, mild motion softness, neutral colors, glossy gray supermarket floor reflections, deep aisle perspective, and authentic everyday details. Make it look like a casual buyer-show or store social media photo rather than a studio fashion shoot. No glamour lighting, no exaggerated posing, no artificial-looking skin, no extra people, no watermark.
```

**点评**："exactly one main shopper, one black basket, two background shoppers..." 用精确点数锁定画面元素，再要求"手机随手拍的不完美构图、轻微运动模糊、荧光灯"，明确反 glamour 布光——UGC 真实感的完整配方。
**来源**：awesome-gpt-image-2 · R109

### 【护肤晨间托盘·品牌控制】
适用：静物商业图、美妆生活方式场景、无logo品牌感控制

```text
Create a 3:4 vertical beauty lifestyle photograph for a premium skincare morning routine. Scene: a travertine bathroom counter beside a soft frosted window, with a minimal glass serum bottle, ceramic cleanser tube, cream jar, folded linen towel, jade roller, small dish of pearl hair clips, and a single dewy white camellia flower. Lighting: natural morning side light, gentle reflections, realistic glass thickness, soft shadows, clean negative space. Aesthetic: quiet luxury, Japanese minimalism meets modern spa editorial, cream / warm stone / translucent pale green palette. No visible brand logos, no readable fake labels except a tiny generic mark "AM ROUTINE", no human face, no clutter, no overdone CGI shine.
```

**点评**："except a tiny generic mark" 是品牌控制的精妙中间态——既允许有标签细节又杜绝假商标幻觉，产品商拍类可直接套用。
**来源**：GPT-Image2-Skill · No. 154

### 【土耳其烤肉 6 场景商业摄影套图】
适用：多场景电商套图，每场景独立背景色 + Global 全局规则

```text
prompt:

8K UHD hyper-realistic commercial food photography, 3:4 aspect ratio. 6 scenes, each on its own solid or gradient background:

Scene 1, Döner slice explosion: Traditional Turkish döner (beef and lamb mix), paper-thin ribbons spiraling outward mid-air, white garlic sauce and red chili sauce splashing, fresh parsley leaves floating. Deep crimson red background.

Scene 2, Dürüm wrap floating: Premium dürüm cut in half and floating vertically, cross-section revealing döner meat, lettuce, tomatoes, onions layered inside, white garlic yogurt sauce drizzling elegantly, subtle spice particles drifting. Warm terracotta orange background.

Scene 3, Sauce pour drama: Mound of freshly sliced döner with crispy charred edges, thick creamy garlic yogurt sauce pouring from above frozen mid-flow, spicy red chili sauce drizzling alongside in thin crimson streams, sliced tomatoes and parsley below, heat vapor rising. Dark charcoal black background.

Scene 4, Deconstructed composition: Toasted lavash bread pieces, döner slices, tomato slices, lettuce leaves, and onion rings all suspended separately at varying heights, glossy sauce ribbons connecting elements artistically, ultra-fine spice dust in the air. Muted sage green background.

Scene 5, Rotating spit close-up: Extreme close-up of vertical döner tower on spit, large döner knife frozen mid-slice, fresh slice falling away, charred bits and seasoning particles in air, heat vapor rising from the fresh cut. Rich golden amber background.

Scene 6, Overhead plate explosion: Top-down view, all ingredients bursting upward in circular pattern, döner slices, french fries, grilled peppers and tomatoes, fresh parsley, sumac, lemon wedges, sauce droplets spraying, elements at varying heights with some rotating. Deep burgundy red background with vignette.

Global: controlled studio lighting emphasizing meat texture and char marks, shallow to medium depth of field, rich contrast, warm savory tones, natural shine, appetizing color grading. No text, logos, people, hands, cartoon style, or plastic-looking food.
```

**点评**："多场景 + 每场景独立背景色 + Global 全局规则"的套图模板，六种食物动感逐一编号，结尾负面清单干净利落——一次生成整套电商视觉。
**来源**：awesome-gpt-image-2-API-and-Prompts · Case 4 · @iamaiistudio

## 避坑清单（组装该类 prompt 时逐条对照）

1. **材质+光影是灵魂**："商品图一旦没有光影，立刻变成地摊货"——布光类型、高光落点、阴影软硬必须写明。（freestylefly 避坑指南电商）
2. **用材质物理行为代替质量形容词**：折射、焦散、水珠、高光畸变、自然反射，比堆 "8K / masterpiece / ultra" 更出高级感。（awesome-gpt-image-2 R99 点评）
3. **品牌只做点缀**：细线、强调色、字体气质即可，"不要把 logo 或大色块铺满画面"；需要标签细节时用 `except a tiny generic mark` 中间态，防模型发明假商标。（freestylefly 避坑指南电商 + GPT-Image2-Skill No. 154 点评）
4. **该清晰的必须清晰**：电商图商标与关键文字写明 `Logo fully sharp, legible, and centered`——模糊 logo 直接废图。（ai-image-prompts-skill ⑰ 点评）
5. **促销文案只给 1-2 句，先分析再出图**：让模型自行脑补卖点文案必然翻车；复杂需求先让它做产品分析/设定，再进入画面描述。（freestylefly 避坑指南电商）
6. **食物锁"层次可读性"**：透明容器逐层点名食材（从下到上）并要求颜色分明；液体/酱料写清来源方向与几何形状（对称冠状液花、垂直淋落），防物理翻车。（awesome-gpt-image-2 R100 点评 + ai-image-prompts ⑰ 点评）
7. **图中标注/callout 用结构化列表**：成分标注类主图给 labels 数组，逐条写 text + position + visual_aid，别用散文描述标注位置。（awesome-gpt-image-2-API-and-Prompts Case 14）
8. **UGC 场景图反 glamour**：精确点数锁元素（exactly one basket / two shoppers）+ 手机随手拍的不完美构图、荧光灯、轻微运动模糊，明确写 no glamour lighting / no studio fashion shoot。（awesome-gpt-image-2 R109 点评）
