import json
def load(assets):
 land=json.loads((assets/'land.json').read_text());sj=None
 def inside(point,ring):
  x,y=point;result=False
  for a,b in zip(ring,ring[1:]+ring[:1]):
   if (a[1]>y)!=(b[1]>y) and x<(b[0]-a[0])*(y-a[1])/(b[1]-a[1])+a[0]:result=not result
  return result
 for g in land:
  for poly in [g['coordinates']] if g['type']=='Polygon' else g['coordinates']:
   if inside((-123.07,48.53),poly[0]) and not any(inside((-123.07,48.53),h) for h in poly[1:]):sj={'type':'Polygon','coordinates':poly}
 if sj is None:raise ValueError('San Juan missing from sourced geometry')
 return {'land':land,'san_juan':sj,'channels':json.loads((assets/'channel_paths.json').read_text()),'timing':json.loads((assets/'timing.json').read_text())}
