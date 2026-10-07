# gpt-image-optimizer · 生图 Prompt 优化 Skill

> 用户说 10%，AI 补 90% —— 一个 [Agent Skill](https://agentskills.io) 标准结构的生图提示词优化库。
> 用户随口一句"画个海报 / 来张头像 / 帮我改图"，AI 自动定位类别、参照精选样例、补全全部细节，产出可直接复制到 GPT-Image / Nano Banana / DALL·E 等图像模型的完美 prompt。

从 6 个开源 prompt 库（合计 5 万+ 社区案例）中蒸馏出 **22 节写作工艺 + 13 类 94 条实战样例**，全部样例经脚本逐字节校验收录。

## 安装

### 方式一：skills CLI（推荐，自动识别 Claude Code / Codex / Cursor / Gemini CLI 等）

```bash
npx skills add oroiteS/gpt-image-optimizer
```

pnpm 等价命令（本项目约定使用 pnpm）：

```bash
pnpm dlx skills add oroiteS/gpt-image-optimizer
```

安装到全局（所有项目可用）：

```bash
npx skills add oroiteS/gpt-image-optimizer --global
```

安装到跨工具通用目录 `~/.agents/skills/`（CLI 中该目标名为 `universal`）：

```bash
npx skills add oroiteS/gpt-image-optimizer -g -a universal -y
```

### 方式二：手动安装

```bash
git clone https://github.com/oroiteS/gpt-image-optimizer.git
# Claude Code
mkdir -p ~/.claude/skills && cp -r gpt-image-optimizer ~/.claude/skills/
# 或其他使用 ~/.agents/skills 的 Agent 运行时
mkdir -p ~/.agents/skills && cp -r gpt-image-optimizer ~/.agents/skills/
```

## 使用

安装后，在支持 Agent Skills 的 AI 助手中直接说：

- 「帮我画张咖啡店开业的海报」→ 自动补全比例、版式、文案、色板、光线
- 「来张头像」→ 默认 1:1、85mm 浅景深、柔和自然光
- 「把这张照片变成手办」（附图）→ 自动切入编辑族：身份锁 + Preserve/Transform 双清单
- 「帮我优化这个生图 prompt」→ 走完整六步流水线重构

也可显式调用：「用 gpt-image-optimizer 生成一张……」

### 六步流水线

```
判输入形态（有参考图→编辑族 / 无→文生图）
→ 分类定位（13 类索引 → 读取对应 gallery 样例）
→ 样例参考（套结构，不抄风格词）
→ 细节补全（默认值推断表：先填后告知，不反问）
→ 组装输出（六块结构：主体任务/构图版式/风格材质/文字标签/输出格式/约束负面）
→ 自检（10 项清单逐条核对）
```

## 目录结构

```
（仓库根即 skill 本体）
├── SKILL.md                  # 主控：六步流水线 + 13 类索引 + 输出约定
└── references/
    ├── craft.md              # 22 节跨类别写作工艺（九层骨架、文字四件套、
    │                         #   负面三分类、身份锁、防漂移三板斧、INTELLIGENCE RULE…）
    ├── photography.md        # 摄影与照片级写实（9 样例）
    ├── portrait-avatar.md    # 人像·头像·写真（9）
    ├── product-ecommerce.md  # 产品与电商（9）
    ├── poster-ad-brand.md    # 海报·广告·品牌（9）
    ├── typography.md         # 字体·文字·书法（8）
    ├── ui-social.md          # UI·社交媒体·截图（9）
    ├── infographic-data.md   # 信息图·数据·科研图（8）
    ├── illustration.md       # 插画与艺术风格（5）
    ├── anime-manga.md        # 动漫·漫画·分镜（5）
    ├── gaming-pixel.md       # 游戏与像素（6）
    ├── character.md          # 角色与一致性（8）
    ├── editing.md            # 图像编辑与风格迁移（8）
    └── architecture-space.md # 建筑与空间（5）
```

每个 gallery 文件 = 定位说明 + 检索 tags + 精选样例（prompt 全文 + 一句点评 + 来源）+ 避坑清单。

## 参考仓库

本 skill 的样例与工艺蒸馏自以下开源项目，各文件内均已标注具体来源：

| 仓库 | 许可证 | 主要贡献 |
|---|---|---|
| [jamez-bondos/awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images) | CC BY 4.0 | 中文写法范式、七段骨架、Emoji 变量、负面清单、反 AI 感写法 |
| [YouMind-OpenLab/awesome-gpt-image-2](https://github.com/YouMind-OpenLab/awesome-gpt-image-2) | CC BY 4.0 | 四种 prompt 形态、防漂移三板斧、LOCK 条款族、参数槽 |
| [EvoLinkAI/awesome-gpt-image-2-API-and-Prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts) | CC0 | 参数化模板、INTELLIGENCE RULE、结构化形态谱系 |
| [wuyoscar/gpt_image_2_skill](https://github.com/wuyoscar/gpt_image_2_skill)（GPT-Image2-Skill） | MIT | craft 写作工艺骨架、反向 prompt 输出契约、模板工程规范 |
| [YouMind-OpenLab/ai-image-prompts-skill](https://github.com/YouMind-OpenLab/ai-image-prompts-skill) | MIT | 检索式工作流、默认值推断、身份锁三段式、{argument} 槽位 |
| [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | MIT | 六块组装结构、四级匹配漏斗、13 类避坑指南、变量系统分级 |

感谢以上项目的社区贡献者。样例 prompt 的原始作者信息保留在各 gallery 文件的来源标注中。

## License

[MIT](LICENSE)（本仓库skill 结构与整合文本）。
样例内容遵循各来源仓库的原许可证（见上表），引用时请保留对应署名。
