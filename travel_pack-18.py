# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: TravelPack
class TagManager:
    def __init__(self, db):
        self.db = db
    
    def add_tag(self, name):
        if not any(t['name'] == name for t in self.db.get('tags', [])):
            self.db.setdefault('tags', []).append({'id': len(self.db.get('tags', [])) + 1, 'name': name})
    
    def remove_tag(self, tag_name):
        tags = self.db.get('tags', [])
        for t in reversed(tags):
            if t['name'] == tag_name:
                del t['id']
                return True
        return False
    
    def add_location_tags(self, location_id, tag_names):
        locations = self.db.setdefault('locations', [])
        loc_idx = next((i for i, l in enumerate(locations) if l.get('id') == location_id), None)
        if loc_idx is not None:
            tags_to_add = [t['name'] for t in self.db.get('tags', []) if t['name'] in tag_names]
            existing_tags = {l.get('tag_ids', set())}
            new_tag_ids = []
            for name in tags_to_add:
                tag_obj = next((t for t in self.db.get('tags', []) if t['name'] == name), None)
                if tag_obj:
                    existing_tags.add(tag_obj['id'])
            locations[loc_idx]['tag_ids'] = list(existing_tags)
    
    def remove_location_tags(self, location_id, tag_names):
        locations = self.db.setdefault('locations', [])
        loc_idx = next((i for i, l in enumerate(locations) if l.get('id') == location_id), None)
        if loc_idx is not None:
            current_tag_ids = set(l.get('tag_ids', []))
            tags_to_remove = [t['name'] for t in self.db.get('tags', []) if t['name'] in tag_names]
            new_current_tags = {current_tag_ids} - {t['id'] for t in self.db.get('tags', []) if t['name'] in tags_to_remove}
            locations[loc_idx]['tag_ids'] = list(new_current_tags)
