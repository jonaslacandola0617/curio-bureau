#!/usr/bin/env node
/* CURIO BUREAU Episode 005 deterministic native-4K renderer.
   Pipeline: canvas vector graphics -> in-memory lossless PNG frames ->
   ffmpeg H.264 encoder with independently mastered 48k audio. */
const {createCanvas,loadImage,registerFont}=require("canvas");
const fs=require("fs"),path=require("path"),vm=require("vm");
const {spawn}=require("child_process"),{once}=require("events");
const root=path.resolve(__dirname,"..");
const dir=path.resolve(root,"out");
const WIDTH=2160,HEIGHT=3840,FPS=30,DURATION=76;
if(fs.existsSync(path.join(root,"fonts","PlayfairDisplay.ttf")))
  registerFont(path.join(root,"fonts","PlayfairDisplay.ttf"),{family:"Playfair Display"});
if(fs.existsSync(path.join(root,"fonts","Manrope.ttf")))
  registerFont(path.join(root,"fonts","Manrope.ttf"),{family:"Manrope"});
const src=fs.readFileSync(path.join(root,"studio","scene.js"),"utf8");
vm.runInThisContext(src,{filename:"scene.js"});
const spec=globalThis.Curio005;
if(!spec||spec.fps!==30||spec.duration!==76)throw Error("Timeline mismatch");
const captions=JSON.parse(fs.readFileSync(path.join(dir,"captions.json")));
fs.mkdirSync(path.join(dir,"qa"),{recursive:true});
async function main(){
 const assets={};
 for(const [name,f] of [["aerial","aerial.jpg"],["after","after.jpg"]]){
  const full=path.join(root,"assets",f);
  if(fs.existsSync(full))assets[name]=await loadImage(full);
 }
 if(!assets.aerial||!assets.after)throw Error("Required documented historical photos absent — do not manufacture evidence");
 const canvas=createCanvas(WIDTH,HEIGHT),ctx=canvas.getContext("2d");
 const vpath=path.join(dir,"Curio_Bureau_EP005_4K_CANDIDATE.mp4");
 const args=["-hide_banner","-loglevel","error","-y","-f","image2pipe","-r","30",
    "-vcodec","png","-i","pipe:0","-i",path.join(dir,"master_mix.wav"),
    "-map","0:v","-map","1:a","-c:v","libx264",
    "-preset","fast","-crf","15","-pix_fmt","yuv420p",
    "-color_primaries","bt709","-color_trc","bt709","-colorspace","bt709",
    "-c:a","aac","-b:a","320k","-ar","48000","-ac","2",
    "-movflags","+faststart","-t",String(DURATION),vpath];
 const ff=spawn("ffmpeg",args,{stdio:["pipe","inherit","inherit"]});
 let failed=null;ff.on("error",err=>{failed=err;});
 const frames=DURATION*FPS;
 const stamps=new Set([0,1,30,60,90,120,240,450,600,780,900,1080,1260,1440,1620,1740,1860,2040,2220,2279]);
 for(let i=0;i<frames;i++){
   if(failed)throw failed;
   spec.render(ctx,i/FPS,assets,captions);
   let buf=canvas.toBuffer("image/png",{compressionLevel:2,filters:0});
   if(stamps.has(i)){
      // retain lossless exact 4K QA checkpoint and smaller JPEG for contact sheet
      fs.writeFileSync(path.join(dir,"qa","frame_"+String(i).padStart(4,"0")+".png"),buf);
      fs.writeFileSync(path.join(dir,"qa","frame_"+String(i).padStart(4,"0")+".jpg"),
          canvas.toBuffer("image/jpeg",{quality:.86,progressive:true}));
   }
   if(!ff.stdin.write(buf))await once(ff.stdin,"drain");
   if(i%150===0)console.log("FRAME",i,"/",frames);
 }
 ff.stdin.end();
 const [code]=await once(ff,"close");
 if(code!==0)throw Error("MP4 encode exited "+code);
 console.log("COMPLETE",vpath,fs.statSync(vpath).size);
}
main().catch(e=>{console.error(e.stack||e);process.exit(1)});
