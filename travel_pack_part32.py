# === Stage 32: Добавь журнал действий пользователя ===
# Project: TravelPack
import json, datetime

class ActionLog:
    def __init__(self):
        self._entries = []

    def log(self, action_type, description):
        entry = {
            "timestamp": datetime.datetime.now().isoformat(),
            "type": action_type,
            "description": description
        }
        self._entries.append(entry)

    def get_log(self):
        return list(reversed(self._entries))

    def clear(self):
        self._entries.clear()

log = ActionLog()
