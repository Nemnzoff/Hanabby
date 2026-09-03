# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: TravelPack
import json, copy, os

MIGRATION_DB = os.path.join(os.path.dirname(__file__), 'travelpack_data.json')

def migrate_db():
    if not os.path.exists(MIGRATION_DB):
        return
    with open(MIGRATION_DB, 'r', encoding='utf-8') as f:
        data = json.load(f)
    if isinstance(data, dict) and 'schema_version' in data:
        current = data['schema_version']
        if current < 2:
            data['schema_version'] = 2
            if 'places' not in data:
                data['places'] = []
            if 'checklists' not in data:
                data['checklists'] = []
            if 'budget' not in data:
                data['budget'] = {'total': 0, 'spent': 0}
            if 'notes' not in data:
                data['notes'] = []
            if 'settings' not in data:
                data['settings'] = {'language': 'ru', 'theme': 'light'}
            with open(MIGRATION_DB, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print("Migration to v2 complete.")
