# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: TravelPack
def sort_items(items, key='date'):
    if not items: return []
    order = {'low': 0, 'medium': 1, 'high': 2}
    reverse = {key == 'priority'}
    def _sort(i):
        val = i.get(key)
        if key == 'priority': return order.get(val.lower(), 1)
        try: return datetime.fromisoformat(val.replace('Z', '+00:00'))
        except: return None
    items.sort(key=_sort, reverse=reverse)
    return items
