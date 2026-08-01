const { chromium } = require('playwright');
const fs=require('fs'), path=require('path');
(async () => {
  const dir=process.argv[2];
  const files=fs.readdirSync(dir).filter(f=>f.endsWith('.html')).sort();
  const b=await chromium.launch({executablePath:process.env.CHROME});
  const p=await b.newPage({viewport:{width:1080,height:1440},deviceScaleFactor:2});
  for(const f of files){
    await p.goto('file://'+path.resolve(dir,f),{waitUntil:'networkidle'});
    await p.waitForTimeout(200);
    await (await p.$('.slide')).screenshot({path:path.join(dir,f.replace('.html','.png'))});
  }
  await b.close(); console.log('rendered',files.length);
})().catch(e=>{console.error(e);process.exit(1)});
