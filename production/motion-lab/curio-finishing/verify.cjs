/* Repeatable mechanism checks; these do not grant creative film approval. */
const fs=require('fs'),path=require('path');
const {chromium}=require(process.env.CODEX_PRIMARY_RUNTIME_NODE_MODULES?process.env.CODEX_PRIMARY_RUNTIME_NODE_MODULES+'/playwright':'playwright');
async function main(){
 const browser=await chromium.launch({headless:true,...(process.env.CURIO_CHROME?{executablePath:process.env.CURIO_CHROME}:{}),args:['--no-sandbox']});
 const page=await browser.newPage();await page.setContent('<html><body></body></html>');await page.addScriptTag({path:path.join(__dirname,'curio-finishing.js')});
 const report=await page.evaluate(()=>{
  const F=CurioFinishing,make=(w,h)=>{let c=document.createElement('canvas');c.width=w;c.height=h;return c;},check=(v,s)=>{if(!v)throw Error(s);};
  let src=make(360,480),s=src.getContext('2d'),dst=make(360,480),d=dst.getContext('2d');
  for(let y=0;y<480;y+=8)for(let x=0;x<360;x+=8){s.fillStyle=((x/8+y/8)%2)?'#eeeeee':'#222222';s.fillRect(x,y,8,8);}
  let params={cx:180,cy:240,rx:70,ry:100,feather:.8,maxBlur:9,outsideGain:.65},f=new F.FocusPass(360,480),before=s.getImageData(0,0,360,480).data;f.apply(src,d,params);let after=d.getImageData(0,0,360,480).data;
  const roi=(a,x,y,w,h)=>{let values=[];for(let j=y;j<y+h;j++)for(let i=x;i<x+w;i++)values.push(a[(j*360+i)*4]);let mean=values.reduce((a,b)=>a+b,0)/values.length;return {mean,variance:values.reduce((a,b)=>a+(b-mean)**2,0)/values.length};};
  let center=0;for(let y=220;y<260;y++)for(let x=160;x<200;x++)center=Math.max(center,Math.abs(before[(y*360+x)*4]-after[(y*360+x)*4]));let raw=roi(before,16,16,32,32),out=roi(after,16,16,32,32);
  check(center===0,'Focus center changed');check(out.variance<raw.variance*.15,'Context not defocused');check(out.mean<raw.mean*.8,'Shared gradient did not darken context');
  let sweep=[0,.25,.5,.75,1].map(strength=>{f.apply(src,d,{...params,strength});return {strength,...roi(d.getImageData(0,0,360,480).data,16,16,32,32)};});check(sweep[0].variance>sweep[2].variance&&sweep[2].variance>sweep[4].variance,'Blur strength is not progressive');
  let options={jitterPx:.5,exposureStops:.04,jitterFps:24,exposureFps:2,grainStrength:.02},a=F.filmState(1.01,options),held=F.filmState(1.02,options),next=F.filmState(1.06,options);check(JSON.stringify(a)===JSON.stringify(held),'Film cadence unstable within hold');check(a.dx!==next.dx,'Jitter cadence does not update');check(Math.abs(a.dx)<=.5&&Math.abs(a.dy)<=.5,'Jitter exceeds amplitude');
  F.filmFinish(src,d,1.2,options);let first=d.getImageData(0,0,360,480).data.slice();F.filmFinish(src,d,1.2,options);let second=d.getImageData(0,0,360,480).data;check(first.every((v,i)=>v===second[i]),'Film sampling is nondeterministic');
  let points=Array.from({length:50},(_,i)=>[i*5,60+Math.sin(i*.1)*15]),edge=F.boilPath(points,1.2),edge2=F.boilPath(points,1.3);check(JSON.stringify(edge[0])===JSON.stringify(points[0])&&JSON.stringify(edge.at(-1))===JSON.stringify(points.at(-1)),'Boil detaches endpoints');check(JSON.stringify(edge)!==JSON.stringify(edge2),'Boil does not evolve');
  let ink=make(240,100),ic=ink.getContext('2d');ic.fillStyle='white';ic.fillRect(0,0,240,100);F.drawInkStroke(ic,[[20,50],[220,50]],{width:4,bleedPx:2,bleedAlpha:.5,color:'#000000'});let core=ic.getImageData(100,50,1,1).data[0],halo=ic.getImageData(100,55,1,1).data[0];check(core<10&&halo<255&&halo>core,'Ink core/spread not separated');
  let near=F.parallaxTransform({z:0},{x:30},{width:360,height:480}),far=F.parallaxTransform({z:800},{x:30},{width:360,height:480});check(Math.abs(near.x-180)>Math.abs(far.x-180),'Depth does not affect displacement');
  return {status:'TECHNICAL_COMPONENT_CHECKS_PASSED',scope:'Synthetic Canvas mechanism checks; no full-film artistic or authentic photo-parallax approval.',focus:{center_max_channel_error:center,source_context:raw,processed_context:out,strength_sweep:sweep},film:{held_cadence:true,deterministic_pixels:true,amplitude_bounded:true},edge_boil:{endpoints_attached:true,evolves:true},ink:{core_pixel:core,spread_pixel:halo},parallax:{near,far,depth_dependence:true},browser_errors:[]};
 });
 fs.writeFileSync(path.join(__dirname,'verification.json'),JSON.stringify(report,null,2)+'\n');await browser.close();console.log(report.status);
}
main().catch(e=>{console.error(e);process.exit(1);});
