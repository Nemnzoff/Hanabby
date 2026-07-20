# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: TravelPack
APP_CONFIG = {
    "app_name": "TravelPack",
    "version": 1,
    "default_currency": "USD",
    "default_language": "ru",
    "max_places_per_trip": 20,
    "max_checklist_items": 50,
    "budget_warn_threshold_pct": 80,
}

def get_config(key: str = None) -> dict | str:
    if key is not None and key in APP_CONFIG:
        return APP_CONFIG[key]
    return dict(APP_CONFIG)
