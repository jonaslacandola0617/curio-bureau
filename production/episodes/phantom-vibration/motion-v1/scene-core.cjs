/* Original Phantom Vibration art. Static review only; no motion approval. */
const fs=require('fs'),path=require('path'),crypto=require('crypto');
const {createCanvas,loadImage,GlobalFonts}=require(process.env.CODEX_PRIMARY_RUNTIME_NODE_MODULES+'/@napi-rs/canvas');
const root=path.resolve(__dirname,'../art-v1');
for(const [file,name] of [['Playfair900.ttf','Playfair Display'],['Manrope800.ttf','Manrope']])if(!GlobalFonts.registerFromPath(path.join(root,'assets',file),name))throw Error('Font registration failed: '+file);
const TL=require('./timeline.json');const W=1080,H=1920,C={ink:'#0D1C2B',ivory:'#F5F0E7',yellow:'#FFE34A',coral:'#F17A61',blue:'#A8C9D8'};
let q,imgs,hidden=false,T=0,age=0,scene=0,duration=1,headings=[],anchors={},stageStart=0,overlayPass=false,buildingMaterial=false; const E=x=>{x=Math.max(0,Math.min(1,x));return 1-Math.pow(1-x,3)},S=x=>{x=Math.max(0,Math.min(1,x));return x*x*(3-2*x)};
function tx(s,x,y,size=32,color=C.ivory,font='Manrope',align='left'){if(!overlayPass)return;q.save();q.fillStyle=color;q.font=`${font==='Manrope'?800:900} ${size}px "${font}"`;q.textAlign=align;q.fillText(s,x,y);q.restore()}
function title(lines,y=235,size=100,color=C.ivory){headings.push({lines,y,size,color,at:stageStart});}
function rule(x,y,x2,y2,color=C.yellow,width=4){if(!overlayPass&&!buildingMaterial)return;q.save();q.strokeStyle=color;q.lineWidth=width;q.beginPath();q.moveTo(x,y);q.lineTo(x2,y2);q.stroke();q.restore()}
function baseLabel(s,x,y,w,color=C.yellow){q.fillStyle=color;q.fillRect(x,y,w,55);tx(s,x+18,y+37,25,C.ink)}
function rng(seed){return()=>{seed=(Math.imul(seed,1664525)+1013904223)>>>0;return seed/4294967296}}
function baseMaterial(dark=true){q.fillStyle=dark?C.ink:C.ivory;q.fillRect(0,0,W,H);let r=rng(91273);q.save();q.globalAlpha=dark?.12:.075;for(let i=0;i<18000;i++){let v=r()>.5?255:0;q.fillStyle=`rgb(${v},${v},${v})`;q.fillRect(r()*W,r()*H,1+r()*2,1+r()*2)}q.globalAlpha=.06;for(let i=0;i<420;i++){let x=r()*W,y=r()*H;rule(x,y,x+r()*33,y+(r()-.5)*4,dark?'#d0c5a7':'#535751',.7)}q.restore()}
function basePhoto(name,x,y,w){if(overlayPass)return;let im=imgs[name];q.drawImage(im,x,y,w,w*im.height/im.width)}
function basePocketMacro(x,y,w,h){if(overlayPass)return;q.save();q.beginPath();q.rect(x,y,w,h);q.clip();q.drawImage(imgs.hip,205,390,530,273,x,y,w,h);q.restore()}
function baseTarget(x,y,r=54){q.save();q.lineWidth=5;q.strokeStyle=C.yellow;q.beginPath();q.arc(x,y,r,-.32,Math.PI*1.66);q.stroke();q.restore()}
function baseSensation(x,y){for(let i=0;i<3;i++){q.save();q.lineWidth=5;q.strokeStyle=C.yellow;q.beginPath();q.arc(x,y,54+i*19,-.6,.6);q.stroke();q.restore()}}
function cap(){}
function folio(dark=true){let color=dark?C.blue:C.ink;tx('CURIO BUREAU',72,78,23,color);tx('PHANTOM VIBRATION',1008,78,21,color,'Manrope','right');rule(72,108,1008,108,color,1);tx('ORIGINAL PHOTOGRAPHIC ILLUSTRATION',72,1800,20,color);tx('Research: Rothberg et al. / BMJ / 2010',72,1840,20,color)}
function grain(){}
function hook(){material();photo('hip',-5,640,1090);title(['You felt it.'],250,116);label('YOUR PHONE DIDN’T.',72,328,435);sensation(640,1150);tx('FELT BUZZ',710,1080,27,C.yellow);rule(720,1100,696,1138);grain();cap(['You felt your phone vibrate.']);}
function check(){material(false);photo('phone',0,325,1080);title(['You check.','Nothing.'],235,105,C.ink);let sx=367,sy=590;attachedText('NO NEW',555,sy+80,37,C.ivory);attachedText('NOTIFICATIONS',555,sy+133,30,C.ivory);attachedText('Illustrative screen',555,sy+195,21,C.blue);grain();cap(['Sometimes, the phone','never vibrated at all.']);tx('An empty screen alone does not prove a phantom vibration.',72,1732,23,C.ink);}
function name(){material();photo('hip',-195,700,1040);photo('phone',648,1130,405);title(['Phantom','vibration.'],240,114);label('FELT',74,1190,150);label('DEVICE STILL',628,1530,315);grain();cap(['A phantom vibration.']);}
function mechanism(stage){material();title(stage===0?['Start with','a sensation.']:stage===1?['What might','you expect?']:['A familiar','interpretation.'],235,99);label('PROPOSED EXPLANATION',72,405,595);pocketMacro(-90,555,1260,650);if(!overlayPass){q.fillStyle=C.ink;q.fillRect(0,1210,1080,590);}target(905,780,70);label(stage===2?'PHONE BUZZ?':'CLOTHING PRESSURE?',72,1250,stage===2?365:530);tx(stage===0?'Possible input, not an established cause.':stage===1?'Expectation may shape the interpretation.':'Same candidate sensation. Different interpretation.',72,1400,29,C.ivory);if(stage>0){rule(103,1480,967,1480,C.blue,3);tx('AMBIGUOUS CUE',72,1550,29,C.blue);tx(stage===2?'“PHONE?”':'EXPECTATION',1008,1640,45,C.yellow,'Manrope','right')}grain();cap(stage===0?['One proposed explanation','starts with what you expect.']:stage===1?['Your brain may interpret','another sensation as a buzz.']:['Clothing pressure is','one possible candidate.']);}
function evidence(){material(false);title(['Reported.','Not explained.'],235,106,C.ink);label('ONE SURVEY / MEDICAL STAFF / 2010',72,435,870);tx('115',72,735,245,C.ink,'Playfair Display');tx('of 169',610,730,100,C.ink,'Playfair Display');tx('reported phantom vibrations',72,825,49,C.ink);rule(72,1125,1008,1125,C.ink,3);tx('WHAT THIS STUDY COUNTED',72,1195,29,C.ink);tx('Self-reported experiences.',72,1270,45,C.ink,'Playfair Display');tx('WHAT IT DID NOT ESTABLISH',72,1400,29,C.ink);tx('The cause.',72,1485,87,C.ink,'Playfair Display');tx('One institution. Not a population-wide prevalence estimate.',72,1620,25,C.ink);tx('ORIGINAL SUMMARY / NO ARTICLE IMAGE REPRODUCED',72,1685,21,C.ink);grain();cap(['Surveys document the experience;','they don’t prove that mechanism.'],false);}
function payoff(){material();photo('hip',-5,680,1090);title(['A real feeling.','An absent alert.'],235,99);label('FELT',72,1080,145);sensation(640,1190);label('DEVICE STILL',655,1360,320);grain();cap(['The sensation can feel real','even when the alert wasn’t.']);}
const names=['01_hook','02_check','03_name','04_candidate','05_interpretation','06_evidence','07_payoff'];
const draw=[hook,check,name,()=>{let a=TL.events.expect-TL.scenes[3].start,b=TL.events.buzz-TL.scenes[3].start;stageStart=age<a?0:age<b?a:b;mechanism(age<a?0:age<b?1:2)},()=>mechanism(2),evidence,payoff];

const mats=new Map();
function material(dark=true){if(overlayPass)return;if(!mats.has(dark)){buildingMaterial=true;let old=q,c=createCanvas(W,H);q=c.getContext('2d');baseMaterial(dark);buildingMaterial=false;q=old;mats.set(dark,c)}q.drawImage(mats.get(dark),0,0)}
function photo(name,x,y,w){let p=E(age/.85),push=S((age-1)/Math.max(1,duration-1)),dx=0,dy=0,z=1;
 if(scene===0){dy=70*(1-p)-30*push;dx=-65*(1-p);z=.98+.02*p+.08*push}
 if(scene===1){dy=50*(1-p);z=.96+.04*p+.045*push}
 if(scene===2){dx=(name==='hip'?-140:200)*(1-p);dy=(name==='hip'?60:100)*(1-p);z=.97+.03*p}
 if(scene===6){dy=60*(1-p)-25*push;dx=-35*(1-p);z=1+.035*push}
 const cx=x+w/2,cy=y+w*imgs[name].height/imgs[name].width/2;anchors[name]={cx,cy,z,dx,dy};q.save();q.translate(cx+dx,cy+dy);q.scale(z,z);basePhoto(name,-w/2,-w*imgs[name].height/imgs[name].width/2,w);q.restore();
}
function at(x,y,name='hip'){const a=anchors[name];return a?[a.cx+(x-a.cx)*a.z+a.dx,a.cy+(y-a.cy)*a.z+a.dy]:[x,y]}
function pocketMacro(x,y,w,h){const p=E(age/.65),z=1+.04*S(age/Math.max(1,duration)),dx=-35*(1-p),dy=22*(1-p);anchors.macro={cx:540,cy:y+h/2,z,dx,dy};q.save();q.translate(540+dx,y+h/2+dy);q.scale(z,z);basePocketMacro(x-540,-h/2,w,h);q.restore()}
function target(x,y,r=54){if(!overlayPass)return;const a=at(x,y,'macro'),p=E((age-.35)/.65);if(!p)return;q.save();q.lineWidth=4+.25*Math.sin(Math.floor(T*12)*1.7);q.strokeStyle=C.yellow;q.beginPath();q.arc(a[0],a[1],r,-.32,-.32+Math.PI*1.85*p);q.stroke();q.restore()}
function sensation(x,y){if(!overlayPass)return;const a=at(x,y),p=E((age-.22)/.35);q.save();q.globalAlpha=p*(.82+.18*Math.sin(age*5));baseSensation(a[0],a[1]);q.restore()}
function attachedText(s,x,y,size,color){const a=at(x,y,'phone');tx(s,a[0],a[1],size*(anchors.phone?.z||1),color,'Manrope','center')}
function label(s,x,y,w,color=C.yellow){if(!overlayPass)return;let start=stageStart+.12;if(s.includes('PROPOSED'))start=0;if(s==='DEVICE STILL')start=.5;const p=E((age-start)/.4);if(!p)return;q.save();q.beginPath();q.rect(x-4,y-4,(w+8)*p,65);q.clip();baseLabel(s,x,y+16*(1-p),w,color);q.restore()}
async function setup(){imgs={};for(const n of ['hip','phone'])imgs[n]=await loadImage(path.join(root,'assets',n+'.png'))}
function render(context,t,index,local,dur){q=context;overlayPass=false;T=t;scene=index;age=local;duration=dur;headings=[];anchors={};stageStart=0;draw[index]();}
function overlay(context,t){q=context;overlayPass=true;headings=[];anchors={};stageStart=0;draw[scene]();for(const h of headings){h.lines.forEach((s,i)=>{let p=E((age-h.at-.04-i*.065)/.48);q.save();q.globalAlpha=p;tx(s,72,h.y+i*h.size*1.08+45*(1-p),h.size,h.color,'Playfair Display');q.restore()})}folio(scene!==1&&scene!==5)}
module.exports={setup,render,overlay};
