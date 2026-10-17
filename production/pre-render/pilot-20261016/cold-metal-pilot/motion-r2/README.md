# Cold Metal R2 — native 4K sequence

Owner requested opening audio/motion correction, infrastructure QA, native 4K and social copy on 17 October 2026. This retains the approved art and complete Bernard source. It is a 13.9-second representative passage, not a complete long-form episode. R1 remains unchanged.

Opening: hand finishes approach by 2.64s, contact ring 2.66–2.86s, paper has one continuous quintic launch 2.78–3.16s before the measured ~3.25s “Touch it” onset. Three printed arrows grow continuously from 3.88s; no discrete one-arrow/three-arrow redraw. Headline crossfades instead of swapping; comparison arrows begin at 7.00 and 8.04s. Focus hunt resolves before the spoken phrase, and comparison focus follows metal then wood before returning to both.

Audio: existing original narration and score construction retained; existing repo cues only. No marker/paper/pencil pile-up. One first-reveal cue at a time; speech-activity gain automation and 6.5kHz filtering protect diction. Complete source samples and protected tail retained, no narration fade. Machine envelope/decode checks do not constitute a human listening certification.

Strong source-local materials, moving grain, transient blur, selected-detail focus/shading, restrained RGB separation, film jitter/exposure, ink bleed/boil and caption protection retained. Native canvas renders are 2160×3840 at30fps; no 1080p movie upscaling. Photographic illustrations retain their original raster detail (spoon887×1774, hand1774×887); native typography/material/optics do not invent photographic detail.

Full-film ending is intentionally absent from this isolated passage, and its protection is not claimed. The complete pilot episode still has its own freeze/approval gate. This native sequence authorization does not mark all five pilot films ready or certify full-film conformity.

## Rebuild

1. `python mix.py` — reuse narration/SFX, rebuild stems and canonical PCM.
2. `node proof.cjs` then `python refresh_coverage.py` — current-source effect tests and bound evidence.
3. `node render.cjs` — guarded 1080p corrected timing review.
4. `node native_proof.cjs` — native picture/caption/determinism/phone-grain proof.
5. `CURIO_STOP_AFTER_CHUNKS=2 node native_capture.cjs` — bounded native lossless capture. Save actual completed chunks to GitHub and record matching receipts before continuing. At most two local unarchived chunks may accumulate.
6. Encode independently from contiguous verified native FFV1 chunks to H264/AAC MP4 and VP9/Opus WebM. Final format/audio/picture checks and verified GitHub readback follow.

See OWNER_REVISION_ORDER.md, FINISHING_COVERAGE.json, NATIVE_PROOF.json, RECOVERY.json, OUTPUT_QA.json, DOWNLOADS.md and POSTS.md as they become available. None of these records substitutes owner review of the revision.

## Restore a saved render

Before recapturing, retrieve the lossless chunk assets identified by RECOVERY.json from the same GitHub Release, put them under chunks/, and compare every SHA256/frame range. Existing verified frames are reused. The source ZIP intentionally does not duplicate multiple gigabytes of lossless checkpoints. Missing final movie downloads are repaired from saved exports or re-encoded from these chunks; do not regenerate images, voice or SFX.
