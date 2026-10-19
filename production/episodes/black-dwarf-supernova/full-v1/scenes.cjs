// Executed in the approved compositor's VM. Reuse materials, optics and fonts.
const FULL=require('../full-v1/timeline.json'),approved=require('./render.cjs');
const retainedSetup=setup;let obs,fullCaptionBox=null,fullOut;
async function fullSetup(){await retainedSetup();await approved.setup();obs=await loadImage(path.join(A,'sirius-hubble.jpg'));fullOut=createCanvas(W,H)}
const oldState=state;
function fullState(t){let joins=[8,14.5,44.1666666667],near=Math.min(...joins.map(x=>Math.abs(t-x)));return{focusY:t<8?1260:t<14.5?730:t<19?640:1360,hunt:1.7*Math.exp(-(((t-9.66)/.14)**2)),transition:Math.exp(-((near/.1)**2))}}
state=fullState;
function fullPlate(t){q=source.getContext('2d');q.setTransform(1,0,0,1,0,0);q.clearRect(0,0,W,H);q.drawImage(bg,0,0);
 if(t<8){let pull=S((t-3.2)/.6),r=L(420,360,pull)*(1-.014*S((t-1.6)/.7)),x=540+16*S((t-.1)/.8);specimen(x,L(1280,1320,pull),r,t);}
 else if(t<14.5){q.drawImage(paper,0,0,W,H);let enter=E((t-8)/.55);q.save();q.translate(-440*(1-enter),0);q.fillStyle=C.ink;q.fillRect(70,457,405,439);q.drawImage(obs,88,475,369,403);q.restore();let u=E((t-12.8)/.5);specimen(L(850,790,u),1390,L(175,204,u),t)}
 else if(t<19){let u=E((t-14.5)/.55);specimen(540,L(1390,610,u),L(204,245,u),t);q.save();q.beginPath();q.moveTo(540,610);q.arc(540,610,245,-Math.PI*.44*u,Math.PI*.44*u);q.closePath();q.clip();q.drawImage(paper,540,365,245,490);q.restore();q.drawImage(paper,70,1120,940,530)}
 else {let contraction=S((t-53.8)/.8);specimen(540,1360,270*(1-.12*contraction),t)}
}
function fullTitle(lines,y=235,size=104,col=C.ivory){for(let i=0;i<lines.length;i++)tx(lines[i],70,y+i*110,size,col,'Playfair Display')}
function chipFull(s,x,y,col=C.yellow,size=24,progress=1){q.save();q.font='800 '+size+'px Manrope';let w=q.measureText(s).width+28;q.beginPath();q.rect(x,y-size-9,w*progress,size+23);q.clip();q.fillStyle=col;q.fillRect(x,y-size-9,w,size+23);tx(s,x+14,y,size,C.ink);q.restore()}
function capFull(t,enabled){fullCaptionBox=null;if(!enabled)return;const c=FULL.captions.find(c=>t>=c.start&&t<c.end);if(!c)return;let lines=[''];q.font='800 43px Manrope';for(const word of c.text.split(' ')){let i=lines.length-1,s=(lines[i]+' '+word).trim();if(q.measureText(s).width>790&&lines[i])lines.push(word);else lines[i]=s}let w=Math.max(...lines.map(x=>q.measureText(x).width))+28,y=918,h=lines.length*54+10;q.fillStyle=C.ink;q.fillRect(540-w/2,y-43,w,h);lines.forEach((s,i)=>tx(s,540,y+i*54,43,C.ivory,'Manrope','center'));fullCaptionBox={x:Math.floor(540-w/2),y:y-43,w:Math.ceil(w),h}}
function footerFull(lines,col=C.blue){lines.forEach((s,i)=>tx(s,70,1777+i*34,21,col))}
function fullOverlays(t){q=out.getContext('2d');const light=t>=8&&t<14.5,col=light?C.ink:C.blue;tx('CURIO BUREAU',70,76,22,col);tx('BLACK DWARF / THEORETICAL FUTURE',1010,76,19,col,'Manrope','right');line(70,107,1010,107,col,1);
 if(t<8){fullTitle(['Dead.','Still unfinished.']);chipFull('A POSSIBLE FUTURE',70,610);if(t>=1.6&&t<3.2){let p=E((t-1.6)/.5);arrow(100,1280,L(100,170,p),1280,C.coral,5);arrow(990,1280,L(990,920,p),1280,C.coral,5)}
 if(t>=3.2)chipFull('UNFINISHED',70,750,C.coral,27,E((t-3.2)/.45));
 if(t>=4.8){let u=E((t-4.8)/.5);line(90,1100,90+275*u,1100,C.yellow,4,[10,7]);tx('MASS ≈ FIXED',90,1060,24,C.yellow)}
 if(t>=6.4){let u=E((t-6.4)/.6);inkStroke(715,1040+95*u,970,1040+95*u,t);tx('LIMIT ↓',760,1195,25,C.coral)}
 footerFull(['Hypothetical black dwarf • AI artist illustration','Surface, illumination and inward marks are illustrative.','Caplan (2020) • conditional far-future model'])}
 else if(t<14.5){fullTitle(['A real remnant.','A hypothetical future.'],233,83,C.ink);chipFull('OBSERVATION',70,428,C.blue);if(t>=9.6){let u=E((t-9.6)/.45);ring(192,774,21,C.yellow,3);if(t>=11.2){line(192,774,L(192,540,E((t-11.2)/.45)),L(774,700,E((t-11.2)/.45)),C.ink,2)}tx('Sirius B',550,685,48,C.ink,'Playfair Display');tx('WHITE DWARF',550,735,25,C.ink);tx('The faint point,',550,800,27,C.ink);tx('not its bright companion.',550,841,25,C.ink)}
 line(70,1055,1010,1055,C.ink,2);tx('NO OBSERVED',70,1190,25,C.ink);tx('BLACK DWARFS',70,1230,25,C.ink);if(t>=12.8){chipFull('HYPOTHETICAL FUTURE',70,1415,C.yellow,22,E((t-12.8)/.4));tx('The future state',70,1350,48,C.ink,'Playfair Display');tx('must be illustrated.',70,1490,40,C.ink,'Playfair Display')}
 tx('Sirius B establishes the remnant class;',70,1585,26,C.ink);tx('it is not the model’s exploding example.',70,1627,26,C.ink);footerFull(['NASA, ESA, H. Bond (STScI), and M. Barstow (University of Leicester)','Hubble heic0516a • CC BY 4.0 • native 369 × 403 source','Lower remnant: AI artist illustration, not the observed star.'],C.ink)}
 else if(t<19){fullTitle(['Held up','from within.'],232,109);ring(540,610,245,C.blue,2);let u=E((t-16)/.55);arrow(150,610,150+130*u,610,C.coral);arrow(930,610,930-125*u,610,C.coral);arrow(550,610,550+146*u,610,C.yellow);tx('GRAVITY',70,765,24,C.coral);tx('ELECTRON PRESSURE',600,865,22,C.yellow);tx('A CHANGE IN COMPOSITION',105,1185,25,C.ink);if(t>=17.6){let p=E((t-17.6)/.55);for(let row=0;row<5;row++)for(let col=0;col<Math.ceil(9*p);col++)ring(140+col*90+(row%2)*18,1250+row*63,13,'#74889B',3);tx('The support comes from within.',105,1596,39,C.ink,'Playfair Display')}
 footerFull(['Conceptual cutaway and printed figure • not a measured interior','Pressure from electrons resists inward gravity.','Caplan (2020) • no numerical scale or simulation'])}
 else {fullTitle(['One more','possible ending.']);
 let notation=E((t-45.8)/.45);q.save();q.globalAlpha=notation;tx('10',65,675,235,C.ivory,'Playfair Display');q.restore();if(t>=47.4){let u=E((t-47.4)/.45);q.save();q.beginPath();q.rect(330,420,330*u,150);q.clip();tx('1100',333,532,92,C.yellow,'Playfair Display');q.restore();tx('YEARS — EARLIEST MODEL ESTIMATE',75,746,25,C.blue)}
 if(t>=49)chipFull('IF PROTONS SURVIVE',70,1115,C.coral,25,E((t-49)/.5));if(t>=50.6){let u=E((t-50.6)/.45);line(70,1160,70+520*u,1160,C.coral,3)}
 if(t>=52.2){let p=E((t-52.2)/.45),r=270*(1-.12*S((t-53.8)/.8));for(let a of[0,Math.PI*.5,Math.PI,Math.PI*1.5])arrow(540+350*Math.cos(a),1360+350*Math.sin(a),540+L(350,r+22,p)*Math.cos(a),1360+L(350,r+22,p)*Math.sin(a),C.coral,5)}
 if(t>=55.4)chipFull('ONE POSSIBLE ENDING',70,1660,C.yellow,24,E((t-55.4)/.45));footerFull(['Hypothesis, not a forecast • proton stability is required','Illustrative inward marks • detailed transient remains uncertain','Caplan (2020) • no black-hole outcome asserted.'])}
}
function fullRenderAt(time,{finish=true,captions=true,ending=true,grainTime=null}={}){let t=Math.floor((time+1e-8)*12)/12,o=fullOut.getContext('2d');o.setTransform(1,0,0,1,0,0);o.clearRect(0,0,W,H);
 if(t>=19&&t<FULL.mechanism_end){let c=approved.renderAt(t-19,{finish,captions,grainTime:grainTime===null?null:grainTime-19});o.drawImage(c,0,0);fullCaptionBox=approved.getCaptionBox()}
 else{fullPlate(t);finishing(t,finish,grainTime===null?t:grainTime);fullOverlays(t);capFull(t,captions);o.drawImage(out,0,0)}
 if(ending)CurioBrand.drawEndcard(o,time,FULL.duration);return fullOut}
module.exports={setup:fullSetup,renderAt:fullRenderAt,state:fullState,getCaptionBox:()=>fullCaptionBox,drawEndcard:CurioBrand.drawEndcard};
