const images={};let fingerBefore,fingerAfter;
const options={heading:true,captions:true,guide:false};
function text(q,s,x,y,size=28,color='#172330',family='Manrope',weight=800){q.font=`${weight} ${size}px ${family}`;q.fillStyle=color;q.fillText(s,x,y)}
function path(q,pts){q.beginPath();for(const p of pts){if(p[0]==='M')q.moveTo(p[1],p[2]);else if(p[0]==='L')q.lineTo(p[1],p[2]);else if(p[0]==='C')q.bezierCurveTo(...p.slice(1));else if(p[0]==='Q')q.quadraticCurveTo(...p.slice(1));else if(p[0]==='Z')q.closePath()}}
function cover(q,im,x,y,w,h){const s=Math.max(w/im.width,h/im.height);q.drawImage(im,x+(w-im.width*s)/2,y+(h-im.height*s)/2,im.width*s,im.height*s)}
function material(q,key,x,y,w,h,a=.25,blend='multiply'){q.save();q.globalAlpha=a;q.globalCompositeOperation=blend;cover(q,images[key],x,y,w,h);q.restore()}
function tag(q,s,x,y,w,c='#f0cc28',angle=0,size=26){q.save();q.translate(x,y);q.rotate(angle);q.shadowColor='#17233028';q.shadowBlur=5;q.shadowOffsetY=4;q.fillStyle=c;q.fillRect(-8,-34,w,51);q.shadowColor='transparent';text(q,s,4,0,size);q.restore()}
function prepare(){for(const [name,sx,sw]of [['fingerBefore',2,203],['fingerAfter',219,203]]){const c=document.createElement('canvas');c.width=203;c.height=282;const q=c.getContext('2d');path(q,[['M',13,282],['L',13,116],['C',9,55,29,18,67,7],['C',119,-10,174,3,186,45],['C',199,76,197,113,197,154],['L',200,282],['Z']]);q.clip();q.filter='grayscale(1) contrast(1.18)';q.drawImage(images['study_pair.jpg'],sx,0,sw,282,0,0,203,282);if(name==='fingerBefore')fingerBefore=c;else fingerAfter=c}}
function drawFinger(q,state){const x=648,y=253,w=380,h=w*282/203;q.save();q.translate(x+w/2,y+h/2);q.rotate(-.10);q.translate(-w/2,-h/2);
 // Source-preserving photo mask; the same crop/scale anchors both observed states.
 q.save();q.shadowColor='#7c4b3b44';q.shadowOffsetX=2;q.shadowOffsetY=-1;q.shadowBlur=0;q.drawImage(state===0?fingerBefore:fingerAfter,0,0,w,h);q.restore();
 q.save();q.shadowColor='#17233066';q.shadowBlur=19;q.shadowOffsetX=-12;q.shadowOffsetY=15;q.drawImage(state===0?fingerBefore:fingerAfter,0,0,w,h);q.restore();
 if(state===1){q.drawImage(fingerBefore,0,0,w,h);q.save();q.beginPath();q.rect(w*.46,0,w*.54,h);q.clip();q.drawImage(fingerAfter,0,0,w,h);q.restore();q.strokeStyle='#f0cc28';q.lineWidth=5;q.beginPath();q.moveTo(w*.46,-10);q.lineTo(w*.46,h+10);q.stroke();q.fillStyle='#f0cc28';q.beginPath();q.arc(w*.46,h*.52,11,0,Math.PI*2);q.fill()}
 if(state===2){q.strokeStyle='#f0cc28';q.lineWidth=5;q.lineCap='round';q.beginPath();q.moveTo(w*.22,h*.39);q.bezierCurveTo(w*.39,h*.30,w*.52,h*.37,w*.43,h*.57);q.stroke();q.beginPath();q.moveTo(w*.39,h*.62);q.bezierCurveTo(w*.51,h*.67,w*.58,h*.66,w*.70,h*.60);q.stroke()}
 material(q,'ink.jpg',0,0,w,h,.05,'soft-light');q.restore();
 tag(q,state===0?'BEFORE IMMERSION':state===1?'OBSERVED COMPARISON':'AFTER 30 MIN IN WATER',590,206,430,'#f0cc28',-.035,25);
 // Secondary source print supplies the other observed state, not a different hand.
 q.save();q.translate(104,505);q.rotate(.07);q.fillStyle='#f7f0de';q.shadowColor='#17233035';q.shadowBlur=10;q.shadowOffsetY=8;q.fillRect(-18,-14,184,272);q.shadowColor='transparent';material(q,'paper.jpg',-18,-14,184,272,.6);q.drawImage(state===0?fingerAfter:fingerBefore,0,0,150,208);text(q,state===0?'AFTER / SAME FIGURE':'BEFORE / SAME FIGURE',-3,239,14);q.restore();
 if(state===1){text(q,'A / BEFORE',645,241,17);text(q,'B / AFTER',858,241,17)}
 text(q,'Research photographs / Guy German',65,795,18,'#48525a','Manrope',650)
}
function tissue(q,state){const u=state/2;q.save();q.translate(537,1390);q.rotate(-.055);q.shadowColor='#101e3045';q.shadowBlur=18;q.shadowOffsetY=19;
 path(q,[['M',-489,-211],['L',451,-225],['L',491,245],['L',-470,269],['Z']]);q.fillStyle='#f5f0e7';q.fill();q.shadowColor='transparent';q.save();q.clip();material(q,'paper.jpg',-500,-240,1020,530,.64);q.restore();
 text(q,'UNDER THE SURFACE',-443,-165,24);text(q,'Mechanism schematic / not to scale',-443,-126,20,'#4b5258','Manrope',650);
 let amp=3+u*25,drop=u*34,contract=u*48;function top(x){return -50+drop+amp*Math.sin((x+405)*.034)*Math.sin((x+420)/850*Math.PI)}
 // Qualitative finger-pulp field: thickness and vessel caliber change independently.
 q.save();q.beginPath();q.moveTo(-424,top(-424));for(let x=-424;x<=424;x+=3)q.lineTo(x,top(x));q.lineTo(447,174-contract);q.bezierCurveTo(210,187-contract,-190,180-contract,-447,172-contract);q.lineTo(-424,top(-424));q.closePath();q.clip();q.fillStyle='#d4bca1';q.fillRect(-470,-100,940,360);material(q,'fibre.jpg',-470,-100,940,360,.55);let seed=3108;const rand=()=>{seed=(seed*1664525+1013904223)>>>0;return seed/4294967296};for(let i=0;i<2400;i++){let x=rand()*900-450,y=rand()*295-60;q.globalAlpha=.16;q.strokeStyle='#5d5448';q.lineWidth=.8;q.beginPath();q.moveTo(x,y);q.lineTo(x+4+rand()*6,y-3);q.stroke()}q.restore();
 // Dashed previous skin boundary is an explanatory reference, not a measured scan.
 if(state){q.save();q.globalAlpha=.48;q.strokeStyle='#172330';q.lineWidth=2;q.setLineDash([8,7]);q.beginPath();q.moveTo(-424,-50);q.lineTo(424,-50);q.stroke();q.restore()}
 // Printed surface layer remains attached to the same supporting field.
 q.beginPath();for(let x=-424;x<=424;x+=3){if(x===-424)q.moveTo(x,top(x));else q.lineTo(x,top(x))}for(let x=424;x>=-424;x-=3)q.lineTo(x,top(x)+19);q.closePath();q.fillStyle='#d57864';q.fill();q.save();q.clip();material(q,'ink.jpg',-435,-83,870,125,.3);q.restore();q.strokeStyle='#273541';q.lineWidth=2;q.stroke();
 q.save();q.beginPath();q.rect(-424,-70,848,260-contract);q.clip();
 const drawVessel=()=>{q.beginPath();q.moveTo(-452,97-contract*.35);q.bezierCurveTo(-267,47,-130,118,11,93);q.bezierCurveTo(160,72,253,112,452,63-contract*.2)};
 if(state){q.save();q.strokeStyle='#a5796b';q.globalAlpha=.3;q.lineWidth=44;q.lineCap='round';drawVessel();q.stroke();q.restore()}
 q.lineCap='butt';let width=44-u*25;drawVessel();q.lineWidth=width+6;q.strokeStyle='#253340';q.stroke();drawVessel();q.lineWidth=width;q.strokeStyle='#bb5f50';q.stroke();drawVessel();q.lineWidth=width*.45;q.strokeStyle='#e5a58a';q.stroke();
 for(const a of [-198,112]){q.beginPath();q.moveTo(a,88);q.bezierCurveTo(a-10,69,a+34,48,a+22,Math.max(top(a+22)+32,45));q.lineWidth=width*.38+3;q.strokeStyle='#253340';q.stroke();q.lineWidth=width*.38;q.strokeStyle='#c8755e';q.stroke()}
 q.restore();
 text(q,state===0?'Vessel before narrowing':state===1?'Vessel narrowing':'Narrower vessel',-437,218,25);text(q,'QUALITATIVE CHANGE',219,218,17,'#48525a','Manrope',700);
 if(state===1){ // A lifted inspection corner exposes the final surface state without a new card.
 q.save();q.translate(373,-213);q.shadowColor='#17233038';q.shadowBlur=9;path(q,[['M',-84,0],['Q',-22,14,30,87],['L',43,0],['Z']]);q.fillStyle='#e3d6bc';q.fill();q.restore()}
 q.restore();
}
function render(state){const q=document.getElementById('frame'+state).getContext('2d');q.clearRect(0,0,1080,1920);q.fillStyle='#ece8dc';q.fillRect(0,0,1080,1920);material(q,'paper.jpg',0,0,1080,1920,.52);q.save();q.globalAlpha=.12;q.strokeStyle='#617687';q.lineWidth=.6;for(let x=40;x<1080;x+=41){q.beginPath();q.moveTo(x,0);q.lineTo(x,1920);q.stroke()}for(let y=24;y<1920;y+=41){q.beginPath();q.moveTo(0,y);q.lineTo(1080,y);q.stroke()}q.restore();
 text(q,'CURIO BUREAU / WATER + SKIN',62,100,22);text(q,'0'+(state+1),968,100,24);
 if(options.heading){text(q,'Your nerves',60,225,85,'#172330','Playfair',900);text(q,'shape this.',60,322,94,'#172330','Playfair',900);q.save();q.globalAlpha=.8;q.fillStyle='#f0cc28';q.rotate(-.015);q.fillRect(60,349,455,16);q.restore()}
 drawFinger(q,state);
 // Screen-fixed caption band stays clear of the photographic subject and mechanism.
 if(options.captions){const ss=[['A familiar change.','What causes it?'],['Blood vessels beneath','the skin narrow.'],['Less volume underneath.','The surface folds.']][state];q.save();q.textAlign='center';text(q,ss[0],540,954,43);text(q,ss[1],540,1012,43);q.restore()}
 tissue(q,state);
 tag(q,state===0?'LOOK BENEATH':state===1?'NARROWING':'THE SURFACE FOLDS',68,1729,state===2?402:326,'#f0cc28',-.025,29);
 text(q,['Same fingertip. Two observed conditions.','A change below the skin.','Water starts it. Nerves help shape it.'][state],63,1810,25,'#26323c','Manrope',700);
 material(q,'ink.jpg',0,0,1080,1920,.07,'soft-light');q.save();let v=q.createRadialGradient(620,740,280,500,1000,1210);v.addColorStop(0,'#14263600');v.addColorStop(1,'#14263628');q.fillStyle=v;q.fillRect(0,0,1080,1920);q.restore();
 text(q,'Photo: Guy German / shared with credit · Schematic: Curio Bureau',63,1880,18,'#34414b','Manrope',650);
 if(options.guide){q.fillStyle='#00bf9720';q.fillRect(0,806,1080,307);q.strokeStyle='#008e73';q.lineWidth=3;q.setLineDash([12,9]);q.strokeRect(0,806,1080,307);text(q,'Caption band / 42–58%',38,856,25)}
}
function draw(){for(let i=0;i<3;i++)render(i)}
function choose(n){document.body.classList.toggle('single',n>=0);document.querySelectorAll('.state').forEach((e,i)=>e.classList.toggle('active',n===i));document.querySelectorAll('[data-state]').forEach(e=>e.setAttribute('aria-pressed',Number(e.dataset.state)===n))}
for(const b of document.querySelectorAll('[data-state]'))b.onclick=()=>choose(Number(b.dataset.state));document.querySelector('#heading').onclick=()=>{options.heading=!options.heading;draw()};document.querySelector('#captions').onclick=()=>{options.captions=!options.captions;draw()};document.querySelector('#guide').onclick=()=>{options.guide=!options.guide;draw()};
(async()=>{await Promise.all([document.fonts.load('900 94px Playfair'),document.fonts.load('800 43px Manrope')]);for(const[k,v]of Object.entries(ASSETS)){if(!v.startsWith('data:image/'))continue;const im=new Image();im.src=v;await im.decode();images[k]=im}prepare();draw();choose(-1);window.artReady=true})();
