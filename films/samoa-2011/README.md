# Samoa 2011 — The Day That Disappeared

**Status:** production baseline archived; Vox-inspired remake **not yet finished**.

## What is here
- `legacy/Curio_Bureau_The_Day_That_Disappeared_REBUILT.html` — original self-contained 1080 × 1920, 30 fps canvas animation with controls and embedded score/FX.
- The legacy HTML is a **reference implementation**, not an approved final. Its visual execution needs the Vox-inspired editorial rebuild and its narration must be loaded separately.
- Render tooling: `../../scripts/render-samoa.mjs` and `../../.github/workflows/samoa-preview.yml`.

## Production brief
**Story:** In 2011, Samoa changed which side of the International Date Line its civil calendar followed. The country went directly from Thursday December 29 to Saturday December 31, skipping Friday December 30. The choice was about easier commercial coordination with Australia and New Zealand. The story is about how dates are a human convention with real economic consequences.

**Creative approach:** Vox-inspired explanation using animated calendars, archival-style editorial composition, a legible Pacific map, the date line, and a timeline comparing regional working weeks. Preserve Curio Bureau's own navy/ivory/gold brand system; do not copy Vox graphic assets, marks, or entire compositions.

## Required production milestones
1. Define a final fact-checked script with timestamped voiceover.
2. Design assets: recognizable layered Pacific map/Samoa marker; calendar typography; office and invoice illustration; day-line graphics.
3. Animate object-to-object transitions and typography with carefully staged reveals and zero arbitrary motion.
4. Mix real SFX from the shared Drive library, with recorded asset filenames and licensing information.
5. Attach narration and align the motion timeline to the actual spoken performance.
6. Render 1080 × 1920 / 30 fps and check audio/video streams, first and last frame, and critical cuts.
7. Only then name the exported master `FINAL`.

## Narration is mandatory for final
The archived baseline contains **music and SFX but no embedded narration**. To export a narrated version in a browser, use **Load Voice**, choose the voiceover MP3, then **Export WebM**. To do so from the GitHub renderer, use `--voice /path/to/voiceover.mp3`.

A CI run without a voiceover is expressly a **preview**, even if its WebM includes an audio stream.

## SFX source
[Curio Bureau shared sound library](https://drive.google.com/drive/folders/1JsF-myJsH4rnyy0NI-OjDL6ZVrSVeC81) is the authority for SFX. It includes Technology, Whooshes, Clock, Suspense, Keyboard, and Bass Drops folders. Store a manifest naming the used clips, license, edit, and cue time; do not commit the bulk library or expose private Drive download credentials.

## CI artifacts
A push to this branch runs the preview workflow, which generates a WebM and probes its technical video/audio streams. This is a mechanical rendering check, **not a creative-quality signoff**.
