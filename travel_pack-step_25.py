# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: TravelPack
def parse_date(date_str):
    """Parse date strings in various formats and return a tuple (year, month, day)."""
    import datetime
    
    if not isinstance(date_str, str) or len(date_str.strip()) == 0:
        raise ValueError("Некорректная дата: пустая строка или не строка")
    
    date_str = date_str.strip()
    
    formats = [
        ("%Y-%m-%d", "YYYY-MM-DD"),
        ("%d.%m.%Y", "DD.MM.YYYY"),
        ("%d/%m/%Y", "DD/MM/YYYY"),
        ("%B %d, %Y", "Month DD, YYYY"),
        ("%b %d, %Y", "Mon DD, YYYY"),
    ]
    
    for fmt, label in formats:
        try:
            dt = datetime.datetime.strptime(date_str, fmt)
            return (dt.year, dt.month, dt.day)
        except ValueError:
            continue
    
    raise ValueError(f"Некорректная дата в формате '{date_str}'. Поддерживаются форматы: YYYY-MM-DD, DD.MM.YYYY, DD/MM/YYYY")


def format_date(year, month, day):
    """Format a date tuple back to string."""
    import datetime
    dt = datetime.datetime(year, month, day)
    return dt.strftime("%d.%m.%Y")
