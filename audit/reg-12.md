# reg-12 — Возрастной барьер в соцсетях
Режим: FACTS. Дата проверки: 2026-10-05.

## Факты
| # | Где (путь в JSON) | Утверждение (кратко) | Вердикт | Источник (URL) | Что исправить |
|---|---|---|---|---|---|
| 1 | arsenal.stats[0]; za.theses[0].primer | Австралия: запрет до 16 лет, с 10.12.2025, штраф платформам до 49,5 млн AUD | ✓ (вторичный, со ссылкой на Bloomberg) | https://expert.ru/news/avstraliya-stala-pervoy-stranoy-s-zapretom-podrostkam-polzovatsya-sotssetyami | URL карточки gazeta.ru не открылся (пустой ответ) — заменить url на expert.ru. Уточнение для устной речи: запрет на аккаунты, смотреть без входа можно |
| 2 | za.infokiller[0].a; traps[0] | Закон действует с 10 декабря 2025, итогов пока нет | ✓ (дата) | https://expert.ru/news/avstraliya-stala-pervoy-stranoy-s-zapretom-podrostkam-polzovatsya-sotssetyami | — |
| 3 | protiv.expect[1].a; protiv.attacks[0] | Австралия штрафует платформы, не детей | ✓ | https://expert.ru/news/avstraliya-stala-pervoy-stranoy-s-zapretom-podrostkam-polzovatsya-sotssetyami ; https://reclaimthenet.org/bill/au-social-media-minimum-age | — |
| 4 | arsenal.stats[1]; za.infokiller[2].a | Депутат Свинцов предложил запрет соцсетей до 14 лет и верификацию через Госуслуги (дек. 2025) | ✓ (вторичный: mentoday со ссылкой на НСН, 22.12.2025) | https://www.mentoday.ru/life/news/22-12-2025/blokirovki-pokajutsya-melochyu-v-gosdume-anonsirovali-jestochaishie-zaprety-dlya-rossiyan-v-socsetyah/ | Это заявление депутата, не законопроект — в карточке так и указано |
| 5 | protiv.theses[0].primer | «Россия, декабрь 2025: предложили обязательную верификацию через Госуслуги» | ⚠ | тот же mentoday | Звучит как госинициатива; это слова одного депутата. Заменить: «Декабрь 2025: депутат Свинцов предложил верификацию аккаунтов через Госуслуги.» |
| 6 | protiv.theses[1].primer | Свинцов признал: дети регистрируются на старших родственников | ✓ | тот же mentoday | — |
| 7 | za.theses[1].primer; za.ask[1] | ГК РФ ст. 28: сделки за малолетних до 14 лет совершают родители | ✓ (кроме мелких бытовых сделок с 6 лет, п. 2) | https://www.zakonrf.info/gk/28/ | — |
| 8 | za.theses[2].primer; za.attacks[1] | Продажа алкоголя до 18 запрещена и штрафуется | ✓ (КоАП ст. 14.16 ч. 2.1) | https://www.zakonrf.info/koap/14.16/ | — |

arsenal.quote пуста (verified:false) — проверять нечего.

Рискованно вслух: не переходить на личность депутата Свинцова (критиковать схему, не человека); называя Instagram/Facebook, помнить, что Meta признана в РФ экстремистской.

## Итого: ошибок 1 (✗ 0, ⚠ 1, ? 0)

## Исправления (fixer)
| Путь в JSON | Было (кратко) | Стало (кратко) | Источник (URL) |
|---|---|---|---|
| arsenal.stats[0].url | gazeta.ru (не открывается) | expert.ru | https://expert.ru/news/avstraliya-stala-pervoy-stranoy-s-zapretom-podrostkam-polzovatsya-sotssetyami |
| arsenal.stats[0].source | Газета.Ru | Эксперт со ссылкой на Bloomberg (вторичный источник) | https://expert.ru/news/avstraliya-stala-pervoy-stranoy-s-zapretom-podrostkam-polzovatsya-sotssetyami |
| arsenal.stats[0].fact | «запретила соцсети детям до 16» | «запретила детям до 16 заводить аккаунты» (смотреть без входа можно) | https://expert.ru/news/avstraliya-stala-pervoy-stranoy-s-zapretom-podrostkam-polzovatsya-sotssetyami |
| protiv.theses[0].primer | «Россия: предложили верификацию через Госуслуги» | «Депутат Свинцов предложил верификацию через Госуслуги» | https://www.mentoday.ru/life/news/22-12-2025/blokirovki-pokajutsya-melochyu-v-gosdume-anonsirovali-jestochaishie-zaprety-dlya-rossiyan-v-socsetyah/ |

## Повторная проверка
| Путь в JSON | Стало (кратко) | Вердикт | Источник (URL) |
|---|---|---|---|
| arsenal.stats[0].url | expert.ru | ✓ открывается (HTTP 200), новость от 10 дек 2025 | https://expert.ru/news/avstraliya-stala-pervoy-stranoy-s-zapretom-podrostkam-polzovatsya-sotssetyami |
| arsenal.stats[0].source | Эксперт со ссылкой на Bloomberg, в силе с 10.12.2025 | ✓ «передает Bloomberg. Запрет вступил в силу 10 декабря» | то же |
| arsenal.stats[0].fact | до 16 лет нельзя заводить аккаунты; штраф до 49,5 млн AUD | ✓ «предотвратить создание учетных записей лицами младше 16 лет… штрафы до 49,5 млн австралийских долларов»; смотреть без входа можно | то же |
| protiv.theses[0].primer | Декабрь 2025: депутат Свинцов предложил верификацию аккаунтов через Госуслуги | ✓ «обязательная верификация всех аккаунтов через портал „Госуслуги“», 22.12.2025 (вторичный, со ссылкой на НСН) | https://www.mentoday.ru/life/news/22-12-2025/blokirovki-pokajutsya-melochyu-v-gosdume-anonsirovali-jestochaishie-zaprety-dlya-rossiyan-v-socsetyah/ |

Правок аудитора нет. validate_card.py: OK, 0 замечаний.

ГОТОВО
- что изменилось: ссылка на Австралию заменена с нерабочей gazeta.ru на expert.ru (вторичный, Bloomberg), факт уточнён: под запретом аккаунты до 16, а не соцсети вообще; primer ПРОТИВ[0] теперь прямо называет это предложением депутата Свинцова, а не госинициативой. Остальные факты (ГК ст. 28, КоАП 14.16, Свинцов про 14 лет) подтверждены в исходном аудите.
