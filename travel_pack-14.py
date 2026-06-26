# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: TravelPack
def generate_summary(trips):
    if not trips:
        return "Нет данных для сводки."
    
    total_budget = sum(t.get('budget', 0) for t in trips.values())
    spent = sum(t.get('spent', 0) for t in trips.values())
    remaining = total_budget - spent
    
    active_checklists = [t['name'] for t in trips.values() if any(item.get('done') is False for item in t.get('checklist', []))]
    
    summary_lines = [
        f"=== Сводка по поездкам ({len(trips)} шт.) ===",
        f"Общий бюджет: {total_budget:.2f}",
        f"Потрачено: {spent:.2f}",
        f"Остаток: {remaining:.2f}",
    ]
    
    if active_checklists:
        summary_lines.append(f"\nАктивные чек-листы:")
        for trip_name in active_checklists:
            summary_lines.append(f"- {trip_name}")
            
    return "\n".join(summary_lines)
