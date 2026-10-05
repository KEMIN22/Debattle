# Factcheck okr-01, okr-07

Ограничение: WebFetch блокируется прокси для всех доменов (consultant, garant, un.org, aei, kremlin, pravo, tass и др.). Проверка шла только по выдаче WebSearch (цитаты и URL из результатов). Ссылки взяты из выдачи, напрямую страницы не открывались.

| Карточка | Пункт | Результат | Ссылка |
|---|---|---|---|
| okr-01 | stats[0] ст. 159 УК | подтверждено (хищение чужого имущества или права на него путём обмана или злоупотребления доверием), verified:true, url заменён на страницу ст. 159 | https://base.garant.ru/10108000/7f1391d5bfd3db19990900228372be85/ |
| okr-01 | stats[1] Ticketmaster / Eras Tour | ЗАМЕНЁН. Ticketmaster действительно заявил про рекордные запросы, но объяснил их ботами и людьми без кодов, то есть заявление не про «спрос, а не обман». Заменено на КоАП РФ ст. 14.4.3 (ФЗ от 27.12.2019 № 493-ФЗ): штраф за продажу билетов на спектакли и в музеи выше номинала, однократная перепродажа личного билета исключена. verified:true | https://www.consultant.ru/document/cons_doc_LAW_34661/1c8e7943d9564838919f0437a6fd46520a4b0aa9/ |
| okr-01 | quote Соуэлл | подтверждено: «There are no solutions, there are only trade-offs» (AEI, IPI, X), перевод «компромиссы» допустим. Первоисточник (книга) не установлен, поэтому ссылка на AEI. verified:true | https://www.aei.org/carpe-diem/video-thomas-sowells-most-profound-economic-insight-and-his-three-questions-for-the-left/ |
| okr-01 | тезисы: ст. 159, Авито/чаты, Fan ID, Пушкинская карта | подтверждено выдачей: дубли объявлений на Авито/Юле; Fan ID привязан к человеку (билет можно передать другому владельцу Fan ID); билет по Пушкинской карте именной по постановлению Правительства. Правок нет | aif.ru/society/law/kak_mozhno_pozhalovatsya_na_perekupshchikov_biletov; premierliga.ru/about/fan-card/; mariinsky.ru/playbill/credit_pushkin/ |
| okr-01 | trap/verdict «разовая перепродажа по номиналу законна» | согласуется с исключением в ст. 14.4.3 КоАП | см. выше |
| okr-07 | stats[0] Конвенция о правах ребёнка, ст. 16 | подтверждено дословно («произвольного или незаконного вмешательства в… тайну корреспонденции»), verified:true | https://www.un.org/ru/documents/decl_conv/conventions/childcon.shtml |
| okr-07 | stats[1] ст. 39 УК | подтверждено (не преступление, если опасность нельзя устранить иными средствами и нет превышения), verified:true | https://www.consultant.ru/document/cons_doc_LAW_10699/68eac2d2c39341d4a45238bffce4ea253949a106/ |
| okr-07 | quote ст. 3 Конвенции | ИСПРАВЛЕНА формулировка по официальному тексту: «первоочередное внимание уделяется наилучшему обеспечению интересов ребенка» (раньше был перифраз «близко к тексту»). verified:true | https://www.un.org/ru/documents/decl_conv/conventions/childcon.shtml |
| okr-07 | ст. 63, 64, 65 СК | подтверждено: 63 воспитание, 64 родители — законные представители и защита прав детей, 65 осуществление родительских прав. Правок нет | https://www.consultant.ru/document/cons_doc_LAW_8982/2236d37faf59dafdc4b2bc53c6b05841fe616ee9/ |
| okr-07 | ст. 69 СК | подтверждено (лишение родительских прав судом) | https://sudact.ru/law/sk-rf/razdel-iv/glava-12_1/statia-69/ |
| okr-07 | ст. 23 Конституции | подтверждено: тайна переписки, ограничение по решению суда | https://constrf.ru/razdel-1/glava-2/st-23-krf |
| okr-07 | поджоги подростками по заданиям из Telegram (2024–2025) | подтверждено: Чебоксары, Нефтеюганск, Санкт-Петербург (авто); Барабинск, Приморье, Бийск (релейные шкафы) | https://ria.ru/20250603/neftejugansk-2020586573.html; https://www.nsk.om1.ru/news/society/406688-tri_podrostka_podozhgli_relejjnyjj_shkaf_v_barabinske_po_ukazaniju_kuratora_iz_telegram/ |

Итого: arsenal verified:true 7 из 7 (okr-01: 2 stats + quote, okr-07: 2 stats + quote). Заменено: 1 stat (Ticketmaster) и формулировка цитаты ст. 3. Осталось false: 0. Валидатор: OK на обоих файлах.
