# 生图 Prompt 写作工艺（Craft）

跨类别核心写作原则，从 6 个开源库共 5 万+ 社区案例中蒸馏。写任何 prompt 前过一遍结构篇；遇到具体缺口（文字、负面、图生图、结构化）再查对应章节。类别专属样例见同目录 `gallery-*.md`。

## 目录

**A. 结构篇**
1. 万能骨架：九层组装公式
2. 画布、比例、版式先行
3. 四种 prompt 形态，按需求选
4. 类别迷你公式速查

**B. 细节篇**
5. 场景密度胜过形容词
6. 材质、光线、色板是三个独立旋钮
7. 媒介出身决定真实感（含摄影词表）
8. 风格锚点四类锚法
9. 物理正确性专项
10. 构图与镜头语言词表

**C. 文字篇**
11. 图中文字四件套
12. 文字排版语法
13. 密集中文排版额外约束

**D. 约束篇**
14. 负面约束：三分类 + 点名坏习惯
15. 防漂移三板斧
16. 身份锁三段式（图生图）
17. 反完美、反美化美学

**E. 编辑篇**
18. 改图不变量
19. 多参考图三件套

**F. 智能篇**
20. INTELLIGENCE RULE：让模型自己推断
21. 默认值推断：先填后告知
22. 商业层级与三眼测试

---

## A. 结构篇

### 1. 万能骨架：九层组装公式

几乎所有高质量 prompt 都可拆成 9 层，顺序高度一致。写 prompt 时逐层检查，缺哪层补哪层：

```text
任务动词/定性句   一张……照片 / 设计一张……海报 / 将……转换成……（动词决定任务类型）
画布与比例       3:4 竖版 / 16:9 横版 / 1:1 方图
主体与身份       谁/什么：年龄、发型发色、五官、肤质、体型、材质、颜色
服装/配饰/细节   逐件列举，精确到耳饰、图案、缝线
姿态与动作       重心、手位、视线方向、表情（枚举展开："喜悦、惊讶、平静"）
环境与背景       从左到右点名场景元素；背景层次与主体的空间关系
光影            主光方向 + 硬软 + 色温（golden hour / 顶部柔光箱 / 冷蓝灰暮色）
构图与镜头       景别 + 机位 + 焦段（85mm）+ 光圈（f/1.8）+ 焦点落点
风格锚 + 质量词 + 文字 + 负面约束（收尾三件套：比例、渲染词、氛围句）
```

短 prompt 是这条骨架的截断版；密级文字越多、结构越复杂，越要把每层写全。锚点信息（主体特征、独特构图）放在 prompt 前 1/3，权重最高。

### 2. 画布、比例、版式先行

最强的 prompt 先分配空间，再描述表面细节。结构重要时先说结构，否则模型把细节预算花在物体上、版式全靠即兴。

常用开头句式：
- `横版 16:9 学术概念图…`
- `设计一张 3:4 竖版海报…`
- `一张正方形 3×3 网格图…`
- `6 格电影分镜，3×2 排布…`
- `主体占画面约 60%，上下各留 20% 负空间…`（比例数值化）

画幅与用途对照：方图 1:1＝头像/图标；竖版 3:4 / 1024×1536＝海报/封面/菜单；横版 16:9 / 1536×1024＝场景/游戏截图/视频封面；9:16＝手机壁纸/短视频/故事条幅。

### 3. 四种 prompt 形态，按需求选

| 形态 | 样子 | 适用 |
|---|---|---|
| **自然语言叙事段** | 一段或数段流畅散文，从头到脚、从主体到环境顺描写 | 人像、场景、创意概念（默认形态） |
| **CAPS 小节式** | `CONCEPT / LIGHTING / OUTFIT / CAMERA / MOOD / NEGATIVE` 全大写小节名 + 空行分段 | 电影感人像、多系统复杂场景 |
| **JSON / 结构树式** | `{ "style": …, "layout": …, "labels": […] }`，键表达版面层级 | 海报、信息图、UI 等版式化产物 |
| **日式八段卡** | `Subject / Main Subject / Expression / Pose / Light / Composition / Texture / Negative` 每段 2-4 句 | 角色设定、需要教学式补全的场合 |

规则：任何格式都可，**一致性更重要**；同一需求内不要混用两种结构。长 prompt 可附一句"Short version"压缩版备用。JSON 不必机器可解析，但保持干净可读；比例和输出情绪也要写进 schema。

### 4. 类别迷你公式速查

- **动漫/漫画**：风格锚点 + 原创角色 + 动作/姿态 + 环境 + 色板 + 勾线/赛璐璐方向 + 安全/IP 边界
- **游戏**：游戏镜头语境 + HUD 元素 + 可玩场景细节 + 截图/显示器真实感
- **摄影**：捕捉设备 + 时间地点 + 平凡的不完美 + 真实道具
- **人像**：身份细节（五官/肤质）+ 服装逐件 + 姿态 + 光向 + 镜头焦段 + 身份锁（图生图）
- **产品/美食**：JSON 配置式（环境/主体/材质/运动系统/输出）+ 悬浮或飞溅动态 + 棚拍灯光
- **海报**：画布比例 → 商业层级（名称>标语>SKU>价格>CTA>小字）→ Exact readable text → 负面防错
- **品牌系统**：logo/字标 + 色板 + 字体系统 + 包装/社媒/触点同板展示 + 虚构品牌名
- **信息图**：版式契约（固定分区）+ 编号标注 + 精确数量 + 图例 + 风格边界（像什么/不像什么）
- **UI**：虚构产品名 + 像素画布 + 信息架构 + 真实文案数据 + production-quality mockup
- **建筑/室内**：房间类型 + 相机/镜头 + 材质 + 光向 + 负空间 + 真实阴影
- **技术插画**：爆炸/剖切结构 + 有序部件 + 编号标注 + 材质 + 蓝图/图版风格
- **纹身**：可刺部位 + 线条/阴影/色彩传统 + 负空间留白 + flash 稿呈现 + 非真人皮肤

## B. 细节篇

### 5. 场景密度胜过形容词

- 模糊：`一家夜晚的便利店`。
- 有力：冰柜贴纸、促销海报、垃圾桶、门口地垫、玻璃反光、共享单车、水珠、手机屏光、湿漉漉的沥青路。

经验值：场景给 **5–12 个具体名词** + **2–4 条材质/光线约束**。禁止堆 `精美`、`专业`、`高质量` 这类没有视觉锚点的空形容词。照片级写实直接写 `photorealistic`，只在必要时加针对性质量线索（胶片颗粒/笔触/微距）。

### 6. 材质、光线、色板是三个独立旋钮

不要压成一个"高级感"。拆开写：
- **材质**：拉丝钢、黄铜、洞石、亚麻、玻璃厚度、冷凝水珠、宣纸、羊毛毡、黏土。
- **光线**：柔光箱、轮廓光、清晨侧光、霓虹反射、暖铜高光、冷蓝灰暮色、体积雾。
- **色板**：低饱和青/锈/骨白；奶油/暖石/淡绿；直接给 HEX 值（#1A1A2E、#E94560）更可控。

对产品渲染、室内、建筑、美妆、技术拆解图尤其重要。中文 prompt 可中英混排：中文负责氛围，英文术语负责精度（c4d、isometric、PBR、Octane、8k）。

### 7. 媒介出身决定真实感

写实照片类要说明"这张图是怎么被拍到的"，而不是只说"逼真"：

| 短语 | 效果 |
|---|---|
| `RAW 直出、未经处理、完整 iPhone 画质` | 削弱 AI 精修感，增加随意真实 |
| `业余 iPhone 照片` | 游客/围观者视角 |
| `从远处人群中拍摄` | 真实现场感 |
| `28mm 镜头视角平视` | 建筑真实感 |
| `低角度仰拍四分之三` | 产品/汽车英雄构图 |
| `清晨自然侧光` | 美妆/生活柔感 |
| `轻微运动模糊 / 闪光灯轻微过曝` | 抓拍动感 |

摄影器材锚定（更高级）：`Shot on Hasselblad`、`85mm f/1.4`、`35mm anamorphic`、`Fujifilm Pro 400H 胶片`、ARRI Alexa——真实器材词汇诱导物理正确的成像。一次只选一个主导拍摄框架，相机参数堆太多会互相冲突。

### 8. 风格锚点四类锚法

1. **具名流派/厂牌**：`MAPPA 风格数字 2D 动画`、`NeurIPS camera-ready`（注意 IP 风险，商用改用形制描述：`手绘水彩动画风`替代`吉卜力风`）。
2. **文化跨界混搭**：`浮世绘 × 希腊神话`、`北欧民俗 × 日式绘本`、`瑞士网格 × Risograph 社区海报`。
3. **材质工艺**：needle-felt 羊毛毡、paper-cut 纸雕、plasticine 黏土、工笔+写意水墨混搭。
4. **导演/调色板**：`Christopher Nolan meets Denis Villeneuve`、`配色：#0F3460 / #E94560 / #EAEAEA`。

### 9. 物理正确性专项

AI 常见物理穿帮，逐一设防（写进正面或负面均可）：
- 投影要贴合面部轮廓并软焦衰减（不要悬空硬影）。
- 布料有重力褶皱，垂坠方向合理。
- 飞溅液体有来源方向，液滴大小近大远小。
- 白色描边是"纸层质感"不是"发光"。
- 多人图：人数写死（`恰好三人`），肢体互不融合，每人在做什么逐个说清。
- 文字物理交互（高级）：文字被磨砂玻璃遮挡产生高斯模糊、文字由酱汁"流出"而成、字母与图形融合——让文字参与场景而非浮在上面。

### 10. 构图与镜头语言词表

- 质量：photorealistic / ultra-detailed / 8K / HDR / subtle film grain / cinematic color grading / editorial finish
- 镜头：85mm 人像 / 35mm 环境 / f/1.4–f/2.8 / shallow depth of field / creamy bokeh / overhead flat lay / eye-level / first-person POV
- 光影：golden hour / soft diffused daylight / chiaroscuro / rim lighting / volumetric fog / warm amber glow
- 皮肤与真实感：realistic skin texture with visible pores / natural facial features / subtle imperfections

## C. 文字篇

### 11. 图中文字四件套

1. **逐条引号**：每一段要显示的文字用直引号包裹、逐字给出，用 `/` 或版位标签分隔：`"山川茶事" / "冷泡系列" / "中杯 16 元"`。多段文字拆全：标题、副标题、模块标签、图例、数字、小字。
2. **`Exact readable text:` 前缀**：全部文字都关键时用此句式起头，并声明 `Do not invent dates, logos, claims`（不得发明未给出的内容）。
3. **信息密度配额**：中文信息图限定"只准 N 个模块、每模块 2–4 条短句、禁止段落块"，防止文字失控。
4. **乱码定向 avoid**：`文字清晰工整、无乱码、无错别字、不混入英文或拼音（除非要求）`；装饰性文字明说 decorative，必须可读则加 `crisp, legible, large enough`。

文案保底策略：能不要文字就不要文字；用户给的文案逐字保留，用户没给的由你设计并全文写出——绝不留"此处写标题"这类占位符。

### 12. 文字排版语法

- **位置 + 字体 + 参数三要素**：`顶部中央大号粗体衬线"立夏"`、`左下角手写体小字`、`vertical Japanese calligraphy`。
- **字号层级规则化**：标题是普通文字的至少 2 倍；文字大小按重要度分级；价格以细小字体呈现。
- **描边与排版**：`Text must be bold (white border or black border)`；指定字体家族（Helvetica Light、经典衬线、毛笔草书）而非只说"好看"。
- **主次分明**：hero 文字（品牌名）与 secondary 文字（说明）分开描述；结尾加 `no text, no watermark` 防模型自作主张加字。

### 13. 密集中文排版额外约束

- 需要时注明 `简体中文` 或 `繁体中文`。
- 所有文案逐字给出，禁让模型编内容。
- 规定版式模块与阅读顺序（从上到下、从右到左等）。
- 书法/牌匾注明风格（`毛笔书法`、`匾额体`、`宣纸纹理`）并防假字 clutter。
- 高密度场景声明"只渲染给出的文字，未提供的区域留白"。

## D. 约束篇

### 14. 负面约束：三分类 + 点名坏习惯

**只在模型有明确坏默认时写 avoid，1–3 条短而准；负面过多会反噬 prompt。** 禁止机械套用固定负面词清单——按当前需求从三类中靶向挑选：

1. **媒介错乱**：`no photo elements, no gradients, no 3D`（要扁平插画时）；`避免动漫风、避免现代赛博朋克`（要水墨时）。
2. **文字失败**：`no garbled characters, no fake logos, no watermark, no extra text`。
3. **安全与 IP**：`no real-person likeness`、`no existing copyrighted characters`、成人题材写明 `adult character only, non-explicit`。

**点名模型已知坏习惯**（高频翻车点，比泛泛负面有效）：
- `plastic skin`（塑料皮肤）、`no extra fingers, no distorted face`（解剖错误）。
- `photo-of-a-poster`（把海报拍成带画框/透视/投影的"照片"——要平面设计稿时必须禁）。
- AI 感来源：`no oversaturated base colours, no grainy AI look`。
- `no fake sponsor logos`（活动海报自造赞助商）、`no random fake kanji clutter`（乱造汉字装饰）。

四种写法按需选：句尾禁止串（短 prompt）/ 独立 `Avoid:` 段 / 独立 `NEGATIVE PROMPT:` 段（长 prompt）/ `Do not…` + 自检清单（结构化）。

### 15. 防漂移三板斧

用户要求"和参考图一样/一共 X 个/九宫格"时必须显式上锁：
1. **精确计数**：`exactly 9 panels`、`恰好五道菜品`、`每行恰好六个姿势` + `Do NOT add or remove frames`。
2. **比例数值化**：`occupying about 60 percent of the canvas`、`TOP 50% / BOTTOM 50%`、`主体居中放大，四周大量负空间`。
3. **LOCK 条款族**（长 prompt 专用）：`FORMAT LOCK / IDENTITY LOCK / COUNT LOCK / POSE LOCK`，可加 `NON-NEGOTIABLE`。多面板网格必须写死网格数（`3×3`、`16 格`）+ 每格角色 + 统一美术方向（色板/服装母题/光线/角色身份）。

### 16. 身份锁三段式（图生图）

涉及"保持这个人不变"的需求（换装、换背景、转风格），身份锁写成三段：
1. **正面清单**：逐五官声明 preserve——`保留面部特征、发型、肤色、痣的位置`。
2. **强指令**：`STRICTLY USE the uploaded photo as the only identity reference`、`face 100% unchanged`、`identity lock`。
3. **负面清单**：`no identity drift, no beautify, no face reshaping, no slimming`。

反 AI 网红脸标配：`Do not beautify, alter, reshape`、`natural asymmetry`、`visible pores`、`像真实路人，不能过度精修`。

### 17. 反完美、反美化美学

生活感/胶片感靠禁止"太完美"获得：
- Negative：`no perfect commercial photography, no studio lighting`。
- Positive：`imperfect natural poses`、`printing imperfections`、`analog grain`、`随手抓拍的倾斜构图`。
- 物理损耗叙事：折痕、褪色、划痕制造岁月质感。

## E. 编辑篇

### 18. 改图不变量

编辑图片要外科手术式：说清改什么，更说清什么必须不变。

- 先说目标变换，再保身份/版式/位置/可读性。
- 编辑海报/样机时，除非要求翻译或替换，必须保留原文：`Translate the text… Do not change any other aspect of the image`。
- 黄金句式：`不得改变墙体位置，保持所有线条与平面图一致，但添加家具、饰面、材质与纵深`（一保留一放开）。
- 常用不变量：`保持构图与图像细节一致`、`同一主体，外观与配色完全一致`、`保持原位置`、`只改 X，其余全部不变`。
- 心法：**prompt 里的保留声明是请求不是保真保证**——产出后要目检。

### 19. 多参考图三件套

1. **声明每张图的角色**：`图 1：产品照片`、`图 2：风格参考`、`图 3：logo/包装`；或 `Image 1 = identity source, Image 2 = composition template only`。
2. **Preserve 清单**：脸、发型、构图、相机角度、元素数量——逐项点名保留。
3. **Transform 清单**：目标风格 + 材质工艺 + 互动方式（`把图 2 的风格应用到图 1 的主体上；把图 3 的 logo 放到包装上`）。

两种立场分清：拼贴纪念类**保留原图**（`Keep the original photo realistic, do not over-edit`）；重绘类**原图不得出现**（`The original photograph must NOT appear anywhere in the result`）。多轮迭代时每轮重申不变量。

## F. 智能篇

### 20. INTELLIGENCE RULE：让模型自己推断

当输入信息少而输出系统复杂（品牌系统、角色设定、世界观），在 prompt 里写一段"推断规则"，授权模型先分析再补全：

```text
INTELLIGENCE RULE:
Before designing, analyze the input and infer:
- 3 identity traits (based on analysis)
- COLOR SYSTEM: extract palette automatically, show HEX codes with usage labels
- TYPOGRAPHY: match personality (luxury → elegant serif / tech → geometric sans / street → bold condensed / corporate → clean neutral sans)
```

配套 **DENSITY RULE** 防空洞：`minimum 30–50 elements, mix of macro + micro components, no empty or filler space`。创作类任务可用"留白即授权"句式：`Infer all missing details from the subject description, including name, role, background specs, and a cohesive color palette`。

### 21. 默认值推断：先填后告知

为用户的模糊需求补全细节时，按类别使用默认值推断表（用户没说 → 你填合理默认 → 事后告知可改项）：

| 用户说 | 默认补全 |
|---|---|
| 画个海报 | 竖版 3:4、现代简约风、主标题+副标题+时间地点、高对比色板 |
| 来张头像 | 1:1 方图、浅景深 85mm、柔和自然光、纯色或虚化背景 |
| 做张信息图 | 竖版、顶部大标题、3–6 个编号模块、每模块 2–4 条短句、扁平插画风 |
| 出张产品图 | 2:3 或 1:1、纯色渐变棚拍背景、柔光箱+轮廓光、低角度英雄机位 |
| 画个表情包 | 16 宫格或单枚、厚白边贴纸风、夸张表情（枚举展开）、纯色底、透明背景 |
| 游戏截图 | 16:9、游戏引擎渲染质感、HUD 元素、戏剧性光效 |
| 改个图 | 只改目标元素 + 三件套身份锁 + Preserve/Transform 清单 |

变量槽写法：`[主体]`、`{argument name="产品名" default="示例值"}`——槽位必须带默认值，让 prompt 删槽即成品、填槽即定制。给变量准备 3–4 个示范值（如材质：磨砂玻璃/拉丝金属/软胶/羊毛毡）。

### 22. 商业层级与三眼测试

海报、广告、菜单要规定层级：产品/活动名最大 → 标语 → SKU/模块 → 价格/日期 → CTA → 小字条款；加 `远距离可读`、`清晰的促销层级`。

**三眼测试**（电影海报、城市海报、时尚封面、高端广告）：
- 第一眼：剪影/主题立刻可辨；
- 第二眼：能读懂叙事世界、产品承诺或 campaign 信息；
- 第三眼：细看有材质、小标签、背景细节与回味。

品牌安全三档：`No visible brand logos`（完全无品牌）/ `仅允许 tiny generic mark "示例标"`（可有小通用标）/ 用户提供授权文案。商业案例一律虚构品牌名（如 AURAE、LUMEN BIO）防商标泄漏。
