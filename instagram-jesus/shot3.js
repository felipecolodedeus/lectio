const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350}});
await p.goto('file:///home/user/lectio/instagram-jesus/post-01-v3/slides.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(800);
for(let i=1;i<=5;i++){await (await p.$('#s'+i)).screenshot({path:`/home/user/lectio/instagram-jesus/post-01-v3/slide-0${i}.png`});}
await b.close()})();
