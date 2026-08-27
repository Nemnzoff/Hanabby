# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: TravelPack
def dry_run(self, op, data, context):
        """Имитация операции без изменения данных."""
        if op == "add_place":
            new_place = Place(**data)
            return {"place": new_place, "added": False, "conflict": None}
        elif op == "add_item":
            new_item = Item(**data)
            return {"item": new_item, "added": False, "conflict": None}
        elif op == "update_budget":
            return {"budget": self._budget, "updated": False}
        elif op == "add_note":
            return {"note": Note(**data), "added": False}
        elif op == "add_checklist":
            return {"checklist": Checklist(**data), "added": False}
        else:
            return {"error": f"Unknown dry-run operation: {op}"}
