/** License-verified CC-BY Niagara Falls documentary photography.
 * Attribution: "American Falls, Niagara Falls", Bob Linsdell, CC BY 2.0.
 * Cropped and visually graded in the original Curio Bureau animation.
 * Source: https://commons.wikimedia.org/wiki/File:American_Falls,_Niagara_Falls_(470587)_(9447240371).jpg
 */
import {mkdir,writeFile,stat} from 'node:fs/promises';
import {createHash} from 'node:crypto';
const name='American_Falls,_Niagara_Falls_(470587)_(9447240371).jpg';
const hash=createHash('md5').update(name).digest('hex');
const url='https://upload.wikimedia.org/wikipedia/commons/'+hash[0]+'/'+hash.slice(0,2)+'/'+encodeURIComponent(name);
const r=await fetch(url,{headers:{'User-Agent':'CurioBureauDocumentary/1.0 (editorial creative commons reuse)'},signal:AbortSignal.timeout(90000)});
if(!r.ok)throw Error('CC licensed waterfall photograph download failed '+r.status+' '+url);
const raw=Buffer.from(await r.arrayBuffer());
if(raw.length<50000||raw[0]!==0xff||raw[1]!==0xd8)throw Error('Photograph appears invalid (JPEG)');
await mkdir('dist/niagara-1969',{recursive:true});
await writeFile('dist/niagara-1969/waterfall-photograph.jpg',raw);
console.log('Verified CC BY waterfall photograph',raw.length,'bytes',url);
