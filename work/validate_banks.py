import json, re, sys
p = sys.argv[1] if len(sys.argv) > 1 else 'docs/data/banks.json'
b = json.load(open(p, encoding='utf-8'))
errs = []
def wc(s): return len(re.findall(r'[\w\-]+', s))
def chk(s, lim, where):
    if not isinstance(s, str) or not s.strip(): errs.append(f'{where}: пусто'); return
    if wc(s) > lim: errs.append(f'{where}: {wc(s)} слов > {lim}: {s[:50]}')
BAN = ['в современном мире','с одной стороны','важно отметить','играет ключевую роль','таким образом','в эпоху','неоспоримо']
def walk(o, where='', lim=15):
    if isinstance(o, dict):
        for k, v in o.items(): walk(v, f'{where}.{k}', 25 if k in ('answer','answer30') else lim)
    elif isinstance(o, list):
        for i, v in enumerate(o): walk(v, f'{where}[{i}]', lim)
    elif isinstance(o, str):
        # поля-метки (time codes, имена) не проверяем жёстко
        chk(o, lim if not where.endswith(('.what','.task','.example','.trap')) else 25, where)
        for w in BAN:
            if w in o.lower(): errs.append(f'{where}: штамп «{w}»')
walk(b)
a = b.get('archetypes', [])
if len(a) != 9: errs.append(f'архетипов {len(a)} != 9')
for x in a:
    for s in 'ab':
        if len(x[s]['args']) != 3 or len(x[s]['criteria']) != 2: errs.append(f'кластер {x["cluster"]}/{s}: args/criteria')
sp = b.get('speech', {})
if len(sp.get('steps', [])) != 5: errs.append('speech.steps != 5')
if len(sp.get('prep', [])) != 3: errs.append('speech.prep != 3')
if len(b.get('questions', [])) != 8: errs.append('questions != 8')
if len(b.get('rescue', [])) != 10: errs.append('rescue != 10')
c = b.get('complications', {})
if len(c.get('foreign', [])) != 9 or any(len(f['bridges']) != 2 for f in c.get('foreign', [])): errs.append('foreign != 9x2')
if len(c.get('idioms', [])) != 15: errs.append('idioms != 15')
if len(c.get('genres', [])) != 6: errs.append('genres != 6')
for k in ('arsenal', 'one_for_all', 'no_prep'):
    if len(c.get(k, [])) != 3: errs.append(f'{k} != 3')
if len(b.get('infokiller', [])) != 10: errs.append('infokiller != 10')
print('\n'.join(errs) if errs else 'OK'); print(len(errs), 'замечаний')
