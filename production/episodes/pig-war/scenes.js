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
function docState(t){let entry=smoother(span(t,5.03,6.10)),approach=smoother(span(t,8.17,9.42)),macro=smoother(span(t,9.22,9.78)),hi=smooth(span(t,9.6,10.6)),pull=smoother(span(t,10.84,11.61)),exit=smoother(span(t,11.82,13.32));
 let scale=mix(.41,.87,approach);scale=mix(scale,1.32,macro);scale=mix(scale,.56,pull);scale*=1-.17*exit;
 let cx=mix(924,520+160*hi,macro);cx=mix(cx,924,pull);let cy=mix(1250,1492,macro);cy=mix(cy,1250,pull);let y=mix(750,960,approach);y=mix(y,735,macro);y=mix(y,770,pull);return{entry,approach,macro,hi,pull,exit,scale,cx,cy,x:540+1180*(1-entry)-1500*exit,y:y-440*exit};}
function docPoint(p,d){return[d.x+(p[0]-d.cx)*d.scale,d.y+(p[1]-d.cy)*d.scale];}
function documentScene(t){if(t<5.03||t>13.32)return;let d=docState(t);ctx.save();ctx.translate(d.x,d.y);ctx.scale(d.scale,d.scale);ctx.translate(-d.cx,-d.cy);ctx.shadowColor='#0d1c2b66';ctx.shadowBlur=24;ctx.shadowOffsetY=14;ctx.drawImage(imgs.treaty,0,0);ctx.shadowBlur=0;ctx.shadowOffsetY=0;
 if(d.hi>0){ctx.save();ctx.globalCompositeOperation='multiply';ctx.globalAlpha=.85;ctx.fillStyle='#FFE100';let w=665*d.hi;ctx.beginPath();ctx.moveTo(278,1450);ctx.lineTo(278+w,1446);ctx.lineTo(278+w,1533);ctx.lineTo(278,1537);ctx.closePath();ctx.fill();ctx.restore();}
 ctx.restore();
 let blur=smooth(span(t,9.15,9.8))*(1-smooth(span(t,10.95,11.55)));
 if(blur>0){let a=docPoint([625,1492],d);sq.drawImage(canvas,0,0);focus.apply(scene,fq,{cx:a[0],cy:a[1],rx:470,ry:125,feather:.9,maxBlur:7,outsideGain:.82,strength:blur});ctx.drawImage(focused,0,0,W,H);}
 if(t>6.3&&t<8.4){ctx.save();ctx.globalAlpha=smooth(span(t,6.3,6.7))*(1-smooth(span(t,8.0,8.4)));glyphLine('1846 TREATY',155,88,t,6.35);ctx.restore();}}

const E=DATA.timing.events;

function baseMap(c,{focusStrength=.8}={}){atlasCached(c);let sj=screen([-123.065,48.535],c);if(focusStrength){sq.drawImage(canvas,0,0);focus.apply(scene,fq,{cx:sj[0],cy:sj[1]-20,rx:380,ry:380,feather:1.05,maxBlur:7,outsideGain:.8,strength:focusStrength});ctx.drawImage(focused,0,0,W,H);}return sj;}
function marker(x,y,u,color,label){if(u<=0)return;ctx.save();ctx.translate(x,y);ctx.scale(backOut(u),backOut(u));ctx.fillStyle=color;ctx.beginPath();ctx.arc(0,0,16,0,Math.PI*2);ctx.fill();ctx.strokeStyle=color;ctx.lineWidth=3;ctx.beginPath();ctx.arc(0,0,28,0,Math.PI*2);ctx.stroke();ctx.restore();if(label)tag(label,x,y-50,{align:'center',size:28,color});}
function gardenReturn(t){let elapsed=t-E.trigger,entry=smoother(span(t,E.trigger,E.trigger+.8)),exit=smoother(span(t,E.soldiers-.65,E.soldiers+.15));ctx.save();ctx.translate(1280*(1-entry)-1280*exit,0);ctx.beginPath();ctx.rect(0,0,W,H);ctx.clip();let p=smoother(span(t,E.pig_property,E.pig_property+1.4)),a=smoother(span(t,E.arrest,E.arrest+1.3)),q=smoother(span(t,E.protection,E.protection+1.3));let c={x:mix(370,480,smoother(span(elapsed,0,5)))-70*p+120*a-40*q,y:960-30*p+25*a,z:mix(240,100,smoother(span(elapsed,0,5)))+115*p-60*a+20*q,exit:0};plane(c,1100,()=>ctx.drawImage(imgs.mountains,-115,-180,W+230,H+360));plane(c,360,()=>ctx.drawImage(imgs.field,-70,-70,W+140,H+210));plane(c,0,()=>puppetPig(elapsed+2.4));
 header(['1859','THE TRIGGER'],t,E.trigger,{size:104,highlight:0,fadeEnd:E.arrest-.35});
 if(t>E.pig_property&&t<E.arrest+.2){ctx.save();let u=smooth(span(t,E.pig_property,E.pig_property+.6));ctx.globalAlpha=u*(1-smooth(span(t,E.arrest-.2,E.arrest+.2)));tag("HUDSON’S BAY COMPANY",540,1490,{align:'center',size:30,color:C.coral,alpha:ctx.globalAlpha});line([[540,1440],[650,1260]],C.coral,4);ctx.restore();}
 header(['THREATENED','ARREST'],t,E.arrest,{size:94,highlight:1,fadeEnd:E.protection-.18});header(['MILITARY','PROTECTION'],t,E.protection,{size:96,highlight:1,fadeEnd:E.soldiers});ctx.restore();}
function escalation(t){let move=smoother(span(t,E.soldiers,E.crisis+1.5)),calm=smoother(span(t,E.restraint,E.diplomacy+1));let c={x:mix(40,-60,move),y:mix(-5,-90,move),s:mix(1.09,1.27,move)-.13*calm};let sj=baseMap(c,{focusStrength:.72});traceCourse('haro',c,1,C.gold);traceCourse('rosario',c,1,C.coral);tag('SAN JUAN ISLAND',sj[0],sj[1]-48,{align:'center',size:30});
 let troop=smooth(span(t,E.soldiers,E.soldiers+.65)),ship=smoother(span(t,E.ships,E.ships+1.6));let anchor=screen([-123.018,48.46],c);marker(anchor[0],anchor[1],troop,C.gold,'U.S. TROOPS');
 ctx.save();let w=1150+320*move,xx=1110*(1-ship)-40-1500*calm,yy=1180+Math.sin(t*1.25)*3;ctx.translate(xx,yy);ctx.rotate(-.01+Math.sin(t*.65)*.003);ctx.drawImage(imgs.ship,0,0,w,w*imgs.ship.height/imgs.ship.width);ctx.restore();
 if(t>E.ships+.7&&t<E.restraint+.3){ctx.save();ctx.globalAlpha=ship*(1-calm);tag('BRITISH WARSHIPS',555,1740,{align:'center',color:C.coral,size:29,alpha:ship*(1-calm)});ctx.restore();}
 header(['SOLDIERS','ARRIVED'],t,E.soldiers,{size:99,highlight:0,fadeEnd:E.ships-.12});header(['WARSHIPS','FOLLOWED'],t,E.ships,{size:98,highlight:0,fadeEnd:E.crisis+.28});header(['AN INTERNATIONAL','CRISIS'],t,E.crisis+.35,{size:90,highlight:1,fadeEnd:E.restraint-.15});
 header(['THEY STEPPED','BACK.'],t,E.restraint,{size:95,fadeEnd:E.diplomacy-.18});header(['DIPLOMACY','PREVAILED'],t,E.diplomacy,{size:91,highlight:0,fadeEnd:E.camps-.16});
 ctx.save();ctx.textAlign='center';ctx.font='600 20px Manrope';ctx.fillStyle=C.ink;ctx.fillText('Deployment symbols · positions and scale are schematic',540,1570);ctx.restore();}

function camps(t){let u=smoother(span(t,E.camps,E.camps+1.35)),v=smoother(span(t,E.camps+2.2,E.camps+3.7)),travel=smoother(span(t,E.joint,E.twelve+1));ctx.fillStyle=C.paper;ctx.fillRect(0,0,W,H);ctx.save();ctx.globalAlpha=.6;ctx.fillStyle=paperPattern;ctx.fillRect(0,0,W,H);ctx.restore();
 sourcePhoto(imgs.english_camp,540+1200*(1-u)-65*travel,360-30*travel,1250+70*travel,-.025);sourcePhoto(imgs.american_camp,540-1200*(1-v)+70*travel,1160-40*travel,1260+80*travel,.023);
 header(['TWO CAMPS.','ONE ISLAND.'],t,E.camps,{size:90,fadeEnd:E.joint-.15});header(['JOINT','OCCUPATION'],t,E.joint,{size:95,fadeEnd:E.arbitration});
 ctx.save();ctx.font='800 24px Manrope';ctx.fillStyle=C.ink;ctx.fillText('ENGLISH CAMP · 1868 · E. L. PORCHER',60,354);ctx.fillStyle=C.paper;ctx.fillRect(45,1114,790,42);ctx.fillStyle=C.ink;ctx.fillText('AMERICAN CAMP · CIRCA 1868',65,1145);ctx.font='600 18px Manrope';ctx.fillText('Historical sources courtesy National Park Service',65,1830);ctx.restore();
 if(t>E.joint){let p=smooth(span(t,E.joint,E.twelve+.4));ctx.save();ctx.fillStyle='#0d1c2bdd';ctx.fillRect(80,870,920,105);ctx.strokeStyle=C.gold;ctx.lineWidth=4;ctx.beginPath();ctx.moveTo(115,937);ctx.lineTo(115+850*p,937);ctx.stroke();ctx.font='800 24px Manrope';ctx.fillStyle=C.paper;ctx.fillText('1860',115,916);ctx.textAlign='right';ctx.fillText('1872',965,916);ctx.restore();}
}
function award(t){let enter=smoother(span(t,E.arbitration,E.arbitration+1.1)),approach=smoother(span(t,E.arbitration+1.8,E.haro+.35)),hi=smooth(span(t,E.selected,E.haro+.65)),leave=smoother(span(t,E.settlement+.2,E.settlement+1.45));let c={x:-60,y:-65,s:1.24};baseMap(c,{focusStrength:.55});traceCourse('haro',c,1,C.gold);traceCourse('rosario',c,1-leave,C.coral);
 if(leave<1){ctx.save();let sc=mix(.78,1.13,approach);ctx.translate(540+1170*(1-enter)-1500*leave,670-210*approach-150*leave);ctx.scale(sc,sc);ctx.rotate(mix(.024,0,approach));ctx.fillStyle=C.paper;ctx.shadowColor='#0d1c2b55';ctx.shadowBlur=24;ctx.fillRect(-510,-300,1020,1190);ctx.shadowBlur=0;ctx.save();ctx.globalAlpha=.42;ctx.fillStyle=paperPattern;ctx.fillRect(-510,-300,1020,1190);ctx.restore();ctx.fillStyle=C.ink;ctx.font='800 23px Manrope';ctx.textAlign='center';ctx.fillText('EDITORIAL TRANSCRIPTION · AWARD EXCERPT',0,-210);ctx.font='900 100px "Playfair Display"';ctx.fillText('21 October',0,-45);ctx.fillText('1872',0,90);ctx.font='600 36px "Playfair Display"';ctx.fillText('“... should be drawn through',0,320);ctx.fillStyle='#FFD919';ctx.fillRect(-315,365,630*hi,107);ctx.fillStyle=C.ink;ctx.font='900 75px "Playfair Display"';ctx.fillText('the Haro Channel.”',0,448);ctx.font='600 24px Manrope';ctx.fillText('English translation · FRUS 1872, document 156',0,650);ctx.fillText('U.S. Department of State, Office of the Historian',0,690);ctx.restore();}
 if(t>E.settlement+.6){header(['HARO','SELECTED'],t,E.settlement+.65,{size:103,highlight:0,fadeEnd:E.payoff});let sj=screen([-123.065,48.535],c);tag('SAN JUAN',sj[0],sj[1]-22,{align:'center',size:35});tag('U.S. CLAIM UPHELD',540,1470,{align:'center',size:30,color:C.ink});}
}
function payoff(t){let u=smoother(span(t,E.payoff,E.payoff+.85)),border=smoother(span(t,E.border,E.border+1.2));baseMap({x:-60,y:-50,s:1.25},{focusStrength:.65});traceCourse('haro',{x:-60,y:-50,s:1.25},1,C.gold);ctx.save();ctx.translate(1250*(1-u)-1200*border,0);ctx.beginPath();ctx.rect(0,0,W,H);ctx.clip();let c={x:450,y:960,z:210,exit:0};plane(c,1100,()=>ctx.drawImage(imgs.mountains,-115,-180,W+230,H+360));plane(c,360,()=>ctx.drawImage(imgs.field,-70,-70,W+140,H+210));plane(c,0,()=>puppetPig(3.7));header(['ONE','CASUALTY.'],t,E.payoff,{size:125,highlight:0,fadeEnd:E.border-.1});ctx.restore();header(['THE REAL','PROBLEM?'],t,E.border,{size:108,fadeEnd:E.brand-.1});
 if(t>E.border+1.05&&t<E.brand){ctx.save();ctx.font='900 132px "Playfair Display"';ctx.textAlign='center';glyphLine('THE BORDER.',1470,132,t,E.border+1.05,{highlight:true});ctx.restore();}
 if(t>=E.brand){ctx.save();let a=smooth(span(t,E.brand,E.brand+.3));ctx.globalAlpha=a;ctx.fillStyle='#f5f0e7ee';ctx.fillRect(85,180,910,270);ctx.fillStyle=C.ink;ctx.textAlign='center';ctx.font='900 85px "Playfair Display"';ctx.fillText('Curio Bureau',540,305);ctx.font='700 28px Manrope';ctx.fillText('Stories, systems, and surprises.',540,375);ctx.restore();}
}
function furniture(t){ctx.save();ctx.font='800 18px Manrope';ctx.fillStyle=C.ink;ctx.fillText('CURIO BUREAU',48,57);ctx.font='600 14px Manrope';ctx.fillText('THE PIG WAR',48,80);ctx.textAlign='center';ctx.font='600 16px Manrope';let credit='';if(t<5.3||(t>=E.trigger&&t<E.soldiers)||(t>=E.payoff&&t<E.border+1.2))credit='ILLUSTRATIVE RECONSTRUCTION';else if(t<13.3)credit='Oregon Treaty · National Archives 299808';else if(t<E.trigger)credit='SAN JUAN ISLAND · SCHEMATIC CLAIM INTERPRETATIONS';else if(t<E.camps)credit='SCHEMATIC DEPLOYMENT · ILLUSTRATIVE FRIGATE';else if(t>=E.arbitration&&t<E.payoff)credit='1872 AWARD · SOURCE TRANSCRIPTION / SCHEMATIC MAP';else if(t>=E.border+1.2)credit='British / U.S. boundary dispute · modern coastal reference';ctx.fillStyle=t<5.3||(t>=E.trigger&&t<E.soldiers)?C.paper:'#405861';if(credit)ctx.fillText(credit,540,1810);ctx.restore();}

function renderScene(t){
 if(t<E.trigger){mapScene(t);if(t<6.05)hook(t);documentScene(t);}
 else if(t<E.soldiers){baseMap({x:-65,y:-50,s:1.22});traceCourse('haro',{x:-65,y:-50,s:1.22},1,C.gold);traceCourse('rosario',{x:-65,y:-50,s:1.22},1,C.coral);gardenReturn(t);}
 else if(t<E.camps)escalation(t);else if(t<E.arbitration)camps(t);else if(t<E.payoff)award(t);else payoff(t);
}

function episodeMotionState(t){return {camera:introCamera(t),doc:docState(t),map:cam(t),native:[canvas.width,canvas.height],titleFamily:'Playfair Display',titleWeight:900};}
