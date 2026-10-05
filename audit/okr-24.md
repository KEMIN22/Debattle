# okr-24 — Фитнес-трекеры: дисциплина или одержимость

EPMC = Europe PMC REST (тот же PMID; pubmed.ncbi.nlm.nih.gov не открылся — «Cookies must be enabled»).

## Факты
| # | Где (путь в JSON) | Утверждение (кратко) | Вердикт | Источник (URL) | Что исправить |
|---|---|---|---|---|---|
| 1 | arsenal.stats[0]; za.theses[0].tezis; protiv.attacks[1] | Ferguson 2022, Lancet Digit Health: ~1800 шагов/день, 39 обзоров, 163 992 участника | ✓ | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:35868813&resultType=core&format=json | — (1800 пересчитано из SMD 0,3–0,6, «около» верно) |
| 2 | arsenal.stats[1]; protiv.theses[2].primer; za/protiv.infokiller | Ли 2019, JAMA Intern Med: женщины, ср. возраст 72, плато ~7500 | ✓ устарело? | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:31141585&resultType=core&format=json | Свежее: Ding 2025, Lancet Public Health — 7000 vs 2000 шагов: риск смерти ниже на 47% (HR 0,53), перегиб 5000–7000. https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE:%22daily%20steps%22%20AND%20AUTH:Ding%20AND%20PUB_YEAR:2025&resultType=core&format=json |
| 3 | za.theses[0].primer; za.infokiller[1].a | Ли 2019: 4400 vs 2700 шагов — смертность ниже; женщины 62+ | ✓ | то же + PDF карточки (range 62–101 лет) https://whish.stanford.edu/wp-content/uploads/2019/10/Step-Volume-Intensity-Mortality_JAMA-IntMedicine-2019-.pdf | — |
| 4 | za.theses[1].pochemu | Палюх 2022: <60 лет до 8000–10 000, 60+ до 6000–8000 | ✓ | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:35247352&resultType=core&format=json | — |
| 5 | za.theses[1].primer; za.expect[0].a; za.infokiller[2].a; protiv.attacks[2] | watchOS 11: кольца ставят на паузу, серия сохраняется | ✓ | https://www.apple.com/newsroom/2024/06/watchos-11-brings-powerful-health-and-fitness-insights/ | Точнее: «паузу ставят кольцам, серия наград не сгорает». Apple называет отдых, травму, выходной (не «поездку») |
| 6 | za.theses[2].pochemu; za.expect[2].a | Лалли: в среднем ~66 дней, разброс большой (18–254) | ✓ (66 — вторичный) | https://api.crossref.org/works/10.1002/ejsp.674 (18–254 дн.); https://www.spring.org.uk/?p=107834 (66 дн.) | 66 — медиана; «около 66 дней» допустимо |
| 7 | za.theses[2].primer; za.infokiller[2].a | Лалли 2010: один пропуск существенно не влиял | ✓ | https://api.crossref.org/works/10.1002/ejsp.674 | — (онлайн 2009, печать 2010 — ок) |
| 8 | protiv.theses[0].primer; protiv.attacks[0]; za.attacks[0] | Финкельштейн 2016 (TRIPPA, Сингапур): после отмены денег эффект не удержался | ✓ устарело? | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:27717766&resultType=core&format=json | Верно только про денежную группу. В той же работе группа «только Fitbit» через 12 мес. +37 мин MVPA/нед к контролю — см. Логику |
| 9 | protiv.theses[1].primer; za.infokiller[0].a | Барон 2017, JCSM: ортосомния, три случая | ✓ | https://pmc.ncbi.nlm.nih.gov/articles/PMC5263088/ | — |
| 10 | za.infokiller[0].a «Массовых данных нет»; za.ask[1]; za.attacks[1]; protiv.expect[0].a; protiv.infokiller[1].a | Доли ортосомнии никто не знает | ⚠ | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=orthosomnia%20AND%20JOURNAL:%22Brain%20Sci%22&resultType=core&format=json | Jahrami 2024, Brain Sci, n=523: ортосомния у 3,0–14,0% (по строгости критерия), 35,8% пользуются трекерами сна. ЗА: «данные малые и разные: 3–14% на 523 человек». ПРОТИВ может назвать цифру |
| 11 | protiv.theses[2].pochemu/primer | Манпо-кэй, 1965; «число придумал маркетинг» | ⚠ | Ли 2019 PDF (см. #3): «likely derives from the trade name… Manpo-kei» | «Число, вероятно, из рекламы шагомера 1965 года» — у Ли «вероятно» |
| 12 | protiv.expect[1].a; protiv.infokiller[1].a; traps[2] | Фитнес-трекинг связан с симптомами РПП у студентов, причина не доказана | ✓ устарело? | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE:%22fitness%20tracking%20technology%22%20AND%20AUTH:Simpson&resultType=core&format=json | Назвать: Симпсон, Маццео 2017, 493 студента |
| 13 | protiv.infokiller[2].a | IDEA (JAMA 2016): с трекером похудели меньше | ✓ устарело? | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:27654602&resultType=core&format=json | — (факт верен, но ответ не про сон — см. Логику) |
| 14 | arsenal.quote | «Когда мера становится целью…» — Стратерн 1997, закон Гудхарта 1975 | ✓ | https://en.wikipedia.org/wiki/Goodhart%27s_law (цитирует статью Strathern, European Review 1997) | Точнее: Стратерн формулирует закон вслед за Хоскином |

## Логика
- Слабый тезис ЗА: №3 («каркас, пока привычка не станет автоматической»). Лалли не про трекеры, а тезис сам признаёт критерий ПРОТИВ. Замена: «Даже бросив часы, люди двигались больше». Почему: TRIPPA, 12 мес.: группа «только Fitbit» +37 мин активности/нед к контролю. Пример: к году трекером пользовались ~10% (Healio 2016). https://www.healio.com/news/endocrinology/20161006/activity-trackers-fail-to-improve-health-outcomes-with-or-without-incentives Оговорка: это «меньше спад», здоровье не улучшилось.
- Слабый тезис ПРОТИВ: №1. Пример про деньги, а не про трекер; та же TRIPPA показывает плюс у группы «только трекер» через год. Замена: «Трекер бросают, а здоровье не меняется». Пример: TRIPPA — к году трекер носили ~10%, улучшений здоровья нет ни в одной группе (Healio 2016, EPMC 27717766). Или IDEA: с трекером похудели меньше.
- Дыра для инфокиллера: ЗА — «массовых данных нет» по ортосомнии ломается Jahrami 2024 (3–14%). ПРОТИВ — Сингапур бьёт по своим же: группа «только Fitbit» через год активнее контроля. Ещё ЗА: Ли/Палюх/Ding — наблюдения, связь, не причина; ПРОТИВ это скажет.
- Атаки мимо: обе тройки атак бьют в тезисы по номерам (ЗА 1→П1, 2→П2, 3→П3; ПРОТИВ 1→З3, 2→З1, 3→З2). Мимо — protiv.infokiller[2]: вопрос про сон, ответ про похудение (IDEA). Заменить: «Сон — не шаги: у тревожных данные трекера кормят ортосомнию, 3–14% (Jahrami 2024)».
- Рискованно вслух: «число придумал маркетинг» без «вероятно»; «ему нужны врач» (za.expect[1]) — звучит как диагноз тревожным; trap[2] про подростков с РПП — говорить осторожно, без медицинских советов; «4400 шагов снижали смертность» — говорить «связаны с меньшей смертностью».

## Итого: ошибок 2 (✗ 0, ⚠ 2, ? 0)

## Исправления (fixer)
| Путь в JSON | Было (кратко) | Стало (кратко) | Источник (URL) |
|---|---|---|---|
| za.infokiller[0].a; za.attacks[1]; za.ask[1] | «Массовых данных нет», «долю не знаете» | Опрос 2024, 523 чел.: ортосомния у 3–14% — меньшинство | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=orthosomnia%20AND%20JOURNAL:%22Brain%20Sci%22&resultType=core&format=json (Jahrami 2024, PMID 39595886) |
| protiv.expect[0].a; protiv.infokiller[1].a; traps[1].exit | «Долю не знаю», «массовых цифр не назову» | 3–14% в опросе 2024 | то же |
| protiv.infokiller[2].a | Ответ про похудение (IDEA) на вопрос о сне | Данные сна кормят ортосомнию: 3–14% (Jahrami 2024) | то же |
| protiv.theses[2].pochemu/primer | «Число придумал маркетинг» | «Число, вероятно, из рекламы шагомера»; «Манпо-кэй», 1965 | https://whish.stanford.edu/wp-content/uploads/2019/10/Step-Volume-Intensity-Mortality_JAMA-IntMedicine-2019-.pdf |
| za.attacks[2]; za.infokiller[1].a | «10 000 — реклама» | «10 000, вероятно, из рекламы» | то же |
| za.theses[0].primer; za.infokiller[1].a | 4400 шагов «снижали смертность» | «связаны с меньшей смертностью» / «смертность ниже» | то же |
| za.theses[1].primer; za.infokiller[2].a | Паузу ставят серии: болезнь, поездка | Кольца ставят на паузу, серия наград не сгорает | https://www.apple.com/newsroom/2024/06/watchos-11-brings-powerful-health-and-fitness-insights/ |
| za.theses[2] (слабый) | Каркас привычки, Лалли 66 дней | Даже сняв трекер, двигаются больше: к году носили 10%, +37 мин/нед к контролю | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:27717766&resultType=core&format=json ; https://www.healio.com/news/endocrinology/20161006/activity-trackers-fail-to-improve-health-outcomes-with-or-without-incentives |
| za.expect[2].a | Лалли: 66 дней | Сингапур: 10% носили, +37 мин/нед | то же |
| protiv.theses[0] (слабый) | После отмены денег эффект не удержался | Трекер бросают (к году 10%), здоровье не меняется ни в одной группе | то же |
| protiv.attacks[0]; za.attacks[0] | Атаки на старые тезисы (деньги / Лалли) | +37 мин — меньший спад, здоровье не улучшилось; здоровье не сдвинул никто, но +37 мин | то же |
| protiv.expect[1].a | Связь с РПП у студентов | Назван источник: Симпсон и Маццео 2017, 493 студента | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE:%22fitness%20tracking%20technology%22%20AND%20AUTH:Simpson&resultType=core&format=json |
| za.expect[1].a | «Ему нужны врач и пауза» | «Ему помогут пауза и отключённые цели» | — (тон) |
| traps[2].exit | «Цели убирают родитель и врач» | «Уязвимым подсчёт может вредить, цели лучше отключить» | — (тон) |
| arsenal.stats[1] | Ли 2019, плато ~7500 (устарело) | Ding 2025: 7000 vs 2000 шагов — риск смерти ниже на 47%, перегиб 5000–7000 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:40713949&resultType=core&format=json (DOI 10.1016/S2468-2667(25)00164-1) |
| arsenal.quote.author | Стратерн 1997, Гудхарт 1975 | Стратерн (1997) вслед за Хоскином | https://en.wikipedia.org/wiki/Goodhart%27s_law |

Валидатор: 0 замечаний.
