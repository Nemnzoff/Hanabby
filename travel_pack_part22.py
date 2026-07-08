# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: TravelPack
import time as _time


def check_expired_reminders(reminders, now=None):
    if now is None:
        now = _time.time()
    expired = []
    for r in reminders:
        deadline = r.get("deadline", 0)
        if not isinstance(deadline, (int, float)):
            continue
        if now > deadline:
            expired.append(r)
    return expired


def notify_expiration(reminders):
    expired = check_expired_reminders(reminders)
    if not expired:
        print("Нет просроченных напоминаний.")
        return
    for r in expired:
        name = r.get("name", "Напоминание")
        print(f"⚠️ Просрочено: {name}")
