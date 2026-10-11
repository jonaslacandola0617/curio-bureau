# 06 — CURIO BUREAU VISUAL IDENTITY BIBLE | v1.0
**Brand promise:** *Stories, systems, and surprises.* The channel makes unusual true events visible by revealing the invisible mechanisms—geography, infrastructure, policy, engineering, physical consequences—and the humans whose lives those mechanisms alter.

## 1. Brand DNA: the five invariants
1. **Evidence, then mechanism.** Every important historical or scientific statement has a sourced visual or an unambiguously labeled original reconstruction. Do not simulate archival photography.
2. **Elegant editorial authority.** Warm ivory typography, deep navy foundations, restrained metallic gold, and confident editorial timing. Avoid tabloid electric-primary overlays and sensational fake screenshots.
3. **One cinematic physical surprise per film.** The chosen subject provides its own signature action. Samoa = absent calendar square; 004 = water finding mine; 005 = tank bursting / viscosity; 006 = road crossing; 007 = screw jacks rising.
4. **Clarity at 216px phone preview width.** Hero object, main claim and causal direction must still read without magnifying the screen.
5. **Restraint with visual richness.** Complex background may be richly constructed, but only one foreground explanatory event competes for attention at once.

## 2. Official color architecture
| Token | Hex | Function | Contrast/placement guidance |
|---|---|---|---|
| Navy-900 / Canvas | #0D1C2B | Brand base; maps, outer negative space, typography field | Never the only background in >2 consecutive major beats |
| Navy-950 / Ink | #091622 | Labels/caption supports, subtle photo grading | Use opacity 70–90% for photo caption backing only if subject unobscured |
| Ivory-100 / Editorial | #F5F0E7 | Main serif titles, high-priority facts, clean archival scans | prefer 8:1+ over midnight navy; audit contrast numerically |
| Gold-500 / Evidence | #C8A26B | Historical dates, causal pointers, selective meaningful highlights | usually <12% total foreground area; never every word |
| Coral-400 / Warning | #D57864 | Human stakes, breached systems, danger marker, changed state | semantic red: limit to warning/consequence, not decorating all animations |
| Surface-200 / Document | #EAE3D6 | Editorial document surfaces and historical evidence backing | warm, not bright web-app white |
| Neutral-600 / Steel | #56616B | Schematics/structure overlays | only paired with strong ivory labels |
| Molasses brown / episode | #7E4C30 | Specific 005 physical material | subject-owned, not global brand token |
| Swedish road blue / episode | #17588D | H signs / actual 006 environment | episode-local historical accuracy |
| Brick/iron / episode | #A4664C/#3F464B | Chicago architecture/material | episode-local palette with global hierarchy preserved |

**Usage rule:** In each composition, one dominant background/archival photo, one legible principal text color, one purposeful meaning-coded accent. An episode-specific color may occupy large environmental regions (molasses, lake, brick), but metadata and typography hierarchy remain brand standard. Ivory inversions have a semantic job: show original evidence, a factual comparison, or a conceptual revelation—not arbitrary visual 'variety'.

## 3. Typography: actual audit and authority levels
**Required families:** Playfair Display (editorial headlines/insights) and Manrope (captions, numbers, evidence, maps, place/date labels). Both fonts appear in accessible source references for 004/006/007; 007 source renderer also uses PIL TrueType, while 004 and 006 HTML contain web font references/fallbacks. **A source reference is not a proof of exact final glyph rendering**. The exact brand family has not been conclusively verified in every video export. Fix by bundling pinned, licensed font assets during rendering, waiting for `document.fonts.ready` and logging hash, family/weight and pixel specimen checks. Do not distribute standalone font files to end users.

### Practical master styles (1080×1920 logical; native 4K is exactly ×2)
| Style | Family / weight | Baseline logical size | Use / line limit |
|---|---|---|---|
| Display Hero | Playfair 600–700 | 76–108px | first-frame startling fact; ≤3 lines; width ≤920px |
| Section Heading | Playfair 600 | 58–76px | evidence/mechanism act heading; 1–2 lines |
| Final Insight | Playfair 600–700 | 64–88px | 1–3 compact lines; over active subject, no blank logo cut |
| Body Fact | Manrope 600–700 | 26–42px | only when screen can carry context; never paragraph cards |
| Data Hero | Manrope 750–850 | 66–125px | isolated sourced 21 / 82.9% / 6,000 |
| Map Place | Manrope 700 | 24–36px | font size increases during geographical zoom |
| Source Credit | Manrope 650–800 | 17–23px | only legible when viewer can see it; exact source in credits too |
| Narration Captions | Manrope 700–800 | 42–55px | one or two lines, ~24–35 characters/line, center band |
| Masthead / File Stamp | Manrope 650–850 | 19–26px | discreet, not constantly stealing viewer gaze |

**Typography rules:** text must be vector/native 4K; optical fit with loaded actual font; track hero Playfair around −0.01 to +0.01em, Manrope all-caps metadata +0.08–0.15em (size-dependent); serif leading ~1.05–1.18; captions ~1.12–1.22; no automatic text wrapping relying on web fallback; avoid tiny 'source' words. Verify actual bounding boxes and pre-crop overscan. These are initial targets, not universal values.

## 4. Consistent master grid
- 9:16 full 2160×3840 render; authoring in 1080×1920 logical coordinates is fine if vector drawing/graphics happen at 2× native scale, not video upscale.
- Horizontal protected inset ≈84 logical pixels / 168px native for most labels; exception full-bleed environments/photos intentionally crop to edge.
- Top protected inset ≈120 logical for labels; do not put the ONLY meaningful action under top nav.
- Captions center: normalized y **0.42–0.58** (native y≈1613–2227); horizontally centered. The *event* is composed around this region, not allowed to vanish underneath it.
- Keep a variable foreground “stage” outside caption band: often upper-third face/mechanism and lower-third causally linked infrastructure, with overlap permitted only after validation.
- Motion transitions may temporarily pass beneath captions but captions must remain legible each frame.
- Bottom 25% is not a reliable narration text home on TikTok or Shorts.

## 5. Visual component system (never a page template)
**Folio stamp:** hairline rule + C/B or full Curio Bureau wordmark. Choose ONE official system for each running film; 001/004 full wordmark and 005–007 abbreviated 'C/B' varied. Standard proposed: small 'C / B' 24px upper-left with episode no./research file upper-right; complete `CURIO BUREAU` only on end card and occasional genuine source title reveal. Film-specific slug can vary.

**Document pointer:** fine gold line ends in a tick, not oversized yellow box; quote highlighted only while spoken; source credit attaches to source card.

**Map pointer:** navy-on-ivory or ivory-on-navy; one highlighted location then an additional causal layer. Avoid random “island blob”; use sourced map data or label as abstract relationship.

**Stat moment:** one large numerical claim accompanied by spatial meaning. E.g., 6,000 screws appears with length of Lake Street frontage, not alone on empty title field.

**Archival distinction:** ivory hairline top label 'HISTORICAL PHOTO / YEAR / ARCHIVE' vs reconstruction footer 'ORIGINAL ILLUSTRATION / NOT DOCUMENTARY FOOTAGE'. Filmic texture does not transform generated material into historical proof.

**End card:** image/motion continues behind mark; Curio Bureau two-line masthead in Playfair + brand line in Manrope, gold line integrated with real story geometry; 0.8–1.8s tail, no hard black reset.

## 6. A recognizable channel without visual monotony
**Keep:** type hierarchy, color roles, research folio, evidence ethics, caption system, audio tonality, note of wonder, timing precision, calibrated camera and clean graphics. **Change every episode:** hero mechanism, environment palette, three major camera angles, transition motif, archival mix, microtexture, music instrumentation and narrative pivot. Distinct identity is the *way Curio Bureau explains facts*, not 'every film has exactly the same title on exactly the same navy card'.

## 7. Best-to-worst brand examples observed
- **Positive:** 001/004 editorial warm ivory on navy establishes personality; 006 82.9% page provides clean document hierarchy; 005 1919 aftermath photos legitimize the investigation; 007 architectural opening supplies environment density and scale.
- **Negative:** 001/004 slow first-frame masthead/title stalls the surprise; 006 H sign and facades are reused too often; 007 vector-scene quality fails next to premium image; 005/004 low captions are masked in app UI.

## 8. Font verification checklist (must become automatic)
1. Resolve font file legally, pin version and SHA-256 in build manifest.
2. Load Playfair 600/700 and Manrope 500/700/800 before first rendered frame.
3. Canvas/browser: `document.fonts.check('700 88px "Playfair Display"')` and analogous Manrope check, record method-specific fallback limitations.
4. PIL renderer: load exact TTF font path, log basename/hash for each font role; test single-page glyph render. If wrong font, FAIL render instead of falling back to Georgia/DejaVu.
5. Take source-generated glyph specimens and compare exported cropped pixels at 100%; verify no unstyled fallback during scene transitions.
6. Enumerate screenshots for Episode 001–007: source-verified/appearance-only/missing. Older films cannot be 'certified' from visual style alone.