// Documentary pixels stay in source coordinates; paper/camera/foreground are independent.
const bridgeMaskPoints=[[.295,.366],[.313,.371],[.362,.420],[.446,.496],[.538,.568],[.628,.639],[.721,.721],[.826,.804],[.815,.811],[.754,.787],[.696,.742],[.682,.748],[.677,.721],[.625,.681],[.600,.682],[.597,.657],[.556,.625],[.542,.629],[.538,.608],[.510,.584],[.499,.590],[.487,.573],[.441,.535],[.427,.538],[.424,.516],[.392,.492],[.378,.502],[.361,.480],[.342,.449],[.323,.414],[.302,.387]];
function bridgePhotoMask(q){q.beginPath();bridgeMaskPoints.forEach((v,i)=>i?q.lineTo(v[0]*1200,v[1]*800):q.moveTo(v[0]*1200,v[1]*800));q.closePath();}
const nearBankPoints=[[0,.83],[.21,.77],[.29,.75],[.48,.72],[.61,.71],[.70,.72],[.84,.78],[.94,.82],[1,.87],[1,1],[0,1]];
function bankMask(q){q.beginPath();nearBankPoints.forEach((v,i)=>i?q.lineTo(v[0]*1200,v[1]*800):q.moveTo(v[0]*1200,v[1]*800));q.closePath();}
let photoPlanes=null;
function getPhotoPlanes(){if(photoPlanes)return photoPlanes;let w=imgs.bridgePhoto.width,h=imgs.bridgePhoto.height,k=w/1200;photoPlanes={};for(let name of ['background','bridge','foreground']){let c=document.createElement('canvas');c.width=w;c.height=h;let q=c.getContext('2d');q.scale(k,k);q.drawImage(imgs.bridgePhoto,0,0,1200,800);if(name==='background'){q.globalCompositeOperation='destination-out';bridgePhotoMask(q);q.fill();bankMask(q);q.fill();}else{q.globalCompositeOperation='destination-in';(name==='bridge'?bridgePhotoMask:bankMask)(q);q.fill();if(name==='foreground'){q.globalCompositeOperation='destination-out';bridgePhotoMask(q);q.fill();}}photoPlanes[name]=c;}return photoPlanes;}
function photoOpening(t,a){
 paper('#ded1b5');let push=ease(span(t,1,4.7)),cameraX=35*Math.sin(t*.5),exit=smooth(span(t,a-.65,a));
 ctx.save();ctx.translate(-1350*exit,0);
 ctx.save();ctx.translate(cameraX*.12,-push*90);ctx.scale(1+push*.035,1+push*.035);title(['LONDON BRIDGE','IN ARIZONA'],t,-.6,245,100,1);ctx.restore();
 ctx.save();ctx.translate(540-cameraX*.4,1290+push*30);ctx.rotate(-.035+push*.025);ctx.scale(1+push*.14,1+push*.14);ctx.translate(-600,-400);
 // Overscanned print matte, fiber edges, physically separate foreground paper corners.
 ctx.shadowColor='#0d1c2b70';ctx.shadowBlur=38;ctx.shadowOffsetY=22;ctx.fillStyle=C.paper;ctx.beginPath();ctx.moveTo(-35,-27);ctx.lineTo(1232,-20);ctx.lineTo(1238,837);ctx.lineTo(-28,830);ctx.closePath();ctx.fill();ctx.shadowBlur=0;CurioMaterials.paper(ctx,-35,-27,1273,864);
 ctx.save();ctx.beginPath();ctx.rect(0,0,1200,800);ctx.clip();
 // Gap backing samples water from the same photograph: an editorial repair, not a source claim.
 ctx.drawImage(imgs.bridgePhoto,0,imgs.bridgePhoto.height*.57,imgs.bridgePhoto.width,imgs.bridgePhoto.height*.13,0,0,1200,800);
 let planes=getPhotoPlanes();ctx.translate(-230,-240);ctx.scale(1.35,1.35);
 ctx.save();ctx.translate(-cameraX*.12,-push*3);ctx.drawImage(planes.background,0,0,1200,800);ctx.restore();
 ctx.save();ctx.translate(cameraX*.23,-push*12);ctx.drawImage(planes.bridge,0,0,1200,800);ctx.restore();
 ctx.save();ctx.translate(cameraX*.48,-push*21);ctx.drawImage(planes.foreground,0,0,1200,800);ctx.restore();

 ctx.restore();CurioMaterials.print(ctx,0,0,1200,800);
 // Photo labels stay printed on the source matte, never inherited by captions.
 txt('LAKE HAVASU CITY · ARIZONA',26,784,23,C.paper);txt('Photo: S. Winkvist, 2011 · CC0',26,819,18,'#344b53');
 ctx.fillStyle='#e6dcc5';ctx.globalAlpha=.8;ctx.save();ctx.translate(36,-18);ctx.rotate(-.21);ctx.fillRect(-55,-24,180,60);CurioMaterials.paper(ctx,-55,-24,180,60);ctx.restore();ctx.save();ctx.translate(1090,805);ctx.rotate(-.18);ctx.fillRect(-55,-24,180,60);CurioMaterials.paper(ctx,-55,-24,180,60);ctx.restore();ctx.restore();
 // A nearer paper strip passes the camera while the entire photo leaves the viewport.
 if(exit>0){ctx.fillStyle='#e9dfc9';ctx.fillRect(1250-1350*exit,-50,1380,2030);CurioMaterials.paper(ctx,1250-1350*exit,-50,1380,2030);}
 ctx.restore();
}
function roughSheet(x,y,w,h,rot,draw){ctx.save();ctx.translate(x,y);ctx.rotate(rot);ctx.shadowColor='#0d1c2b65';ctx.shadowBlur=27;ctx.shadowOffsetY=18;ctx.fillStyle=C.paper;ctx.beginPath();for(let i=0;i<=24;i++){let xx=-w/2+w*i/24,yy=-h/2+Math.sin(i*7.1)*2.5;i?ctx.lineTo(xx,yy):ctx.moveTo(xx,yy);}ctx.lineTo(w/2+4,h/2-2);ctx.lineTo(-w/2-3,h/2+2);ctx.closePath();ctx.fill();ctx.shadowBlur=0;CurioMaterials.paper(ctx,-w/2,-h/2,w,h);draw();ctx.restore();}
function saleEvidenceShot(t,a){
 paper('#dbd7c9');let enter=ease(span(t,a,a+.7)),price=ease(span(t,a+.8,a+2.2)),select=ease(span(t,a+6,a+7.4));
 title(['A landmark.','For sale.'],t,a,235,109);
 // Contemporary source remains distinct from our purchase summary.
 roughSheet(490,1320+190*(1-enter)-select*35,920,640,-.065+select*.03,()=>{
  txt('PARLIAMENTARY RECORD',-400,-250,24);txt('24 April 1968',-400,-202,25);txt('London Bridge (Sale)',-400,-118,54,C.ink,'Playfair Display');
  txt('Mr. MacDermot',-400,-47,28);ctx.fillStyle=C.gold;ctx.fillRect(-405,3,738*select,111);
  txt('“no power to prevent',-390,48,45,C.ink,'Playfair Display');txt('the sale”',-390,103,45,C.ink,'Playfair Display');
  txt('Reply concerning the sale of constituent parts.',-400,164,24);txt('Transcript excerpt · not a purchase receipt',-400,211,21,'#4d6265');
  txt('Contains Parliamentary information licensed',-400,259,16,'#4d6265');txt('under the Open Parliament Licence v3.0.',-400,281,16,'#4d6265');
 });
 ctx.save();ctx.globalAlpha=1-select*.92;ctx.translate(80*price,-110*price);ctx.scale(1+price*.12,1+price*.12);
 roughSheet(565,1300+230*(1-enter),690,425,.035,()=>{
  txt('EDITORIAL PURCHASE SUMMARY',-297,-148,22);txt('April 1968',-297,-93,34);ctx.fillStyle=C.gold;ctx.fillRect(-300,-53,603*price,103);txt('$2,460,000',-292,30,79,C.ink,'Playfair Display');
  txt('Buyer: Robert McCulloch',-297,107,28);txt('Source: USGS / TIME, April 26, 1968',-297,165,18,'#465b60');
 });ctx.restore();
 if(select>.01){ctx.save();ctx.globalAlpha=select;txt('AN ATTRACTION FOR',540,723,36,C.ink,'Manrope','center');txt('LAKE HAVASU CITY',540,780,42,C.ink,'Playfair Display','center');ctx.restore();}
 sourceLabel('Sale record: Hansard, 24 April 1968 · UK Parliament');
}
