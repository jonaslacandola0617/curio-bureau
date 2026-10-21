const fs=require('fs'),path=require('path'),vm=require('vm');
const {createCanvas,loadImage,GlobalFonts}=require('@napi-rs/canvas');
const P=__dirname,root=process.env.CURIO_REPO_ROOT||path.resolve(P,'../../../..');
const assets=path.join(root,'production/pre-render/pilot-20261016/cold-metal-pilot/art-v1/assets');
GlobalFonts.registerFromPath(path.join(assets,'Playfair900.ttf'),'Playfair Display');GlobalFonts.registerFromPath(path.join(assets,'Manrope.ttf'),'Manrope');
vm.runInThisContext(fs.readFileSync(path.join(root,'production/engine/browser/brand.js'),'utf8'));
(async()=>{const tl=JSON.parse(fs.readFileSync(path.join(P,'timeline.json'))),bg=await loadImage(path.join(P,'ending-base.png'));fs.mkdirSync(path.join(P,'ending'),{recursive:true});const st=Math.round(tl.ending_start*30);for(let n=st;n<tl.frames;n++){const c=createCanvas(1080,1920),q=c.getContext('2d');q.drawImage(bg,0,0);CurioBrand.drawEndcard(q,n/30,tl.duration);fs.writeFileSync(path.join(P,'ending',String(n-st).padStart(3,'0')+'.png'),c.toBuffer('image/png'))}console.log('Exact shared brand module used:',tl.frames-st,'30fps frames')})().catch(e=>{console.error(e);process.exit(1)});
