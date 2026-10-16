const fs=require('fs'),path=require('path'),{spawn}=require('child_process');
const {spawnSync}=require('child_process');
const {createCanvas,loadImage,GlobalFonts}=require(process.env.CODEX_PRIMARY_RUNTIME_NODE_MODULES+'/@napi-rs/canvas');
const R=__dirname,A=path.resolve(R,'../art-v1/assets'),ENGINE=path.resolve(R,'../../../../engine');
global.document={createElement:()=>createCanvas(1,1)};
require(path.join(ENGINE,'browser/finishing.js'));require('./editorial-finish.cjs');
GlobalFonts.registerFromPath(path.join(A,'Playfair900.ttf'),'Playfair Display');GlobalFonts.registerFromPath(path.join(A,'Manrope800.ttf'),'Manrope');
const timeline=JSON.parse(fs.readFileSync(path.join(R,'timeline.json'))),E=x=>{x=Math.max(0,Math.min(1,x));return x*x*(3-2*x)},bell=(t,a,b,c,d)=>E((t-a)/(b-a))*(1-E((t-c)/(d-c)));
let scene,finish,source,out,ctx,scale=1,options={},current=0;
function direction(t){const f=options,cut=bell(t,6.38,6.57,6.72,7.02),hunt=bell(t,3.2,3.34,3.5,3.76),u=E((t-3.9)/.8);return{
 focus:{shadeStrength:f.focus_shading===false?0:.22,strength:f.selective_focus===false?0:.84*bell(t,3.0,3.6,5.8,6.35),cx:368+(540-368)*u,cy:650+(1430-650)*u,rx:370,ry:290,blur:5.4},
 cut:f.motion_blur===false?0:cut,hunt:f.focus_hunt===false?0:1.4*hunt,dx:-18*cut,
 fringePx:f.chromatic===false?0:.95,jitterPx:f.mechanical_jitter===false?0:.45,
 exposureStops:f.exposure===false?0:.024,grainStrength:f.moving_grain===false?0:.23};}
function captions(target,t,mask=false){const cap=timeline.captions.find(x=>t>=x.start&&t<x.end);if(!cap)return;const q=target;q.save();q.setTransform(scale,0,0,scale,0,0);q.font='800 43px Manrope';q.textAlign='center';let lines=cap.lines,w=Math.max(...lines.map(x=>q.measureText(x).width))+54,h=lines.length*55+18,y=960-h/2;q.fillStyle=mask?'#fff':'rgba(10,22,34,1)';q.fillRect(540-w/2,y,w,h);q.fillStyle='#fff';lines.forEach((s,i)=>q.fillText(s,540,y+48+i*55));q.restore()}
function renderAt(t,opts={}){options=opts;current=t;let sourceT=opts.sourceTime??t;const s=source.getContext('2d');s.setTransform(scale,0,0,scale,0,0);s.clearRect(0,0,1080,1920);scene.render(s,sourceT,opts);
 if(opts.focus_shading===false){/* selected-focus treatment omitted together for the independent shade proof variant */}
 // The shared pass couples selective blur and surrounding shade to the same field.
 finish.apply(source,ctx,opts.filmTime??t,{enabled:opts.finishing!==false});
 ctx.save();ctx.globalCompositeOperation='destination-over';ctx.fillStyle=sourceT<6.6?'#0D1C2B':'#F5F0E7';ctx.fillRect(0,0,out.width,out.height);ctx.restore();
 if(opts.captions!==false)captions(ctx,t);return out;
}
async function setup(w=1080){scale=w/1080;let loaded={};for(const[k,n]of Object.entries({steel:'steel-spoon.png',wood:'wood-spoon.png',hand:'hand.png'}))loaded[k]=await loadImage(path.join(A,n));scene=require('./scene-core.cjs')(createCanvas,loaded);source=createCanvas(w,Math.round(w*1920/1080));out=createCanvas(w,source.height);ctx=out.getContext('2d');finish=new CurioEditorialFinish.EditorialFinish(w,out.height,direction);}
async function encode(){const gate=spawnSync('python3',[path.join(R,'preflight.py')],{stdio:'inherit'});if(gate.status!==0)throw Error('Pre-capture gate failed');await setup();const n=timeline.frames,output=path.join(R,'Cold_Metal_Sequence.mp4');let ff=spawn('ffmpeg',['-y','-v','error','-f','rawvideo','-pixel_format','rgba','-video_size','1080x1920','-framerate','30','-i','pipe:0','-i',path.join(R,'audio/mix.wav'),'-map','0:v','-map','1:a','-c:v','libx264','-preset','fast','-crf','19','-pix_fmt','yuv420p','-c:a','aac','-b:a','256k','-ar','48000','-t',String(timeline.duration),'-movflags','+faststart',output],{stdio:['pipe','inherit','inherit']});let exited=new Promise((resolve,reject)=>ff.on('exit',code=>code===0?resolve():reject(Error('ffmpeg '+code))));
 for(let nFrame=0;nFrame<n;nFrame++){const canvas=renderAt(nFrame/30);const pixels=canvas.getContext('2d').getImageData(0,0,canvas.width,canvas.height).data;if(!ff.stdin.write(Buffer.from(pixels.buffer,pixels.byteOffset,pixels.byteLength)))await new Promise(resolve=>ff.stdin.once('drain',resolve));if(nFrame%60===0){fs.writeFileSync(path.join(R,'RENDER_PROGRESS.json'),JSON.stringify({frames_done:nFrame,frames_total:n,stage:'local preview capture; final archive pending'}));console.log(nFrame+'/'+n)}}ff.stdin.end();await exited;console.log(output)}
module.exports={setup,renderAt,captions,getDebug:()=>({source,finish}),getContext:()=>ctx,getOutput:()=>out,direction};
if(require.main===module)encode().catch(e=>{console.error(e);process.exit(1)});
