from pathlib import Path
import runpy,json
root=Path(__file__).parent
base=runpy.run_path(str(root/'build.py'))
html=base['html']
filters='''<svg aria-hidden="true" style="position:absolute;width:0;height:0;overflow:hidden"><defs>
<filter id="chromatic" x="-8%" y="-8%" width="116%" height="116%" color-interpolation-filters="sRGB">
<feColorMatrix in="SourceGraphic" type="matrix" values="1 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 1 0" result="red"/><feOffset in="red" dx="2.8" dy=".65" result="r"/>
<feColorMatrix in="SourceGraphic" type="matrix" values="0 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 1 0" result="cyan"/><feOffset in="cyan" dx="-2.4" dy="-.4" result="c"/><feBlend in="r" in2="c" mode="screen"/>
</filter>
<filter id="printed-ink" x="-3%" y="-8%" width="106%" height="116%" color-interpolation-filters="sRGB">
<feTurbulence type="fractalNoise" baseFrequency=".027 .095" numOctaves="2" seed="13" result="noise"/><feDisplacementMap in="SourceGraphic" in2="noise" scale=".8" xChannelSelector="R" yChannelSelector="G" result="rough"/><feGaussianBlur in="rough" stdDeviation=".18"/>
</filter>
</defs></svg>'''
css='''
.finish-grain{position:absolute;inset:0;z-index:19;pointer-events:none;mix-blend-mode:soft-light;opacity:.3;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='200'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.78' numOctaves='3' seed='27' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");background-size:230px 230px}
.finish-exposure{position:absolute;inset:0;z-index:18;pointer-events:none;background:radial-gradient(ellipse at 58% 46%,#fff4 0%,transparent 44%,#070d1870 100%);mix-blend-mode:soft-light}
.finish-dust{position:absolute;inset:0;z-index:20;pointer-events:none;opacity:.24;background:radial-gradient(ellipse 1.6px 3px at 9% 36%,#fff 99%,transparent),radial-gradient(ellipse 3px 1.2px at 87% 21%,#fff 99%,transparent),radial-gradient(ellipse 1.8px 2.5px at 58% 70%,#111 99%,transparent),radial-gradient(ellipse 2px 2px at 72% 85%,#fff 99%,transparent)}
.headline{filter:url(#printed-ink);text-shadow:.4px .35px .35px currentColor,-.25px .25px .2px currentColor}
.art > svg{filter:url(#printed-ink)}
.finish-label{box-shadow:0 3px 1px #06111c16;filter:url(#printed-ink)}
.finish-photo-overlay{pointer-events:none;mask-repeat:no-repeat;mask-position:center;mask-size:contain;-webkit-mask-repeat:no-repeat;-webkit-mask-position:center;-webkit-mask-size:contain}
.finish-chroma,.finish-focus{pointer-events:none}
body.unfinished .finish-grain,body.unfinished .finish-exposure,body.unfinished .finish-dust,body.unfinished .finish-chroma,body.unfinished .finish-focus,body.unfinished .finish-photo-overlay{display:none}
body.unfinished .headline,body.unfinished .art>svg{filter:none;text-shadow:none}
body.unfinished .finish-label{filter:none;box-shadow:none}
'''
js='''
(async()=>{
await document.fonts.ready;await Promise.all([...document.images].map(i=>i.decode()));
const arts=[...document.querySelectorAll('.art')];
for(const [index,art] of arts.entries()){
 const photos=[...art.querySelectorAll('img:not(.material)')];
 for(const [j,image] of photos.entries()){
  if(index===1&&j===0)image.style.clipPath='circle(45% at 50% 50%)';
  const baseFilter=image.style.filter||'';
  // Fringe and compound focus are copies of the actual image, registered to its parent.
  const edge=image.cloneNode();edge.classList.add('finish-chroma');edge.setAttribute('aria-hidden','true');edge.alt='';edge.style.position='absolute';
  if(!image.style.position){edge.style.left=image.offsetLeft+'px';edge.style.top=image.offsetTop+'px';edge.style.width=image.offsetWidth+'px';edge.style.height=image.offsetHeight+'px'}
  edge.style.filter=baseFilter+' url(#chromatic)';edge.style.opacity=index===2?'.62':'.92';edge.style.maskImage='radial-gradient(ellipse at 56% 49%,transparent 42%,#000 82%)';edge.style.webkitMaskImage=edge.style.maskImage;
  image.insertAdjacentElement('afterend',edge);
  const soft=image.cloneNode();soft.classList.add('finish-focus');soft.setAttribute('aria-hidden','true');soft.alt='';soft.style.position='absolute';
  if(!image.style.position){soft.style.left=image.offsetLeft+'px';soft.style.top=image.offsetTop+'px';soft.style.width=image.offsetWidth+'px';soft.style.height=image.offsetHeight+'px'}
  // Keep model, astronaut and spectral proof crisp; soften outer context only.
  const isEarth=index===1&&j===0;
  const blur=isEarth?4.5:(index===3?4:2.6);
  soft.style.filter=baseFilter+' blur('+blur+'px)';soft.style.opacity=isEarth?'.85':'.6';soft.style.maskImage=isEarth?'linear-gradient(#000,#000)':'radial-gradient(ellipse at '+(index===3?'64% 53%':'55% 49%')+',transparent 42%,#000 100%)';soft.style.webkitMaskImage=soft.style.maskImage;
  edge.insertAdjacentElement('afterend',soft);
  // Ink dots sit on photographs; the source-alpha mask keeps cutout backgrounds clean.
  const print=document.createElement('div');print.className='finish-photo-overlay';print.style.cssText=image.style.cssText;print.style.position='absolute';
  if(!image.style.position){print.style.left=image.offsetLeft+'px';print.style.top=image.offsetTop+'px';print.style.width=image.offsetWidth+'px';print.style.height=image.offsetHeight+'px'}
  print.style.filter='none';print.style.maskImage='url("'+image.src+'")';print.style.webkitMaskImage=print.style.maskImage;print.style.maskSize=image.style.objectFit==='cover'?'cover':'contain';print.style.webkitMaskSize=print.style.maskSize;
  print.style.backgroundImage='radial-gradient(#08121dcc .6px,transparent .95px)';print.style.backgroundSize='4px 4px';print.style.mixBlendMode='multiply';print.style.opacity=index===2?'.10':'.18';soft.insertAdjacentElement('afterend',print);
 }
 for(const tag of art.querySelectorAll('.label'))if(tag.style.background)tag.classList.add('finish-label');
 // Material above image stacks remains tied to print, fibre or plastic roles.
 const mats=[...art.querySelectorAll('.material')];for(const m of mats){const o=Number(m.style.opacity||1);m.dataset.unfinishedOpacity=o;m.dataset.finishedOpacity=Math.min(.8,o*1.35);m.style.opacity=m.dataset.finishedOpacity}
 for(const type of ['finish-exposure','finish-grain','finish-dust']){const layer=document.createElement('div');layer.className=type;art.querySelector('.safe').before(layer)}
}
const b=document.createElement('button');b.id='finish-toggle';b.textContent='Finishing: on';b.setAttribute('aria-pressed','true');b.onclick=()=>{const off=document.body.classList.toggle('unfinished');b.textContent=off?'Finishing: off':'Finishing: on';b.setAttribute('aria-pressed',!off);document.querySelectorAll('.material').forEach(m=>m.style.opacity=off?m.dataset.unfinishedOpacity:m.dataset.finishedOpacity)};document.querySelector('.tools').append(b);
await Promise.all([...document.images].map(i=>i.decode()));window.finishReady=true;
})();
'''
html=html.replace('</style>',css+'</style>',1).replace('<main class="gallery">',filters+'<main class="gallery">',1).replace('</html>','<script>'+js+'</script></html>')
html=html.replace('Four visual arguments.','Four finished visual tests.').replace('Static artwork for owner review. Judge image choice, composition, typography and material craft before motion. These are original design studies, not approved channel templates.','Finished static composites: stronger paper, ink and plastic, photographic print grain, selective focus, chromatic edge separation and optical shading. Compare finishing on/off; owner artwork review precedes motion.')
out=root/'finished';out.mkdir(exist_ok=True)
(out/'Curio_Bureau_Finished_Visuals.html').write_text(html)
(root/'finishing_recipe.json').write_text(json.dumps({'status':'OWNER_REVIEW_PENDING','still_only':True,'effects':{'chromatic_edge_shift_logical_px':[2.8,-2.4],'focus_blur_logical_px':{'background_earth':4.5,'eye_periphery':4,'other_periphery':2.6},'ink_contour_displacement_logical_px':.8,'ink_softening_px':.18,'local_material_gain':1.35,'film_grain_opacity':.3,'photographic_ink_dot_spacing_px':4},'preserve':'Unshifted photographic centre, factual colours, model identity and legible labels. No temporal jitter/flicker/focus hunt in stills.'},indent=2))
print('finished HTML',len(html))
