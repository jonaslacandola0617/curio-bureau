# Curio production engine v1

Working extraction of the approved Pig War implementation, not a new creative Bible. Shared browser functions preserve the existing pixel behavior. Original episode source and published movies remain untouched.

## Run

From the repository root, substitute the private project directory containing `assets/` and `baseline/`:

```bash
python3 production/engine/curio.py check --episode production/episodes/pig-war --project /absolute/private/pig_war_full --out /absolute/private/build
python3 production/engine/curio.py preview --episode production/episodes/pig-war --project /absolute/private/pig_war_full --out /absolute/private/build
python3 production/engine/curio.py render --episode production/episodes/pig-war --project /absolute/private/pig_war_full --out /absolute/private/build
python3 production/engine/curio.py package --episode production/episodes/pig-war --project /absolute/private/pig_war_full --out /absolute/private/build
```

`plan --profile native` reports `render`, `remux` or `reuse` without encoding. `audio` runs the episode's deterministic audio director through the shared decode/cue/normalization utilities. Voice generation is never implicit. `render --start 9.3 --seconds 1` creates explicitly named short native `Smoke` outputs; it never records a full-film render cache. `preview` without a range renders the complete 1080p film. Browser Studio opens directly from disk, without a server or network assets.

Dependencies: Python (NumPy/SciPy for audio), FFmpeg/ffprobe, Node, Playwright and Chromium. Set `CURIO_CHROME` or use `--chrome`; normal Chromium executables are detected. The Work runtime's Node/modules are used when available; ordinary Node/Playwright also work. Do not call external image/speech/SFX services during routine rebuilds.

## Shared versus authored

`browser/` owns runtime buffers, easing/drawing utilities, typography, captions, grain/material finishing, native focus, player and explicit HTML/CSS templates. `audio.py` owns sample decode, placement and mastering utilities. `tools/render.cjs` renders lossless PNGs at fixed frame times. `curio.py` validates inputs, builds, tracks dependencies, encodes/remuxes and packages.

The episode owns data preparation, sourced geography, artwork registration, composition, objects, choreography, source labels, narration events, score direction and cue selection. `episode.json` declares those inputs. Required adapter functions: `renderScene(t)`, `furniture(t)` and optional `episodeMotionState(t)`. The supported v1 frame profile is 1080×1920 logical, native ×2, 30 fps. Materials use named `paper` and `ink` image slots. Data includes duration, phrase captions and episode-owned events. This is intentionally an extraction, not a universal declarative storyboard language.

## Cache correctness

Visual fingerprint includes engine/build code, episode config/code/data, images, pinned fonts and timing. Audio fingerprint is the exact mixed WAV. Output hashes prevent trusting missing/corrupted cache files.

- Identical fingerprints and outputs: reuse.
- Same visual fingerprint, changed mix: copy encoded video packets and replace audio in MP4/WebM/download MP4.
- Timing, artwork, type or animation change: render visuals again.
- The audio stage has a separate fingerprint for its script, shared audio utilities, stems, cues and timing.

Cache granularity is **whole visual render versus audio**, not per-shot frames. Per-shot transition dependencies, raw-frame transfer optimization and automated shot collision analysis are later extensions. v1 does not claim to shorten an uncached full native render; its gain is preventing unnecessary repeated work.

## Outputs and checks

Native `render` encodes H.264 CRF15/AAC 320k and VP9 CRF22/Opus 256k directly from the same native PNG frame stream. It also produces a CRF20 download MP4 with a runtime-based bitrate ceiling and an actual <512 MiB check. No 1080p upscale is used. Browser export is supported in the default 1080p studio; `?scale=2` is for native production capture and safely directs users back to standard preview for browser export. Browser exports are synchronized review copies; cadence depends on the device, and they do not replace the authoritative fixed-cadence masters.

Input checks include pinned font hashes, asset presence, caption order/bounds in time, 48k stereo PCM and matching audio/timeline duration. Encode checks independently validate resolution, codecs, frame count, duration, stereo/rate and full decode. These checks do **not** certify factual/rights review, exact spoken word alignment, caption/UI visibility, perceptual SFX quality, loudness or creative approval. Preserve the Bible's complete release gates and run full episode-specific encoded QA before release; never promote a technical pass to FINAL MASTER.

The WAV embedding contract currently requires a canonical 44-byte PCM16 stereo WAV. The audio stage produces it. Unexpected headers fail explicitly rather than being misread.

## Verification

See `VERIFICATION.json`: 22 exact native RGB checkpoints; 120 exact moving RGBA comparisons over three difficult transitions; unchanged authoritative mix and three stems; native three-format integration test; audio-remux video packet identity; cache/visual-invalidation/font-rejection checks; complete browser review recording with duration/audio validation. Sample comparisons are not a whole-film pixel certification or independent listening approval.

Private assets and generated studios/packages must never enter this public repository. `package` includes required private rebuild inputs and notices, not unrelated old assets or tutorial source pixels. The original Pig War private source bundle remains the historical baseline.
