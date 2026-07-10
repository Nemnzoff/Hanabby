# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: TravelPack
def print_table(headers, rows):
    """Compact console table: prints headers and row data aligned."""
    col_widths = [len(str(h)) for h in headers]
    for r in rows:
        for i, v in enumerate(r):
            if len(str(v)) > col_widths[i]:
                col_widths[i] = len(str(v))

    lines = []
    sep_parts = ['-' * w for w in col_widths]
    lines.append('  |'.join(sep_parts))
    header_line = '  '.join(f'{h:<{col_widths[i]}}' for i, h in enumerate(headers))
    lines.append(header_line)
    lines.append('  |'.join('-' * col_widths[i] for i in range(len(headers))))

    for r in rows:
        row_str = '  '.join(f'{str(r[i]):<{col_widths[i]}}' if i < len(r) else '' for i in range(len(headers)))
        lines.append(row_str)

    print('\n'.join(lines))
