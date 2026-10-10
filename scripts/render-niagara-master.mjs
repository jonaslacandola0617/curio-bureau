#!/usr/bin/env node
/** Curio Bureau deterministic 1080x1920/30fps PNG-frame renderer, H264+AAC master.
    Film timing and captions both come from renderAt(frame/30).
    Audio comes from synchronized browser/WebAudio WebM capture.
*/
import { chromium } from 'playwright';
import { mkdir, stat } from 'node:fs/promises';
import { spawn } from 'node:child_process';
import { once } from 'node:events';
import { resolve } from 'node:path';
import { pathToFileURL } from 'node:url';

const html=resolve(process.env.CURIO_HTML||'dist/niagara-1969/Curio_Bureau_Niagara_1969_Editorial.html');
const audioWebm=resolve(process.env.CURIO_WEBM||'dist/niagara-1969/Curio_Bureau_Niagara_1969_Editorial.webm');
const out=resolve(process.env.CURIO_MP4||'dist/niagara-1969/Curio_Bureau_Niagara_1969_Editorial.mp4');
const QA=resolve('dist/niagara-1969/qa-frames');
await mkdir(QA,{recursive:true});
const b=await chromium.launch({headless:true});
try{
 const page=await b.newPage({viewport:{width:1080,height:1920},deviceScaleFactor:1});
 let pageErrors=[];page.on('pageerror',e=>pageErrors.push(e.message));
 await page.goto(pathToFileURL(html).href,{waitUntil:'load',timeout:60000});
  const photoReady=await page.evaluate(async()=>await window.NIAGARA_READY);
  if(!photoReady)throw new Error('Historic documentary photo asset was not loaded');

 await page.evaluate(async()=>{
  await document.fonts.load('600 100px "Playfair Display"');
  await document.fonts.load('800 42px "Manrope"');
  await document.fonts.ready;
 });
 const pre=await page.evaluate(()=>{
  const faces=Array.from(document.fonts).map(f=>({family:f.family,status:f.status}));
  return{faces, duration:window.getDuration?.(),fps:window.getFPS?.(),geodata:window.CURIO_QA?.mapLoaded,captions:window.CURIO_QA?.captionCount,sfx:Object.keys(window.CURIO_SFX||{}).length,photo:window.CURIO_QA?.photoLoaded};
 });
 console.log('FILM MANIFEST:',JSON.stringify(pre));
 if(!pre.faces.some(f=>f.family.toLowerCase().includes('playfair')&&f.status==='loaded'))throw Error('Playfair Display not actually loaded');
 if(!pre.faces.some(f=>f.family.toLowerCase().includes('manrope')&&f.status==='loaded'))throw Error('Manrope not actually loaded');
 if(pre.duration!==64||pre.fps!==30||!pre.geodata||!pre.photo||pre.captions<32||pre.sfx<11)throw Error('Required film assets incomplete');
 const cv=page.locator('#film');
 const audits=[0,.2,.8,2,4,6.5,7.9,8.03,9,12,15.9,16.03,17,20,24.9,25.03,26,30,33.9,34.03,37,40,41.9,42.03,45,48,50.9,51.03,54,57.9,58.03,60,61,62,63,63.8,63.96];
 let failed=[];
 for(const t of audits){
  const report=await page.evaluate(t=>window.inspectFrame(t),t);
  if(report.issues.length)failed.push({time:t,issues:report.issues});
  const name=('000000'+Math.round(t*100)).slice(-6);
  await cv.screenshot({path:resolve(QA,'frame-'+name+'.png'),timeout:25000});
 }
 if(failed.length)throw Error('BUILD-FAIL clipped critical title '+JSON.stringify(failed.slice(0,12)));
 if(pageErrors.length)throw Error('Browser script errors: '+pageErrors.join('; '));
 console.log('QA frame text scan passed:',audits.length,'frames. Native pixels captured.');
 // Deterministic 30fps PNG stream directly into high quality H.264 encoder.
 // Recording audio from WebM avoids two concurrent independent clocks.
 const args=['-y','-loglevel','error','-threads','2','-f','image2pipe','-framerate','30','-vcodec','png','-i','pipe:0','-i',audioWebm,
 '-map','0:v:0','-map','1:a:0','-c:v','libx264','-preset','medium','-crf','16','-pix_fmt','yuv420p',
 '-r','30','-c:a','aac','-ar','48000','-b:a','256k','-af','loudnorm=I=-14:TP=-1.3:LRA=9',
 '-t','64','-movflags','+faststart',out];
 const ff=spawn('ffmpeg',args,{stdio:['pipe','inherit','inherit']});
 ff.stdin.on('error',err=>console.error('ffmpeg pipe',err.message));
 let exitCode;const exited=once(ff,'exit').then(([code])=>(exitCode=code));
 for(let f=0;f<1920;f++){
  const base64=await page.evaluate(f=>{
    window.renderAt(f/30);
    return document.getElementById('film').toDataURL('image/png').split(',')[1];
  },f);
  const data=Buffer.from(base64,'base64');
  if(!ff.stdin.write(data))await once(ff.stdin,'drain');
  if(f%240===0)console.log('Native deterministic video frames',f,'/ 1920');
 }
 ff.stdin.end();await exited;
 if(exitCode!==0)throw Error('FFmpeg native master encoder failed code '+exitCode);
 const info=await stat(out);if(info.size<3000000)throw Error('Suspiciously small video '+info.size);
 console.log('NATIVE MASTER SUCCESS',out,info.size);
}finally{await b.close()}
