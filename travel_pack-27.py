# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: TravelPack
import os, json

def reset_demo_data(traveler_db):
    """Сбросить демо-данные: удалить все чек-листы, места, заметки и вернуть пустые списки."""
    for key in list(traveler_db.keys()):
        del traveler_db[key]
    traveler_db['checklists'] = []
    traveler_db['places'] = []
    traveler_db['notes'] = []
    return True

def clear_state():
    """Очистить все данные приложения (включая демо), вернуть сообщение."""
    try:
        reset_demo_data(traveler_db)
        if os.path.exists('travel_pack.json'):
            with open('travel_pack.json', 'w') as f:
                json.dump({'checklists': [], 'places': [], 'notes': []}, f, indent=2)
        return "Состояние полностью очищено. Демо-данные сброшены."
    except Exception as e:
        return f"Ошибка очистки: {e}"

def get_demo_data():
    """Возвращает демо-данные для заполнения приложения при старте."""
    demo = {
        'checklists': [
            {'id': 1, 'title': 'До вылета', 'items': ['Паспорт', 'Билет', 'Рюкзак', 'Зарядка'], 'done': []},
            {'id': 2, 'title': 'На месте', 'items': ['Визитная карточка', 'Переводчик', 'Деньги'], 'done': []}
        ],
        'places': [
            {'id': 1, 'name': 'Парк', 'type': 'nature', 'notes': 'Хороший отдых'},
            {'id': 2, 'name': 'Музей', 'type': 'culture', 'notes': 'Интересные экспонаты'}
        ],
        'notes': [
            {'id': 1, 'title': 'Бюджет на поездку', 'content': 'Около 500$', 'created': '2024-01-01'},
            {'id': 2, 'title': 'Важные номера', 'content': 'Скорая: 112, Полиция: 102', 'created': '2024-01-01'}
        ]
    }
    return demo

def load_demo_data(traveler_db):
    """Загрузить демо-данные в структуру приложения."""
    demo = get_demo_data()
    for key in ['checklists', 'places', 'notes']:
        if key in demo:
            traveler_db[key] = demo[key]
    return True
