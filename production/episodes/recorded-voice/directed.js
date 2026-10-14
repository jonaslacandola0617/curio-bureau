// Reconstructed from the saved editorial plan. Actual sourced photography carries the argument.
let micMatte;
function microphone(x,y,w,rotation=0){
 if(!micMatte){let c=document.createElement('canvas');c.width=1876;c.height=640;let q=c.getContext('2d');q.drawImage(imgs.mic,1900,775,1876,640,0,0,1876,640);let d=q.getImageData(0,0,c.width,c.height),p=d.data,seen=new Uint8Array(c.width*c.height),queue=new Int32Array(c.width*c.height),head=0,tail=0;
 const add=i=>{if(i<0||i>=seen.length||seen[i])return;seen[i]=1;if((p[i*4]*.2126+p[i*4+1]*.7152+p[i*4+2]*.0722)>=165){queue[tail++]=i;p[i*4+3]=0;}};
 for(let j=0;j<c.width;j++){add(j);add((c.height-1)*c.width+j);}for(let j=0;j<c.height;j++){add(j*c.width);add(j*c.width+c.width-1);}while(head<tail){let i=queue[head++],x=i%c.width;add(i-c.width);add(i+c.width);if(x)add(i-1);if(x<c.width-1)add(i+1);}q.putImageData(d,0,0);micMatte=c;
 }
 ctx.save();ctx.translate(x,y);ctx.rotate(rotation);ctx.shadowColor='#000a';ctx.shadowBlur=22;ctx.shadowOffsetY=16;ctx.drawImage(micMatte,-w/2,-w*micMatte.height/micMatte.width/2,w,w*micMatte.height/micMatte.width);ctx.restore();
}
function tag(s,x,y,size=28,color=C.paper){ctx.save();ctx.font=`700 ${size}px Manrope`;let w=ctx.measureText(s).width+34;ctx.fillStyle='#0d1c2be8';ctx.fillRect(x-17,y-size-9,w,size+24);text(s,x,y,size,color);ctx.restore();}
function earPrint(x,y,w,h,r=0){photograph(imgs.ear,x,y,w,h,r,'Travis Isaacs / CC BY 2.0');}
function skullPrint(x,y,w,h,r=0){photograph(imgs.skull,x,y,w,h,r,'John Campbell / CC BY 2.0 / teaching model');}
function modelPrint(x,y,w,h,r=0){photograph(imgs.earModel,x,y,w,h,r,'Science Museum / Wellcome / CC BY 4.0 / ear model');}
function selection(x,y,rx,ry,strength){sq.setTransform(1,0,0,1,0,0);sq.drawImage(canvas,0,0);focus.apply(scene,fq,{cx:x,cy:y,rx,ry,strength,maxBlur:7,feather:1.05,outsideGain:.46});ctx.save();ctx.setTransform(1,0,0,1,0,0);ctx.beginPath();ctx.rect(0,350*RENDER_SCALE,canvas.width,1150*RENDER_SCALE);ctx.clip();ctx.drawImage(focused,0,0);ctx.restore();}
function hook(t){let out=arrival(t,E.routes-.4,E.routes+.18),push=arrival(t,.48,2.04),drift=span(t,2,E.routes);ctx.save();ctx.translate(-2250*out,0);
 earPrint(540+155*push,480-130*push,1140+110*push,820,.06-.035*push);
 microphone(550-180*push,1280+120*push,1020+1250*push,-.19+.20*push);
 ctx.save();ctx.globalAlpha=1-span(t,1.05,1.65);ctx.translate(-70*push,-240*push);title(['Why does your voice','sound different?'],t,0,{y:212,size:99,highlight:1});ctx.restore();
 if(t>1.7){let u=arrival(t,1.7,2.1);ctx.save();ctx.globalAlpha=u;tag('ON A RECORDING.',160,380,47,C.yellow);ctx.restore();}
 tag('Airborne microphone / Anonimski / CC0',90,1675,22);ctx.restore();}
function routes(t){let en=arrival(t,E.routes-.4,E.routes+.18),out=arrival(t,E.air-.35,E.air+.14),u=arrival(t,E.routes+.20,E.routes+1.1);ctx.save();ctx.translate(1900*(1-en),-2200*out);
 earPrint(395-145*u,415+50*u,980,645,-.08);skullPrint(730+65*u,1170-80*u,760,515,.08-.04*u);
 title(['Two routes.'],t,E.routes,{y:239,size:142,highlight:0});
 tag('AIR',112,1190,45,C.yellow);tag('BODY',637,1240,45,'#ef7962');
 stroke([[360,850],[360,1180],[180,1180]],C.yellow,8,span(t,E.routes+.55,E.routes+1.18),t,22);
 tag('Photographs + conceptual paths',103,1750,22);ctx.restore();}
function airRoute(t){let en=arrival(t,E.air-.35,E.air+.14),z=arrival(t,E.air+.12,E.air+.90),out=arrival(t,E.body-.35,E.body+.15);ctx.save();ctx.translate(-1900*(1-en)-2100*out,0);
 ctx.save();ctx.translate(555,740);ctx.scale(1+.27*z,1+.27*z);ctx.translate(-555,-740);earPrint(500,390-70*z,1190,890,-.04+.04*z);stroke([[110,820],[250,787],[390,748],[570,740]],C.yellow,12,span(t,E.air+.12,E.air+.95),t,23);ctx.restore();
 title(['Through the air.'],t,E.air,{y:236,size:113,highlight:0});tag('TO YOUR EARS',110,1410,41,C.yellow);tag('Normal hearing continues through the ear structures.',103,1610,25);ctx.restore();}
function bodyRoute(t){let en=arrival(t,E.body-.35,E.body+.15),z=arrival(t,E.body+.25,E.body+1.15),inspect=arrival(t,E.extra-.1,E.extra+.8),out=arrival(t,E.mic-.4,E.mic+.16);ctx.save();ctx.translate(1700*(1-en),-2300*out);
 skullPrint(355-100*z,420-40*z,1000+70*z,700,-.06);modelPrint(720-100*inspect,1120-100*inspect,795+120*inspect,640,.09-.08*inspect);
 title(t<E.extra?['Through your body.']:['An extra route.'],t,t<E.extra?E.body:E.extra,{y:243,size:110,highlight:0});
 let u=span(t,E.body+.4,E.body+1.8);stroke([[445,805],[535,920],[684,1180],[707,1320]],'#EF7962',10,u,t,24);
 if(u>.3){ctx.save();ctx.globalAlpha=.2+.15*Math.sin(t*4);ctx.strokeStyle='#FFDA12';ctx.lineWidth=6;for(let i=0;i<3;i++){ctx.beginPath();ctx.ellipse(450,720,95+i*35+10*Math.sin(t*3),135+i*35,0,0,Math.PI*2);ctx.stroke();}ctx.restore();}
 tag('SKULL + OTHER TISSUES',98,1540,32,'#ef7962');tag('Teaching models / illustrative vibration paths',98,1695,23);ctx.restore();if(en>.98&&out<.03&&t>E.extra)selection(650,1340,375,260,.36*inspect);}
function micRoute(t){let en=arrival(t,E.mic-.4,E.mic+.16),z=arrival(t,E.mic+.25,E.mic+1.02),no=arrival(t,E.mic+2,E.mic+2.5),out=arrival(t,E.playback-.4,E.playback+.15);ctx.save();ctx.translate(-1750*(1-en)-2300*out,0);
 earPrint(750+190*z,1130,920,600,.09);microphone(430-80*z,650,1110+360*z,-.06+.08*z);
 title(['The microphone','captures air.'],t,E.mic,{y:218,size:108,highlight:1});stroke([[105,847],[270,803],[412,782]],C.yellow,10,span(t,E.mic+.5,E.mic+1.15),t,26);tag('AIR',100,927,42,C.yellow);
 if(no>.01){ctx.save();ctx.globalAlpha=no;tag('NOT THE INTERNAL VIBRATIONS',104,1450,33,'#ef7962');ctx.restore();}tag('Microphone photo / Anonimski / CC0',100,1685,22);ctx.restore();}
function playback(t){let en=arrival(t,E.playback-.4,E.playback+.15),out=arrival(t,E.resolve-.4,E.resolve+.15),u=arrival(t,E.playback+.3,E.playback+1.1);ctx.save();ctx.translate(1850*(1-en),-2300*out);
 modelPrint(770+50*u,1150,720,620,.075);microphone(430-50*u,625,1260,-.03);
 ctx.save();ctx.translate(500,1240);ctx.rotate(-.045);paper(900,263,()=>{text('RECORDED NARRATION / ACTUAL SIGNAL',-406,57,22);let a=DATA.waveform;stroke(a.map((v,i)=>[-405+i*810/(a.length-1),157+v*50]),C.ink,3,1,t,33);});ctx.restore();
 title(t<E.conditions?['Playback leaves','something out.']:['The mic + room','change it, too.'],t,t<E.conditions?E.playback:E.conditions,{y:220,size:105,highlight:1});
 tag('Waveform is this narration, not a bone-conduction measurement.',95,1650,22);ctx.restore();if(en>.99&&out<.03)selection(455,670,420,220,.30*u);}
function resolution(t){let en=arrival(t,E.resolve-.4,E.resolve+.15),z=arrival(t,E.resolve+.4,E.resolve+1.5);ctx.save();ctx.translate(0,2150*(1-en));
 earPrint(430+65*z,426-80*z,1210,820,-.04+.04*z);microphone(610-180*z,1350+80*z,1170+180*z,.1-.18*z);
 title(['Both are you.'],t,E.resolve,{y:234,size:129,highlight:0});if(t>E.resolve+1.5){ctx.save();ctx.globalAlpha=arrival(t,E.resolve+1.5,E.resolve+1.95);tag('DIFFERENT ROUTES.',143,1540,49,C.yellow);ctx.restore();}tag('Same voice. Different listening experience.',110,1695,26);ctx.restore();}
function renderScene(t){desk();if(t<E.routes+.18)hook(t);if(t>=E.routes-.4&&t<E.air+.14)routes(t);if(t>=E.air-.35&&t<E.body+.15)airRoute(t);if(t>=E.body-.35&&t<E.mic+.16)bodyRoute(t);if(t>=E.mic-.4&&t<E.playback+.15)micRoute(t);if(t>=E.playback-.4&&t<E.resolve+.15)playback(t);if(t>=E.resolve-.4)resolution(t);}
function furniture(t){}
function episodeOptics(t){let hunt=0;for(let a of [.42,E.body+.24,E.mic+.18])hunt=Math.max(hunt,CurioMotion.hunt(t,{start:a,duration:.34,radii:[0,2.2,3.6,0]}));return {blurPx:hunt,fringePx:.55+.12*Math.sin(t*.8),cx:540,cy:750};}
function episodeMotionState(t){return {episode:'recorded-voice-rebuild-r2',time:t,images:'Sourced photography',conceptual:'Paths/pulses not measured vibrations',captions:'screen fixed'};}
