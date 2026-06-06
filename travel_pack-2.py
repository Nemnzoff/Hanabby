# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: TravelPack
class TravelData:
    def __init__(self):
        self.checklists = {}
        self.places = {}
        self.budgets = {}
        self.notes = {}

    def validate_place_name(self, name):
        if not isinstance(name, str) or len(name.strip()) == 0:
            return False, "Имя места должно быть непустой строкой."
        return True, ""

    def validate_budget(self, amount):
        try:
            val = float(amount)
            if val < 0:
                return False, "Бюджет не может быть отрицательным."
            return True, str(val)
        except ValueError:
            return False, "Неверный формат бюджета (нужно число)."

    def validate_checklist_item(self, item):
        if not isinstance(item, str) or len(item.strip()) == 0:
            return False, "Пункт чек-листа должен быть непустой строкой."
        return True, ""

    def add_place(self, name, description=""):
        valid, msg = self.validate_place_name(name)
        if not valid:
            print(msg)
            return None
        self.places[name] = {"description": description}
        return self.places[name]

    def set_budget(self, place_name, amount):
        valid, msg = self.validate_budget(amount)
        if not valid:
            print(msg)
            return None
        if place_name in self.budgets:
            del self.budgets[place_name]
        self.budgets[place_name] = float(valid)
        return self.budgets[place_name]

    def add_checklist(self, place_name, item):
        valid, msg = self.validate_place_name(place_name)
        if not valid:
            print(msg)
            return None
        valid, msg = self.validate_checklist_item(item)
        if not valid:
            print(msg)
            return None
        if place_name not in self.checklists:
            self.checklists[place_name] = []
        self.checklists[place_name].append(item)
        return self.checklists[place_name]

    def add_note(self, place_name, note):
        if not isinstance(note, str) or len(note.strip()) == 0:
            print("Заметка должна быть непустой строкой.")
            return None
        if place_name not in self.notes:
            self.notes[place_name] = []
        self.notes[place_name].append(note)
        return self.notes[place_name]
