import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {resolve} from 'node:path';
const root='films/niagara-1969/studio/',dir='dist/niagara-1969';
const template=await readFile(resolve(root,'film.template.html'),'utf8');
const motion=await readFile(resolve(root,'motion.js'),'utf8');
const director=await readFile(resolve(root,'director.js'),'utf8');
const photo=(await readFile(dir+'/waterfall-photograph.jpg')).toString('base64');
const geo=JSON.parse(await readFile(dir+'/geography.json','utf8'));
const captions=JSON.parse(await readFile(dir+'/captions.json','utf8'));
const narration=(await readFile(dir+'/narration-embedded.mp3')).toString('base64');
if(photo.length<100000||geo.length<7||captions.length<32||narration.length<100000)throw Error('Missing license-verified picture, geography, speech subtitles or narration');
const names=['sweep','arrow','click','type','fast','riser','popup','cinematic','chime','tick','debris'];
const fx={};
for(const n of names){let contents=(await readFile('films/niagara-1969/assets/sfx/'+n+'.base64.txt','utf8')).trim();if(contents.length<700)throw Error('Expected Drive SFX missing: '+n);fx[n]=contents}
let result=template.replace('/* SFX_PACK_PLACEHOLDER */',
 'window.CURIO_SFX='+JSON.stringify(fx)+';\nwindow.CURIO_EMBEDDED_VOICE='+JSON.stringify(narration)+';\nwindow.CURIO_CAPTIONS='+JSON.stringify(captions)+';\nwindow.CURIO_GEO='+JSON.stringify(geo)+';\nwindow.NIAGARA_PHOTO='+JSON.stringify(photo)+';')
 .replace('/* MOTION_CODE_PLACEHOLDER */',motion+'\n'+director);
if(result.includes('SFX_PACK_PLACEHOLDER')||result.includes('MOTION_CODE_PLACEHOLDER')||!result.includes('const nfQA'))throw Error('HTML assembly failed');
await mkdir(dir,{recursive:true});
const path=dir+'/Curio_Bureau_Niagara_1969_Editorial.html';
await writeFile(path,result);
console.log('NIAGARA BUILT',result.length,'chars',geo.length,'real states,',captions.length,'word-based caption groups,',names.length,'Drive effects, CC BY photograph');
