# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: TravelPack
def calculate_monthly_stats(trips, expenses):
    from datetime import date
    stats = {}
    for trip in trips:
        if not hasattr(trip, 'start_date'): continue
        start = trip.start_date
        month_key = f"{start.year}-{start.month:02d}"
        if month_key not in stats: stats[month_key] = {'trips': 0, 'days': 0}
        stats[month_key]['trips'] += 1
        end = trip.end_date or start.replace(day=28)
        for d in range(start.day, min(end.day + 1, 32)):
            try: date(year=start.year, month=start.month, day=d)
            except ValueError: continue
            stats[month_key]['days'] += 1
    total_expenses = sum(expenses.values()) if expenses else 0
    for key in sorted(stats.keys()):
        m_stats = stats[key]
        avg_days = round(m_stats['days'] / max(1, m_stats['trips']), 2)
        print(f"Месяц {key}: поездок={m_stats['trips']}, дней={m_stats['days']}, сред. длительность={avg_days} дн.")
