#!/usr/bin/env python3
"""Добавить строки в таблицу окружных/региональных тем SUMMARY.md: add_rows.py okr|reg 'строка' ..."""
import sys
sec, rows = sys.argv[1], sys.argv[2:]
p = 'audit/SUMMARY.md'; s = open(p, encoding='utf-8').read()
end = s.find('\n## Региональные') if sec == 'okr' else s.find('\n## Ручная проверка')
if end < 0: end = len(s)
s = s[:end].rstrip('\n') + '\n' + '\n'.join(rows) + '\n' + s[end:]
open(p, 'w', encoding='utf-8').write(s)
