#!/usr/bin/env python3
"""Собирает docs/offline.html: тот же сайт, все данные вшиты внутрь, без сети."""
import glob, json, os, re

ROOT = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.join(ROOT, 'docs')
DATA = os.path.join(DOCS, 'data')

def load(path):
    with open(path, encoding='utf-8') as f:
        return json.load(f)

topics = load(os.path.join(DATA, 'topics.json'))
banks_path = os.path.join(DATA, 'banks.json')
cards = {}
for p in sorted(glob.glob(os.path.join(DATA, 'cards', '*.json'))):
    cards[os.path.splitext(os.path.basename(p))[0]] = load(p)

data = {
    'topics': topics['topics'],
    'clusters': topics['clusters'],
    'banks': load(banks_path) if os.path.exists(banks_path) else {},
    'cards': cards,
}
blob = json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')

with open(os.path.join(DOCS, 'index.html'), encoding='utf-8') as f:
    html = f.read()

assert '/*__INLINE_DATA__*/' in html, 'нет маркера данных в index.html'
html = html.replace('/*__INLINE_DATA__*/', 'window.__DATA__=' + blob + ';')
# офлайн: без внешних шрифтов (системный шрифт)
html = re.sub(r'<!--FONTS-->.*?<!--/FONTS-->', '', html, flags=re.S)
assert 'http://' not in html.split('<script>')[0] and 'fonts.googleapis' not in html

out = os.path.join(DOCS, 'offline.html')
with open(out, 'w', encoding='utf-8') as f:
    f.write(html)
print('offline.html: %d КБ, тем %d, карточек %d, банки: %s' % (
    os.path.getsize(out) // 1024, len(data['topics']), len(cards), 'да' if data['banks'] else 'нет'))
