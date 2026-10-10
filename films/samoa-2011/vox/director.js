/* CURIO BUREAU / DIRECTOR'S CUT / PRODUCTION v2
   Override legacy scene drawing with art-directed editorial compositions.
   All major headings: Playfair Display. All labels/captions: Manrope.
   Factual geography: Natural Earth from builder. Caption cues: neural TTS boundaries.
*/
const COUNTRY_GEO=window.CURIO_GEO||[];
const CAPTION_CUES=window.CURIO_CAPTIONS||[];
const SAFE={left:84,right:996,top:120,bottom:1670};
const qa={issues:[],titles:[],mapLoaded:COUNTRY_GEO.length>3,captionCount:CAPTION_CUES.length};
window.CURIO_QA=qa;
const sq=(v)=>Math.round(v*100)/100;
const color={white:'#F5F0E7',paper:'#EDE5D6',navy:'#0D1C2B',deep:'#081521',gold:'#C8A26B',gold2:'#E8BF7A',coral:'#D57864',ink:'#172937',blue:'#204F65',sea:'#1D4861',sage:'#AEB9A6',mist:'#A9C0BC'};
function paintRect(x,y,w,h,fill,rad=0){g.beginPath();g.roundRect(x,y,w,h,rad);g.fillStyle=fill;g.fill()}
function typeface(size=28,colorName=color.ink,weight=600){g.font=weight+' '+size+'px "Manrope",Arial,sans-serif';g.fillStyle=colorName;g.textBaseline='alphabetic'}
function label(t,x,y,size=26,clr=color.ink,weight=700,spacing=0){
 typeface(size,clr,weight);const tr=g.getTransform();const pure=Math.abs(tr.a-1)<.001&&Math.abs(tr.d-1)<.001&&Math.abs(tr.b)<.001&&Math.abs(tr.c)<.001&&Math.abs(tr.e)<.001&&Math.abs(tr.f)<.001;
 if(pure&&x>=SAFE.left&&y<1685){while(g.measureText(t).width+x>SAFE.right&&size>15){size--;typeface(size,clr,weight)}}
 if(!spacing){g.fillText(t,x,y);return}
 let xx=x;for(const ch of t){g.fillText(ch,xx,y);xx+=g.measureText(ch).width+spacing}
}
function heading(t,x,y,size=94,clr=color.white,maxW=904,weight=600){
 let sz=size;
 const tr=g.getTransform(),screenSpace=(Math.abs(tr.a-1)<.001&&Math.abs(tr.b)<.001&&Math.abs(tr.c)<.001&&Math.abs(tr.d-1)<.001&&Math.abs(tr.e)<.001&&Math.abs(tr.f)<.001);
 if(screenSpace)maxW=Math.min(maxW,SAFE.right-x);
 while(sz>28){g.font=weight+' '+sz+'px "Playfair Display",Georgia,serif';if(g.measureText(t).width<=maxW)break;sz-=1}
 let box=g.measureText(t);if(screenSpace&&(x<SAFE.left||x+box.width>SAFE.right+1||y<SAFE.top||y>SAFE.bottom))qa.issues.push({text:t,x,y,w:sq(box.width),size:sz});
 qa.titles.push({text:t,x,y,font:'Playfair Display',size:sz});g.fillStyle=clr;g.textAlign='left';g.textBaseline='alphabetic';g.fillText(t,x,y);
}
function dataTitle(t,x,y,size=54,clr=color.white,maxW=895){
 let sz=size;typeface(sz,clr,800);while(g.measureText(t).width>maxW&&sz>23){sz--;typeface(sz,clr,800)}g.textAlign='left';g.fillText(t,x,y)
}
function dotDraw(x,y,r,c){g.beginPath();g.arc(x,y,r,0,Math.PI*2);g.fillStyle=c;g.fill()}
function rule(x,y,w,c=color.gold,h=5){paintRect(x,y,w,h,c)}
function plate(x,y,w,h,c=color.paper){g.save();g.shadowColor='#05090C90';g.shadowBlur=37;g.shadowOffsetY=17;paintRect(x,y,w,h,c,3);g.restore()}
function deco(bg=color.navy,light=false,seed=0){
 paintRect(0,0,W,H,bg);
 const ink=light?'#133044':'#F5F0E7';
 for(let i=0;i<150;i++){const x=rand(3*i+12+seed)*W,y=rand(3*i+88+seed)*H;paintRect(x,y,1+2*rand(i+seed),1.5,ink+'20')}
 for(let i=0;i<25;i++)stroke(0,i*80+rand(i+seed)*16,W,i*80+rand(i+seed)*16,ink+'06',2);
 const grad=g.createLinearGradient(0,0,W,H);grad.addColorStop(0,'#ffffff0c');grad.addColorStop(.65,'#00000000');grad.addColorStop(1,'#0000001b');paintRect(0,0,W,H,grad)
}
function mast(scene,labelText,dark=false){
 const c=dark?color.ink:color.white;
 rule(84,124,45,color.gold,6);label('CURIO BUREAU',154,137,21,c,800,4.5);
 label('RESEARCH FILE  /  001',85,195,17,dark?'#54707A':'#98ACB6',700,2.1);
 stroke(85,1746,995,1746,dark?'#45616A66':'#F5F0E755',2);
 label(labelText.toUpperCase(),85,1793,19,c,800,1.1);
 typeface(18,color.gold,800);g.textAlign='right';g.fillText('0'+(scene+1)+' / 08',996,1793);g.textAlign='left';
}
function cropPath(points,fill,opacity=1){
 g.save();g.globalAlpha*=opacity;g.beginPath();g.moveTo(points[0],points[1]);for(let i=2;i<points.length;i+=2)g.lineTo(points[i],points[i+1]);g.closePath();g.fillStyle=fill;g.fill();g.restore()
}
function inkRule(x,y,w,h=7){paintRect(x,y,w,h,color.coral)}
function texturePanel(x,y,w,h,sea=false){
 plate(x,y,w,h,sea?'#28566A':color.paper);
 g.save();g.beginPath();g.rect(x,y,w,h);g.clip();
 for(let i=0;i<80;i++)paintRect(x+rand(i*7+6)*w,y+rand(i*9+6)*h,1,3,sea?'#f5f0e723':'#37475118');
 for(let i=0;i<10;i++)stroke(x,y+i*h/9,x+w,y+i*h/9,sea?'#F5F0E71A':'#22394811',1);
 g.restore()
}
function callout(s,x,y,w=280,cl=color.coral){paintRect(x,y-34,w,55,cl);label(s,x+15,y,21,color.white,800,1.1)}
function stamp2(s,x,y,rot=0){
 g.save();g.translate(x,y);g.rotate(rot);g.strokeStyle=color.coral;g.lineWidth=6;g.strokeRect(-182,-49,364,98);
 let sz=40;typeface(sz,color.coral,800);while(g.measureText(s).width>332) {sz-=1;typeface(sz,color.coral,800)}
 g.textAlign='center';g.fillText(s,0,13);g.restore();
}
function printClock(cx,cy,r,progress=0){
 dotDraw(cx+12,cy+15,r+16,'#0B152455');dotDraw(cx,cy,r,color.paper);
 for(let j=0;j<3;j++){g.strokeStyle=j===0?color.gold:color.ink;g.lineWidth=j===0?10:1.6;g.beginPath();g.arc(cx,cy,r-j*18,0,Math.PI*2);g.stroke()}
 for(let h=0;h<60;h++){let a=-Math.PI/2+h*Math.PI/30;let inner=r-(h%5===0?51:37),outer=r-20;
 stroke(cx+inner*Math.cos(a),cy+inner*Math.sin(a),cx+outer*Math.cos(a),cy+outer*Math.sin(a),color.ink,h%5===0?6:2)}
 for(let h=1;h<=12;h++){let a=-Math.PI/2+h*Math.PI/6;typeface(30,color.ink,700);g.textAlign='center';g.fillText(String(h),cx+(r-91)*Math.cos(a),cy+(r-91)*Math.sin(a)+11)}
 const ang=-Math.PI/2+progress*Math.PI*2;
 stroke(cx,cy,cx+Math.cos(ang)*r*.77,cy+Math.sin(ang)*r*.77,color.coral,10);
 const ha=-Math.PI/2+progress*Math.PI/6;stroke(cx,cy,cx+Math.cos(ha)*r*.47,cy+Math.sin(ha)*r*.47,color.ink,18);dotDraw(cx,cy,15,color.gold)
}
function printCalendar(x,y,w,h,date,week,tilt=0){
 g.save();g.translate(x+w/2,y+h/2);g.rotate(tilt);
 g.shadowColor='#05132266';g.shadowBlur=27;g.shadowOffsetY=16;paintRect(-w/2,-h/2,w,h,color.paper,3);
 g.shadowColor='transparent';g.shadowBlur=0;
 paintRect(-w/2,-h/2,w,104,color.coral);
 label('DECEMBER 2011',-w/2+37,-h/2+66,34,color.white,800,2);
 for(let i=0;i<3;i++){dotDraw(-w/2+95+i*(w-190)/2,-h/2+8,8,color.navy)}
 heading(String(date),-w/2+53,h/2-155,188,color.navy,w-100,600);
 stroke(-w/2+46,h/2-128,w/2-40,h/2-128,'#182C3855',2);
 label(week,-w/2+47,h/2-56,31,color.ink,800,2);
 g.restore()
}
function dataStripe(labelText,x,y,width=350){paintRect(x,y,width,77,color.navy);label(labelText,x+27,y+51,27,color.white,800,1.4)}
function project(lon,lat,rect){let v=lon<0?lon+360:lon;return [rect.x+(v-110)/110*rect.w,rect.y+(25-lat)/82*rect.h]}
function drawCoast(rect,alpha=1){
 g.save();g.globalAlpha*=alpha;g.beginPath();g.roundRect(rect.x,rect.y,rect.w,rect.h,3);g.clip();
 paintRect(rect.x,rect.y,rect.w,rect.h,'#1E526A');
 for(let lon=115;lon<222;lon+=15){let x=project(lon,-12,rect)[0];stroke(x,rect.y,x,rect.y+rect.h,'#B9CAC225',2)}
 for(let lat=-50;lat<=20;lat+=10){let y=project(160,lat,rect)[1];stroke(rect.x,y,rect.x+rect.w,y,'#B9CAC225',2)}
 const cr=(n)=>n==='Australia'?'#A4B3A4':n==='New Zealand'?'#CBD0B8':n==='Fiji'?'#E0C7A4':'#96B4AB';
 for(const region of COUNTRY_GEO){
  let gg=region.geometry;if(!gg)continue;const multi=gg.type==='MultiPolygon'?gg.coordinates:[gg.coordinates];
  for(const poly of multi){for(const ring of poly){if(ring.length<3)continue;
   g.beginPath();let start=null;
   for(const coords of ring){if(!Array.isArray(coords))continue;let [px,py]=project(coords[0],coords[1],rect);
    if(!start){g.moveTo(px,py);start=[px,py]}else g.lineTo(px,py)}
   g.closePath();g.fillStyle=cr(region.name);g.fill();g.strokeStyle='#E3E0CC99';g.lineWidth=1.4;g.stroke();
  }}
 }
 // At 110m scale Samoa is too small to see reliably: use a geodetically anchored marker.
 const point=(lon,lat,r,name,col=color.gold)=>{
   const [xx,yy]=project(lon,lat,rect);dotDraw(xx,yy,r,col);return [xx,yy]
 };
 const aus=point(134,-25,3,'Australia','#D9BD90');
 const nz=point(172,-42,3,'New Zealand','#D9BD90');
 const sam=point(-172.1,-13.76,11,'Samoa',color.coral);
 dotDraw(sam[0],sam[1],21,'#D5786428');g.strokeStyle=color.coral;g.lineWidth=3;g.beginPath();g.arc(sam[0],sam[1],27,0,Math.PI*2);g.stroke();
 g.restore();return{sam,aus,nz};
}
function pathLine(rect,xOffset,t){
 const a=rect.x+rect.w*xOffset,b=rect.y;
 g.save();g.beginPath();g.rect(rect.x,rect.y,rect.w,rect.h);g.clip();
 g.beginPath();g.setLineDash([16,14]);g.lineWidth=6;g.strokeStyle=color.gold;
 let xx=a;g.moveTo(xx,b+30);g.bezierCurveTo(xx-20,b+rect.h*.28,xx+40,b+rect.h*.55,xx+10,b+rect.h-15);
 g.stroke();g.setLineDash([]);g.restore();
}
function frame0(t){
 deco(color.deep,false,10);mast(0,'The vanished date');
 const v=out((t-.2)/1.0);g.save();g.globalAlpha=v;
 heading('The day that',100,366,107,color.white,850);
 heading('disappeared.',100,487,104,color.white,860);
 g.restore();rule(104,519,600*out((t-.7)/1.2),color.gold,8);
 const b=out((t-1)/1.2);g.save();g.globalAlpha=b;g.translate(0,(1-b)*150);
 texturePanel(87,600,905,764);
 printCalendar(120,648,518,628,'30','FRIDAY',-.045);
 g.save();g.translate(752,919);g.rotate(.085);
 texturePanel(-140,-182,270,340);
 dataTitle('SAMOA',-106,-62,48,color.ink,250);
 label('29 → 31',-104,35,47,color.coral,800);
 label('DEC 2011',-104,106,24,color.ink,700);
 g.restore();g.restore();
 const k=out((t-4)/1.3);g.save();g.globalAlpha=k;stamp2('ONE DAY MISSING',545,1301,-.07);g.restore();
 label('THE PACIFIC / 2011',106,1405,22,color.gold,800,4);
}
function frame1(t){
 deco('#172E40');mast(1,'A date is removed');
 heading('Thursday.',102,340,98,color.white);
 heading('Then Saturday.',102,455,91,color.gold);
 const show=out((t-.3)/1.2);
 g.save();g.globalAlpha=show;texturePanel(80,570,923,776);
 printCalendar(120,625,405,553,'29','THURSDAY',-.07);
 printCalendar(545,682,405,553,'31','SATURDAY',.06);g.restore();
 let q=out((t-1.9)/1.2);
 g.save();g.globalAlpha=q;g.translate(0,50*(1-q));
 paintRect(324,1133,428,120,color.paper);label('FRIDAY, DEC 30',359,1202,41,color.ink,800);
 for(let k=0;k<4;k++)stroke(332,1124+k*35,752,1124+k*35,color.coral,8);g.restore();
 const s=out((t-3.7)/.75);g.save();g.globalAlpha=s;stamp2('SKIPPED',553,1392,-.09);g.restore();
 label('29 DECEMBER → 31 DECEMBER',100,1640,29,color.white,800);
}
function frame2(t){
 deco('#132B3D');mast(2,'Samoa and the International Date Line');
 heading('A map explains',100,335,95,color.white);
 heading('the mystery.',100,455,98,color.gold);
 const z=out((t-.3)/1.7);g.save();g.globalAlpha=z;g.translate(0,(1-z)*230);
 let m={x:92,y:556,w:898,h:861};let labels=drawCoast(m);
 pathLine(m,.69,t);
 const [sx,sy]=labels.sam;
 stroke(sx+5,sy-6,sx+106,sy-66,color.white,4);
 const pinX=Math.min(735,sx+42);paintRect(pinX,sy-116,226,71,color.paper);label('SAMOA',pinX+18,sy-71,27,color.ink,800);
 label('AUSTRALIA',150,1022,27,color.ink,800);
 label('NEW ZEALAND',490,1322,24,color.white,800);
 g.restore();
 const k=out((t-4.2)/1.0);
 g.save();g.globalAlpha=k;
 dataStripe('INTERNATIONAL DATE LINE',106,1464,865);
 label('Boundary shown schematically',110,1593,25,color.mist,700);
 g.restore();
}
function frame3(t){
 deco(color.paper,true);mast(3,'The cost of a calendar',true);
 heading('A business problem.',90,338,90,color.ink,910);
 label('THE TRADING WEEK',97,420,26,color.coral,800,4);
 const row=(y,country,days,shift,accent)=>{
  paintRect(93,y,897,188,color.white);rule(93,y,897,accent,7);label(country,115,y+52,28,color.ink,800);
  for(let i=0;i<7;i++){let x=114+i*121;paintRect(x,y+80,101,82,days[i]==='W'?color.ink:'#D1D9D4');
    label(['M','T','W','T','F','S','S'][i],x+38,y+130,29,days[i]==='W'?color.white:'#7C8E91',800)}
 };
 const v=out((t-.4)/1.2);g.save();g.globalAlpha=v;
 row(540,'SAMOA     /     OLD CALENDAR',['W','W','W','W','W','X','X'],0,color.coral);
 row(788,'AUSTRALIA / NEW ZEALAND',['W','W','W','W','W','X','X'],1,color.gold);
 g.restore();
 // Temporal misalignment is revealed as translucent weekend barriers.
 let k=out((t-3)/1.5);g.save();g.globalAlpha=k;
 paintRect(615,530,235,455,'#D578642D');stroke(610,537,610,976,color.coral,7,[20,12]);
 label('LESS OVERLAP',114,1128,50,color.ink,800);
 heading('More friction.',112,1270,87,color.ink);
 g.restore();label('Calendar days can change economics.',112,1366,25,color.ink,700);
}
function frame4(t){
 deco('#10283B');mast(4,'A Pacific decision');
 heading('Move the calendar.',100,350,88,color.white);
 heading('Change the week.',100,462,90,color.gold);
 const m={x:91,y:535,w:895,h:885};let marks=drawCoast(m);
 let q=out((t-2.0)/2);
 pathLine(m,.49,0);
 g.save();g.globalAlpha=q;pathLine(m,.74,0);g.restore();
 const [sx,sy]=marks.sam;
 g.strokeStyle=color.coral;g.lineWidth=8;g.beginPath();g.arc(sx,sy,47,Math.PI*.2,Math.PI*(.2+1.9*q));g.stroke();
 if(t>3.7){let a=out((t-3.7)/1.1);g.save();g.globalAlpha=a;
 paintRect(101,1448,880,175,color.paper);
 dataTitle('SAME ISLAND.',135,1520,47,color.ink,805);
 dataTitle('NEW DAY.',135,1584,51,color.coral,805);
 g.restore()}
 label('SCHEMATIC SHIFT / LOCAL CALENDAR',105,1665,20,color.mist,700,1);
}
function frame5(t){
 deco('#152F43');mast(5,'Midnight on 29 December');
 heading('Midnight.',102,370,108,color.white);
 const appear=out((t-.2)/1.0);g.save();g.globalAlpha=appear;
 printClock(540,947,368,clamp((t-1.6)/3.5));
 g.restore();
 const z=out((t-3.4)/.9);
 g.save();g.globalAlpha=z;
 paintRect(110,1380,859,174,color.paper);
 dataTitle('THU 29   →   SAT 31',149,1475,57,color.ink,808);
 label('The hands moved. The date jumped.',124,1624,25,color.white,700);
 g.restore();
}
function frame6(t){
 deco('#1B3240');mast(6,'The law accounted for the lost day');
 heading('The law thought',97,336,95,color.white);
 heading('of the workers.',97,449,95,color.gold);
 let up=out((t-.3)/1.2);g.save();g.globalAlpha=up;g.translate(0,(1-up)*140);
 texturePanel(101,561,855,849);
 label('SAMOA   /   ACT 6 OF 2011',145,658,26,color.ink,800,2);
 stroke(143,682,910,682,color.ink,3);
 heading('International',141,771,65,color.ink,752,600);
 heading('Date Line Act',141,853,66,color.ink,760,600);
 label('SECTION 8',145,960,30,color.coral,800,3);
 label('EFFECT ON PAY AND ALLOWANCES',145,1018,25,color.ink,800);
 for(let i=0;i<7;i++){let yy=1073+i*39;rule(144,yy,i%2===0?715:610,'#22384944',10)}
 const highlight=out((t-2.5)/1.7);paintRect(138,1232,747*highlight,64,'#C8A26B88');
 label('PAY FOR NORMAL HOURS LOST',154,1278,29,color.ink,800);
 g.restore();
 const c=out((t-4.5)/1.0);g.save();g.globalAlpha=c;stamp2('PAID',770,1396,.10);g.restore();
 label('SOURCE: INTERNATIONAL DATE LINE ACT 2011, §8',112,1655,19,color.mist,800);
}
function frame7(t){
 deco(color.deep);mast(7,'Curio Bureau');
 let a=out((t-.15)/1.1);g.save();g.globalAlpha=a;g.translate(0,(1-a)*75);
 heading('Time is also',110,483,100,color.white,840);
 heading('an agreement.',110,614,99,color.white,855);
 rule(110,667,700,color.gold,9);
 g.restore();
 const b=out((t-1.5)/1.1);
 g.save();g.globalAlpha=b;
 label('AND SAMOA REWROTE ONE.',111,808,39,color.coral,800,1);
 // Tall documentary feature rule connecting claim to signature.
 stroke(110,916,110,1250,color.gold,6);
 label('DECEMBER 2011   /   THE PACIFIC',146,1007,26,color.mist,800,1.4);
 label('THE DAY THAT DISAPPEARED',146,1073,25,color.white,800,1.1);
 g.restore();
 const c=out((t-2.6)/1.0);g.save();g.globalAlpha=c;
 heading('Curio Bureau',110,1313,108,color.white,850);
 label('STORIES, SYSTEMS, AND SURPRISES.',114,1388,22,color.gold,800,2.3);
 g.restore();
}
// Replace former slideshow scenes with the properly art-directed editorial composition.
scenes.splice(0,scenes.length,frame0,frame1,frame2,frame3,frame4,frame5,frame6,frame7);
function captionsAt(sec){
 if(CAPTION_CUES.length<25)return;
 const line=CAPTION_CUES.find(x=>sec>=x.start&&sec<x.end);
 if(!line)return;
 const f=Math.min(1,(sec-line.start)*9,(line.end-sec)*12);
 g.save();g.globalAlpha=clamp(f,.0,1);
 // Reserved lower third, always within mobile-platform safety zone.
 paintRect(80,1450,920,182,'#081521E9',10);rule(128,1463,125,color.gold,5);
 let words=line.text.split(' '),a=[''];typeface(44,color.white,800);
 for(const word of words){let ix=a.length-1,trial=a[ix]?a[ix]+' '+word:word;
  if(g.measureText(trial).width>792&&a[ix])a.push(word);else a[ix]=trial;
 }
 if(a.length>2){a=[line.text.slice(0,28),line.text.slice(28)]}
 for(let j=0;j<a.length;j++){let size=44;typeface(size,color.white,800);
   while(g.measureText(a[j]).width>792 && size>26){size--;typeface(size,color.white,800)}
   g.textAlign='center';g.fillText(a[j],540,a.length===1?1565:1525+j*68);
 }
 g.restore();
}
const originalRender=renderAt;
renderAt=function(sec){
 qa.issues.length=0;qa.titles.length=0;
 originalRender(sec);
 captionsAt(sec);
};
window.renderAt=renderAt;
window.setTime=sec=>player.seek(sec);
window.setFrame=f=>player.seek(f/FPS);
window.renderFrame=f=>renderAt(f/FPS);
window.getDuration=()=>D;
window.getFPS=()=>FPS;
window.inspectFrame=sec=>{renderAt(sec);return{at:sec,font:'Playfair Display and Manrope',geodata:qa.mapLoaded,captionCount:qa.captionCount,issues:qa.issues.slice(),titles:qa.titles.slice()}};
// Original synth was effectively inaudible; replace with consciously composed editorial score.
const CUE_FILES={
 sweep:'mixkit-fast-small-sweep-transition-166.wav',
 arrow:'mixkit-arrow-whoosh-1491.wav',
 click:'mixkit-interface-device-click-2577.wav',
 type:'mixkit-mechanical-typewriter-single-hit-1382.wav',
 fast:'Fast-woosh.wav',
 riser:'ES_Riser Metallic - SFX Producer.mp3',
 popup:'Pop-up-woosh.mp3',
 cinematic:'mixkit-cinematic-whoosh-fast-transition-1492.wav',
 chime:'mixkit-retro-confirmation-tone-2860.wav',
 tick:'Mouse click.mp3'
};
const SCORE_CUES=[
 [0.25,'sweep',.37,'headline entrance'],[1.6,'type',.39,'archive calendar reveal'],
 [2.7,'popup',.43,'calendar date settles'],[4.8,'cinematic',.45,'missing day stamp'],
 [7.7,'arrow',.38,'date change'],[8.25,'fast',.50,'paper slide 29'],
 [9.8,'sweep',.45,'second calendar'],[11.6,'click',.38,'deleted Friday'],
 [13.2,'type',.32,'news confirmation'],[15.5,'riser',.38,'map handoff'],
 [16.2,'cinematic',.38,'geo map enters'],[18.4,'popup',.35,'Samoa locator'],
 [20.6,'arrow',.40,'date line trace'],[22.7,'chime',.21,'map key'],
 [24.7,'fast',.48,'map to grid'],[25.3,'type',.40,'calendar grid starts'],
 [26.8,'click',.35,'schedule region A'],[28.4,'tick',.48,'schedule region B'],
 [30.1,'sweep',.40,'week offset'],[32.6,'chime',.28,'business comparison'],
 [33.7,'arrow',.45,'map reset'],[34.5,'cinematic',.45,'return to Samoa'],
 [36.7,'riser',.32,'date line shifts'],[38.6,'click',.34,'new day marker'],
 [40.6,'chime',.28,'week realignment'],[41.7,'sweep',.41,'to clock'],
 [42.3,'fast',.35,'clock appears'],[44.3,'tick',.48,'first clock tick'],
 [45.1,'tick',.53,'second clock tick'],[45.9,'tick',.58,'third clock tick'],
 [46.7,'tick',.65,'fourth clock tick'],[47.4,'cinematic',.62,'midnight leap'],
 [49.2,'click',.44,'Saturday locks'],[50.7,'sweep',.42,'clock to act'],
 [51.3,'type',.44,'act enters'],[52.5,'type',.32,'act section'],
 [54.3,'sweep',.30,'law highlight'],[56.2,'click',.43,'wage stamp'],
 [57.8,'riser',.36,'insight incoming'],[58.2,'cinematic',.45,'statement reveal'],
 [60.3,'sweep',.28,'lower reveal'],[61.2,'chime',.37,'logo signature'],
 [62.2,'popup',.22,'final line settles']
];
cueEvents.splice(0,cueEvents.length,...SCORE_CUES.map(q=>q.slice(0,3)));
window.CURIO_CUE_SHEET=SCORE_CUES.map(([at,key,vol,trigger])=>({at,key,filename:CUE_FILES[key],vol,trigger}));
const oldInit=player.init.bind(player);
player.init=async function(){await oldInit();if(Object.keys(this.fx).length<10)throw Error('Drive SFX not decoded: '+Object.keys(this.fx).join(','))};
player.attach=function(context,dest,offset,start){
 // WebAudio mastering bus: prevents simultaneous sound events from hard-clipping.
 const comp=context.createDynamicsCompressor();comp.threshold.value=-19;comp.knee.value=20;comp.ratio.value=5;comp.attack.value=.004;comp.release.value=.22;
 const master=context.createGain();master.gain.value=.79;comp.connect(master);master.connect(dest);
 function put(src,volume,bus=comp){let a=context.createGain();a.gain.value=volume;src.connect(a);a.connect(bus);return src}
 for(const [at,key,vol] of cueEvents){
  const buffer=player.fx[key];if(!buffer){qa.issues.push({missingSFX:key});continue}
  if(at+buffer.duration<=offset)continue;
  const o=context.createBufferSource();o.buffer=buffer;
  put(o,vol);const begin=Math.max(at,offset);o.start(start+begin-offset,Math.max(0,offset-at));player.sources.push(o);
 }
 if(player.voice&&offset<player.voice.duration){
  const v=context.createBufferSource();v.buffer=player.voice;put(v,.98);v.start(start,offset);player.sources.push(v);
 }
 const chords=[[130.81,164.81,196,261.63],[146.83,185,220,293.66],[123.47,155.56,185,246.94],[130.81,164.81,196,261.63]];
 for(let bar=0;bar<32;bar++){
  const at=bar*2;if(at+2<=offset)continue;
  const st=Math.max(at,offset),dur=Math.min(2,at+2-st),when=start+st-offset;
  const chord=chords[Math.floor(bar/4)%4];
  // Suspended pad: still perceivable below dialogue, unlike the former .003 oscillators.
  for(let n=0;n<chord.length;n++){
   const o=context.createOscillator(),flt=context.createBiquadFilter(),env=context.createGain();
   o.type=n===0?'triangle':'sine';o.frequency.value=chord[n]*(n===0?.5:1);
   flt.type='lowpass';flt.frequency.value=n===0?850:1550;
   const v=n===0?.075:.040;env.gain.setValueAtTime(.0001,when);env.gain.linearRampToValueAtTime(v,when+.24);
   env.gain.setValueAtTime(v,when+Math.max(.25,dur-.19));env.gain.exponentialRampToValueAtTime(.0001,when+dur);
   o.connect(flt);flt.connect(env);env.connect(comp);o.start(when);o.stop(when+dur+.03);player.sources.push(o);
  }
 }
 // Soft rhythmic motif: musical pulse, not synthetic whoosh.
 for(let beat=0;beat<128;beat++){
  const at=beat*.5;if(at<offset||at>=64)continue;const when=start+at-offset;
  const o=context.createOscillator(),env=context.createGain();o.type='sine';
  let root=chords[Math.floor(beat/16)%4][0];
  const idx=[0,2,1,3][beat%4];o.frequency.value=[root,root*1.5,root*2,root*1.5][idx];
  const vol=beat%4===0?.036:.012;
  env.gain.setValueAtTime(.0001,when);env.gain.linearRampToValueAtTime(vol,when+.012);env.gain.exponentialRampToValueAtTime(.0001,when+.21);
  o.connect(env);env.connect(comp);o.start(when);o.stop(when+.24);player.sources.push(o);
 }
};
if(!qa.mapLoaded||qa.captionCount<35)throw Error('Documentary release dependencies missing: geodata/captions');
renderAt(.01);
