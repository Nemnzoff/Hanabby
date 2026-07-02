# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: TravelPack
def archive_old_trips(travel_plans, cutoff_date=None):
    if cutoff_date is None:
        from datetime import date, timedelta
        cutoff_date = date.today() - timedelta(days=365)
    
    archived_count = 0
    for plan in travel_plans:
        end_date = plan.get('end_date')
        status = plan.get('status', 'active')
        
        if (status == 'completed' or 
            (isinstance(end_date, str) and date.fromisoformat(end_date) < cutoff_date)):
            
            old_plan = travel_plans.pop(travel_plans.index(plan))
            old_plan['archived'] = True
            old_plan['archive_date'] = date.today().isoformat()
            archived_count += 1
    
    return archived_count

# Пример вызова:
# archived = archive_old_trips(travel_plans)
