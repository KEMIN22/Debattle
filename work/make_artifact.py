#!/usr/bin/env python3
"""docs/offline.html -> страница для публикации как Artifact (без doctype/head/body, без печати, поля 16px).
python3 work/make_artifact.py <выходной_файл>"""
import re, sys
s = open('docs/offline.html', encoding='utf-8').read()
style = re.search(r'<style>.*?</style>', s, re.S).group(0)
body = re.search(r'<body>(.*)</body>', s, re.S).group(1)
for a, b in [(".wrap{padding:12px 14px", ".wrap{padding:12px 16px"), ("padding:10px 14px;display:flex", "padding:10px 16px;display:flex"),
             ("position:sticky;top:0;", "position:sticky;top:env(safe-area-inset-top,0px);")]:
    if a in style: style = style.replace(a, b)
style = style.replace("<style>", "<style>\n:root{color-scheme:dark}\n", 1)
body = re.sub(r"<div class=\"row\"><button class=\"btn alt\" data-act=\"print1\"[^<]*(?:'\+id\+')?[^<]*</button></div>", "", body)
body = body.replace('<div class="row"><button class="btn alt sm" data-act="printAll">🖨 Печать готовых карточек</button></div>', '')
open(sys.argv[1], 'w', encoding='utf-8').write('<title>Твой Ход × Дебаттл</title>\n' + style + '\n' + body)
print('ok', len(body) // 1024, 'КБ')
