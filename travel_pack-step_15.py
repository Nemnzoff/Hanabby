# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: TravelPack
def calculate_weekly_stats(trips):
    weekly_data = {}
    for trip in trips:
        if not trip.get('dates'): continue
        start, end = trip['dates']['start'], trip['dates']['end']
        current_date = datetime(start.year, start.month, start.day)
        while current_date <= datetime(end.year, end.month, end.day):
            week_key = (current_date - timedelta(days=current_date.weekday())).isoformat()
            weekly_data.setdefault(week_key, {'count': 0, 'total_cost': 0})[0] += 1
            if trip.get('budget'): weekly_data[week_key]['total_cost'] += trip['budget']['amount']
            current_date += timedelta(days=7)
    return weekly_data
