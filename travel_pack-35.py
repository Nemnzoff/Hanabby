# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: TravelPack
def get_next_action(trip):
    """Recommends the next action based on current trip state."""
    if not trip.get("name"):
        return "Заполните название поездки."
    if not trip.get("destination") and not trip.get("places"):
        return "Добавьте хотя бы одно место назначения или список мест."
    if not trip.get("budget", {}).get("total"):
        return "Укажите общий бюджет поездки."
    if not trip.get("checklist"):
        return "Заполните чек-лист: визы, страховка, документы."
    if not trip.get("notes") and not trip.get("itinerary"):
        return "Добавьте заметки или маршрут поездки."
    for date in trip.get("dates", []):
        if not isinstance(date, datetime) or date.date() < today:
            continue
        elif date.date() > today + timedelta(days=30):
            continue
        else:
            return f"Подготовка к дате {date.strftime('%d.%m')}: проверьте детали."
    return "Поездка готова! Удачи в путешествии!"
