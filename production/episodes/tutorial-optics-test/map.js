const project=(lon,lat)=>[(lon+123.03)*665,(48.60-lat)*1000];
function screen(ll,c){let p=project(...ll);return[540+(p[0]-c.x)*c.s,820+(p[1]-c.y)*c.s];}
function geometryPath(g){let p=new Path2D();let polygons=g.type==='Polygon'?[g.coordinates]:g.coordinates;for(const polygon of polygons)for(const ring of polygon){ring.forEach((ll,i)=>{let q=project(...ll);i?p.lineTo(...q):p.moveTo(...q);});p.closePath();}return p;}
const land=DATA.land.map(geometryPath),sjPath=geometryPath(DATA.san_juan);



const atlasCache=new Map();
function atlas(c){ctx.fillStyle=C.water;ctx.fillRect(0,0,W,H);ctx.save();ctx.translate(540,820);ctx.scale(c.s,c.s);ctx.translate(-c.x,-c.y);
 ctx.lineWidth=.6/c.s;ctx.strokeStyle='#758b8945';
 for(let lon=-124;lon<=-122;lon+=.2){let a=project(lon,47.7),b=project(lon,49.3);line([a,b],'#758b8945',.6/c.s);}for(let lat=47.8;lat<=49.2;lat+=.2)line([project(-124.1,lat),project(-122,lat)],'#758b8945',.6/c.s);
 for(const p of land){ctx.save();ctx.translate(1.5/c.s,2/c.s);ctx.globalAlpha=.18;ctx.fillStyle=C.ink;ctx.fill(p,'evenodd');ctx.restore();ctx.fillStyle=C.land;ctx.fill(p,'evenodd');ctx.strokeStyle='#355a59';ctx.lineWidth=1.1/c.s;ctx.stroke(p);}
 ctx.globalCompositeOperation='multiply';ctx.globalAlpha=.88;ctx.fillStyle=paperPattern;ctx.fillRect(-1600,-1600,3200,3200);ctx.globalAlpha=.17;ctx.fillStyle=inkPattern;ctx.fillRect(-1600,-1600,3200,3200);ctx.restore();
 const labels=[['VANCOUVER',[-123.6,48.67],0],['ISLAND',[-123.6,48.63],0],['MAINLAND',[-122.40,48.65],0],['ORCAS',[-122.89,48.69],0],['LOPEZ',[-122.88,48.46],0],['SHAW',[-122.96,48.57],0],['STRAIT OF JUAN DE FUCA',[-123.11,48.18],0]];
 ctx.font='600 23px Manrope';ctx.fillStyle='#324d50';ctx.textAlign='center';for(const [name,ll] of labels){let p=screen(ll,c);ctx.fillText(name,...p);}ctx.textAlign='left';
}
function traceCourse(name,c,u,color){if(u<=0)return;let pts=DATA.channels[name].map(ll=>screen(ll,c));let lens=[0];for(let i=1;i<pts.length;i++)lens.push(lens.at(-1)+Math.hypot(pts[i][0]-pts[i-1][0],pts[i][1]-pts[i-1][1]));let cut=u*lens.at(-1),out=[pts[0]];
 for(let i=1;i<pts.length;i++){if(lens[i]<=cut)out.push(pts[i]);else{let k=clamp((cut-lens[i-1])/(lens[i]-lens[i-1]));out.push([mix(pts[i-1][0],pts[i][0],k),mix(pts[i-1][1],pts[i][1],k)]);break;}}
 // The thin line is a sourced schematic. Its geographic center does not jitter.
 ctx.save();ctx.lineCap='round';CurioFinishing.drawInkStroke(ctx,out,{color,width:6,bleedPx:1,bleedAlpha:.25});ctx.restore();
}
