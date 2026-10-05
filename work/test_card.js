const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const p = await (await b.newContext({ viewport: { width: 390, height: 900 }, hasTouch: true })).newPage();
  const errs = []; p.on('pageerror', e => errs.push(e.message));
  await p.goto('file:///home/user/Debattle/docs/offline.html#/t/okr-07'); await p.waitForSelector('.sw');
  await p.click('.sw button:nth-child(2)'); console.log('on:', await p.locator('.sw button.on').innerText());
  await p.click('summary >> text=Арсенал'); await p.screenshot({ path: 'work/shot_card2.png', fullPage: false });
  await p.evaluate(() => window.print = () => { window.__printed = true });
  await p.click('[data-act=print1]'); await p.waitForTimeout(200);
  console.log('print pcs:', await p.locator('#print-root .pc').count(), 'printed:', await p.evaluate(() => window.__printed));
  console.log('errors', JSON.stringify(errs)); await b.close();
})();
