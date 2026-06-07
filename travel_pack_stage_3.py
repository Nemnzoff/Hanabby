# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: TravelPack
travel_data = {
    "destinations": [],
    "checklists": {},
    "budget": {"total": 0, "spent": 0},
    "notes": []
}

def add_destination(name, country, days):
    travel_data["destinations"].append({"name": name, "country": country, "days": days})
    return f"Добавлено: {name} ({country}) на {days} дней."

def add_checklist(destination_name, items):
    if destination_name not in travel_data["checklists"]:
        travel_data["checklists"][destination_name] = []
    for item in items:
        travel_data["checklists"][destination_name].append(item)
    return f"Чек-лист для {destination_name} обновлен."

def add_note(text):
    travel_data["notes"].append({"text": text, "timestamp": time.time()})
    return "Заметка сохранена."

def set_budget(total):
    travel_data["budget"]["total"] = total
    return f"Бюджет установлен на {total}"

import time
