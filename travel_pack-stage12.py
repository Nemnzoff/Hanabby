# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: TravelPack
def load_from_json(filepath):
    try:
        import json
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, list):
            for item in data:
                add_trip(item.get('name'), item.get('places', []), item.get('budget', 0), item.get('notes', ''))
        elif isinstance(data, dict):
            add_trip(data.get('name'), data.get('places', []), data.get('budget', 0), data.get('notes', ''))
    except FileNotFoundError:
        print(f"Файл {filepath} не найден.")
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON в файле {filepath}: {e}")
    except Exception as e:
        print(f"Неожиданная ошибка при загрузке данных из {filepath}: {e}")
