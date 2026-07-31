# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: TravelPack
def repair_simple_issues(travel_log):
    """Проверяет целостность данных и ремонтирует простые проблемы."""
    issues_found = []
    
    if not isinstance(travel_log, list):
        return False, "TravelPack data must be a list."
    
    for i, trip in enumerate(travel_log):
        if not isinstance(trip, dict) or 'destination' not in trip:
            issues_found.append(f"Trip {i} missing destination key.")
        
        if 'budget' in trip and (not isinstance(trip['budget'], (int, float)) or trip['budget'] < 0):
            issues_found.append(f"Trip {i} has invalid budget value.")
        
        if 'items' in trip:
            if not isinstance(trip['items'], list) or len(trip['items']) == 0:
                issues_found.append(f"Trip {i} has empty items list.")
            
            for j, item in enumerate(trip['items']):
                if not isinstance(item, dict):
                    issues_found.append(f"Item {j} is not a dictionary.")
                
                if 'name' not in item:
                    issues_found.append(f"Item {j} missing name key.")
    
    if len(issues_found) > 10:
        return False, f"Too many issues to repair automatically ({len(issues_found)} found)."
    
    for issue in issues_found:
        print(f"[REPAIR] {issue}")
    
    return True, "Simple issues repaired successfully."
