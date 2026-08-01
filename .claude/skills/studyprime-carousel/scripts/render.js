// Render all slide*.html in a dir to slide*.png at 1080x1440 @2x.
// Usage: NODE_PATH=/opt/node22/lib/node_modules CHROME=<chrome> node render.js <html_dir>
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
(async () => {
  const dir = process.argv[2];
  const files = fs.readdirSync(dir).filter(f => f.endsWith('.html')).sort();
  const chrome = process.env.CHROME ||
    (fs.existsSync('/opt/pw-browsers') &&
      fs.readdirSync('/opt/pw-browsers').filter(d => d.startsWith('chromium') && !d.includes('headless'))
        .map(d => `/opt/pw-browsers/${d}/chrome-linux/chrome`).find(fs.existsSync));
  const b = await chromium.launch(chrome ? { executablePath: chrome } : {});
  const p = await b.newPage({ viewport: { width: 1080, height: 1440 }, deviceScaleFactor: 2 });
  for (const f of files) {
    await p.goto('file://' + path.resolve(dir, f), { waitUntil: 'networkidle' });
    await p.waitForTimeout(200);
    await (await p.$('.slide')).screenshot({ path: path.join(dir, f.replace('.html', '.png')) });
  }
  await b.close();
  console.log('rendered', files.length, 'slides');
})().catch(e => { console.error(e); process.exit(1); });
