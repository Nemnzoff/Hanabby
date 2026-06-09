# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: TravelPack
def edit_record(record_id, updates):
    if not updates:
        print("Нет данных для обновления.")
        return
    for key in list(records.keys()):
        if records[key].get('id') == record_id:
            records[key].update(updates)
            print(f"Запись {record_id} обновлена.")
            return
    print(f"Запись с ID {record_id} не найдена.")

def delete_record(record_id):
    for key in list(records.keys()):
        if records[key].get('id') == record_id:
            del records[key]
            print(f"Запись {record_id} удалена.")
            return
    print(f"Запись с ID {record_id} не найдена.")

def view_record(record_id):
    for key in records.keys():
        if records[key].get('id') == record_id:
            print(records[key])
            return
    print(f"Запись с ID {record_id} не найдена.")
