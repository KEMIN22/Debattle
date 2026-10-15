// Проверка вкладки «Доп.» (extra-01) в offline.html, телефонный viewport
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const ctx = await b.newContext({ viewport: { width: 390, height: 800 }, hasTouch: true });
  const p = await ctx.newPage(); const errs = []; p.on('pageerror', e => errs.push(e.message));
  await p.addInitScript(() => localStorage.setItem('dbt_reg', '1'));
  await p.goto('file:///home/user/Debattle/docs/offline.html#/extra'); await p.waitForSelector('.topic');
  console.log('tabs:', (await p.locator('.tab').allInnerTexts()).join(' | '));
  console.log('extra topics:', await p.locator('.topic').count(), '| overflow-x:', await p.evaluate(() => document.documentElement.scrollWidth > innerWidth));
  console.log('row:', (await p.locator('.topic').first().innerText()).replace(/\n/g, ' / '));
  await p.screenshot({ path: 'work/shot_extra_list.png' });
  await p.click('.topic'); await p.waitForSelector('.sw');
  console.log('title:', (await p.locator('.ttl').innerText()).slice(0, 60), '| sections:', await p.locator('#card details').count());
  await p.screenshot({ path: 'work/shot_extra_card.png' });
  await p.click('.back'); await p.waitForTimeout(200); console.log('back ->', await p.evaluate(() => location.hash));
  await p.fill('#q', 'уэст'); console.log('search уэст:', await p.locator('.topic').count());
  await p.evaluate(() => { window.print = () => { window.__p = 1 }; });
  await p.evaluate(() => location.hash = '#/t/extra-01'); await p.waitForSelector('[data-act=print1]'); await p.click('[data-act=print1]'); await p.waitForTimeout(200);
  console.log('print:', await p.locator('#print-root .pc h3').innerText());
  console.log('errors', JSON.stringify(errs)); await b.close();
})();
