# 08 — AUDIO, SOUND EFFECTS, SCORE & CENTER-CAPTION BIBLE
## Why the audio standard is no longer discretionary
At -37 dBFS / minimum 0.85s, Episode 004's *isolated natural voice* contains seven long silences: 4.62–8.16 (3.54s), 13.03–17.15 (4.11s), 25.82–30.20 (4.38s), 33.79–39.16 (5.37s), 47.65–51.16 (3.51s), 58.52–62.16 (3.64s) and 71.96–75.00 (3.04s). Episode 005 source logs independently show 2.86–5.12s gaps across seven preallocated scenes. Episodes 006 and 007: **zero** intervals exceeding 0.85s under the same threshold on available voice WAVs, with measured clip boundary gaps ~0.25–0.38s. These are reproducible technical findings, not subjective impressions. Detection depends on threshold and cannot replace critical listening.

## 1. Voice director's standard
- Natural, intelligible documentary storytelling in which astonishment is earned; not hyperactive, synthetic or breathless.
- Approve scripted pronunciation of place names and individuals, establish pronunciation reference voice, listen at normal speed.
- Intro opening word must be present by first visual action; first 3 seconds contain one clear complete idea.
- Record/assemble all spoken lines into ONE unpadded master sequence; trim leading/trailing quiet room from individual clips, preserve ~0.12–0.55s natural breath, never preassign empty scene slots.
- Any unexpected **>0.85s** speech silence editorial FAIL; any **>1.20s** narration gap between passages RELEASE FAIL, even with music; intentional >0.85s pauses need creative-director signoff and animated action that continues story (and may still fail release by user standard).
- Final word to video end **0.8–1.8s** normally. A 5-second voice-free static masthead is prohibited.
- Never rate-speed/time-stretch voices to solve a sync error. If VO overruns, rewrite/rerecord or extend visual mechanism meaningfully and adjust timeline.

## 2. Mechanical speech-gap QC
Decode voice stem to 48k WAV; use:

```bash
ffmpeg -i voice.wav -af 'silencedetect=noise=-37dB:d=0.85' -f null - 2>voice_silence.txt
```

Compute every gap from actual decoded signal and merge with per-clip measured true bounds. Also inspect thresholds −30dB/−42dB when room noise could mask speech offset; normal speech pauses can show lower-level breaths/noise so include listening. Export machine-readable `voice_gap_QA.json` with clip ID, spoken start/end, gap to next speech, scene ID, intended pause reason, max gap and final tail. Fail build if empty report, if a scene keeps a fixed overlong slot, or if any policy threshold exceeded.

## 3. Audio bus architecture
| Bus | Content | Audio-design standard | Test |
|---|---|---|---|
| VOICE | approved narrator | up-front, natural, lightly de-essed; center stable | headphones + phone, every word |
| MUSIC | recorded/licensed evolving score | actual melody/harmony/harmonic rhythm and emotional arc, not buried sine pad | audible across dialogue gaps at phone volume |
| AMBIENCE | grounded location | scene-accurate street/water/earth/construction bed with spatial texture | spatial movement matches camera environment |
| DETAIL SFX | jack ratchet, ripples, drops, H sign clicks | clear transient with causal visible event | expected ±100–200ms trigger window |
| IMPACT | controlled rupture, collapse, steel fracture | intense but physically plausible and not over-compressed | no clipped bass or generic hit on every cut |
| TRANSITIONS | page, object, camera switch | optional, only when object moves/cut needs editorial signal | remove if transition is already clear |
| MASTER | sum with ducking and limiter | approximately -14 to -12 LUFS, ≤-1 dBTP, 48k stereo | measure actual delivered AAC/Opus |

Original score should use 3–4 clearly differentiated harmonic sections. Example Chicago: dampened felt piano + bowed strings → tentative click/rattle → steady ratchet-driven percussion at synchronized screw motif → wider harmonic arrival → reduced ending theme. Example Boston: ominous metal drones and documentary strings, pressure accent, sudden drop on consequence, restrained human-stakes coda. Avoid identical template soundtrack across all seven historical subjects.

## 4. Recorded effects vs synthesis
Inventory actual Curio Bureau Drive SFX and each delivered episode manifest before mix. Track `filename / owner / catalog URL / license / transformations / scene trigger / scene time / gain / pan`. Actual recorded effects are preferred for culturally and physically grounded sounds. A synthesized wave/ratchet is permitted only if it passes listening and provenance statements; do not falsely name it a field recording.

**Episode examples:** 004 reported recorded water/rumble/debris clips; check Freesound individual reuse license. 007 included original procedural Foley and a rumble source in source package; verify clip rights before publication. All sound must be inspected at comparable loudness to voice; a measurable stem is not necessarily audible or well-placed.

## 5. Caption identity and accessibility
- Exact font: Manrope 700/800; approximately 42–55px at logical 1080×1920, rendered vector-sharp at 2160×3840.
- Short, natural phrases one or two lines; no wide opaque dark banner across the lower third. Use transparent/low-visual-weight shaped support only where background readability demands.
- **Primary safe band:** vertical **42–58%** of visible picture; nominal y=1613–2227 native 4K. Caption midpoint variable based on scene, but always clear of app UI and main mechanism; recompose shot before moving caption into bottom UI.
- Horizontal default center; evidence panels and hero mechanics strategically above/below. On shots with centered machinery, create a designed inactive inset/negative-space slot for the phrase.
- Actual final spoken word boundaries must drive SRT and burned-in text. Edge TTS service sometimes emits zero word boundaries: **do not quietly estimate cues and declare final**. Use forced aligner (whisperX/MFA or other tested alignment) and manually check against recorded final voice.
- Regression suite overlays realistic TikTok right buttons/bottom profile and YouTube Shorts bottom info/right controls on representative **encoded MP4 and WebM frames**; FAIL on clipping, overlap, occlusion or unreadability at ~216px phone width.
- Image remains caption-clean when captions absent for alternate platform localization if practical. SRT delivered alongside burned captions.

## 6. Actual output verification
1. Export mix and voice WAV separately; measure the speech QA report first.
2. Master music/SFX on audio timeline anchored to narration; inspect SFX timing as visible object triggers.
3. Encode both H.264/AAC MP4 and VP9/Opus WebM at true native 4K.
4. Decode compressed audio from BOTH outputs and listen to random phrase joints + beginning/mid/end; use `ebur128`/`loudnorm` for measured report and true-peak metering.
5. Output alignment report includes caption onset error per phrase, video and audio duration difference, and a count of overlapping UI captions.
6. Require signed creative listening pass: compelling music, sound specificity, nonrobot voice, transitions with natural breath, and no cut-off ending.