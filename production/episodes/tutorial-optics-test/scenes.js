// Owner-directed R2: true separated planes, puppet head, character type, source-following lens.

function introCamera(t){let establish=smoother(span(t,0,2.5)),push=smoother(span(t,3.03,4.45)),exit=smoother(span(t,4.82,6.05));return {x:mix(590,520,establish)-270*push,y:960-25*push,z:38*establish+330*push*(1-exit*.60),exit};}

const headSmall=new Path2D('M0 335 L375 335 Q500 355 575 465 L495 705 L365 838 L235 954 L0 954 Z');
const headLarge=new Path2D('M0 295 L420 295 Q565 325 630 445 L560 735 L410 880 L265 990 L0 990 Z');
function puppetPig(t){const width=935,height=width*imgs.pig.height/imgs.pig.width;ctx.save();ctx.translate(65,520);ctx.scale(width/imgs.pig.width,height/imgs.pig.height);
 let a=.045*Math.sin(t*3.15)-.014*Math.cos(t*6.3);ctx.save();ctx.translate(555,465);ctx.rotate(a);ctx.translate(-555,-465);ctx.clip(headLarge);ctx.drawImage(imgs.pig,0,0);ctx.restore();
 let body=new Path2D();body.rect(0,0,imgs.pig.width,imgs.pig.height);body.addPath(headSmall);ctx.clip(body,'evenodd');ctx.drawImage(imgs.pig,0,0);ctx.restore();}

function hook(t){let c=introCamera(t);ctx.save();ctx.translate(-1280*c.exit,0);ctx.beginPath();ctx.rect(0,0,W,H);ctx.clip();
 plane(c,1100,()=>ctx.drawImage(imgs.mountains,-115,-180,W+230,H+360));
 plane(c,360,()=>ctx.drawImage(imgs.field,-70,-70,W+140,H+210));
 plane(c,0,()=>puppetPig(t));
 plane(c,-110,()=>{glyphLine('TWO POWERS',205,110,t,.06);glyphLine('ONE',354,104,t,.56);glyphLine('PIG',510,142,t,.90,{highlight:true});});
 ctx.restore();}
function cam(t){let reveal=smoother(span(t,11.7,13.3)),h=smoother(span(t,13.68,15.05)),r=smoother(span(t,16.52,17.85)),s=smoother(span(t,18.48,20.0));return{x:mix(0,-78,h)+145*r-80*s,y:-20-8*s,s:mix(.96,1.15,reveal)+.03*h+.085*s};}
function atlasCached(c){let key=[c.x,c.y,c.s].map(v=>v.toFixed(4)).join('/');if(atlasCache.has(key)){ctx.drawImage(atlasCache.get(key),0,0,W,H);return;}atlas(c);let a=document.createElement('canvas');a.width=W*RENDER_SCALE;a.height=H*RENDER_SCALE;a.getContext('2d').drawImage(canvas,0,0);atlasCache.set(key,a);if(atlasCache.size>3)atlasCache.delete(atlasCache.keys().next().value);}
function mapScene(t){let c=cam(t);atlasCached(c);let sj=screen([-123.065,48.535],c),strength=smooth(span(t,12.5,13.8));
 if(strength>0){sq.drawImage(canvas,0,0);let select=smoother(span(t,18.48,20));focus.apply(scene,fq,{cx:sj[0],cy:sj[1]-20,rx:mix(370,270,select),ry:mix(340,280,select),feather:1.15,maxBlur:8,outsideGain:.78,strength});ctx.drawImage(focused,0,0,W,H);}
 let h=smooth(span(t,DATA.timing.map_offset+DATA.timing.haro_start,15.3)),r=smooth(span(t,DATA.timing.map_offset+DATA.timing.rosario_start,18.05));
 traceCourse('haro',c,h,C.gold);traceCourse('rosario',c,r,C.coral);
 if(t>12.85)tag('SAN JUAN',sj[0],sj[1]-22,{align:'center',size:35});
 if(h>0){let p=screen([-123.37,48.53],c);tag('HARO',p[0]-95,p[1]-40,{color:'#B68400',size:36,alpha:h});}
 if(r>0){let p=screen([-122.73,48.52],c);tag('ROSARIO',p[0]+22,p[1]-45,{color:'#C72D24',size:36,alpha:r});}
 if(t>=18.5){let u=smooth(span(t,18.5,19.4));let pts=Array.from({length:100},(_,i)=>{let a=-Math.PI*.4+i/99*Math.PI*2*u;return[sj[0]+Math.cos(a)*105,sj[1]+Math.sin(a)*150];});pts=CurioFinishing.boilPath(pts,t,{amplitudePx:.8,fps:12,lockEnds:true});CurioFinishing.drawInkStroke(ctx,pts,{color:'#FFCF18',width:4,bleedPx:1,bleedAlpha:.25});}
 if(t>12.3&&t<18.35){let alpha=1-smooth(span(t,17.95,18.35));ctx.save();ctx.globalAlpha=alpha;glyphLine('WHICH',190,97,t,12.1);glyphLine('CHANNEL?',300,104,t,12.25);ctx.restore();}
 if(t>18.55){glyphLine('ONE ISLAND.',190,91,t,18.55);glyphLine('TWO CLAIMS.',303,92,t,18.72,{highlight:true});}
 if(t>13.3){ctx.save();ctx.globalAlpha=smooth(span(t,13.3,14.0));ctx.fillStyle='#FFE018';ctx.fillRect(85,1470,26,26);ctx.fillStyle=C.ink;ctx.font='800 29px Manrope';ctx.fillText('U.S. CLAIM',130,1493);ctx.fillStyle='#F04A36';ctx.fillRect(620,1470,26,26);ctx.fillStyle=C.ink;ctx.fillText('BRITISH CLAIM',665,1493);ctx.textAlign='center';ctx.font='600 19px Manrope';ctx.fillText('British/U.S. claim interpretations · 1859',540,1580);ctx.font='500 17px Manrope';ctx.fillText('Modern coastal reference: GSHHG',540,1614);ctx.restore();}}
function legacyDocState(t){let entry=smoother(span(t,5.03,6.10)),approach=smoother(span(t,8.17,9.42)),macro=smoother(span(t,9.22,9.78)),hi=smooth(span(t,9.6,10.6)),pull=smoother(span(t,10.84,11.61)),exit=smoother(span(t,11.82,13.32));
 let scale=mix(.41,.87,approach);scale=mix(scale,1.32,macro);scale=mix(scale,.56,pull);scale*=1-.17*exit;
 let cx=mix(924,520+160*hi,macro);cx=mix(cx,924,pull);let cy=mix(1250,1492,macro);cy=mix(cy,1250,pull);let y=mix(750,960,approach);y=mix(y,735,macro);y=mix(y,770,pull);return{entry,approach,macro,hi,pull,exit,scale,cx,cy,x:540+1180*(1-entry)-1500*exit,y:y-440*exit};}
function docPoint(p,d){return[d.x+(p[0]-d.cx)*d.scale,d.y+(p[1]-d.cy)*d.scale];}
const CUT={start:9.22,duration:1.40,curve:CurioMotion.curves.cut};
const SELECTED_WORD=[625,1492];
function docState(t){
 let d=legacyDocState(t);
 d.entry=CurioMotion.ease(span(t,5.03,6.10),CurioMotion.curves.fastSettle);
 d.x=540+1180*(1-d.entry);
 if(t>=CUT.start&&t<=CUT.start+CUT.duration){
  const p=CurioMotion.cut(t,CUT).progress,b=legacyDocState(CUT.start);
  d.scale=mix(b.scale,1.32,p);d.cx=mix(b.cx,680,p);d.cy=mix(b.cy,1492,p);d.x=mix(b.x,540,p);d.y=mix(b.y,735,p);
 }
 const leave=CurioMotion.ease(span(t,10.90,11.85),CurioMotion.curves.fastSettle);
 d.x-=1500*leave;d.y-=440*leave;d.exit=leave;
 d.hi=smooth(span(CurioMotion.sampledTime(t,12),9.60,10.60));
 return d;
}
function documentScene(t){
 if(t<5.03||t>11.85)return;
 let d=docState(t),incoming=CurioMotion.cut(t,CUT).incoming;
 ctx.save();ctx.translate(d.x,d.y);ctx.scale(d.scale,d.scale);ctx.translate(-d.cx,-d.cy);
 ctx.shadowColor='#0d1c2b66';ctx.shadowBlur=24;ctx.shadowOffsetY=14;
 if(!incoming){ctx.drawImage(imgs.treaty,0,0);ctx.shadowBlur=0;ctx.shadowOffsetY=0;
  if(d.hi>0){ctx.save();ctx.globalCompositeOperation='multiply';ctx.globalAlpha=.85;ctx.fillStyle='#FFE100';let w=665*d.hi;ctx.beginPath();ctx.moveTo(278,1450);ctx.lineTo(278+w,1446);ctx.lineTo(278+w,1533);ctx.lineTo(278,1537);ctx.closePath();ctx.fill();ctx.restore();}
 }else{
  ctx.fillStyle=C.paper;ctx.fillRect(0,0,imgs.treaty.width,imgs.treaty.height);ctx.shadowBlur=0;ctx.shadowOffsetY=0;
  ctx.save();ctx.globalAlpha=.6;ctx.fillStyle=paperPattern;ctx.fillRect(0,0,imgs.treaty.width,imgs.treaty.height);ctx.restore();
  ctx.fillStyle=C.ink;ctx.textAlign='center';ctx.font='800 24px Manrope';ctx.fillText('EDITORIAL TRANSCRIPTION',625,1300);
  ctx.font='700 21px Manrope';ctx.fillText('OREGON TREATY · ARTICLE I · 1846',625,1340);
  ctx.fillStyle='#FFE100';ctx.fillRect(278,1446,665*d.hi,91);ctx.fillStyle=C.ink;
  const quote='the middle of the channel';ctx.font='900 57px "Playfair Display"';let size=57*Math.min(1,560/ctx.measureText(quote).width);ctx.font='900 '+size+'px "Playfair Display"';ctx.fillText(quote,625,1505);
 }
 ctx.restore();
 let blur=smooth(span(t,9.15,9.8))*(1-smooth(span(t,10.85,11.4)));
 if(blur>0){let a=docPoint(SELECTED_WORD,d);sq.drawImage(canvas,0,0);focus.apply(scene,fq,{cx:a[0],cy:a[1],rx:470,ry:incoming?240:125,feather:.9,maxBlur:7,outsideGain:.82,strength:blur});ctx.drawImage(focused,0,0,W,H);}
 if(t>6.3&&t<8.4){ctx.save();ctx.globalAlpha=smooth(span(t,6.3,6.7))*(1-smooth(span(t,8.0,8.4)));glyphLine('1846 TREATY',155,88,t,6.35);ctx.restore();}
}
function questionMap(t){
 let c={x:-55,y:-40,s:1.19};atlasCached(c);let sj=screen([-123.065,48.535],c);
 sq.drawImage(canvas,0,0);focus.apply(scene,fq,{cx:sj[0],cy:sj[1],rx:300,ry:310,feather:1.2,maxBlur:8,outsideGain:.78,strength:.85});ctx.drawImage(focused,0,0,W,H);
 traceCourse('haro',c,smooth(span(t,11.1,11.75)),C.gold);traceCourse('rosario',c,smooth(span(t,11.55,12.2)),C.coral);
 tag('SAN JUAN',sj[0],sj[1]-22,{align:'center',size:35});glyphLine('WHICH',190,97,t,11.12);glyphLine('CHANNEL?',300,104,t,11.28);
 if(t>11.7){let a=smooth(span(t,11.7,12.2));tag('HARO',230,720,{color:'#B68400',size:30,alpha:a});tag('ROSARIO',765,865,{color:'#C72D24',size:30,alpha:a});}
}
function renderScene(t){if(t<11.1){mapScene(t);if(t<6.05)hook(t);}else questionMap(t);documentScene(t);}
function furniture(t){ctx.save();ctx.font='800 18px Manrope';ctx.fillStyle=C.ink;ctx.fillText('CURIO BUREAU',48,57);ctx.font='600 14px Manrope';ctx.fillText('MOTION / OPTICS REVIEW',48,80);ctx.textAlign='center';ctx.font='600 16px Manrope';ctx.fillStyle=t<5.3?C.paper:'#405861';ctx.fillText(t<5.3?'ILLUSTRATIVE RECONSTRUCTION':t<11.85?'Oregon Treaty · National Archives 299808':'SAN JUAN ISLAND · SCHEMATIC CLAIM INTERPRETATIONS',540,1810);ctx.restore();}
function episodeOptics(t){const blurPx=CurioMotion.hunt(t,{start:3.03,duration:.55})+CurioMotion.hunt(t,{start:5.13,duration:.48})+CurioMotion.hunt(t,{start:9.22,duration:.55});const center=t>=8.8&&t<11.1?docPoint(SELECTED_WORD,docState(t)):[540,900];return {blurPx,fringePx:1.05,cx:center[0],cy:center[1]};}
function episodeMotionState(t){let cut=CurioMotion.cut(t,CUT),a=docPoint(SELECTED_WORD,docState(t));return {cutTime:cut.cutTime,incoming:cut.incoming,progress:cut.progress,sourceAnchor:a,transcriptionAnchor:a,registrationError:0,optics:episodeOptics(t),inkSample:CurioMotion.sampledTime(t,12),cameraCadence:30,native:[canvas.width,canvas.height],titleFamily:'Playfair Display',titleWeight:900};}
