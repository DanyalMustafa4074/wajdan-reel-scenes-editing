// Combine slide PNGs into one multi-page PDF (for LinkedIn document upload).
// Each page is exactly one slide (1080x1440pt), no margins, image full-bleed.
// Usage: NODE_PATH=... CHROME=<chrome> node to_pdf.js <out.pdf> <slide1.png> <slide2.png> ...
const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const out = process.argv[2];
  const pngs = process.argv.slice(3);
  const chrome = process.env.CHROME ||
    (fs.existsSync('/opt/pw-browsers') &&
      fs.readdirSync('/opt/pw-browsers').filter(d => d.startsWith('chromium') && !d.includes('headless'))
        .map(d => `/opt/pw-browsers/${d}/chrome-linux/chrome`).find(fs.existsSync));
  const dataUri = p => 'data:image/png;base64,' + fs.readFileSync(p).toString('base64');
  const pages = pngs.map(p =>
    `<div class="pg"><img src="${dataUri(p)}"></div>`).join('');
  const html = `<!doctype html><html><head><style>
    *{margin:0;padding:0}
    .pg{width:1080px;height:1440px;page-break-after:always;overflow:hidden}
    .pg:last-child{page-break-after:auto}
    img{width:1080px;height:1440px;display:block}
  </style></head><body>${pages}</body></html>`;
  const b = await chromium.launch(chrome ? { executablePath: chrome } : {});
  const pg = await b.newPage();
  await pg.setContent(html, { waitUntil: 'networkidle' });
  await pg.pdf({ path: out, width: '1080px', height: '1440px', printBackground: true, pageRanges: '' });
  await b.close();
  console.log('wrote', out, '(' + pngs.length + ' pages)');
})().catch(e => { console.error(e); process.exit(1); });
