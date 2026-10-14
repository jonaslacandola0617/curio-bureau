const images={};let portraitMono,micMatte,field,bodyTint;
const scene={heading:true,safe:false};
function path(q,points){q.beginPath();for(const p of points){if(p[0]==='M')q.moveTo(p[1],p[2]);else if(p[0]==='L')q.lineTo(p[1],p[2]);else if(p[0]==='C')q.bezierCurveTo(...p.slice(1));else if(p[0]==='Q')q.quadraticCurveTo(...p.slice(1));else if(p[0]==='Z')q.closePath()}}
function txt(q,s,x,y,size=28,colour='#172330',family='Manrope',weight=800){q.font=`${weight} ${size}px ${family}`;q.fillStyle=colour;q.fillText(s,x,y)}
function cover(q,im,x,y,w,h){const s=Math.max(w/im.width,h/im.height);q.drawImage(im,x+(w-im.width*s)/2,y+(h-im.height*s)/2,im.width*s,im.height*s)}
function material(q,key,x,y,w,h,opacity=.2,mode='multiply'){q.save();q.globalCompositeOperation=mode;q.globalAlpha=opacity;cover(q,images[key],x,y,w,h);q.restore()}
function label(q,s,x,y,w,colour='#f0cd29',rotation=0,size=28){q.save();q.translate(x,y);q.rotate(rotation);q.shadowColor='#0003';q.shadowBlur=4;q.shadowOffsetY=4;q.fillStyle=colour;q.fillRect(-8,-34,w,54);q.shadowColor='transparent';txt(q,s,5,5,size);q.restore()}
function prepare(){portraitMono=document.createElement('canvas');portraitMono.width=images['speaking_portrait_v1.png'].width;portraitMono.height=images['speaking_portrait_v1.png'].height;let p=portraitMono.getContext('2d');p.filter='grayscale(1) contrast(1.13)';p.drawImage(images['speaking_portrait_v1.png'],0,0);p.filter='none';p.globalCompositeOperation='source-atop';p.globalAlpha=.17;cover(p,images['ink.jpg'],0,0,portraitMono.width,portraitMono.height);
bodyTint=document.createElement('canvas');bodyTint.width=portraitMono.width;bodyTint.height=portraitMono.height;let b=bodyTint.getContext('2d');b.drawImage(portraitMono,0,0);b.globalCompositeOperation='source-in';b.fillStyle='#d57864';b.fillRect(0,0,b.canvas.width,b.canvas.height);
micMatte=document.createElement('canvas');micMatte.width=1876;micMatte.height=640;let m=micMatte.getContext('2d');m.drawImage(images['microphone.jpg'],1900,775,1876,640,0,0,1876,640);let d=m.getImageData(0,0,m.canvas.width,m.canvas.height),p1=d.data,seen=new Uint8Array(m.canvas.width*m.canvas.height),que=new Int32Array(seen.length),a=0,z=0;const add=i=>{if(i<0||i>=seen.length||seen[i])return;seen[i]=1;if(p1[4*i]*.2126+p1[4*i+1]*.7152+p1[4*i+2]*.0722>=165){que[z++]=i;p1[i*4+3]=0}};for(let x=0;x<m.canvas.width;x++){add(x);add((m.canvas.height-1)*m.canvas.width+x)}for(let y=0;y<m.canvas.height;y++){add(y*m.canvas.width);add(y*m.canvas.width+m.canvas.width-1)}while(a<z){let i=que[a++],x=i%m.canvas.width;add(i-m.canvas.width);add(i+m.canvas.width);if(x)add(i-1);if(x<m.canvas.width-1)add(i+1)}m.putImageData(d,0,0);
field=document.createElement('canvas');field.width=1080;field.height=1920;const f=field.getContext('2d');f.save();f.translate(0,180);path(f,[['M',-60,551],['C',70,390,271,410,392,525],['C',475,602,593,605,653,743],['C',664,832,586,916,414,935],['C',208,957,81,1068,-20,1008],['Z']]);f.clip();f.fillStyle='#eccb28';f.fillRect(0,0,1080,1920);material(f,'fibre.jpg',0,350,800,850,.42);let seed=8127;function rand(){seed=(seed*1664525+1013904223)>>>0;return seed/4294967296}for(let i=0;i<21000;i++){let x=rand()*760,y=385+rand()*720;f.globalAlpha=.16+rand()*.18;f.fillStyle=i%3?'#342c1b':'#fff7d9';f.fillRect(x,y,rand()*1.8+.3,rand()*2+.3)}f.globalAlpha=.2;f.strokeStyle='#2b2118';f.lineWidth=2;for(let i=0;i<13;i++){f.beginPath();for(let x=0;x<700;x+=4){let y=660+i*15+Math.sin(x*.016+i*.8)*22+Math.sin(x*.041)*7;if(x===0)f.moveTo(x,y);else f.lineTo(x,y)}f.stroke()}f.restore()}
function portrait(q,state){const x=252,y=508,w=1010,h=1212; q.save();q.shadowColor='#09131b44';q.shadowBlur=21;q.shadowOffsetY=18;q.drawImage(bodyTint,x+32,y-14,w,h);q.shadowColor='transparent';q.drawImage(portraitMono,x,y,w,h);q.restore(); // Source-associated colour stays behind the same speaking subject.
 q.save();q.globalAlpha=.24;q.beginPath();q.ellipse(902,1035,130,275,-.24,0,Math.PI*2);q.clip();q.drawImage(bodyTint,x+10,y-6,w,h);q.restore();
 label(q,'BODY',824,1192,164,'#d57864',-.06,34);txt(q,'internal component',824,1251,22,'#26313a','Manrope',700)
}
function mic(q){q.save();q.translate(-80,1145);q.rotate(-.12);q.scale(-1,1);q.shadowColor='#0006';q.shadowBlur=16;q.shadowOffsetY=18;q.drawImage(micMatte,-460,-157,920,314);q.restore()}
function record(q,state){if(state===0)return;const u=state===1?.55:1;const cx=455,cy=1432,angle=state===1?-.19:-.10;q.save();q.translate(cx,cy);q.rotate(angle);q.shadowColor='#07121c66';q.shadowBlur=25;q.shadowOffsetY=26;
 path(q,[['M',-405,-175],['L',355,-193],['Q',383,-170,385,-125],['L',405,248],['L',-389,264],['Q',-414,220,-405,-175],['Z']]);q.fillStyle='#f5f0e7';q.fill();q.shadowColor='transparent';q.save();q.clip();material(q,'paper.jpg',-415,-200,840,480,.64);q.globalAlpha=.95;
 // A source-exact texture fragment, not newly drawn data, occupies the captured image window.
 q.drawImage(field,0,830,360,125,-355,-135,650,225);
 if(state===1){q.fillStyle='#f5f0e7';q.fillRect(-355+650*u,-141,650*(1-u)+10,239)}
 txt(q,'RECORDED',-352,156,47,'#172330','Playfair',900);txt(q,'AIRBORNE COMPONENT',-352,201,23);
 if(state===2){q.strokeStyle='#172330';q.lineWidth=3;q.beginPath();envelope.forEach((v,i)=>{let x=-347+i*640/(envelope.length-1),y=67-v*45;if(i===0)q.moveTo(x,y);else q.lineTo(x,y)});q.stroke();txt(q,'Existing narration / signal envelope',-352,241,18,'#3b4550','Manrope',650)}
 q.restore();q.restore();
 if(state===1){q.save();q.translate(372,1260);q.rotate(-.26);q.shadowColor='#0006';q.shadowBlur=20;q.shadowOffsetY=16;path(q,[['M',-270,-245],['Q',-40,-166,145,85],['L',-7,191],['Q',-98,-32,-338,-91],['Z']]);q.fillStyle='#f2d030';q.fill();q.shadowColor='transparent';q.save();q.clip();q.drawImage(field,0,830,360,125,-350,-260,650,500);material(q,'paper.jpg',-350,-260,650,500,.18);q.restore();q.restore()}
}
function render(state){const q=document.getElementById('frame'+state).getContext('2d');q.clearRect(0,0,1080,1920);q.fillStyle='#eeeae0';q.fillRect(0,0,1080,1920);material(q,'paper.jpg',0,0,1080,1920,.52);q.save();q.globalAlpha=.12;q.strokeStyle='#647687';q.lineWidth=.6;for(let x=42;x<1080;x+=38){q.beginPath();q.moveTo(x,0);q.lineTo(x,1920);q.stroke()}for(let y=20;y<1920;y+=38){q.beginPath();q.moveTo(0,y);q.lineTo(1080,y);q.stroke()}q.restore();
 txt(q,'CURIO BUREAU / CAPTURE STUDY',74,111,22,'#172330','Manrope',800);txt(q,'0'+(state+1),965,111,26);
 if(scene.heading){txt(q,'What gets recorded?',74,248,84,'#172330','Playfair',900)}
 q.save();q.globalAlpha=state===2?.58:1;q.drawImage(field,0,0);q.restore();label(q,'AIR',130,698,142,'#f0cd29',-.06,41);portrait(q,state);mic(q);
 if(state===1){q.save();q.strokeStyle='#f5f0e7';q.lineWidth=5;q.setLineDash([13,9]);q.strokeRect(0,830,360,125);q.restore()}
 record(q,state);
 // Finishing describes the substrate and printing, while face detail stays readable.
 material(q,'ink.jpg',0,0,1080,1920,.09,'soft-light');q.save();let g=q.createRadialGradient(610,850,160,540,940,1150);g.addColorStop(0,'#fff0');g.addColorStop(1,'#07172745');q.fillStyle=g;q.fillRect(0,0,1080,1920);q.restore();
 if(state===0){label(q,'TWO COMPONENTS',90,1693,361,'#f0cd29',-.04,29);txt(q,'One stays with the speaker.',82,1770,35,'#172330','Playfair',900)}
 if(state===1){label(q,'SELECTION',89,1760,247,'#f0cd29',-.04,30)}
 if(state===2){label(q,'AIR KEPT',80,1761,233,'#f0cd29',-.04,32);txt(q,'Original internal component stays at source.',76,1823,24)}
 txt(q,'Portrait illustration · conceptual material · no anatomical measurement',74,1883,19,'#23313e','Manrope',650);
 if(scene.safe){q.fillStyle='#00dba720';q.fillRect(0,806,1080,307);q.strokeStyle='#009b79';q.lineWidth=3;q.setLineDash([12,10]);q.strokeRect(0,806,1080,307);q.setLineDash([]);txt(q,'Caption composition review: 42–58%',25,845,25)}
}
function redraw(){for(let i=0;i<3;i++)render(i)}
function choose(n){document.body.classList.toggle('single',n>=0);document.querySelectorAll('.item').forEach((e,i)=>e.classList.toggle('active',i===n));document.querySelectorAll('[data-select]').forEach(b=>b.setAttribute('aria-pressed',Number(b.dataset.select)===n))}
document.querySelectorAll('[data-select]').forEach(b=>b.onclick=()=>choose(Number(b.dataset.select)));document.querySelector('#headings').onclick=()=>{scene.heading=!scene.heading;redraw()};document.querySelector('#safe').onclick=()=>{scene.safe=!scene.safe;redraw()};
(async()=>{await Promise.all([document.fonts.load('900 84px Playfair'),document.fonts.load('800 28px Manrope')]);await document.fonts.ready;for(const [key,value] of Object.entries(ASSETS)){if(!value.startsWith('data:image/'))continue;const im=new Image();im.src=value;await im.decode();images[key]=im}prepare();redraw();choose(-1);window.artReady=true})();
