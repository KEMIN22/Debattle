// Смоук-тест offline.html в мобильном viewport
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const p = await (await b.newContext({ viewport: { width: 390, height: 800 }, hasTouch: true })).newPage();
  const errs = []; p.on('pageerror', e => errs.push(e.message)); p.on('console', m => m.type() === 'error' && errs.push(m.text()));
  await p.goto('file:///home/user/Debattle/docs/offline.html');
  const log = (k, v) => console.log(k, v);
  log('topics okr', await p.locator('.topic').count());
  await p.click('.tab:nth-child(2)'); await p.waitForTimeout(200); log('topics reg', await p.locator('.topic').count());
  await p.fill('#q', '7'); log('search 7', await p.locator('.topic').count());
  await p.fill('#q', 'vpn'); await p.fill('#q', 'родител'); log('search родител', await p.locator('.topic').count());
  await p.fill('#q', '');
  await p.click('.tab:nth-child(1)'); await p.click('.topic >> nth=0'); await p.waitForSelector('.sw');
  log('card sections', await p.locator('#card details').count());
  await p.click('.sw button:nth-child(2)'); log('side2 on', await p.locator('.sw button.on').innerText());
  await p.screenshot({ path: 'work/shot_card.png' });
  await p.click('[data-go="#/banks"]', { timeout: 2000 }).catch(() => p.evaluate(() => location.hash = '#/banks'));
  log('bank details', await p.locator('details').count());
  await p.evaluate(() => location.hash = '#/draw');
  await p.check('#comp'); await p.click('[data-act=draw]'); await p.waitForSelector('.draw');
  log('draw card hidden', (await p.locator('#drawcard').count()) === 0 || (await p.locator('#drawcard').innerHTML()) === '');
  if (await p.locator('[data-act=reveal]').count()) { await p.click('[data-act=reveal]'); log('revealed', (await p.locator('#drawcard').innerHTML()).length > 50); }
  await p.click('#bstart'); await p.waitForTimeout(1300); log('clock', await p.locator('#clock').innerText());
  await p.screenshot({ path: 'work/shot_draw.png' });
  await p.evaluate(() => location.hash = '#/okr');
  log('errors', JSON.stringify(errs));
  await b.close();
})();
