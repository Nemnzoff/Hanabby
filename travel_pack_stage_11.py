# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: TravelPack
import json, os

def save_to_file(data: dict, filename: str = "travel_pack.json") -> None:
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Данные успешно сохранены в {filename}")
    except Exception as e:
        print(f"Ошибка при сохранении файла: {e}")

def load_from_file(filename: str = "travel_pack.json") -> dict | None:
    if not os.path.exists(filename):
        return None
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"Данные успешно загружены из {filename}")
        return data
    except Exception as e:
        print(f"Ошибка при загрузке файла: {e}")
        return None
