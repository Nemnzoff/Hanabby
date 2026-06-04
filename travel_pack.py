# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: TravelPack
import json
from datetime import datetime

def load_data():
    try:
        with open("travel_pack.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"trips": [], "budget": 0}

def save_data(data):
    with open("travel_pack.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def add_trip(name, destination, start_date, budget):
    data = load_data()
    trip = {
        "id": len(data["trips"]) + 1,
        "name": name,
        "destination": destination,
        "start_date": start_date,
        "budget": float(budget),
        "spent": 0.0,
        "checklist": [],
        "notes": ""
    }
    data["trips"].append(trip)
    save_data(data)
    return trip

def add_checklist_item(trip_id, item):
    data = load_data()
    for trip in data["trips"]:
        if trip["id"] == trip_id:
            trip["checklist"].append(item)
            save_data(data)
            return True
    return False

def update_budget(trip_id, amount):
    data = load_data()
    for trip in data["trips"]:
        if trip["id"] == trip_id:
            trip["spent"] += float(amount)
            save_data(data)
            return trip["spent"]
    return None

def get_all_trips():
    data = load_data()
    return data["trips"]

if __name__ == "__main__":
    # Демонстрационные данные
    add_trip("Лето", "Санкт-Петербург", "2024-06-15", 30000)
    add_checklist_item(1, "Купить билеты")
    add_checklist_item(1, "Забронировать отель")
    update_budget(1, 5000)
    print("Данные инициализированы.")
