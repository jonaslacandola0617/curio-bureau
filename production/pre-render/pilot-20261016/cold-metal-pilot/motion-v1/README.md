# Cold Metal — moving passage v1

**13.9-second, 1080×1920 / 30fps review. 417 frames. OWNER MOTION / LISTENING REVIEW PENDING.** This is the representative sequence authorized after owner art approval, not a complete native 4K film.

The hand approaches a recognizable spoon, makes contact, and the selection leads into a moving printed heat-flow explanation. A registered blurred cut reveals the paired metal/wood comparison. The actual complete Bernard source determines the available duration; the final phrase and about 0.95s of source tail space are preserved. Photographic assets are original generated illustrations; arrows are qualitative, not measured heat ratios.

## Preventing forgotten finishing

The adopted contract already required finishing. The implementation now supplies a reusable [short checklist](../../../../engine/FINISHING_CHECKLIST.md), `finishing_audit.py`, shot-specific `FINISHING_COVERAGE.json` and actual rendered proof. A new proof run invalidates its predecessor and records exact picture-source hashes. Preflight independently checks those bindings, including a negative drift test. The capture command calls preflight before FFmpeg; stale source, missing evidence or incomplete mixed-audio bytes stop it. Essential material texture and moving grain cannot be silently excluded.

The original rendered effect proof took about **13 seconds** in this environment; the updated run, including the hidden-panel regression, took **16.775 seconds**. All eleven independently toggled picture effects changed actual pixels. Grain changed over a held source with other film variations disabled; repeating the same time was byte-identical. Peripheral focus changes exceeded changes in the selected region; blur returned to zero for the settled hold. Opaque caption pixels were identical with finishing toggled. The actual encoded phone frames retain visible texture. These are execution checks, not an artistic resemblance score.

Coverage: source-local material/fibers and photo varnish; moving grain; transient camera/transition blur; selected-detail focus and the same-field surround shading; brief focus hunt; restrained chromatic separation; mechanical jitter; exposure shift; local ink bleed; anchored edge boil; protected captions. The exact full-film ending is deliberately **not included or certified** in this isolated passage. It must be restored and tested in the completed film.

## Actual fixes and limits

The first native adapter exposed two issues before encoding: deferred canvas buffer reuse lost picture opacity, and a transformed gradient mask did not match browser behavior. The local adapter now snapshots native buffers and uses the shared explicit spatial FocusPass for blur/shading. Encoded-frame inspection also caught inherited-alpha leaks in an unrevealed panel; the image layers now inherit panel opacity, and a hidden-panel on/off pixel test blocks that regression. Legacy browser finishing code is untouched. Closed, fully opaque frames and selected/peripheral behavior are tested.

An incomplete intermediate WAV was caught before delivery. The original narration and stems were intact. The final mix is written as complete canonical PCM, and preflight now checks its real frame count and byte length. The earlier draft movies received corrected audio through stream-copy remux; H.264 and VP9 packet hashes stayed unchanged for that repair. No picture frames were recaptured to correct audio. The later panel-opacity visual fix required a new picture capture; final movie fingerprints are recorded separately in OUTPUT_QA.json. See AUDIO_REMUX_QA.json and NARRATION_TAIL_QA.json.

MP4 and WebM independently passed codec/dimension/frame-count/full-decode/audio-duration checks. Final encoded loudness and true peak are in OUTPUT_QA.json. No headphone/phone human listening pass or owner motion approval is fabricated. Captions are phrase estimates informed by measured pauses; no independent word alignment is claimed.

This preview's WebM is a VP9/Opus review transcode from the H.264 review picture, not an independently encoded native master. The final 4K MP4/WebM workflow remains governed by the existing native source requirements. Source crop magnifications from art-v1 remain a final-detail limitation and must be resolved before the full native freeze.

## Audio and persistence

Voice: one approved Bernard voice generation, task `37575f5f-aea2-44d1-9e10-46cbe82388d2`, retained as `audio/voice_original.mp3`. No alternate audition or repeated voice generation. Reused repo camera, paper, marker and pencil cues; no new SFX generated. Music is a new original harmonic miniature with a developing motif and separate stem. SFX cue events/provenance are in SFX_CUE_SHEET.json. Designed sounds are editorial cues, not authentic sounds of physiology or heat.

Small source files and original narration are in Git. Actual movie bytes, complete self-contained review/source package and proof images are in the versioned GitHub review release once delivery receipts are recorded. No Drive destination or temporary link is the primary archive.

## Reproduce or inspect

- `python mix.py` rebuilds the exact source-derived mix; it does not generate voice or SFX.
- `node proof.cjs` renders A/B and temporal/protected-caption proof.
- `python preflight.py` checks approval records, actual proof/source hashes and complete mixed audio.
- `node render.cjs` captures this 1080p passage, with the preflight guard.
- `python verify.py` independently decodes the final movies and saves encoded phone evidence.
- `Review.html` opens the saved movies offline and offers the verified full-length WebM including audio. It downloads the saved export instead of risking a second browser capture. The static HTML links are structurally checked; browser playback has not been independently certified in this environment.

Dependencies: the observed Node/native-canvas runtime used by art-v1, Python NumPy/SciPy and FFmpeg/ffprobe. Original assets, selected SFX, fonts/notices, code, narration, stems, proofs and both movies are included in the review package. The clean extracted package must pass preflight and input hash verification before delivery.
