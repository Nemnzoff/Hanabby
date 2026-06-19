# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: TravelPack
def export_to_json():
    import json
    data = {
        "trip_name": trip_data.get("name", ""),
        "budget": trip_budget,
        "places": places_list,
        "checklists": checklists_dict,
        "notes": notes_text
    }
    return json.dumps(data, ensure_ascii=False, indent=2)
