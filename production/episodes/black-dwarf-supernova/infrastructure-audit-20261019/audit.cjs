/* Read-only native effect isolation of frozen motion-v1. Never writes movie/source. */
const fs=require('fs'),path=require('path'),vm=require('vm'),crypto=require('crypto');
const root=path.resolve(__dirname,'../motion-v1'),file=path.join(root,'render.cjs'),src=fs.readFileSync(file,'utf8');
const digest=b=>crypto.createHash('sha256').update(b).digest('hex');
function load(edits=[]){let code=src;for(const[a,b]of edits){if(!code.includes(a))throw Error('Isolation target missing: '+a);code=code.replace(a,b)}let mod={exports:{}};vm.runInNewContext(code,{require:require('module').createRequire(file),module:mod,exports:mod.exports,__dirname:root,process,Buffer,console},{filename:file});return mod.exports}
const pixels=c=>Buffer.from(c.getContext('2d').getImageData(0,0,1080,1920).data);
const cases=[
 ['material_texture',8,[['bg=mat(false,W,H);paper=mat(true,940,585);','bg=mat(false,W,H);paper=mat(true,940,585);for(const [c,col] of [[bg,C.ink],[paper,C.ivory]]){let p=c.getContext("2d");p.fillStyle=col;p.fillRect(0,0,c.width,c.height)}'],['q.globalAlpha=.075;q.drawImage(print','q.globalAlpha=0;q.drawImage(print']]],
 ['moving_grain',8,[['o.globalAlpha=.17;let bank','o.globalAlpha=0;let bank']]],
 ['motion_blur',9.666667,[['p.transition*5+p.hunt','p.hunt']]],
 ['selective_focus',8,[['o.drawImage(mask,0,0);','/* isolated selective blur disabled */']]],
 ['focus_shading',8,[["rgba(5,14,23,.12)","rgba(5,14,23,0)"]]],
 ['focus_hunt',9.666667,[['hunt:1.7*Math.exp','hunt:0*Math.exp']]],
 ['chromatic',8,[[')*.45,0',')*0,0']]],
 ['mechanical_jitter',8,[['Math.sin(k*7.17)*.28','Math.sin(k*7.17)*0'],['Math.cos(k*3.13)*.28','Math.cos(k*3.13)*0']]],
 ['exposure',8,[['Math.abs(e*.014)','Math.abs(e*0)']]],
 ['marker_wobble',20.5,[['j=.55*Math.sin','j=0*Math.sin']]]
];
(async()=>{let original=load();await original.setup();let results=[];for(const[name,t,edits]of cases){let alt=load(edits);await alt.setup();let a=pixels(original.renderAt(t)),box=original.getCaptionBox(),b=pixels(alt.renderAt(t));let sum=0,changed=0,cap=0;for(let i=0;i<a.length;i+=4){let d=Math.abs(a[i]-b[i])+Math.abs(a[i+1]-b[i+1])+Math.abs(a[i+2]-b[i+2]);sum+=d;if(d)changed++}if(box)for(let y=box.y+3;y<box.y+box.h-3;y++)for(let x=box.x+3;x<box.x+box.w-3;x++){let i=(y*1080+x)*4;cap+=Math.abs(a[i]-b[i])+Math.abs(a[i+1]-b[i+1])+Math.abs(a[i+2]-b[i+2])}results.push({effect:name,time:t,mean_abs_rgb:sum/(1080*1920*3),changed_pixels:changed,opaque_caption_difference:cap,execution:changed>0&&cap===0?'PASS':'REVISE'});console.log(name,results.at(-1).execution,results.at(-1).mean_abs_rgb)}
let envelope=[9,9.5,9.583334,9.666667,9.75,10,10.166667,10.5].map(time=>{let t=Math.floor((time+1e-8)*12)/12,s=original.state(t);return{time,scene_time:t,hunt_radius:s.hunt,transition_radius:s.transition*5}});
let frozen=JSON.parse(fs.readFileSync(path.join(root,'SOURCE_FINGERPRINT.json'))),drift=frozen.files.filter(x=>digest(fs.readFileSync(path.join(root,x.path)))!==x.sha256).map(x=>x.path);
let r={scope:'Native still diagnostics only; no new movie or revised creative source',renderer_sha256:digest(src),audit_sha256:digest(fs.readFileSync(__filename)),frozen_source_drift:drift,effects:results,settling_envelope:envelope,limitations:['Independent execution is not encoded perceptual acceptance.','Marker translation is not ink bleed or contour edge boil.','Spatial blur/shading use a common focus anchor but different feather profiles.','Existing build_release.py does not call shared production_standard/finishing_audit validators.','Full-film ending and full 57-item look-back remain pending.'],decision:'HOLD_FULL_RENDER'};
fs.writeFileSync(path.join(__dirname,'NATIVE_EFFECT_AUDIT.json'),JSON.stringify(r,null,2)+'\n');if(drift.length||results.some(x=>x.execution!=='PASS'))process.exitCode=1;
})().catch(e=>{console.error(e);process.exit(1)});
