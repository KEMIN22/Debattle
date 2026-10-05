# reg-02 — Удержание молодых в бигтехе: смысл и культура или деньги и рост

## Факты
| # | Где (путь в JSON) | Утверждение (кратко) | Вердикт | Источник (URL) | Что исправить |
|---|---|---|---|---|---|
| 1 | arsenal.stats[0]; protiv.theses[2].primer | ВОЗ, 2019: выгорание в МКБ-11 как профессиональный феномен, итог хронического стресса на работе | ✓ | https://www.who.int/news/item/28-05-2019-burn-out-an-occupational-phenomenon-international-classification-of-diseases (28.05.2019) | — (уточнение: «не классифицируется как болезнь») |
| 2 | arsenal.quote | «a syndrome conceptualized as resulting from chronic workplace stress that has not been successfully managed» | ✓ | там же, дословно | — |
| 3 | za.attacks[2] | «ВОЗ связывает выгорание со стрессом на работе, а не с размером оклада» | ⚠ | там же: про оклад у ВОЗ ни слова | «а не с окладом» — это вывод команды, не ВОЗ. Сказать: «ВОЗ: выгорание — от неуправляемого хронического стресса на работе» |
| 4 | arsenal.stats[1]; protiv.theses[0].primer | ИТ-ипотека под 5% запущена в 2022 | ⚠ устарело | https://habr.com/ru/post/664182 (4.05.2022, вторичный); https://content.renins.ru/ipoteka/it-ipoteka-2026/ | Факт 2022 верен (постановление № 805 от 30.04.2022), но с лета 2024 ставка до 6%, лимит 9 млн, без Москвы и Петербурга, программа до 2030. Не говорить «сейчас 5%»; добавить «с 2024 — до 6%» |
| 5 | za.theses[0].primer, pochemu | Герцберг, 1959: достижения мотивируют, зарплата лишь снимает недовольство | ✓ | https://www.businessballs.com/improving-workplace-performance/frederick-herzberg-motivation-theory/ (1959, ~200 инженеров и бухгалтеров); https://www.simplypsychology.org/herzbergs-two-factor-theory.html | — НО у Герцберга «Advancement» (повышение, карьерный рост) — тоже мотиватор, не гигиена (simplypsychology) |
| 6 | za.infokiller[1].q/a | «Герцберг писал про заводы» | ✓ (ответ) | businessballs, см. #5 | Усилить ответ: исследование 1959 года — опрос около 200 инженеров и бухгалтеров, не заводских рабочих |
| 7 | za.infokiller[1].a | Теория самодетерминации: автономия, компетентность, связь с людьми | ✓ | https://selfdeterminationtheory.org/theory/ | — |
| 8 | za.theses[2].primer | Google Project Aristotle: главное — психологическая безопасность | ✓ | https://rework.withgoogle.com/intl/en/guides/understand-team-effectiveness (опубликовано 2016; «In order of importance: Psychological safety») | — |
| 9 | za.theses[1].primer | Нацпроект «Экономика данных» с 2025: ИИ, цифровые платформы, кадры | ✓ | https://3dnews.ru/1118935/predstavlen-natsproekt-ekonomika-dannih-s-byudgetom-1-trillion-rubley-na-bligayshie-pyat-let/amp (27.02.2025: ФП «Искусственный интеллект», «Цифровые платформы…», «Кадры для цифровой трансформации»); https://www.comnews.ru/content/238000/2025-02-27/2025-w09/1007/nacproekt-ekonomika-dannykh-raskryl-plany-cifrovizacii-rossii-gryaduschie-pyat-let (2025–2030, 1 трлн руб.) | — |
| 10 | protiv.theses[1].primer | Грейды junior/middle/senior с вилками дохода | — (общая практика, не проверялось) | — | Не называть конкретных вилок |

Рискованно вслух: ЗА опирается на Герцберга, а у него карьерный рост — мотиватор; ПРОТИВ может развернуть: «по вашему же Герцбергу перспективы — мотиватор». ЗА: признать и делать упор на «зарплата — гигиена».

## Итого: ошибок 2 (✗ 0, ⚠ 2, ? 0)

## Исправления (fixer)
| Путь в JSON | Было (кратко) | Стало (кратко) | Источник (URL) |
|---|---|---|---|
| za.attacks[2] | ВОЗ связывает выгорание со стрессом, «а не с размером оклада» | ВОЗ: выгорание — от неуправляемого хронического стресса на работе; вывод про команду — отдельно, от нас | https://www.who.int/news/item/28-05-2019-burn-out-an-occupational-phenomenon-international-classification-of-diseases |
| arsenal.stats[1] | ИТ-ипотека под 5% запущена в 2022 (Хабр) | С 2022; в 2026-м — до 6%, до 9 млн руб., без Москвы и Петербурга; year 2026 | https://realty.rbc.ru/news/69b2cf1b9a794758af2acf56 (2026, Минцифры); https://www.pnp.ru/social/it-ipoteku-prodlili-do-2030-goda-i-povysili-predelnuyu-stavku-po-ney-do-6.html (с августа 2024: 6%, 9 млн, до 2030) |
| protiv.theses[0].primer | ИТ-ипотека (с 2022) | ИТ-ипотека (с 2022, с 2024 — до 6%) | те же |
| za.infokiller[1].a | Только теория самодетерминации | + Герцберг опрашивал около 200 инженеров и бухгалтеров, не заводских | https://www.businessballs.com/improving-workplace-performance/frederick-herzberg-motivation-theory/ |
| arsenal.quote.url | нет | добавлен URL ВОЗ | https://www.who.int/news/item/28-05-2019-burn-out-an-occupational-phenomenon-international-classification-of-diseases |

## Повторная проверка
| Путь в JSON | Новое утверждение | Вердикт | Источник (URL) | Действие |
|---|---|---|---|---|
| za.attacks[2] | ВОЗ: выгорание — от неуправляемого хронического стресса на работе; про команду — наш вывод | ✓ | https://www.who.int/news/item/28-05-2019-burn-out-an-occupational-phenomenon-international-classification-of-diseases | — |
| arsenal.stats[1] | С 2022; в 2026 — до 6%, до 9 млн, без Москвы и Петербурга | ⚠→✓ | https://finance.mail.ru/article/usloviya-it-ipoteki-68259356/ (26.01.2026: 6%, 9 млн, не Москва/СПб); https://www.pnp.ru/social/it-ipoteku-prodlili-do-2030-goda-i-povysili-predelnuyu-stavku-po-ney-do-6.html (с 08.2024, запуск 2022) | На странице РБК только про 6% для «Сколково», нет 9 млн и Москвы/СПб — URL и source заменены на Mail.ru |
| protiv.theses[0].primer | ИТ-ипотека (с 2022, с 2024 — до 6%) | ✓ | pnp.ru (см. выше) | — |
| za.infokiller[1].a | Герцберг опрашивал около 200 инженеров и бухгалтеров | ✓ | https://www.businessballs.com/improving-workplace-performance/frederick-herzberg-motivation-theory/ («1959 research … among 200 engineers and accountants») | — |
| arsenal.quote.url | URL ВОЗ, цитата дословно | ✓ | URL ВОЗ выше | — |

validate_card.py: OK, 0 замечаний.

ГОТОВО
- что изменилось: za.attacks[2] — убрано приписанное ВОЗ «а не с окладом»; ИТ-ипотека обновлена до условий 2026 (до 6%, 9 млн, без Москвы/СПб), источник stats[1] заменён на Mail.ru 26.01.2026 (РБК не содержал 9 млн и Москву/СПб).
- В ответ на «Герцберг про заводы» добавлено: опрос ~200 инженеров и бухгалтеров; у цитаты ВОЗ появился URL. Остальные факты карточки ✓.
