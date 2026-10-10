import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {resolve} from 'node:path';
const base='films/centralia-1962/';
const root=base+'studio/';
const template=await readFile(resolve(root,'film.template.html'),'utf8');
const motion=await readFile(resolve(root,'motion.js'),'utf8');
const director=await readFile(resolve(root,'director.js'),'utf8');
const captions=JSON.parse(await readFile('dist/centralia-1962/captions.json','utf8'));
const geo=JSON.parse(await readFile('dist/centralia-1962/geography.json','utf8'));
const narration=(await readFile('dist/centralia-1962/narration-embedded.mp3')).toString('base64');
if(captions.length<35||geo.length<8||narration.length<100000)throw Error('Cannot produce Centralia film: subtitle/geographic/audio assets missing');
const names=['sweep','arrow','click','type','fast','riser','popup','cinematic','chime','tick','rumble','debris','bass','pulse'];
const fx={};
for(const name of names){const b=(await readFile(base+'assets/sfx/'+name+'.base64.txt','utf8')).trim();if(b.length<400)throw Error('Sound missing '+name);fx[name]=b}
let html=template.replace('/* SFX_PACK_PLACEHOLDER */',
 'window.CURIO_SFX='+JSON.stringify(fx)+';\nwindow.CURIO_EMBEDDED_VOICE='+JSON.stringify(narration)+';\nwindow.CURIO_CAPTIONS='+JSON.stringify(captions)+';\nwindow.CURIO_GEO='+JSON.stringify(geo)+';')
.replace('/* MOTION_CODE_PLACEHOLDER */',motion+'\n'+director);
if(html.includes('SFX_PACK_PLACEHOLDER')||html.includes('MOTION_CODE_PLACEHOLDER')||!html.includes('const QA_C='))throw Error('Centralia film bundle invalid');
await mkdir('dist/centralia-1962',{recursive:true});
await writeFile('dist/centralia-1962/Curio_Bureau_Centralia_Editorial.html',html);
console.log('CENTRALIA HTML built:',html.length,'chars',captions.length,'captions',geo.length,'US state polygons',names.length,'real Drive sounds, embedded voice');
