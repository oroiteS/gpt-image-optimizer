# 角色与一致性

> 覆盖角色设定图（多视角/三视图/表情锚点）、表情包贴纸、IP 手办化、Emoji 物化、角色卡片与多人合影一致性。写作前先读 2-3 条最相关样例，套用其结构而非照抄内容。

tags: 角色设定图, 三视图, 表情包贴纸, IP手办化, 角色卡片, 角色一致性

## 样例

### 【专业角色设定图（档案+五向转面+表情锚点）】
适用：要一张完整角色设定表：多视角转面、表情集、服装材质拆解、技术注释

```text
Create a highly detailed, professional character design sheet for an anime-style female warrior named {argument name="character name" default="RU RIO"}. The layout should be organized into distinct sections on a dark background with gold and white text.

**Top Left (Profile):** A header titled "CHARACTER PROFILE" featuring a winged emblem. Below it, the name "RU RIO" in large serif font, subtitle "SWORD QUEEN". Include a data list: AGE (22), HEIGHT (172cm), OCCUPATION (Sword Queen), AFFILIATION (The Royal Court of Elysion), TITLE (Heir to the Radiant Throne), ELEMENT (Light), WEAPON (Regal Longsword "Lumina Regalia"). Add a "PERSONALITY" section describing her as calm and unwavering, and a "LIKES/DISLIKES" section. End with a quote: "A queen's blade shall never waver."

**Top Center (Main Art):** A large, high-quality bust portrait of the character looking slightly upward. She has short black hair, grey eyes, and wears intricate silver plate armor with gold filigree and a high collar.

**Top Right (Turnaround & Analysis):** A section labeled "ORTHOGRAPHIC TURNAROUND" showing five full-body views of the character standing straight: FRONT, 3/4 FRONT, SIDE, 3/4 BACK, and BACK. To the right of this is a "PROPORTIONAL ANALYSIS" diagram showing the front view with horizontal grid lines marking head-to-foot ratios (Head x 1, Head to Chin, etc.).

**Middle Band (Expressions):** A row labeled "EXPRESSION ANCHORS" containing eight square panels showing close-ups of the character's face with different emotions: NEUTRAL, CALM, DETERMINED, PROUD, SOFT SMILE, SWEET SMILE, CONCERN/HANDLING, and BATTLE CRY.

**Bottom Left (Wardrobe):** A section titled "WARDROBE & ACCESSORIES BREAKDOWN". It displays the full outfit on a mannequin, followed by isolated items labeled: CLOAK, TORSO ARMOR, GAUNTLETS, LEG ARMOR, BOOTS, and various small accessories like belts and jewelry.

**Bottom Center (Materials & Details):** Two rows. The top row is "MATERIAL PALETTE" showing swatches for SILVER STEEL, MIDNIGHT SATIN, STARCHED TOP, ROYAL LEATHER, and GILDED TRIM. The bottom row is "DETAIL CLOSE-UPS" showing macro shots of SHOULDER PAULDRON, CHEST ORNAMENT, THIGH STRAP & CHAIN, THIGH HARP & CHAIN, and SWORD HILT DETAIL.

**Bottom Right (Technical):** A column with "TECHNICAL NOTES" listing bullet points about the silhouette and fabrics. Below that, a "COLOR SCHEME" strip with diamond-shaped color swatches. Finally, a "RIG & MOVEMENT REFERENCE" section showing three small wireframe/skeleton diagrams of the character.
```

**点评**：按档案数据/主立绘/五向正交转面+头身比网格/8 格表情锚点/衣柜拆解/材质色板/技术注释分区，等于把画师交稿规范直接翻译成 prompt。
**来源**：awesome-gpt-image-2 · R39（Raycast 参数化）

### 【三分区角色设定集（Hero+转面+细节）】
适用：只给一段角色描述，要一张排版干净的概念展示板，细节允许模型自动补全

```text
Create a high-end, asymmetric editorial CHARACTER CONCEPT SHOWCASE from these inputs:

[STYLE]: stylized 3D stop-motion claymation style with rich tactile textures of clay, felt, and leather, and warm cinematic studio lighting
[SUBJECT_DESCRIPTION]: A charming and slightly eccentric traveling medieval alchemist and cartographer. He wears a heavy, oversized patched wool coat over a worn leather tunic, multiple small glowing potion vials and rolled-up parchment scrolls strapped to his utility belt, a wide-brimmed traveler's hat, and thick round brass spectacles. He has a messy, hand-sculpted ginger beard, warm curious eyes, and a friendly smile. He carries an ancient, brass-trimmed leather satchel. His design features exaggerated, whimsical proportions and a cozy, rustic medieval aesthetic.

Create the layout in a clean 16:9 widescreen format on a neutral studio gray or warm off-white background with a minimal technical border. The design must look like a premium production visual bible, using clean typography, no clutter, no watermarks, and no logos. Apply [STYLE] only to the character and visual elements, keeping the presentation layout clean, structured, and minimal.

Infer all missing details from the subject description, including name, role, brief background specs, and a cohesive color palette.

Use this tri-fold layout:

1. HERO SPOTLIGHT (Left 40% of the board)
- Show one large, highly detailed full-body dynamic action pose of the subject.
- This pose should showcase the character's primary personality, attitude, and silhouette.

2. TECHNICAL TURNAROUND (Center 35% of the board)
- Show exactly two clean full-body views: Front View and Back View.
- The subject should be in a relaxed, neutral stance.
- Place these views over very subtle vertical and horizontal grid lines resembling a technical schematic blueprint.

3. KEY DETAILS (Right 25% of the board)
- EXPRESSION TRIO: Exactly 3 large, highly expressive close-up headshots showing core emotional states: Calm/Neutral, Highly Focused/Intense, and a Dynamic/Expressive emotion (like a smirk or fierce grin).
- GEAR CALLOUTS: Exactly 2 clean, isolated close-up panels showing primary wardrobe textures, signature accessories, or weapons/gear.

4. SPECS & COLOR BANNER (Bottom Edge)
- A minimalist, horizontal typography block listing Name, Role, Age, and Core Theme.
- Adjacent to the text, display 5 to 6 clean geometric color swatches showing the character's primary color palette with no labels.

Ensure complete character and costume consistency across all sections. The Hero Spotlight must visually anchor the sheet, offering a clean, open, and professional layout that avoids dense, repetitive, or cluttered grids.
```

**点评**：[STYLE]/[SUBJECT] 输入区 + 40/35/25 三分区版面 + 底部色板条，"Infer all missing details" 把名字、职业、色板都授权给模型补全。
**来源**：awesome-gpt-image-2-API-and-Prompts · Case 375 · @itsPixieVerse

### 【多人合影一致性（参考图计数防串脸）】
适用：上传多张角色参考图合成一张合影，最怕串脸、复制粘贴、人数对不上

```text
Prompt of the Day: 40K POWER ARMOUR SQUAD ⚔️🛡️💜💚

Today’s Prompt of the Day turns your characters into a 40K-inspired warriors. Yes this was done before but i wanted to see how much better GPT 2 can do it now

Use one character reference for a solo warrior, or attach multiple character references to create a full squad. The prompt is built to count every reference image and turn each one into a separate visible character, with no helmets covering their faces.

Type your chosen scene into the SCENE SELECTOR at the top, then attach your character reference image or images.

Try scenes like:

a brutal battlefield charge
a gothic starship boarding action
a candlelit shrine world cathedral
an industrial forge world
a grim underhive alley
a quiet off-duty barracks scene
a solemn prayer before battle

Have fun with this one ⚔️🛡️

............................PROMPT STARTS HERE............................

SCENE SELECTOR:
[Type the 40K-inspired scene you want here.]
Examples:

brutal battlefield charge through smoke, fire, shell craters, and ruined gothic architecture

boarding action inside a colossal warship corridor
cathedral-like shrine world interior filled with candles, banners, stained glass, and incense haze
industrial forge world with sparks, chains, molten metal, pipes, and huge machinery
command deck before battle with tactical holograms and vast void windows
grim underhive alleyway with pipes, neon grime, metal walkways, and urban decay
heroic last stand surrounded by wreckage, fallen enemies, burning vehicles, and drifting ash
quiet off-duty scene inside a fortress barracks, armoury, workshop, canteen, or hangar
solemn prayer before battle with relics, banners, candles, incense smoke, and sacred war symbols
everyday-life scene in a gothic sci-fi military stronghold, training yard, armoury, repair bay, or mess hall
Use the typed scene selector as the main scene concept.
If no custom scene is typed, choose one of the example scenes that best fits the attached character reference image or images and the overall character vibe.
Adapt the environment, action, pose, props, camera, and mood to match the selected scene.
Keep the final scene clearly inspired by 40K-style grimdark far-future gothic military sci-fi.

STRICT REFERENCE COUNT RULE:
Before creating the image, count the number of attached character reference images.
Create exactly one main character from each attached character reference image.
The number of main characters in the final image must exactly match the number of attached character reference images.
If 1 character reference image is attached, create exactly 1 main character.
If 2 character reference images are attached, create exactly 2 main characters.
If 3 character reference images are attached, create exactly 3 main characters.
If 4 character reference images are attached, create exactly 4 main characters.
If more character reference images are attached, create exactly that same number of main characters.
Each attached character reference image is a separate person.
Each attached character reference image must appear once and only once as their own distinct main character.
Do not treat any attached character reference image as optional.
Do not ignore, drop, replace, combine, or simplify any attached character reference image.

MULTI-CHARACTER IDENTITY RULE:
Use every attached character reference image as its own separate character identity source.
Character 1 must be based only on the first attached character reference image.
Character 2 must be based only on the second attached character reference image.
Character 3 must be based only on the third attached character reference image.
Character 4 must be based only on the fourth attached character reference image.
Continue this pattern for any additional attached character reference images.

Do not use the first attached character reference image to create multiple characters.
Do not duplicate the first character to fill the group.
Do not create variations, twins, clones, alternate outfits, mirrored copies, recolours, or slightly edited versions of the same character.
Do not merge two or more attached character references into one design.
Do not let one character’s face, hairstyle, colours, outfit motifs, body type, species traits, or accessories replace another character’s identity.
SINGLE-CHARACTER FALLBACK RULE:
If only one character reference image is attached, create one main character only.
Do not create a squad, clone group, twin, alternate version, second warrior, companion, or duplicate of the character.
The single character should remain the only main subject.

THREE-CHARACTER PRIORITY RULE:
If three character reference images are attached, this is a three-character squad image.
All three referenced characters must appear together in the same scene.
All three faces must be visible.
All three armour designs must be distinct.
All three characters must be clearly separated in the composition.
Use a readable left-center-right squad arrangement unless the selected scene needs another clear formation.
CHARACTER REFERENCE RULES:
Preserve each attached character’s face shape, hairstyle, hair colour, eye colour, expression, body language, signature colour palette, outfit motifs, accessories, silhouette, species traits, proportions, and overall character vibe.
The final image must clearly show every attached character as a separate, recognizable individual.
Every character must still clearly look like their own attached reference image.

Keep each character’s head uncovered with no helmet, full face mask, or visor covering the face.
The face, hair, and identity of every referenced character must remain clearly visible.
Hard style rule:
Use the attached character reference image or images as the visual style reference for the final image.
Preserve the visual art style, rendering language, line quality, colour handling, facial stylization, shading style, texture treatment, background treatment, and overall stylization of the attached reference image or images while transforming the character or characters into 40K-inspired power-armoured warriors.
If the references are anime, keep them anime. If they are stylized, keep that stylization.
Do not turn the final image photorealistic unless specifically requested.
Scene concept:
Create a 16:9 horizontal widescreen cinematic illustration based on the scene written in the SCENE SELECTOR.
Show the attached character or characters transformed into custom 40K-inspired grimdark far-future power-armoured warriors.
The image should feel heavy, dramatic, mythic, warlike, and character-driven, with strong atmosphere, clear storytelling, and a powerful sense of scale.

Character transformation:
Transform every attached reference character into a custom 40K-inspired power-armoured version of themselves while preserving their original identity.
The redesign should center on massive stylized power armour with broad shoulder plates, reinforced chest armour, heavy gauntlets, armoured boots, thick mechanical joints, gothic sci-fi military detailing, sacred-warrior ornamentation, battlefield wear, and an oversized futuristic weapon.
The armour must feel imposing, brutal, ceremonial, expensive, and engineered for endless war.
Keep the head uncovered so each character’s original face, hair, and expression remain visible.
Use each attached character’s colours, motifs, accessories, outfit shapes, symbols, materials, personality, and overall vibe as the foundation for their armour redesign.
The armour should feel like it belongs in a 40K-inspired universe, but it must be custom-built from the attached character’s own identity.
If multiple characters are present, each one must have a distinct armour design based on their own original reference rather than all wearing identical suits.
Armour design:
Give each character huge futuristic power armour inspired by 40K-style grimdark gothic sci-fi warfare.
Include broad pauldrons, a strong chest plate, layered armour segments, mechanical joints, reinforced thighs, heavy boots, thick gauntlets, power cables, vents, seals, relic-like details, engraved plates, purity-scroll-like decorations, battle damage, and character-specific symbols.
Adapt each armour design to that character’s original style, colour palette, outfit motifs, accessories, personality, and silhouette.
Keep the armour stylized to match the attached reference image or images rather than realistic.

Weapon design:
Give each character a fitting oversized futuristic weapon inspired by 40K-style grimdark sci-fi warfare.
The weapon can be a heavy explosive sci-fi rifle, massive energy weapon, brutal motorized serrated melee weapon, glowing power blade, ceremonial war hammer, plasma-like cannon, heavy pistol, or other far-future battlefield weapon appropriate to their vibe and role.
Each character’s weapon should be different and should match that character’s identity, armour design, and role in the scene.
If the selected scene is calm, ceremonial, or off-duty, the weapon may be held at rest, slung, holstered, leaned nearby, placed on a table, or carried ceremonially, but it should still be visible.
If the selected scene is battle-heavy, make each weapon active, weighty, readable, and integrated into the pose.
Scene adaptation rules:
If the selected scene is battle-heavy, make the action dynamic but readable, with strong poses, clear silhouettes, environmental destruction, smoke, fire, debris, and a strong sense of momentum.
If the selected scene is solemn, sacred, or ceremonial, focus on mood, scale, banners, relics, candles, incense, stained glass, and reverent atmosphere.
If the selected scene is indoors, use gothic sci-fi architecture, industrial machinery, cathedral-scale interiors, fortress spaces, armouries, barracks, command rooms, or military infrastructure that fit the selected location.
If the selected scene is everyday-life or off-duty, keep the armour and 40K-inspired universe intact, but show the character or characters in a grounded moment such as maintenance, briefing, prayer, conversation, eating, resting, training, repairing gear, or preparing equipment.
If multiple characters are present, make their interaction clear and readable, with each one contributing to the scene rather than standing as vague duplicates.
Environment and composition:
Build the environment around the selected scene.
The setting should feel like the kind of place the character or characters naturally belong in once translated into a 40K-inspired grimdark far-future war universe.
Use a wide 16:9 horizontal cinematic composition.
Keep the main subject or subjects clearly visible, central or compositionally dominant, and easy to read at a glance.
If one character is present, give them a strong hero composition with a clear silhouette and dominant visual presence.
If multiple characters are present, arrange them so every character remains readable and identifiable with clean silhouette separation.
For three attached references, use a clear three-person squad composition with all three faces visible.
Use background architecture, smoke, debris, banners, machinery, sparks, haze, relics, gothic shapes, or cathedral-like scale to support the scene without overpowering the characters.
Lighting and mood:
Use lighting that matches the selected scene.
The image should feel grim, cinematic, epic, and immersive, with dramatic contrast and strong atmosphere.
Use battlefield firelight, smoky haze, stained-glass glow, cold ship lighting, industrial sparks, moody rim light, incense haze, harsh military illumination, glowing machinery, or distant explosions where appropriate.
The mood should feel powerful, warlike, sacred, brutal, and character-specific while still reflecting each original character’s personality.
Quality and rendering:
Polished, premium-quality stylized illustration with clean linework, crisp rendering, readable forms, powerful armour design, expressive visible faces, strong weapon design, and clear composition.
Keep the strongest detail concentrated on the referenced character or characters, their armour, their faces, and their weapons.
Maintain strong visual hierarchy and readability.
The background should support the characters rather than becoming busier than them.

Do not:
Do not ignore the SCENE SELECTOR.
Do not create more or fewer main characters than the number of attached character reference images.
Do not create only two characters if three character reference images are attached.
Do not duplicate the first attached character instead of using the second or third reference.

Do not merge multiple attached references into fewer characters.
Do not make any referenced character a clone, twin, recolour, armour variant, or alternate version of another referenced character.
Do not hide, crop, mask, or cover any referenced character’s face.
Do not make every character wear the same identical armour if multiple references are provided.

Do not make the weapon tiny, modern, toy-like, or visually unimportant.
Do not make the background busier than the characters.
Do not make the main subjects blurry, tiny, hidden, or unreadable.
Do not create messy anatomy, extra limbs, malformed hands, distorted faces, or muddy textures.
Do not use photorealism unless specifically requested.

..............................END OF PROMPT..................................
#POTD #promptoftheday #AI #AiArt #Art #AnimeArt #40K #Grimdark #PowerArmour #SciFi #CharacterDesign #DigitalArt #AnimeStyle #CommunityPrompt
```

**点评**：全库最复杂的多人一致性系统：引用图计数规则、Character N 一一对应、单人 fallback、SCENE SELECTOR 场景选择器，多人合照防串脸的终极范本。
**来源**：awesome-gpt-image-2-API-and-Prompts · Case 367 · @EvaGlitchAI

### 【表情包贴纸（编号枚举姿势）】
适用：以上传形象为主角做一套 chibi 表情包/贴纸，每个姿势不同

```text
创作一套全新的 chibi sticker，共六个独特姿势，以用户形象为主角：
1. 双手比出剪刀手，俏皮地眨眼；
2. 泪眼汪汪、嘴唇微微颤动，呈现可爱哭泣的表情；
3. 张开双臂，做出热情的大大拥抱姿势；
4. 侧卧入睡，靠着迷你枕头，带着甜甜的微笑；
5. 自信满满地向前方伸手指，周围点缀闪亮特效；
6. 手势飞吻，周围飘散出爱心表情。
保留 chibi 美学风格：夸张有神的大眼睛、柔和的面部线条、活泼俏皮的短款黑色发型、配以大胆领口设计的白色服饰，背景使用充满活力的红色，并搭配星星或彩色纸屑元素进行装饰。周边适当留白。
Aspect ratio: 9:16
```

**点评**：编号枚举 6 个姿势 + 统一风格描述收尾，是多格/成套生成的标准结构；"以用户形象为主角"配合上传头像即得个性化结果。
**来源**：awesome-gpt4o-images · 案例 27 · @dotey

### 【IP 手办化（包装盒公式）】
适用：把照片人物变成 Funko Pop / 盲盒 / 收藏玩具包装盒

```text
把照片中的人物变成 Funko Pop 公仔包装盒的风格，以等距视角（isometric）呈现，并在包装盒上标注标题为"JAMES BOND"。包装盒内展示的是照片中人物形象，旁边搭配有人物的必备物品（手枪、手表、西装、其他）同时，在包装盒旁边还应呈现该公仔本体的实物效果，采用逼真的、具有真实感的渲染风格。
```

**点评**：盒子（等距视角）+ 盒内公仔 + 必备配件 + 盒旁本体实物，四层构图一次说清，"IP 化人像"的通用公式。
**来源**：awesome-gpt4o-images · 案例 24 · @dotey

### 【参考图转 3D 收藏玩具（身份保持前置）】
适用：照片转潮玩/手办渲染图，要求保脸保识别点、玩具质感

```text
将输入照片转换为高端 3D 收藏玩具形象。
身份保持：保留原始人物/角色的脸部身份、主要发型、表情气质和服装识别点。
造型比例：大头设计，五官轻微夸张，身体比例玩具化，但整体仍保持高级设计感。
材质：哑光 vinyl / resin / collectible figure finish，皮肤和服饰材质要有细节。
灯光与背景：柔和棚拍光，干净背景，[黑色/白色/品牌色]，主体居中，轮廓清晰。
质感：超清锐度，真实材质反射，8K render，premium designer toy aesthetic。
约束：不要改变身份，不要廉价塑料感，不要多角色，不要复杂背景，不要文字水印。
输出：一张完整的高端收藏玩具渲染图。
```

**点评**："身份保持"放在第一行——图生图任务的黄金法则：先声明必须保留什么，再声明要改变什么。
**来源**：freestylefly-awesome-gpt-image-2 · 模板层 tpl-character（No. 96)

### 【角色卡片（RPG 收藏卡）】
适用：职业卡/属性卡/收藏卡，带技能条、名牌、包装盒质感边框

```text
创建一张 RPG 收藏风格的数字角色卡。
角色设定为 {Programmer}，自信地站立，配有与其职业相关的工具或符号。
以 3D 卡通风格呈现，采用柔和光照，展现鲜明的个性。
添加技能条或属性数值，例如 [技能1 +x]、[技能2 +x]，如 Creativity +10、UI/UX +8。
卡片顶部添加标题横幅，底部放置角色名牌。
卡片边框应干净利落，如同真实的收藏公仔包装盒。
背景需与职业主题相匹配。
配色方面使用温暖的高光与符合职业特征的色调。
```

**点评**：逐行短句指令（每行一个要素）的版式控制法，比大段落更不易漏元素，适合卡片类需求。
**来源**：awesome-gpt4o-images · 案例 44 · @berryxia_ai

### 【Emoji 物化（极短模板）】
适用：把 emoji 变成雪糕/玩偶/靠垫等 3D 实体，纯色背景

```text
生成图片：将【🍓】变成变成一根奶油雪糕，奶油在雪糕顶上呈曲线流动状看起来美味可口，45度悬浮在空中，q版 3d 可爱风格，一致色系的纯色背景
```

**点评**：60 字完成一个完整出图——模型对"中文口语 + emoji 变量"响应极好，是最低成本的物化模板骨架。
**来源**：awesome-gpt4o-images · 案例 63 · @ZHO_ZHO_ZHO

## 避坑清单（组装该类 prompt 时逐条对照）

1. 拆解五官，不要只写"很美的女孩"：拆到"桃花眼、高鼻梁、野生眉"级别的具体特征，并写清服装材质。
2. 一致性约束前置：角色一致性/身份保持写在动作与内容列表之前——动作序列越长越容易换脸换衣服。
3. 多格先锁网格再填内容：面板数、编号、每格内部结构（标题/姿态/说明/箭头）先写死。
4. 表情包防翻车三件套：每个形象完整无残缺、画面无多余分离元素、严格禁止出现文字或确保文字准确（优先选择无文字）。
5. 玩具化必须保留身份锚点：脸部身份、主要发型、表情气质、服装识别点要点名保留，同时禁"廉价塑料感"。
6. 参考图是唯一事实来源：写明 "The reference image is the absolute and sole source of truth — do not rely on any prior knowledge"，防止模型用训练知识"修正"参考图长相。
7. 多人合照防串脸：人数=参考图张数、Character N 一一对应、禁止克隆/双胞胎/换色变体/多图合并成一角色。
8. 反 AI 感负面词挂载：plastic skin、多余手指、畸形手、过度磨皮。
