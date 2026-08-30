# === Stage 43: Добавь пагинацию длинных списков ===
# Project: TravelPack
class Pagination:
    def __init__(self, items, page_size=10):
        self.items = items
        self.page_size = page_size
        self.total_pages = (len(items) + page_size - 1) // page_size if items else 0
        self.current_page = 1

    def get_page(self, page):
        start = (page - 1) * self.page_size
        end = start + self.page_size
        return self.items[start:end]

    def get_page_info(self):
        return {
            'current_page': self.current_page,
            'total_pages': self.total_pages,
            'page_size': self.page_size,
            'total_items': len(self.items),
            'has_next': self.current_page < self.total_pages,
            'has_prev': self.current_page > 1,
        }

    def navigate(self, direction):
        if direction == 'next' and self.has_next:
            self.current_page += 1
        elif direction == 'prev' and self.has_prev:
            self.current_page -= 1
        return self.get_page_info()
