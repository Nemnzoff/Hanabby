# === Stage 45: Добавь восстановление из резервной копии ===
# Project: TravelPack
import json, os, sys

def load_backup(backup_path):
    if not os.path.exists(backup_path):
        print(f"Резервная копия не найдена: {backup_path}")
        return None
    try:
        with open(backup_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"Резервная копия успешно загружена из {backup_path}")
        return data
    except Exception as e:
        print(f"Ошибка чтения резервной копии: {e}")
        return None

def restore_backup(backup_path, output_path=None):
    data = load_backup(backup_path)
    if data is None:
        return False
    if output_path is None:
        output_path = sys.argv[0] if len(sys.argv) > 1 else "travel_pack.py"
    if not output_path.endswith('.py'):
        output_path += '.py'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(json.dumps(data, indent=2, ensure_ascii=False))
    print(f"Резервная копия восстановлена в {output_path}")
    return True
