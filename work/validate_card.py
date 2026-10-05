import json, re, sys
BAN = ['в современном мире','с одной стороны','важно отметить','играет ключевую роль','таким образом','в эпоху','неоспоримо']
wc = lambda s: len(re.findall(r'[\w\-]+', s))
errs = []
def need(c, lim, w):
    if not isinstance(c, str) or not c.strip(): errs.append(f'{w}: пусто'); return
    if wc(c) > lim: errs.append(f'{w}: {wc(c)}>{lim}: {c[:45]}')
    for b in BAN:
        if b in c.lower(): errs.append(f'{w}: штамп «{b}»')
for f in sys.argv[1:]:
    c = json.load(open(f, encoding='utf-8')); n = f.split('/')[-1]
    need(c.get('core'), 15, n+' core')
    for s in ('za', 'protiv'):
        x = c[s]; w = f'{n} {s}'
        need(x['criterion'], 15, w+' criterion'); need(x['killer'], 12, w+' killer'); need(x['image'], 15, w+' image')
        if len(x['theses']) != 3: errs.append(w+' theses!=3')
        for i, t in enumerate(x['theses']):
            for k in ('tezis', 'pochemu', 'primer'): need(t[k], 15, f'{w} theses[{i}].{k}')
        for k, cnt in (('attacks', 3), ('ask', 2)):
            if len(x[k]) != cnt: errs.append(f'{w} {k}!={cnt}')
            for i, a in enumerate(x[k]): need(a, 15, f'{w} {k}[{i}]')
        for k in ('expect', 'infokiller'):
            if len(x[k]) != 3: errs.append(f'{w} {k}!=3')
            for i, e in enumerate(x[k]): need(e['q'], 15, f'{w} {k}[{i}].q'); need(e['a'], 25, f'{w} {k}[{i}].a')
    a = c['arsenal']
    if len(a['stats']) != 2: errs.append(n+' stats!=2')
    for s in a['stats']:
        for k in ('fact', 'source', 'year', 'url', 'verified'):
            if k not in s: errs.append(n+' stat без '+k)
    for k in ('text', 'author', 'verified'):
        if k not in a['quote']: errs.append(n+' quote без '+k)
    need(a['life'], 25, n+' life')
    if len(c['traps']) != 3: errs.append(n+' traps!=3')
    for i, t in enumerate(c['traps']): need(t['problem'], 15, f'{n} traps[{i}].problem'); need(t['exit'], 25, f'{n} traps[{i}].exit')
    v = c['verdict']; need(v['why'], 40, n+' verdict.why')
    if v['winner'] not in ('za', 'protiv'): errs.append(n+' verdict.winner')
print('\n'.join(errs) if errs else 'OK', '\n', len(errs), 'замечаний')
