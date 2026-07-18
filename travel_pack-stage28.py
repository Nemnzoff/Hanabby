# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: TravelPack
import statistics


def compute_travel_metrics(trips):
    """Вычисляет ключевые метрики проекта TravelPack."""
    if not trips:
        return {
            "total_trips": 0,
            "avg_budget": 0,
            "avg_distance_km": 0,
            "total_checked_items": 0,
            "most_visited_place": None,
            "countries_covered": [],
            "budget_utilization": {},
        }

    total_budget = sum(t.get("budget", t.get("spent", {}).get("total", 0)) for t in trips)
    avg_distance_km = statistics.mean([t.get("distance_km", 0) for t in trips]) if trips else 0.0
    total_checked_items = sum(len(t.get("checklist", [])) for t in trips)

    place_visits = {}
    countries = set()
    budget_by_trip = {}
    for trip in trips:
        place_name = trip.get("place", {}).get("name", "Unknown")
        budget_by_trip[trip.get("id")] = {
            "budget": trip.get("budget"),
            "spent": trip.get("spent", {}).get("total", 0),
            "utilization_pct": (
                (trip["spent"]["total"] / trip["budget"]) * 100
                if trip.get("budget") and trip["budget"] > 0
                else None
            ),
        }
        place_visits[place_name] = place_visits.get(place_name, 0) + 1
        countries.update(trip.get("countries", []))

    most_visited_place = max(place_visits, key=place_visits.get) if place_visits else None
    countries_covered = sorted(countries)

    return {
        "total_trips": len(trips),
        "avg_budget": total_budget / len(trips) if trips else 0.0,
        "avg_distance_km": avg_distance_km,
        "total_checked_items": total_checked_items,
        "most_visited_place": most_visited_place,
        "countries_covered": countries_covered,
        "budget_utilization": budget_by_trip,
    }
