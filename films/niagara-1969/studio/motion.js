'use strict';
/* CURIO BUREAU | FILM 001
   "The Waterfall They Switched Off" — original Vox-inspired editorial film.
   Art direction: Pacific cartography, archival collage, kinetic type, document graphics.
   Deterministic frame-at-time renderer. No stock video or copyrighted Vox artwork.
*/
const W=1080,H=1920,FPS=30,D=64;
const canvas=document.getElementById('film'),g=canvas.getContext('2d',{alpha:false});
const C={navy:'#0D1C2B',navy2:'#162D40',cream:'#F5F0E7',gold:'#C8A26B',coral:'#D57864',mint:'#96B6AF',ink:'#1A2E3C',paper:'#EEE8DC',tan:'#DDD0B9',muted:'#9DAFB7'};
const $=id=>document.getElementById(id);
const clamp=(v,a=0,b=1)=>Math.max(a,Math.min(b,v));
const mix=(a,b,t)=>a+(b-a)*t;
const ease=x=>{x=clamp(x);return x*x*(3-2*x)};
const out=x=>1-Math.pow(1-clamp(x),3);
const p=(t,a,b)=>ease((t-a)/(b-a));
const rand=i=>{let z=Math.sin(i*78.233+1.724)*43758.5453;return z-Math.floor(z)};
const R=(x,y,w,h,c,r=0)=>{g.fillStyle=c;g.beginPath();g.roundRect(x,y,w,h,r);g.fill()};
const stroke=(x1,y1,x2,y2,color,width=3,dash=[])=>{g.strokeStyle=color;g.lineWidth=width;g.setLineDash(dash);g.beginPath();g.moveTo(x1,y1);g.lineTo(x2,y2);g.stroke();g.setLineDash([])};
function txt(s,x,y,size=50,color=C.cream,weight=700,align='left',serif=false){g.fillStyle=color;g.font=(serif?'':'')+weight+' '+size+'px '+(serif?'"Playfair Display",Georgia,serif':'"Manrope",Arial,sans-serif');g.textAlign=align;g.textBaseline='alphabetic';g.fillText(s,x,y);}
function wrapped(s,x,y,maxW,size=49,color=C.cream,leading=1.18,serif=false){
 const words=s.split(' ');let l='',yy=y;
 for(let i=0;i<words.length;i++){const test=l?l+' '+words[i]:words[i];g.font='700 '+size+'px '+(serif?'"Playfair Display",Georgia,serif':'"Manrope",Arial,sans-serif');if(g.measureText(test).width>maxW&&l){txt(l,x,yy,size,color,700,'left',serif);l=words[i];yy+=size*leading}else l=test}
 if(l)txt(l,x,yy,size,color,700,'left',serif);return yy;
}
function poly(points,c,strokeC='',sw=1){g.beginPath();g.moveTo(points[0],points[1]);for(let i=2;i<points.length;i+=2)g.lineTo(points[i],points[i+1]);g.closePath();g.fillStyle=c;g.fill();if(strokeC){g.strokeStyle=strokeC;g.lineWidth=sw;g.stroke()}}
function ring(x,y,r,c,width=3){g.strokeStyle=c;g.lineWidth=width;g.beginPath();g.arc(x,y,r,0,Math.PI*2);g.stroke()}
function dot(x,y,r,c){g.fillStyle=c;g.beginPath();g.arc(x,y,r,0,Math.PI*2);g.fill()}
function shadow(){g.shadowColor='#0005';g.shadowBlur=23;g.shadowOffsetY=20}
function shadowOff(){g.shadowColor='transparent';g.shadowBlur=0;g.shadowOffsetY=0}
function lines(x,y,w,n=6,col='#415768',step=27){for(let i=0;i<n;i++)R(x,y+i*step,w*(0.65+0.35*rand(i+Math.floor(x))),3,col)}
function charSpace(s,x,y,sz,col,spacing=5){g.font='800 '+sz+'px "Manrope",Arial';g.fillStyle=col;g.textAlign='left';for(const ch of s){g.fillText(ch,x,y);x+=g.measureText(ch).width+spacing}}
function arrow(x1,y1,x2,y2,c,w=5){stroke(x1,y1,x2,y2,c,w);const a=Math.atan2(y2-y1,x2-x1);poly([x2,y2,x2-22*Math.cos(a-.52),y2-22*Math.sin(a-.52),x2-22*Math.cos(a+.52),y2-22*Math.sin(a+.52)],c)}
function pill(s,x,y,w,c=C.cream,textColor=C.navy){R(x,y-38,w,57,c,28);txt(s,x+w/2,y,20,textColor,800,'center')}
function under(x,y,w,c=C.gold){R(x,y,w,7,c)}
function paper(x,y,w,h,rotate=0,shade=C.cream){
 g.save();g.translate(x+w/2,y+h/2);g.rotate(rotate);shadow();R(-w/2,-h/2,w,h,shade,3);shadowOff();
 for(let k=0;k<26;k++){let yy=-h/2+k*h/26;stroke(-w/2+15,yy,w/2-15,yy,'#B6A8950C',1)}
 g.restore();
}
function vignette(){let v=g.createRadialGradient(W*.5,H*.4,260,W*.5,H*.5,1370);v.addColorStop(0,'#0000');v.addColorStop(1,'#02071399');R(0,0,W,H,v)}
function noise(){for(let i=0;i<220;i++){const x=rand(i+31)*W,y=rand(i+83)*H;R(x,y,1.4,1.4,i%3===0?'#F5F0E71B':'#0A152319')}}
function base(bg=C.navy){R(0,0,W,H,bg);for(let x=0;x<W;x+=72)stroke(x,0,x,H,'#FFFFFF07',1);for(let y=0;y<H;y+=72)stroke(0,y,W,y,'#FFFFFF06',1)}
function chrome(scene,section){
 R(70,104,44,7,C.gold);charSpace('CURIO BUREAU',135,113,23,C.cream,6);
 txt('FIELD NOTES  /  001',70,169,17,C.muted,700);
 stroke(70,1780,1010,1780,C.cream+'44',2);
 txt(section.toUpperCase(),70,1829,21,C.cream,700);
 txt(('0'+(scene+1)).slice(-2)+' / 08',1010,1829,20,C.gold,800,'right');
}
function textSplash(linesArr,t,x=75,y=390,sz=96){
 linesArr.forEach((s,i)=>{let q=out((t-i*.22)/.75);g.save();g.globalAlpha=q;g.translate((1-q)*-80,(1-q)*25);txt(s,x,y+i*sz*1.06,sz,C.cream,800);g.restore()});
}
function calendarPage(x,y,w,h,num,month,col=C.cream,angle=0,scale=1){
 g.save();g.translate(x+w/2,y+h/2);g.rotate(angle);g.scale(scale,scale);
 shadow();R(-w/2,-h/2,w,h,col,9);shadowOff();R(-w/2,-h/2,w,108,C.coral);txt(month,-w/2+35,-h/2+73,38,C.cream,800);
 txt(num,0,155,225,C.navy,800,'center');stroke(-w/2+40,h/2-107,w/2-40,h/2-107,'#20384A44',3);txt('2011',0,h/2-43,34,C.ink,700,'center');
 for(let i=-1;i<=1;i++)R(i*119-7,-h/2-11,14,39,C.ink,7);g.restore();
}
function timetable(x,y,w,h,heading,clock,text1,accent){
 shadow();R(x,y,w,h,C.paper,8);shadowOff();R(x,y,w,14,accent);txt(heading,x+35,y+70,23,C.ink,800);
 txt(clock,x+35,y+160,72,C.navy,800);
 stroke(x+35,y+191,x+w-35,y+191,'#5B697055',2);
 txt(text1,x+35,y+235,28,C.ink,700);
}
function landscape(x,y,w,h,sea=false){
 g.save();g.translate(x,y);R(0,0,w,h,sea?'#7CA5A3':'#D4C5A8');
 if(sea){R(0,h*.62,w,h*.38,'#557E8E');for(let i=0;i<9;i++)stroke(rand(i+40)*w,h*.67+rand(i+59)*h*.28,rand(i+41)*w,h*.7+rand(i+62)*h*.28,'#F4F0DB55',3)}
 else {poly([0,h*.73,w*.24,h*.27,w*.45,h*.72,w*.69,h*.18,w,h*.67,w,h,0,h],'#99A8A1');poly([0,h*.91,w*.2,h*.47,w*.43,h*.76,w*.55,h*.48,w,h*.9,w,h,0,h],'#617D82')}
 for(let i=0;i<13;i++){let xx=i*w/13, hh=45+rand(i+4)*h*.23;R(xx,h*.62-hh,w/24,hh+10,'#263E4F');for(let j=0;j<3;j++)R(xx+5,h*.63-hh+j*15,3,5,'#E4C28B')}
 g.restore();
}
function newsCutout(x,y,w,h,rot=0){
 g.save();g.translate(x+w/2,y+h/2);g.rotate(rot);paper(-w/2,-h/2,w,h,0);
 R(-w/2+25,-h/2+30,w-50,8,C.navy);txt('THE PACIFIC EDITION',-w/2+30,-h/2+80,33,C.navy,800);
 stroke(-w/2+25,-h/2+100,w/2-25,-h/2+100,'#223948',3);
 txt('A DAY',-w/2+30,-h/2+190,74,C.navy,800);
 txt('DISAPPEARS',-w/2+30,-h/2+258,61,C.navy,800);
 landscape(-w/2+30,-h/2+300,w-60,230,true);
 lines(-w/2+30,-h/2+558,w-60,7,'#22394888',23);
 g.restore();
}
function map(x,y,w,h,zoom=1,labels=true){
 g.save();g.translate(x,y);g.scale(zoom,zoom);
 R(0,0,w,h,'#1D4A60',8);for(let yy=70;yy<h;yy+=85)stroke(0,yy,w,yy,'#B4C9CA26',2);
 for(let xx=65;xx<w;xx+=94)stroke(xx,0,xx,h,'#B4C9CA18',2);
 // Simplified, intentionally schematic Pacific-region coastline silhouettes.
 poly([0,0,192,0,211,55,180,116,227,183,160,221,189,263,118,290,96,383,0,345],'#99B6A6');
 poly([0,450,101,397,200,435,267,518,279,605,238,672,142,663,93,710,0,695],'#B6BFA8');
 poly([225,616,248,632,261,681,252,762,276,800,251,813,226,750],'#C5CEB9');
 poly([488,25,546,13,578,76,562,159,503,179,474,110],'#8EB2AD');
 poly([w-130,0,w,0,w,h*.82,w-54,h*.72,w-85,h*.41,w-117,h*.23],'#C2B39B');
 poly([377,402,393,413,388,441,371,439],'#C9C5A9');
 dot(448,495,8,C.gold);dot(483,468,6,C.cream);dot(582,349,5,C.cream);
 if(labels){txt('AUSTRALIA',45,540,25,C.navy,800);txt('NEW',222,716,18,C.navy,800);txt('ZEALAND',205,746,18,C.navy,800);
 txt('FIJI',370,382,19,C.cream,700);txt('HAWAII',560,283,18,C.cream,700);txt('SAMOA',498,472,24,C.cream,800);}
 g.restore();
}
function dateline(y1,y2,x=566,shift=0){
 g.save();g.setLineDash([15,17]);g.lineWidth=8;g.strokeStyle=C.gold;g.beginPath();g.moveTo(x, y1);g.bezierCurveTo(x-42,y1+160,x+80+shift,y2-170,x+20+shift,y2);g.stroke();g.setLineDash([]);g.restore();
}
function stamp(s,x,y,rot=0){
 g.save();g.translate(x,y);g.rotate(rot);g.strokeStyle=C.coral;g.lineWidth=7;g.strokeRect(-155,-52,310,104);txt(s,0,18,51,C.coral,800,'center');g.restore();
}
function scene0(t){base();chrome(0,'The calendar is an agreement');
 const k=p(t,0.2,1.1);g.save();g.translate(0,-(1-k)*85);g.globalAlpha=k;
 txt('ONE NIGHT.',80,410,101,C.cream,800);txt('ONE COUNTRY.',80,530,97,C.cream,800);g.restore();
 let v=p(t,2.1,3.2);txt('ONE MISSING',80,730,100,C.gold,800);g.save();g.globalAlpha=v;txt('DAY.',80,851,208,C.cream,800);g.restore();
 let q=p(t,3.0,5);g.save();g.translate(420+(1-q)*260,1000);g.rotate(-.10+q*.08);
 paper(-275,-80,610,570,0);R(-240,-45,540,100,C.coral);txt('DECEMBER',-208,23,51,C.cream,800);txt('30',28,316,284,C.navy,800,'center');g.restore();
 stroke(80,940,996,940,C.cream+'33',2);
 if(t>5.3){g.save();g.globalAlpha=p(t,5.3,6.3);stamp('DELETED',550,1475,-.16);g.restore()}
 txt('SAMOA  /  2011',80,1675,25,C.gold,800);
}
function scene1(t){base('#122536');chrome(1,'Friday vanished');
 txt('THURSDAY',80,335,28,C.muted,800);txt('DEC 29',78,454,104,C.cream,800);
 stroke(80,511,995,511,C.cream+'55',4);
 const flip=p(t,.7,2.4),jump=p(t,3.4,4.6);
 calendarPage(110,620,620,820,'29','DECEMBER',C.cream,-.07,1);
 g.save();g.translate(440,1010);g.rotate(-flip*.3);g.globalAlpha=1-flip;
 calendarPage(-330,-400,620,820,'30','DECEMBER',C.paper,.025,Math.max(.2,1-flip*.35));g.restore();
 g.save();g.globalAlpha=p(t,2.0,3.0);calendarPage(390+(1-jump)*490,755,510,670,'31','DECEMBER',C.cream,.12,.9);g.restore();
 if(t>3.2){g.save();g.globalAlpha=p(t,3.2,4.4);stamp('NO FRIDAY',505,1540,-.1);g.restore()}
 txt('29  →  31',82,1676,72,C.gold,800);
 if(t>5){txt('THE 30TH NEVER ARRIVED.',78,1736,30,C.cream,700)}
}
function scene2(t){base('#0F2638');chrome(2,'A line across the ocean');
 txt('THE WORLD',75,364,94,C.cream,800);txt('HAS A SEAM.',75,470,105,C.gold,800);
 const v=p(t,.5,2.0);
 g.save();g.translate(0,(1-v)*360);g.globalAlpha=v;shadow();R(80,608,920,845,C.cream,5);shadowOff();map(111,640,858,765,.97,true);g.restore();
 const d=p(t,2.2,5);g.save();g.globalAlpha=d;dateline(652,1360,660,-130*d);
 R(550,1395,410,69,C.navy);txt('INTERNATIONAL DATE LINE',565,1439,22,C.cream,800);g.restore();
 if(t>5.1){R(80,1540,920,148,'#203D50');txt('Not a wall.',110,1605,41,C.cream,700,true);txt('A decision about tomorrow.',110,1660,34,C.mint,600)}
}
function scene3(t){base(C.paper);chrome(3,'Business weeks out of sync');
 txt('ONE OCEAN.',75,365,107,C.ink,800);txt('TWO CALENDARS.',75,472,87,C.coral,800);
 // Side-by-side documentary schedule sheets
 const u=p(t,.2,1.2);g.save();g.globalAlpha=u;g.translate(0,(1-u)*110);
 timetable(78,625,435,342,'SAMOA','FRI','Still Thursday',C.coral);
 timetable(566,625,435,342,'AUSTRALIA','SAT','A day ahead',C.gold);
 g.restore();
 for(let i=0;i<7;i++){
   const day=['M','T','W','T','F','S','S'][i],x=80+i*133;
   txt(day,x+59,1106,25,C.ink,800,'center');
   R(x,1154,113,148,i<5?'#B7C1B9':'#CAD0C6');
   if(i<5){R(x+7,1164,99,128,C.navy2);txt(day,x+58,1242,45,C.cream,700,'center');}
 }
 const b=p(t,2,4);R(83,1370,890*b,12,C.coral);R(83,1405,890,7,C.ink+'44');
 txt('A DIFFICULT TIME TO DO BUSINESS',82,1495,32,C.ink,800);
 const sh=p(t,5.1,6.7);g.save();g.globalAlpha=sh;shadow();R(68,1550,940,175,C.navy);shadowOff();txt('Monday here.',105,1620,46,C.cream,700,true);txt('Tuesday there.',105,1692,52,C.gold,700,true);g.restore();
}
function scene4(t){base();chrome(4,'The Pacific connection');
 txt('A DIFFERENT',70,368,97,C.cream,800);txt('SIDE OF TIME.',70,474,98,C.gold,800);
 // A desk of overlapping clipped editorial artifacts
 const b=p(t,.2,1.7);g.save();g.globalAlpha=b;g.translate(0,(1-b)*210);
 g.save();g.translate(535,1050);g.rotate(.045);shadow();R(-450,-420,900,750,C.paper,3);shadowOff();map(-415,-385,830,681,1,false);g.restore();
 dateline(670,1320,695,-65*p(t,2,4));ring(577,1095,65,C.gold,6);dot(577,1095,15,C.coral);
 g.restore();
 let q=p(t,2.5,4.5);g.save();g.globalAlpha=q;
 shadow();R(92,1370,890,215,C.cream);shadowOff();
 txt('SAMOA',125,1450,69,C.ink,800);txt('↗  24 HOURS',124,1542,56,C.coral,800);
 g.restore();
 if(t>5){txt('CHANGE THE DATE LINE.',75,1690,31,C.cream,700)}
}
function scene5(t){base('#14293B');chrome(5,'Midnight becomes Saturday');
 const reveal=p(t,.2,1.5);
 txt('MIDNIGHT.',78,372,99,C.cream,800);
 g.save();g.globalAlpha=reveal;g.translate(0,(1-reveal)*130);
 // Huge analog clock, cutout styled with annotations.
 shadow();dot(541,1025,364,C.paper);shadowOff();ring(541,1025,364,C.gold,9);ring(541,1025,328,C.navy,2);
 for(let i=0;i<12;i++){let a=i*Math.PI/6-Math.PI/2;let ra=305;dot(541+Math.cos(a)*ra,1025+Math.sin(a)*ra,i%3===0?10:6,C.navy)}
 const hands=p(t,2,5.7);const a=-Math.PI/2+hands*Math.PI*2;
 stroke(541,1025,541+Math.cos(a)*228,1025+Math.sin(a)*228,C.coral,19);stroke(541,1025,541+Math.cos(a*2)*151,1025+Math.sin(a*2)*151,C.navy,24);dot(541,1025,25,C.gold);g.restore();
 R(94,1480,891,133,C.navy2);txt('THURSDAY → SATURDAY',125,1566,56,C.cream,800);
 let s=p(t,4,5.8);R(94,1637,891*s,15,C.gold);
}
function scene6(t){base(C.paper);chrome(6,'What happened to the missing day');
 const reveal=p(t,.3,1.4);
 newsCutout(60+(1-reveal)*230,390,690,1050,-.04);
 g.save();g.globalAlpha=p(t,1.9,3);g.translate(740,1090);g.rotate(.11);
 shadow();R(-210,-260,420,580,C.navy,2);shadowOff();
 R(-160,-210,320,14,C.gold);txt('PAYSLIP',-155,-143,42,C.cream,800);
 lines(-155,-100,295,6,'#F5F0E788',40);
 stroke(-155,135,159,135,C.cream+'55',3);txt('FRIDAY',-155,193,40,C.gold,700);
 txt('PAID',-155,253,70,C.cream,800);g.restore();
 const s=p(t,4.1,5.6);g.save();g.globalAlpha=s;stamp('STILL PAID',546,1660,-.08);g.restore();
}
function scene7(t){base('#091723');chrome(7,'Curio Bureau');
 // Calendar becomes a newspaper heading then a philosophical end card.
 const k=p(t,.2,1.6);g.save();g.globalAlpha=k;g.translate(0,(1-k)*65);
 txt('A DAY',70,520,183,C.cream,800);txt('CAN',73,680,183,C.cream,800);txt('DISAPPEAR.',70,843,115,C.gold,800);
 under(72,903,620,C.gold);g.restore();
 const q=p(t,2.4,3.4);
 g.save();g.globalAlpha=q;txt('TIME IS ALSO',73,1155,79,C.cream,700,true);
 txt('AN AGREEMENT.',73,1252,72,C.cream,700,true);g.restore();
 g.save();g.globalAlpha=p(t,4.1,5);stroke(75,1450,1000,1450,C.gold,5);txt('Curio Bureau',76,1585,99,C.cream,700,true);
 charSpace('STORIES. SYSTEMS. SURPRISES.',79,1650,19,C.gold,4);g.restore();
}
const scenes=[scene0,scene1,scene2,scene3,scene4,scene5,scene6,scene7];
const starts=[0,8,16,25,34,42,51,58,64],sections=['The calendar is an agreement','Friday vanished','A line across the ocean','Business weeks out of sync','The Pacific connection','Midnight becomes Saturday','What happened to the missing day','Curio Bureau'];
function sceneIndex(t){let k=0;while(k<7&&t>=starts[k+1])k++;return k}
function renderAt(sec){const t=clamp(sec,0,D-.0001);let i=sceneIndex(t),local=t-starts[i];
 g.save();scenes[i](local);g.restore();
 if(i>0&&local<.75){const f=out(local/.75);g.save();g.beginPath();g.rect(0,0,W*(1-f),H);g.clip();scenes[i-1](starts[i]-starts[i-1]-.03);g.restore();}
 // The restraint of print grain is part of the editorial identity.
 vignette();noise();R(0,H-5,W*(t/D),5,C.gold);
}
window.renderAt=renderAt;window.setTime=t=>{player.seek(t)};window.setFrame=n=>{player.seek(n/FPS)};
const embedded=window.CURIO_SFX||{};
const cURL=b=>'data:audio/wav;base64,'+b;
const cueEvents=[
 [0.45,'sweep',.10],[2.6,'type',.24],[5.55,'click',.40],
 [8.25,'sweep',.22],[10.25,'arrow',.15],[12.2,'click',.36],[15.3,'type',.20],
 [16.4,'sweep',.14],[18.6,'arrow',.15],[22.3,'click',.18],
 [25.4,'type',.19],[27.8,'click',.20],[30.4,'sweep',.16],
 [34.4,'arrow',.24],[38.1,'sweep',.17],
 [42.25,'sweep',.10],[44.9,'click',.30],[47.3,'arrow',.18],
 [51.5,'type',.28],[54.2,'click',.26],[56.5,'type',.16],
 [58.4,'sweep',.10],[61.9,'click',.14]
];
const player={time:0,playing:false,exporting:false,audioCtx:null,voice:null,fx:{},sources:[],started:0,raf:0,
 async init(){
   if(!this.audioCtx)this.audioCtx=new (window.AudioContext||window.webkitAudioContext)();
   await this.audioCtx.resume();
   for(const [name,b64] of Object.entries(embedded)){if(this.fx[name]||!b64)continue;
     try{const res=await fetch(cURL(b64));this.fx[name]=await this.audioCtx.decodeAudioData(await res.arrayBuffer())}catch(e){console.warn(name,e)}
   }
 },
 stopSources(){for(const s of this.sources){try{s.stop()}catch(e){}}this.sources=[]},
 attach(context,dest,offset,start){
   const connect=(src,vol)=>{const gain=context.createGain();gain.gain.value=vol;src.connect(gain);gain.connect(dest);return src};
   for(const [at,key,vol] of cueEvents){const buffer=this.fx[key];if(!buffer||at+buffer.duration<=offset)continue;
     const begin=Math.max(at,offset);const src=connect(context.createBufferSource(),vol);src.buffer=buffer;src.start(start+begin-offset,Math.max(0,offset-at));this.sources.push(src)}
   if(this.voice&&offset<this.voice.duration){const src=connect(context.createBufferSource(),1.12);src.buffer=this.voice;src.start(start,offset);this.sources.push(src)}
   // Understated, deterministic documentary score with soft suspended chords and restrained pulses.
   const chord=[[130.81,164.81,196,261.63],[146.83,174.61,220,293.66],[123.47,155.56,185,246.94],[130.81,164.81,196,261.63]];
   for(let bar=0;bar<32;bar++){let at=bar*2; if(at+2<=offset)continue;
     let startAt=Math.max(at,offset),dur=Math.min(2,at+2-startAt);
     const notes=chord[Math.floor(bar/4)%4];
     for(let n=0;n<notes.length;n++){let o=context.createOscillator(),gain=context.createGain();
       o.type=n===0?'triangle':'sine';o.frequency.value=notes[n]*(n===0?.5:1);
       const st=start+(startAt-offset),v=(n===0?.007:.0036);
       gain.gain.setValueAtTime(.00001,st);gain.gain.linearRampToValueAtTime(v,st+.15);
       gain.gain.setValueAtTime(v,st+Math.max(.15,dur-.23));gain.gain.exponentialRampToValueAtTime(.00001,st+dur);
       o.connect(gain);gain.connect(dest);o.start(st);o.stop(st+dur+.02);this.sources.push(o)
     }
   }
 },
 async play(){await this.init();this.pause();if(this.time>=D-.1)this.time=0;const c=this.audioCtx;this.attach(c,c.destination,this.time,c.currentTime+.05);
   this.started=performance.now()-this.time*1000;this.playing=true;$('play').textContent='Ⅱ Pause';
   const tick=()=>{if(!this.playing)return;const t=(performance.now()-this.started)/1000;
     if(t>=D){this.pause();this.seek(0);return}this.time=t;renderAt(t);$('seek').value=t;this.raf=requestAnimationFrame(tick)};tick();
 },
 pause(){this.playing=false;cancelAnimationFrame(this.raf);this.stopSources();$('play').textContent='▶ Play'},
 seek(t){let playing=this.playing;this.pause();this.time=clamp(t,0,D);renderAt(this.time);$('seek').value=this.time;if(playing)this.play()}
};
window.player=player;
$('seek').addEventListener('input',e=>player.seek(+e.target.value));
$('play').onclick=()=>player.playing?player.pause():player.play();
$('replay').onclick=()=>{player.seek(0);player.play()};
$('voiceFile').addEventListener('change',async e=>{const file=e.target.files?.[0];if(!file)return;await player.init();
 const data=await file.arrayBuffer();player.voice=await player.audioCtx.decodeAudioData(data);$('voiceStatus').textContent='Narration loaded: '+file.name+' ('+player.voice.duration.toFixed(1)+'s)';});
async function exportFilm({download=true}={}){
 player.pause();await player.init();const c=player.audioCtx;
 if(!window.MediaRecorder||!canvas.captureStream)throw new Error('Chrome or Edge required for WebM export');
 const t=canvas.captureStream(0).getVideoTracks()[0];
 if(!t.requestFrame)throw new Error('Manual capture frame control unavailable');
 const dest=c.createMediaStreamDestination();let stream=new MediaStream([t,...dest.stream.getAudioTracks()]);
 const types=['video/webm;codecs=vp9,opus','video/webm;codecs=vp8,opus','video/webm'];const mime=types.find(x=>MediaRecorder.isTypeSupported(x))||'';
 const recorder=new MediaRecorder(stream,{mimeType:mime,videoBitsPerSecond:9200000,audioBitsPerSecond:192000});
 const chunks=[];const done=new Promise((resolve,reject)=>{recorder.ondataavailable=e=>{if(e.data.size)chunks.push(e.data)};recorder.onstop=()=>resolve(new Blob(chunks,{type:'video/webm'}));recorder.onerror=e=>reject(e.error)});
 player.exporting=true;$('status').textContent='Rendering 0%';
 renderAt(0);t.requestFrame();recorder.start(1000);
 let begin=c.currentTime+.08;
 player.attach(c,dest,0,begin);
 await new Promise(resolve=>{let last=-1;const tick=()=>{
   let sec=Math.max(0,c.currentTime-begin),fr=Math.min(FPS*D-1,Math.floor(sec*FPS));
   if(fr>=0&&fr!==last){renderAt(fr/FPS);t.requestFrame();last=fr}
   if(sec>=D){resolve();return}
   if(fr%30===0&&fr>=0)$('status').textContent='Rendering '+Math.round(100*sec/D)+'%';
   setTimeout(tick,5)
 };tick()});
 player.stopSources();recorder.stop();let result=await done;t.stop();dest.stream.getTracks().forEach(x=>x.stop());
 player.exporting=false;$('status').textContent='WebM exported · '+(result.size/1048576).toFixed(1)+' MB'+(player.voice?' · narration mixed':' · NO NARRATION: PREVIEW ONLY');
 if(download){let u=URL.createObjectURL(result),a=document.createElement('a');a.href=u;a.download='Curio_Bureau_Niagara_1969_Editorial.webm';document.body.append(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(u),60000)}
 return result;
}
window.exportCurioWebM=exportFilm;
$('export').onclick=()=>exportFilm().catch(e=>{$('status').textContent=e.message;console.error(e)});
renderAt(.01);
