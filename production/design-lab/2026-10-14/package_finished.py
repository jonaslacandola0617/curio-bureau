from pathlib import Path
import zipfile
from PIL import Image,ImageDraw,ImageFont
r=Path(__file__).parent;f=r/'finished'
font=ImageFont.truetype(str(r/'browser_assets/Manrope.ttf'),20)
overview=Image.new('RGB',(1120,2060),'#101319');d=ImageDraw.Draw(overview)
for i in range(1,5):
 im=Image.open(f/f'Finished_Visual_0{i}.png');assert im.size==(1080,1920)
 im=im.resize((540,960),Image.Resampling.LANCZOS);x=10+(i-1)%2*560;y=42+(i-1)//2*1010;overview.paste(im,(x,y));d.text((x,y-30),f'0{i} / '+['Voice','Space','Light','Vision'][i-1],fill='#f5f0e7',font=font)
overview.save(f/'Finished_Four_Visuals.png')
with zipfile.ZipFile(f/'Curio_Bureau_Finished_Visuals_Source.zip','w',zipfile.ZIP_DEFLATED,compresslevel=5) as z:
 z.writestr('design_lab/deliverables/','')
 for folder in ['browser_assets','font_notices']:
  for p in (r/folder).iterdir():z.write(p,'design_lab/'+str(p.relative_to(r)))
 for n in ['build.py','finish.py','render_finished.mjs','package_finished.py','finished_qa.json','finishing_recipe.json','boards.json','assets.lock.json']:z.write(r/n,'design_lab/'+n)
 for p in f.iterdir():
  if p.suffix!='.zip':z.write(p,'design_lab/finished/'+p.name)
