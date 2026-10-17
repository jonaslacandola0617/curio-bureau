// A fresh process bounds deferred native-canvas allocations to at most three frames.
const m=require('./render.cjs');
(async()=>{await m.setup(2160);const start=Number(process.argv[2]),count=Number(process.argv[3]);for(let i=0;i<count;i++){const c=m.renderAt((start+i)/30);const d=c.getContext('2d').getImageData(0,0,2160,3840).data;if(!process.stdout.write(Buffer.from(d.buffer,d.byteOffset,d.byteLength)))await new Promise(r=>process.stdout.once('drain',r));await new Promise(setImmediate);if(global.gc)global.gc();}})().catch(e=>{console.error(e);process.exit(1)});
