const { chromium } = require('playwright');
(async () => {
  const path = 'file://' + require('path').resolve('build/final.html');
  const out = process.argv[2] || 'build/slide1.png';
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
  const p = await b.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 2 });
  await p.goto(path, { waitUntil: 'networkidle' });
  await p.waitForTimeout(400);
  const el = await p.$('.slide');
  await el.screenshot({ path: out });
  await b.close();
  console.log('wrote', out);
})().catch(e=>{console.error(e);process.exit(1)});
