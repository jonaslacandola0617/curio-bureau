'use strict';
/** CURIO BUREAU 003 – THE WATERFALL THEY SWITCHED OFF
 * Original editorial motion documentary; eight custom 2.5D scenes.
 * Authoritative subject: American Falls, not the Horseshoe Falls.
 * All motion derives from absolute 64-second master time.
 */
const NF={navy:'#0D1C2B',ink:'#132637',deep:'#071521',cream:'#F5F0E7',paper:'#EDE5D6',gold:'#C8A26B',coral:'#D57864',sea:'#1E536A',blue:'#30768E',foam:'#DEF7F0',aqua:'#80B9BD',sage:'#A8B7A9',dark:'#294051',shale:'#53616A',dolomite:'#B5AC99'};
const GEO=window.CURIO_GEO||[],CAP=window.CURIO_CAPTIONS||[];
const NF_S={l:84,r:996,top:122,titleEnd:1390,capTop:1450,capBottom:1635};
const nfQA={issues:[],titles:[],geodata:GEO.length>=7&&GEO.some(z=>z.name==='New York'),captionCount:CAP.length,photoLoaded:false};
window.CURIO_QA={get issues(){return nfQA.issues},get mapLoaded(){return nfQA.geodata},get captionCount(){return nfQA.captionCount},get photoLoaded(){return nfQA.photoLoaded}};
const photo=new Image();
window.NIAGARA_READY=new Promise((res,rej)=>{
 photo.onload=()=>{nfQA.photoLoaded=photo.naturalWidth>600;res(nfQA.photoLoaded)};
 photo.onerror=()=>rej(new Error('Required CC BY Niagara photo failed to load'));
});
photo.src='data:image/jpeg;base64,'+(window.NIAGARA_PHOTO||'');
const smooth=(t)=>{t=Math.max(0,Math.min(1,t));return t*t*(3-2*t)};
const out3=(t)=>1-Math.pow(1-Math.max(0,Math.min(1,t)),3);
const nfp=(t,a,b)=>smooth((t-a)/(b-a));
const nfr=(x,y,w,h,c,rr=0)=>{g.beginPath();g.roundRect(x,y,w,h,rr);g.fillStyle=c;g.fill()};
const nfdot=(x,y,r,c)=>{g.beginPath();g.arc(x,y,r,0,Math.PI*2);g.fillStyle=c;g.fill()};
const nfs=(pts,c=NF.cream,w=3,dash=[])=>{g.beginPath();g.moveTo(pts[0],pts[1]);for(let i=2;i<pts.length;i+=2)g.lineTo(pts[i],pts[i+1]);g.strokeStyle=c;g.lineWidth=w;g.setLineDash(dash);g.stroke();g.setLineDash([])};
const nfpPoly=(pts,c,edge='',lw=2)=>{g.beginPath();g.moveTo(pts[0],pts[1]);for(let i=2;i<pts.length;i+=2)g.lineTo(pts[i],pts[i+1]);g.closePath();g.fillStyle=c;g.fill();if(edge){g.strokeStyle=edge;g.lineWidth=lw;g.stroke()}};
function nfText(t,x,y,size=27,c=NF.cream,weight=700,spacing=0){
 g.fillStyle=c;g.font=weight+' '+size+'px "Manrope",Arial,sans-serif';g.textBaseline='alphabetic';g.textAlign='left';
 if(spacing){let px=x;for(const ch of t){g.fillText(ch,px,y);px+=g.measureText(ch).width+spacing}return}
 const m=g.getTransform();if(Math.abs(m.a-1)<.001&&Math.abs(m.d-1)<.001&&Math.abs(m.b)<.001&&Math.abs(m.c)<.001&&x>=84&&x<990&&y<1450){while(g.measureText(t).width+x>996&&size>15){size--;g.font=weight+' '+size+'px "Manrope",Arial,sans-serif'}}
 g.fillText(t,x,y);
}
function nfTitle(t,x,y,size=102,c=NF.cream,maxW=890){
 let z=size,w=Math.min(maxW,NF_S.r-x);
 do{g.font='600 '+z+'px "Playfair Display",Georgia,serif';if(g.measureText(t).width<=w)break;z--}while(z>27);
 let aw=g.measureText(t).width,mt=g.getTransform();const identity=Math.abs(mt.a-1)<.001&&Math.abs(mt.b)<.001&&Math.abs(mt.c)<.001&&Math.abs(mt.d-1)<.001&&Math.abs(mt.e)<.001&&Math.abs(mt.f)<.001;
 if(identity&&(x<NF_S.l||x+aw>NF_S.r+1||y<NF_S.top||y>NF_S.titleEnd))nfQA.issues.push({title:t,x,y,width:Math.ceil(aw),size:z});
 nfQA.titles.push({title:t,x,y,size:z});
 g.fillStyle=c;g.textBaseline='alphabetic';g.textAlign='left';g.fillText(t,x,y);
}
function nfClip(x,y,w,h,draw){g.save();g.beginPath();g.rect(x,y,w,h);g.clip();draw();g.restore()}
function nfPaper(x,y,w,h,light=true){g.save();g.shadowColor='#0009';g.shadowBlur=28;g.shadowOffsetY=20;nfr(x,y,w,h,light?NF.paper:NF.dark,3);g.restore()}
function nfGrain(seed=0){for(let j=0;j<180;j++){let xx=rand(j+seed)*W,yy=rand(j*3+seed)*H;nfr(xx,yy,1.6,1.6,j%2?'#F5F0E709':'#131E3007')}}
function nfBase(bg=NF.deep,tag='FIELD NOTE / 003',scene=0,light=false){
 nfr(0,0,W,H,bg);const grid=light?'#1936490A':'#E5F5F20B';
 for(let x=0;x<W;x+=85)nfs([x,0,x,H],grid,1);
 for(let y=0;y<H;y+=85)nfs([0,y,W,y],grid,1);
 nfGrain(scene*217);
 nfr(86,128,54,7,NF.gold);nfText('CURIO BUREAU',165,143,20,light?NF.ink:NF.cream,800,5);
 nfText('FIELD NOTES    /    003',88,193,16,light?'#456479':'#9AB2BB',800,2);
 nfs([86,1750,995,1750],light?'#1D3A4A55':'#E9E4D655',2);
 nfText(tag.toUpperCase(),87,1803,19,light?NF.ink:NF.cream,800,1.1);
 nfText(String(scene+1).padStart(2,'0')+'  /  08',885,1803,19,NF.gold,800);
}
function nfBadge(t,x,y,w=290,fill=NF.coral,c=NF.cream){nfr(x,y,w,62,fill,2);nfText(t,x+18,y+42,24,c,800,1)}
function nfArrow(x1,y1,x2,y2,col=NF.gold,w=8){
 nfs([x1,y1,x2,y2],col,w);let a=Math.atan2(y2-y1,x2-x1);nfpPoly([x2,y2,x2-23*Math.cos(a-.50),y2-23*Math.sin(a-.50),x2-23*Math.cos(a+.50),y2-23*Math.sin(a+.50)],col);
}
function nfPhotoFrame(x,y,w,h,t,scale=1){
 nfPaper(x-12,y-12,w+24,h+24);
 nfClip(x,y,w,h,()=>{
  const ratio=photo.naturalWidth/photo.naturalHeight||1.5;
  const actualH=h*1.05*scale,actualW=Math.max(w*1.08,actualH*ratio),shift=Math.sin(t*.27)*10;
  g.drawImage(photo,x+(w-actualW)/2+shift,y+(h-actualH)/2,actualW,actualH);
  nfr(x,y,w,h,'#0D1C2B26');nfr(x,y,w,h,'#C8A26B13');
  for(let i=0;i<5;i++)nfs([x,y+i*h/5,x+w,y+i*h/5],'#EEE7D50B',2);
 });
}
function nfCliff(x,y,w,h,detail=1){
 nfClip(x,y,w,h,()=>{
  const grd=g.createLinearGradient(x,y,x+w,y+h);grd.addColorStop(0,'#BDB2A0');grd.addColorStop(.42,'#67727A');grd.addColorStop(1,'#263E4B');nfr(x,y,w,h,grd);
  for(let i=0;i<14;i++){let yy=y+i*h/14,offset=12*Math.sin(i*13);
    nfs([x,yy+offset,x+w*.25,yy+offset+16,x+w*.56,yy+offset-8,x+w,yy+offset+18],'#F1E5CB21',2+(i%3));
  }
  for(let i=0;i<31;i++){let xx=x+rand(i*7+5)*w,yy=y+rand(i*13+11)*h;
    nfs([xx,yy,xx+12*Math.sin(i),yy+40+rand(i+5)*110,xx-19+rand(i+3)*20,yy+170],'#102C38AA',1.3+rand(i+7)*4);
  }
  for(let i=0;i<22;i++){let xx=x+i*w/23,yy=y+h*.75+rand(i+21)*h*.15;
    nfpPoly([xx,yy,xx+23,yy-17,xx+60,yy-7,xx+76,yy+26,xx+27,yy+36],i%3===0?'#8C9C98':'#536773','#172F43',1.1)}
  nfr(x,y,w,h,'#EDE1C20D');
 });
}
function nfCascade(x,y,w,h,t,water=1){
 if(water<=.001)return;
 g.save();g.globalAlpha=water;nfClip(x,y,w,h,()=>{
  const sea=g.createLinearGradient(x,y,x+w,y+h);sea.addColorStop(0,'#9EE5DA');sea.addColorStop(.28,'#2C7890');sea.addColorStop(1,'#133F60');
  for(let i=0;i<76;i++){
   const xx=x+i*w/76 + Math.sin(t*.8+i*1.7)*5;
   const drift=Math.sin(i*.31+t*.43)*20;
   g.beginPath();g.moveTo(xx,y-15);
   g.bezierCurveTo(xx+13,y+h*.35,xx+drift-19,y+h*.65,xx+drift+8,y+h+15);
   g.strokeStyle=i%4===0?'#E7FFF4':i%3===0?'#7DC1CD':'#4A9FB0';
   g.globalAlpha=water*(i%4===0?.72:.42);g.lineWidth=(i%5+1)*2.5+1.7;g.stroke();
  }
  for(let i=0;i<130;i++){let xx=x+rand(i+19)*w,yy=y+h*(.72+rand(i*4)*.27)+Math.sin(t*2+i)*11;
   nfdot(xx,yy,1.8+(i%5),i%3===0?'#FFFFFF':'#A7E0DE');
  }
 });g.restore();
}
function nfMist(x,y,w,h,t,alpha=.8){
 g.save();g.globalAlpha=alpha;
 for(let i=0;i<37;i++){let xx=x+rand(i*3+11)*w,yy=y+rand(i*5+22)*h;
  nfdot(xx+Math.sin(t*.23+i)*19,yy+Math.cos(t*.11+i)*12,4+rand(i)*17,i%3===0?'#F5F0E7':'#9CB8C4');
 }g.restore();
}
function nfRiverPanel(x,y,w,h,t,progress=0){
 // Geographic orientation: river flows north/up; USA mainland east/right; Goat Island center; Canadian Horseshoe west.
 nfClip(x,y,w,h,()=>{
  nfr(x,y,w,h,'#E0DDCD');
  for(let i=0;i<16;i++){let yy=y+i*h/16;nfs([x,yy,x+w,yy],'#31475A14',2)}
  nfpPoly([x+10,y+h*.73,x+90,y+h*.20,x+240,y+30,x+320,y+h*.15,x+225,y+h*.79,x+160,y+h-20], '#4F8795');
  nfpPoly([x+w*.50,y+h*.92,x+w*.66,y+h*.65,x+w*.72,y+h*.19,x+w*.87,y+40,x+w-5,y+h*.13,x+w-20,y+h*.93],progress>.72?'#407B94':'#71959E');
  nfpPoly([x+w*.33,y+h*.19,x+w*.59,y+h*.13,x+w*.64,y+h*.5,x+w*.51,y+h*.68,x+w*.35,y+h*.57,x+w*.27,y+h*.39], '#9FAD9A','#385B5C',4);
  // Barrier between Goat Island (middle) and mainland (right), across eastern channel near upstream section.
  const a=smooth((progress-.10)/.66);
  if(a>0){for(let i=0;i<13;i++){let k=Math.min(1,Math.max(0,a*13-i));g.save();g.globalAlpha=k;let xx=x+w*(.57+i*.021),yy=y+h*(.61+i*.002);
    nfpPoly([xx,yy,xx+24,yy-22,xx+57,yy-15,xx+61,yy+11,xx+22,yy+24],i%3===0?'#9E9789':'#756F66','#3C4950',2);g.restore()}}
  // Current redirected to the unblocked western channel.
  const flow=smooth((progress-.2)/.8);
  for(let i=0;i<6;i++){
   let yy=y+h*(.84-i*.063);
   nfArrow(x+w*.50,yy,x+w*(.28-flow*.10),yy-h*(.13+flow*.06),i%2?NF.foam:'#B6E1D9',4);
  }
  for(let i=0;i<4;i++){let xx=x+w*(.76+i*.03);nfArrow(xx,y+h*.72,xx-8,y+h*.28,'#D57864',3)}
  if(a>.3){nfs([x+w*.58,y+h*.66,x+w*.90,y+h*.64],NF.coral,10)}
  nfText('GOAT ISLAND',x+w*.33,y+h*.42,23,NF.ink,800);
  nfText('HORSESHOE',x+15,y+h*.88,21,NF.cream,800);
  nfText('AMERICAN',x+w*.65,y+h*.88,21,NF.ink,800);
 });
}
function nfDocument(x,y,w,h){
 nfPaper(x,y,w,h);
 for(let i=0;i<34;i++)nfs([x+25,y+i*h/34,x+w-25,y+i*h/34],'#172B3808',1);
}
function nfPhotoLabel(x,y,s){nfr(x,y-28,Math.min(870,36+s.length*13),48,NF.deep);nfText(s,x+18,y+5,19,NF.cream,800,1)}
function nfHeadlineDate(y=630){nfBadge('1969 / NIAGARA, NEW YORK',110,y,516,NF.gold,NF.deep)}
function nfCover(name,sub){nfTitle(name,99,366,103,NF.cream,890);nfText(sub,101,417,24,NF.gold,800,2)}
function nfNYInset(x,y,w,h){
 const entry=GEO.find(f=>f.name==='New York');
 nfClip(x,y,w,h,()=>{
  nfr(x,y,w,h,NF.deep);
  for(let i=0;i<9;i++)nfs([x+i*w/9,y,x+i*w/9,y+h],'#E1F5EA17',1);
  for(let i=0;i<5;i++)nfs([x,y+i*h/5,x+w,y+i*h/5],'#E1F5EA19',1);
  if(entry&&entry.geometry){
   let multi=entry.geometry.type==='MultiPolygon'?entry.geometry.coordinates:[entry.geometry.coordinates];
   for(const poly of multi)for(const ring of poly){
    g.beginPath();let begun=false;
    for(const [lon,lat] of ring){let xx=x+(lon+80.7)/9.7*w,yy=y+(45.7-lat)/6.0*h;
     if(!begun){g.moveTo(xx,yy);begun=true}else g.lineTo(xx,yy)}
    g.closePath();g.fillStyle=NF.sage;g.fill();g.strokeStyle='#F5F0E755';g.lineWidth=1.5;g.stroke();
   }
  }
  const pinX=x+(-79.075+80.7)/9.7*w,pinY=y+(45.7-43.083)/6.0*h;
  nfdot(pinX,pinY,7,NF.coral);g.strokeStyle=NF.coral;g.lineWidth=2;g.beginPath();g.arc(pinX,pinY,16,0,Math.PI*2);g.stroke();
  nfText('NIAGARA',x+15,y+h-16,18,NF.cream,800);
 });
 nfs([x,y,x+w,y,x+w,y+h,x,y+h,x,y],NF.gold,3);
}
function nfScene0(t){
 nfBase(NF.deep,'The great dewatering',0);
 const push=nfp(t,0,5.5);
 nfPhotoFrame(96,390,891,1050,t,1.06+push*.055);
 // Historic engineering still moves around the photograph: water disappears gradually, revealing original cliff art.
 const drained=nfp(t,2.75,5.6);
 g.save();g.globalAlpha=drained;nfCliff(98,392,887,1044);g.restore();
 nfCascade(122,769,841,618,t,1-drained);
 nfMist(115,1130,850,200,t,(1-drained)*.43);
 g.save();g.globalAlpha=.94;
 nfr(90,247,910,150,NF.deep);nfTitle('They stopped a waterfall.',103,356,92);
 g.restore();
 nfHeadlineDate(1319);
 nfBadge('AMERICAN FALLS',110,1397,368,NF.coral);
 nfText('Horseshoe Falls kept flowing.',111,1677,24,NF.foam,700);nfText('Present-day photo: Bob Linsdell / CC BY 2.0',111,1720,16,NF.gold,700);
}
function nfScene1(t){
 nfBase('#132A3A','One river. Two waterfalls.',1);
 nfTitle('Not all of Niagara.',101,358,94);
 nfText('THE WATER WENT SOMEWHERE ELSE',101,429,24,NF.gold,800,1.2);
 const a=.38+.62*nfp(t,0,.95);
 g.save();g.globalAlpha=a;nfPaper(92,516,894,955);nfRiverPanel(111,535,857,917,t,.03);
 nfText('CANADA',139,592,25,NF.cream,800,2);
 nfText('UNITED STATES',701,751,20,NF.ink,800,1);nfNYInset(705,552,238,174);
 nfBadge('AMERICAN FALLS  → DRY',422,1250,510,NF.coral);
 nfBadge('HORSESHOE  →  FLOWING',121,1360,540,NF.deep);
 g.restore();
 const b=nfp(t,4,6.6);g.save();g.globalAlpha=b;nfText('FLOW DIAGRAM / NOT TO SCALE',121,1530,22,NF.aqua,800);g.restore();
}
function nfScene2(t){
 nfBase('#0D283A','The temporary rock cofferdam',2);
 nfTitle('A dam made of stone.',93,342,98);
 nfText('GOAT ISLAND  /  UPSTREAM CHANNEL',100,415,24,NF.gold,800,1.4);
 const a=nfp(t,.6,5.8);
 nfPaper(90,516,902,914);nfRiverPanel(106,532,873,883,t,a);
 g.save();g.globalAlpha=nfp(t,2,3.4);
 nfr(108,1191,858,142,NF.deep);nfText('ROCKS REDIRECT THE FLOW',131,1256,40,NF.cream,800);
 nfText('Temporary cofferdam  ·  June 1969',134,1308,23,NF.gold,700);
 g.restore();
 const q=nfp(t,4.2,6);g.save();g.globalAlpha=q;nfBadge('HORSESHOE KEPT FLOWING',116,1360,620,NF.gold,NF.deep);g.restore();
}
function nfScene3(t){
 nfBase(NF.paper,'What the water revealed',3,true);
 nfTitle('Under the waterfall.',104,346,100,NF.ink);
 nfText('THE EXPOSED AMERICAN FALLS',105,418,25,NF.coral,800,2);
 // A careful original dry geology illustration; never misrepresent it as a historical photograph.
 nfPaper(92,509,891,939);nfCliff(111,529,854,870);
 const reveal=nfp(t,.8,2.5);
 g.save();g.globalAlpha=reveal;
 nfs([570,600,650,737,760,772],NF.gold,7);
 nfBadge('FRACTURED ROCK FACE',575,745,363,NF.gold,NF.deep);
 nfs([445,1140,390,1234,230,1243],NF.foam,6);
 nfBadge('FALLEN STONE / TALUS',134,1240,477,NF.deep);
 g.restore();
 const pp=nfp(t,4,5.6);g.save();g.globalAlpha=pp;
 nfBadge('ORIGINAL ENGINEERING ILLUSTRATION',113,1374,728,NF.deep);
 g.restore();
 nfText('Engineers could finally inspect the rock.',107,1674,22,NF.ink,700);
}
function nfScene4(t){
 nfBase('#122B3A','Geology: cracks, pressure, erosion',4);
 nfTitle('What holds a cliff?',98,348,93);
 nfText('LOCKPORT DOLOMITE  /  ROCHESTER SHALE',98,424,22,NF.gold,800);
 nfPaper(95,526,891,914);
 nfClip(112,543,858,882,()=>{
  nfr(112,543,858,882,'#C1B9A9');
  for(let i=0;i<6;i++){let yy=590+i*63;nfs([112,yy,340,yy+18,622,yy-14,972,yy+28],'#45566658',5)}
  nfr(112,857,858,530,NF.shale);
  for(let i=0;i<7;i++){let yy=874+i*78;nfs([112,yy,434,yy-9,773,yy+15,967,yy],'#EDE5D645',3)}
  // Fractures: clearly independently drawn, evidence oriented.
  nfs([551,567,585,700,546,803,600,937,566,1124,625,1294],NF.coral,9);
  nfs([394,570,424,775,399,936,478,1122],NF.deep,8);
  // Bore/drilling machine silhouette, rig with components and core bit.
  const rig=nfp(t,1.1,3.4);
  nfr(714,564,139,68,NF.deep);nfr(751,617,33,690*rig,NF.ink);
  nfr(738,560,67,29,NF.gold);nfr(696,561,182,21,NF.deep);
  nfs([740,565,733,768,772,768,782,1305],NF.gold,8);
  for(let i=0;i<12;i++)nfr(775,601+i*58,19,10,NF.paper);
  nfdot(767,1299*rig+565*(1-rig),19,NF.coral);
  nfText('48 CORE BORINGS',144,673,26,NF.ink,800);
  nfText('ROCK FRACTURES',142,1165,26,NF.cream,800);
  nfText('PRESSURE MEASUREMENTS',144,1344,22,NF.cream,800);
 });
 const dial=nfp(t,3.7,5.9);g.save();g.globalAlpha=dial;
 nfdot(294,947,126,NF.paper);g.strokeStyle=NF.gold;g.lineWidth=8;g.strokeRect(167,821,254,254);
 for(let i=0;i<11;i++){let theta=Math.PI*(.15+i*.075),xx=294+Math.cos(theta)*89,yy=951+Math.sin(theta)*89;nfdot(xx,yy,5,NF.ink)}
 nfArrow(294,947,333,899,NF.coral,11);nfText('H₂O',257,1034,34,NF.ink,800);
 g.restore();
}
function nfScene5(t){
 nfBase('#0D2435','Restoration: November 25, 1969',5);
 nfTitle('The water returns.',95,345,100,NF.cream);
 nfText('25 NOVEMBER 1969  /  GRADUAL RESTORATION',101,423,23,NF.gold,800);
 const a=nfp(t,.6,5.5);
 nfPaper(92,516,898,895);
 nfCliff(107,532,868,864);
 nfCascade(120,744,841,640,t,.03+.97*a);
 nfMist(112,1144,859,162,t,a*.67);
 nfBadge('AMERICAN FALLS  /  FLOW RESTORED',126,1299,770,NF.deep);
 g.save();g.globalAlpha=nfp(t,4.1,5.4);
 nfBadge('HORSESHOE ALWAYS FLOWING',111,1380,654,NF.gold,NF.deep);
 g.restore();
}
function nfScene6(t){
 nfBase('#172F3D','The 1975 policy verdict',6);
 nfTitle('What should we save?',97,344,88);
 nfText('1975  /  INTERNATIONAL JOINT COMMISSION',103,410,22,NF.gold,800,1);
 let p=.44+.56*nfp(t,0,1.0);
 g.save();g.globalAlpha=p;
 nfDocument(117,506,838,960);
 nfText('INTERNATIONAL JOINT COMMISSION',157,593,22,NF.ink,800,2);
 nfs([158,616,907,616],NF.ink,3);
 nfTitle('Preservation and',155,723,62,NF.ink,745);
 nfTitle('Enhancement',155,799,62,NF.ink,745);
 nfTitle('of the American Falls',155,875,59,NF.ink,749);
 nfText('1975  /  FINAL REPORT',159,946,25,NF.coral,800,2);
 for(let i=0;i<5;i++)nfr(158,1012+i*41,730-(i%3)*67,9,'#334C5555');
 g.restore();
 const x=nfp(t,2.5,4.8);g.save();g.globalAlpha=x;
 nfr(151,1190,762,158,NF.gold);
 nfText('DO NOT ARTIFICIALLY',175,1253,40,NF.ink,800);
 nfText('BEAUTIFY THE ROCK.',176,1322,39,NF.ink,800);
 g.restore();
 nfText('Report finding: paraphrased; see IJC 1975.',145,1420,20,NF.ink,700);
}
function nfScene7(t){
 nfBase(NF.deep,'Stories, systems, and surprises',7);
 nfPhotoFrame(85,386,914,998,t,1.0);
 nfr(86,353,911,360,NF.deep+'ED');
 nfTitle('Let nature',107,498,113,NF.cream,844);
 nfTitle('change.',107,637,134,NF.gold,844);
 let q=nfp(t,1.2,2.5);
 g.save();g.globalAlpha=q;
 nfPaper(112,1026,845,175);
 nfText('1969  /  ENGINEERING',147,1108,28,NF.ink,800);
 nfText('1975  /  LEAVE IT NATURAL',147,1165,27,NF.coral,800);
 g.restore();
 let b=nfp(t,2.6,3.6);g.save();g.globalAlpha=b;
 nfr(85,1262,914,231,NF.deep);
 nfTitle('Curio Bureau',103,1383,105,NF.cream);
 nfText('STORIES, SYSTEMS, AND SURPRISES.',108,1430,21,NF.gold,800,1.0);
 g.restore();
}
scenes.splice(0,scenes.length,nfScene0,nfScene1,nfScene2,nfScene3,nfScene4,nfScene5,nfScene6,nfScene7);
starts.splice(0,starts.length,0,7,15,23,32,42,51,58,64);
const nfOldRender=renderAt;
function nfCaptions(t){
 const row=CAP.find(q=>t>=q.start&&t<q.end);if(!row)return;
 const a=Math.min(1,(t-row.start)*10,(row.end-t)*12);
 g.save();g.globalAlpha=Math.max(0,a);
 nfr(86,1455,909,177,'#071521E9',9);nfr(122,1466,148,6,NF.gold);
 let parts=[''];g.font='800 43px "Manrope",Arial';
 for(const word of row.text.split(' ')){
  const i=parts.length-1,test=(parts[i]?parts[i]+' ':'')+word;
  if(g.measureText(test).width>779&&parts[i])parts.push(word);else parts[i]=test;
 }
 if(parts.length>2){nfQA.issues.push({subtitleRowOverlong:row.text});parts=parts.slice(0,2)}
 for(let i=0;i<parts.length;i++){
  let sz=43;g.font='800 '+sz+'px "Manrope",Arial';
  while(sz>27&&g.measureText(parts[i]).width>790){sz--;g.font='800 '+sz+'px "Manrope",Arial'}
  g.textAlign='center';g.textBaseline='alphabetic';g.fillStyle=NF.cream;
  g.fillText(parts[i],540,parts.length>1?1536+i*65:1571);
 }
 g.restore();
}
renderAt=function(t){nfQA.issues.length=0;nfQA.titles.length=0;const sec=Math.max(0,Math.min(D-.00001,t));let idx=0;while(idx<7&&sec>=starts[idx+1])idx++;g.save();scenes[idx](sec-starts[idx]);g.restore();nfCaptions(sec);nfr(0,H-5,W*sec/D,5,NF.gold)};
window.renderAt=renderAt;window.setTime=t=>player.seek(t);window.setFrame=f=>player.seek(f/FPS);
window.renderFrame=f=>renderAt(f/FPS);window.getDuration=()=>D;window.getFPS=()=>FPS;
window.inspectFrame=t=>{renderAt(t);return{at:t,photoLoaded:nfQA.photoLoaded,geodata:nfQA.geodata,captionCount:nfQA.captionCount,issues:nfQA.issues.slice(),titles:nfQA.titles.slice()}};
if(!nfQA.geodata||nfQA.captionCount<32)throw Error('Niagara film missing real geodata or word-boundary captions.');
const NF_FILE={sweep:'mixkit-fast-small-sweep-transition-166.wav',arrow:'mixkit-arrow-whoosh-1491.wav',click:'mixkit-interface-device-click-2577.wav',type:'mixkit-mechanical-typewriter-single-hit-1382.wav',fast:'Fast-woosh.wav',riser:'ES_Riser Metallic - SFX Producer.mp3',popup:'Pop-up-woosh.mp3',cinematic:'mixkit-cinematic-whoosh-fast-transition-1492.wav',chime:'mixkit-retro-confirmation-tone-2860.wav',tick:'Mouse click.mp3',debris:'lordsonny_two-debris-break-253779.mp3'};
const NF_CUES=[
 [.20,'sweep',.34,'falling water montage'],[1.30,'cinematic',.28,'hero photo push'],
 [2.85,'debris',.31,'cofferdam graphic takes control'],[3.85,'type',.28,'1969 label'],
 [4.92,'fast',.44,'water disappearance'],[6.71,'arrow',.31,'chart into map'],
 [7.16,'sweep',.33,'regional locator'],[8.33,'click',.27,'American falls locator'],
 [9.35,'popup',.31,'Horseshoe label'],[10.9,'arrow',.34,'separate water channels'],
 [12.4,'type',.28,'two waterfalls annotated'],[14.7,'cinematic',.41,'map-to-dam geometry'],
 [15.35,'debris',.31,'rock placement 1'],[16.2,'debris',.31,'rock placement 2'],
 [17.1,'debris',.31,'rock placement 3'],[17.9,'debris',.30,'cofferdam sealed'],
 [19.6,'arrow',.33,'rerouted water velocity'],[21.6,'sweep',.27,'flow explanation finish'],
 [22.68,'fast',.43,'river to rock face'],[23.42,'cinematic',.34,'dry cliff reveal'],
 [25.4,'type',.26,'rock fracture annotation'],[27.26,'click',.22,'talus overlay'],
 [28.4,'debris',.24,'rock cross-section'],[31.5,'arrow',.30,'geology cutaway'],
 [32.30,'debris',.22,'rock layer reveal'],[33.48,'click',.27,'core drill arm'],[34.6,'tick',.25,'drill descends'],
 [36.1,'type',.26,'48 borings annotation'],[37.6,'click',.28,'pressure gauge'],
 [38.8,'popup',.22,'crack labels'],[41.65,'riser',.25,'transition to restoration'],
 [42.35,'debris',.30,'dam breakdown'],[43.65,'arrow',.35,'water reconnect'],
 [45.2,'fast',.40,'river current resumes'],[46.9,'sweep',.34,'first cascade'],
 [48.7,'cinematic',.30,'full flowing water'],[50.70,'type',.21,'1975 archival transition'],
 [51.18,'sweep',.35,'policy report enters'],[52.45,'type',.28,'1975 publication'],
 [54.5,'click',.27,'highlighted recommendation'],[56.2,'chime',.25,'document conclusion'],
 [58.1,'arrow',.30,'final waterfall and policy'],[60.5,'sweep',.29,'quote settling'],
 [61.35,'chime',.38,'masthead signature'],[63.1,'popup',.15,'final hold']
];
cueEvents.splice(0,cueEvents.length,...NF_CUES.map(q=>q.slice(0,3)));
window.CURIO_CUE_SHEET=NF_CUES.map(([at,key,gain,trigger])=>({at,filename:NF_FILE[key],gain,trigger,source:'Owner Google Drive SFX library'}));
const nfInit=player.init.bind(player);
player.init=async function(){
 await nfInit();
 if(Object.keys(this.fx).length<11)throw Error('Niagara user Drive sound pack not fully decoded');
 if(!this.voice&&window.CURIO_EMBEDDED_VOICE){
  const rsp=await fetch('data:audio/mpeg;base64,'+window.CURIO_EMBEDDED_VOICE);
  this.voice=await this.audioCtx.decodeAudioData(await rsp.arrayBuffer());
  $('voiceStatus').textContent='Niagara narration included · '+this.voice.duration.toFixed(1)+' seconds';
 }
 if(!this.voice)throw Error('Niagara master cannot render without narration');
};
// Noise-loop source is ORIGINAL sound design, not misrepresented archival audio.
function nfWaterBuffer(ctx){
 if(player._waterBuffer)return player._waterBuffer;
 const sr=ctx.sampleRate,dur=4,buffer=ctx.createBuffer(2,Math.floor(sr*dur),sr);
 for(let c=0;c<2;c++){
  const a=buffer.getChannelData(c);let seed=1234567+3949*c,z=0;
  for(let i=0;i<a.length;i++){seed=(seed*1664525+1013904223)>>>0;
    const white=seed/4294967296*2-1;z=.985*z+.015*white;
    a[i]=Math.max(-1,Math.min(1,white*.27+z*.95));
  }
 }player._waterBuffer=buffer;return buffer;
}
player.attach=function(ctx,dest,offset,start){
 const comp=ctx.createDynamicsCompressor();comp.threshold.value=-18;comp.knee.value=21;comp.ratio.value=4.1;comp.attack.value=.007;comp.release.value=.2;
 const master=ctx.createGain();master.gain.value=.81;comp.connect(master);master.connect(dest);
 const route=(src,vol)=>{let v=ctx.createGain();v.gain.value=vol;src.connect(v);v.connect(comp);return src};
 for(const [when,key,gain] of cueEvents){
  const b=player.fx[key];if(!b)continue;
  if(when+b.duration<=offset)continue;
  const s=route(ctx.createBufferSource(),gain);s.buffer=b;let on=Math.max(when,offset);s.start(start+on-offset,Math.max(0,offset-when));player.sources.push(s);
 }
 if(player.voice&&offset<player.voice.duration){const v=route(ctx.createBufferSource(),1.08);v.buffer=player.voice;v.start(start,offset);player.sources.push(v)}
 // Waterfall roar band, mixed down during dry American Falls sequence but preserving distant Horseshoe.
 const buffer=nfWaterBuffer(ctx);
 const source=ctx.createBufferSource();source.buffer=buffer;source.loop=true;source.loopEnd=4;
 let lp=ctx.createBiquadFilter();lp.type='lowpass';lp.frequency.value=1900;
 let gWater=ctx.createGain();source.connect(lp);lp.connect(gWater);gWater.connect(comp);
 // absolute audio envelope – avoid incorrect 0s values on seek.
 const waterGain=t=>t<3?(.24-.02*t):t<6?.18*(1-smooth((t-3)/3))+.027:t<42?.028:t<50?.028+.19*smooth((t-42)/8):.218;
 const st=start;
 gWater.gain.setValueAtTime(waterGain(offset),st);
 for(let tick=Math.ceil(offset*4)/4;tick<=D;tick+=.25)gWater.gain.linearRampToValueAtTime(waterGain(tick),st+tick-offset);
 source.start(start,offset%4);player.sources.push(source);
 // Layered evolving chord pad + little descending water-drop musical arpeggio.
 const chords=[[130.81,164.81,196,261.63],[146.83,174.61,220,293.66],[123.47,155.56,185,246.94],[130.81,164.81,196,261.63]];
 for(let bar=0;bar<32;bar++){
  let at=bar*2;if(at+2<=offset)continue;
  const t0=Math.max(at,offset),dur=Math.min(2,at+2-t0),when=start+t0-offset,ns=chords[Math.floor(bar/4)%4];
  for(let n=0;n<ns.length;n++){
   const o=ctx.createOscillator(),flt=ctx.createBiquadFilter(),env=ctx.createGain();
   o.type=n===0?'triangle':'sine';o.frequency.value=ns[n]*(n===0?.5:1);
   flt.type='lowpass';flt.frequency.value=900+(n*210);
   let volume=n===0?.067:.037;
   if(t0<7)volume*=.75;if(t0>=43&&t0<=52)volume*=1.18;
   env.gain.setValueAtTime(.0001,when);env.gain.linearRampToValueAtTime(volume,when+.20);
   env.gain.setValueAtTime(volume,when+Math.max(.24,dur-.19));env.gain.exponentialRampToValueAtTime(.0001,when+dur);
   o.connect(flt);flt.connect(env);env.connect(comp);o.start(when);o.stop(when+dur+.02);player.sources.push(o);
  }
 }
 for(let beat=0;beat<128;beat++){
  let at=beat*.5;if(at<offset||at>=64)continue;
  const t=start+at-offset,o=ctx.createOscillator(),a=ctx.createGain();
  const root=chords[Math.floor(beat/16)%4][0],f=[1,1.5,2,1.5][beat%4];
  o.frequency.value=root*f;o.type='sine';
  const vol=beat%4===0?.025:.011;
  a.gain.setValueAtTime(.0001,t);a.gain.linearRampToValueAtTime(vol,t+.018);a.gain.exponentialRampToValueAtTime(.0001,t+.21);
  o.connect(a);a.connect(comp);o.start(t);o.stop(t+.23);player.sources.push(o);
 }
};
renderAt(.03);
