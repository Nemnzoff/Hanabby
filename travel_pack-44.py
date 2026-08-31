# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: TravelPack
def backup_data_file(file_path):
    """Создаёт резервную копию файла данных с timestamp в имени."""
    import shutil, datetime
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = file_path.rsplit(".", 1)[0] + f"_backup_{timestamp}.json"
    shutil.copy2(file_path, backup_path)
    print(f"[Backup] {file_path} -> {backup_path}")
    return backup_path
