# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: TravelPack
def demo_quick_test():
    print("🧪 TravelPack — Быстрый ручной Тест")
    print("=" * 40)
    destinations = [
        {"name": "Paris", "country": "France"},
        {"name": "Tokyo", "country": "Japan"},
        {"name": "New York", "country": "USA"},
    ]
    for d in destinations:
        print(f"  📍 {d['name']}, {d['country']}")
