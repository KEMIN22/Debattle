"""python3 work/A/make_brief.py <группа> <id> [<id>...] -> work/A/<группа>/brief.md (только нужный кусок данных)"""
import json, os, re, sys
grp, ids = sys.argv[1], sys.argv[2:]
d = json.load(open('docs/data/topics.json', encoding='utf-8'))
T = {t['id']: t for t in d['topics']}; cl = {c['id']: c['name'] for c in d['clusters']}
spec = open('spec/SPEC.md', encoding='utf-8').read()
sec = lambda n: re.search(r'## ' + n + r'.*?\n(.*?)(?=\n## |\Z)', spec, re.S).group(0)
b = ("# БРИФ: спор по группе тем\n\nКонтекст: команда из 3 школьников/студентов на турнире дебатов «Твой Ход × Дебаттл» "
     "(1 мин подготовки, 2 мин речь, вопросы 15 сек, свободное оппонирование 3 мин, эксперт-«инфокиллер»). "
     "Карточку не читают вслух — по ней вспоминают. Всё на русском.\n\n## Темы (формулировки дословно)\n")
for i in ids:
    t = T[i]
    b += f"- {i} (кластер {t['cluster']}: {cl[t['cluster']]}): {t['title']}" + (f" [партнёр: {t['partner']}]" if t.get('partner') else '') + "\n"
b += "\n" + sec('СТИЛЬ') + "\n\n" + sec('КАРТОЧКА ТЕМЫ') + """
## Точные имена полей для одной стороны (side) одной темы
{"criterion":"","theses":[{"tezis":"","pochemu":"","primer":""} x3],"killer":"до 12 слов","image":"","attacks":["удар по тезису соперника" x3],"ask":["вопрос-ловушка до 15 слов" x2],"expect":[{"q":"неудобный вопрос нам","a":"ответ до 25 слов"} x3],"infokiller":[{"q":"провокация эксперта","a":"ответ до 25 слов"} x3]}
Общее для темы: "arsenal_candidates": {"stats":[{"fact":"","source":"","year":0,"url":"","verified":false} x2],"quote":{"text":"","author":"","verified":false},"life":"подсказка, какой личный опыт вспомнить, НЕ выдумывать историю"} и "traps":[{"problem":"что может пойти не так","exit":"как выйти"} x3].
Любая строка до 15 слов (ответы до 25). Пример должен ДОКАЗЫВАТЬ тезис, а не работать на соперника. Не повторяй один сюжет (мошенники, камеры, ленты соцсетей) в разных темах и тезисах. Статистику, номера статей законов и цитаты ставь только если уверен на 100%; verified всегда false (проверка — позже). Нет уверенности — не пиши цифру/статью, дай надёжный факт без цифры.
"""
os.makedirs(f'work/A/{grp}', exist_ok=True)
open(f'work/A/{grp}/brief.md', 'w', encoding='utf-8').write(b)
print(grp, ids, len(b.split()), 'слов')
