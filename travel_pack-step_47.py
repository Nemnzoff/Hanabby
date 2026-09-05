# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: TravelPack
def demo():
    """Показывает основной пользовательский сценарий TravelPack."""
    print("=== TravelPack Demo ===\n")

    # 1. Создаём места
    places = {
        "Париж": {"type": "city", "cost": 200, "notes": "Романтика и еда"},
        "Рим": {"type": "city", "cost": 150, "notes": "История и пицца"},
        "Сочи": {"type": "beach", "cost": 80, "notes": "Море и закат"},
    }
    print("Добавлены места:")
    for name, info in places.items():
        print(f"  {name} ({info['type']}) — {info['cost']}$", info["notes"])

    # 2. Создаём чек-лист
    checklist = ["Упаковать чемоданы", "Купить билеты", "Забронировать отель", "Загрузить карты"]
    print(f"\nЧек-лист: {', '.join(checklist)}")

    # 3. Добавляем места в планировку
    itinerary = {}
    for name, info in places.items():
        itinerary[name] = info
    print(f"\nПланировка: {list(itinerary.keys())}")

    # 4. Проверяем бюджет
    total_cost = sum(info["cost"] for info in itinerary.values())
    budget = 500
    print(f"\nБюджет: {budget}$, потрачено: {total_cost}$, осталось: {budget - total_cost}$")

    # 5. Добавляем заметку
    notes = {"general": "Отличный отпуск! Не забыть крем от загара."}
    print(f"\nЗаметки: {notes['general']}")

    # 6. Завершаем чек-лист
    checklist.append("Все готово!")
    print(f"\nФинальный чек-лист: {', '.join(checklist)}")
    print("\n=== Demo завершён ===")
