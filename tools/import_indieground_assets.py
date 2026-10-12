#!/usr/bin/env python3
"""Import the owner's licensed ZIPs to a Git-ignored local material directory.

No downloads, no uploads, no guessed substitute assets. SHA-256 verification
and an exact manifest member list prevent silent asset swaps or ZIP traversal.
"""
import argparse,hashlib,json,os,pathlib,sys,zipfile

ROOT=pathlib.Path(__file__).resolve().parents[1]
CATALOG=ROOT/'assets/visual/indieground/catalog.json'
LOCAL=ROOT/'assets/visual/indieground/local'

def digest(data):return hashlib.sha256(data).hexdigest()

def main():
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('zip_directory',type=pathlib.Path,help='Directory of your licensed Indieground ZIPs')
 parser.add_argument('--pack',action='append',default=[],help='Import only this catalog pack; repeat for several')
 args=parser.parse_args();catalog=json.loads(CATALOG.read_text())
 selected=[p for p in catalog['packs'] if not args.pack or p['id'] in args.pack]
 unknown=set(args.pack)-{p['id'] for p in catalog['packs']}
 if unknown:parser.error('Unknown packs: '+', '.join(sorted(unknown)))
 assets={};missing=[];verified=[]
 for pack in selected:
  if pack['availability']!='received':missing.append(pack['archive']);continue
  path=args.zip_directory/pack['archive']
  if not path.is_file():missing.append(pack['archive']);continue
  # Stream the archive hash; large licensed originals need not sit in memory.
  h=hashlib.sha256()
  with path.open('rb') as f:
   for block in iter(lambda:f.read(1024*1024),b''):h.update(block)
  if h.hexdigest()!=pack['archive_sha256']:raise ValueError('Archive hash mismatch: '+path.name)
  staged=[]
  with zipfile.ZipFile(path) as z:
   for item in pack['assets']:
    member=pathlib.PurePosixPath(item['member'])
    if member.is_absolute() or '..' in member.parts:raise ValueError('Unsafe ZIP member')
    info=z.getinfo(item['member'])
    if info.file_size!=item['bytes']:raise ValueError('Member size mismatch: '+item['member'])
    b=z.read(info)
    if digest(b)!=item['sha256']:raise ValueError('Member hash mismatch: '+item['member'])
    target=ROOT/item['local_path']
    if LOCAL.resolve() not in target.resolve().parents:raise ValueError('Destination outside private root')
    staged.append((target,b,item))
   # Preserve supplied authorship/terms notices beside the licensed originals.
   for member in pack.get('readme_members',[]):
    b=z.read(member);target=LOCAL/pack['id']/'notices'/pathlib.PurePosixPath(member).name
    staged.append((target,b,None))
  for target,b,item in staged:
   target.parent.mkdir(parents=True,exist_ok=True)
   if not target.exists() or digest(target.read_bytes())!=digest(b):
    temp=target.with_name(target.name+'.importing');temp.write_bytes(b);os.replace(temp,target)
   if item:assets[item['id']]={'path':item['local_path'],'sha256':item['sha256'],'width':item['width'],'height':item['height'],'mode':item['mode']}
  verified.append(pack['id'])
 LOCAL.mkdir(parents=True,exist_ok=True)
 index={'status':'LOCAL_PRIVATE_ASSETS','source_files_not_for_public_redistribution':True,'packs_verified':verified,'missing_archives':missing,'assets':assets}
 index_path=LOCAL/'IMPORT_REPORT.json';index_path.write_text(json.dumps(index,indent=2))
 print(json.dumps({'packs_verified':len(verified),'image_files_verified':len(assets),'missing_archives':missing,'report':str(index_path.relative_to(ROOT))},indent=2))
 return 0

if __name__=='__main__':
 try:sys.exit(main())
 except (ValueError,zipfile.BadZipFile,KeyError) as e:print('Import failed:',e,file=sys.stderr);sys.exit(1)
