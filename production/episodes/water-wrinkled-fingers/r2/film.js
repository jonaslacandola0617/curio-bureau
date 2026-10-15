const DURATION=36.3,SCALE=Number(new URLSearchParams(location.search).get('scale')||1);
function foundation(q,t,dark=false){q.fillStyle=dark?'#172b39':'#ece8dc';q.fillRect(0,0,1080,1920);q.save();q.globalAlpha=dark?.16:1;q.drawImage(backing,0,0);q.restore();}
let overlays=[];function queueOverlay(fn){overlays.push(fn)}
function caption(q,lines){queueOverlay(q=>{q.save();q.textAlign='center';lines.forEach((s,i)=>{q.font='800 43px Manrope';let w=q.measureText(s).width;q.fillStyle='#f5f0e7';q.fillRect(540-w/2-20,908+i*58,w+40,58);text(q,s,540,953+i*58,43)});q.restore()})}
function printedPhoto(q,img,sx,sy,sw,sh,x,y,w,h,rot=0){q.save();q.translate(x+w/2,y+h/2);q.rotate(rot);q.shadowColor='#12233077';q.shadowBlur=22;q.shadowOffsetY=16;q.drawImage(img,sx,sy,sw,sh,-w/2,-h/2,w,h);q.shadowColor='transparent';material(q,'ink.jpg',-w/2,-h/2,w,h,.28,'soft-light');material(q,'plastic.jpg',-w/2,-h/2,w,h,.23,'screen');q.restore()}
function heading(q,lines,t,size=108,y=245){queueOverlay(q=>{q.save();q.filter=`blur(${(window.lastFinishingState?.cut||0)*5*SCALE}px)`;q.beginPath();q.rect(40,y-size-10,1010,lines.length*size*1.13+60);q.clip();q.translate(0,130*(1-span(t,0,.48)));lines.forEach((s,i)=>text(q,s,60,y+i*size*1.08,size,'#172330','Playfair',900));q.restore()})}
function finish(q,t){q.save();q.globalAlpha=.12;q.globalCompositeOperation='soft-light';q.drawImage(printFinish,0,0);q.restore();q.save();q.globalAlpha=.008*(.5+.5*Math.sin(Math.floor(t*12)*3.1));q.fillStyle='#172330';q.fillRect(0,0,1080,1920);q.restore()}
function hook(q,t,closing=false){foundation(q,t);const p=span(t,0,3.1);let z=1+.20*p;
 // A photographic inspection crop, not a fabricated macro or a skin morph.
 q.save();q.translate(540+18*p,1190-55*p);q.scale(z,z);q.rotate(-.07+.035*p);q.translate(-540,-1190);
 printedPhoto(q,images['wrinkled_photo.jpg'],2780,360,1300,2350,180,370,820,1482,-.015);q.restore();
 // Duplicated offset print edges are material registration, never new evidence.
 q.save();q.globalCompositeOperation='multiply';q.globalAlpha=.14;printedPhoto(q,images['wrinkled_photo.jpg'],2780,360,1300,2350,183,372,820,1482,-.015);q.restore();
 q.save();let gr=q.createLinearGradient(0,0,0,700);gr.addColorStop(0,'#ece8dc');gr.addColorStop(.58,'#ece8dcf9');gr.addColorStop(1,'#ece8dc00');q.fillStyle=gr;q.fillRect(0,0,1080,950);q.restore();
 heading(q,closing?['Familiar folds.','Active response.']:['Your nerves','make wrinkles.'],t,closing?94:108,235);
 tag(q,closing?'MORE THAN SOAKING':'WATER + YOUR NERVOUS SYSTEM',64,closing?1680:615,closing?425:655,'#f0cc28',-.025,27);
 // An annotation selects a real groove; the photo retains its geometry.
 q.save();q.strokeStyle='#f0cc28';q.lineWidth=5;strokeCubic(q,[600,1180,720,1130,855,1205,777,1345],span(t,.6,1.25));q.restore();
 text(q,'Photograph / Sebastian Wallroth · CC BY 3.0 · crop',60,1870,18,'#34414b','Manrope',650);
 if(!closing){let cap=t<3.8?["These wrinkles aren't just",'water soaking into your skin.']:['Your nervous system','helps create them.'];caption(q,cap)}else caption(q,t<1.4?['A familiar wrinkle,']:['with an active response','underneath.']);finish(q,t)
}
function grip(q,t){foundation(q,t);heading(q,['A better grip?'],t,116,240);let move=span(t,0,2.0);q.save();q.translate(540,570);q.scale(1+.10*move,1+.10*move);q.translate(-540,-570);
 printedPhoto(q,images['grip_study.png'],0,0,1750,1311,65,320,950,712,-.025);q.restore();
 // Camera selects the actual finger/load-cell contact in the experimental image.
 let sel=span(t,.4,1.1);q.save();q.strokeStyle='#f0cc28';q.lineWidth=5;strokeCubic(q,[720,650,660,550,865,535,906,651],sel);q.restore();
 text(q,'Davis / 2021 · actual grip-force apparatus',64,1084,24);text(q,'Figure 1 · cropped and annotated · CC BY',64,1124,20,'#48525a');
 const a=span(t,2.82,3.3),b=span(t,4.82,5.25);let shift=span(t,6.1,6.65);
 q.save();q.translate(0,-30*shift);q.globalAlpha=a;tag(q,'BENEFIT IN SOME TASKS',70,1285,596,'#f0cc28',-.015,30);text(q,'2013 / wet-object handling',76,1350,30);text(q,'2021 / grip-force efficiency',76,1400,30);q.restore();
 q.save();q.globalAlpha=b;q.translate(35*(1-b),0);tag(q,'NO BENEFIT IN ANOTHER TEST',70,1520,708,'#e98972',.015,30);text(q,'2014 / wet-object dexterity',76,1585,30);q.restore();
 if(t>6.1){q.save();q.globalAlpha=shift;text(q,'Different tasks. Mixed evidence.',70,1745,35);q.restore()}
 let lines=t<2.5?['Could that help you','grip wet objects?']:t<4.8?['Some experiments','found a benefit.']:t<6.1?["Others didn't."]:t<8.7?['So better grip','is a possibility,']:['not a proven','evolutionary purpose.'];caption(q,lines);finish(q,t)
}
let world,worldCtx,finisher;
function renderAt(t){const output=canvas.getContext('2d',{willReadFrequently:true});overlays=[];ctx=worldCtx;ctx.setTransform(SCALE,0,0,SCALE,0,0);ctx.globalAlpha=1;ctx.filter='none';ctx.globalCompositeOperation='source-over';window.editorialTime=t;
 if(t<6.6)hook(ctx,t);else if(t<18.6)renderMechanism(t-6.6);else if(t<30.6)grip(ctx,t-18.6);else hook(ctx,t-30.6,true);
 ctx=output;finisher.apply(world,ctx,t,{enabled:!window.disableFinishing});ctx.setTransform(SCALE,0,0,SCALE,0,0);for(const draw of overlays)draw(ctx);CurioBrand.drawEndcard(ctx,t,DURATION);window.currentTime=t;
}
(async()=>{await Promise.all([document.fonts.load('900 108px Playfair'),document.fonts.load('900 104px "Playfair Display"'),document.fonts.load('800 43px Manrope')]);for(const[k,v]of Object.entries(ASSETS)){if(!v.startsWith('data:image/'))continue;let im=new Image();im.src=v;await im.decode();images[k]=im}prepare();prepareCaches();canvas=document.querySelector('canvas');canvas.width=1080*SCALE;canvas.height=1920*SCALE;ctx=canvas.getContext('2d',{willReadFrequently:true});world=document.createElement('canvas');world.width=canvas.width;world.height=canvas.height;worldCtx=world.getContext('2d');finisher=new CurioEditorialFinish.EditorialFinish(canvas.width,canvas.height);window.canvas=canvas;window.ctx=ctx;window.renderAt=renderAt;window.renderReady=true;renderAt(0)})();
