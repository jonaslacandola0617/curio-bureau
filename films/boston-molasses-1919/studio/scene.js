/* CURIO BUREAU / EPISODE 005 — ART-DIRECTED 2D/2.5D CANVAS
 * Original vector illustration. Historical photographs are separately attributed.
 * Exact render is derived solely from absolute timeline seconds. */
(function(root){
"use strict";
const W=1080,H=1920,DURATION=76,FPS=30;
const P={navy:"#0D1C2B",ink:"#091622",ivory:"#F5F0E7",gold:"#C8A26B",coral:"#D57864",brown:"#54331F",amber:"#AD7950",steel:"#53616A",silver:"#C8CED0",dim:"#8F9BA0"};
const TAU=Math.PI*2;
const clamp=(v,a=0,b=1)=>Math.max(a,Math.min(b,v));
const ease=x=>{x=clamp(x);return x*x*(3-2*x)};
const inv=(t,a,b)=>ease((t-a)/(b-a));
const lerp=(a,b,f)=>a+(b-a)*f;
function fill(ctx,color,x,y,w,h){ctx.fillStyle=color;ctx.fillRect(x,y,w,h)}
function line(ctx,color,width,pts){ctx.beginPath();pts.forEach((p,i)=>i?ctx.lineTo(p[0],p[1]):ctx.moveTo(p[0],p[1]));ctx.strokeStyle=color;ctx.lineWidth=width;ctx.stroke()}
function round(ctx,x,y,w,h,r,color){ctx.beginPath();ctx.roundRect(x,y,w,h,r);ctx.fillStyle=color;ctx.fill()}
function circle(ctx,x,y,r,c){ctx.beginPath();ctx.arc(x,y,r,0,TAU);ctx.fillStyle=c;ctx.fill()}
function txt(ctx,s,x,y,size=34,color=P.ivory,font="Manrope",align="left",weight=600,max){
  ctx.save();ctx.font=weight+" "+size+"px '"+font+"'";ctx.fillStyle=color;ctx.textAlign=align;
  ctx.textBaseline="alphabetic";if(max)ctx.fillText(s,x,y,max);else ctx.fillText(s,x,y);ctx.restore();
}
function head(ctx,t,section){
  const a=.65+.2*Math.sin(t*.7);
  txt(ctx,"C / B",80,108,28,P.gold,"Manrope","left",800);
  line(ctx,"rgba(200,162,107,.4)",2,[[185,95],[832,95]]);
  txt(ctx,("0"+5)+" / "+section,996,108,20,P.gold,"Manrope","right",700);
  const pr=clamp(t/DURATION);
  fill(ctx,"rgba(245,240,231,.14)",80,1850,920,2);
  fill(ctx,P.gold,80,1850,920*pr,2);
}
function background(ctx,t,variant=0){
  fill(ctx,P.navy,0,0,W,H);
  let grad=ctx.createLinearGradient(0,0,1200,1920);
  grad.addColorStop(0,variant===1?"#283341":"#0D1C2B");grad.addColorStop(.52,"#132433");grad.addColorStop(1,"#06121D");
  fill(ctx,grad,0,0,W,H);
  ctx.strokeStyle="rgba(245,240,231,.035)";ctx.lineWidth=1;
  for(let i=0;i<25;i++){let x=(i*139+Math.sin(t*.23+i)*6)%1120;ctx.beginPath();ctx.moveTo(x,0);ctx.lineTo(x+160,1920);ctx.stroke()}
  for(let j=0;j<8;j++){ctx.beginPath();ctx.moveTo(0,j*263-52);ctx.lineTo(W,j*263-52);ctx.stroke();}
  for(let k=0;k<260;k++){let x=(k*7919)%1080,y=(k*5237)%1920;fill(ctx,"rgba(245,240,231,.035)",x,y,2,2);}
}
function windowGrid(ctx,x,y,w,h,seed){
  for(let yy=y+30;yy<y+h-20;yy+=80){for(let xx=x+23;xx<x+w-18;xx+=56){
    let k=(((xx*.33+yy*.17+seed*43)|0)%5);
    fill(ctx,k===0?"#D3BB86":"#253847",xx,yy,24,44);
    line(ctx,"rgba(10,20,27,.6)",3,[[xx+12,yy],[xx+12,yy+44]]);
  }}
}
function city(ctx,t,shift=0){
  ctx.save();ctx.translate(shift,0);
  // historically inspired illustration; deliberately not a photographic reconstruction
  const blocks=[
    [-100,312,280,775,"#35414A"],[180,210,190,850,"#687078"],[370,360,210,675,"#3A4850"],
    [575,270,245,760,"#515F64"],[820,365,300,740,"#39454E"]];
  blocks.forEach((b,i)=>{
    fill(ctx,b[5],b[0],b[1],b[2],b[3]);windowGrid(ctx,b[0],b[1],b[2],b[3],i);
    line(ctx,"#A0A7A0",3,[[b[0],b[1]],[b[0]+b[2],b[1]]]);
    for(let z=0;z<4;z++)line(ctx,"rgba(245,240,231,.13)",2,[[b[0],b[1]+190*z],[b[0]+b[2],b[1]+190*z]]);
  });
  // Boston-style elevated rail with truss assembly
  fill(ctx,"#1E2F39",0,746,W,36);
  for(let x=24;x<1100;x+=185){
    fill(ctx,"#243640",x,760,26,440);
    line(ctx,"#8B8D80",7,[[x+13,785],[x+180,1040],[x+13,1040],[x+180,785]]);
    for(let y=830;y<1130;y+=108)line(ctx,"#86959A",2,[[x,y],[x+26,y]]);
    circle(ctx,x+13,769,5,P.gold);
  }
  line(ctx,P.gold,3,[[0,784],[W,784]]);
  // street, trolley rails, walkway
  fill(ctx,"#20272B",0,1115,W,675);
  for(let n=0;n<6;n++){
    let m=n*175;
    line(ctx,"rgba(196,178,148,.33)",3,[[540+(m-540)*.28,1115],[m*1.9-420,1790]]);
  }
  // horse cart as composed silhouette
  const drift=Math.sin(t*.5)*5;
  ctx.save();ctx.translate(240+drift,1274);
  fill(ctx,"#B7A999",0,0,265,132);fill(ctx,"#273640",16,25,228,91);
  fill(ctx,P.gold,25,20,206,12);
  for(let x of [60,211]){circle(ctx,x,140,51,"#18232A");circle(ctx,x,140,35,"#9CA39B");circle(ctx,x,140,11,"#28303B");for(let i=0;i<8;i++){let a=i*TAU/8;line(ctx,"#4D565A",3,[[x,140],[x+34*Math.cos(a),140+34*Math.sin(a)]])}}
  line(ctx,"#A7A39A",7,[[245,46],[360,70],[382,90]]);
  ctx.restore();
  ctx.restore();
}
function flood(ctx,t,amount=1,offsetY=1190){
  const advance=amount*1200,drift=t*64;
  const g=ctx.createLinearGradient(0,offsetY-280,0,1920);
  g.addColorStop(0,"#9C6341");g.addColorStop(.28,"#5F3828");g.addColorStop(.63,"#341E19");g.addColorStop(1,"#281715");
  ctx.save();
  ctx.beginPath();
  ctx.moveTo(-180,1910);
  for(let x=-150;x<1190;x+=22){
    let edge=offsetY+90*Math.sin((x+drift)/150)-45*Math.sin((x+t*170)/56);
    edge-=170*(1-ease((x+50)/800))*amount;
    ctx.lineTo(x,edge);
  }
  ctx.lineTo(1300,1990);ctx.closePath();ctx.fillStyle=g;ctx.fill();
  // multiple viscous shear bands and high-light troughs
  for(let i=0;i<18;i++){
    let y=offsetY+65+i*44; ctx.beginPath();
    for(let x=-120;x<=1200;x+=17){
      let yy=y+11*Math.sin((x+drift*(1+i*.04))/60+i*.78)+17*Math.sin(x/147+t*.85+i);
      if(x===-120)ctx.moveTo(x,yy);else ctx.lineTo(x,yy);
    }
    ctx.strokeStyle=i%3===0?"rgba(222,159,104,.48)":"rgba(28,14,13,.46)";
    ctx.lineWidth=i%3===0?9:6;ctx.stroke();
  }
  // surface droplets and chunks
  for(let k=0;k<32;k++){
    let x=(k*157+83+t*(35+k%4*10))%1200-70;
    let y=offsetY+32+(k*79)%430+Math.sin(t*2.1+k)*16;
    const r=3+(k%5)*2;
    circle(ctx,x,y,r,k%3?"#AA6A43":"#CC9360");
  }
  ctx.restore();
}
function rivets(ctx,x,y,w,h,t){
  for(let xx=x+33;xx<x+w-25;xx+=61)for(let yy=y+28;yy<y+h-20;yy+=122){
    circle(ctx,xx,yy,5,"#A7A49A");circle(ctx,xx-1,yy-1,2,"#E1D5B7");
  }
}
function tank(ctx,t,detail=0){
  ctx.save();ctx.translate(0,detail?-160:0);
  const x=196,y=310,w=668,h=1030;
  const shadow=ctx.createLinearGradient(x,y,x+w,y);
  shadow.addColorStop(0,"#1A2933");shadow.addColorStop(.11,"#56636B");
  shadow.addColorStop(.45,"#88908F");shadow.addColorStop(.8,"#3D4C56");shadow.addColorStop(1,"#1A2A34");
  fill(ctx,shadow,x,y,w,h);
  // cylinder elliptical top and curved bands
  ctx.beginPath();ctx.ellipse(x+w/2,y,w/2,73,0,0,TAU);ctx.fillStyle="#65747A";ctx.fill();
  ctx.beginPath();ctx.ellipse(x+w/2,y+h,w/2,67,0,0,TAU);ctx.fillStyle="#26343D";ctx.fill();
  for(let j=0;j<10;j++){
    const by=y+55+j*95;line(ctx,"rgba(198,202,196,.45)",3,[[x,by],[x+w,by]]);
    ctx.beginPath();ctx.ellipse(x+w/2,by,w/2,45,0,0,Math.PI);ctx.strokeStyle="rgba(0,10,19,.38)";ctx.lineWidth=4;ctx.stroke();
  }
  for(let col of [x+55,x+w/2,x+w-40]){
    line(ctx,"rgba(225,215,180,.27)",3,[[col,y+32],[col,y+h-18]]);
  }
  rivets(ctx,x,y,w,h,t);
  // ladder
  fill(ctx,"#B4A586",x+w-118,y+128,7,777);
  fill(ctx,"#B4A586",x+w-75,y+128,7,777);
  for(let s=0;s<23;s++)line(ctx,"#D8C4A0",5,[[x+w-114,y+147+s*32],[x+w-71,y+147+s*32]]);
  line(ctx,"#AFAF9E",6,[[x+70,y+6],[x+85,y-180],[x+330,y-180],[x+330,y-120]]);
  if(detail){const a=inv(t,18,22);let off=a*24;for(let i=0;i<16;i++)circle(ctx,x+70+(i*37)%60,y+330+i*45,3+(i%3),P.brown);}
  ctx.restore();
}
function archival(ctx,img,t,title,sub,pan=0){
  if(!img){round(ctx,50,250,980,1150,20,"#283744");txt(ctx,"ARCHIVAL PHOTO ASSET UNAVAILABLE",540,830,28,P.ivory,"Manrope","center");return;}
  const rx=57,ry=235,rw=966,rh=1265;
  ctx.save();ctx.beginPath();ctx.rect(rx,ry,rw,rh);ctx.clip();
  const scale=1.06+inv(t,pan,pan+12)*.15;
  const ratio=Math.max(rw/img.width,rh/img.height)*scale;
  const sw=img.width*ratio,sh=img.height*ratio;
  const px=rx+(rw-sw)*(.5+.12*Math.sin(t*.18)),py=ry+(rh-sh)*(.56+.07*Math.cos(t*.13));
  ctx.drawImage(img,px,py,sw,sh);
  fill(ctx,"rgba(13,28,43,.12)",rx,ry,rw,rh);
  ctx.restore();
  round(ctx,72,290,890,78,12,"rgba(9,22,34,.89)");
  txt(ctx,title,106,341,29,P.ivory,"Manrope","left",700);
  txt(ctx,sub,84,1470,20,P.gold,"Manrope","left",800);
}
function cardHeader(ctx,title,sub,y=236){
 txt(ctx,title,72,y,66,P.ivory,"Playfair Display","left",650,935);
 txt(ctx,sub.toUpperCase(),77,y+58,21,P.gold,"Manrope","left",800,940);
 line(ctx,"rgba(200,162,107,.5)",3,[[77,y+81],[1002,y+81]]);
}
function sceneHook(ctx,t,a){
 city(ctx,t,-40*Math.sin(t*.2));
 flood(ctx,t,a,1005-85*Math.sin(t*.2));
 let r=inv(t,.5,2.2);
 fill(ctx,"rgba(9,22,34,"+(0.08+0.17*r)+")",0,0,1080,665);
 txt(ctx,"THIS WASN'T WATER.",76,400,62,P.ivory,"Playfair Display","left",700,960);
 if(t>=1.7) {
  txt(ctx,"MOLASSES.",74,530,108,P.gold,"Playfair Display","left",700,950);
  round(ctx,78,557,310*inv(t,1.7,2.6),8,4,P.coral);
 }
 if(t>4){txt(ctx,"BOSTON  ·  1919",82,675,26,P.ivory,"Manrope","left",700);}
 ctx.save();ctx.globalAlpha=inv(t,5.5,6.4)*.85;
 line(ctx,P.ivory,5,[[845,790],[845,560],[890,560]]);txt(ctx,"THE SOURCE?",880,535,24,P.ivory,"Manrope","center",700);ctx.restore();
}
function sceneTank(ctx,t){
 tank(ctx,t);
 let q=inv(t,8.5,10.3);
 round(ctx,70,380,500,115,12,P.navy);txt(ctx,"2.3 MILLION",88,459,65,P.ivory,"Playfair Display","left",700);
 txt(ctx,"US GALLONS",91,505,25,P.gold,"Manrope","left",800);
 txt(ctx,"NORTH END  /  COMMERCIAL ST.",88,1440,28,P.gold,"Manrope","left",800);
 txt(ctx,"A 50-FOOT STEEL TANK",88,1510,42,P.ivory,"Playfair Display","left",600);
 // map line morphing to site location
 line(ctx,"rgba(200,162,107,.75)",4,[[60,1160],[160,1070],[210,1110],[290,1025],[440,1080]]);
 circle(ctx,440,1080,7,P.coral);
 if(t>12){txt(ctx,"PURlTY DISTILLING  /  TANK",88,1590,22,P.dim,"Manrope","left",700);}
}
function sceneWarnings(ctx,t){
 background(ctx,t,1);
 // large asymmetric sectional wall
 ctx.save();ctx.translate(-80,0);
 fill(ctx,"#394852",120,220,760,1270);
 let steel=ctx.createLinearGradient(120,0,850,0);
 steel.addColorStop(0,"#3C4B57");steel.addColorStop(.5,"#77868A");steel.addColorStop(1,"#263843");
 fill(ctx,steel,120,220,760,1270);
 for(let y=248;y<1480;y+=220){
  line(ctx,"rgba(208,217,213,.5)",4,[[120,y],[880,y]]);
  for(let x=150;x<875;x+=95){circle(ctx,x,y,9,"#C0C2B8");circle(ctx,x-2,y-2,3,"#F5F0E7");}
 }
 // pressure visualization grows from bottom
 const p=inv(t,19,26);
 ctx.globalAlpha=.15+.16*p;
 fill(ctx,P.coral,150,1320-p*610,680,610+p*30);ctx.globalAlpha=1;
 // animated leak falling from row 3
 for(let i=0;i<14;i++){
  const drop=(((t-18.5)*(200+i*4)+i*77)%640+640)%640;
  ctx.beginPath();ctx.ellipse(830+Math.sin(i)*12,885+drop,4+2*(i%3),11,0,0,TAU);ctx.fillStyle="#AE704B";ctx.fill();
 }
 ctx.restore();
 txt(ctx,"THE WARNINGS",80,330,70,P.ivory,"Playfair Display","left",700);
 round(ctx,770,480,260,300,12,P.navy);
 txt(ctx,"LEAKS",795,565,51,P.gold,"Playfair Display","left",700);
 line(ctx,P.coral,6,[[790,600],[1012,600]]);
 txt(ctx,"REPORTED",794,655,27,P.ivory,"Manrope","left",800);
 txt(ctx,"BEFORE THE",794,696,25,P.ivory,"Manrope","left",700);
 txt(ctx,"RUPTURE",794,737,25,P.ivory,"Manrope","left",800);
 if(t>23){txt(ctx,"TANK WALL  /  SCHEMATIC SECTION",78,1580,23,P.gold,"Manrope","left",750);}
}
function sceneFailure(ctx,t){
 background(ctx,t);
 cardHeader(ctx,"HOW DID IT FAIL?","ENGINEERING RECONSTRUCTION",276);
 const p=inv(t,28,34);
 // detailed cylindrical cross-section
 const cx=550,cy=1060;circle(ctx,cx,cy,420,"#314451");circle(ctx,cx,cy,355,"#B37B52");circle(ctx,cx,cy,320,"#62432D");
 for(let j=0;j<20;j++){
  let a=j*TAU/20,cx2=cx+390*Math.cos(a),cy2=cy+390*Math.sin(a);
  circle(ctx,cx2,cy2,9,"#D5C8AA");
 }
 // twisted radial stress contour arcs
 for(let j=0;j<7;j++){
  ctx.beginPath();ctx.arc(cx,cy,232+j*21,Math.PI*1.03,Math.PI*1.72);
  ctx.strokeStyle=j%2?P.coral:P.gold;ctx.lineWidth=3+j;ctx.globalAlpha=.22+.1*j;ctx.stroke();ctx.globalAlpha=1;
 }
 ctx.save();ctx.translate(cx,cy);ctx.rotate(-.2);
 const gap=30+270*p;
 const crack=[[-10,-405],[8,-250],[-14,-120],[12,30],[-30,150],[5,322],[0,418]].map(([x,y])=>[x+gap/2,y]);
 line(ctx,"#E3B176",11,crack);
 ctx.restore();
 const q=inv(t,30,35);
 for(let i=0;i<18;i++){
   let x=380+i*17,y=1370+i*6+t*28;
   line(ctx,"rgba(218,123,87,"+(q*.7)+")",3,[[x,y],[x+(i%3)*20,y-40]]);
 }
 round(ctx,88,570,340,100,11,P.navy);txt(ctx,"STEEL + SEAMS",111,631,30,P.ivory,"Manrope","left",800);
 round(ctx,670,1370,330,120,11,P.navy);txt(ctx,"UNDER LOAD",700,1441,34,P.coral,"Manrope","left",800);
 txt(ctx,"PROPOSED LOAD PATH  •  NOT TO SCALE",80,1670,20,P.dim,"Manrope","left",600);
}
function sceneDisaster(ctx,t,assets){
 city(ctx,t,-15);
 flood(ctx,t,1.1,940);
 const show=inv(t,36,38);
 txt(ctx,"JANUARY 15, 1919",90,290,26,P.gold,"Manrope","left",850);
 if(t>=40) {
  const alpha=inv(t,40,41.6);
  ctx.save();ctx.globalAlpha=alpha;
  round(ctx,68,380,500,200,14,"rgba(9,22,34,.90)");
  txt(ctx,"21",93,490,112,P.ivory,"Playfair Display","left",700);
  txt(ctx,"LIVES LOST",251,483,28,P.coral,"Manrope","left",800);
  ctx.restore();
 }
 if(t>=42){txt(ctx,"PEOPLE / HOMES / STREETS",88,645,31,P.ivory,"Manrope","left",800);}
}
function sceneRescue(ctx,t,assets){
 background(ctx,t);
 const img=t<55?assets.aerial:assets.after;
 archival(ctx,img,t,t<55?"THE AFTERMATH":"RESCUE AND RECOVERY",
          "1919 PHOTOGRAPH  /  BOSTON ARCHIVAL COLLECTION",50);
 if(t<55){
  txt(ctx,"21 DEAD",76,1584,70,P.ivory,"Playfair Display","left",700);
  txt(ctx,"~150 INJURED",76,1666,47,P.gold,"Manrope","left",800);
 } else{
  round(ctx,67,1535,940,150,12,P.navy);
  txt(ctx,"RESCUERS FOUGHT THROUGH THE DEBRIS",93,1592,26,P.ivory,"Manrope","left",700,880);
  txt(ctx,"HARBOR SALT WATER HELPED THE CLEANUP",93,1647,25,P.gold,"Manrope","left",700,880);
 }
}
function sceneInvestigation(ctx,t,assets){
 background(ctx,t);
 if(assets.after)archival(ctx,assets.after,t,"AFTER THE COLLAPSE","JANUARY 1919 / PUBLIC-DOMAIN ARCHIVE",61);
 fill(ctx,"rgba(13,28,43,.78)",0,290,1080,1460);
 const p=inv(t,63,67);
 round(ctx,70,335,940,850,15,"#F1EBE0");
 txt(ctx,"CURIO BUREAU",105,407,25,P.navy,"Manrope","left",800);
 line(ctx,P.gold,4,[[104,436],[975,436]]);
 txt(ctx,"THE INVESTIGATION",105,540,52,P.navy,"Playfair Display","left",700);
 txt(ctx,"1919",113,628,36,P.brown,"Manrope","left",800);
 txt(ctx,"Tank breaks. Owners suggest sabotage.",113,695,25,P.navy,"Manrope","left",650,840);
 line(ctx,P.gold,4,[[120,730],[120,838]]);
 txt(ctx,"1925",113,902,37,P.coral,"Manrope","left",850);
 txt(ctx,"An auditor finds negligence.",113,955,27,P.navy,"Manrope","left",800);
 txt(ctx,"EDITORIAL SUMMARY — NOT AN ORIGINAL DOCUMENT",110,1135,17,"#53616A","Manrope","left",700);
 const u=inv(t,69,72);
 if(t>=69){
   round(ctx,80,1240,925,350,12,P.navy);
   txt(ctx,"THE WARNING",122,1370,70,P.ivory,"Playfair Display","left",700);
   txt(ctx,"SIGNS WERE",122,1458,75,P.ivory,"Playfair Display","left",700);
   txt(ctx,"ALREADY THERE.",122,1546,75,P.gold,"Playfair Display","left",700);
 }
 if(t>=74){
  fill(ctx,P.navy,0,0,1080,1920);
  txt(ctx,"CURIO",104,795,156,P.ivory,"Playfair Display","left",650);
  txt(ctx,"BUREAU",104,957,156,P.ivory,"Playfair Display","left",650);
  line(ctx,P.gold,6,[[108,1005],[962,1005]]);
  txt(ctx,"Stories, systems, and surprises.",111,1070,37,P.gold,"Manrope","left",700);
  txt(ctx,"005  /  THE GREAT MOLASSES FLOOD",112,1210,24,P.ivory,"Manrope","left",700);
 }
}
function caption(ctx,cues,t){
 let cue=cues.find(c=>t>=c.start&&t<c.end);
 if(!cue) return;
 const msg=cue.text;
 // sentence-length protection: two lines max at phone scale
 const words=msg.trim().split(/\s+/);
 let lines=[];let acc="";
 for(const w of words){
  if((acc+" "+w).length>23 && acc){lines.push(acc);acc=w}else acc+=(acc?" ":"")+w;
 } if(acc)lines.push(acc);
 const y=1632-lines.length*58;
 round(ctx,61,y-63,958,lines.length*62+73,17,"rgba(6,16,25,.92)");
 lines.forEach((ln,i)=>txt(ctx,ln,540,y+i*62,46,P.ivory,"Manrope","center",800,908));
}
function render(ctx,t,assets={},cues=[]){
 t=clamp(t,0,DURATION-1/FPS);
 ctx.save();ctx.setTransform(1,0,0,1,0,0);
 // apply native 4K scaling from logical 1080x1920
 ctx.scale(ctx.canvas.width/W,ctx.canvas.height/H);
 background(ctx,t);
 const c=t<8?0:t<18?1:t<28?2:t<36?3:t<48?4:t<62?5:6;
 if(c===0)sceneHook(ctx,t,1);
 if(c===1)sceneTank(ctx,t);
 if(c===2)sceneWarnings(ctx,t);
 if(c===3)sceneFailure(ctx,t);
 if(c===4)sceneDisaster(ctx,t,assets);
 if(c===5)sceneRescue(ctx,t,assets);
 if(c===6)sceneInvestigation(ctx,t,assets);
 if(t<74)head(ctx,t,["DISASTER","THE SCALE","WARNINGS","WHY IT FAILED","THE SURGE","RECOVERY","ACCOUNTABILITY"][c]);
 if(t<74)caption(ctx,cues,t);
 ctx.restore();
}
root.Curio005={render,duration:DURATION,fps:FPS,style:P};
})(typeof window!=="undefined"?window:globalThis);
