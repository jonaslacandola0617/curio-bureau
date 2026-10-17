const fs=require('fs'),path=require('path'),crypto=require('crypto');
const {createCanvas,loadImage,GlobalFonts}=require(process.env.CODEX_PRIMARY_RUNTIME_NODE_MODULES+'/@napi-rs/canvas');
const root=path.resolve(__dirname,'../art-v2'),out=path.join(root,'rendered');fs.mkdirSync(out,{recursive:true});
const fontRoot=path.resolve(root,'../../cold-metal-pilot/art-v1/assets');
GlobalFonts.registerFromPath(path.join(fontRoot,'Playfair900.ttf'),'Playfair Display');GlobalFonts.registerFromPath(path.join(fontRoot,'Manrope800.ttf'),'Manrope');
const C={navy:'#0D1C2B',ivory:'#F5F0E7',ink:'#172932',green:'#B9D18A',mint:'#7DA44F',blue:'#9FC9E1',gold:'#DFB66D',yellow:'#FFE24D',coral:'#E38872'};
let ctx,I={},heading=true;let T=0,local=0,scene=0;const E=x=>{x=Math.max(0,Math.min(1,x));return x*x*(3-2*x)};const originals={};
function rand(s){return()=>{s=(Math.imul(s,1664525)+1013904223)>>>0;return s/4294967296}}
function text(s,x,y,size=28,color=C.ivory,family='Manrope',weight=800,align='left'){ctx.save();ctx.fillStyle=color;ctx.font=`${weight} ${size}px "${family}"`;ctx.textAlign=align;ctx.fillText(s,x,y);ctx.restore()}
function title(lines,x,y,size=92,color=C.ivory){if(heading)lines.forEach((s,n)=>{ctx.save();let p=E(((scene===3?T-7.19:local)-.10-n*.10)/.52);ctx.globalAlpha=p;text(s,x,y+n*size*1.06+65*(1-p),size,color,'Playfair Display',900);ctx.restore()});}
function originalStroke(points,color,width=4,dashed=false){ctx.save();ctx.beginPath();ctx.moveTo(...points[0]);for(let n=1;n<points.length;n++)ctx.lineTo(...points[n]);ctx.lineJoin='round';ctx.lineCap='round';ctx.strokeStyle=color;ctx.lineWidth=width;if(dashed)ctx.setLineDash([10,12]);ctx.stroke();ctx.restore()}
function originalGrain(c,x,y,w,h,strength=.16,light=false){const q=c.getContext('2d'),r=rand(4107),tile=createCanvas(160,160),t=tile.getContext('2d'),d=t.createImageData(160,160);for(let n=0;n<d.data.length;n+=4){let v=r()>.52?255:0;d.data[n]=d.data[n+1]=d.data[n+2]=v;d.data[n+3]=r()*255*strength}t.putImageData(d,0,0);q.save();q.beginPath();q.rect(x,y,w,h);q.clip();q.fillStyle=q.createPattern(tile,'repeat');q.fillRect(x,y,w,h);q.strokeStyle=light?'rgba(70,58,41,.10)':'rgba(211,227,217,.05)';q.lineWidth=.6;for(let i=0;i<300;i++){let a=x+r()*w,b=y+r()*h;q.beginPath();q.moveTo(a,b);q.lineTo(a+12+r()*58,b-2+r()*4);q.stroke()}q.restore()}
function bg(light=false){ctx.fillStyle=light?C.ivory:C.navy;ctx.fillRect(0,0,1080,1920);let g=ctx.createRadialGradient(480,640,10,480,850,1350);g.addColorStop(0,light?'rgba(255,255,255,.28)':'rgba(85,117,91,.31)');g.addColorStop(1,'rgba(0,0,0,.27)');ctx.fillStyle=g;ctx.fillRect(0,0,1080,1920);grain(ctx.canvas,0,0,1080,1920,.17,light);if(scene<2||scene>4)text('C / B',62,70,24,light?C.ink:C.ivory);text('EVERYDAY SCIENCE',1018,70,18,light?C.ink:C.blue,'Manrope',800,'right')}
function footer(light=false){const col=light?'#52615d':'#A4B4B9';text('ORIGINAL PHOTOGRAPHIC ILLUSTRATIONS · CONCEPTUAL FIGURE',62,1837,16,col);text('Evidence: McKemy et al., Nature (2002) · TRPM8',62,1871,17,col)}
function originalPic(n,x,y,w,rot=0,blur=0,alpha=1){const im=I[n],h=w*im.height/im.width;ctx.save();ctx.translate(x+w/2,y+h/2);ctx.rotate(rot);ctx.globalAlpha=alpha;ctx.filter=blur?`blur(${blur}px)`:'none';ctx.shadowColor='rgba(0,0,0,.30)';ctx.shadowBlur=20;ctx.shadowOffsetY=15;ctx.drawImage(im,-w/2,-h/2,w,h);ctx.shadowColor='transparent';ctx.filter='none';ctx.globalAlpha=alpha*.10;ctx.globalCompositeOperation='screen';ctx.drawImage(im,-w/2+1.5,-h/2,w,h);ctx.restore()}
function tag(s,x,y,w,color=C.yellow,ink=C.ink){ctx.save();if(scene===0&&s==='NOT CHILLED'){const p=E(local/.85),push=E((local-1.5)/2.35),z=.90+.22*p+.12*push;ctx.translate(500-280*(1-p)-52*push,1740+180*(1-p)-180*push);ctx.rotate(.10*(1-p)-.035*push);ctx.scale(z,z);ctx.translate(-500,-1740);}ctx.translate(x,y);ctx.rotate(-.035);ctx.fillStyle=color;ctx.fillRect(0,0,w,53);grain(ctx.canvas,0,0,0,0,0);text(s,w/2,36,24,ink,'Manrope',800,'center');ctx.restore()}
function quiet(light=false){let g=ctx.createLinearGradient(0,790,0,1130);let b=light?'245,240,231':'13,28,43';g.addColorStop(0,`rgba(${b},0)`);g.addColorStop(.25,`rgba(${b},.97)`);g.addColorStop(.75,`rgba(${b},.97)`);g.addColorStop(1,`rgba(${b},0)`);ctx.fillStyle=g;ctx.fillRect(0,790,1080,340)}
function plate(active=0,x=140,y=1250){ctx.save();ctx.translate(x,y);ctx.rotate(-.018);ctx.shadowColor='rgba(0,0,0,.4)';ctx.shadowBlur=30;ctx.shadowOffsetY=18;ctx.fillStyle='#E9E1D0';ctx.beginPath();ctx.moveTo(0,7);ctx.lineTo(800,0);ctx.lineTo(810,450);ctx.lineTo(4,458);ctx.closePath();ctx.fill();ctx.shadowColor='transparent';
 text('COLD-SENSITIVE CHANNEL',38,55,22,C.ink);text('TRPM8',38,113,58,C.ink,'Manrope',800);text('CONCEPTUAL / NOT TO SCALE',770,52,16,'#64736b','Manrope',800,'right');
 // A generic labeled membrane/channel print; no claim of recovered molecular geometry.
 for(let row=0;row<2;row++)for(let k=0;k<31;k++){let xx=27+k*25,yy=205+row*69;if(xx>290&&xx<495)continue;ctx.beginPath();ctx.arc(xx,yy,8,0,Math.PI*2);ctx.fillStyle='#A99B7E';ctx.fill();stroke([[xx-3,yy+(row?-10:10)],[xx-6,yy+(row?-29:29)]],'#AA9A7B',2);stroke([[xx+3,yy+(row?-10:10)],[xx+6,yy+(row?-29:29)]],'#AA9A7B',2)}
 ctx.fillStyle=active?'#628565':'#777B6C';for(let side of[-1,1]){ctx.save();ctx.translate(400,242);ctx.scale(side,1);ctx.beginPath();ctx.moveTo(-15,-99);ctx.bezierCurveTo(-115,-113,-119,-45,-92,-21);ctx.bezierCurveTo(-129,13,-103,90,-26,98);ctx.bezierCurveTo(-52,52,-44,-53,-15,-99);ctx.fill();ctx.strokeStyle='#394D43';ctx.lineWidth=3;ctx.stroke();ctx.restore()}
 if(active){ctx.strokeStyle=C.coral;ctx.lineWidth=6;ctx.beginPath();ctx.ellipse(400,242,128,113,0,0,Math.PI*2);ctx.stroke();text('CAN ACTIVATE',400,407,27,C.ink,'Manrope',800,'center')}else text('INPUT → RESPONSE',400,407,25,C.ink,'Manrope',800,'center');
 text('membrane',35,337,21,'#5D665D');ctx.restore();grain(ctx.canvas,x,y,810,458,.19,true)}
function opening(){bg();pic('mouth',315,320,1350,-.025);pic('mint',-140,1100,1280,-.13);quiet();title(['Cold.','Without ice.'],62,228,108);tag('NOT CHILLED',92,1450,270);text('Why can mint feel cold?',72,1743,37,C.ivory);footer()}
function menthol(){bg(true);pic('mint',-120,300,1080,.13);quiet(true);title(['Look inside','the question.'],62,210,86,C.ink);stroke([[666,565],[949,700],[949,1287],[755,1287]],C.ink,3);ctx.fillStyle='#DAD0B7';ctx.fillRect(95,1228,835,365);grain(ctx.canvas,95,1228,835,365,.20,true);text('COMPOUND FOUND IN PEPPERMINT',130,1285,22,C.ink);text('MENTHOL',130,1390,81,C.ink,'Manrope',800);stroke([[132,1430],[885,1430]],C.ink,2);text('a chemical input',130,1505,39,C.ink);tag('NOT A MICROGRAPH',72,1670,361,'#DEC899');footer(true)}
function converge(level){bg();pic('mint',-90,175,675,-.15,level===0?2:0);pic('ice',665,290,458,.12,level===1?5:0);title(level===2?['Two inputs.','One channel.']:['Different routes','to cold.'],62,112,81);text('MENTHOL',105,695,31,C.green);text('COOLING',811,748,31,C.blue,'Manrope',800,'center');plate(level===2?1:0);
 const icePath=[[883,790],[971,835],[971,1185],[691,1245],[544,1485]];
 stroke(icePath,C.blue,7);
 const leafPath=[[240,743],[104,807],[104,1180],[355,1238],[544,1485]];
 if(level>0)stroke(leafPath,C.gold,7);else stroke([[240,743],[104,807],[104,1120]],'#8C9279',3,true);
 if(level===1){tag('A SECOND INPUT',69,1134,315,C.gold);text('same anchored channel',552,1755,30,C.ivory,'Manrope',800,'center')}if(level===2)text('Different inputs can activate TRPM8.',540,1755,32,C.ivory,'Manrope',800,'center');footer()}
function sensation(){bg(true);pic('mouth',245,260,1300,-.02);pic('mint',-90,1190,1010,-.19);quiet(true);title(['Feeling cold','is a signal.'],62,212,96,C.ink);tag('COOL SENSATION',62,1195,379,C.yellow);tag('SENSATION ≠ TEMPERATURE',62,1680,720,C.yellow);footer(true)}
function payoff(){bg();pic('mint',-120,230,760,-.21);pic('ice',680,315,460,.12);quiet();title(['Different input.'],62,200,96);title(['Familiar sensation.'],62,1230,79);plate(1,140,1340);stroke([[245,760],[103,825],[103,1370],[430,1455],[540,1582]],C.gold,6);stroke([[870,786],[974,835],[974,1370],[650,1455],[540,1582]],C.blue,6);tag('MENTHOL',85,1270,239,C.gold);tag('COOLING',735,1270,247,C.blue);footer()}
const states=[['01_hook',opening],['02_menthol',menthol],['03_input_initial',()=>converge(0)],['04_input_intermediate',()=>converge(1)],['05_input_resolved',()=>converge(2)],['06_sensation',sensation],['07_payoff',payoff]];

const materials=new Map();
function grain(c,x,y,w,h,strength=.16,light=false){if(!w||!h)return;const key=[w,h,strength,light].join('/');if(!materials.has(key)){const p=createCanvas(Math.ceil(w),Math.ceil(h));originalGrain(p,0,0,w,h,strength,light);materials.set(key,p)}c.getContext('2d').drawImage(materials.get(key),x,y)}
function pic(n,x,y,w,rot=0,blur=0,alpha=1){
 let dx=0,dy=0,z=1,r=0;
 if(scene===0){const p=E(local/.85),push=E((local-1.5)/2.35);if(n==='mint'){dx=-280*(1-p)-52*push;dy=180*(1-p)-180*push;z=.90+.22*p+.12*push;r=.10*(1-p)-.035*push}else{dx=80*(1-p)-80*push;dy=35*(1-p)-35*push;z=1+.06*push}}
 else if(scene===1){let p=E(local/.9);if(n==='mint'){dx=-75*(1-p);dy=160*(1-p)-26*p;z=1+.12*p;r=-.06*(1-p)}}
 else if(scene===5){let p=E(local/.85),push=E((local-2.5)/2.4);if(n==='mouth'){dx=140*(1-p)-55*push;z=1+.065*push}else{dx=-130*(1-p);dy=180*(1-p)-70*push;z=.98+.07*push}}
 else if(scene===6){let p=E(local/.85);dx=n==='mint'?-140*(1-p):140*(1-p);dy=35*(1-p);}
 ctx.save();ctx.translate(x+w/2+dx,y+w*I[n].height/I[n].width/2+dy);ctx.rotate(r);ctx.scale(z,z);originalPic(n,-w/2,-w*I[n].height/I[n].width/2,w,rot,blur,alpha);ctx.restore();
}
function partial(points,p){p=Math.max(0,Math.min(1,p));let lens=points.slice(1).map((v,i)=>Math.hypot(v[0]-points[i][0],v[1]-points[i][1])),remain=lens.reduce((a,b)=>a+b,0)*p,res=[points[0]];for(let i=0;i<lens.length;i++){if(remain>=lens[i]){res.push(points[i+1]);remain-=lens[i]}else{let q=remain/lens[i];res.push([points[i][0]+(points[i+1][0]-points[i][0])*q,points[i][1]+(points[i+1][1]-points[i][1])*q]);break}}return res}
function stroke(points,color,width=4,dashed=false){let p=1;
 if(scene>=2&&scene<=4&&points.length>3){if(color===C.blue)p=E((T-11.95)/1.05);if(color===C.gold)p=E((T-17.5)/1.0)}
 if(scene===6&&points.length>3)p=E((local-(color===C.blue?.45:.05))/.9);
 if(p<=0)return;let pts=partial(points,p); // Stable anchors, tiny source-local ink-edge boil.
 if(width>=6){const j=Math.floor(T*12);pts=pts.map((v,i)=>i===0||i===pts.length-1?v:[v[0]+Math.sin(j*1.7+i)*.65,v[1]+Math.cos(j*1.3+i)*.65])}
 originalStroke(pts,color,width,dashed);
}
async function setup(){for(const n of['mint','ice','mouth'])I[n]=await loadImage(path.join(root,'assets',n+'.png'))}
function render(q,t,index,age){ctx=q;T=t;scene=index;local=age;heading=true;if(index===0)opening();else if(index===1)menthol();else if(index===2)converge(0);else if(index===3)converge(1);else if(index===4)converge(2);else if(index===5)sensation();else payoff();}
module.exports={setup,render};
