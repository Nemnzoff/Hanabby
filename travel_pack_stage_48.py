# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: TravelPack
class TravelLog:
    def __init__(self, name, date, budget):
        self.name = name
        self.date = date
        self.budget = budget
        self.spent = 0.0
        self.checklists = {}
        self.places = {}
        self.notes = []
        self.items = []

    def add_item(self, name, price, done=False):
        item = {"name": name, "price": price, "done": done}
        self.items.append(item)
        if done:
            self.spent += price
        return item

    def remove_item(self, index):
        if 0 <= index < len(self.items):
            item = self.items.pop(index)
            if item["done"]:
                self.spent -= item["price"]
            return item
        return None

    def add_place(self, name, description):
        place = {"name": name, "description": description, "visited": False}
        self.places[name] = place
        return place

    def mark_place_visited(self, name):
        if name in self.places:
            self.places[name]["visited"] = True

    def add_note(self, text):
        self.notes.append(text)
        return text

    def get_summary(self):
        return {
            "trip_name": self.name,
            "date": self.date,
            "budget": self.budget,
            "spent": self.spent,
            "remaining": self.budget - self.spent,
            "items_count": len(self.items),
            "places_count": len(self.places),
            "notes_count": len(self.notes),
        }

    def to_dict(self):
        return {
            "name": self.name,
            "date": self.date,
            "budget": self.budget,
            "spent": self.spent,
            "items": self.items,
            "places": self.places,
            "notes": self.notes,
        }
