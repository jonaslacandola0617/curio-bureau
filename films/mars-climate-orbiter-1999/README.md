# CURIO BUREAU — Episode 008: The Spacecraft Lost in Translation

**Status:** Render candidate workflow; NOT a certified final master.
**Source branch:** `film/mars-climate-orbiter-1999`. Governing standard: [Creative and Production Bible v1.2](../../production/CURIO_BUREAU_MASTER_PRODUCTION_BIBLE.md).

## Visual concept
Nine original animated 2D/2.5D scenes driven by the recorded spoken phrase timeline. The signature motion system tracks a spacecraft entering Mars occultation, follows an Earth-to-Mars route, descends into the ground SOFTWARE unit interface, magnifies small-thruster behavior, and confronts the orbit-altitude discrepancy before the missing radio signal.

Artwork combines a credited NASA/USGS 4798px Mars Viking mosaic with original vector spacecraft assemblies, perspective props, depth layers, technical diagrams, type, and a masked investigation graphic. No historic crash/fireball is invented.

## Production source
- `src/studio_template.html`: original 2160×3840 deterministic Canvas and playback/scrubbing/WebM convenience studio, nine animated scene implementations.
- `src/build_audio.py`: neural recorded speech in natural phrase chunks, measured transitions, phrase-boundary SRT, original sampled-instrument MIDI score and designed Foley.
- `src/render.py`: Chromium native-4K PNG frames streamed losslessly to FFmpeg H264/AAC master and VP9/Opus variant; actual ffprobe & tail checks; end-user studio/asset ZIP.
- `.github/workflows/ep008-mars-film.yml`: the remote reproduction recipe.
- `docs/RESEARCH_LOCK_AND_RIGHTS.md`: three candidate stories, fact checking and licensing.
- `docs/shot_fingerprint.csv`: nine shots' unique composition and motion mechanisms.

## Permanent brand safeguards
Playfair Display headlines; Manrope captions, maps/labels. Navy #0D1C2B, ivory #F5F0E7, gold #C8A26B and coral #D57864, plus NASA/Mars subject colors. Captions 42–58% vertical center, true measured speech clips, no extended narration gaps. Both MP4 and WebM must contain actual native 2160×3840 30fps pictures with 48k stereo audio.

## Important QA limitations
1. The nine shots need artistic approval based on actual *moving* encoded results. A functioning renderer is NOT proof of Vox-level polish.
2. Caption clip boundaries are derived from trimmed audio; there is no promise of per-word forced alignment. Inspect actual spoken timing.
3. A sampled-instrument score is original composition but its final timbre, volume and mix need phone/headphone listening tests; verify soundfont terms before monetized publication.
4. The final fate is not confirmed photographed: there is no cinematic explosion. The illustration is explicitly explanatory.
5. These files on GitHub are the source; the published videos are generated as separate workflow artifacts, not binary commits.
