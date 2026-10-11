# 07 — MOTION & ANIMATION BIBLE | Curio Bureau v1
## The contract
Movement is documentary explanation. Every motion action must answer **WHAT changed? WHY? IN WHICH DIRECTION? HOW MUCH?** A sophisticated but uninformative zoom or fade fails. An animation lasting seven seconds must contain a *sequence of evolving knowledge*, not a beautiful initial diagram and six seconds of holding.

## 1. Basic animation grammar
**Motion channels:** `{scene.camera, scene.world, scene.hero, scene.mechanism, scene.evidence, scene.annotation, scene.caption, scene.audio}`. Each is separately timeline-controlled and composited. No scene may move a camera purely to avoid stagnation without a new causal reveal.

**Easing presets (not mandatory for physical motion):**
- Fast reveal / cursor highlight: cubic ease-out `1 − (1−t)^3` (fast settle), 0.18–0.38s.
- Polished camera reframe: cubic ease-in-out `3t² − 2t³`, 0.45–1.1s.
- Historical photo drift: smoothed long camera 1.5–4s plus new evidence overlay within first 1s; drift ALONE never fills the beat.
- Physical cause: use event-specific acceleration (fall gravity, winch rotation, water/viscosity, driver braking, ratchet step). Do not apply same generic cubic to all matter.
- Sudden consequence: sharp 0.08–0.18s anticipation/impact into physically slower recovery; sound hit must connect.
- Headline conclusion: 0.25–0.55s mask/reveal and hold only long enough to absorb claim; end card ≤1.8s after spoken last word.

**Virtual camera:** define the film with at least THREE distinct shot scales (macro, human/object, systemic map/section). Use a 2.5D stack of 4–7 meaningful planes: environment backdrop (0.08× parallax), buildings (0.25×), scene props (0.55×), hero object (1.0×), evidence layer (1.05×), caption/folio fixed screen-space. Recalibrate per story; never move labels with the distant scenery if unreadable.

**Continuity:** match one real causal line/object between shots—shoreline → contour line → mine tunnel; pressure seam → flood wave; road centerline → H sign; screw threads → engineering elevation. If match impossible, use an intentional hard editorial cut rather than template fade.

**Transitions:** at most one generic dissolve in any rolling 15 seconds unless source material demands it; semantic match cuts are preferred, but do not force a match where it misstates physics. Sound triggers are scarce meaningful actions, not every scene change.

## 2. Fourteen composition families — with function, assets and motion
| ID | Family | Causal job | Required assets | Correct dynamic behavior | QA mistake to avoid |
|---|---|---|---|---|---|
| C01 | Consequence full-bleed | Show the unbelievable event before context | detailed cinematic environment + event elements | event already developing frame 1 | headline first, event later |
| C02 | Physical mechanism sectional | Reveal hidden path/load/pressure | cross-section with named parts and load arrows | introduce one mechanism part every narration clause | generic slab rectangles |
| C03 | Object macro | Connect small cause to big effect | high-detail screw/rivet/pipe/cart component | real rotation/strain/change | basic icon tween |
| C04 | Human scale | Explain risk or coordination | designed period figures/real sources, believable scale | gesture→physical reaction→new stake | stickmen and speculative witness speech |
| C05 | Archival proof | Ground claim in primary media | cleared high-resolution photo/print/document | reframe, highlight exact cited detail; cut to meaning | archival used as wallpaper |
| C06 | Geographic system | Establish causality in space | sourced GIS/map geometry | region→point→direction→physical consequence | arbitrary country/lake blob |
| C07 | Data spatial comparison | Answer how many/how much | data visual semantic scales | numeric change plus visible physical relation | solitary giant stat on navy |
| C08 | Documentary paper macro | Highlight evidence conclusion | verified scan with item-level rights | 1 original phrase highlighted timed to voice | generated fake newspaper |
| C09 | Temporally locked before/after | Show change while geography is stable | same camera/map/section both states | matched wipe aligned to physical landmark | unrelated split cards |
| C10 | Asymmetric collage | Unify independent source types | clipped original photo, plan, annotation, map | source A docks into mechanism B | repeated scrapbook template |
| C11 | First-person explanatory camera | Make difficult physical system intuitive | authored POV with real props | track through machine / along pipe / inside vehicle | fake historic POV presented as record |
| C12 | Timeline across cause | Distinguish multi-year events | source-dated labels + actual places | each date changes depicted system | dates on static card with no context |
| C13 | Kinetic editorial argument | One short paradox statement | verified phrase, key object/mask | words uncover physical evidence | 5+ seconds large text alone |
| C14 | Environmental resolution | Show what remained changed | complete transformed place/system | final cause physically resolves into mark | cut to empty logo screen |

An episode should feature **≥6 distinct families** if length permits, but this is a planning heuristic, not an arbitrary visual quota. Any composition can be repeated if physical continuity adds explanatory value; repeated CAMERA/OBJECT/STATE combinations without new knowledge fail.

## 3. Subject-driven signature motion: never repeat the 'hero trick'
- **Samoa:** sheet of paper/calendar flips from Dec 29 to Dec 31 while crossed-out 30 shrinks; world-date-line boundary slides beneath island. Mechanism: time-zone boundary governance, not magical time reversal.
- **Lake Peigneur:** under-lake mine galleries flood via cross-section, shoreline ground deformation and rising surface vortex. Need properly staged water flow, exact geographic anchors. A 2D donut is not a lake.
- **Boston:** steel joint separates, pressure reduces and heavy viscous laminar/sheer bands shove period carts; source photo supplies factual aftermath. Don't reuse blue lake-ripple algorithm tinted brown.
- **Sweden:** measured lane change of authorized vehicles under street restriction; H sign and 04:50/05:00 timing controls. No every-car stampede.
- **Chicago:** jackscrew thread rotates and raises beam/building by incremental step; sewer grade is physically established first. Machinery must support the depicted mass.

## 4. Animation stage design example — Chicago 5.8-second lift sequence
**0.0–0.9s:** 1:1 physical screw-thread macro. An operator turns one handle ~90°; upper bearing moves a small, visible increment; ratchet sound matches each bite.
**0.9–1.8s:** camera reveals four adjacent supports and timber load-distributing beams; transparent arrows show weight into beds, NOT weight floating.
**1.8–2.9s:** camera rises to building brick bond, window jambs and storefront; paint dust shakes, sill shifts very slightly relative to old street line.
**2.9–4.0s:** historical 1860 Lake Street frontage widens; source tag '320 ft / 6,000 jacks'; three sections rise in plausible synchronized increments.
**4.0–5.8s:** street-to-foundation cutaway reveals brick being placed beneath; next scene derives its raised road surface from this aligned new grade.

**The source model must keep the building object constant across shots**; a flat PNG zoom followed by unrelated vector rectangles is an art-direction failure (Episode 007).

## 5. Map example — 006 Dagen H 4-second choreography
0–0.5s: actual neighborhood junction outlines from credible road plan; 0.5–1.5s: arrows show OLD left-hand movement; 1.5–2.4s: camera isolates a sign change and note 'traffic restricted'; 2.4–3.3s: 04:50 authorized move right; 3.3–4s: 05:00 travel resumes; if signs claim 06:00 general traffic, move that to subsequent timeline beat. Every moment teaches a distinct rule.

## 6. Editorial information choreography
- Every VO clause has an explicit object, action, and resultant state. Example: 'water entered underground galleries' = 1) shaft opening appears 2) flow propagates to gallery 3) crew route exits, not a subtitle over a still mine.
- **Single focal change rule:** darken/soften no-longer-relevant planes, enlarge active mechanism, return scene environment only after change is understood.
- **Precision:** facts such as 21 deaths, 52 miners escaping, 82.9% advisory vote, and 6,000 screws must be matched to appropriate subject/episode. Never repurpose a numeric template with wrong connotation or source.
- **Archival animation:** parallax extraction is allowed if genuine image boundaries can be separated credibly; do not create fabricated moving historical persons or actions.

## 7. Shot building and technical structure
Each scene is authored as deterministic `render(t, state)` with timeline-derived state, not accumulated real-time deltas. Scene assets are separated into world geometry, depth planes, mechanism, evidence, type and SFX triggers. Statically cache expensive high-resolution assets but render all type and geometry at native 4K. Composition states are keyed by **narration word events**, with scene layout reflowed when the voice changes. Include a debug layer visualizing caption zone, safe areas, asset native resolution, active stage and semantic motion event.

## 8. Six-shot visual diversity test
Print six **consecutive** major beats at phone size, remove captions and IDs, ask: which changed camera family, which new mechanism and which fact learned? FAIL if three-or-more shots could be mistaken for same still with updated words; FAIL if source art has a >2× detail-quality swing between adjacent shots. Record aspect/treatment counts in `shot_fingerprint.csv`.

## 9. Delivery QA
Motion grade passes only when (a) no placeholder humans/buildings where main focus, (b) captions do not obscure mechanism, (c) no >5-second narrated beat where meaningful picture change fails, (d) no sequence relies on an animated title floating in emptiness, (e) 3 detailed closeup samples from FIRST/MIDDLE/END meet same asset standard, and (f) shot-specific animation mechanism remains truthful.