const { chromium } = require('playwright');
(async () => {
  const file='file://'+require('path').resolve(process.argv[2]);
  const out=process.argv[3];
  const b=await chromium.launch({executablePath: process.env.CHROME});
  const p=await b.newPage({viewport:{width:1080,height:1440},deviceScaleFactor:2});
  await p.goto(file,{waitUntil:'networkidle'}); await p.waitForTimeout(300);
  await (await p.$('.slide')).screenshot({path:out}); await b.close(); console.log('wrote',out);
})().catch(e=>{console.error(e);process.exit(1)});
