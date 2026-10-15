# Wrinkled fingers R2 — finishing audit

Owner correction: 15 October2026,15:50 Asia/Manila: missing grain, material texture, camera blur and transition blur; review infrastructure and render again4K. R1's finishing is rejected. R1 remains a historical artifact and is not the new quality benchmark.

## What was already specified
IMAGE_LED_OWNER_DIRECTION sections3/6, SCIENCE_PAPER_IMAGE_STANDARD sections43/70–74, TUTORIAL_OPTICS_2026_10_13 and the shared finishing.js/optics.js already require visible role-specific materials, moving film grain, short focus hunts, selective focus with matching luminance gradient, restrained chromatic separation, mechanical jitter/exposure, local ink bleed/edge boil, sharp critical captions and the exact untouched ending.

## What the actual R1 implementation missed
The custom build did not import or invoke either shared optical/film implementation. The material_profile label did not activate them. Its finish() drew an ink JPEG at.12 soft-light plus a.008 opacity flat exposure tint. The mechanism used.07 ink overlay and.004 tint. These are not animated grain. Only the mechanism photo was blurred at.9 logical px, without a coordinated focus field. No transient camera/transition blur was called. Plastic was packaged but never drawn. Existing marker jitter was not the shared ink bleed/edge-boil operation. Background material was cached at1080p, and no encoded phone-size material check challenged the missing effects. Technical format/loudness checks had been mistaken for finishing coverage.

## Corrected R2 render path
Scene artwork → native shared editorial-finishing pass → sharp captions/critical title overlay → exact shared London Bridge endcard. Existing scene geometry and complete full_mix.wav remain the source. No narration, music or SFX regeneration.

- Stronger paper/fiber background; print-local ink and plastic sheen. Material belongs to the object, not a universal brown overlay.
- Deterministic moving grayscale grain at12fps, coarse enough to survive phone-size review; 30fps camera and delivery.
- Shared filmState: mechanical jitter±.72 logical px at18fps, exposure variation±.065 stops at5fps.
- Short camera focus hunt up to3.8 logical px, with a second small settle pulse after incoming transitions.
- Feathered source-local selective blur up to4–6 logical px, coordinated with up to18% surround shading. Native compositing is a feathered multi-plane approximation, not After Effects compound-blur equivalence.
- Three timed camera joins:6.2–7.02,18.26–19.02,30.15–31.02s. Outgoing/incoming motion,12 logical px transient defocus, directional integration and settling; padded overscan protects borders. Peaks align with the original edit/action cues.
- Reconstructed RGB separation±.72 logical px in holds, up to1.32 during fast transitions; no screen-blend red wash.
- Shared boilPath/drawInkStroke: selected marker lines only,12fps,.65px boil,.85px bleed/.34 bleed alpha. Scientific/photo boundaries are not deformed.
- Caption drawing occurs after finishing. Opaque caption plate in the opening/grip/closing prevents grain or blur contamination. Mechanism captions retain their approved typography and are composited last.
- Exact ending drawn last. Native A/B test at35.9s gives zero changed pixels with finishing on/off.

Native verification: checks/finishing_verification.json. Deterministic repeated frame, effects-on/off differences at camera/focus states, unchanged opaque caption region, unchanged endcard. This establishes actual execution, not artistic certification. Phone-size still and encoded moving checks are separately recorded. No claim of proprietary Vox settings or100% equivalence.

## Infrastructure repair
Add shared browser/editorial-finish.js, explicit per-episode finishing declarations, runtime proof and a finishing release checklist. Custom renderers must demonstrate the same output contract; config names and module presence alone do not pass. Future shot timings/focus points must be authored for their own subjects, not copied from this episode. Preserve historical approved exports.

## Recovery
Native2160×3840/30fps/1089 frames is recaptured in bounded80-frame ranges, at most2 workers. Source and actual native lossless bytes are saved before a range is declared durable. Oversize chunks are split into ordered transport parts with individual SHA256 and saved identities; recovery joins parts and verifies the whole chunk SHA256. Local transport parts may be removed only after successful durable save if the verified original chunk remains locally. Durable native chunks/parts are retained through final delivery. Encode resumes from completed ranges, never from an upscaled R1 export.
