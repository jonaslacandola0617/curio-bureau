/* CURIO BUREAU / CENTRALIA 002 / ORIGINAL EDITORIAL MOTION
   Film 64.0s @30fps, 1080x1920. 2D/2.5D documentary motion;
   no copied Vox visuals, no placeholder buildings or maps.
*/
const CT=window.CURIO_CAPTIONS||[],CG=window.CURIO_GEO||[];
const PA={night:'#0D1C2B',deep:'#081521',paper:'#F5F0E7',sand:'#E5D7C2',gold:'#C8A26B',coral:'#D57864',ember:'#F0935C',flame:'#F9C56A',slate:'#213C51',steel:'#718591',char:'#222B33',coal:'#171C23',earth:'#766758',clay:'#A38B72',cream:'#EDE8DA',green:'#859A8D'};
const CURIO_SAFE={l:84,r:996,titleTop:126,titleBottom:1420,captionTop:1450,captionBottom:1631};
const QA_C={issues:[],titles:[],geodata:CG.length>=8&&CG.some(f=>f.name==='Pennsylvania'),captions:CT.length,audio:0};
window.CURIO_QA={get issues(){return QA_C.issues}, get mapLoaded(){return QA_C.geodata},get captionCount(){return QA_C.captions}};
const cbClamp=(v,a=0,b=1)=>Math.max(a,Math.min(b,v));
const cbOut=x=>1-Math.pow(1-cbClamp(x),3);
const cbSm=x=>{x=cbClamp(x);return x*x*(3-2*x)};
const cbP=(t,a,b)=>cbSm((t-a)/(b-a));
const cbL=(a,b,k)=>a+(b-a)*k;
const cbR=(x,y,w,h,c,r=0)=>{g.beginPath();g.roundRect(x,y,w,h,r);g.fillStyle=c;g.fill()};
const cbDot=(x,y,r,c)=>{g.beginPath();g.arc(x,y,r,0,Math.PI*2);g.fillStyle=c;g.fill()};
const cbStroke=(pts,c=PA.paper,w=2,dash=[])=>{g.beginPath();g.moveTo(pts[0],pts[1]);for(let i=2;i<pts.length;i+=2)g.lineTo(pts[i],pts[i+1]);g.strokeStyle=c;g.lineWidth=w;g.setLineDash(dash);g.stroke();g.setLineDash([])};
const cbPoly=(pts,fill,sc='',sw=2)=>{g.beginPath();g.moveTo(pts[0],pts[1]);for(let i=2;i<pts.length;i+=2)g.lineTo(pts[i],pts[i+1]);g.closePath();g.fillStyle=fill;g.fill();if(sc){g.strokeStyle=sc;g.lineWidth=sw;g.stroke()}};
function cbLabel(s,x,y,size=23,color=PA.paper,weight=700,space=0){
 g.font=weight+' '+size+'px "Manrope",Arial,sans-serif';g.fillStyle=color;g.textAlign='left';g.textBaseline='alphabetic';
 if(!space){if(g.getTransform().is2D&&Math.abs(g.getTransform().a-1)<.001&&Math.abs(g.getTransform().e)<.001 && y<1380)while(g.measureText(s).width+x>CURIO_SAFE.r&&size>14){size--;g.font=weight+' '+size+'px "Manrope",Arial,sans-serif'}g.fillText(s,x,y);return}
 let xx=x;for(const ch of s){g.fillText(ch,xx,y);xx+=g.measureText(ch).width+space}
}
function cbTitle(s,x,y,size=96,color=PA.paper,max=890){
 let px=Math.min(max,CURIO_SAFE.r-x),z=size;
 do{g.font='600 '+z+'px "Playfair Display",Georgia,serif';if(g.measureText(s).width<=px)break;z--}while(z>26);
 const width=g.measureText(s).width;if(x+width>CURIO_SAFE.r+1||x<CURIO_SAFE.l||y>CURIO_SAFE.titleBottom||y<CURIO_SAFE.titleTop)QA_C.issues.push({type:'title',text:s,x,y,width,size:z});
 g.fillStyle=color;g.textAlign='left';g.textBaseline='alphabetic';g.fillText(s,x,y);QA_C.titles.push({s,x,y,z});
}
function cbNumber(s,x,y,size,color=PA.paper){g.font='800 '+size+'px "Manrope",Arial';g.textAlign='left';g.fillStyle=color;g.fillText(s,x,y)}
function cbNoise(seed=0){
 for(let i=0;i<145;i++){const x=rand(i*7+113+seed)*W,y=rand(i*5+17+seed)*H;cbR(x,y,1.4,1.4,i%4?'#FFFFFF12':'#00000021')}
}
function cbBg(c=PA.night,seed=0){
 cbR(0,0,W,H,c);const gr=g.createLinearGradient(0,0,W,H);gr.addColorStop(0,'#FFFFFF0D');gr.addColorStop(.56,'#FFFFFF00');gr.addColorStop(1,'#0000002E');cbR(0,0,W,H,gr);
 for(let i=0;i<30;i++)cbStroke([0,i*74,W,i*74],'#F5F0E707',1);
 cbNoise(seed)
}
function cbRule(x,y,w,c=PA.gold,h=6){cbR(x,y,w,h,c)}
function cbMast(n,section,dark=false){
 let cl=dark?PA.night:PA.paper;cbRule(87,111,42,PA.gold,6);cbLabel('CURIO BUREAU',147,128,20,cl,800,4.3);
 cbLabel('FIELD FILE / 002',88,181,16,dark?'#61747D':'#97ACB9',800,2.4);
 cbStroke([87,1746,995,1746],dark?'#30455855':'#ECF3F74A',2);
 cbLabel(section.toUpperCase(),87,1791,18,cl,800,1.1);g.textAlign='right';g.font='800 18px Manrope,Arial';g.fillStyle=PA.gold;g.fillText('0'+(n+1)+' / 08',993,1791);g.textAlign='left';
}
function cbPanel(x,y,w,h,fill=PA.paper,angle=0,shadow=true){
 g.save();g.translate(x+w/2,y+h/2);g.rotate(angle);
 if(shadow){g.shadowBlur=34;g.shadowColor='#03080D70';g.shadowOffsetY=20}
 cbR(-w/2,-h/2,w,h,fill,3);g.restore();
}
function cbTypeBars(x,y,w,n=5,c='#22394866'){
 for(let i=0;i<n;i++)cbR(x,y+i*32,w*(.59+.41*rand(i+Math.floor(x))),6,c)
}
function cbTypedDocument(x,y,w,h,kind='report'){
 cbPanel(x,y,w,h,PA.cream,-.014,true);
 g.save();g.translate(x,y);g.rotate(-.014);
 cbLabel(kind==='report'?'UNITED STATES / 1983':'PENNSYLVANIA / MAY 1962',36,78,24,PA.night,800,1.7);
 cbStroke([30,95,w-30,95],PA.night,3);
 cbTitle(kind==='report'?'THE HIDDEN COST':'A FIRE UNDER',35,182,56,PA.night,w-65);
 cbTitle(kind==='report'?'OF A MINE FIRE':'THE TOWN',35,251,53,PA.night,w-65);
 cbRule(34,281,w-65,PA.coral,7);
 cbTypeBars(36,318,w-75,5,'#233D4A73');
 cbR(34,503,w-69,114,PA.night);cbLabel(kind==='report'?'1983 FEDERAL STUDY':'PROBABLE ORIGIN',49,550,22,PA.paper,800);
 cbLabel(kind==='report'?'EXTINGUISH: $663M':'DUMP FIRE → COAL',48,591,30,PA.gold,800);
 g.restore()
}
function cbWindow(x,y,w=30,h=43,lit=false){
 cbR(x,y,w,h,lit?'#E6BF7B':'#1D3846',2);cbStroke([x+w/2,y,x+w/2,y+h],'#B0B6AB',2);cbStroke([x,y+h*.55,x+w,y+h*.55],'#B0B6AB',2);cbR(x-3,y+h-6,w+6,6,'#3B4C54')
}
function cbHouse(cx,base,scale=1,shape=0,brightness=1){
 g.save();g.translate(cx,base);g.scale(scale,scale);g.globalAlpha*=brightness;
 const w=165+shape*12,h=156+shape*5;
 g.shadowColor='#050C14A0';g.shadowBlur=14;g.shadowOffsetY=10;
 cbR(-w/2,-h,w,h,shape%2===0?'#CEC8BA':'#AEB6AA');g.shadowBlur=0;g.shadowOffsetY=0;
 cbPoly([-w/2,-h,-w/2+33,-h-88,w/2+13,-h-90,w/2,-h],shape%2===0?'#495466':'#5C605D','#0F2638',2);
 cbPoly([w/2,-h,w/2+13,-h-90,w/2+49,-h-58,w/2+49,0,w/2,0],'#76807C','#283B47',2);
 cbR(-w/2+18,-h-108,24,50,'#817B72');cbR(-w/2+14,-h-110,33,10,'#CEC6B9');
 cbWindow(-w/2+21,-h+34,38,53,shape%3===0);cbWindow(w/2-60,-h+34,38,53,shape%3===1);
 cbR(-18,-91,42,91,'#364C57');cbR(-15,-87,34,86,'#34536B');cbDot(14,-38,3,PA.gold);
 cbStroke([-w/2,0,w/2+49,0],'#D1C6B4',5);cbR(-w/2-14,-7,w+71,9,'#838C85');
 cbR(-w/2+15,-15,42,12,'#7D927C');cbR(w/2-55,-15,42,12,'#7D927C');
 g.restore()
}
function cbTree(x,ground,scale=1,leaf='#617A70',bare=false){
 g.save();g.translate(x,ground);g.scale(scale,scale);
 cbPoly([-11,0,12,0,8,-140,-4,-140],'#574A3C');
 for(let i=0;i<5;i++){const xx=(i-2)*36,yy=-185+(i%2)*22,r=49+(i%2)*9;
 if(!bare){cbDot(xx,yy,r,leaf);cbDot(xx+17,yy+11,26,'#849A8C88')}
 else{cbStroke([0,-112,xx,yy,xx-35,yy-40],'#544D42',10)}}
 g.restore()
}
function cbStreet(y=790,fromX=87,toX=994,dense=true){
 cbR(fromX,y-37,toX-fromX,53,'#87928E');
 cbR(fromX,y+14,toX-fromX,40,'#374B56');
 cbStroke([fromX,y+24,toX,y+24],'#CDD4C67A',3,[21,18]);
 cbR(fromX,y+53,toX-fromX,14,'#B4B4A4');
 for(let i=0;i<7;i++)cbR(fromX+29+i*132,y+57,32,9,'#EAE4D155');
 if(dense){
   for(let i=0;i<5;i++){let cx=169+i*175;cbHouse(cx,y-35,.68+.07*(i%2),i%3);if(i%2===0)cbTree(cx+92,y-35,.55,'#6D8277')}
 }
}
function cbLayers(surf=840,end=1412,pulse=0.0){
 cbR(86,surf,908,end-surf,'#A48B73');
 cbPoly([86,surf,994,surf,994,surf+111,86,surf+140],'#8A796A');
 cbPoly([86,surf+135,320,surf+131,500,surf+166,750,surf+134,994,surf+125,994,surf+252,86,surf+275],'#6B584C');
 cbPoly([86,surf+265,260,surf+282,500,surf+253,715,surf+266,994,surf+255,994,surf+378,86,surf+369],PA.coal);
 cbPoly([86,surf+365,250,surf+356,600,surf+377,850,surf+357,994,surf+377,994,end,86,end],'#605046');
 cbPoly([86,surf+485,260,surf+469,500,surf+491,850,surf+472,994,surf+490,994,end,86,end],'#292D31');
 for(let i=0;i<80;i++){let x=94+rand(i+38)*887,yy=surf+rand(i+118)*(end-surf);
 cbR(x,yy,3+rand(i+201)*12,1.7,i%2?'#C9B19C33':'#080D1033')}
}
function cbMineTunnel(cx,y,w=320,rise=145){
 g.save();
 cbR(cx-w/2,y-rise,w,rise,'#121C25');
 g.beginPath();g.ellipse(cx,y-rise,w/2,rise*.8,Math.PI,0,Math.PI,true);g.closePath();g.fillStyle='#0F1A23';g.fill();
 for(let i=0;i<5;i++){const xx=cx-w/2+30+i*(w-65)/4;cbR(xx,y-rise+15,9,rise+4,'#8C6C51');cbR(xx-12,y-rise+23,45,10,'#AD8660')}
 cbR(cx-w/2,y-14,w,14,'#8A725C');cbStroke([cx-w/2,y,cx+w/2,y],'#4B5360',4);
 for(let i=0;i<9;i++)cbR(cx-w/2+19+i*w/10,y-9,25,10,'#B2916F');
 g.restore()
}
function cbGlow(x,y,r,factor=1){
 const radial=g.createRadialGradient(x,y,5,x,y,r);radial.addColorStop(0,'#FFDD8299');radial.addColorStop(.24,'#FF8C4C90');radial.addColorStop(.65,'#B3423A55');radial.addColorStop(1,'#E34A2000');
 g.save();g.globalAlpha*=factor;cbDot(x,y,r,radial);g.restore()
}
function cbEmberFront(t,xx=430,y=1160,len=340){
 for(let i=0;i<11;i++){
  const x=xx+i*len/12+Math.sin(i*2+t*.7)*11,r=17+19*rand(i+5);
  cbGlow(x,y+Math.sin(i*.75+t*.3)*28,r*3,.6+.3*Math.sin(t*2+i));
  cbDot(x,y+Math.sin(i*.6+t*.8)*14,2+rand(i+16)*5,i%2?PA.ember:PA.flame);
 }
 for(let i=0;i<24;i++){
   let k=(t*.15+rand(i*7+9))%1,baseX=xx+rand(i+91)*len;
   cbDot(baseX, y-12-k*180,1+rand(i+17)*4,'#F4C089'+Math.floor((1-k)*160).toString(16).padStart(2,'0'));
 }
}
function cbVent(x,surf,t,alpha=1){
 g.save();g.globalAlpha*=alpha;
 for(let i=0;i<3;i++){const dx=i*23-21;
  g.beginPath();g.moveTo(x+dx,surf+20);g.bezierCurveTo(x-36+dx+25*Math.sin(t+i),surf-37,x+30+dx-30*Math.sin(t*.6),surf-125,x+dx+34*Math.sin(t+i),surf-205);
  g.lineWidth=8-i*2;g.strokeStyle=['#DBDDD47B','#F5F0E766','#E6E4E54B'][i];g.stroke()
 }
 g.restore()
}
function cbMark(label,x,y,width=310,color=PA.coral){
 cbR(x,y-35,width,63,color);cbLabel(label,x+19,y+6,23,PA.paper,800,1.0)
}
function cbCaption(sec){
 if(CT.length<30)return;const cue=CT.find(x=>sec>=x.start&&sec<x.end);if(!cue)return;
 const alpha=cbClamp(Math.min((sec-cue.start)*9,(cue.end-sec)*11),0,1);
 g.save();g.globalAlpha=alpha;
 cbR(80,1451,920,180,'#071520EF',9);cbRule(114,1469,137,PA.gold,5);
 let parts=[''];g.font='800 43px "Manrope",Arial';
 for(const word of cue.text.split(' ')){let j=parts.length-1,tr=parts[j]?parts[j]+' '+word:word;
  if(g.measureText(tr).width>805&&parts[j])parts.push(word);else parts[j]=tr}
 if(parts.length>2)QA_C.issues.push({type:'caption-too-many-lines',text:cue.text});
 let n=Math.min(2,parts.length);
 for(let j=0;j<n;j++){let txt=parts[j],size=43;g.font='800 '+size+'px "Manrope",Arial';while(g.measureText(txt).width>815&&size>27){size--;g.font='800 '+size+'px "Manrope",Arial'}
  g.fillStyle=PA.paper;g.textAlign='center';g.fillText(txt,540,n===1?1566:1529+j*66)}
 g.restore();
}
function cbMapStates(rect,alpha=1){
 g.save();g.globalAlpha*=alpha;g.beginPath();g.rect(rect.x,rect.y,rect.w,rect.h);g.clip();
 cbR(rect.x,rect.y,rect.w,rect.h,'#D6D7CA');
 const pr=(lon,lat)=>[rect.x+(lon+83.0)/14.0*rect.w,rect.y+(44.5-lat)/8.8*rect.h];
 for(let lon=-83;lon<=-69;lon+=2){let xx=pr(lon,39)[0];cbStroke([xx,rect.y,xx,rect.y+rect.h],'#22384C18',2)}
 for(let lat=38;lat<=44;lat+=1){let yy=pr(-77,lat)[1];cbStroke([rect.x,yy,rect.x+rect.w,yy],'#22384C18',2)}
 for(const shape of CG){const ggeo=shape.geometry,polys=ggeo.type==='MultiPolygon'?ggeo.coordinates:[ggeo.coordinates];for(const polygon of polys){for(const points of polygon){
  if(points.length<3)continue;g.beginPath();let one=true;for(const coord of points){const [xx,yy]=pr(coord[0],coord[1]);if(one){g.moveTo(xx,yy);one=false}else g.lineTo(xx,yy)}g.closePath();g.fillStyle=shape.name==='Pennsylvania'?'#B68B72':'#98A99F';g.fill();g.strokeStyle='#F5F0E7C8';g.lineWidth=2.8;g.stroke()}}}
 const [cx,cy]=pr(-76.34,40.805);
 cbDot(cx,cy,12,PA.coral);cbDot(cx,cy,21,'#D578642A');g.strokeStyle=PA.coral;g.lineWidth=4;g.beginPath();g.arc(cx,cy,34,0,Math.PI*2);g.stroke();
 g.restore();return [cx,cy]
}
function cbFissure(x,y,depth,k=1){
 const grow=cbOut(k);cbStroke([x,y,x+23*grow,y+62*grow,x+5*grow,y+112*grow,x+55*grow,y+181*grow,x+43*grow,y+239*grow],PA.deep,12*grow);
 cbStroke([x+6,y+91*grow,x-53*grow,y+136*grow,x-62*grow,y+158*grow],PA.deep,7*grow);
 cbGlow(x+23*grow,y+100*grow,65*grow,.8)
}
function cbScene0(t){
 cbBg('#0E2233',4);cbMast(0,'The fire beneath the town');
 const head=cbOut((t+.25)/.86);g.save();g.globalAlpha=head;
 cbTitle('The town that',98,360,96,PA.paper);
 cbTitle('would not cool.',98,475,96,PA.gold);g.restore();
 cbR(84,550,912,833,'#D8CCB7');g.save();g.beginPath();g.rect(84,550,912,833);g.clip();
 const drift=Math.sin(t*.25)*12;
 g.save();g.translate(drift,0);
 cbR(83,550,920,200,'#455D6A');
 for(let i=0;i<5;i++)cbDot(170+i*180,590-i%2*28,62,'#B1AEA31E');
 cbStreet(848,85,996,true);cbLayers(903,1384);
 cbMineTunnel(485,1322,415,125);
 const b=cbP(t,2.3,5.3);cbEmberFront(t,250+200*b,1130,350*b+65);
 cbVent(613,853,t,cbP(t,4,5.3));cbFissure(610,855,290,b);
 g.restore();g.restore();
 cbRule(97,1391,905,PA.coral,6);
 cbLabel('CENTRALIA  /  PENNSYLVANIA',103,1417,21,PA.gold,800,1.7);
}
function cbScene1(t){
 cbBg('#173247',5);cbMast(1,'Pennsylvania · May 1962');
 cbTitle('It started',97,334,103,PA.paper);
 cbTitle('out of sight.',97,448,99,PA.gold);
 const m={x:87,y:571,w:906,h:796};
 let q=cbP(t,.25,1.65);g.save();g.globalAlpha=q;g.translate(0,70*(1-q));
 cbPanel(82,557,918,822,PA.paper,.01);let pin=cbMapStates(m);
 cbStroke([pin[0]+15,pin[1]-8,pin[0]+98,pin[1]-66],PA.night,4);const mx=Math.min(740,pin[0]+75),my=pin[1]-140;
 cbR(mx,my,227,65,PA.night);cbLabel('CENTRALIA',mx+15,my+43,24,PA.paper,800);
 cbLabel('PENNSYLVANIA',112,672,28,PA.night,800,2.1);
 g.restore();
 let p=cbP(t,2.2,4.0);g.save();g.globalAlpha=p;
 cbPanel(114,1031,680,307,PA.cream,-.045);
 cbLabel('MAY   /   1962',153,1111,35,PA.coral,800,2);
 cbStroke([150,1139,724,1139],PA.night,3);
 cbTitle('A fire began.',152,1229,66,PA.night,584);
 cbLabel('PROBABLE ORIGIN: TRASH PIT',153,1287,22,PA.night,800);
 g.restore();
 const info=cbP(t,4.65,5.8);g.save();g.globalAlpha=info;cbMark('INTO ABANDONED MINES',172,1375,600,PA.coral);g.restore();
}
function cbScene2(t){
 cbBg(PA.deep,10);cbMast(2,'How a fire survives underground');
 cbTitle('Coal. Air.',96,326,103,PA.paper);
 cbTitle('A hidden maze.',96,443,95,PA.gold);
 const k=cbP(t,.15,1.1);g.save();g.globalAlpha=k;
 cbR(83,568,914,795,'#C6B196');cbLayers(604,1362);
 cbMineTunnel(403,1050,420,187);cbMineTunnel(750,1217,315,125);
 cbStroke([216,1096,750,1198],'#2D2D32',84);
 cbStroke([225,1096,760,1198],PA.coral+'77',9);
 cbEmberFront(t,360+cbP(t,1.5,6.2)*185,980,235+cbP(t,2,6)*140);
 for(let j=0;j<4;j++){const xx=505+j*68;let bounce=Math.sin(t*1.5+j)*15;cbStroke([xx,900+bounce,xx+10,845+bounce],PA.gold,4);cbPoly([xx+10,842+bounce,xx+1,854+bounce,xx+20,856+bounce],PA.gold)}
 cbVent(718,613,t,cbP(t,2,3));g.restore();
 const c=cbP(t,3.4,5.0);g.save();g.globalAlpha=c;
 cbMark('COAL SEAM',112,805,298,PA.night);cbMark('AIR ROUTES',710,976,270,PA.coral);
 cbLabel('SCHEMATIC / NOT TO SCALE',114,1404,20,PA.paper,700,1.9);g.restore();
}
function cbDrill(x,y,depth=440,t=0){
 cbR(x-8,y-50,17,60,'#5C6470');cbR(x-43,y-64,87,14,PA.night);cbPoly([x-21,y-64,x,y-119,x+21,y-64],'#6D7E83');
 for(let i=0;i<5;i++)cbStroke([x-40+i*20,y-58,x-40+i*20,y-19],'#B6B8A5',2);
 cbR(x-4,y,8,depth*cbP(t,.3,2),PA.gold);
 cbPoly([x-9,y+depth*cbP(t,.3,2),x+9,y+depth*cbP(t,.3,2),x,y+depth*cbP(t,.3,2)+23],PA.coral)
}
function cbScene3(t){
 cbBg('#EAE4D6',6);cbMast(3,'Trying to stop the fire',true);
 cbTitle('How do you stop',94,335,85,PA.night);
 cbTitle('a buried fire?',94,433,85,PA.coral);
 cbPanel(86,518,908,830,'#C5AD91');
 cbLayers(575,1339);
 cbMineTunnel(509,1130,620,170);cbEmberFront(t,327+cbP(t,2,7)*160,1070,375);
 const k=cbP(t,.5,2);g.save();g.globalAlpha=k;cbDrill(316,562,466,t);cbDrill(756,560,526,t-.4);g.restore();
 const p=cbP(t,2.3,4.4);
 for(let i=0;i<24;i++){const x=319+rand(i*4+4)*45,yy=890+rand(i+72)*250;cbDot(x,yy+cbP(t,2.4,4.8)*38,2+3*rand(i+17),'#84BDDA'+Math.floor((1-p*.65)*230).toString(16).padStart(2,'0'))}
 cbMark('DRILL',155,642,187,PA.night);cbMark('BACKFILL',654,642,273,PA.night);
 const show=cbP(t,4.9,6);g.save();g.globalAlpha=show;cbR(105,1258,856,88,PA.night);cbLabel('YEARS OF CONTROL EFFORTS',136,1316,28,PA.paper,800,1.2);g.restore();
}
function cbRoad(y,crack=0){
 cbR(94,y,897,295,'#54646A');
 cbPoly([94,y,994,y,974,y+66,120,y+66],'#9BA5A1');
 cbR(100,y+88,888,13,'#DCD9C7');
 for(let i=0;i<5;i++)cbR(127+i*176,y+164,90,9,'#DED9BF');
 cbStroke([103,y+255,978,y+255],'#E2DCD266',4);
 if(crack>0)cbFissure(560,y+30,190,crack);
}
function cbScene4(t){
 cbBg('#11273B',3);cbMast(4,'1983 · A dangerous turning point');
 cbTitle('The ground',96,336,99,PA.paper);
 cbTitle('gave way.',96,454,104,PA.gold);
 const k=cbP(t,.20,1.6);g.save();g.globalAlpha=k;cbPanel(84,541,916,745,'#D2C8B9');cbRoad(578,cbP(t,2,4));g.restore();
 const d=cbP(t,3.0,4.35);g.save();g.globalAlpha=d;cbR(95,1120,898,233,PA.night);
 cbLabel('GOVERNMENT STUDY  /  1983',125,1185,26,PA.paper,800,1.8);
 cbNumber('$663M',128,1299,120,PA.gold);
 cbLabel('ESTIMATED COST TO EXTINGUISH',128,1335,22,PA.paper,800);g.restore();
 const danger=cbP(t,4.4,5.7);g.save();g.globalAlpha=danger;cbMark('ROAD SUBSIDENCE',107,1409,486,PA.coral);g.restore();
}
function cbScene5(t){
 cbBg('#223849',9);cbMast(5,'The decision to relocate');
 cbTitle('Then the homes',97,336,91,PA.paper);
 cbTitle('disappeared.',97,449,96,PA.gold);
 const p=cbP(t,.4,1.4);
 g.save();g.globalAlpha=p;cbPanel(89,539,900,827,'#CAD2C1');cbR(96,537,891,470,'#8CA497');
 for(let i=0;i<4;i++)cbR(98,556+i*107,884,6,'#B5C4B7A0');
 for(let i=0;i<7;i++){let x=112+i*130;cbR(x,702,104,266,'#AFC2B0');cbStroke([x,702,x,968],'#69847788',3)}
 cbR(98,1000,882,148,'#455B66');cbStroke([120,1068,950,1068],'#EEEDE57A',7,[75,45]);
 for(let i=0;i<5;i++){let gone=cbP(t,1.4+i*.7,2.7+i*.7);g.save();g.globalAlpha=1-gone;cbHouse(190+i*167,1008,.67,i%3);g.restore();
  if(gone>.1){cbR(140+i*167,945,107,28,'#4D665BAA')}}
 g.restore();
 let q=cbP(t,2.5,4.2);g.save();g.globalAlpha=q;
 cbR(118,1191,838,153,PA.night);cbLabel('CONGRESS  /  1984',147,1241,26,PA.paper,800,1.9);
 cbNumber('$42 MILLION',143,1313,64,PA.gold);
 g.restore();
 const z=cbP(t,5.1,6.1);g.save();g.globalAlpha=z;cbMark('RELOCATION FUNDS',163,1403,669,PA.coral);g.restore();
}
function cbScene6(t){
 cbBg('#152A39',15);cbMast(6,'The town today');
 cbTitle('Almost empty.',95,335,102,PA.paper);
 cbTitle('Still burning.',95,452,97,PA.gold);
 const b=cbP(t,.3,1.3);g.save();g.globalAlpha=b;
 cbPanel(86,550,909,819,'#8D9D96');
 cbR(88,550,900,329,'#3A5768');cbPoly([88,800,270,720,430,764,585,690,752,748,995,710,995,903,88,903],'#6A887D');
 cbTree(184,850,.86,'#6C897B');cbHouse(521,884,.75,1);cbTree(820,861,1.03,'#69887A');
 cbR(98,876,889,85,'#475863');cbStroke([98,928,987,928],'#E4D9C18A',4,[37,29]);
 cbLayers(967,1362);cbMineTunnel(560,1326,560,160);cbEmberFront(t,350+Math.sin(t*.25)*20,1176,415);
 cbVent(755,880,t,cbP(t,1.2,2.3));
 g.restore();
 let c=cbP(t,3,4.7);g.save();g.globalAlpha=c;
 cbR(113,1323,861,103,PA.night);
 cbLabel('DANGEROUS GASES  •  GROUND COLLAPSE',139,1390,26,PA.paper,800);g.restore();
}
function cbScene7(t){
 cbBg(PA.deep,17);cbMast(7,'Curio Bureau');
 const beam=g.createLinearGradient(0,680,0,1400);beam.addColorStop(0,'#D5786400');beam.addColorStop(.55,'#D5786433');beam.addColorStop(1,'#D5786400');
 cbR(80,688,923,713,beam);
 const k=cbP(t,.1,1.15);g.save();g.globalAlpha=k;
 cbTitle('The town left.',100,445,96,PA.paper);
 cbTitle("The fire didn't.",100,565,94,PA.gold);
 cbRule(104,623,713,PA.coral,9);g.restore();
 const z=cbP(t,1.2,2.7);g.save();g.globalAlpha=z;
 cbLayers(861,1257);cbMineTunnel(520,1220,602,141);cbEmberFront(t,300,1137,485);
 cbLabel('CENTRALIA  /  MAY 1962 – PRESENT',105,1342,25,PA.paper,800,1.8);
 g.restore();
 let b=cbP(t,3.2,4.45);g.save();g.globalAlpha=b;
 cbTitle('Curio Bureau',103,1413,100,PA.paper);
 cbLabel('STORIES, SYSTEMS, AND SURPRISES.',108,1695,21,PA.gold,800,1.4);
 g.restore();
}
scenes.splice(0,scenes.length,cbScene0,cbScene1,cbScene2,cbScene3,cbScene4,cbScene5,cbScene6,cbScene7);
const renderOld=renderAt;
renderAt=function(t){QA_C.issues.length=0;QA_C.titles.length=0;renderOld(t);cbCaption(t)};
window.renderAt=renderAt;window.setFrame=n=>player.seek(n/FPS);window.renderFrame=n=>renderAt(n/FPS);
window.getDuration=()=>D;window.getFPS=()=>FPS;
window.inspectFrame=t=>{renderAt(t);return{at:t,font:'Playfair Display + Manrope',geodata:QA_C.geodata,captionCount:CT.length,titleCount:QA_C.titles.length,issues:QA_C.issues.slice()}};
if(!QA_C.geodata||CT.length<35)throw Error('Missing verified Pennsylvania geography or word-timed captions');
const FX_NAMES={sweep:'mixkit-fast-small-sweep-transition-166.wav',arrow:'mixkit-arrow-whoosh-1491.wav',click:'mixkit-interface-device-click-2577.wav',type:'mixkit-mechanical-typewriter-single-hit-1382.wav',fast:'Fast-woosh.wav',riser:'ES_Riser Metallic - SFX Producer.mp3',popup:'Pop-up-woosh.mp3',cinematic:'mixkit-cinematic-whoosh-fast-transition-1492.wav',chime:'mixkit-retro-confirmation-tone-2860.wav',tick:'Mouse click.mp3',rumble:'freesound_community-earth-rumble-6953.mp3',debris:'lordsonny_two-debris-break-253779.mp3',bass:'06 Medium Bass Drop B.wav',pulse:'mixkit-mystwrious-bass-pulse-2298.wav'};
const FX_CUES=[
[.3,'rumble',.20,'underground wake'],[.48,'cinematic',.37,'headline reveal'],[1.35,'sweep',.28,'street enters'],[2.55,'debris',.27,'cross section cracks'],[3.5,'pulse',.15,'coal glow'],[5.3,'arrow',.23,'smoke enters'],[7.8,'fast',.42,'map transition'],
[8.32,'popup',.37,'Pennsylvania map reveal'],[9.5,'type',.28,'1962 label'],[10.8,'click',.28,'Centralia pin'],[12.2,'sweep',.35,'archival document'],[13.0,'type',.38,'probable cause'],[15.45,'riser',.25,'underworld transition'],
[16.25,'rumble',.15,'coal seams'],[16.5,'cinematic',.30,'geology reveal'],[18.8,'pulse',.23,'underground combustion'],[20.5,'arrow',.30,'air motion'],[22.1,'sweep',.28,'hot front expansion'],[24.75,'fast',.38,'geology to drilling'],
[25.3,'type',.34,'attempted control diagram'],[26.4,'click',.35,'drilling begins'],[27.6,'debris',.22,'backfill impact'],[29.2,'sweep',.23,'water flow'],[31.2,'pulse',.18,'still spreading'],[33.75,'cinematic',.35,'road transition'],
[34.45,'rumble',.21,'road subsidence'],[35.6,'debris',.42,'road crack'],[37.5,'bass',.22,'663m figure'],[39.0,'type',.31,'1983 report'],[41.75,'fast',.42,'relocation transition'],
[42.5,'type',.33,'policy frame'],[43.6,'click',.27,'first house removed'],[44.7,'sweep',.28,'second house removed'],[45.6,'popup',.28,'third house removed'],[46.7,'debris',.20,'last street clears'],[48.2,'chime',.24,'42 million appropriation'],[50.7,'arrow',.40,'present day wipe'],
[51.4,'rumble',.20,'persistent fire'],[52.2,'sweep',.27,'near empty street'],[54.5,'pulse',.16,'gas vents'],[55.7,'debris',.16,'collapse danger'],[57.75,'riser',.27,'closing statement'],
[58.3,'cinematic',.35,'the town left'],[59.5,'bass',.22,'the fire did not'],[60.8,'rumble',.12,'last fire glow'],[61.3,'chime',.36,'Curio Bureau title'],[62.6,'popup',.20,'brand signature']
];
cueEvents.splice(0,cueEvents.length,...FX_CUES.map(r=>r.slice(0,3)));
window.CURIO_CUE_SHEET=FX_CUES.map(([at,key,gain,event])=>({time:at,filename:FX_NAMES[key],gain,event}));
const initOld=player.init.bind(player);
player.init=async function(){
 await initOld();
 if(Object.keys(this.fx).length<14)throw Error('Centralia Drive SFX pack not fully decoded: '+Object.keys(this.fx).length);
 if(!this.voice&&window.CURIO_EMBEDDED_VOICE){
  let r=await fetch('data:audio/mpeg;base64,'+window.CURIO_EMBEDDED_VOICE);
  this.voice=await this.audioCtx.decodeAudioData(await r.arrayBuffer());
  $('voiceStatus').textContent='Embedded Centralia narration loaded · '+this.voice.duration.toFixed(1)+' seconds';
 }
 if(!this.voice)throw Error('Narration not embedded in Centralia film');
};
player.attach=function(ctx,dest,offset,start){
 const comp=ctx.createDynamicsCompressor();comp.threshold.value=-19;comp.knee.value=19;comp.ratio.value=4;comp.attack.value=.006;comp.release.value=.21;
 const bus=ctx.createGain();bus.gain.value=.84;comp.connect(bus);bus.connect(dest);
 const route=(src,gain)=>{const v=ctx.createGain();v.gain.value=gain;src.connect(v);v.connect(comp);return src};
 for(const [when,key,gain]of cueEvents){const buf=player.fx[key];if(!buf){QA_C.issues.push({missingFX:key});continue}
  if(when+buf.duration<=offset)continue;let at=Math.max(when,offset);let source=ctx.createBufferSource();source.buffer=buf;route(source,gain);source.start(start+at-offset,Math.max(0,offset-when));player.sources.push(source)}
 if(player.voice&&offset<player.voice.duration){let s=ctx.createBufferSource();s.buffer=player.voice;route(s,1.04);s.start(start,offset);player.sources.push(s)}
 // Scored low-register cinematic bed with actual harmonic progression and breathing dynamics.
 const harmonies=[[110,138.59,164.81,220],[98,123.47,146.83,196],[116.54,146.83,174.61,233.08],[103.83,130.81,164.81,207.65]];
 for(let bar=0;bar<32;bar++){let when=bar*2;if(when+2<=offset)continue;
 let at=Math.max(offset,when),dur=Math.min(2,when+2-at),abs=start+at-offset,notes=harmonies[Math.floor(bar/4)%4];
 for(let n=0;n<4;n++){let o=ctx.createOscillator(),filter=ctx.createBiquadFilter(),env=ctx.createGain();
  o.type=n===0?'triangle':'sine';o.frequency.value=notes[n]*(n===0?.5:1);filter.type='lowpass';filter.frequency.value=n<2?730:1560;
  const level=n===0?.080:.030;
  env.gain.setValueAtTime(.0001,abs);env.gain.linearRampToValueAtTime(level,abs+.22);env.gain.setValueAtTime(level,abs+Math.max(.26,dur-.28));env.gain.exponentialRampToValueAtTime(.0001,abs+dur);
  o.connect(filter);filter.connect(env);env.connect(comp);o.start(abs);o.stop(abs+dur+.02);player.sources.push(o)}
 }
 for(let beat=0;beat<128;beat++){const at=beat*.5;if(at<offset||at>=64)continue;
  const time=start+at-offset,root=harmonies[Math.floor(beat/16)%4][0],osc=ctx.createOscillator(),vol=ctx.createGain();
  osc.type='sine';osc.frequency.value=[root,root*1.5,root*2,root*1.5][beat%4];
  const gain=beat%4===0?.045:.016;vol.gain.setValueAtTime(.0001,time);vol.gain.linearRampToValueAtTime(gain,time+.01);vol.gain.exponentialRampToValueAtTime(.0001,time+.22);
  osc.connect(vol);vol.connect(comp);osc.start(time);osc.stop(time+.23);player.sources.push(osc)
 }
};
renderAt(.01);
