# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: TravelPack
def print_trip_summary(trip):
    """Выводит одну запись о поездке в компактном формате."""
    if not trip:
        return None
    print(f"{'='*40}")
    print(f"📍 {trip['destination']}")
    print(f"   {'-'*18} | {'-'*5} | {'-'*7}")
    print(f"   День  : {trip['days']:2d}      Бюджет: {trip.get('budget', 'N/A'):>6}")
    print(f"   {'─'*40}")
    if trip.get('tasks'):
        done = sum(1 for t in trip['tasks'] if t['done'])
        total = len(trip['tasks'])
        print(f"   Задачи: {done}/{total} выполнены")
        for i, task in enumerate(trip['tasks'], 1):
            status = "✅" if task['done'] else "⬜"
            print(f"      {i}. [{status}] {task['title']}")
    if trip.get('places'):
        print("   Места:")
        for place in trip['places']:
            print(f"      • {place['name']} — {place.get('notes', '')}")
    if trip.get('notes'):
        print(f"   💬 Заметки: {trip['notes'][:80]}")
    print(f"{'='*40}")
