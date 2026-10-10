# Asset, rights and sound manifest — Curio Bureau EP005

## Archival images
| Asset | Origin | File-specific rights note |
|---|---|---|
| `assets/aerial.jpg` | BPL [BostonMolassesDisaster.jpg](https://commons.wikimedia.org/wiki/File:BostonMolassesDisaster.jpg), Flickr ID 4901555337 | US public domain (pre-1931 publication in Commons license). |
| `assets/after.jpg` | Boston Elevated Railway / Boston City Archives [9800-018-023](https://commons.wikimedia.org/wiki/File:Boston_Elevated_Railway_after_the_Molasses_Flood,_January_1919,_from_the_City_of_Boston_Archives_-_9800-018-023.jpg) | US public domain. If automated archive download fails, renderer uses source BPL panorama in two different crops; note this as an archival variation gap, not a second archive image. |

## Design / code
- `studio/scene.js`: all original camera, street facades, period wagon, elevated railroad truss, tank illustration, riveted stress mechanism, mole of molasses, editorial document and typography.
- Reenactment render is an **ILLUSTRATION**. Do not claim original 1919 moving footage.
- Typeface: Playfair Display and Manrope, Google Fonts Open Font License; bundling licenses in production package.
- Styles: brand-locked Curio Bureau navy / ivory / gold / coral with steel and molasses contextual accents.

## Audio cue sheet (generated original sound design — no third-party SFX binaries)
| Time | Source | Event | Mixing role |
|---|---|---|---|
| 0.0 | `audio_ep005.py`, resonant partials and noise | Metal rupture | Impact |
| 0.5–6.5 | Spectral filtered moving broadband noise | Heavy wave | Ambience |
| 18.8–25 | Original falling-pitch drop transients | Leaking tank | Detail SFX |
| 23.7 / 25.6 / 27.1 | Scraped broadband textured impact | Metal wall stress | Detail SFX |
| 29.2–34 | Independent steel resonances and moving rupture body | Tank failure | Impact |
| 30–45 | Layered viscous liquid broadband wave | Flood advancing | Ambience |
| 37–45 | Five debris impulse variants | Street objects collide | Impact |
| 53–61 | Shaped high-frequency spray noise | Saltwater cleanup | Detail SFX |
| 62–70 | Paper/document movement transients | Inquiry transition | Transition |

**Original music:** harmonically composed D minor progression with plucked / string timbres, bass movement, shaker/percussion and dynamic scene-specific intensity, file `out/music.wav`. This is not sourced from a commercial music library and not a standalone infrasound bed. It still requires a *perceptual music-quality check* before FINAL.

**Voice:** `en-US-AndrewNeural`, natural-rate neural narration; per-scene recorded voice data and timestamped actual TTS WordBoundary events. `out/voice_timing.json`, `out/captions.srt`.

**Connected Google Drive SFX gap:** The user's connected Curio Bureau SFX library has many potential clips, but authenticated files were not injected into this GitHub public codebase because redistributing those media files without asset-by-asset licensing verification would be inappropriate. All sound effects in this build are original synthesis; replace with provenance-cleared existing recordings where sonic realism requires it.

## Credits
Historic research: City of Boston Archives; Boston Public Library; 1919 Boston Elevated Railway source imagery.
Original illustration, graphics, music and bespoke sound design: Curio Bureau editorial production.
