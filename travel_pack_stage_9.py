# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: TravelPack
import json, sys

def load_initial_data(json_string):
    try:
        data = json.loads(json_string)
        if not isinstance(data, dict):
            raise ValueError("JSON должен содержать объект")
        
        # Инициализация структуры данных по умолчанию
        default_structure = {
            "trips": [],
            "places": {},
            "budgets": {},
            "notes": {}
        }
        
        # Объединение с дефолтной структурой, если ключи отсутствуют
        for key in default_structure:
            if key not in data or (key == "trips" and not isinstance(data[key], list)):
                data[key] = []
            elif key != "trips":
                # Для словарей (places, budgets, notes) проверяем типы значений
                current_type = type(default_structure[key]).__name__ if default_structure[key] else dict
                expected_type = str if isinstance(data.get(key), list) else dict
                data[key] = {k: v for k, v in data[key].items() if isinstance(v, (str, int, float))}

        return data
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
        sys.exit(1)

# Пример использования с тестовой строкой
if __name__ == "__main__":
    test_json = '''
    {
      "trips": [{"id": 1, "title": "Отпуск", "date": "2024-10-01"}],
      "places": {"Paris": {"cost": 500}, "London": {"cost": 600}},
      "budgets": {"Paris": 1000, "London": 800},
      "notes": {"Paris": "Виза нужна", "London": "Музейный проездной"}
    }'''
    
    loaded_data = load_initial_data(test_json)
    print(f"Загружено {len(loaded_data['trips'])} поездок и {len(loaded_data['places'])} мест.")
