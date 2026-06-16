# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: TravelPack
def main_menu():
    print("\n=== TravelPack: Меню ===")
    print("1. Показать все поездки")
    print("2. Добавить новую поездку")
    print("3. Редактировать поездку")
    print("4. Удалить поездку")
    print("5. Выход")
    choice = input("Выберите действие (1-5): ")
    if choice == "1":
        for trip in trips:
            print(f"\n{trip['id']}. {trip['name']} ({trip['location']})")
            print(f"   Бюджет: {trip.get('budget', 0)} | Статус: {trip.get('status', 'Не начато')}")
    elif choice == "2":
        name = input("Название поездки: ")
        location = input("Место: ")
        budget_str = input("Бюджет (или Enter для пропуска): ")
        status = input("Статус (планируется/в пути/завершена) или Enter: ")
        trips.append({
            "id": len(trips) + 1,
            "name": name,
            "location": location,
            "budget": float(budget_str) if budget_str else None,
            "status": status or "Не начато",
            "checklist": [],
            "notes": ""
        })
    elif choice == "3":
        idx = int(input("ID поездки для редактирования: ")) - 1
        if 0 <= idx < len(trips):
            t = trips[idx]
            print(f"Текущее название: {t['name']}")
            new_name = input("Новое название (Enter чтобы оставить): ") or t['name']
            print(f"Текущее место: {t['location']}")
            new_loc = input("Новое место (Enter чтобы оставить): ") or t['location']
            budget_str = input(f"Текущий бюджет: {t.get('budget', 0)}\nНовый бюджет (или Enter): ")
            if budget_str != "":
                t["budget"] = float(budget_str)
            print(f"Текущий статус: {t['status']}")
            new_status = input("Новый статус (Enter чтобы оставить): ") or t['status']
            t["name"], t["location"], t["status"] = new_name, new_loc, new_status
    elif choice == "4":
        idx = int(input("ID поездки для удаления: ")) - 1
        if 0 <= idx < len(trips):
            del trips[idx]
            print("Поездка удалена.")
    elif choice == "5":
        print("Выход из программы.")
        return False
