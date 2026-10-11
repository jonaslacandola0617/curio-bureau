# Curio Bureau 009 — Release QA ledger (live, evidence qualified)
**Do not label FINAL MASTER without independent real-artifact QA and creative audio signoff.**

## Passes before full render
- Nine visually differentiated animated scenes and 27 distinct sampled frame states; actual Playwright screenshot at true 2160×3840 each.
- Actual Playfair Display/Manrope font face loading verified in Chrome PRIVATE renderer; exported user project contains no raw font file.
- Revised composition moved tank, speaker truck and radio instrument away from y 42–58% center caption band. Static/motion-sample contact inspection reviewed.
- Actual Edge TTS narration A/B auditions produced for opening and twist: GuyNeural and AndrewNeural at different style/rate/pitch. Chosen GuyNeural for the candidate; creative listening NOT independently done.
- 16 cue events loaded from 50 first-party synthesized SFX library with exact path and SHA256 in generated audio_cue_sheet.csv.
- Recorded clip-to-clip gap maximum 0.28s in successful audio preflight, with duration approx 65.2s total. Isolated waveform silence detection generated in workflow; examine before FINAL.
- Historical source truth from Army / WWII Museum; no authentic 1945 recorded sound/photo used or falsely described.
- Preflight GitHub Actions run: https://github.com/jonaslacandola0617/curio-bureau/actions/runs/38134405677
- Full native-4K render GitHub Actions run: https://github.com/jonaslacandola0617/curio-bureau/actions/runs/38134568599

## Must still pass
- Both actual encoded H264/AAC MP4 and VP9/Opus WebM dimensions, frame rate, decoded last frames and sound tracks (do not assume passed until job finishes).
- Full subjective real-time film watch, especially the weakest middle mechanism shots, repeated top text, readable captions at phone size and scene transitions.
- Human headphone/mobile audition of final encoded mixed tracks and two opening A/B voice performances, final expressive narration performance verdict. Do not infer human emotional satisfaction from generated A/B audio files.
- Actual spoken-word subtitle timing; current SRT uses verified **phrase** start/end from recorded clips but WordBoundary events returned zero, so per-word synchronization is not certified.
- Original score use of FluidR3 instrument soundfont licensing checked for intended distribution. Score notes are original but the sample-library terms should be confirmed.
- Final source rights and nondeceptive reconstruction labels, no fake historical recordings.

## Verdict
**NATIVE 4K REVIEW CANDIDATE (not FINAL).** Pending full moving picture/audio, word-alignment, copyright review and user's artistic acceptance.
