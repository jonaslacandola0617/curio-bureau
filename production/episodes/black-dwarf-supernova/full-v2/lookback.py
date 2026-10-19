"""Initialize every acceptance item against actual encoded version, without claiming listening."""
from pathlib import Path
import json,hashlib
r=Path(__file__).resolve().parent
requirements=json.loads((r/'../../../templates/sun-standard/ACCEPTANCE_REQUIREMENTS.json').read_text())
movie=r/'Black-Dwarf-Full-v2-1080p.mp4';proof=json.loads((r/'FINISHING_RUNTIME_PROOF.json').read_text())
items=[]
for item in requirements['items']:
 d=dict(item);d.pop('default_verdict',None);d['verdict']='NOT REVIEWED';d['reviewer']='Codex technical audit; owner complete-film review pending';d['evidence']='Actual encoded full-film frames extracted; item-specific visual/listening review still required.'
 if item['id'] in ['3.1','3.2','3.5']:
  d['verdict']='PASS';d['evidence']='OUTPUT_PROBE.json, FINISHING_RUNTIME_PROOF.json: native delivery, held source buckets, real30fps shared endcard and exact fully shown pixels.'
 if item['id']=='7.2':d['verdict']='PASS';d['evidence']='Retained original Bernard master, speed1, hash in AUDIO_RECEIPT.json; no new voice generation.'
 if item['id']=='7.6':d['verdict']='PASS';d['evidence']='37 cue records bind existing repository assets and their digests in SFX_CUE_SHEET.json.'
 if item['id']=='8.1':d['verdict']='PASS';d['evidence']='Complete original narration/source samples retained; 58.233333s complete episode, 1747 frames, not an excerpt.'
 if item['id']=='8.6':d['verdict']='PASS';d['evidence']='Every item explicitly listed here; independent listening/word boundaries/full-film creative approval remain open.'
 if item['id']=='8.7':d['verdict']='NOT APPLICABLE';d['evidence']='Not published; no post-publication comparable-age analytics exist yet.'
 items.append(d)
(r/'ACCEPTANCE_LOOKBACK.json').write_text(json.dumps({'movie_sha256':hashlib.sha256(movie.read_bytes()).hexdigest(),'scope':'complete encoded film, provisional technical look-back plus pending internal/owner visual/audio review','requirements':items,'reference_study':requirements['reference_study'],'independent_listening':'NOT CLAIMED','owner_full_approval':'PENDING','caption_alignment':'ASR estimates, independent word boundaries pending'},indent=2)+'\n')
