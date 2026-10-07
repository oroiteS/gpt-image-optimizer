#!/usr/bin/env python3
"""gpt-image-optimizer 深度检索层：搜索 15,210 条社区 prompt 数据。

数据来源：YouMind-OpenLab/ai-image-prompts-skill（MIT），data/prompts/*.json
用法：
  python3 scripts/search_prompts.py search "关键词1 关键词2" [--category poster-flyer] [--limit 8]
  python3 scripts/search_prompts.py view 35920            # 按 id 查看全文
  python3 scripts/search_prompts.py stats                 # 各分类条目统计

规则：
  - search 多关键词为 AND 关系（都命中才算）；大小写不敏感；匹配 title/content/description
  - 输出仅为预览（前 400 字符），确认有用后用 view 取全文
  - 数据含上游已知瑕疵：约 5% 条目尾部截断、literal \n、跨类重复——脚本自动解码并标记疑似截断
"""
import argparse
import glob
import json
import os
import re
import sys

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "prompts")
ALL_CATEGORIES = [
    "app-web-design", "comic-storyboard", "ecommerce-main-image", "game-asset",
    "infographic-edu-visual", "others", "poster-flyer", "product-marketing",
    "profile-avatar", "social-media-post", "youtube-thumbnail",
]

# 中→英术语映射：数据主体为英文 prompt，中文关键词需扩展为英文同义词（任一命中即算）。
# 方法论来源：上游 freestylefly 库 style-library 的中英 keywords 标签表。
ZH2EN = {
    "海报": "poster flyer", "传单": "flyer", "横幅": "banner", "封面": "cover thumbnail",
    "头像": "avatar profile pfp", "证件照": "id photo passport", "写真": "portrait photoshoot",
    "自拍": "selfie", "表情包": "sticker meme emoji", "贴纸": "sticker",
    "产品": "product", "电商": "ecommerce commerce shop", "商品": "product merchandise",
    "包装": "packaging", "广告": "advertising commercial ad", "品牌": "brand identity",
    "logo": "logo wordmark", "菜单": "menu", "名片": "business card",
    "邀请函": "invitation", "简历": "resume cv",
    "信息图": "infographic", "图表": "chart diagram graph", "思维导图": "mindmap",
    "流程图": "flowchart flow diagram", "时间线": "timeline", "地图": "map",
    "插画": "illustration", "水彩": "watercolor", "油画": "oil painting",
    "涂鸦": "graffiti doodle", "刺绣": "embroidery", "剪纸": "paper cut papercraft",
    "像素": "pixel", "等距": "isometric", "微缩": "miniature diorama tilt-shift",
    "黏土": "clay plasticine", "毛毡": "felt wool", "玻璃": "glass",
    "金属": "metal chrome", "霓虹": "neon",
    "动漫": "anime manga", "漫画": "comic manga", "分镜": "storyboard panel",
    "吉卜力": "ghibli", "皮克斯": "pixar", "q版": "chibi", "二次元": "anime",
    "游戏": "game gaming", "游戏资产": "game asset sprite", "精灵表": "sprite sheet",
    "手办": "figurine action-figure collectible funko blind-box", "玩偶": "plush doll stuffed", "宝可梦": "pokemon",
    "界面": "ui mockup app", "网页": "web landing website", "应用": "app mobile",
    "手机": "smartphone iphone mobile", "直播": "live streaming", "弹幕": "danmaku comment",
    "youtube": "youtube", "缩略图": "thumbnail",
    "摄影": "photography photo", "写实": "photorealistic realistic", "电影感": "cinematic film",
    "复古": "retro vintage", "极简": "minimalist minimal", "赛博朋克": "cyberpunk",
    "蒸汽朋克": "steampunk", "波普": "pop art", "超现实": "surreal",
    "人物": "character person portrait", "女孩": "girl woman", "男孩": "boy man",
    "情侣": "couple", "家庭": "family", "猫": "cat", "狗": "dog", "龙": "dragon",
    "美食": "food drink", "咖啡": "coffee", "茶": "tea", "蛋糕": "cake dessert",
    "饮料": "beverage drink soda", "水果": "fruit", "餐厅": "restaurant cafe",
    "建筑": "architecture building", "室内": "interior room", "家具": "furniture",
    "风景": "landscape scenery", "城市": "city urban", "森林": "forest",
    "海洋": "ocean sea", "太空": "space galaxy astronaut", "日落": "sunset",
    "雪": "snow", "雨": "rain", "樱花": "cherry blossom sakura",
    "化妆": "makeup cosmetic beauty", "香水": "perfume fragrance", "手表": "watch",
    "珠宝": "jewelry jewelry", "服装": "fashion outfit clothing", "鞋": "sneaker shoe",
    "婚礼": "wedding", "运动": "sport fitness", "健身": "fitness gym workout",
    "教育": "education learning", "医疗": "medical health", "金融": "finance money",
    "圣诞": "christmas", "节日": "festival holiday", "新年": "new year",
    "图标": "icon", "壁纸": "wallpaper", "专辑": "album cover music",
    "对比": "before after comparison", "翻译": "translate", "上色": "colorize",
}


def is_cjk(s: str) -> bool:
    return any("\u4e00" <= c <= "\u9fff" for c in s)


def expand_keyword(k: str):
    """中文词 → [原词 + 英文同义词]；ASCII 词 → [原词]。返回 (展示词, 匹配词列表)。"""
    k = k.strip().lower()
    if is_cjk(k):
        extra = ZH2EN.get(k, "").split()
        return k, [k] + extra if extra else [k]
    return k, [k]


def decode_content(s: str) -> str:
    """上游部分条目把换行存成字面 \\n，解码以便阅读。"""
    return s.replace("\\n", "\n") if "\\n" in s else s


def looks_truncated(s: str) -> bool:
    """上游 CMS 在 ~3000 字符处硬截断过约 5% 条目：长度接近阈值且结尾异常。"""
    if len(s) < 2500:
        return False
    tail = s.rstrip()
    if tail and tail[-1] in "]})\"'。！？.!?:：":
        # 结尾符号正常但仍可能是 JSON 断在字符串内，再做括号平衡粗查
        pass
    else:
        if len(s) >= 2900:
            return True
    for a, b in (("[", "]"), ("{", "}"), ("(", ")")):
        if s.count(a) > s.count(b) and len(s) >= 2900:
            return True
    return False


def iter_entries(category: str | None):
    cats = [category] if category else ALL_CATEGORIES
    for cat in cats:
        path = os.path.join(DATA_DIR, f"{cat}.json")
        if not os.path.exists(path):
            continue
        try:
            data = json.load(open(path, encoding="utf-8"))
        except Exception as e:
            print(f"⚠️ {cat}.json 解析失败: {e}", file=sys.stderr)
            continue
        items = data if isinstance(data, list) else data.get("prompts", [])
        for it in items:
            if isinstance(it, dict):
                yield cat, it


def preview(s: str, n: int = 400) -> str:
    s = re.sub(r"\n{2,}", "\n", s).strip()
    return s[:n] + ("…" if len(s) > n else "")


def cmd_stats(_args):
    total = 0
    print(f"{'分类':<28}{'条目':>8}")
    for cat in ALL_CATEGORIES:
        n = sum(1 for _ in iter_entries(cat))
        total += n
        print(f"{cat:<28}{n:>8}")
    print(f"{'合计':<28}{total:>8}（跨类重复未去重）")


def cmd_search(args):
    raw_keywords = [k for k in args.query.lower().split() if k]
    if not raw_keywords:
        sys.exit("至少输入一个关键词")
    groups = [expand_keyword(k) for k in raw_keywords]  # [(展示词, [同义词...]), ...] AND 关系
    expanded_note = "；".join(
        f"{show}→{'/'.join(syns[1:]) if len(syns) > 1 else '(原词)'}" for show, syns in groups
    )
    hits = 0
    for cat, it in iter_entries(args.category):
        hay = " ".join(str(it.get(f, "")) for f in ("title", "content", "description")).lower()
        if all(any(syn in hay for syn in syns) for _, syns in groups):
            hits += 1
            if hits > args.limit:
                continue
            content = decode_content(str(it.get("content", "")))
            flag = " ⚠️疑似截断" if looks_truncated(content) else ""
            ref = " 📎需参考图" if it.get("needReferenceImages") else ""
            print(f"[{hits}] ({cat}) id={it.get('id')}  {str(it.get('title', ''))[:60]}{flag}{ref}")
            print(f"    {preview(content)}")
            print()
    if hits == 0:
        print("无命中。建议：换关键词 / 减少关键词数 / 换 --category / 回退 gallery 常规流程。")
    else:
        print(f"检索扩展：{expanded_note}")
        more = f"（共 {hits} 条命中" + (f"，仅显示前 {args.limit} 条" if hits > args.limit else "") + "；看全文：python3 scripts/search_prompts.py view <id>）"
        print(more)


def cmd_view(args):
    for cat, it in iter_entries(None):
        if str(it.get("id")) == str(args.id):
            content = decode_content(str(it.get("content", "")))
            print(f"### {it.get('title', '')}  ({cat} · id={it.get('id')}"
                  f"{' · 📎需参考图' if it.get('needReferenceImages') else ''}"
                  f"{' · ⚠️疑似截断' if looks_truncated(content) else ''})\n")
            print(content)
            return
    sys.exit(f"未找到 id={args.id}")


def main():
    p = argparse.ArgumentParser(description="深度检索 15,210 条社区生图 prompt")
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("search", help="关键词检索（多词 AND）")
    s.add_argument("query")
    s.add_argument("--category", choices=ALL_CATEGORIES, default=None)
    s.add_argument("--limit", type=int, default=8)
    v = sub.add_parser("view", help="按 id 查看全文")
    v.add_argument("id")
    sub.add_parser("stats", help="各分类条目统计")
    args = p.parse_args()
    if not os.path.isdir(DATA_DIR):
        sys.exit(f"数据目录不存在: {DATA_DIR}")
    {"search": cmd_search, "view": cmd_view, "stats": cmd_stats}[args.cmd](args)


if __name__ == "__main__":
    main()
