from pathlib import Path
import json,time,subprocess
r=Path(__file__).parent.resolve()
while True:
 try:
  if json.loads((r/'recovery.json').read_text()).get('durable_frames')==1089:break
 except (FileNotFoundError,json.JSONDecodeError):pass
 time.sleep(3)
for name in ['encode.py','qa.py','package.py']:subprocess.run(['python3',str(r/name)],check=True)
subprocess.run([__import__('os').environ['CODEX_PRIMARY_RUNTIME_NODE'],str(r/'test_player.cjs')],check=True)
print('FINAL_FILES_VERIFIED',flush=True)
