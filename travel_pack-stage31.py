# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: TravelPack
def switch_profile(selected=None):
    if selected is None:
        print("Выберите профиль:\n")
        for i, p in enumerate(profiles, 1):
            active = " (активен)" if p["active"] else ""
            print(f"  {i}. {p['name']}{active}")
        try:
            choice = int(input("\nНомер профиля: ")) - 1
            if 0 <= choice < len(profiles):
                selected = choice
            else:
                print("Некорректный выбор.")
                return
        except ValueError:
            return

    if selected is None or not isinstance(selected, int) or selected < 0 or selected >= len(profiles):
        print("Ошибка профиля.")
        return

    current = profiles[selected]
    if current["active"]:
        current["active"] = False
        active_count = sum(1 for p in profiles if p["active"])
        if active_count == 0:
            print("Все профили неактивны. Деактивируйте текущий.")
            return
        selected = min(i for i, p in enumerate(profiles) if p["active"])
    else:
        other_active = [i for i, p in enumerate(profiles) if p["active"]]
        if other_active and selected in other_active:
            print("Уже есть другой активный профиль.")
            return

    current["active"] = True

    for key in ["checklists", "destinations", "budget", "notes"]:
        stored_key = f"user_{selected}_{key}"
        if stored_key not in profile_storage and user_data.get(f"global_{key}"):
            profile_storage[stored_key] = {user["name"]: user_data[f"global_{key}"] for user in users.values()}

    print(f"Переключено на профиль: {current['name']}")
