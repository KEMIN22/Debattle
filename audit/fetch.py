#!/usr/bin/env python3
"""Открыть страницу и найти на ней цифру/фразу (замена WebFetch, который блокирует прокси).

  python3 audit/fetch.py URL                 — текст страницы (первые 6000 символов)
  python3 audit/fetch.py URL "шаблон" [...]  — только строки с совпадениями (regex, без учёта регистра) ± контекст
Код выхода: 0 — страница открыта; 2 — не открылась (вердикт «?»).
"""
import html, re, subprocess, sys

def get(url):
    r = subprocess.run(['curl', '-sS', '-L', '--compressed', '--max-time', '30', '-A',
                        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124 Safari/537.36',
                        '-w', '\n__HTTP__%{http_code}', url], capture_output=True)
    raw = r.stdout
    m = re.search(rb'\n__HTTP__(\d+)$', raw)
    code = m.group(1).decode() if m else '000'
    body = raw[:m.start()] if m else raw
    enc = 'utf-8'
    cm = re.search(rb'charset=["\']?([\w-]+)', body[:3000], re.I)
    if cm: enc = cm.group(1).decode().lower()
    try: text = body.decode(enc, 'replace')
    except LookupError: text = body.decode('utf-8', 'replace')
    return code, text, r.stderr.decode('utf-8', 'replace')

def clean(t):
    t = re.sub(r'(?is)<(script|style|noscript|svg)[^>]*>.*?</\1>', ' ', t)
    t = re.sub(r'(?i)<br\s*/?>|</(p|div|li|tr|h\d|td|th)>', '\n', t)
    t = html.unescape(re.sub(r'<[^>]+>', ' ', t))
    lines = [re.sub(r'[ \t\xa0]+', ' ', l).strip() for l in t.split('\n')]
    return '\n'.join(l for l in lines if l)

if __name__ == '__main__':
    if len(sys.argv) < 2: print(__doc__); sys.exit(1)
    url, pats = sys.argv[1], sys.argv[2:]
    code, raw, err = get(url)
    txt = clean(raw)
    bad = code not in ('200', '203') or len(txt) < 200 or 'Host not in allowlist' in raw
    print(f'HTTP {code} | {len(txt)} симв. | {url}')
    if bad:
        print('НЕ ОТКРЫЛАСЬ:', (err or txt[:300]).strip()); sys.exit(2)
    if not pats:
        print(txt[:6000]); sys.exit(0)
    L = txt.split('\n'); hit = 0
    import signal; signal.signal(signal.SIGPIPE, signal.SIG_DFL)
    for i, l in enumerate(L):
        if any(re.search(p, l, re.I) for p in pats):
            hit += 1
            print(f'--- стр. {i}:'); print('\n'.join(x[:500] for x in L[max(0, i-1):i+2]))
            if hit >= 25: break
    if not hit: print('СОВПАДЕНИЙ НЕТ (страница открыта, но шаблон не найден)')
