from pathlib import Path
from PIL import Image,ImageDraw
r=Path(__file__).resolve().parent;ts=[2.5,2.7,2.9,3.16,3.4,3.88,4.2,4.9,5.1,6.45,6.6,6.9,7.4,8.4,10.3,12.2,13.6]
b=Image.new('RGB',(1620,1570),'#0d1c2b');d=ImageDraw.Draw(b)
for i,t in enumerate(ts):
 im=Image.open(r/'proof'/f'encoded_{t}.png');x=(i%6)*270;y=(i//6)*520;b.paste(im,(x,y));d.text((x+12,y+490),f'{t:.2f}s · encoded 4K MP4',fill='#f5f0e7')
b.save(r/'Cold_Metal_R2_Review.jpg',quality=92)
