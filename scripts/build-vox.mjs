import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {resolve} from 'node:path';
const root='films/samoa-2011/vox/';
const template=await readFile(resolve(root,'film.template.html'),'utf8');
const motion=await readFile(resolve(root,'motion.js'),'utf8');
const names=['sweep','arrow','click','type'];
const b64={};
for(const n of names)b64[n]=(await readFile(resolve('films/samoa-2011/assets/sfx/',n+'.base64.txt'),'utf8')).trim();
let output=template.replace('/* SFX_PACK_PLACEHOLDER */','window.CURIO_SFX='+JSON.stringify(b64)+';')
 .replace('/* MOTION_CODE_PLACEHOLDER */',motion);
if(output.includes('PLACEHOLDER')||!output.includes('function exportFilm'))throw new Error('Invalid film build');
await mkdir('dist/samoa-2011',{recursive:true});
await writeFile('dist/samoa-2011/Curio_Bureau_Samoa_Vox_Editorial.html',output);
console.log('Built self-contained original Vox-inspired film:',output.length,'characters');
