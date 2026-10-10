import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {resolve} from 'node:path';
const root='films/samoa-2011/vox/';
const template=await readFile(resolve(root,'film.template.html'),'utf8');
const motion=await readFile(resolve(root,'motion.js'),'utf8');
const director=await readFile(resolve(root,'director.js'),'utf8');
const captions=JSON.parse(await readFile('dist/samoa-2011/captions.json','utf8'));
const geo=JSON.parse(await readFile('dist/samoa-2011/geography.json','utf8'));
if(captions.length<35||geo.length<4)throw Error('Missing aligned captions or geography');
const names=['sweep','arrow','click','type','fast','riser','popup','cinematic','chime','tick'];
const narrationB64=(await readFile('dist/samoa-2011/narration-embedded.mp3')).toString('base64');
if(narrationB64.length<100000)throw Error('Embedded narration missing or too small');
const b64={};
for(const n of names){let data=(await readFile(resolve('films/samoa-2011/assets/sfx/',n+'.base64.txt'),'utf8')).trim();
 if(data.length<80)throw Error('SFX missing or too small: '+n);
 b64[n]=data;}
let output=template.replace('/* SFX_PACK_PLACEHOLDER */',
 'window.CURIO_SFX='+JSON.stringify(b64)+';\nwindow.CURIO_EMBEDDED_VOICE='+JSON.stringify(narrationB64)+';\nwindow.CURIO_CAPTIONS='+JSON.stringify(captions)+';\nwindow.CURIO_GEO='+JSON.stringify(geo)+';')
 .replace('/* MOTION_CODE_PLACEHOLDER */',motion+'\n'+director);
if(output.includes('PLACEHOLDER')||!output.includes('function exportFilm')||!output.includes('const CAPTION_CUES'))throw Error('Invalid film build');
await mkdir('dist/samoa-2011',{recursive:true});
await writeFile('dist/samoa-2011/Curio_Bureau_Samoa_Vox_Editorial.html',output);
console.log('Built self-contained Curio Bureau documentary:',output.length,'characters, captions',captions.length,'country shapes',geo.length,'original Drive sounds',names.length);
