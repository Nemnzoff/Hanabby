# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: TravelPack
class Template:
    def __init__(self, name, checklist=None, places=None, budget=None, notes=""):
        self.name = name
        self.checklist = checklist or []
        self.places = places or []
        self.budget = budget or 0
        self.notes = notes

class TemplateManager:
    def __init__(self):
        self.templates = {}

    def add(self, template):
        self.templates[template.name] = template

    def get(self, name):
        return self.templates.get(name)

    def create_from_template(self, name, **kwargs):
        tmpl = self.templates[name]
        notes = kwargs.get("notes", tmpl.notes)
        budget = kwargs.get("budget", tmpl.budget) if budget is not None else tmpl.budget
        places = kwargs.get("places", [])
        checklist = [item for item in tmpl.checklist if item not in places and item not in checklist]
        return TravelEntry(name=name, checklist=checklist + places, budget=budget, notes=notes)

    def list_templates(self):
        return [{"name": k, "checklist": v.checklist, "budget": v.budget} for k, v in self.templates.items()]
