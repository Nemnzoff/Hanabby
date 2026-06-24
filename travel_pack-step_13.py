# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: TravelPack
def search_trips(query, fields=None):
    if not query: return []
    q = query.lower()
    if fields is None: fields = ['destination', 'notes']
    results = [t for t in trips if any(q in str(getattr(t, f, '')).lower() for f in fields)]
    return sorted(results, key=lambda x: (x.get('date') or '').startswith(str(x['year']), 0))
