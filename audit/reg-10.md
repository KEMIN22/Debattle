# reg-10 — Реформа образования под ИИ-рынок (режим FACTS)
## Факты
| # | Где (путь в JSON) | Утверждение (кратко) | Вердикт | Источник (URL) | Что исправить |
|---|---|---|---|---|---|
| 1 | arsenal.stats[0]; za.theses[1].primer; protiv.theses[0].primer; traps[2] | С 1.09.2027 новый ФГОС СОО: математика, биология, химия, физика в 10–11 кл. прикладнее; навыки работы с ИИ — в метапредметных результатах | ✓ | https://xn--90aivcdt6dxbc.xn--p1ai/articles/news/s-2027-goda-uroki-matematiki-biologii-khimii-i-fiziki-stanut-bolee-prikladnymi/ (Объясняем.рф, 6.08.2026) | — |
| 2 | arsenal.stats[1]; za.theses[0].primer; traps[2] | С 1 сентября 2026 (2026/27) в школах профиль «Искусственный интеллект» | ✓ | https://expert.ru/news/v-shkolakh-s-1-sentyabrya-nachnut-izuchat-profil-iskusstvennyy-intellekt (Эксперт, 20.05.2026, Кравцов — РИА) | Уточнение: профиль — в рамках углублённого изучения информатики, не для всех. Можно добавить в primer «в углублённой информатике» |
| 3 | za.theses[2].primer; protiv.theses[1].primer | Внеурочный курс «ИИ и информационная безопасность» — со 2-й четверти 2026/27 | ✓ | https://science.mail.ru/news/56144-minprosvesheniya-dobavilo-kurs-po-ii-i-kiberbezopasnosti/ (5.09.2026, со ссылкой на РБК/Интерфакс); https://www.postupashkin.ru/news/vneurochnye-kursy-vtoraya-chetvert-2026 | Для 5–11 классов (можно добавить) |
| 4 | za.infokiller[1].a; traps[0].exit; verdict.why; za.infokiller[2].a | «Обязательных уроков ИИ нет»: профиль, внеурочка, навыки в стандарте | ⚠ | https://science.mail.ru/news/56144-minprosvesheniya-dobavilo-kurs-po-ii-i-kiberbezopasnosti/ ; https://www.postupashkin.ru/news/vneurochnye-kursy-vtoraya-chetvert-2026 | Уроков ИИ в сетке нет — верно. Но РБК/Mail пишут «перечень обязательных курсов внеурочки» (курс ИИ в нём), а письмо Минпросвещения рекомендательное, объём решает школа. Формулировка: «Обязательных уроков ИИ нет; внеурочный курс рекомендован, объём решает школа» |
| 5 | protiv.expect[2].a | Стандарт 2027 «закрепляет направление для всей школы» | ⚠ | https://xn--90aivcdt6dxbc.xn--p1ai/articles/news/s-2027-goda-uroki-matematiki-biologii-khimii-i-fiziki-stanut-bolee-prikladnymi/ | Новый ФГОС — среднего общего образования (10–11 кл.), не всей школы. Заменить «для всей школы» → «для всех 10–11 классов» |

Без фактов (рассуждения, не проверялись): za/protiv pochemu, attacks, ask, infokiller «данных не назову» — выдуманных цифр нет. arsenal.quote пуст (verified:false) — ок.

- Рискованно вслух: «обязательных уроков ИИ нет» — соперник может процитировать РБК про «обязательный перечень внеурочки»; говорить «уроков в сетке нет, курс внеурочный и рекомендованный».

## Итого: ошибок 2 (✗ 0, ⚠ 2, ? 0)

## Исправления (fixer)
| Путь в JSON | Было (кратко) | Стало (кратко) | Источник (URL) |
|---|---|---|---|
| za.theses[0].primer | «В школах с 1 сентября 2026 вводят профиль ИИ» | «…в углублённой информатике вводят профиль ИИ» | https://expert.ru/news/v-shkolakh-s-1-sentyabrya-nachnut-izuchat-profil-iskusstvennyy-intellekt |
| za.infokiller[1].a | «Обязательных уроков ИИ в этих шагах нет» | «Уроков ИИ в сетке нет; профиль по выбору, курс рекомендован, объём решает школа» | https://science.mail.ru/news/56144-minprosvesheniya-dobavilo-kurs-po-ii-i-kiberbezopasnosti/ |
| traps[0].exit | «обязательных уроков нет» | «уроков ИИ в сетке нет; курс внеурочный и рекомендованный, объём решает школа» | https://www.postupashkin.ru/news/vneurochnye-kursy-vtoraya-chetvert-2026 |
| verdict.why | «внеурочка… без обязательных уроков» | «рекомендованная внеурочка… без уроков ИИ в сетке» | https://science.mail.ru/news/56144-minprosvesheniya-dobavilo-kurs-po-ii-i-kiberbezopasnosti/ |
| protiv.expect[2].a | «закрепляет направление для всей школы» | «…для всех 10–11 классов» | https://xn--90aivcdt6dxbc.xn--p1ai/articles/news/s-2027-goda-uroki-matematiki-biologii-khimii-i-fiziki-stanut-bolee-prikladnymi/ |

## Повторная проверка
| Путь в JSON | Стало (fixer) | Вердикт | Источник (URL) | Что сделано |
|---|---|---|---|---|
| za.theses[0].primer | «в углублённой информатике вводят профиль ИИ» | ✓ | https://expert.ru/news/v-shkolakh-s-1-sentyabrya-nachnut-izuchat-profil-iskusstvennyy-intellekt («в рамках углубленного курса информатики», с 2026/27) | — |
| za.infokiller[1].a | «профиль по выбору, курс рекомендован, объём решает школа» | ⚠ | https://science.mail.ru/news/56144-minprosvesheniya-dobavilo-kurs-po-ii-i-kiberbezopasnosti/ («перечень обязательных курсов внеурочной деятельности»); https://mel.fm/novosti/4153967-v-rossyskikh-shkolakh-so-vtoroy-chetverti-202627-goda-poyavitsya-novy-kurs («во всех школах», «не предмет из расписания с оценками, но скорее всего обязательный») | «рекомендован, объём решает школа» не подтверждается (postupashkin.ru не открылся). Исправлено: «Профиль — в углублённой информатике, курс ИИ внеурочный, без оценок.» |
| traps[0].exit | «курс внеурочный и рекомендованный, объём решает школа» | ⚠ | те же | Исправлено: «уроков ИИ в сетке нет. Курс ИИ внеурочный, без оценок.» |
| verdict.why | «рекомендованная внеурочка… без уроков ИИ в сетке» | ⚠ | те же | «рекомендованная внеурочка» → «внеурочный курс без оценок» |
| protiv.expect[2].a | «для всех 10–11 классов» | ✓ | https://xn--90aivcdt6dxbc.xn--p1ai/articles/news/s-2027-goda-uroki-matematiki-biologii-khimii-i-fiziki-stanut-bolee-prikladnymi/ («новый ФГОС среднего общего образования… в 10–11-х классах», с 1.09.2027) | — |

Рискованно вслух: не говорить «курс необязательный» — Mail/РБК: курс в перечне обязательных курсов внеурочки. Безопасно: «уроков ИИ в расписании нет, курс внеурочный, без оценок».
validate_card.py: OK, 0 замечаний.

ГОТОВО
- что изменилось: исходный аудит — 2 ⚠ (обязательность курса ИИ, «вся школа» вместо 10–11 кл.); fixer уточнил профиль (углублённая информатика) и стандарт (10–11 кл.) — подтверждено.
- Мои правки: «курс рекомендован, объём решает школа» источниками не подтверждается (Mail/РБК: перечень обязательных курсов внеурочки) → в za.infokiller[1].a, traps[0].exit, verdict.why заменено на «курс ИИ внеурочный, без оценок».
