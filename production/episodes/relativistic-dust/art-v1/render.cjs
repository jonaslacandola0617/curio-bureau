'use strict';
const fs=require('fs'),path=require('path'),crypto=require('crypto');
const {createCanvas,loadImage,GlobalFonts}=require('@napi-rs/canvas');
const R=__dirname,O=path.join(R,'rendered'),W=1080,H=1920;
fs.mkdirSync(O,{recursive:true});
const F=path.join(R,'../../black-dwarf-supernova/art-v1/assets');
for(const [f,n] of [['Playfair900.ttf','Playfair Display'],['Manrope800.ttf','Manrope']])if(!GlobalFonts.registerFromPath(path.join(F,f),n))throw Error('Font failed: '+f);
const C={navy:'#0D1C2B',ivory:'#F5F0E7',yellow:'#F5CF54',coral:'#D57864',blue:'#A9C9D4',muted:'#8B9EA9'};
let q,atlas,hidden=false,current='';const boxes=[];
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
function txt(s,x,y,size=30,col=C.ivory,f='Manrope',align='left',max=940){
 q.save();function ft(){q.font=(f==='Manrope'?800:900)+' '+size+'px "'+f+'"'}ft();
 while(q.measureText(s).width>max&&size>16){size--;ft()}
 q.fillStyle=col;q.textAlign=align;q.fillText(s,x,y);
 boxes.push({frame:current,text:s,x,y,size,width:q.measureText(s).width,align});q.restore();
}
function line(x,y,X,Y,col=C.muted,w=2,dash=[]){q.save();q.strokeStyle=col;q.lineWidth=w;q.setLineDash(dash);q.beginPath();q.moveTo(x,y);q.lineTo(X,Y);q.stroke();q.restore()}
function arrow(x,y,X,Y,col=C.yellow,w=5){line(x,y,X,Y,col,w);const a=Math.atan2(Y-y,X-x);line(X,Y,X-18*Math.cos(a-.5),Y-18*Math.sin(a-.5),col,w);line(X,Y,X-18*Math.cos(a+.5),Y-18*Math.sin(a+.5),col,w)}
function circle(x,y,r,col=C.muted,w=2){q.save();q.strokeStyle=col;q.lineWidth=w;q.beginPath();q.arc(x,y,r,0,Math.PI*2);q.stroke();q.restore()}
function rect(x,y,w,h,col){q.fillStyle=col;q.fillRect(x,y,w,h)}
function grain(x,y,size){const cw=atlas.width/2,ch=atlas.height/2;q.save();q.beginPath();q.arc(x+size/2,y+size/2,size/2,0,Math.PI*2);q.clip();q.drawImage(atlas,0,0,cw,ch,x,y,size,size);q.restore()}
function surface(kind,x=240,y=1130,size=600){const cw=atlas.width/2,ch=atlas.height/2,cell=kind==='intact'?[1,0]:kind==='contact'?[0,1]:[1,1];if(size>cw||size>ch)throw Error('Image crop enlarged beyond native cell');q.drawImage(atlas,cell[0]*cw,cell[1]*ch,cw,ch,x,y,size,size)}
function fiber(light=false){let seed=1493;const rnd=()=>((seed=(Math.imul(seed,1664525)+1013904223)>>>0)/4294967296);q.save();q.globalAlpha=light?.09:.045;for(let i=0;i<2600;i++){const x=rnd()*1080,y=rnd()*1920;line(x,y,x+2+rnd()*13,y+(rnd()-.5)*2,light?'#6C6559':C.blue,.55)}q.restore()}
function base(light=false){rect(0,0,W,H,light?C.ivory:C.navy);fiber(light);const col=light?C.navy:C.blue;txt('CURIO BUREAU',70,76,23,col);txt('RELATIVISTIC DUST',1010,76,20,col,'Manrope','right',470);line(70,108,1010,108,col,1)}
function heading(lines,light=false){if(hidden)return;lines.forEach((s,i)=>txt(s,70,235+i*112,106,light?C.navy:C.ivory,'Playfair Display'))}
function cap(lines,light=false){if(hidden)return;lines.forEach((s,i)=>txt(s,540,927+i*57,43,light?C.navy:C.ivory,'Manrope','center',940))}
function footer(lines,light=false){const col=light?C.navy:C.blue;lines.forEach((s,i)=>txt(s,70,1775+i*32,21,col));txt('STATIC ART REVIEW / DRAFT CAPTIONS / NOT A MOTION APPROVAL',70,1880,18,col)}
function tag(s,x,y,col=C.yellow){q.font='800 22px Manrope';rect(x,y-28,q.measureText(s).width+25,40,col);txt(s,x+12,y,22,C.navy)}
function opening(){base();heading(['Just dust.','Until it hits.']);grain(340,375,400);txt('ENLARGED ILLUSTRATIVE GRAIN',540,805,23,C.blue,'Manrope','center');cap(['At one-fifth the speed of light,','a speck becomes an impact hazard.']);surface('crater');line(540,1075,540,1130,C.yellow,3);footer(['Original grain and surface illustrations; separate, non-comparable scales.','No measured crater dimension or guaranteed whole-probe destruction.'])}
function evidence(){
 base(true);heading(['Sparse space.','Real obstacles.'],true);txt('RESEARCH / EDITORIAL SUMMARY',70,430,24,C.navy);line(70,455,1010,455,C.navy,2);
 txt('Hoang • Lazarian • Burkhart • Loeb',70,515,30,C.navy);txt('The interaction of relativistic spacecrafts',70,568,34,C.navy,'Playfair Display');txt('with the interstellar medium',70,614,34,C.navy,'Playfair Display');txt('Astrophysical Journal, 2017',70,674,26,C.navy);
 rect(70,716,940,55,'#F0D879');txt('Modeled dust impacts can crater and erode surfaces.',90,753,29,C.navy);
 cap(['Space between stars looks empty.','It still contains gas and dust.'],true);surface('intact',70,1135,600);grain(735,1160,260);
 txt('A FUTURE PROBE’S SURFACE',70,1680,23,C.navy);txt('ILLUSTRATIVE SPECIMEN',725,1515,20,C.navy,'Manrope','left',285);
 footer(['Source: arXiv:1608.05284v2 / impact discussion and protection strategies.','Editorial paraphrase, not a scan, quotation or copied paper figure.','Original illustrations, not experimental images.'],true)
}
function target(x,y){surface('intact',x,y,180);line(x,y,x,y+180,C.coral,5);txt('PROBE SURFACE',x+90,y+226,22,C.blue,'Manrope','center',280)}
function reference(stage){
 base();heading(stage===0?['One encounter.','Two viewpoints.']:stage===1?['Change the frame.','Keep the encounter.']:['From the probe,','dust comes at it.']);
 tag(['AMBIENT-MEDIUM FRAME','CHANGE OF REFERENCE FRAME','PROBE FRAME'][stage],70,438,stage===1?C.coral:C.yellow);
 grain(180,515,160);target(730,505);circle(260,595,88,C.yellow,2);line(348,595,728,595,C.muted,2,[7,9]);
 if(stage===0){arrow(705,730,415,730);txt('SURFACE MOVES LEFT',420,784,24,C.yellow);txt('Grain at rest in this idealized frame',70,489,22,C.blue)}
 if(stage===1){txt('SAME GRAIN',145,760,24,C.yellow);txt('SAME SURFACE',690,760,24,C.coral);txt('No second acceleration is added.',540,817,28,C.ivory,'Manrope','center')}
 if(stage===2){arrow(370,730,655,730);txt('GRAIN APPROACHES RIGHT',350,784,24,C.yellow);txt('Surface at rest in this frame',70,489,22,C.blue)}
 cap(stage===0?['Now send a tiny probe through it','at roughly 60,000 km a second.']:stage===1?['In the probe’s frame,','the dust comes at it that fast.']:['The danger comes','from relative speed.']);
 rect(70,1120,940,480,C.ivory);txt('ONE RELATIVE ENCOUNTER SPEED',110,1190,26,C.navy);txt('0.2c',110,1365,141,C.navy,'Playfair Display');txt('≈ 60,000 km/s',110,1445,52,C.navy);txt('Not 0.2c + 0.2c',110,1530,30,C.navy);
 txt(stage===1?'The coordinate viewpoint changes.':'Diagram keeps the same grain and target.',540,1660,27,C.blue,'Manrope','center',940);
 footer(['Original working figure / arrows and object sizes are schematic.','Selected grain and surface are the same in all three states.','No additional acceleration, collision or measured density is depicted.'])
}
function contact(){base();heading(['Energy,','concentrated.']);grain(70,430,270);txt('RELATIVE SPEED',405,500,26,C.yellow);txt('Tiny mass can still carry',405,564,35,C.ivory,'Playfair Display');txt('substantial kinetic energy.',405,611,35,C.ivory,'Playfair Display');txt('Outcome depends on the impact.',405,688,24,C.blue);cap(['On impact, that energy can','heat and eject surface material.']);surface('contact');footer(['Qualitative contact illustration; colors do not measure temperature.','Not a nuclear reaction, combustion, blast wave or impact simulation.'])}
function crater(){base();heading(['A little loss.','Across a journey.']);surface('intact',70,455,310);surface('crater',700,455,310);arrow(420,610,650,610);txt('INTACT',225,807,24,C.blue,'Manrope','center');txt('ONE LOCAL SCAR',855,807,24,C.blue,'Manrope','center');cap(['Repeated impacts can erode','the spacecraft’s surface.']);surface('crater');txt('LOCAL DAMAGE / CUMULATIVE DESIGN PROBLEM',540,1090,24,C.yellow,'Manrope','center');footer(['Displayed scar is illustrative, not a predicted size or impact rate.','Damage depends on material, grain population, speed and route.'])}
function protection(){base();heading(['Reaching a star','is only half of it.']);grain(70,430,250);surface('intact',670,420,330);arrow(350,590,620,590);line(660,420,660,750,C.coral,10);txt('INCIDENT DUST',70,795,24,C.blue);txt('CANDIDATE PROTECTION',650,795,22,C.coral,'Manrope','left',360);cap(['Fast enough to reach another star—','tough enough to survive the journey?']);surface('intact',70,1170,600);txt('GRAINS',730,1240,30,C.ivory);txt('MATERIAL',730,1330,30,C.ivory);txt('ROUTE',730,1420,30,C.ivory);txt('All affect the result.',730,1520,25,C.blue,'Manrope','left',290);footer(['Protective layers and smaller frontal area are research strategies.','Concept only: not a validated shield or a claim of impossible travel.'])}
const states=[['01_hook',opening],['02_evidence',evidence],['03_frame_initial',()=>reference(0)],['04_frame_intermediate',()=>reference(1)],['05_frame_resolved',()=>reference(2)],['06_contact',contact],['07_crater',crater],['08_protection_payoff',protection]];
async function main(){
 atlas=await loadImage(path.join(R,'assets/dust-atlas-v1.png'));if(atlas.width<1200||atlas.height<1200)throw Error('Atlas insufficient native detail');
 const records=[];for(hidden of [false,true])for(const [id,draw] of states){current=id+(hidden?'_labels_only':'');const can=createCanvas(W,H);q=can.getContext('2d');draw();const b=can.toBuffer('image/jpeg',94),name=current+'.jpg';fs.writeFileSync(path.join(O,name),b);const im=await loadImage(b);if(im.width!==W||im.height!==H)throw Error('Wrong dimensions');records.push({id:current,path:'rendered/'+name,width:W,height:H,bytes:b.length,sha256:hash(b),hidden})}
 const manifest={source_commit:process.env.GITHUB_SHA||null,stage:'STATIC_ART_REVIEW',production_standard:'sun-disappeared-v1',owner_art_approval:'NOT REVIEWED',motion:'NOT RENDERED',voice:'NOT RECORDED',atlas:{path:'assets/dust-atlas-v1.png',width:atlas.width,height:atlas.height,sha256:hash(fs.readFileSync(path.join(R,'assets/dust-atlas-v1.png'))),max_surface_cell_footprint:600},fonts:['Playfair900.ttf','Manrope800.ttf'].map(f=>({path:'../../black-dwarf-supernova/art-v1/assets/'+f,sha256:hash(fs.readFileSync(path.join(F,f)))})),caption_band:'42–58%; draft samples, not word-aligned',records};
 fs.writeFileSync(path.join(R,'ART_MANIFEST.json'),JSON.stringify(manifest,null,2)+'\n');fs.writeFileSync(path.join(R,'TEXT_METRICS.json'),JSON.stringify(boxes,null,2)+'\n');
 const sheet=createCanvas(8*270,590),s=sheet.getContext('2d');s.fillStyle=C.navy;s.fillRect(0,0,sheet.width,sheet.height);for(let i=0;i<states.length;i++){const im=await loadImage(path.join(O,states[i][0]+'.jpg'));s.drawImage(im,i*270,0,270,480);s.fillStyle=C.ivory;s.font='16px sans-serif';s.fillText(states[i][0].replaceAll('_',' '),i*270+10,520)}fs.writeFileSync(path.join(R,'Relativistic_Dust_Art_Contact_v1.jpg'),sheet.toBuffer('image/jpeg',94));
 const data=name=>'data:image/jpeg;base64,'+fs.readFileSync(path.join(O,name+'.jpg')).toString('base64');
 const cards=states.map(([id])=>'<article><h2>'+id.replaceAll('_',' ')+'</h2><img src="'+data(id)+'" data-normal="'+data(id)+'" data-clean="'+data(id+'_labels_only')+'"></article>').join('');
 fs.writeFileSync(path.join(R,'Relativistic_Dust_Art_Review_v1.html'),'<!doctype html><meta charset="utf-8"><title>Relativistic Dust Art v1</title><style>body{background:#0D1C2B;color:#F5F0E7;font:17px system-ui;margin:24px}header{max-width:900px}button{padding:14px;font:inherit}main{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:20px}img{width:100%;height:auto}h2{font-size:17px}</style><header><h1>The Dust Between Us and the Stars</h1><p>Eight native 1080×1920 static frames, original illustrative assets and source-based working figures. Not observations, validated impact simulations or an animated film. Review the three reference-frame states and impact/crater sequence. Grain and surface images use different illustrative scales. Draft captions are unrecorded; owner/motion/audio approval remains pending.</p><button>Hide titles and draft captions</button></header><main>'+cards+'</main><footer><p>Sources: Hoang et al. (2017), arXiv:1608.05284v2; Long (2023), arXiv:2307.12160; OpenStax relativistic energy. No source figures copied. Original ImageGen atlas; pinned Playfair Display 900 and Manrope. Hashes and dimensions in ART_MANIFEST.json.</p></footer><script>let clean=false;document.querySelector("button").onclick=()=>{clean=!clean;document.querySelectorAll("img").forEach(im=>im.src=clean?im.dataset.clean:im.dataset.normal);document.querySelector("button").textContent=clean?"Restore titles and captions":"Hide titles and draft captions"};</script>');
 console.log(JSON.stringify({states:8,frames:records.length,atlas:[atlas.width,atlas.height],native_surface_footprint:600,owner_approval:'NOT REVIEWED'}));
}
main().catch(e=>{console.error(e);process.exit(1)});
