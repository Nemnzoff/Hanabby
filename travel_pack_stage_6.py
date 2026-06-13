# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: TravelPack
class Filter:
    def __init__(self, records):
        self.records = records
    
    def filter_by_status(self, status):
        return [r for r in self.records if r.get('status') == status]
    
    def filter_by_category(self, category):
        return [r for r in self.records if r.get('category') == category]
    
    def filter_by_tag(self, tag):
        return [r for r in self.records if any(tag in t for t in r.get('tags', []))]
    
    def combine_filters(self, status=None, category=None, tags=None):
        result = self.records
        if status:
            result = self.filter_by_status(status)
        if category:
            result = [r for r in result if r.get('category') == category]
        if tags:
            result = [r for r in result if any(tag in t for tag in tags for t in r.get('tags', []))]
        return result
