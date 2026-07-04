# === Stage 20: Добавь восстановление записей из архива ===
# Project: TravelPack
import json, os, datetime

def restore_from_archive(archive_path):
    if not os.path.exists(archive_path):
        return
    try:
        with open(archive_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for key in ['trips', 'checklists', 'places', 'budgets', 'notes']:
            if key in data and isinstance(data[key], list):
                existing = globals().get(key, [])
                for item in data[key]:
                    if not any(item.get('id') == e['id'] for e in existing):
                        existing.append(item)
        with open('travel_pack_data.json', 'w', encoding='utf-8') as f:
            json.dump({k: v for k, v in globals().items() if isinstance(v, list)}, f, ensure_ascii=False, indent=2)
    except Exception:
        pass
