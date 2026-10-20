from pathlib import Path
r=Path(__file__).resolve().parent;o=r.parent/'2026-10-20-four-original-tests'
s=(o/'render.cjs').read_text().replace("A=path.join(R,'assets')","A=path.join(R,'../2026-10-20-four-original-tests/assets')").replace('async function setup(){','async function setupBase(){')
s=s.replace("const TOPICS=",(r/'scenes-v2.cjs').read_text()+'\nconst TOPICS=')
s=s.replace("foot.forEach((s,i)=>text(s,65,1790+i*44,23,darkType?'#455761':C.grey));",'')
s=s.replace("ORIGINAL VISUAL TEST ","REBUILT VISUAL TEST ").replace('y=918,h=',"y=(id==='02-diomede'?1000:932),h=")
s=s.replace('[0,1.6,2.8,3.8,4.8,5.8,6.8,7.8,8.5,9.4,10.5,11.8]','[0,.8,1.6,2.4,3.2,4,4.8,5.2,5.5,6.4,7.2,8.2,8.6,9.4,10.5,11.8]')
s=s.replace("let darkType=id==='02-diomede'","let darkType=false")
(r/'render.cjs').write_text(s)
