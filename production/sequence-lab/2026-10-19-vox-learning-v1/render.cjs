const fs=require('fs'),path=require('path'),vm=require('vm'),{spawn}=require('child_process');
const {createCanvas,loadImage,GlobalFonts}=require(process.env.CODEX_PRIMARY_RUNTIME_NODE_MODULES+'/@napi-rs/canvas');
const R=__dirname,repo=path.resolve(R,'../../..'),A=path.join(repo,'production/episodes/black-dwarf-supernova/art-v1/assets');
for(const [f,n]of[['Playfair900.ttf','Playfair Display'],['Manrope800.ttf','Manrope']])if(!GlobalFonts.registerFromPath(path.join(A,f),n))throw Error(f);
vm.runInThisContext(fs.readFileSync(path.join(repo,'production/engine/browser/brand.js'),'utf8'));
const W=1080,H=1920,D=19.5,F=585,C={ink:'#0D1C2B',ivory:'#F5F0E7',coral:'#CB503C',gold:'#86671F',muted:'#727C82'};
const TL=require('./timeline.json'),S=x=>{x=Math.max(0,Math.min(1,x));return x*x*(3-2*x)},L=(a,b,p)=>a+(b-a)*p;
let image,paper,photo,canvas,layer,grain=[];let q;
function text(s,x,y,size=32,color=C.ink,font='Manrope',align='left'){q.save();q.font=`${font==='Manrope'?800:900} ${size}px "${font}"`;q.fillStyle=color;q.textAlign=align;q.fillText(s,x,y);q.restore()}
function line(x,y,X,Y,color=C.ink,w=3,dash=[]){q.save();q.strokeStyle=color;q.lineWidth=w;q.setLineDash(dash);q.beginPath();q.moveTo(x,y);q.lineTo(X,Y);q.stroke();q.restore()}
function circle(x,y,r,color,w=3){q.save();q.strokeStyle=color;q.lineWidth=w;q.beginPath();q.arc(x,y,r,0,Math.PI*2);q.stroke();q.restore()}
function arrow(x,y,X,Y,color=C.coral,w=4){line(x,y,X,Y,color,w);let a=Math.atan2(Y-y,X-x);for(let z of[-.45,.45])line(X,Y,X-16*Math.cos(a+z),Y-16*Math.sin(a+z),color,w)}
function rng(s){return()=>((s=(Math.imul(s,1664525)+1013904223)>>>0)/4294967296)}
async function setup(){image=await loadImage(path.join(A,'remnant-illustration-v2.png'));paper=createCanvas(W,H);q=paper.getContext('2d');q.fillStyle=C.ivory;q.fillRect(0,0,W,H);let r=rng(1719);for(let i=0;i<38000;i++){q.fillStyle=r()>.5?'rgba(63,48,29,.10)':'rgba(255,255,255,.60)';q.fillRect(r()*W,r()*H,.7+r()*1.5,.8+r()*2)}for(let i=0;i<1300;i++)line(r()*W,r()*H,r()*W,r()*H,'rgba(78,67,48,.006)',.5);for(let i=0;i<1300;i++){let x=r()*W,y=r()*H;line(x,y,x+3+r()*17,y+(r()-.5)*4,'rgba(78,67,48,.10)',.55)}
photo=createCanvas(840,840);q=photo.getContext('2d');q.beginPath();q.arc(420,420,414,0,Math.PI*2);q.clip();q.drawImage(image,64,390,814,832,0,0,840,840);q.globalCompositeOperation='soft-light';q.globalAlpha=.22;q.drawImage(paper,0,0,840,840);
canvas=createCanvas(W,H);layer=createCanvas(W,H);for(let k=0;k<12;k++){let c=createCanvas(270,480),p=c.getContext('2d'),d=p.createImageData(270,480),r=rng(k*133+84);for(let i=0;i<d.data.length;i+=4){d.data[i]=d.data[i+1]=d.data[i+2]=r()*255;d.data[i+3]=255}p.putImageData(d,0,0);grain.push(c)}}
function state(t){let inspect=S((t-3.65)/1.05),returning=S((t-12.65)/1.0);let smallX=660,smallY=1280,smallR=145;let cx=L(540,smallX,inspect),cy=L(1080,smallY,inspect),r=L(455,smallR,inspect);let camera=L(1,2.75,returning),tx=L(smallX,540,returning)-smallX*camera,ty=L(smallY,1080,returning)-smallY*camera;let lim=L(550,1050,S((t-7.5)/1.15));lim=L(lim,1190,S((t-9.3)/1.15));lim=L(lim,1430,S((t-11.25)/1.3));let collapse=S((t-13.65)/2.2);return {inspect,returning,cx,cy,r:r*(1-.16*collapse),camera,tx,ty,lim,collapse}}
function worldTransform(s){q.translate(s.tx,s.ty);q.scale(s.camera,s.camera)}
function render(time,{headings=true,finish=true,captions=true}={}){let t=Math.floor((time+1e-8)*12)/12,s=state(t);q=canvas.getContext('2d');q.setTransform(1,0,0,1,0,0);q.fillStyle=C.ink;q.fillRect(0,0,W,H);q.save();worldTransform(s);q.drawImage(paper,0,0);q.restore();
// Photographic layer optics only: a brief hunt at the representation handoff, then settle.
let p=layer.getContext('2d');p.clearRect(0,0,W,H);p.save();p.translate(s.tx,s.ty);p.scale(s.camera,s.camera);p.drawImage(photo,s.cx-s.r,s.cy-s.r,s.r*2,s.r*2);p.restore();q.save();if(finish){let hunt=1.7*Math.exp(-(((t-4.04)/.15)**2));q.filter=`blur(${hunt.toFixed(3)}px)`}q.drawImage(layer,0,0);q.restore();
q.save();worldTransform(s);
if(t<3.65){if(t>2.25){let u=S((t-2.25)/.5),y=L(450,550,S((t-2.25)/1.2));line(95,y,95+880*u,y,C.coral,7);text('SUPPORT LIMIT',95,y-30,30,C.coral)}if(headings){text('What changes?',70,285,89,C.ink,'Playfair Display');text('A THEORETICAL BLACK-DWARF MODEL',75,345,25,C.muted)}if(t>1.4){let u=S((t-1.4)/.45);line(95,1550,95+880*u,1550,C.gold,5,[12,9]);text('MASS',95,1610,32,C.gold);text('nearly fixed',95,1653,30,C.gold)}}
// The support comparison becomes the main image rather than a lower inset.
if(t>=3.65){let a=s.inspect*(1-S((t-12.65)/.6));q.save();q.globalAlpha=a;for(let y=430;y<=1520;y+=100){line(150,y,970,y,'#D9D2C5',1);line(137,y,160,y,C.muted,2)}arrow(150,1530,150,410,C.muted,2);text('MORE',73,410,23,C.muted);text('LESS',73,1560,23,C.muted);
text('Support versus mass',200,270,68,C.ink,'Playfair Display');text('QUALITATIVE COMPARISON · NOT A PHYSICAL BOUNDARY',200,324,22,C.muted);
let fixed=1280;line(170,fixed,985,fixed,C.gold,6,[16,10]);circle(170,fixed,10,C.gold,4);text('MASS',210,1360,37,C.gold);text('nearly fixed',210,1403,29,C.gold);
// Support marker crosses a fixed reference; size and position of specimen stay unchanged.
line(170,s.lim,970,s.lim,C.coral,8);line(170,550,970,550,'#BCA89A',2,[6,9]);if(t>7.5){arrow(945,570,945,s.lim-20,C.coral,4)}text('LIMIT',850,s.lim-26,32,C.coral,'Manrope','right');
if(t<7.5)text('mass the remnant can support',210,605,29,C.coral);
if(t>5.9&&t<7.5){let u=S((t-5.9)/.5);line(173,fixed+20,173+790*u,fixed+20,C.gold,3)}
if(t>9.3){q.save();q.globalAlpha*=S((t-9.3)/.45);q.fillStyle=C.ink;q.fillRect(205,365,700,60);text('SOME MASSIVE REMNANTS ONLY',225,407,29,C.ivory);q.restore()}
if(s.lim>1280){q.save();q.globalAlpha*=.13;q.fillStyle=C.coral;q.fillRect(170,1280,810,s.lim-1280);q.restore();text('mass exceeds support',210,1510,37,C.coral,'Playfair Display')}
q.restore()}
q.restore();
if(t>=13.1){let a=S((t-13.1)/.5);q.save();q.globalAlpha=a;if(headings){text('Possible collapse',70,290,82,C.ink,'Playfair Display');text('RETURN TO THE SAME REMNANT · ILLUSTRATIVE CLOSE-UP',75,345,23,C.muted)}let x=s.cx*s.camera+s.tx,y=s.cy*s.camera+s.ty,r=s.r*s.camera;for(let angle of[0,Math.PI,.5*Math.PI,1.5*Math.PI]){let outer=r+85,inner=r+18;arrow(x+outer*Math.cos(angle),y+outer*Math.sin(angle),x+inner*Math.cos(angle),y+inner*Math.sin(angle),C.coral,5)}q.restore()}
if(finish){q.save();q.globalAlpha=.075;q.globalCompositeOperation='soft-light';q.drawImage(grain[Math.floor(t*12)%12],0,0,W,H);q.restore()}
// Screen-space source qualifiers and captions stay clean after optical/material passes.
text('CURIO BUREAU',70,78,23);text('VISUAL LEARNING TEST / 01',1010,78,21,C.muted,'Manrope','right');line(70,110,1010,110,C.muted,1);
text('Hypothetical remnant · AI illustration',70,1742,27,C.muted);text('Conditional model · if protons do not decay',70,1785,27,C.ink);text('Caplan (2020) · no measured scale or time rate',70,1828,25,C.muted);
let c=TL.captions.find(c=>t>=c.start&&t<c.end);if(c&&captions){q.font='800 43px Manrope';let ls=[''];for(const word of c.text.split(' ')){let i=ls.length-1,v=(ls[i]+' '+word).trim();if(q.measureText(v).width>660&&ls[i])ls.push(word);else ls[i]=v}let w=Math.max(...ls.map(x=>q.measureText(x).width))+30,h=ls.length*54+16,y=918;q.fillStyle=C.ink;q.fillRect(540-w/2,y-44,w,h);ls.forEach((s,i)=>text(s,540,y+54*i,43,C.ivory,'Manrope','center'))}
CurioBrand.drawEndcard(q,time,D);return canvas}
async function main(){await setup();if(process.argv[2]==='stills'){fs.mkdirSync(path.join(R,'qa'),{recursive:true});for(let t of[0,1.8,3.9,4.6,6.2,7.8,8.6,10.2,11.8,12.5,13.1,14.4,16.7,18.0,19.2])for(let hidden of[false,true])fs.writeFileSync(path.join(R,'qa',`frame-${t}${hidden?'-labels-only':''}.jpg`),render(t,{headings:!hidden,captions:!hidden}).toBuffer('image/jpeg',91));return}
let start=+process.argv[3],end=+process.argv[4],file=process.argv[5];let ff=spawn('ffmpeg',['-nostdin','-y','-v','error','-f','rawvideo','-pixel_format','rgba','-video_size','1080x1920','-framerate','30','-i','pipe:0','-an','-c:v','libx264rgb','-crf','0','-preset','veryfast','-pix_fmt','rgb24','-threads','2',file],{stdio:['pipe','inherit','inherit']});let done=new Promise((r,j)=>ff.on('exit',c=>c?j(Error(c)):r()));let last=-1,buf;for(let n=start;n<end;n++){let k=Math.floor(n*12/30);if(k!==last||n>=552){let d=render(n/30).getContext('2d').getImageData(0,0,W,H).data;buf=Buffer.from(d.buffer,d.byteOffset,d.byteLength);last=k}if(!ff.stdin.write(buf))await new Promise(r=>ff.stdin.once('drain',r));if(n%60===0)console.log('frame',n)}ff.stdin.end();await done}
module.exports={setup,render,state};if(require.main===module)main().catch(e=>{console.error(e);process.exit(1)});
