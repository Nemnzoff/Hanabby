# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: TravelPack
import sys
import os

def colorize(text, color):
    """Apply ANSI color codes to text."""
    if os.name != 'nt':
        return f"\033[{color}m{text}\033[0m"
    return text

def enable_color():
    """Enable ANSI color support."""
    if os.name != 'nt':
        sys.stdout.reconfigure(encoding='utf-8')
    return True

def disable_color():
    """Disable ANSI color support."""
    if os.name != 'nt':
        sys.stdout.reconfigure(encoding='utf-8')
    return True

# ANSI color codes
COLORS = {
    'red': '31',
    'green': '32',
    'yellow': '33',
    'blue': '34',
    'magenta': '35',
    'cyan': '36',
    'white': '37',
    'bold': '1',
}

def print_colored(text, color='white'):
    """Print text with ANSI color codes."""
    if os.name != 'nt':
        print(f"\033[{COLORS.get(color, '37')}m{text}\033[0m", end='')
    else:
        print(text, end='')
