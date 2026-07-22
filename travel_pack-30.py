# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: TravelPack
class TravelProfiles:
    def __init__(self):
        self.profiles = {}
    
    def add_profile(self, name, budget=0, currency="USD"):
        if name in self.profiles:
            return f"Профиль '{name}' уже существует."
        profile = {"budget": budget, "currency": currency}
        self.profiles[name] = profile
        return f"Профиль '{name}' добавлен с бюджетом {budget} {currency}."
    
    def get_profile(self, name):
        if name not in self.profiles:
            raise ValueError(f"Профиль '{name}' не найден.")
        return self.profiles[name]
    
    def delete_profile(self, name):
        if name not in self.profiles:
            return f"Профиль '{name}' не найден."
        del self.profiles[name]
        return f"Профиль '{name}' удалён."
