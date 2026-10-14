/* Original Curio directed paper/image science composition. Native logical coordinates. */
const C={ink:'#0D1C2B',paper:'#F5F0E7',yellow:'#FFDA12',red:'#DD3933',blue:'#347CAB'};
const E=DATA.timing.events;
const arrival=(t,a,b)=>CurioMotion.ease(span(t,a,b),CurioMotion.curves.fastSettle);
function text(s,x,y,size=30,color=C.ink,align='left',serif=false){ctx.save();ctx.fillStyle=color;ctx.textAlign=align;ctx.font=`${serif?900:700} ${size}px ${serif?'"Playfair Display"':'Manrope'}`;ctx.fillText(s,x,y);ctx.restore();}
function stroke(points,color,width,progress,t,seed=1){if(progress<=0)return;let p=CurioFinishing.boilPath(points,t,{seed,amplitudePx:.48,fps:12,lockEnds:true,wavelengthPx:35});let len=p.slice(1).map((a,i)=>Math.hypot(a[0]-p[i][0],a[1]-p[i][1])),remain=len.reduce((a,b)=>a+b,0)*clamp(progress),draw=[p[0]];for(let i=0;i<len.length;i++){let u=clamp(remain/len[i]);draw.push([mix(p[i][0],p[i+1][0],u),mix(p[i][1],p[i+1][1],u)]);remain-=len[i];if(remain<=0)break;}CurioFinishing.drawInkStroke(ctx,draw,{color,width,bleedPx:.35,bleedAlpha:.22});}
function marker(x,y,w,h,u,t,color=C.yellow){ctx.save();ctx.globalAlpha*=.93;ctx.fillStyle=color;ctx.beginPath();ctx.moveTo(x,y+2);ctx.lineTo(x+w*clamp(u),y-2+Math.sin(Math.floor(t*12)));ctx.lineTo(x+w*clamp(u),y+h);ctx.lineTo(x,y+h+3);ctx.closePath();ctx.fill();ctx.restore();}
function desk(){ctx.fillStyle=C.ink;ctx.fillRect(0,0,W,H);CurioMaterials.surface(ctx,'paperFiber',0,0,W,H,{alpha:.36,mode:'soft-light',tileWidth:1420});CurioMaterials.surface(ctx,'photocopy',0,0,W,H,{alpha:.13,mode:'screen',tileWidth:1000});}
function paper(w,h,draw,{kind='clean',color=C.paper}={}){ctx.save();ctx.shadowColor='#0008';ctx.shadowBlur=23;ctx.shadowOffsetY=14;ctx.fillStyle=color;ctx.beginPath();ctx.moveTo(-w/2,0);ctx.lineTo(w/2-18,kind==='clip'?4:0);ctx.lineTo(w/2,kind==='clip'?23:0);ctx.lineTo(w/2,h-7);ctx.lineTo(w/2-9,h);ctx.lineTo(-w/2+5,h-3);ctx.closePath();ctx.fill();ctx.shadowColor='transparent';ctx.save();ctx.clip();CurioMaterials.paper(ctx,-w/2,0,w,h);draw(-w/2,0,w,h);ctx.restore();if(kind==='clip'){ctx.fillStyle='#d8d0c0';ctx.beginPath();ctx.moveTo(w/2-18,3);ctx.lineTo(w/2-18,24);ctx.lineTo(w/2,24);ctx.closePath();ctx.fill();}ctx.restore();}
function photograph(img,x,y,w,h,rot=0,credit='NASA',crop){ctx.save();ctx.translate(x,y);ctx.rotate(rot);paper(w,h+73,()=>{ctx.save();ctx.beginPath();ctx.rect(-w/2+19,19,w-38,h-25);ctx.clip();if(crop){ctx.drawImage(img,...crop,-w/2+19,19,w-38,h-25);}else{let s=Math.max((w-38)/img.width,(h-25)/img.height),iw=img.width*s,ih=img.height*s;ctx.drawImage(img,-iw/2,19+((h-25)-ih)/2,iw,ih);}CurioMaterials.print(ctx,-w/2+19,19,w-38,h-25);ctx.restore();text(credit,-w/2+28,h+43,19);});ctx.restore();}
function title(lines,t,a,{y=215,size=110,highlight=-1,color=C.paper}={}){lines.forEach((s,i)=>{let u=arrival(t,a+i*.10,a+i*.10+.42);ctx.save();ctx.globalAlpha*=u;ctx.translate(540,y+i*size*1.06+80*(1-u));ctx.font=`900 ${size}px "Playfair Display"`;let width=ctx.measureText(s).width,scale=Math.min(1,950/width);ctx.scale(scale,scale);if(i===highlight)marker(-width/2-22,-size*.83,width+44,size*1.04,span(t,a+.08,a+.44),t);text(s,0,0,size,i===highlight?C.ink:color,'center',true);ctx.restore();});}
function focusHere(x,y,rx,ry,strength,maxBlur=9){sq.setTransform(1,0,0,1,0,0);sq.drawImage(canvas,0,0);focus.apply(scene,fq,{cx:x,cy:y,rx,ry,strength,maxBlur,feather:1.05,outsideGain:.56});ctx.save();ctx.setTransform(1,0,0,1,0,0);ctx.drawImage(focused,0,0);ctx.restore();}

// Source photographs dominate; paper is their material, not the subject.
function label(s,x,y,size=26,color=C.paper){ctx.save();ctx.font=`700 ${size}px Manrope`;let w=ctx.measureText(s).width+32;ctx.fillStyle='#0d1c2bdc';ctx.fillRect(x-16,y-size-9,w,size+22);text(s,x,y,size,color);ctx.restore();}
function astro(x,y,h,rot=0,elongation=0,alpha=1){ctx.save();ctx.globalAlpha=alpha;ctx.translate(x,y);ctx.rotate(rot);let w=h*imgs.astro.width/imgs.astro.height;ctx.shadowColor='#0009';ctx.shadowBlur=21;ctx.shadowOffsetX=12;ctx.shadowOffsetY=19;ctx.drawImage(imgs.astro,-w/2,-h/2-h*elongation,w,h*(1+elongation));ctx.restore();}
function earth(x,y,d,rot=0){ctx.save();ctx.translate(x,y);ctx.rotate(rot);ctx.beginPath();ctx.arc(0,0,d/2,0,Math.PI*2);ctx.clip();ctx.drawImage(imgs.earth,-d/2,-d/2,d,d);CurioMaterials.print(ctx,-d/2,-d/2,d,d);ctx.restore();}
function imagePlane(im,x,y,w,h,r=0,crop,credit=''){photograph(im,x,y,w,h,r,credit,crop);}
function photoSpine(x,top,h,curve=0,length=0,alpha=1){ctx.save();ctx.globalAlpha=alpha;let w=h*imgs.spinePhoto.width/imgs.spinePhoto.height;ctx.shadowColor='#0005';ctx.shadowBlur=10;ctx.shadowOffsetX=8;ctx.shadowOffsetY=11;
 // Strip warp of a photographed model, not a diagnostic image or growth simulation.
 const slices=80,step=imgs.spinePhoto.height/slices;for(let i=0;i<slices;i++){let u=i/slices,v=(i+1)/slices;let dx=curve*Math.sin(Math.PI*u)*Math.sin(Math.PI*u);let dy=top+u*h-(1-u)*length;ctx.drawImage(imgs.spinePhoto,0,i*step,imgs.spinePhoto.width,step+.6,x-w/2+dx,dy,w,(h+length)/slices+.6);}ctx.restore();}
function sourceCredit(t){label('Model photo: John Campbell / CC BY 2.0 / cropped + animated',96,1667,20);}
function intro(t){const out=arrival(t,E.evidence-.42,E.evidence+.17),push=arrival(t,.78,2.20),drift=span(t,1.9,E.evidence);ctx.save();ctx.translate(-1900*out,0);
 earth(730+90*push,1600+105*push,1950+170*push,-.055*push);
 // Independent opposing travel gives depth, rather than a flat whole-frame zoom.
 astro(545-220*push-32*drift,825+105*push-25*drift,775+785*push,-.10+.12*push);
 ctx.save();ctx.translate(-120*push,-290*push);ctx.globalAlpha=1-span(t,1.10,1.73);title(['Space can make','you taller.'],t,0,{y:210,size:114,highlight:1});ctx.restore();
 if(t>1.53){let u=arrival(t,1.53,1.98);ctx.save();ctx.translate(0,80*(1-u));ctx.globalAlpha=u;label('BUT YOU DON’T KEEP IT.',145,1390,47,C.yellow);ctx.restore();}
 label('NASA photographs / editorial composite',103,1720,22);ctx.restore();}
function evidence(t){const en=arrival(t,E.evidence-.42,E.evidence+.18),out=arrival(t,E.anatomy-.43,E.anatomy+.14),grow=arrival(t,E.limit-.08,E.limit+.91);ctx.save();ctx.translate(1700*(1-en)-1700*out,0);
 earth(800,1350,1570,-.03-.012*(t-E.evidence));
 // The same source silhouette keeps a fixed bottom: an explicitly exaggerated height comparison.
 astro(300-15*grow,715,605,-.55,0,.48);astro(737+15*grow,715-45*grow,605,-.55,.10*grow,1);
 label('NORMAL HEIGHT',135,1195,27);label('IN ORBIT',630,1195,27,C.yellow);
 stroke([[175,961],[870,961]],C.paper,4,span(t,E.evidence+.15,E.evidence+.5),t,12);
 title(['Up to 3%'],t,E.limit-.15,{y:310,size:153,highlight:0});
 ctx.save();ctx.translate(540,1340);ctx.rotate(-.025);paper(750,143,()=>{text('Height change exaggerated for explanation',-341,64,27);text('Not a measurement of the photographed astronaut',-341,112,23);});ctx.restore();
 label('NASA / spinal ultrasound investigation',133,1650,24);ctx.restore();}
function anatomy(t){let en=arrival(t,E.anatomy-.43,E.anatomy+.14),peel=arrival(t,E.anatomy+.40,E.anatomy+1.20);ctx.save();ctx.translate(1430*(1-en),0);
 imagePlane(imgs.modelFull,455-260*peel,430-25*peel,1100,755,-.09+.04*peel,null,'John Campbell / CC BY 2.0 / physical model');
 ctx.save();ctx.translate(680,1120);ctx.rotate(.07);paper(850,490,()=>{text('THE CHANGE IS',-374,88,32);text('in your spine.',-375,217,99,C.ink,'left',true);text('A real physical anatomy model',-374,394,31);});ctx.restore();
 photoSpine(735+15*peel,365-85*peel,650+80*peel,0,0,peel);
 title(['Your spine.'],t,E.anatomy,{y:242,size:116});sourceCredit(t);ctx.restore();}
function loadDiagram(t){let micro=arrival(t,E.micro+.05,E.micro+1.03),straight=arrival(t,E.straighten+.05,E.straighten+.95),longer=arrival(t,E.lengthen+.02,E.lengthen+.86),exit=arrival(t,E.research-.4,E.research+.12),inspection=span(t,E.earth,E.research);ctx.save();ctx.translate(0,-2030*exit);
 // Stacked source prints establish physical identity; the foreground cutout alone changes.
 imagePlane(imgs.modelDetail,257-120*micro,1180+55*inspection,1020,470,-.09-.015*inspection,null,'John Campbell / CC BY 2.0 / model detail');
 ctx.save();ctx.translate(750+115*micro,300-45*micro);ctx.rotate(.08);paper(590,690,()=>{ctx.save();ctx.beginPath();ctx.rect(-278,16,556,556);ctx.clip();ctx.drawImage(imgs.earth,-300,-14,610,610);ctx.restore();text('EARTH / NASA VIIRS COMPOSITE',-261,650,20);});ctx.restore();
 ctx.save();ctx.translate(332,680);ctx.scale(1+.26*straight,1+.26*straight);ctx.translate(-332,-680);ctx.save();ctx.translate(328,245);ctx.rotate(-.03);paper(525,756,()=>{});ctx.restore();
 // The original curved silhouette remains as a registration ghost as the foreground image straightens.
 photoSpine(332,385,580,100,0,.22*straight);photoSpine(332+20*micro,385,580,100*(1-straight),84*longer,1);
 let arrow=1-micro;if(arrow>.025){ctx.save();ctx.globalAlpha=arrow;stroke([[333,288],[333,367]],C.yellow,13,1,t,14);stroke([[309,336],[333,367],[357,336]],C.yellow,13,1,t,14);ctx.restore();}ctx.restore();
 title([t<E.micro?'Body weight.':t<E.straighten?'Less loading.':'Straighten.'],t,t<E.micro?E.earth:t<E.straighten?E.micro:E.straighten,{y:199,size:105,highlight:0});
 if(longer>0){ctx.save();ctx.globalAlpha=longer;label('+ LENGTHEN',623,803,42,C.yellow);stroke([[546,385-62*longer],[585,385-62*longer],[585,972],[546,972]],C.yellow,7,longer,t,15);ctx.restore();}
 label('Same photographed model. Different illustrative loading.',97,1570,24);label('Motion exaggerated / not a measured medical image',97,1620,23);sourceCredit(t);ctx.restore();
 if(exit<.1&&straight>.3)focusHere(344,680,280,340,.27*straight,5);}
function investigation(t){let en=arrival(t,E.research-.4,E.research+.12),z=arrival(t,E.ultrasound-.3,E.ultrasound+.95),out=arrival(t,E.fit-.38,E.fit+.15);ctx.save();ctx.translate(-1600*(1-en)-1800*out,0);
 // Two real views of the same NASA source are staged as overlapping research prints.
 imagePlane(imgs.modelDetail,740-45*z,1150+70*z,750,470,.10,null,'PHYSICAL MODEL / JOHN CAMPBELL');
 ctx.save();ctx.translate(475,780);ctx.scale(1+.43*z,1+.43*z);ctx.translate(-475,-780);imagePlane(imgs.ultrasound,540-58*z,420-42*z,1160,775,-.028+.025*z,null,'NASA / ISS036-E-035753');ctx.restore();
 title(['Studied in orbit.'],t,E.research,{y:225,size:101,highlight:0});stroke([[257,1300],[367,1015],[464,887]],C.yellow,7,span(t,E.ultrasound+.1,E.ultrasound+.72),t,16);label('REAL SPINAL ULTRASOUND',127,1398,32,C.yellow);label('Chris Cassidy + Luca Parmitano / ISS, 2013',127,1460,26);ctx.restore();if(en>.9&&out<.08)focusHere(445,820,420,180,.48*z,7);}
function fitting(t){let en=arrival(t,E.fit-.38,E.fit+.15),out=arrival(t,E.return-.42,E.return+.15),z=arrival(t,E.suits-.22,E.suits+.75),drift=span(t,E.fit,E.return);ctx.save();ctx.translate(1650*(1-en),-2200*out);
 imagePlane(imgs.ultrasound,205-75*z,1130+80*drift,1060,640,-.085,null,'NASA / ISS INTERIOR / CREW CONTEXT');
 imagePlane(imgs.hero,704-135*z,416-75*z,1030+95*z,580+55*z,.065-.085*z,null,'NASA / ACTUAL SPACEFLIGHT PHOTOGRAPH');
 // The foreground spacesuit cutout is freed from its print and moves across the printed source planes.

 title(['A changing body.','A fixed fit.'],t,E.fit,{y:209,size:103,highlight:1});
 ctx.save();ctx.translate(580,1415);ctx.rotate(-.04);paper(720,151,()=>{marker(-328,23,655,65,z,t);text('SEATS + SPACESUITS',-311,73,42,C.ink,'left',true);text('NASA NTRS / 20110023150 / editorial summary',-321,130,22);});ctx.restore();ctx.restore();}
function resolution(t){let en=arrival(t,E.return-.42,E.return+.13),recover=arrival(t,E.return+.35,E.return+1.98),resolve=arrival(t,E.resolve,E.resolve+.8),drift=span(t,E.return,38);ctx.save();ctx.translate(0,2200*(1-en));
 earth(755-180*drift,1570+65*drift,1820+170*drift,-.04+.08*drift);
 // Return to the photographic subject; comparison shrinks toward the registered normal state.
 astro(552-55*drift,772-30*drift,950+90*drift,.04-.10*drift,.09*(1-recover));
 ctx.save();ctx.translate(875,1270);ctx.rotate(.055);paper(280,344,()=>{photoSpine(0,24,224,36*(1-recover),18*(1-recover));text('NORMAL HEIGHT',-116,300,25);});ctx.restore();
 title(t<E.resolve?['Back on Earth,','back to normal.']:['The extra height','is temporary.'],t,t<E.resolve?E.return:E.resolve,{y:216,size:101,highlight:1});
 label('Illustrative height change / NASA photograph',111,1580,23);if(resolve>.2)label('TEMPORARY CHANGE. SAME ASTRONAUT.',111,1648,32,C.yellow);ctx.restore();}
function captions(t){let cap=DATA.timing.captions.find(a=>t>=a.start&&t<=a.end);if(!cap)return;ctx.save();let size=42;ctx.font=`700 ${size}px Manrope`;while(ctx.measureText(cap.text).width>906&&size>36){size--;ctx.font=`700 ${size}px Manrope`;}let w=ctx.measureText(cap.text).width+56;ctx.fillStyle='#0d1c2bee';ctx.beginPath();ctx.roundRect((W-w)/2,1021,w,91,13);ctx.fill();ctx.strokeStyle='#c8a26b88';ctx.lineWidth=1.3;ctx.stroke();ctx.fillStyle=C.paper;ctx.textAlign='center';ctx.fillText(cap.text,540,1081);ctx.restore();}

function renderScene(t){desk();if(t<E.evidence+.18)intro(t);if(t>=E.evidence-.42&&t<E.anatomy+.14)evidence(t);if(t>=E.anatomy-.43&&t<E.earth)anatomy(t);if(t>=E.earth&&t<E.research+.12)loadDiagram(t);if(t>=E.research-.4&&t<E.fit+.15)investigation(t);if(t>=E.fit-.38&&t<E.return+.15)fitting(t);if(t>=E.return-.42)resolution(t);}
function furniture(t){}
function episodeOptics(t){let hunt=0;for(const a of [.48,E.anatomy+.35,E.ultrasound-.20])hunt=Math.max(hunt,CurioMotion.hunt(t,{start:a,duration:.37,radii:[0,2.6,4.2,0]}));return {blurPx:hunt,fringePx:.58+.22*Math.sin(t*.9),cx:540,cy:720};}
function episodeMotionState(t){return {episode:'astronaut-height-r2',time:t,stage:t<E.evidence?'photo-parallax-closeup':t<E.anatomy?'photo-stature-comparison':t<E.research?'animated-physical-spine-photograph':t<E.fit?'actual-ultrasound':t<E.return?'spacesuit-photo-stack':'photographic-return',height_explanation:'Explicitly labeled illustrative warp of sourced photography',captions:'screen fixed'};}
