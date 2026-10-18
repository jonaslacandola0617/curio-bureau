from pathlib import Path
import json,subprocess,hashlib
r=Path(__file__).resolve().parent
voice=r/'audio/voice-original.mp3';wav=r/'audio/voice-edit.wav';mp3=r/'audio/voice-review.mp3'
subprocess.run(['ffmpeg','-v','error','-y','-i',str(voice),'-filter_complex','[0:a]atrim=end=26.05,asetpts=PTS-STARTPTS[a];[0:a]atrim=start=26.70,asetpts=PTS-STARTPTS[b];[a][b]concat=n=2:v=0:a=1,aresample=48000,pan=stereo|c0=c0|c1=c0[out]','-map','[out]','-c:a','pcm_s24le',str(wav)],check=True)
subprocess.run(['ffmpeg','-v','error','-y','-i',str(wav),'-c:a','libmp3lame','-b:a','128k',str(mp3)],check=True)
probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration:stream=sample_rate,channels','-of','json',str(wav)]))
gaps=subprocess.run(['ffmpeg','-hide_banner','-i',str(wav),'-af','silencedetect=noise=-37dB:d=0.85','-f','null','-'],text=True,stderr=subprocess.PIPE).stderr
(r/'qa/voice_silence.txt').write_text(gaps)
(r/'qa/AUDIO_PREP.json').write_text(json.dumps({'source_sha256':hashlib.sha256(voice.read_bytes()).hexdigest(),'edited_wav_sha256':hashlib.sha256(wav.read_bytes()).hexdigest(),'probe':probe,'silent_cut':[26.05,26.70],'source_measured_quiet':[25.8604,26.9697],'removed_seconds':.65,'time_stretch':False,'remaining_detected_gaps_over_085s':[s for s in gaps.splitlines()if 'silence_start' in s],'closing_ASR_text':'We’d spend those final minutes living in the Sun’s past.','independent_listening':'NOT CLAIMED; owner can audition full narration in review HTML','word_alignment':'New local ASR run on edited audio; verification still needed before final captions'},indent=2)+'\n')
print('Rebuilt natural-speed edited narration; saved measured gap QA.')
