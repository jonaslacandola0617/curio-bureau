from pathlib import Path
import subprocess,json,hashlib,sys
r=Path(__file__).resolve().parent
records=[]
for name in sys.argv[1:]:
 p=r/'chunks'/name
 probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-count_frames','-show_entries','stream=width,height,codec_name,pix_fmt,r_frame_rate,nb_read_frames','-of','json',str(p)]))['streams'][0]
 parts=name.removesuffix('.mkv').split('-');start,end=map(int,parts[1:]);count=end-start+1
 assert probe['width']==1080 and probe['height']==1920 and int(probe['nb_read_frames'])==count
 record={'file':name,'start_frame':start,'end_frame':end,'count':count,'source_commit':'30cea6213c2d5a6005c8595ce1e8ddb21aaccdf2','sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size,'probe':probe,'lossless':'libx264rgb CRF0 / RGB24; source alpha opaque','archive_status':'LOCALLY_VERIFIED'}
 (r/'chunks'/(name+'.json')).write_text(json.dumps(record,indent=2)+'\n');records.append(record)
print(json.dumps(records,indent=2))
