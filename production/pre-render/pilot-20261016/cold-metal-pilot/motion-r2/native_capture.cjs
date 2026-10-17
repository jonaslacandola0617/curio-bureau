// Native integer-frame capture with complete lossless checkpoints and source identity.
const fs=require('fs'),path=require('path'),crypto=require('crypto'),{spawn,spawnSync}=require('child_process'),m=require('./render.cjs');
const R=__dirname,hash=b=>crypto.createHash('sha256').update(b).digest('hex'),T=JSON.parse(fs.readFileSync(path.join(R,'timeline.json'))),chunkSize=30;
const sources=['render.cjs','scene-core.cjs','editorial-finish.cjs','native_capture.cjs','timeline.json','audio/mix.wav'];
const fingerprint=hash(Buffer.from(JSON.stringify(sources.map(p=>[p,hash(fs.readFileSync(path.join(R,p)))]))));
async function main(){let pre=spawnSync('python3',[path.join(R,'preflight.py')],{stdio:'inherit'});if(pre.status)throw Error('Preflight failed');
let proof=JSON.parse(fs.readFileSync(path.join(R,'NATIVE_PROOF.json')));if(proof.native[0]!==2160||proof.errors.length)throw Error('Native proof missing');for(const [p,h]of Object.entries(proof.source_fingerprints))if(hash(fs.readFileSync(path.join(R,p)))!==h)throw Error('Stale native proof: '+p);
fs.mkdirSync(path.join(R,'chunks'),{recursive:true});let recovery={scope:'Native 13.9s sequence R2',width:2160,height:3840,fps:30,total_frames:T.frames,source_fingerprint:fingerprint,chunks:[]};
let existing=path.join(R,'RECOVERY.json');if(fs.existsSync(existing)){let d=JSON.parse(fs.readFileSync(existing));if(d.source_fingerprint===fingerprint)recovery=d;}
await m.setup(2160);let stop=Number(process.env.CURIO_STOP_AFTER_CHUNKS||9999),rendered=0;
for(let start=0;start<T.frames;start+=chunkSize){let count=Math.min(chunkSize,T.frames-start),name=`chunk_${String(start).padStart(4,'0')}_${count}.mkv`,dest=path.join(R,'chunks',name),old=recovery.chunks.find(x=>x.start_frame===start);
if(old&&fs.existsSync(dest)&&hash(fs.readFileSync(dest))===old.sha256){console.log('REUSE',name);continue;}
// Prevent more than two fresh unarchived chunks accumulating between durable checkpoints.
let pending=recovery.chunks.filter(x=>x.storage_status!=='DURABLE').length;if(pending>=2)throw Error('Two locally verified chunks await GitHub storage receipts; checkpoint before continuing');
let partial=dest+'.partial.mkv';let ff=spawn('ffmpeg',['-nostdin','-y','-v','error','-f','rawvideo','-pixel_format','rgba','-video_size','2160x3840','-framerate','30','-i','pipe:0','-an','-c:v','ffv1','-level','3','-coder','1','-context','1','-g','1','-threads','2','-pix_fmt','gbrp',partial],{stdio:['pipe','inherit','inherit']});let done=new Promise((res,rej)=>ff.on('exit',c=>c===0?res():rej(Error('FFV1 '+c))));
for(let frame=start;frame<start+count;frame++){if(global.gc)global.gc();let c=m.renderAt(frame/30),d=c.getContext('2d').getImageData(0,0,2160,3840).data;if(!ff.stdin.write(Buffer.from(d.buffer,d.byteOffset,d.byteLength)))await new Promise(res=>ff.stdin.once('drain',res));if(frame%10===0)console.log('FRAME',frame,'/',T.frames);}
ff.stdin.end();await done;let raw=spawnSync('ffprobe',['-v','error','-count_frames','-select_streams','v:0','-show_entries','stream=width,height,nb_read_frames','-of','json',partial],{encoding:'utf8'});let v=JSON.parse(raw.stdout).streams[0];if(v.width!==2160||v.height!==3840||+v.nb_read_frames!==count)throw Error('Chunk decode/count failed');fs.renameSync(partial,dest);
let record={file:'chunks/'+name,start_frame:start,frame_count:count,sha256:hash(fs.readFileSync(dest)),bytes:fs.statSync(dest).size,decode:'PASS',storage_status:'LOCAL_VERIFIED',source_fingerprint:fingerprint};recovery.chunks=recovery.chunks.filter(x=>x.start_frame!==start);recovery.chunks.push(record);fs.writeFileSync(existing,JSON.stringify(recovery,null,2)+'\n');console.log('CHUNK_VERIFIED',name,record.bytes);rendered++;if(rendered>=stop)break;
}console.log('Capture checkpoint complete');}
main().catch(e=>{console.error(e);process.exit(1)});
