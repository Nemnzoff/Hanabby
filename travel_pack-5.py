# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: TravelPack
def remove_record(record_id, records_list):
    """
    Удаляет запись по ID из списка. Возвращает обновленный список и сообщение о результате.
    Если записи нет, возвращает исходный список и уведомление.
    """
    if record_id in records_list:
        index = records_list.index(record_id)
        removed_item = records_list.pop(index)
        return records_list, f"Запись '{removed_item}' успешно удалена."
    else:
        return records_list, f"Запись с ID {record_id} не найдена."

# Пример вызова (раскомментируйте для тестирования):
# updated_list, status_msg = remove_record(105, my_records)
# print(status_msg)
# print(updated_list)
