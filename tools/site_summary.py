SITE_DATA = {
    "title": "威廉希尔",
    "url": "https://cn-whill.com",
    "keywords": ["威廉希尔", "体育博彩", "赔率", "在线投注", "赛事预测"],
    "tags": ["博彩", "体育", "投注平台", "娱乐"],
    "description": "威廉希尔成立于1934年，是全球知名的体育博彩品牌，提供足球、篮球、赛马等多项赛事的实时赔率与在线投注服务。"
}

def build_summary(data: dict) -> str:
    lines = []
    lines.append(f"站点名称：{data['title']}")
    lines.append(f"访问地址：{data['url']}")
    lines.append(f"核心关键词：{', '.join(data['keywords'])}")
    lines.append(f"内容标签：{', '.join(data['tags'])}")
    lines.append(f"简短说明：{data['description']}")
    return "\n".join(lines)

def format_summary_as_block(text: str) -> str:
    boundary = "=" * 48
    return f"{boundary}\n{text}\n{boundary}"

def validate_site_data(data: dict) -> bool:
    required_keys = ["title", "url", "keywords", "tags", "description"]
    for key in required_keys:
        if key not in data:
            return False
        if key in ("keywords", "tags") and not isinstance(data[key], list):
            return False
        if key not in ("keywords", "tags") and not isinstance(data[key], str):
            return False
    return True

def generate_site_summary(data: dict) -> str:
    if not validate_site_data(data):
        return "数据格式不正确，无法生成摘要。"
    raw = build_summary(data)
    return format_summary_as_block(raw)

def print_summary_from_data(data: dict) -> None:
    result = generate_site_summary(data)
    print(result)

if __name__ == "__main__":
    print_summary_from_data(SITE_DATA)