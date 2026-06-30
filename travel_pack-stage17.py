# === Stage 17: Добавь группировку записей по категориям ===
# Project: TravelPack
def group_by_category(records, categories):
    grouped = {cat: [] for cat in categories}
    for rec in records:
        cat = rec.get('category', 'other') or 'other'
        if cat not in grouped:
            grouped[cat] = []
        grouped[cat].append(rec)
    return grouped

def render_grouped_list(grouped, fields=None):
    if fields is None:
        fields = ['title', 'description']
    for cat, items in grouped.items():
        print(f"\n[{cat}]")
        for item in items:
            vals = [str(item.get(f)) for f in fields]
            print("  - " + ", ".join(vals) if vals else "- (пусто)")
