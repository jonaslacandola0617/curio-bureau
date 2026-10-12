# THE VOX-STYLE MOTION DESIGN & EDITING TECHNIQUES BIBLE

*A Complete Practical Knowledge Base for an AI Motion Designer and Video Editor*

Prepared from the ten supplied short video tutorials · 12 October 2026

## How to use this book

Use Book X to find a technique by production problem, then retrieve its complete A–L recipe in Book VII. Books II–VI explain relationships between those recipes. Books VIII–IX provide original plans and exercises. Book XI supplies the operating procedure, quality gates, coverage audit, and gaps register.

This is a practical extraction from a small, specific tutorial collection—not an official Vox production manual and not a claim that all Vox work follows one preset. Creator claims about “Vox” are preserved as claims or stylistic observations, not independently verified production facts.

### Evidence contract and inspection limits

All ten local MP4s were surveyed chronologically using approximately one sampled frame per second, including examples, instructional sections, promotional endings, and end cards. Selected controls were inspected at the supplied 576 × 1024 resolution. Ambiguous instructional passages in T01, T02, T04, T06, and T09 were additionally sampled at approximately four frames per second. Motion descriptions compare ordered frames and visible timelines; they are not frame-by-frame playback measurements.

**Audio was not audibly reviewed or independently transcribed.** Instructor advice below is supported by burned-in captions and on-screen text. Caption-supported speech is explicitly distinguished from direct interface evidence. Exact sound character, timing by ear, uncaptured speech, and the final mix remain unverified. This matters especially for T03. No video was omitted from the visual survey, but fleeting unsampled actions and speech without captions may be absent. The book therefore does not claim exhaustive audiovisual transcription or execution-tested project reconstruction.

The source clips omit substantial setup. This book preserves those omissions and then offers practical completions where useful. No external tutorial, advertised preset package, project file, or asset pack was treated as inspected evidence. No After Effects or Photoshop project was executed to validate these recipes.

| Evidence label | Meaning | How to use it |
|---|---|---|
| **Demonstrated (D)** | A control, action, layer arrangement, or result is visible | Reproduce the observed portion; do not infer hidden setup automatically |
| **Caption-supported instruction (C)** | Burned-in captions or instructional text express the advice | Treat as the supplied clip’s instruction, not an independently verified audio transcript |
| **Observed result (R)** | A finished example is shown without its construction | Use for a target appearance; implementation must be supplied separately |
| **Inference / proposed completion (I)** | Technical explanation, missing setup, diagnostic, or original application supplied here | Test in the target project; do not attribute to the creator |
| **Exact** | A readable value or command | Exact to that source moment, not necessarily a final or universal setting |
| **Approximate** | Estimated appearance, time, or amount | Adjust and verify; do not represent as a measured preset |
| **Not specified** | No usable value or procedure is available | Leave open or choose an explicitly original test value |

Source timestamps refer to the supplied video, rounded to useful local ranges. They do not refer to timecodes shown inside the creator’s project. A timeline time of `00:03:12` is not the source clip’s 3.5-second point. The delivered MP4 dimensions and frame rate likewise do not establish the creator’s working composition or export settings.

## Contents

1. Book I — Foundations
2. Book II — The Motion Design Toolbox
3. Book III — Visual Construction
4. Book IV — Specialized Vox-inspired Effects
5. Book V — The Art of Transitions
6. Book VI — Editing Tips, Tricks & Professional Shortcuts
7. Book VII — Complete Technique Recipes
8. Book VIII — Creative Application
9. Book IX — Training Exercises
10. Book X — Master Technique Index
11. Book XI — AI Agent Operating Manual

# BOOK I — FOUNDATIONS

## 1. Tutorial catalog

All titles below are descriptive catalog titles, not verified original publication titles. T01–T04, T06, and T08–T10 display Chris Moran branding; T05 and T07 display Denys Zhylin Tutorials branding. Creator identification is based on visible branding only.

| ID / duration | Descriptive title | Software and subject | Level / prerequisites | Dependencies and learning outcome |
|---|---|---|---|---|
| T01 / 31.61 s | Film jitter, exposure flicker, and grain | After Effects; global analog imperfection | Intermediate; effects, 2D Position, expressions | Transform, Exposure, Add Grain; an existing composition. Other effects and a branded preset are visible but not prerequisites for the two expressions. Outcome: subtle global instability with known expression caveat. |
| T02 / 52.61 s | Hand-drawn annotation and edge boil | After Effects; Trim Paths, Roughen Edges, Turbulent Displace | Intermediate; shape paths, strokes, effects, expressions | Newspaper image and stroke annotation; no demonstrated need for a third-party plugin. Outcome: a line that draws on and continually changes contour. |
| T03 / 27.15 s | Tactile sound effects | Premiere-style audio editing timeline, plus an After Effects panel visible below; physical sound association | Beginner/intermediate; importing and aligning audio | Sound files or self-recordings; Freesound and Soundly are suggested sources, not required services. Outcome: an editable sound-layer plan; audible mix not verified. |
| T04 / 26.05 s | Moving map spotlight and selective blur | After Effects; radial gradient, Multiply, Compound Blur, border reveal | Intermediate; blend modes, adjustment layers, shape paths | Prepared map; Google Earth attribution visible. No map-building plugin taught. Outcome: a sharp, brighter area of attention moves across the map. |
| T05 / 66.52 s | Five editorial techniques for explainers | Finished examples; construction software not established | Beginner conceptually; script and asset planning | No required plugin shown. Outcome: visualize claims, explain relationships, plan motion and transitions, coordinate story/edit/graphics. Operational settings absent. |
| T06 / 31.26 s | Cut at the peak of the motion curve | After Effects; eased Position, parenting, hard cut | Intermediate; keyframes, speed graph, Parent & Link | Two objects or aligned scene elements. EaseCopy panel is incidental. Outcome: change the represented object while preserving moving continuity. |
| T07 / 32.95 s | Make articles readable and tactile | Result montage; a full After Effects highlighter tutorial is advertised, not included | Beginner conceptually; article selection and visual hierarchy | Article imagery, paper treatment. Outcome: plan article framing, texture, and emphasis; exact construction omitted. |
| T08 / 34.80 s | Text animators, presets, and readable typography | After Effects; fill animator and preset command, plus result showcases | Intermediate; text layers and selectors | Editable type; no demonstrated external dependency. Outcome: understand per-character selection and save a reusable animation; random/odometer implementations incomplete. |
| T09 / 41.39 s | Photo parallax from separated image planes | Photoshop and After Effects; separation, Clone Stamp, 3D spacing, camera move | Intermediate/advanced; image masks, layered files, 3D camera | A photo with distinct depth; optional Depth script shown. Outcome: construct layered parallax with repaired hidden regions. |
| T10 / 30.15 s | Chromatic edges, 12 fps treatment, easing, and texture | After Effects 2024 visible; finishing and speed-graph demonstration | Mixed; effects, frame sampling, speed graph | Quick Chromatic Aberration 3 for the demonstrated color-fringe method; textures. Outcome: controlled finishing and a rapid move with a long settling tail. |

### Source file registry

- **T01** — `017833d6758add159d297d753e03e084.mp4`

- **T02** — `37901357392ee8d7c14db082a78b701d.mp4`

- **T03** — `4b14c84e681d7c91605262059df0d9f3.mp4`

- **T04** — `4ddac5f4d09320da3574f855072240ad.mp4`

- **T05** — `67d5920a705ab69ca0840d5c0223e283.mp4`

- **T06** — `719b931f0927612a86eb7b988c09608c.mp4`

- **T07** — `aeed047136abe7bd6dda38dda80f6023.mp4`

- **T08** — `ceafa2d2481f7965d870e02fb67574bb.mp4`

- **T09** — `d29898c682425d563099b86e1c108116.mp4`

- **T10** — `f1c5ee3e7479d70b0060bc80af8a330c.mp4`

## 2. What the supplied material actually teaches

The strongest operational demonstrations are expressions and grain (T01), edge boil (T02), the map attention rig (T04), cutting the motion curve (T06), and photo parallax (T09). T08 supplies partial text-animator construction and a preset command. T10 shows controls and a graph but omits several setup actions. T05 and T07 mainly teach editorial selection through examples.

No supplied clip teaches a full quantitative chart, geospatial data import, automatic route generation, an animated numeric counter expression, render delivery specifications, music ducking, a halftone workflow, or a complete export pipeline. These are legitimate future production needs, but they are not tutorial-derived recipes in this book. Numbers and diagrams appear as examples; their presence is not evidence of their construction.

## 3. Working concepts needed before the recipes

**Property versus effect.** A layer has transforms such as Position and Scale; a Transform *effect* is a separate operation in the effect stack. T01 uses the effect’s Position for its global jitter. Copying that expression to an unrelated 3D property would change the problem and can create a dimension mismatch.

**Keyframe versus expression.** A keyframe records a value at a time. An expression computes a value from time or other inputs. T06 shapes a keyframed movement; T02 changes an effect seed through `time*4`. These are different sources of animation even when both produce motion.

**Spatial path versus temporal speed.** Where an object travels and how fast it gets there are separate decisions. T06 relies on a velocity peak. T10’s graph is highly asymmetric: a sharp acceleration followed by a long deceleration. “Eased” does not imply one universal bell-shaped curve.

**Visibility versus movement.** A hard cut changes which object is visible. Parenting makes objects share transformations. T06 combines the two; parenting alone does not create a cut or align mismatched artwork automatically.

**Shape paths versus masks.** T02 and T04 use Trim Paths on shape strokes. They do not demonstrate a mask-based wipe. Treating the visible Add > Trim Paths command as mask instruction would lose the actual workflow.

**Texture, grain, jitter, flicker, and frame sampling.** Texture adds surface variation; grain adds small image noise; jitter moves the image; flicker changes brightness; Posterize Time changes temporal sampling. They can coexist, but they are not interchangeable “film” sliders.

**Layer depth versus a flat zoom.** T09 separates foreground, midground, and background so their projected relationships change under a camera move. Enlarging one flattened image preserves internal relationships and cannot produce the same parallax.

## 4. Evidence-informed production hierarchy

An inferred order of work is: establish the claim, choose evidence, make the main relationship readable, animate it, connect scenes, then finish. This order is a synthesis of T05’s story/edit/graphics advice, T07’s directed article reading, and T08’s clutter warning. It is not a quoted seven-step process from a tutorial.

A useful effect must survive three questions: what information does it expose; where should the eye move; what remains understandable when the movement stops? If none has an answer, keep the effect optional.

# BOOK II — THE MOTION DESIGN TOOLBOX

## 1. Motion families and their controls

| Behavior | Recipe | Driving property | What the viewer perceives | Important distinction |
|---|---|---|---|---|
| Fast arrival, slow settling | MOT-01 | Eased transform; a percentage-per-second graph is visible | A decisive move that gently comes to rest | Source does not provide exact influence percentages |
| Draw along a line | SHP-01 | Trim Paths range | A mark or border being traced | Drawing the path and animating its visible extent are separate tasks |
| Global image instability | FIN-01 | Transform effect Position expression | Tiny mechanical movement | 24 Hz expression sampling is not the same as a 12 fps picture treatment |
| Changing contour | FIN-05 / FIN-06 | Turbulent Displace Random Seed and spatial scale | A hand-drawn edge that keeps changing | Small noisy contour and broad wobble are separate effect passes |
| Moving attention | MAP-01 / MAP-02 | Radial gradient Start Point | Bright/sharp region moves between locations | Move the control field, not necessarily the whole map |
| Matched motion across a cut | TRN-01 | Parent Position animation plus layer visibility | One moving subject becomes another | Parent inheritance must be paired with visual registration |
| Per-character emphasis | TYP-02 | Text animator Fill Color and selector | Color travels through a line of type | Changing a text layer’s whole fill is not a selector sweep |
| Depth from a photograph | IMG-04 | 3D planes and camera/rig position | Foreground and background shift differently | Camera spacing and hidden-region repair must agree |

## 2. Timing without invented defaults

None of these clips establishes a universal shot length, number of keyframes per second, or standard ease influence. T05 recommends ongoing visual change; it does not supply a mandatory cut interval. T10 shows a long settling phase; copying its graph’s shape is more defensible than inventing an exact cubic Bézier or calling the visible axis maximum a target velocity.

For an original scene, choose the movement’s narrative endpoint first. Then allocate movement time before that endpoint and readable hold time after it. A label that never settles conflicts with the readability objective in T07 and T08. Test timing against the actual narration rather than treating a proposed exercise duration as extracted instruction.

## 3. Coordinating multiple motion systems

A proposed hierarchy is one main change, one supporting change, and optional ambient movement. For example, move the map’s focus first, reveal the target border second, and keep texture stationary. This combines T04 with T08’s warning; the exact overlap is an original choice.

Do not stack T10’s asymmetric easing onto T06’s transition without checking the cut frame. The maximum speed may no longer occur halfway through the move. Locate the actual peak after editing the curve.

Motion blur is not operationally taught here. T01’s Transform interface includes shutter-related controls, but no usable motion-blur tuning workflow is demonstrated. If blur is added to an original sequence, label it an additional treatment and evaluate legibility and edge artifacts.

# BOOK III — VISUAL CONSTRUCTION

## 1. Build assets for the operation they must support

| Asset | Required preparation | Source support | Failure avoided |
|---|---|---|---|
| Newspaper/article | Enough resolution for the final crop; preserve source context | Framing and highlighting results in T07 | Enlarged unreadable text or emphasis detached from its source |
| Drawn annotation | Shape path with stroke and room around the contour | T02 | A fill-only shape or clipped displacement |
| Map | Prepared base map plus independent highlight/border layers | T04 | Attempting to obtain regional geometry from a blur effect |
| Parallax photo | Foreground/midground/background on separate layers | T09 | A flat enlargement mistaken for depth |
| Hidden image regions | Retouched coverage behind separated subjects | Clone Stamp instruction in T09 | Holes or duplicated subjects exposed by camera motion |
| Animated typography | Editable text, animator properties, readable line length | T08 | A raster screenshot that cannot receive character selectors |
| Tactile sound | A usable file whose event can align with a graphic action | T03 | Arbitrary audio with no correspondence to the visible event |

## 2. Preserve demonstrated layer relationships

T04 visibly has “Vox Sauce,” “Uptown Highlight,” “Highlight,” “Radial gradient,” textures, eyes, an adjustment layer, a gray solid, map-related layers, and a background. Several overlays and correction layers are already present. The tutorial teaches a selected sub-rig, not every layer’s construction. Its gradient is set to Multiply; the Compound Blur adjustment is lower in the shown stack. An original rebuild can use fewer layers while preserving the demonstrated relationship: sharp annotations above, map content affected by selective blur, and a visible gradient contributing darkening.

T09’s Photoshop layers are named Foreground, Midground, and background. That is functional naming: each label communicates the plane’s depth role. Layer names do not establish exact Z coordinates. Keep the preserved original photo separate from the repaired and isolated working layers as a proposed production safeguard.

T01 places multiple finishing effects on a layer named “Vox Sauce.” The name is organizational, not a built-in After Effects feature. Its presence in other clips does not prove identical settings across all projects.

## 3. Typography and data boundaries

Article highlighting (TYP-01) emphasizes a passage in a source image; a fill animator (TYP-02) changes editable characters. They solve related attention problems with different assets. Do not promise character-level changes to text embedded in a photograph without first recreating or isolating it.

The `$600,000,000` example in T08 supports a numeric-display appearance, not an arithmetic counter. If a scene needs values to increase proportionally over time, a separate validated data/counter method is needed. This book deliberately has no fabricated DAT recipe.

# BOOK IV — SPECIALIZED VOX-INSPIRED EFFECTS

## 1. Finishing is a stack of distinct operations

T01’s visible order is Quick Chromatic Aberration 3 → Posterize Time → Exposure → Add Grain → Transform. This is an observed project stack, not an instruction to activate every effect on every scene. T10 repeats several of these effects and separately demonstrates textures and easing.

The two important temporal values are not contradictory: T01’s jitter expression says `posterizeTime(24)`, while Posterize Time displays `12.0` in T01 and T10. One is inside an expression and one is an image effect. Effects appearing later in a stack can introduce their own changes; a 12 fps effect does not justify claiming every downstream operation updates only twelve times per second. Check the final rendered cadence.

## 2. Edge boil has three jobs

1. FIN-04 establishes a rough contour through Roughen Edges.
2. FIN-05 adds fine changing edge disturbance with small-size Turbulent Displace and a seed expression.
3. FIN-06 optionally adds broader contour motion with a second displacement pass.

T02’s shown order is useful evidence. Reordering effects may change how one distortion treats the result of another. Begin with the observed order before making an explicitly original alternative.

## 3. Map focus uses one field in two roles

MAP-01 uses a light-centered radial gradient as a Multiply overlay. MAP-02 uses that gradient as a Compound Blur control with **Invert Blur checked**, so the central light region can remain clearer while darker surroundings blur. The same animated center directs both attention cues. This is a specific relationship, not a generic vignette plus unrelated blur.

The source provides Maximum Blur **15.0**, Stretch Map to Fit **checked**, and Invert Blur **checked** at approximately 11.5 seconds. The menu briefly highlights another layer while open; captions direct selection of the gradient. A hovered menu item must not be mistaken for the completed assignment.

## 4. Photo depth needs more than separated layers

T09 teaches image selection, separation, Clone Stamp repair, spacing in 3D, optional script assistance, and slow camera movement. The missing portions—precise masking, import options, camera creation, compensating apparent size after depth changes, and exact keyframes—must be supplied as proposed completion, not reported as demonstrated clicks. IMG-02 through IMG-04 and WRK-02 preserve that boundary.

# BOOK V — THE ART OF TRANSITIONS

## 1. The fully taught transition: cutting the curve

TRN-01 is the most operational transition in the corpus. Animate the first object with strong easing; parent the second to the first; align the visual handoff; cut at the peak of velocity. The creator’s demonstration pairs a yellow circle and blue square, then shows more complex image-to-illustration examples.

A graph peak is a timing opportunity, not a substitute for composition. The outgoing and incoming subjects still need compatible screen position, scale, and direction. Parent inheritance by itself preserves a child’s offset; it does not guarantee that its visible artwork occupies the same place as the parent’s artwork.

## 2. Other transition families are overview evidence

T05 names or illustrates zooms, slides, and match cuts. Their hidden rigs, masks, keyframes, and exact cut times are not shown. TRN-02 supplies a planning method and clearly labeled reconstruction options. It must not be presented as a second fully demonstrated After Effects tutorial.

## 3. Select between transition methods

| Situation | Select | Why | Constraint |
|---|---|---|---|
| One object changes representation while continuing motion | TRN-01 | Explicit shared movement and peak-speed handoff | Requires registration and a compatible motion path |
| Two shots share composition but need no moving rig | TRN-02 match-cut plan | The visual correspondence can carry continuity | Exact operational workflow is an original completion |
| A detail becomes the next scene’s subject | TRN-02 zoom plan | Scale can connect context and detail | Do not zoom past useful image resolution |
| Two unrelated ideas need a clear boundary | Simple cut, an original editorial choice | Avoids implying a false relationship | A simple cut is not a missing “Vox effect” |

A transition should establish a relationship that exists in the explanation. T05’s support for seamlessness is not a requirement to disguise every boundary.

# BOOK VI — EDITING TIPS, TRICKS & PROFESSIONAL SHORTCUTS

## 1. Small details worth preserving

| Detail | Source | Why it matters / use |
|---|---|---|
| Option-click a property stopwatch to enter an expression | T01, about 16–19 s | Apply code to the intended property; the on-screen instruction is Mac-oriented |
| Use the Transform effect for the demonstrated Position jitter | T01, 15–20 s | Preserves the distinction between an effect transform and a layer transform |
| Position expression samples at 24; its wiggle arguments are 6 and 1 | T01, 20 s | Frequency, amplitude, and sampling are different controls |
| Exposure expression includes an unused `floorTime` variable | T01, 20 s | Its frequency comment does not make the original expression hold values at that frequency |
| Add Grain viewing mode is Final Output | T01, 22 s | Avoids mistaking a preview-region configuration for the full-image result |
| Roughen Edges Border roughly half the stroke width | T02, 27–30 s | Scales the roughness to the line instead of copying an arbitrary large border |
| Animate **Random Seed**, inside Evolution Options | T02, 36–40 s | Do not paste `time*4` into Evolution by mistake |
| Duplicate Turbulent Displace, increase Size, lower Amount | T02, 43–47 s | Separates broad wobble from fine edge chatter |
| Source sound from libraries or record it yourself | T03, 14–16 s | Sound choice is material-based, not tied to a specific product |
| Adjust the levels after arranging audio | T03, 19 s | A sound’s source loudness does not establish its final mix role |
| Multiply gradient plus inverted Compound Blur | T04, 8–15 s | Correct blur polarity is essential to a sharp focus region |
| Parent the second object to the first | T06, 9.5–13 s | Shares the driving motion without separately guessing two curves |
| Make the hard cut at maximum velocity | T06, 13–17 s | Preserves perceived motion through a representation change |
| Save Animation Preset command | T08, 9 s | Reuses selected animator behavior rather than rebuilding it |
| Choose a photograph with clear depth planes | T09, 13–18 s | Makes the separation useful before any camera work |
| Clone Stamp the hidden regions | T09, 21–24.5 s | Prevents holes when the foreground moves away |
| Depth script is optional; manual placement is explicitly allowed | T09, 28–31 s | Do not make a third-party utility a mandatory dependency |
| Posterize Time displays 12.0 | T10, 10–12 s | Gives an explicit frame-sampling treatment, not an export requirement |
| Long easing is visibly asymmetric | T10, 13–16 s | A rapid start and long settling tail differ from symmetric easing |

Windows equivalents and other software shortcuts are not shown. This book does not label them extracted instructions. A context menu’s Copy item in T02 and its caption “duplicate” describe one repeated effect operation; the exact keyboard route is not established.

## 2. Incidental interface versus taught dependency

EaseCopy is visible in some After Effects workspaces but no copying operation through that panel is taught. Photoshop toolbars contain many tools, but T09 specifically names Clone Stamp. T08’s Animate menu contains numerous properties; hovering Stroke Color does not mean that is the chosen property when the expanded animator visibly contains Fill Color.

Quick Chromatic Aberration 3 is explicitly recommended in T10, so FIN-08 records it as a dependency of that particular demonstrated method. Claims that it is free reflect the source clip, not a current price or compatibility check. “Secret Sauce” presets, full YouTube lessons, downloadable files, and follow requests are promotional context; their contents are not available evidence.

## 3. Comparison and apparent contradictions

| Related advice | Preserve separately | Production interpretation (inference) |
|---|---|---|
| T05 recommends constant visual change; T08 warns against too much animated text | Neither advice specifies a measured maximum motion density | Keep progression active while giving the reading target a stable attention window |
| T06 shows strong in/out easing; T10 shows a sharply peaked, long-tail curve | They are different timing examples, not one universal preset | Use the curve suited to a transition or a settling reveal; relocate the cut if the curve changes |
| T01 position code samples at 24; T10 picture effect uses 12 | Expression sampling and image sampling are different scopes | Check the composed output rather than forcing all numbers to match |
| T07 advocates paper texture; T10 says solid fills are rarely used in its examples | These are styling recommendations, not evidence that flat color is forbidden | Preserve contrast; texture is optional when it harms a dense diagram or small type |
| T09 offers Depth and manual spacing | Script UI is shown; full manual construction is not | Choose based on availability and control, with a separate validation pass |
| T02 uses Trim Paths for annotation; T04 uses it for borders | Same operator, different asset and narrative role | Reuse the path-reveal principle while preserving geographic accuracy |

## 4. Hidden lessons, explicitly inferred

| Observation and change | Result visible in the source | Inferred principle | Transfer |
|---|---|---|---|
| T02 reduces Roughen Edges Border from a much larger displayed value to 7.10 | The circle’s contour remains recognizable | Distortion must be judged relative to stroke width | Scale roughness with the annotation, not the canvas alone |
| T02 adds a second displacement with larger Size and reduced Amount | Broader unevenness accompanies fine texture | Spatial frequency and displacement amplitude do different jobs | Use separate passes when one effect cannot independently tune both scales |
| T04 couples gradient position to two attention treatments | Emphasis travels across the map | A shared control reduces contradictory cues | Drive darkening and focus from one intentional target |
| T06 uses one object as another’s parent | Both can follow the same motion through a cut | Common motion control can prevent timing drift | Use one driver for a handoff, then check alignment separately |
| T09 repairs the image behind a separated subject | Camera movement can expose plausible surroundings | Asset preparation must anticipate future visibility | Design the maximum move before finishing the retouch |
| T08 follows attractive type samples with an overloaded example | Competing text weakens reading priority | Local animation quality cannot compensate for attention conflict | Remove or delay a competing event before polishing another curve |

# BOOK VII — COMPLETE TECHNIQUE RECIPES

Each recipe preserves the original demonstrated or caption-supported sequence first. Proposed completions are labeled. Its universal principle follows the original workflow. “No error shown” means the clip does not demonstrate a troubleshooting incident; it does not mean the method cannot fail.

### MOT-01 — Rapid movement with a long settling ease

**Category:** Motion · **Difficulty:** Intermediate · **Software:** After Effects

**Prerequisites:** Transform keyframes and speed graph

**Related:** TRN-01, IMG-01, EDT-05

#### A. What is this technique?

A transform changes quickly early in its movement, then decelerates over a longer tail. This is a timing treatment, not an extra texture or blur effect.

#### B. Problem solved

A constant-speed move can arrive abruptly; an evenly distributed slow move can feel indecisive. The demonstrated graph concentrates speed early while allowing a gentle arrival.

#### C. Finished result

In T10, the graph rises steeply to a narrow peak and slopes gradually toward zero. The visual implication is a brisk initial change followed by increasingly small movements. T06 shows a different, more centrally peaked transition curve; keep the examples distinct.

#### D. Required components

A layer with transform animation, at least a start and end keyframe, and the Graph Editor. These are supported by the UI; the precise property selection and full setup are not all visible in T10.

#### E. Original workflow, gaps, and proposed completion

**Original:** (1) T10 displays an already animated composition and advises smooth ease-ins over a long period. (2) It shows a percentage-per-second speed graph with a steep early peak and long tail, inviting the viewer to copy the easing. The full handle-edit sequence is missing.

**Proposed completion:** Create start/end transform keys for the required composition change. Open the speed graph for that property. Shape the outgoing acceleration and incoming deceleration so most displacement occurs early, then the object approaches the endpoint slowly. Inspect the composition after each handle change; the endpoint must stay fixed and the move must finish before the next reading task. Do not enter the graph-axis maximum as a property value.

#### F. Motion mechanics and software-independent principle

Animate a transform, not the graph itself. The area under a speed curve corresponds to the amount of change; stretching the tail while preserving endpoints redistributes movement in time. The screenshot shows percentage/second units, consistent with a percentage-valued property, but does not justify naming a hidden selection with certainty. Universal principle: allocate speed according to the desired arrival behavior.

#### G. Settings and parameters

**Exact visible:** the graph’s vertical reference reaches 250 %/sec; this is an axis label, not a prescribed peak. **Approximate:** fast early peak, long decay. **Not specified:** influence percentages, exact property endpoints, exact duration, handle coordinates, motion blur.

#### H. Instructor tips

T10, 13–16 s: use smooth, extended easing. It matters when a visual should settle rather than stop mechanically. Apply by matching the curve’s qualitative shape, then judging the actual object movement. T06’s heavy ease-in/out advice belongs to its transition objective.

#### I. Mistakes and troubleshooting

No editing error is shown. **Inferred diagnostics:** an excessively long tail can keep text subtly moving during reading; shorten or finish it earlier. Overshoot is not shown and should not be added merely because a curve is being edited. A zero-speed section in the middle can create an unintended pause.

#### J. Original applications

Bring a archival headline or diagram into its reading position. Combine with TYP-02 after the main move settles. For a fast moving handoff, use TRN-01’s peak-speed rule rather than assuming the cut is at the temporal midpoint.

#### K. Quality evaluation

The arrival is decisive, the endpoint is exact, and the final reading frame is stable. Compare the default interpolation and revised curve at actual playback speed. A pleasing graph that produces unclear motion fails.

#### L. Source and confidence

D/C, high confidence in the shown curve shape and captioned advice; medium confidence in interpreting the selected property. Proposed reconstruction is not execution-tested.

**Source files:** `f1c5ee3e7479d70b0060bc80af8a330c.mp4` (T10, 13–16 s); `719b931f0927612a86eb7b988c09608c.mp4` (T06, 6–9 s).

### SHP-01 — Draw an annotation or border with Trim Paths

**Category:** Shapes · **Difficulty:** Beginner/intermediate · **Software:** After Effects

**Prerequisites:** An editable stroked shape path

**Related:** FIN-04, FIN-05, MAP-02

#### A. What is this technique?

Trim Paths controls the visible portion of a shape path, allowing a line to appear as if it is being drawn. T02 applies it to an annotation; T04 applies it to a regional border.

#### B. Problem solved

An instantaneous complete outline lacks the directional emphasis of a drawing action. A path reveal can indicate which word or region is being selected.

#### C. Finished result

The annotation develops around the target word; the map border develops around the target region. The completed path remains readable. Edge boil in T02 is a later treatment, not the mechanism that draws the line.

#### D. Required components

Shape layer, path, visible stroke, and Trim Paths operator. A newspaper or map supplies context. Path creation, exact stroke width, caps, and every keyframe are not fully taught.

#### E. Original workflow, gaps, and proposed completion

**Original:** (1) Work with an existing shape path. (2) Open the shape layer’s Add menu and choose **Trim Paths**. (3) Show the line developing over time. In T04 the same menu is used for a border.

**Proposed completion:** Prepare an unfilled stroked path around the subject. Place Trim Paths in the shape group containing that path. Hold Start at 0% and animate End from 0% to 100% over your chosen reveal interval. This endpoint pair is an implementation choice, not an extracted parameter pair. Scrub to confirm that the first visible segment starts where the reader should look. If it travels in the wrong direction, revise path direction or use an appropriate range/offset treatment and verify the result.

#### F. Motion mechanics and software-independent principle

The artwork need not translate; its visible path extent changes. The path’s vertex order determines the direction of a basic End reveal. Curves control reveal speed, but no numeric easing is supplied. Universal principle: progressively expose a spatial route instead of merely fading an entire outline.

#### G. Settings and parameters

**Exact:** Add > Trim Paths. **Not specified:** keyframe times, Start/End endpoints, stroke thickness, colors as numeric values, cap style, curve influences. The proposed 0→100% End animation is explicitly a completion.

#### H. Instructor tips

T04, 18–20 s: simple borders can be brought to life with Trim Paths. Use it when identifying a region. T02, 21–25 s: construct the stroke reveal before treating its hand-drawn contour.

#### I. Mistakes and troubleshooting

No explicit error is shown. **Inferred:** putting the operator in the wrong group can animate unrelated paths; isolate the intended group. A filled shape can produce an unexpected filled result. An inaccurate map outline remains inaccurate after a beautiful reveal.

#### J. Original applications

Trace an important source phrase, mark a district, or reveal a diagram connection. Combine with FIN-05 only when a hand-drawn finish helps; technical boundaries may need cleaner edges.

#### K. Quality evaluation

The complete stroke is continuous, the reveal direction is meaningful, and it does not obscure the label. Check the first frame, partial reveal, final frame, and a later hold.

#### L. Source and confidence

D/R, high confidence in operator and intended uses; setup and timing incomplete. All added endpoint choices are I.

**Source files:** `37901357392ee8d7c14db082a78b701d.mp4` (T02, 21–25 s); `4ddac5f4d09320da3574f855072240ad.mp4` (T04, 18–20 s).

### FIN-01 — Subtle global Position jitter

**Category:** Finishing · **Difficulty:** Intermediate · **Software:** After Effects

**Prerequisites:** 2D effect Position and expression entry

**Related:** WRK-03, FIN-02, FIN-03, FIN-09

#### A. What is this technique?

A time-driven expression introduces small horizontal and vertical changes to the Transform effect’s Position. The clip relates this to film gate weave.

#### B. Problem solved

Perfectly fixed digital compositions can feel sterile within a tactile treatment. Small global movement adds irregularity without rebuilding the scene’s individual animations.

#### C. Finished result

The composition continues its intended animation while its overall image shifts subtly. It should feel slightly unstable at the frame level, not like a camera searching for the subject.

#### D. Required components

An existing composition, a finishing layer called “Vox Sauce” in the example, **Distort > Transform**, and an expression on the effect’s 2D Position. The exact creation of the finishing layer is skipped.

#### E. Original workflow, gaps, and proposed completion

**Original:** (1) Search for Transform in Effects & Presets; the Distort effect is shown. This supplies a separate image transformation. (2) Open Transform > Position and Option-click its stopwatch. The expression editor becomes available. (3) Enter the displayed code:

```javascript
posterizeTime(24);
x = wiggle(6,1)[0];
y = wiggle(6,1)[1];
[x,y];
```

(4) Preview the subtly moving composition. Verify the expression is on **effect Position**, not Exposure or Scale.

**Gap / proposed completion:** If rebuilding the global treatment, arrange a finishing adjustment or precomposition-based layer so the effect reaches the intended image. Test scope by temporarily increasing movement, then restore subtle values. The source’s full layer setup is not shown.

#### F. Motion mechanics and software-independent principle

`wiggle(6,1)` supplies frequency and amplitude arguments; `[0]` and `[1]` take the X and Y components. The final array supplies a 2D position. `posterizeTime(24)` limits expression evaluation sampling; it is not the 12 fps Posterize Time effect. Universal principle: perturb the whole image by a small amount around its intended position.

#### G. Settings and parameters

**Exact code values:** 24, 6, 1. **Visible project state:** effect Anchor Point 540,960; Scale 103.0 appears around 19 s. These are composition-specific and the scaling action is not explained. **Not specified:** a universal resolution-scaled amplitude, expression duration, or mandatory overscan.

#### H. Instructor tips

T01, 15–20 s: two small expressions are presented as a simple route to the treatment. Use the position one for movement and the exposure one for brightness; putting both on one property does not reproduce the demonstration.

#### I. Mistakes and troubleshooting

No error shown. **Inferred:** edge slivers may appear when the image shifts beyond its bounds; add only enough overscan to cover the maximum movement. The visible 103% scale may serve that role, but its intent is not confirmed. A 2-component result is not a complete 3D Position expression.

#### J. Original applications

Add a mild archival instability to a photograph-and-document sequence. Keep critical small captions legible; leave a precise technical chart steadier if jitter harms comparison.

#### K. Quality evaluation

No exposed frame edges, expression errors, or distracting drift. Compare on/off at delivery size. The treatment should survive a pause without making the composition misaligned.

#### L. Source and confidence

D/C, high confidence in code transcription and effect target; layer setup and overscan purpose are incomplete/inferred.

**Source files:** `017833d6758add159d297d753e03e084.mp4` (T01, 4–8 s; 15–20 s).

### FIN-02 — Exposure flicker, with an original-code caveat

**Category:** Finishing · **Difficulty:** Intermediate · **Software:** After Effects

**Prerequisites:** Exposure effect and expressions

**Related:** FIN-01, FIN-03, WRK-03

#### A. What is this technique?

The Exposure property receives random small positive and negative values. T01 presents it as exposure flicker associated with early film.

#### B. Problem solved

Uniform brightness can feel too mechanically consistent for the intended film treatment. Slight variations add temporal imperfection.

#### C. Finished result

The whole treated image fluctuates gently in brightness while retaining readable contrast. No large flashes or total exposure swings are the demonstrated goal.

#### D. Required components

Exposure effect, its Master Exposure property, expression editor, and image content. The source uses a global finishing stack; full layer setup is omitted.

#### E. Original workflow, gaps, and proposed completion

**Original:** Enable an expression on Exposure and use the displayed slide. Transcription, preserving its logic:

```javascript
seedRandom(index + time, true);
flickerStrength = 0.04; // adjust: 0.02 - 0.1 for subtlety
freq = 2;             // flicker frequency per second

holdTime = 1 / freq;
floorTime = Math.floor(time / holdTime) * holdTime;
randomVal = random(-flickerStrength, flickerStrength);

randomVal
```

The screenshot has line wrapping; the code above preserves the variables, values, and operations. **Important source defect:** `floorTime` is calculated but never used. `freq` therefore does not actually control a held interval in this displayed code; the seed still depends on continuous `time`.

**Proposed correction, not the creator’s code:** if the intended result is a new held exposure value twice per second, use a quantized seed:

```javascript
flickerStrength = 0.04;
freq = 2;
stepIndex = Math.floor(time * freq);
seedRandom(index + stepIndex, true);
random(-flickerStrength, flickerStrength);
```

Test both versions on the same image. Choose based on intended cadence. This correction has been reasoned from the code, not executed in After Effects.

#### F. Motion mechanics and software-independent principle

The output is scalar brightness variation, independent of spatial jitter. The original seed changes with time; the corrected proposal changes only at discrete intervals. `true` makes the random sequence independent of implicit time evolution, but explicitly adding `time` to the seed still varies the seed. Universal principle: separate amplitude from update cadence and ensure the cadence variable actually participates in the output.

#### G. Settings and parameters

**Exact slide:** strength 0.04; suggested comment range 0.02–0.1; frequency variable 2. **Visible evaluated state:** Exposure 0.02 in a later frame, not a fixed target. Offset 0.0000 and Gamma 1.00 are visible supporting settings. **Not specified:** rendered fluctuation frequency of the entire downstream stack.

#### H. Instructor tips

T01, 20 s: keep the strength small; the code comment supplies the subtlety range. Use when mild brightness variation adds material character. The frequency comment describes intention, but the actual original expression must be audited before promising two changes per second.

#### I. Mistakes and troubleshooting

The creator does not diagnose the unused variable. **Analysis here:** changing `freq` in the original does not affect the returned value through `floorTime`; it can create false confidence in a rate control. **Other inferred check:** if text contrast noticeably pulses, reduce strength or restrict the effect’s scope.

#### J. Original applications

Use on an archival montage with FIN-01 and FIN-03. Prefer stable exposure for a sequence requiring exact visual comparison of similar shades. Do not add flicker solely because a “Vox” stack exists.

#### K. Quality evaluation

The code runs without errors, the intended cadence is observable, and neither bright nor dark sampled states destroys information. A successful correction makes changing frequency visibly affect hold lengths.

#### L. Source and confidence

D/C, high confidence in the slide values and unused-variable finding. Proposed correction is I and requires application testing. No audible explanation was independently checked.

**Source files:** `017833d6758add159d297d753e03e084.mp4` (T01, 18–20.5 s; 22 s).

### FIN-03 — Add a restrained grain finish

**Category:** Finishing · **Difficulty:** Beginner · **Software:** After Effects

**Prerequisites:** Effects panel and delivery-size preview

**Related:** FIN-01, FIN-02, FIN-07

#### A. What is this technique?

Add Grain introduces fine image noise as a finishing treatment after the expression demonstrations.

#### B. Problem solved

Very clean layers can feel disconnected from a tactile or archival presentation. Fine grain can make the assembled image feel more materially consistent.

#### C. Finished result

The same composition remains visible with a small surface texture. The grain should be subordinate to text and subject edges.

#### D. Required components

Add Grain effect and a layer that affects the intended image. Grain is visible within a broader pre-existing finishing stack, so the before/after cannot isolate every effect.

#### E. Original workflow, gaps, and proposed completion

**Original:** Search for and apply Add Grain; open its controls; use Viewing Mode **Final Output**; adjust Tweaking > Intensity while viewing the picture. Size, Softness, and Aspect Ratio remain visibly at 1.000. Intensity is actively scrubbed—0.000 and 0.300 are visible at different moments. Verify the effect is evaluated across the image rather than judged only from a small preview region.

**Proposed completion:** Disable other finishing effects for one comparison to judge what grain alone adds, then restore the stack. Inspect at delivery size and after a short export; this isolation/export check is not shown in the clip.

#### F. Motion mechanics and software-independent principle

This recipe adds surface variation rather than purposeful object movement. Animation settings for the grain itself are not opened sufficiently to recover a temporal recipe. Universal principle: use controlled fine texture to tie layers together without changing their informational structure.

#### G. Settings and parameters

**Exact visible:** Final Output; Preset [None]; Size 1.000; Softness 1.000; Aspect Ratio 1.000. **Exact intermediate samples:** Intensity 0.000 and 0.300; these show an adjustment, not a universally prescribed final value. **Not specified:** complete grain animation settings or final delivery compression.

#### H. Instructor tips

T01, 21–23 s: add a little grain after the position/exposure treatment. It matters when the finish still looks too clean; apply conservatively and judge the whole picture.

#### I. Mistakes and troubleshooting

No error shown. **Inferred:** grain can make tiny text shimmer or disappear in compression. Lower intensity or isolate the finish if the information becomes less readable. A paused enlarged preview can exaggerate the perceived texture.

#### J. Original applications

Finish mixed archival photographs and graphics. Combine with FIN-07’s paper treatment only if the two texture scales remain distinguishable. Paper texture need not imply heavy digital grain.

#### K. Quality evaluation

The treatment remains fine, consistent, and unobtrusive through motion and export. If the viewer notices crawling noise before the emphasized phrase, it is too strong for that scene.

#### L. Source and confidence

D/C, high confidence in effect and readable control states; exact final Intensity and grain temporal settings remain unresolved.

**Source files:** `017833d6758add159d297d753e03e084.mp4` (T01, 21–23 s).

### FIN-04 — Roughen a drawn stroke before animating its edge

**Category:** Finishing · **Difficulty:** Intermediate · **Software:** After Effects

**Prerequisites:** A stroked annotation shape

**Related:** SHP-01, FIN-05, FIN-06

#### A. What is this technique?

Roughen Edges modifies the contour of an annotation so it resembles a less uniform drawn mark. This static preparation is distinct from the subsequent animated boil.

#### B. Problem solved

A perfectly smooth vector circle can look disconnected from a rough newspaper or hand-marked aesthetic.

#### C. Finished result

The circle remains a clear annotation around the word, but its edge is less geometrically perfect. Later displacement gives it changing motion.

#### D. Required components

Existing stroke shape and Roughen Edges. The newspaper supplies context; it does not need the effect. No external brush or plugin is established as necessary.

#### E. Original workflow, gaps, and proposed completion

**Original:** (1) Start with the already created blue circular annotation. (2) Apply **Roughen Edges**. (3) Adjust Border; captions say roughly **half your stroke width**. (4) The controls settle into a readable state with Border 7.10 and Edge Sharpness 5.67. A larger Border 36.10 appears during adjustment. Check that the circle’s intended line remains intact.

**Gap / completion:** Actual stroke width is not clearly established. Measure your own stroke width and use the half-width advice as the starting relationship; the example’s 7.10 is not evidence that all strokes should use that number.

#### F. Motion mechanics and software-independent principle

No temporal driver is established in this stage. The operation changes the stroke’s spatial contour. Universal principle: create imperfections at a scale appropriate to the mark’s thickness before adding temporal variation.

#### G. Settings and parameters

**Exact visible:** Edge Type Roughen; Border 7.10 and Edge Sharpness 5.67 at about 29.5 s; Border 36.10 in an earlier adjustment. **Caption relationship:** Border approximately half stroke width. **Not specified:** full remaining effect settings and stroke width.

#### H. Instructor tips

T02, 27–30 s: relate Border to half the stroke width. This matters when moving the effect between thick circles and thin arrows. Apply the proportional relationship first, then inspect whether the line remains continuous.

#### I. Mistakes and troubleshooting

No explicit error diagnosis. **Inferred from adjustment:** too much border treatment can consume or shred the line; decrease Border before compensating by blindly thickening every stroke. Do not infer that the peach Edge Color swatch controls the blue line under every Edge Type.

#### J. Original applications

Use on editorial circles, arrows, and hand-marked diagrams. A measured engineering boundary may benefit from the cleaner SHP-01 result instead.

#### K. Quality evaluation

The annotation remains legible and continuous at viewing size; roughness adds character without making the mark look damaged or inaccurately placed.

#### L. Source and confidence

D/C, high confidence in half-width instruction and readable values. Why the creator chose the particular sharpness value is not explained.

**Source files:** `37901357392ee8d7c14db082a78b701d.mp4` (T02, 24–30 s).

### FIN-05 — Animate fine edge boil through Random Seed

**Category:** Finishing · **Difficulty:** Intermediate · **Software:** After Effects

**Prerequisites:** FIN-04, effect expressions

**Related:** FIN-04, FIN-06, WRK-03

#### A. What is this technique?

A small-scale Turbulent Displace pass changes the annotation’s contour over time. Its **Random Seed** is expression-driven.

#### B. Problem solved

A single roughened still contour can still look frozen. Repeated contour changes evoke separately drawn frames without redrawing the artwork by hand.

#### C. Finished result

The circular mark stays around the same word while small edge variations continually change. The result is surface activity rather than the entire circle traveling across the page.

#### D. Required components

A stroked annotation, preceding Roughen Edges, Turbulent Displace, and Random Seed under Evolution Options. The fine displacement follows Roughen Edges in the demonstrated progression.

#### E. Original workflow, gaps, and proposed completion

**Original:** Apply Turbulent Displace. Set Displacement to Turbulent; increase Amount to **80.0** and reduce Size to **2.0**. Expand **Evolution Options**, expose **Random Seed**, enable its expression, and type:

```javascript
time*4
```

Preview the changing annotation. Verify that the expression belongs to Random Seed; the visible Evolution value remains 0x+0.0° in the setup. The source does not teach a separate keyed Evolution animation.

#### F. Motion mechanics and software-independent principle

`time*4` advances the seed-control value by four units per second. That is not sufficient evidence to promise exactly four finished drawing changes per second: the property’s handling of fractional values and the composition’s temporal sampling affect the visible result. Universal principle: vary the distortion pattern while holding the annotation’s narrative position stable.

#### G. Settings and parameters

**Exact:** Amount 80.0; Size 2.0; Complexity 1.0; Offset 540.0,960.0; Evolution 0x+0.0° in the shown setup; expression `time*4`. **Not specified:** independently measured boil cadence or all render-quality settings. Offset is composition-specific.

#### H. Instructor tips

T02, 36–40 s: animate Random Seed to produce the frame-to-frame variation. Use after the static stroke is visually correct. The clip’s small Size creates fine disturbance; do not confuse Size with an output scale percentage.

#### I. Mistakes and troubleshooting

No error shown. **Inferred:** animating Evolution instead changes the nature of the pattern motion and is not the recorded recipe. Applying this to the newspaper itself distorts source text; keep the effect scoped to the mark. Excessive edge activity can look like noise.

#### J. Original applications

Make arrows, circles, and diagram annotations feel hand-drawn. Pair the initial SHP-01 reveal with a continuing boil after the stroke finishes; that is consistent with the demonstrated layered approach.

#### K. Quality evaluation

The marked target stays clear, the contour changes, and line thickness remains usable. Check both a paused frame and several seconds of movement. If the whole word seems to wobble, the effect scope is probably wrong.

#### L. Source and confidence

D/C, high confidence in effect target and parameters. Exact temporal quantization and unshown property behavior require testing.

**Source files:** `37901357392ee8d7c14db082a78b701d.mp4` (T02, 30–42 s).

### FIN-06 — Add broader wobble with a second displacement pass

**Category:** Finishing · **Difficulty:** Intermediate · **Software:** After Effects

**Prerequisites:** FIN-05 working on a stroke

**Related:** FIN-04, FIN-05

#### A. What is this technique?

A duplicate Turbulent Displace effect is adjusted to operate at a larger spatial scale with a lower displacement amount.

#### B. Problem solved

The first small-size pass makes a lively edge but may not provide the broader hand-drawn movement the creator wants.

#### C. Finished result

Fine edge changes remain, while the overall circular contour has larger, gentler unevenness. The mark must still surround its target.

#### D. Required components

Existing fine-boil effect and a second Turbulent Displace on the same stroke. No second shape layer is required by the shown method.

#### E. Original workflow, gaps, and proposed completion

**Original:** The creator recommends duplicating Turbulent Displace; a context-menu Copy action is visible and a **Turbulent Displace 2** subsequently appears. Increase the duplicate’s Size and lower its Amount. The UI passes through Size 50.0 then 52.0; Amount is scrubbed down from 80.0, with different smaller values visible. Check the result in the composition rather than adopting an arbitrary value from the middle of a drag.

**Gap / proposed completion:** The copied expression’s complete state is not reopened. Confirm that the intended Random Seed animation exists on the second pass if a changing broad contour is desired. The source does not provide a clean final preset card for this pass.

#### F. Motion mechanics and software-independent principle

Size sets the spatial scale of the distortion pattern; Amount determines displacement strength. A larger pattern need not have a larger strength. Universal principle: use separate frequency bands of imperfection so fine texture and broad deformation can be tuned independently.

#### G. Settings and parameters

**Exact observed states:** duplicate Size 50.0 and 52.0; Amount 80.0 before reduction; smaller states include 21.0 in survey frames and 16.0 in a later dense sample. Treat these as a live adjustment sequence, not a definitive final value. **Caption-supported:** increase Size, lower Amount. **Not specified:** final committed Amount.

#### H. Instructor tips

T02, 43–47 s: duplicate, increase Size, reduce Amount when more movement is wanted. It matters when fine edge chatter is insufficient but increasing the first pass would merely damage the line.

#### I. Mistakes and troubleshooting

No error shown. **Inferred:** copying the effect without reducing Amount can produce overly large excursions. Two aggressive passes can cause edge clipping or overlap the text; reduce the broad pass first. Do not replace the original Size 2.0 if the aim is to preserve both scales.

#### J. Original applications

Use on loose illustrative annotations. Omit it for tight text underlines or borders where broad movement could misidentify the target.

#### K. Quality evaluation

The mark remains semantically accurate throughout the loop, with no broken contour or off-target drift. Fine and broad changes should feel related rather than like a liquid warp.

#### L. Source and confidence

D/C, high confidence in duplication strategy and direction of adjustments; final numeric amount and retained expression state are incomplete.

**Source files:** `37901357392ee8d7c14db082a78b701d.mp4` (T02, 42–48 s).

### MAP-01 — Move a radial Multiply spotlight across a map

**Category:** Maps · **Difficulty:** Intermediate · **Software:** After Effects

**Prerequisites:** Prepared map and blend modes

**Related:** MAP-02, SHP-01, EDT-05

#### A. What is this technique?

A radial gradient overlays a map in Multiply mode. Its lighter center leaves the target relatively bright while darker surroundings recede.

#### B. Problem solved

A map with several equally strong regions offers little reading priority. The moving gradient directs attention without removing the rest of the geography.

#### C. Finished result

The map remains recognizable; emphasis travels toward the relevant region. In the shown example, labeled districts such as NODA and UPTOWN compete until the focus treatment separates one from its surroundings.

#### D. Required components

Prepared map; radial gradient layer; Multiply blending; an animated gradient center. The source’s map, texture, and highlight construction predates this demonstration.

#### E. Original workflow, gaps, and proposed completion

**Original:** Create a radial gradient layer; set its blend mode to **Multiply**. Later, animate the gradient’s center. The timeline exposes **Start Point** on the “Radial gradient” layer, with animation enabled. Verify that a lighter central area preserves the map while the surrounding field darkens it.

**Gap / proposed completion:** The exact gradient creation dialog and colors are not shown. Build a light-centered, darker-edged gradient large enough to cover the frame. Place it over the map. Choose start and end focus positions based on the places mentioned by the narration. Keyframe the center between those positions and inspect both endpoints before adjusting the motion curve. If using a different gradient implementation, confirm which control moves the center.

#### F. Motion mechanics and software-independent principle

The map may stay still while the control field moves. In Multiply, light portions preserve more of the underlying image than dark portions; the effect is relative emphasis, not a simulated physical light source. Universal principle: animate an attention field independently from the underlying information.

#### G. Settings and parameters

**Exact:** Multiply; layer name Radial gradient; Start Point animated. A visible point reads approximately 293.2,487.2 at one project time; it is not a reusable destination. **Not specified:** colors, radius, endpoint times, speed curve, original map dimensions.

#### H. Instructor tips

T04, 6–9 s: a radial gradient in Multiply is the basic attention trick. T04, 14.5–17 s: animate its center to move the emphasis. Use when retaining regional context matters more than tightly cropping the map.

#### I. Mistakes and troubleshooting

No explicit error shown. **Inferred:** a reversed gradient can darken the target; inspect polarity before animating. Too small a radius can clip a region’s label from the focus area. Texture should not obscure the location names.

#### J. Original applications

Follow a narration comparing neighborhoods, river basins, or regions. Add SHP-01 for a specific boundary and MAP-02 for selective clarity. These combinations preserve the source’s map-focused approach.

#### K. Quality evaluation

The target is obvious at each hold, surrounding geography remains useful, and the traveling focus does not imply that locations physically move.

#### L. Source and confidence

D/C, high confidence in gradient, Multiply, and animated Start Point. Gradient construction and final timing are incomplete.

**Source files:** `4ddac5f4d09320da3574f855072240ad.mp4` (T04, 0–9.5 s; 14.5–17 s).

### MAP-02 — Use the gradient as an inverted Compound Blur map

**Category:** Maps · **Difficulty:** Intermediate · **Software:** After Effects

**Prerequisites:** MAP-01 and adjustment-layer scope

**Related:** MAP-01, SHP-01

#### A. What is this technique?

Compound Blur uses another layer’s luminance as a spatial blur control. T04 assigns the radial gradient and shows inverted blur polarity.

#### B. Problem solved

Brightness alone may not separate a focal map region strongly enough. Selective sharpness reinforces the same target.

#### C. Finished result

The central emphasized area stays clearer; surrounding map areas soften. As the gradient center moves, the area of clarity moves with it.

#### D. Required components

Radial gradient, Compound Blur on an adjustment layer, and map imagery below the affected layer. Foreground annotations can remain above that adjustment. The visible project has many pre-existing layers that are not needed to understand the sub-rig.

#### E. Original workflow, gaps, and proposed completion

**Original:** (1) Create an Adjustment Layer using the New menu. (2) Apply **Compound Blur**. (3) Open **Blur Layer** and choose the gradient, as instructed by captions. (4) Animate the gradient center to move the result. At about 11.5 s, controls visibly read **Maximum Blur 15.0**, **Stretch Map to Fit checked**, and **Invert Blur checked**. The open dropdown briefly highlights another layer during navigation; the instruction explicitly identifies the gradient.

**Verification before animation:** the bright center must be the clearer region. If the center is more blurred, resolve the polarity or assignment before tuning timing.

**Proposed completion:** Place the adjustment to affect only the desired map content, keep crisp labels or borders above it if appropriate, and test the map layer sampling in the actual project. If the chosen gradient is generated by effects and the blur input does not reflect it, use a rendered/precomposed control field or the applicable layer-source option; this compatibility fix is not demonstrated.

#### F. Motion mechanics and software-independent principle

The same field controls visible darkening and blur distribution. Inverting the mapping changes which brightness range receives stronger blur. Universal principle: one spatial control can synchronize different attention cues. Changing Maximum Blur does not move the focus center.

#### G. Settings and parameters

**Exact visible state:** Maximum Blur 15.0, Stretch Map to Fit on, Invert Blur on. **Exact instruction:** gradient as Blur Layer. **Not specified:** every layer-source option, focus radius, complete final ordering of all map layers, animation durations.

#### H. Instructor tips

T04, 11–14.5 s: select the gradient from the dropdown. It matters because an unrelated input will create an unrelated blur pattern. Use the same gradient when brightness and sharpness should point to the same region.

#### I. Mistakes and troubleshooting

No error shown. **Inferred:** a source assignment of None or the hovered “Vox Sauce” entry will not reproduce the instructed map. Incorrect adjustment placement may soften labels or eyes that should stay crisp. Fix scope and polarity before merely reducing Maximum Blur.

#### J. Original applications

Use for a map with dense neighboring information. For two equally important regions, a single moving focus may be misleading; use sequential holds or a separately designed multi-region control, labeled as an original extension.

#### K. Quality evaluation

Correct region clear, context softly present, no abrupt boundary in blur, and no unintended degradation of labels. Pause at every narrative location and check the bright and sharp regions coincide.

#### L. Source and confidence

D/C, high confidence in checked controls and instructed input. The exact completion of the dropdown and input-source behavior need project verification.

**Source files:** `4ddac5f4d09320da3574f855072240ad.mp4` (T04, 9.5–17 s).

### TRN-01 — Hard cut at peak velocity with shared parenting

**Category:** Transitions · **Difficulty:** Intermediate · **Software:** After Effects

**Prerequisites:** Position keyframes, speed graph, Parent & Link

**Related:** MOT-01, TRN-02, EDT-05

#### A. What is this technique?

Two objects share a movement, but visibility switches from the first to the second at the movement’s highest speed. The creator calls this cutting the curve.

#### B. Problem solved

A representation change can feel disconnected if the incoming subject starts a new unrelated move or stops the outgoing momentum.

#### C. Finished result

The yellow circle moves into the fast part of its curve, becomes a blue square through a hard cut, and the square continues toward the eased finish. Image-to-illustration examples apply the same continuity idea.

#### D. Required components

Two objects or compatible scene elements, a Position animation on the first, a parent link from second to first, and layer in/out points or equivalent visibility timing. The first remains available as a motion driver even when it is no longer visible.

#### E. Original workflow, gaps, and proposed completion

**Original:** (1) Animate the first object with heavy ease-in and ease-out; inspect its speed graph. (2) Use **Parent & Link** to parent the second object to the first. Captions explicitly say this matches speed and position. (3) Find the peak of velocity in the graph. (4) Make a **hard cut** there: outgoing visible segment ends where incoming begins. The source shows an abutting handoff, not a dissolve.

**Missing alignment / proposed completion:** Register the visible subjects at the handoff. Parenting inherits transformations but retains a child’s spatial relationship; it does not magically align unrelated artwork. Check anchor points, scale, and local offset at the cut. Keep the driver’s animation intact across the whole move. Inspect the frame before, at, and after the cut, then play the sequence at speed. Do not shift the incoming animation to restart at its own in-point.

#### F. Motion mechanics and software-independent principle

One continuous motion trajectory underlies two visible identities. The outgoing object carries acceleration; the incoming object carries continuation/deceleration. A speed-graph peak marks maximum speed, not necessarily halfway in time. For the same direction, the velocity’s direction also needs to agree. Universal principle: change appearance while preserving the motion relationship that the viewer is tracking.

#### G. Settings and parameters

**Exact instruction:** strong easing, second parented to first, hard cut at peak velocity. **Not specified:** keyframe times, influence values, screen-space endpoints, prescribed speed, or motion-blur settings. Axis labels in pixels/second are example measurements, not a global target.

#### H. Instructor tips

T06, 9.5–13 s: parent the second object to the first to coordinate motion. T06, 13–17 s: cut at peak velocity. Use for an object-to-illustration or symbol-to-source handoff where continuity has explanatory value.

#### I. Mistakes and troubleshooting

No explicit failed cut is shown. **Inferred:** a double-visible frame creates a flash; a gap creates an empty frame; a child offset produces a jump. A fade is a different transition. Deleting the parent after the cut may break the intended driver relationship.

#### J. Original applications

Change a ship photograph into a route diagram, a photographed machine into a labeled schematic, or a source headline into a graphic statement. Use new assets that share a meaningful focal point rather than copying the example.

#### K. Quality evaluation

The focal subject occupies a compatible place through the cut, direction and apparent speed remain continuous, and no gap or overlap appears. The destination settles into a readable frame.

#### L. Source and confidence

D/C/R, high confidence in parenting and cut timing. Artwork alignment and complete layer visibility operations are partly inferred completion.

**Source files:** `719b931f0927612a86eb7b988c09608c.mp4` (T06, 0–21 s).

### EDT-01 — Build tactile sound around visible material actions

**Category:** Editing/audio · **Difficulty:** Beginner/intermediate · **Software:** Premiere-style timeline; After Effects also visible

**Prerequisites:** Timeline audio placement and suitable sound files

**Related:** SHP-01, IMG-01, FIN-07

#### A. What is this technique?

Short material-related sounds accompany graphic actions: paper movement, marker-like contact, camera mechanisms, and tape or cassette operations. This is the creator’s tactile sound design concept.

#### B. Problem solved

Graphic movement alone may lack a tangible sense of contact or material. A relevant sound can reinforce the action and its timing.

#### C. Finished result

The source shows physical sound categories, recording near a microphone, and multiple audio clips placed beneath picture. The final audible character cannot be described as verified here because audio was not auditioned.

#### D. Required components

A visual action, matching sound file or self-recording, separate audio tracks, and gain controls. Sound libraries are optional sources. Exact recording microphone settings, sample format, EQ, compression, and final loudness are not supplied.

#### E. Original workflow, gaps, and proposed completion

**Original:** (1) Identify tangible sound categories. (2) Find sounds through Freesound or Soundly, or record them yourself. (3) Place sound clips on the editing timeline beneath the video; paper movement and another mechanical-sounding file name are visible. (4) Adjust clip levels; captions explicitly direct this action.

**Proposed completion:** Mark the visual event’s contact/onset frame. Trim and position a candidate sound so its meaningful onset corresponds to that action, not merely its file start. Audition under narration, adjust level, and add a second layer only if it contributes a separate useful texture or impact. This synchronization and listening procedure is a practical completion; exact original onset offsets were not recovered.

#### F. Motion mechanics and software-independent principle

The audio event is coordinated with a visual event. Transient alignment, length, and overlap influence the perceived weight of the action, but no measured synchronization offset is established. Universal principle: use sound with a material analogy and a clear temporal relationship to the image.

#### G. Settings and parameters

**Exact visible moment:** a level tooltip reads 7.8 dB around 19 s during a drag. It is an intermediate adjustment, not a target mix level, loudness standard, or safe recommendation for every source. **Not specified:** final gain, peak ceiling, integrated loudness, EQ, fades, music mix.

#### H. Instructor tips

T03, 9–16 s: choose tactile source families; obtain library sounds or self-record. T03, 19 s: adjust levels. Use when a paper reveal, annotation, or mechanical graphic has a distinct material action. Current availability or licensing of named services is not verified by this book.

#### I. Mistakes and troubleshooting

No audible problem was verified. **Inferred:** a loud transient can mask a narrated word; rebalance by listening. A long file’s first sample may precede its meaningful event. Repeating an identical sound on every unrelated action can become distracting.

#### J. Original applications

Pair a page reveal with paper movement or a drawn annotation with a soft writing-related sound. The exact pairing is an original design choice. Do not add sound to every frame of edge boil; the source does not teach that.

#### K. Quality evaluation

Required listening gate: narration remains intelligible, onsets feel intentional, no clicks or clipped peaks appear, and the sound suggests the visible material. The present analysis cannot certify that gate for the tutorial’s own mix.

#### L. Source and confidence

D/C, high confidence in listed categories and timeline level adjustment; no auditory verification. Audio timing and final mix confidence remain low until auditioned.

**Source files:** `4b14c84e681d7c91605262059df0d9f3.mp4` (T03, 0–22 s).

#### EDT-01 reference bank — the source’s tactile sound list

At approximately T03 13 s, the on-screen list contains: paper movement; circuit breaker on; quick page flick; sticky note peel; film camera shutter snap; Polaroid eject pop; VHS cassette snap-in; typewriter; mechanical button click; pencil scratch; chalk drag; zipper; cloth movement; coin spin on table; wood block tap; drawer slam; light switch flick; Velcro rip; box lid pop open; match strike.

This is a material vocabulary, not twenty separately demonstrated recording or mixing workflows. File licensing, recording conditions, and sound quality must be checked when choosing actual assets. The source’s suggested destinations are named for traceability, not presented as verified current service recommendations.

### EDT-02 — Translate narrated claims into explanatory visual assets

**Category:** Editorial · **Difficulty:** Beginner · **Software:** Construction software not shown

**Prerequisites:** A script and relevant evidence/assets

**Related:** EDT-03, EDT-04, IMG-01, MAP-01, TYP-02

#### A. What is this technique?

Choose visible representations for the script’s numbers, places, historical events, and relationships. The tutorial separately emphasizes visualizing information and using motion design to explain ideas.

#### B. Problem solved

An uninterrupted speaker or decorative montage may not expose what the sentence is asking the audience to understand.

#### C. Finished result

Numbers appear as explicit figures, places as maps, source claims as articles, and relationships as diagrams or cutout compositions. The source montage demonstrates possible asset categories, not their production steps.

#### D. Required components

Narration or script; suitable maps, source documents, photographs, type, or diagrams. No specific software, chart plugin, or asset pack is established.

#### E. Original workflow, gaps, and proposed completion

**Original conceptual sequence:** T05 first recommends visualizing the information, including numbers, places, and history. It then shows motion design using maps, newspapers, diagrams, and cutout photographs. No interface construction is shown.

**Proposed completion:** Underline the sentence’s main relationship: location, comparison, change, sequence, or attribution. Select the simplest asset that makes that relationship visible. Prepare a beginning and ending frame before animating. Verify the visual actually supports the claim; a number on screen alone does not demonstrate growth, and an unrelated archive image is not evidence of the stated event.

#### F. Motion mechanics and software-independent principle

Motion is used to reveal or organize a relationship, not prescribed as one property. Universal principle: match the visual representation to the informational job. A diagram requires its own validated structure; the examples do not establish a chart-animation algorithm.

#### G. Settings and parameters

**Exact:** no operational values supplied. **Not specified:** frame durations, chart geometry, quantitative scaling, animation rig, masks, or data source. Any build values in an original scene must be labeled original.

#### H. Instructor tips

T05, 4–15 s: visualize different information types. T05, 15–26 s: use motion design to explain ideas. It matters when the viewer needs to see a relationship; choose the visual form according to the sentence, then retrieve a relevant practical recipe.

#### I. Mistakes and troubleshooting

No technical correction is shown. **Inferred:** avoid literal illustration that adds no explanation. Do not infer exact chart construction from a montage of circles with numbers. Verify facts independently when producing a real documentary scene.

#### J. Original applications

For “the city expanded north,” choose a map comparison rather than a generic skyline. For “the article made a claim,” use IMG-01 and TYP-01. The decisions are original applications of the source advice.

#### K. Quality evaluation

The audience can identify the same main idea from the image and narration. The asset is relevant, readable, and does not suggest unsupported quantities or causation.

#### L. Source and confidence

C/R, high confidence in the two editorial recommendations; operational implementation is I. No chart/cutout construction should be attributed to T05.

**Source files:** `67d5920a705ab69ca0840d5c0223e283.mp4` (T05, 4–26 s).

### EDT-03 — Plan ongoing visual progression without losing reading time

**Category:** Editorial · **Difficulty:** Beginner · **Software:** Construction software not shown

**Prerequisites:** Script beats and a rough edit

**Related:** EDT-02, EDT-05, IMG-01

#### A. What is this technique?

The scene changes as the explanation progresses: a crop moves, a source is emphasized, a location changes, or a new element enters. This is broader than cutting constantly.

#### B. Problem solved

A static image that outlasts its informational job can stall the visual explanation. Conversely, constant competing motion can prevent reading.

#### C. Finished result

T05’s montage keeps introducing or reframing information. T08’s overloaded typography example shows the competing risk: several animated words demand attention at once.

#### D. Required components

A rough edit, a sequence of meaningful beats, and assets that can reveal additional information. No automated pacing tool or exact cut interval is taught.

#### E. Original workflow, gaps, and proposed completion

**Original:** T05 recommends that something keep changing and illustrates moving images, labels, maps, and highlights. Its claim that this helps viewer retention is instructor advice, not a measured guarantee. T08 separately warns against overwhelming animated text.

**Proposed completion:** Mark each new information beat. Assign one visual change to that beat: reveal, reframe, replace, or emphasize. Keep the target stable while the viewer must read it. Review a silent pass to see whether changes guide the eye and a narrated pass to check whether they arrive with the explanation. Remove changes that merely reset attention without adding information.

#### F. Motion mechanics and software-independent principle

Timing is editorial: which change follows which sentence. No single transform curve is prescribed. Universal principle: progression should track information density, while reading holds protect comprehension.

#### G. Settings and parameters

**Caption-supported qualitative guidance:** scenes rarely remain unchanged for long in the creator’s examples. **Not specified:** compulsory seconds per shot, cuts per minute, overlap duration, or retention statistics.

#### H. Instructor tips

T05, 26–40 s: ongoing visual change supports pace. Use when a static scene needs progression. T08, 22–26 s: avoid simultaneously competing type. Apply by choosing a primary event rather than animating every available layer.

#### I. Mistakes and troubleshooting

T08 explicitly presents overload as a problem. **Inferred fixes:** delay supporting text, stop background motion during a dense quote, or remove a redundant move. Cutting faster is not automatically a solution to a confusing scene.

#### J. Original applications

A document scene can progress from source context to headline to highlighted phrase. It need not jump to unrelated imagery every few seconds.

#### K. Quality evaluation

Each change adds meaning; the viewer knows where to look; the edit has sufficient hold time for actual text. A motionless but useful reading hold passes when it serves the sentence.

#### L. Source and confidence

C/R, high confidence in the two positions; their reconciliation is explicit expert synthesis, not a combined instructor rule.

**Source files:** `67d5920a705ab69ca0840d5c0223e283.mp4` (T05, 26–40 s); `ceafa2d2481f7965d870e02fb67574bb.mp4` (T08, 22–26 s).

### EDT-04 — Coordinate story, edit, and graphics as one production plan

**Category:** Editorial · **Difficulty:** Beginner · **Software:** Construction software not shown

**Prerequisites:** Script and rough scene order

**Related:** EDT-02, EDT-03, EDT-05

#### A. What is this technique?

Plan the narrative, edit, and graphic choices together. The tutorial’s fifth recommendation states that the result depends on more than graphics alone.

#### B. Problem solved

A technically attractive effect can fail when it arrives at the wrong sentence or does not support the story’s logic.

#### C. Finished result

The intended finished result is a coherent explainer where visual content and edit progression support the narration. No single unique transition or effect is demonstrated by this advice.

#### D. Required components

Script, sequence structure, and graphic plan. These are planning components rather than a required software stack.

#### E. Original workflow, gaps, and proposed completion

**Original:** T05 closes its five-part overview by joining storytelling, editing, and graphics. It supplies examples but no production checklist.

**Proposed completion:** Before polishing, write each shot’s claim, supporting asset, main visual action, and reason for the next shot. Build a rough edit with placeholder motion. Check whether the claim is understandable before adding grain, chromatic fringes, or complex typography. Revise scene order when a missing explanation cannot be fixed by motion.

#### F. Motion mechanics and software-independent principle

Motion supports the shot’s role in a larger explanation. Universal principle: local visual quality and sequence-level clarity are different requirements; both must pass.

#### G. Settings and parameters

No exact parameters or prescribed project organization supplied. A planning table is an original workflow aid, not a creator template.

#### H. Instructor tips

T05, 48–58 s: the combined storytelling/editing/graphics contribution matters. Use before choosing an elaborate effect. Apply by requiring a narrative reason for each recipe used.

#### I. Mistakes and troubleshooting

No interface mistake shown. **Inferred:** adding finish to a structurally unclear sequence hides the problem temporarily. Diagnose missing context, wrong order, or unsupported inference before adjusting effects.

#### J. Original applications

Use in every original animation plan in Book VIII. For a short economic explainer, establish the comparison and evidence before deciding whether the numbers should roll like an odometer.

#### K. Quality evaluation

The sequence works as a rough cut, every effect has a job, and transitions preserve the explanation’s logic. Removing a finish effect should not remove the argument itself.

#### L. Source and confidence

C/R, high confidence in the editorial recommendation; the production procedure here is proposed synthesis.

**Source files:** `67d5920a705ab69ca0840d5c0223e283.mp4` (T05, 48–58 s).

### TRN-02 — Plan zoom, slide, and compositional match transitions

**Category:** Transitions · **Difficulty:** Beginner/intermediate · **Software:** Construction software not shown

**Prerequisites:** Two shots with a meaningful correspondence

**Related:** TRN-01, MOT-01, IMG-01

#### A. What is this technique?

Select a shared scale change, directional movement, or composition to connect two scenes. T05 presents zooms, slides, and match cuts as transition families.

#### B. Problem solved

Disconnected shot changes can interrupt flow; arbitrary complex transitions can imply relationships that the story does not contain.

#### C. Finished result

A focal detail can lead into the next scene, an outgoing movement can be continued, or a similarly placed subject can replace another. The montage supports the family of results, not a hidden exact rig.

#### D. Required components

Two source shots or compositions with a planned correspondence. Camera, masks, mattes, and parent rigs are not established for these montage examples.

#### E. Original workflow, gaps, and proposed completion

**Original:** T05 names and illustrates the families in a short montage. No construction steps are visible.

**Proposed completion:** For a zoom, choose the outgoing detail and incoming scale relationship before animating. For a slide, choose a consistent screen direction and an incoming composition that continues it. For a compositional match, align the important subject’s position, scale, and silhouette across the cut. Make a rough direct cut first; then add only the movement needed. If the objective specifically requires peak-speed continuity, use the separately demonstrated TRN-01 procedure instead of attributing that rig to T05.

#### F. Motion mechanics and software-independent principle

Scale, position, or static correspondence can carry continuity. Their timing is scene-dependent. Universal principle: let the viewer track a stable relationship across changing images.

#### G. Settings and parameters

No exact keyframes, durations, easing, masks, motion blur, or overlap values supplied. Any numerical plan is an original reconstruction.

#### H. Instructor tips

T05, 40–47 s: use seamless transitions such as zooms, slides, and match cuts. Apply when two ideas have a visual connection worth preserving. The source does not say every cut must use all three.

#### I. Mistakes and troubleshooting

No explicit troubleshooting shown. **Inferred:** a zoom can expose pixelation; a slide can reverse direction accidentally; a match cut can fail if the matched object shifts position. Fix the correspondence before adding more blur.

#### J. Original applications

Connect a building exterior to an architectural diagram through a shared window shape, or an article photograph to its separate crop. Avoid a match that suggests two unrelated people or places are identical.

#### K. Quality evaluation

The shared visual relationship is clear, destination readable, and transition does not become a separate spectacle. A simple cut is acceptable when no meaningful match exists.

#### L. Source and confidence

C/R, high confidence in named families; all implementation here is I and requires testing.

**Source files:** `67d5920a705ab69ca0840d5c0223e283.mp4` (T05, 40–47 s).

### IMG-01 — Reframe an article from context to reading detail

**Category:** Images · **Difficulty:** Beginner · **Software:** Construction software not shown

**Prerequisites:** High-resolution article image and a clear target passage

**Related:** TYP-01, MOT-01, FIN-07, EDT-03

#### A. What is this technique?

Animate the framing of an article so the viewer sees its context, then the part relevant to the narration. This is a source-image treatment, not character animation.

#### B. Problem solved

A complete page contains too much small text for a viewer to search while listening. A purposeful crop directs reading without demanding that the whole article be read.

#### C. Finished result

The article is shown as an identifiable source; the view moves closer to the headline or relevant passage. The clip later pairs this directed reading with highlighting.

#### D. Required components

Article image, a composition large enough for the needed framing, and a means of changing position/scale or camera framing. The clip does not expose the construction software or rig.

#### E. Original workflow, gaps, and proposed completion

**Original:** T07 shows zooming/reframing article examples and recommends that the source not remain static. It later demonstrates attention directed to a selected headline. No interface sequence is supplied.

**Proposed completion:** Import a legible article image. Set a context frame showing enough of the source to identify it. Choose a detail frame where the target phrase can be read at delivery size. Animate position and scale together so that phrase arrives at a deliberate reading position. Hold the detail for the actual narration. Verify the crop preserves the intended wording and does not remove a qualifier essential to its meaning.

#### F. Motion mechanics and software-independent principle

The whole source image changes framing; individual printed characters do not need separate layers. Coupled position and scale prevent the target from drifting during enlargement. Universal principle: reveal information by changing the viewer’s access to detail.

#### G. Settings and parameters

No exact duration, scale endpoint, anchor point, camera setting, or easing curve provided. The visible “zoom in/out” advice is qualitative. Use MOT-01 only as a separately sourced timing option.

#### H. Instructor tips

T07, 3–7 s: use article movement. T07, 16–24 s: viewers should not need to read everything to locate what narration discusses. Apply by planning the reading target before keyframing.

#### I. Mistakes and troubleshooting

No correction demonstrated. **Inferred:** enlargement cannot recover absent resolution; obtain a better source or recreate a clearly labeled quotation. A crop that removes context can distort the source’s meaning. Do not move text continuously through its entire reading interval.

#### J. Original applications

Reveal a report’s title, then its conclusion; show a historical headline, then a relevant sentence. Combine with TYP-01 for a controlled emphasis pass and EDT-01 for a restrained paper sound.

#### K. Quality evaluation

The source can be identified, the intended passage is readable, the move lands cleanly, and the audience is not asked to search unrelated text.

#### L. Source and confidence

C/R, high confidence in target appearance and recommendation; all keyframe construction is proposed completion.

**Source files:** `aeed047136abe7bd6dda38dda80f6023.mp4` (T07, 3–7 s; 16–24 s).

### FIN-07 — Integrate paper and surface textures

**Category:** Finishing · **Difficulty:** Beginner/intermediate · **Software:** Result examples in T07; After Effects visible in T10

**Prerequisites:** Readable base artwork and suitable texture assets

**Related:** IMG-01, FIN-03, TYP-01

#### A. What is this technique?

Introduce visible paper or print-like surface variation into article cards, type, or graphic fills. T07 emphasizes a real-world paper feel; T10 shows textured rather than perfectly solid surfaces.

#### B. Problem solved

A clean digital rectangle or uniformly filled shape can feel disconnected from a tactile editorial composition.

#### C. Finished result

T07’s article appears more like a paper object, with irregular surface/edge character. T10 shows texture within enlarged text and a colored numbered circle. These are appearance demonstrations, not a complete common compositing recipe.

#### D. Required components

Base artwork and a texture treatment. T07’s apparent paper edges and depth may require additional artwork, but exact layers, masks, shadows, and blend modes are not supplied. T10’s particular texture source is not established.

#### E. Original workflow, gaps, and proposed completion

**Original:** T07 contrasts static digital-looking source presentation with paper-like presentation. T10 shows close views of textured lettering and a circle while recommending texture. Neither shows every construction step.

**Proposed completion:** First choose whether texture belongs to a page surface, a printed fill, or the whole frame. Prepare that surface separately. Composite a texture at low strength, limiting it to the relevant asset if necessary. For paper edges, use an actual cutout or a deliberately constructed irregular silhouette; for printed letters, keep texture inside the letter shape. Inspect contrast after each treatment. These are proposed approaches, not demonstrated track-matte or masking instructions.

#### F. Motion mechanics and software-independent principle

The surface need not animate. If the article moves, its texture should usually move with it so the material appears attached; this is an inferred compositing requirement. Universal principle: material variation should follow the object whose surface it represents.

#### G. Settings and parameters

No exact blend mode, opacity, roughness, shadow, texture scale, or mask settings established for these examples. “No solid colors” is the creator’s styling generalization in T10, not a mandatory rule.

#### H. Instructor tips

T07, 8–15 s: use texture to make article presentation feel more physical. T10, 17–20 s: surface texture is a recurring characteristic in the examples. Use when material character helps integrate the assets.

#### I. Mistakes and troubleshooting

No error shown. **Inferred:** texture can erase thin letters or look like dirt floating independently of the page. Reduce strength, change scale, or attach it to the correct layer group. Surface credibility does not authenticate the underlying document.

#### J. Original applications

Treat a public-domain letter, a report excerpt, or a diagram card. Combine with FIN-03 only after checking that broad paper variation and fine grain do not create excessive noise.

#### K. Quality evaluation

Text remains readable, texture scale fits the object, and all material details move coherently. Edge treatment must not clip the source text.

#### L. Source and confidence

C/R, high confidence in appearance and advice; specific compositing methods and values are I. Do not attribute a complete paper preset to either clip.

**Source files:** `aeed047136abe7bd6dda38dda80f6023.mp4` (T07, 8–15 s); `f1c5ee3e7479d70b0060bc80af8a330c.mp4` (T10, 17–20 s).

### TYP-01 — Highlight the passage that narration discusses

**Category:** Typography/annotation · **Difficulty:** Beginner · **Software:** Construction software not shown

**Prerequisites:** Source image and correctly selected words

**Related:** IMG-01, SHP-01, EDT-05

#### A. What is this technique?

A colored highlight identifies the relevant words in an article. It is an editorial emphasis layer, distinct from changing the fill of editable text characters.

#### B. Problem solved

The viewer cannot comfortably read an entire page and listen simultaneously. Emphasis removes the search task.

#### C. Finished result

A source article remains visible, but a specific headline or phrase receives yellow emphasis. The attention target is narrower than the full document.

#### D. Required components

Article image, selected passage, and a highlight graphic or equivalent treatment. The full highlighter tutorial is advertised later in T07 but is not part of the supplied clip.

#### E. Original workflow, gaps, and proposed completion

**Original:** T07 shows selected headline emphasis and explains why important information should be highlighted. It does not show the highlighter effect’s actual construction.

**Proposed completion:** Verify the exact words to emphasize. Create a simple highlight area aligned to their baseline and width. Choose a compositing arrangement that retains readable letter contrast. Reveal it at the relevant narration beat, then hold it. If a wipe or mask is chosen, document it as an original implementation; this source does not establish the specific mask, matte, brush, or blend mode.

#### F. Motion mechanics and software-independent principle

The semantic selection is the primary operation. The reveal might move across words, but no exact wipe direction or driver is recovered. Universal principle: reduce competition by marking the relevant subset of existing information.

#### G. Settings and parameters

Yellow appearance is visible; numeric color, opacity, duration, geometry, blend mode, and keyframe values are not specified. A rectangular wipe is a proposed simplification, not the supplied creator’s verified recipe.

#### H. Instructor tips

T07, 16–24 s: guide viewers to what the narrator is discussing instead of asking them to find it. Apply by matching the highlight’s words precisely to the claim.

#### I. Mistakes and troubleshooting

No construction error shown. **Inferred:** highlighting too much defeats selection; opaque color may cover the words; an animation that outruns narration can reveal a conclusion prematurely. Fix selection and readability before polishing the reveal.

#### J. Original applications

Mark the decisive phrase in a report, a date in a clipping, or a definition in a source. For a hand-marked circle rather than a filled highlight, use SHP-01 plus FIN-04/05.

#### K. Quality evaluation

The right words remain legible and context remains available. The emphasized span is no larger than the explanatory task requires.

#### L. Source and confidence

C/R, high confidence in editorial purpose and result; low confidence in original implementation because it is not supplied. All construction guidance is I.

**Source files:** `aeed047136abe7bd6dda38dda80f6023.mp4` (T07, 16–24 s).

### TYP-02 — Sweep a text animator’s Fill Color through characters

**Category:** Typography · **Difficulty:** Intermediate · **Software:** After Effects

**Prerequisites:** Editable text and selector basics

**Related:** WRK-01, EDT-05, TYP-03

#### A. What is this technique?

A text animator changes character fill according to a selector. This allows some letters to be treated while others remain in their base color.

#### B. Problem solved

Changing an entire text layer’s fill at once cannot create the demonstrated traveling character-level color emphasis.

#### C. Finished result

The examples show letters changing between yellow and dark fill across the phrase. A later “FILL ANIMATION” demonstration shows the color treatment progressing through the word group.

#### D. Required components

Editable text, an Animator containing Fill Color, and a Range Selector. The UI shows Start, End, Offset, Advanced, and a yellow Fill Color swatch. The complete animation keyframes are not exposed.

#### E. Original workflow, gaps, and proposed completion

**Original:** Open a text layer’s **Animate** menu. The expanded existing animator visibly contains **Fill Color**; a color picker is shown. The cursor passes over Stroke Color in the menu, but that hover is not evidence that Stroke Color drives the demonstrated result. The clip shows fill-animation outputs.

**Proposed completion:** Add a Fill Color animator to an editable text layer and choose the intended highlight color. With one selector, first confirm which characters are selected. Animate End or Offset so the affected range travels across the desired text. For a simple fill-up, a proposed starting design is Start 0%, End 0→100%; for a traveling band, keep a limited range and move Offset. Test selector direction and final color state before saving a preset. These endpoint choices are not all shown by the creator.

#### F. Motion mechanics and software-independent principle

The text’s layout can remain stationary while its character treatment changes. Selector coverage determines where the animator applies; Fill Color determines the selected characters’ appearance. Universal principle: separate a per-element treatment from the rule that selects elements over time.

#### G. Settings and parameters

**Exact visible state:** one expanded Range Selector shows End 0% and Offset 0%; Fill Color is yellow. **Not specified:** complete keyframe endpoints, selector shape, smoothness, units, easing, exact color, or timing. A separate odometer layer’s Offset −100% is not a Fill Color setting.

#### H. Instructor tips

T08, 5–9 s: use text animators and save reusable behavior. Use when characters need selective emphasis without splitting every letter into a separate layer.

#### I. Mistakes and troubleshooting

No construction error shown. **Inferred:** animating the base Character fill changes all text; selecting the wrong range can leave the phrase half-treated. A selected range with no visible color contrast may make the animator seem broken.

#### J. Original applications

Reveal an important keyword within a short statement. Keep surrounding text stable; use EDT-05 to avoid multiple simultaneous color sweeps.

#### K. Quality evaluation

Character order and selected range match the intention; the complete final phrase is readable; color changes do not compete with a separate moving headline.

#### L. Source and confidence

D/C/R, high confidence in the Fill Color animator and menu; exact selector choreography is partly missing. Proposed implementation requires preview testing.

**Source files:** `ceafa2d2481f7965d870e02fb67574bb.mp4` (T08, 5–8 s; 10–15 s).

### TYP-03 — Random-order character appearance as a result target

**Category:** Typography · **Difficulty:** Intermediate · **Software:** After Effects context; construction not shown

**Prerequisites:** Editable text and a readable final phrase

**Related:** TYP-02, EDT-05, WRK-01

#### A. What is this technique?

Letters appear in a scattered order until a complete phrase is visible. The clip labels this “Random Appearing Letters.”

#### B. Problem solved

A uniform whole-line reveal can be less distinctive than a short per-character build, when the phrase can wait to be read until complete.

#### C. Finished result

Partial letters appear across the phrase, followed by the completed text. It is a showcase lasting only a short interval, not a full selector lesson.

#### D. Required components

Text plus a per-character visibility or appearance control. The exact animator, selector ordering, and random seed are not shown.

#### E. Original workflow, gaps, and proposed completion

**Original:** T08 displays the named result; no settings or interface steps for this variation are demonstrated.

**Proposed completion:** Use an opacity-based text animator with a randomized selection/order mechanism available in the target application, or explicitly schedule character visibility. Verify the property names and behavior in that application before committing. Keep the random order deterministic for repeatable renders. End with every character visible and hold the complete phrase. This is a proposed reconstruction, not a claim that the creator used a particular Randomize Order checkbox.

#### F. Motion mechanics and software-independent principle

Character onset times differ rather than the entire line fading together. The phrase’s overall location stays stable. Universal principle: stagger element visibility while guaranteeing a complete, stable endpoint.

#### G. Settings and parameters

No exact onset spacing, opacity values, selector settings, seed, duration, or easing supplied. Do not derive settings from the title alone.

#### H. Instructor tips

The showcase offers this as one text-animation possibility, T08 16–17 s. The explicit cross-cutting tip is T08’s later warning to avoid overwhelming the viewer. Use for short text whose meaning does not depend on reading the incomplete state.

#### I. Mistakes and troubleshooting

No error shown. **Inferred:** a long sentence can remain unreadable too long; random intermediate fragments can form misleading words. Shorten the phrase or choose an ordered reveal for critical information.

#### J. Original applications

Introduce a short section label or puzzle-related title. Avoid randomizing a precise instruction or number at the moment it must be understood.

#### K. Quality evaluation

The final phrase is complete and readable, no characters remain hidden, and the build does not delay comprehension past the relevant narration.

#### L. Source and confidence

R, high confidence in the named appearance; original implementation unknown. Proposed method is I and requires verification.

**Source files:** `ceafa2d2481f7965d870e02fb67574bb.mp4` (T08, 16–17 s).

### TYP-04 — Odometer-style text and numeric-display showcase

**Category:** Typography · **Difficulty:** Intermediate/advanced · **Software:** After Effects context; full construction not shown

**Prerequisites:** Editable text or prepared character elements

**Related:** TYP-02, WRK-01, EDT-05

#### A. What is this technique?

The clip showcases an animation labeled “ODOMETER” and says numbers can also be treated. It suggests a mechanical character-change appearance, not a demonstrated arithmetic counter.

#### B. Problem solved

A static number or title can be introduced with a distinctive mechanical character, provided the final value remains unambiguous.

#### C. Finished result

The word ODOMETER and a numeric display such as `$600,000,000` appear in the sequence. Sampled frames establish the showcase and endpoint; they do not recover every intermediate glyph or prove a specific rolling construction.

#### D. Required components

Text layers or character elements. The timeline briefly shows an ODOMETER text layer with Range Selector Offset at −100%. This is not enough to establish which animator properties, masks, or expressions make the full result.

#### E. Original workflow, gaps, and proposed completion

**Original:** Show the odometer-labeled example, then the “numbers too” example. No complete build is demonstrated.

**Proposed completion:** If a rolling-counter appearance is required, construct a separately validated character-column or text-animator rig. Define the exact final string first, including currency sign and separators. Make each position resolve to that string, then hold. If the number represents a measured change over time, separately validate its data and interpolation; a decorative reveal must not imply that intermediate numbers are factual measurements. A simple ordered reveal is an acceptable substitute when a rolling rig cannot be verified.

#### F. Motion mechanics and software-independent principle

The perceived operation is character-level change before a stable endpoint. Neither continuous counting nor exact vertical travel is established from the available control evidence. Universal principle: decorative state transitions must resolve reliably to the intended semantic value.

#### G. Settings and parameters

**Exact visible incidental state:** ODOMETER Range Selector Offset −100%. **Exact shown example string:** `$600,000,000`. **Not specified:** actual numeric expression, digit-column geometry, masking, character offsets, loop logic, or final timing.

#### H. Instructor tips

T08, 18–21 s: presents this style as usable for letters and numbers. Use only when the mechanical reveal supports the subject and does not interfere with immediate reading.

#### I. Mistakes and troubleshooting

No error shown. **Inferred:** do not treat an intermediate decorative glyph as data. Commas and currency symbols can jump if the layout is not controlled. A preset that works on one word length may fail on another.

#### J. Original applications

Reveal a final archival budget figure or a short machine-themed label. For proportional population growth, use a separately validated data representation rather than assuming this showcase supplies one.

#### K. Quality evaluation

Final string exact, punctuation stable, no unfinished character movement, and no false implication about intermediate values. Test replacement text lengths before reuse.

#### L. Source and confidence

R plus limited D, high confidence in names and visible endpoint, low confidence in hidden construction. No tutorial-derived numeric-counter algorithm exists here.

**Source files:** `ceafa2d2481f7965d870e02fb67574bb.mp4` (T08, 5.5 s; 18–21 s).

### WRK-01 — Save selected animation behavior as a preset

**Category:** Workflow · **Difficulty:** Intermediate · **Software:** After Effects

**Prerequisites:** A working animator and deliberate property selection

**Related:** TYP-02, TYP-03, TYP-04

#### A. What is this technique?

Save a working animation’s selected properties as an animation preset that can be applied to another layer.

#### B. Problem solved

Repeatedly rebuilding the same text behavior wastes effort and introduces inconsistent timings or settings.

#### C. Finished result

A reusable behavior can be applied to different text. The clip shows the save command and examples; it does not show a complete clean-layer reapplication test.

#### D. Required components

A working animation, selected properties, and the Animation menu. Exact saved file name, location, property selection, and preset contents are not exposed.

#### E. Original workflow, gaps, and proposed completion

**Original:** After showing text animators, open **Animation > Save Animation Preset…**. The menu also contains Apply Animation Preset, but a full application sequence is not shown.

**Proposed completion:** Select only the animator/effects and keyframes intended for reuse; avoid accidentally including source-specific position or other irrelevant properties. Save a clearly named preset. Create a fresh text layer with different content and use Apply Animation Preset to test it at the intended timeline point. Check timing, color, final visibility, and whether source-specific values were copied. Adjust selection and resave if the new layer moves to an unintended location.

#### F. Motion mechanics and software-independent principle

The preset preserves behavior; it does not decide whether that behavior suits the new text. Universal principle: package a tested operation with a clear scope and endpoint contract.

#### G. Settings and parameters

**Exact command:** Animation > Save Animation Preset. **Not specified:** selected property scope, storage path, duration, naming scheme, application time, or compatibility version.

#### H. Instructor tips

T08, 8–11 s: save a useful animation. Apply when repeating a known treatment across similar elements. The value is consistency and speed, not an exemption from testing new content.

#### I. Mistakes and troubleshooting

No error shown. **Inferred:** saving broad transforms can relocate new text; saving source text can replace intended content; long replacement text may exceed the animation’s readable time. Test the preset on a new layer before production use.

#### J. Original applications

Build a small, validated kit for section labels and short emphasis phrases. Keep distinct presets for fill sweeps and random reveals rather than one overloaded all-purpose animation.

#### K. Quality evaluation

The preset behaves predictably on fresh content, leaves unrelated layout intact, resolves fully, and has an explicit dependency list.

#### L. Source and confidence

D/C, high confidence in save command; selection, save dialog, and reuse verification are proposed completion.

**Source files:** `ceafa2d2481f7965d870e02fb67574bb.mp4` (T08, 8–11 s).

### EDT-05 — Give animated typography one clear reading priority

**Category:** Editorial/typography · **Difficulty:** Beginner · **Software:** After Effects examples; judgment is software-independent

**Prerequisites:** A scene with multiple text elements

**Related:** TYP-01, TYP-02, EDT-03

#### A. What is this technique?

Choose which text the viewer should read now, and subordinate or delay competing animated text.

#### B. Problem solved

Several animated words can each be attractive while making the scene collectively unreadable.

#### C. Finished result

T08 deliberately shows an overloaded frame with competing phrases such as “WHERE DO I LOOK” and “STATISTIC.” The successful target is the opposite reading behavior: one obvious primary message, with supporting information available afterward.

#### D. Required components

Text elements with distinct narrative roles and a timeline that can separate their entries. No special effect is required.

#### E. Original workflow, gaps, and proposed completion

**Original:** T08 demonstrates clutter and warns that the viewer will not know what to read. T07’s article guidance separately prioritizes the relevant passage.

**Proposed completion:** Identify the one phrase needed for the current narration beat. Keep it the strongest by timing, position, or contrast. Delay a secondary reveal until the primary phrase has been understood. Reduce or remove animation from already-read labels. Review the scene silently and ask what a viewer would read first; if the answer is ambiguous, change event timing before adding new styles.

#### F. Motion mechanics and software-independent principle

Staggering is a proposed solution to observed competition, not a measured stagger setting from the tutorial. Motion onset is a strong attention event; several simultaneous onsets can divide that attention. Universal principle: coordinate events around a reading sequence.

#### G. Settings and parameters

No exact delay, word count, font size, duration, or maximum number of elements supplied. The source does not establish a universal one-text-layer limit.

#### H. Instructor tips

T08, 22–26 s: avoid overwhelming text animation. Use when combining multiple presets or statistics. Apply by asking what should be read at each beat, then suppressing competing events.

#### I. Mistakes and troubleshooting

**Explicit problem:** competing text prevents clear reading order. **Proposed fixes:** stagger entries, hold the primary phrase, simplify supporting motion, or remove redundant words. Making everything larger usually worsens the conflict.

#### J. Original applications

Use in a two-number comparison, article-plus-callout scene, or map with labels. Constant scene progression from EDT-03 can coexist with a stable reading target.

#### K. Quality evaluation

The first reading target is obvious, supporting elements arrive logically, and the viewer can complete the reading before the next major change.

#### L. Source and confidence

C/R, high confidence in warning and example; timing remedies are I supported by the observed problem.

**Source files:** `ceafa2d2481f7965d870e02fb67574bb.mp4` (T08, 22–26 s); `aeed047136abe7bd6dda38dda80f6023.mp4` (T07, 16–24 s).

### IMG-02 — Separate a photograph into depth planes

**Category:** Images · **Difficulty:** Intermediate · **Software:** Photoshop

**Prerequisites:** Image selection, layer editing, and subject isolation

**Related:** IMG-03, IMG-04, WRK-02

#### A. What is this technique?

Separate the foreground, midground, and background of one photograph into independent image layers.

#### B. Problem solved

A flattened image can move or enlarge, but its internal depth relationships cannot respond independently to a camera move.

#### C. Finished result

The rocky foreground, cable-car midground, and mountain background become separate layers that can reconstruct the original composition and later move with different projected relationships.

#### D. Required components

A photograph with clear depth, a layered image document, and isolated foreground/midground/background elements. The exact selection tools and mask refinement are not shown. Fine cable lines complicate the source example but their full treatment is not demonstrated.

#### E. Original workflow, gaps, and proposed completion

**Original:** Choose an image with plenty of depth and a clear foreground, midground, and background. In Photoshop, separate those elements into their own layers. The Layers panel visibly names **Foreground**, **Midground**, and **background**; layer visibility is toggled to show separation.

**Proposed completion:** Preserve the original photo. Identify the silhouette of each plane and isolate it using a suitable selection/mask method. Keep the layers registered to the original canvas so they reconstruct correctly. Toggle each layer individually to find unwanted fragments, missing edges, or transparency where the object should be opaque. Recombine all planes before proceeding to repair and camera work. The choice of selection tool and exact mask settings are additional implementation decisions.

#### F. Motion mechanics and software-independent principle

No motion is needed at this stage. The operation creates independently addressable visual planes. Universal principle: make the asset’s structure match the depth relationships the animation must reveal.

#### G. Settings and parameters

**Exact source organization:** three named depth roles. **Not specified:** mask feather, selection method, edge-decontamination settings, image dimensions, or export/import options. Three planes are the example, not a maximum.

#### H. Instructor tips

T09, 13–18 s: begin with a depth-rich photo. This matters because a photograph with no useful occlusion or depth separation may produce weak parallax despite extensive masking. Select the image before building the rig.

#### I. Mistakes and troubleshooting

No mask error shown. **Inferred:** losing thin wires or leaving bright halos can expose the cutout. Too many planes increase labor without necessarily adding visible depth. A close crop may leave no room for the planned move.

#### J. Original applications

Animate a historic street, industrial interior, or landscape with distinct planes. Use fewer planes for a subtle move; add planes only when the visible depth relationships justify them.

#### K. Quality evaluation

Recombined layers match the original framing, isolated silhouettes are clean, and the chosen separation supports the intended camera direction.

#### L. Source and confidence

D/C, high confidence in three-plane method and names; selection tools and detailed mask workflow are proposed completion.

**Source files:** `d29898c682425d563099b86e1c108116.mp4` (T09, 13–20.5 s).

### IMG-03 — Repair regions hidden behind extracted subjects

**Category:** Images · **Difficulty:** Intermediate · **Software:** Photoshop

**Prerequisites:** IMG-02 and basic retouching

**Related:** IMG-02, IMG-04

#### A. What is this technique?

Use Clone Stamp to patch image regions that were hidden behind a subject now placed on its own layer.

#### B. Problem solved

When parallax shifts the subject relative to the background, the original subject-shaped region can become visible. Without repair it may show a hole, a duplicate subject, or an obvious patch.

#### C. Finished result

The background continues plausibly behind the extracted cable car and foreground. A camera move can reveal those areas without immediately exposing the separation.

#### D. Required components

Separated source layers, a background or relevant hidden plane to repair, and the Clone Stamp tool. The exact brush parameters and sampling choices are not supplied.

#### E. Original workflow, gaps, and proposed completion

**Original:** After layer separation, T09 names **Clone Stamp** and instructs patching areas behind the extracted elements. A close view of the missing region and surrounding landscape accompanies this instruction.

**Proposed completion:** Hide the foreground subject temporarily. Work on a duplicate or non-destructive retouch layer with appropriate sampling. Sample nearby compatible texture and rebuild the region that the planned camera move could expose. Continue mountain edges, gradients, and texture direction rather than repeating a conspicuous landmark. Restore the subject and test an exaggerated preview of the intended move. Repair only after identifying how much hidden area is actually needed; brush size, opacity, and sampling controls must be chosen for the image.

#### F. Motion mechanics and software-independent principle

The retouch is static, but its required coverage is determined by future motion. Universal principle: prepare pixels for newly visible areas before animating occlusion changes.

#### G. Settings and parameters

**Exact tool:** Clone Stamp. **Not specified:** brush size, hardness, opacity, sample point, retouch margin, or final repaired layer structure. A white-looking region in the recording is not proof of the final alpha format.

#### H. Instructor tips

T09, 21–24.5 s: patch behind separated elements. Use whenever a camera move reveals previously occluded image areas. The repair is part of the parallax workflow, not optional polish after rendering.

#### I. Mistakes and troubleshooting

No finished failure is shown. **Inferred:** repeating mountain features, mismatched lighting, and unrepaired original subject fragments become visible when the foreground moves. Test at the maximum move, not just the centered starting frame.

#### J. Original applications

Repair behind a building, person, or archival object before a small lateral camera move. Avoid inventing historically meaningful detail in a factual image; keep the camera move modest when faithful repair is uncertain.

#### K. Quality evaluation

No hole, duplicated subject, obvious clone repetition, or edge mismatch appears anywhere the final camera exposes. The untouched visible evidence remains recognizable.

#### L. Source and confidence

D/C, high confidence in tool and purpose; full brush procedure and quality of the final hidden reconstruction are not verified.

**Source files:** `d29898c682425d563099b86e1c108116.mp4` (T09, 21–24.5 s).

### IMG-04 — Create parallax with 3D image planes and a camera move

**Category:** Images/motion · **Difficulty:** Intermediate/advanced · **Software:** After Effects, following Photoshop preparation

**Prerequisites:** IMG-02, IMG-03, 3D layers and camera basics

**Related:** IMG-02, IMG-03, WRK-02, MOT-01

#### A. What is this technique?

Place separated image planes at different depths and move a camera or camera rig so their projected relationships change. The clip calls the result parallax.

#### B. Problem solved

A simple flat image zoom preserves all internal relationships and can look flat. Depth-separated layers allow nearer and farther elements to behave differently.

#### C. Finished result

The rocky foreground, cable car, and distant mountains retain the original scene but shift relative to one another as the viewpoint changes. A side view shows the flat planes distributed in 3D.

#### D. Required components

Layered photo, repaired hidden regions, three-dimensional image planes, a camera or camera rig, and movement keyframes. The optional Depth script in WRK-02 can assist setup; the creator also says manual placement is possible.

#### E. Original workflow, gaps, and proposed completion

**Original:** Bring the separated layers into After Effects; space them out in 3D; optionally use Depth to do the spacing; then slowly move the camera. The captions use “dolly.” The clip does not show a complete import dialog, camera-creation dialog, layer-size compensation procedure, or start/end keyframe sequence.

**Proposed manual completion:** Import the layered document in a way that preserves separate layers and their registration. Make the image planes 3D. Create a camera, then place foreground nearer and background farther in a side/custom view. Re-establish the original framing by adjusting each plane’s scale/position while checking the camera view. Add a small camera or rig move that reveals relative shifts. Render a short preview and check every newly exposed region. Reduce the move or extend repairs if edges or missing areas appear.

Do not merely move planes in Z and accept a changed starting composition. Depth placement changes apparent size under perspective; framing compensation is part of the proposed manual method, not a demonstrated numeric formula from the clip.

#### F. Motion mechanics and software-independent principle

Relative depth makes nearby planes respond more strongly to viewpoint translation than distant ones. The caption’s “dolly” is broad language here: sampled UI states show a transform Position with changing X while Z is displayed at −1500, and the complete camera/rig assignment is not readable. Therefore the source does not establish a pure Z-axis dolly recipe. Universal principle: create relative projected motion through depth and viewpoint change.

#### G. Settings and parameters

**Exact incidental sampled transform state:** Position 745.0,960.0,−1500.0 around 32 s; other samples show changed X. The owner and full endpoint pair are not established, so these are not reusable camera coordinates. **Not specified:** final plane depths, camera duration, movement distance, ease values, depth of field, or focal settings for a manual rig.

#### H. Instructor tips

T09, 25–31 s: distribute the layers in 3D, with an optional script or manually. T09, 32–36 s: use a slow camera move. Apply modest motion first so the image still reads as one coherent scene.

#### I. Mistakes and troubleshooting

The clip contrasts flat movement with the richer result. **Inferred failures:** edge gaps, unscaled far planes, doubled subjects, and oversized moves that expose unrepaired areas. Fix the asset coverage and framing before adding blur to conceal defects.

#### J. Original applications

Create a restrained move through an archival street or scientific photograph. Use IMG-01 instead when the main task is reading a document rather than showing scene depth.

#### K. Quality evaluation

Original image remains coherent, depth order is plausible, movement produces relative shifts, and no plane edge or retouch flaw is revealed. Do not equate stronger parallax with better factual presentation.

#### L. Source and confidence

D/C/R, high confidence in overall workflow and result; manual setup, exact camera axis, and keyframes are incomplete. Proposed manual reconstruction requires application validation.

**Source files:** `d29898c682425d563099b86e1c108116.mp4` (T09, 24.5–36 s).

### WRK-02 — Use the optional Depth script for parallax setup

**Category:** Workflow · **Difficulty:** Intermediate · **Software:** After Effects with optional Depth utility

**Prerequisites:** Separated layers and an understood parallax goal

**Related:** IMG-04, IMG-02

#### A. What is this technique?

The creator uses a utility labeled Depth to help distribute layers for a parallax setup and states that the work can also be done manually.

#### B. Problem solved

Manually arranging many image planes and a camera rig can be repetitive. A utility can speed that setup if its behavior fits the scene.

#### C. Finished result

The utility’s panel offers focal length, layer-distance/spacing controls, a camera-null option, and Disperse/Move buttons. It supports the already shown layered-depth result.

#### D. Required components

After Effects, separated layers, and the optional script. The full product identifier, installation procedure, current compatibility, and code are not supplied for verification.

#### E. Original workflow, gaps, and proposed completion

**Original:** Show the Depth product page, then the utility panel; the cursor points to **Disperse**. The creator says it can perform the setup in one click and adds that manual setup is possible. The complete selection state and all resulting layer transforms are not visible.

**Proposed completion:** Before running a utility, duplicate the working composition, confirm selected layers and intended depth order, and verify the utility’s current instructions. Afterward inspect the camera view and side view. Check apparent sizes, plane order, camera-null relationship, and whether the original framing is preserved. Do not assume the displayed example settings are appropriate to a different composition.

#### F. Motion mechanics and software-independent principle

The utility automates rig construction; it does not replace image preparation or final motion design. Universal principle: automate repeatable setup only when the resulting structure is inspectable.

#### G. Settings and parameters

**Exact panel state:** version label v1.0.2; Focal Length 50mm; Layer Distance 0; Layer Spacing 1000; Create Camera Null checked; buttons Disperse and Move. **Not specified:** complete algorithm, resulting Z positions, selection ordering, current license, current price, or compatibility.

#### H. Instructor tips

T09, 28–31 s: use Depth as a shortcut, or do the setup manually. Use when it saves time and the operator can validate the generated rig. It is not a mandatory dependency for parallax.

#### I. Mistakes and troubleshooting

No utility failure shown. **Inferred:** running it on the wrong layer selection can produce an unwanted structure. If the utility is unavailable, follow IMG-04’s proposed manual route instead of installing an unrelated similarly named tool.

#### J. Original applications

Use for a repeated archive-photo workflow after one manual rig has established the intended structure. Keep the shortcut optional in a transferable production plan.

#### K. Quality evaluation

Generated structure is understood, the camera framing is correct, and no unexplained plugin dependency prevents the project from being reopened or revised.

#### L. Source and confidence

D/C, high confidence in visible panel states and optional status; behavior and current availability not verified.

**Source files:** `d29898c682425d563099b86e1c108116.mp4` (T09, 28–31 s).

### FIN-08 — Add restrained chromatic edge separation

**Category:** Finishing · **Difficulty:** Beginner/intermediate · **Software:** After Effects; Quick Chromatic Aberration 3

**Prerequisites:** A finishing layer and the named plugin

**Related:** FIN-01, FIN-03, FIN-09

#### A. What is this technique?

Slightly separate color channels at high-contrast edges, producing a small colored fringe. T10 explicitly names Quick Chromatic Aberration 3 as its method.

#### B. Problem solved

Perfectly registered digital edges can feel too pristine for the example’s optical finish.

#### C. Finished result

Enlarged black type on a light background shows colored edge offsets in the comparison. At normal viewing size the intended effect is subtle, not a conspicuous glitch.

#### D. Required components

Image content, a layer covering the intended composition, and **Quick Chromatic Aberration 3** for the demonstrated plugin-based method. The plugin also appears in T01’s existing effect stack.

#### E. Original workflow, gaps, and proposed completion

**Original:** T10 shows the edge treatment and says a layer of chromatic aberration is applied over everything. It names the plugin and describes it as free. The full installation and parameter-edit sequence is omitted.

**Proposed completion:** Confirm the exact plugin and compatibility before using it. Apply it at the intended finishing scope; compare on/off on both large imagery and small type. Increase only enough to see the treatment, then judge at actual delivery size. A manually separated-channel implementation would be an adaptation requiring verification, not the supplied workflow.

#### F. Motion mechanics and software-independent principle

No specific animated aberration parameter is demonstrated. This is principally a spatial edge treatment. Universal principle: a small channel-registration imperfection can alter perceived optical character without changing content.

#### G. Settings and parameters

**Exact name:** Quick Chromatic Aberration 3. **Not specified:** channel offsets, strength, falloff, edge handling, animation, or final amount. “Free” is the clip’s historical claim, not verified current pricing.

#### H. Instructor tips

T10, 3–8 s: keep the effect subtle enough to go largely unnoticed and apply as an overall treatment. Use when it unifies the look without degrading fine information.

#### I. Mistakes and troubleshooting

No error shown. **Inferred:** large fringes reduce text clarity and may look like an intentional glitch rather than optical imperfection. A plugin name visible in T01 does not prove every parameter or activation state.

#### J. Original applications

Finish a broad editorial composition. Reduce or omit on dense maps, small labels, or diagrams where exact edges carry information.

#### K. Quality evaluation

The unzoomed image remains crisp enough to read; fringes do not dominate; frame edges do not reveal unintended channel displacement artifacts.

#### L. Source and confidence

D/C/R, high confidence in plugin name and intended restraint; exact settings and current dependency status unresolved.

**Source files:** `f1c5ee3e7479d70b0060bc80af8a330c.mp4` (T10, 3–8 s); `017833d6758add159d297d753e03e084.mp4` (T01, 16–22 s).

### FIN-09 — Apply a 12 fps picture-sampling treatment

**Category:** Finishing · **Difficulty:** Beginner/intermediate · **Software:** After Effects

**Prerequisites:** An animated composition and effect scope

**Related:** MOT-01, FIN-01, FIN-05

#### A. What is this technique?

Posterize Time reduces the temporal sampling of the image it affects. The source shows a Frame Rate value of 12.0.

#### B. Problem solved

Fully smooth digital animation may not fit the graphic, tactile cadence chosen for these examples.

#### C. Finished result

Movement can retain its designed ease while changing in more discrete visible steps. The source presents this as a recurring stylistic treatment, not a requirement for every explainer.

#### D. Required components

An animated layer or composition and the **Posterize Time** effect. A global finishing layer is shown; the precise scope of every upstream/downstream effect is not exhaustively demonstrated.

#### E. Original workflow, gaps, and proposed completion

**Original:** T10 recommends reducing the cadence to around twelve and shows Posterize Time with **Frame Rate 12.0**. T01’s finishing stack also displays 12.0.

**Proposed completion:** Apply the effect to the intended image scope and set 12. Preview a movement both with and without the effect. Check whether fine annotations, text sweeps, and cuts still read. Keep delivery frame rate as a separate decision; the tutorial does not instruct exporting a 12 fps file. Inspect the final stack, since other operations after the temporal effect may still introduce changes.

#### F. Motion mechanics and software-independent principle

Temporal stepping changes when the picture updates; easing changes where it is at those samples. Smooth curves and stepped output can coexist. Universal principle: control motion trajectory and temporal sampling independently.

#### G. Settings and parameters

**Exact visible:** Posterize Time > Frame Rate 12.0. **Distinct exact value elsewhere:** T01’s Position expression uses `posterizeTime(24)`. **Not specified:** mandatory composition fps, export fps, shutter angle, or a measured effective rate for all downstream effects.

#### H. Instructor tips

T10, 9–12 s: use Posterize Time for the lower-cadence treatment. Apply when deliberate stepping suits the visual material. Treat broad claims about all examples as stylistic commentary, not verified universal Vox practice.

#### I. Mistakes and troubleshooting

No error shown. **Inferred:** rapid small movement may jump too far between visible samples; revise its distance/duration or omit the treatment locally. A 12 fps effect is not a substitute for aligning a cut to the actual displayed motion.

#### J. Original applications

Use on hand-drawn annotation or a paper collage. Preserve smoother motion for a different shot if stepping harms its explanatory function; consistency is a considered choice, not blind identical settings.

#### K. Quality evaluation

Stepping feels intentional, important states remain visible, text stays readable, and cuts do not produce a misleading hold or skip.

#### L. Source and confidence

D/C, high confidence in effect and value. Source does not establish export specifications or universal usage.

**Source files:** `f1c5ee3e7479d70b0060bc80af8a330c.mp4` (T10, 9–12 s); `017833d6758add159d297d753e03e084.mp4` (T01, 22 s).

### WRK-03 — Enter and audit property expressions

**Category:** Workflow · **Difficulty:** Intermediate · **Software:** After Effects

**Prerequisites:** Property hierarchy and basic expression syntax

**Related:** FIN-01, FIN-02, FIN-05

#### A. What is this technique?

Enable an expression on a specific animatable property and verify that its output drives the intended behavior.

#### B. Problem solved

Correct code on the wrong property can produce an error or a different effect. A code comment can also describe an intention the actual code fails to implement.

#### C. Finished result

The expression editor appears beneath the targeted property. Position returns a two-number array; Exposure returns one number; Random Seed receives `time*4`.

#### D. Required components

An expression-capable property, the source code, and a preview. The source shows a Mac-oriented Option-click instruction; no Windows shortcut is demonstrated.

#### E. Original workflow, gaps, and proposed completion

**Original:** T01 shows Option-clicking the stopwatch and entering expressions for Position and Exposure. T02 expands Evolution Options and enters code on Random Seed.

**Proposed audit:** Before pasting, confirm the full property path. After pasting, check for an error indicator, then scrub to two or more different times. Verify that each intended control variable changes the result. For FIN-02, changing the unused frequency variable in the original does not influence the output through its computed hold time; retain the original as evidence and test the separately proposed correction. Do not silently substitute one expression and still call it verbatim source code.

#### F. Motion mechanics and software-independent principle

Expressions supply values over time without requiring a keyframe at every change. Property dimensions and output type must match. Universal principle: an executable rule should be checked for scope, type, and causal influence—not just copied from a screenshot.

#### G. Settings and parameters

**Exact demonstrated interaction:** Option-click stopwatch. **Exact targets:** Transform effect Position; Exposure; Turbulent Displace > Evolution Options > Random Seed. **Not specified:** expression engine version or cross-platform shortcut demonstration.

#### H. Instructor tips

T01’s slide presents expressions as accessible and suggests AI can help write them. Apply that advice with verification: generated or copied code must still be checked. T02’s target hierarchy is a useful safeguard against pasting into Evolution instead of Random Seed.

#### I. Mistakes and troubleshooting

No expression error dialog is shown. **Inferred checks:** array dimension mismatch, wrong property, nonfunctional variables, and unintended resets. Evaluate at multiple times and compare with the unmodified layer before blaming the whole project.

#### J. Original applications

Build a small code library with target property, expected output type, source, and a test description. Reuse only when the new target has the same intended semantics.

#### K. Quality evaluation

No errors, correct target, visible intended behavior, and controls demonstrably affect the output. Code fidelity and practical correctness are recorded separately when they diverge.

#### L. Source and confidence

D/C plus I audit, high confidence in shown interactions and target paths. No After Effects execution test was performed for this document.

**Source files:** `017833d6758add159d297d753e03e084.mp4` (T01, 16–20.5 s); `37901357392ee8d7c14db082a78b701d.mp4` (T02, 36–40 s).

# BOOK VIII — CREATIVE APPLICATION

## 1. Technique selection framework

The following framework is **expert synthesis**, grounded in the source problems and outcomes. It is not another tutorial-derived preset.

| Decision | Ask | Select when supported | Reject or defer when |
|---|---|---|---|
| Narrative meaning | Is the sentence locating, comparing, quoting, changing, or connecting? | EDT-02 to choose the representation | A decorative asset cannot demonstrate the claim |
| Available assets | Is the text editable, the source legible, or the photo separable? | TYP-02 for editable text; IMG-01 for source images; IMG-02–04 for depth-rich photos | A raster article cannot directly receive character selectors |
| Required motion | Must something draw, travel, change identity, or reveal detail? | SHP-01, MOT-01, TRN-01, IMG-01 respectively | An animation adds no useful state or relationship |
| Complexity | How many simultaneous reading tasks exist? | EDT-05 to establish priority | Several presets compete for the same attention window |
| Aesthetic | Does material character help the subject? | FIN-03/07, optionally FIN-01/02/08/09 | The treatment damages information or merely copies a look |
| Production constraints | Is the method fully demonstrated, partially shown, or only a showcase? | Prefer well-supported methods for a tight deadline | A missing rig cannot be validated in available time |
| Surrounding scenes | What direction, scale, and focal position should continue? | TRN-01 or TRN-02 when a real correspondence exists | A transition falsely equates different subjects |
| Comprehension | What needs to remain readable after movement? | Add a stable endpoint and adequate hold | The target never resolves before the narration moves on |

**Example: “The country’s population doubled in only fifty years.”** First identify a quantity comparison over time. Verify the actual country, dates, figures, and source; none is supplied by that hypothetical sentence. A simple two-state display can communicate the relation more directly than an odometer flourish. EDT-02 supports choosing the representation; TYP-02 can emphasize the endpoint; EDT-05 protects reading order. TYP-04 does **not** provide a validated numerical counter, and no DAT recipe in this corpus teaches proportional charts. If proportional areas, a counter, or a map-based population density animation is required, obtain and validate an additional method. Do not claim that a montage supplies missing data mechanics.

## 2. Seven-stage scene construction

1. **Establish composition.** Choose the reading target and context. Use IMG-01 for a source, MAP-01 for geography, or IMG-02 for a depth-rich image. Draw a starting frame before applying finish.
2. **Introduce necessary information.** Give the source, location, or statement an identifiable presence. Use SHP-01 or TYP-02 only if their reveal behavior helps introduce it.
3. **Animate the main relationship.** Move the map focus, reframe the article, or change the camera viewpoint. Name the animated property and its endpoint; “make it dynamic” is not a build instruction.
4. **Add support.** Introduce one needed label, annotation, or tactile sound. EDT-05 governs priority; EDT-01 requires an actual listening check.
5. **Refine timing.** Shape a curve for its job using MOT-01 or TRN-01, then reserve reading time. Recheck the endpoint after changing timing.
6. **Connect to the next sequence.** Choose a cut, match, or movement connection from Book V. Do not add a transition solely because a recipe is available.
7. **Finish selectively.** Evaluate FIN-03/07 first, then optional chromatic separation, cadence, jitter, or flicker. Check each effect’s contribution independently and together.

## 3. Motion choreography contract

Before building, record: **first event; stationary anchor; overlapping support; eye target; settling time; disappearing elements; next-scene handoff.** This is an original planning contract informed by T04’s moving focus, T06’s shared driver, T07’s reading target, and T08’s overload warning.

For example, in a map comparison, the map can remain stationary while the focus field moves; the border begins only after the new area is clear; a label remains still while the viewer reads; the previous region’s emphasis diminishes; the next shot begins from the current focal location. This is a suggested combination, not a sequence demonstrated across the supplied clips.

## 4. Original plan A — “Two neighborhoods, one transit connection”

**Status:** Fictional training scenario. All proposed timings, layout choices, and sound placements below are original design values, not extracted tutorial settings. A factual production must use verified geographic data and accurate service information.

**Narrative objective:** Establish two neighborhoods, compare their location, then identify the connection. The animation should explain geography rather than merely decorate a map.

**Techniques and reasons:** MAP-01/02 (T04) share one moving focus field; SHP-01 (T04/T02) draws selected boundaries; EDT-05 (T08) keeps one reading target; EDT-01 (T03) provides an optional restrained tactile accent. FIN-03 (T01) is optional finish.

**Assets:** a prepared accurate map; two separate boundary paths; two labels; a separately verified connection graphic; a radial control layer; optional sound file. Map creation and route geometry are outside the supplied lessons.

**Suggested 12-second choreography:**

| Time | Picture/action | Driver and dependency | Verification |
|---|---|---|---|
| 0–2 s | Establish map and first neighborhood | Stable map; light/sharp focus at A | Context and A’s label readable |
| 2–3.5 s | Trace A’s boundary | SHP-01 on prepared path | Path follows actual boundary; no route implied |
| 3.5–5.5 s | Move attention from A to B | One animated gradient center drives MAP-01/02 | Bright and sharp areas remain aligned |
| 5.5–7 s | Trace B’s boundary and hold label | New stroke reveal after focus arrives | B gets priority; A becomes subordinate |
| 7–9 s | Introduce the connection | An original graphic reveal, separately constructed | Geometry accurate; the reveal is not falsely attributed to the map tutorial |
| 9–12 s | Hold both locations and the connection | Reduce selective suppression if both must be compared | Both labels and the connection can be understood together |

**Layer plan:** primary labels and borders above the blur adjustment; radial Multiply layer over the map treatment; Compound Blur input assigned to the radial field; map imagery below. Preserve accurate attribution on the map source.

**Sound plan:** one optional soft paper/mark accent on a boundary completion. Audition against narration; no invented tutorial gain target. Continuous edge-boil motion does not need continuous sound.

**Risk and revision:** a single sharp focus can hide the other location during the final comparison. Reduce or bypass the focus treatment for the joint hold. This is an original narrative adjustment, not a source conflict.

**Acceptance:** every location is readable at its beat; the blur’s polarity is correct; the route graphic is accurate; both places are available for the final comparison. The sequence still communicates with all finishing effects disabled.

## 5. Original plan B — “What the report actually says”

**Status:** Fictional training document. Do not present a fabricated report as real evidence. All durations below are proposed.

**Narrative objective:** Show the source, guide the reader to one sentence, and carry that sentence into a short explanatory statement.

**Techniques and reasons:** IMG-01 and TYP-01 (T07) establish source and selected reading; FIN-07 (T07/T10) supplies a restrained paper surface; TYP-02 and EDT-05 (T08) emphasize the new editable statement; EDT-01 (T03) supports the page action; MOT-01 (T10) shapes the arrival.

**Assets:** legible training report with a clearly marked fictional status; exact target sentence; a separate editable statement that accurately paraphrases it; paper texture; optional paper sound.

**Suggested 10-second choreography:**

| Time | Picture/action | Purpose and driver | Verification |
|---|---|---|---|
| 0–2 s | Show report title and context | Stable source frame | Report can be identified |
| 2–4 s | Reframe toward the target sentence | Coupled scale/position; rapid move with slow settle | Sentence reaches readable size without losing needed context |
| 4–5 s | Reveal highlight | TYP-01 proposed construction | Exact intended words emphasized; letters retain contrast |
| 5–7 s | Hold the source sentence | No new competing text animation | Viewer has time to read |
| 7–8 s | Cut to concise editable statement | Simple original editorial cut | Paraphrase preserves the source’s meaning |
| 8–9 s | Sweep fill across its key phrase | TYP-02 | Correct range and final color state |
| 9–10 s | Settle and hold | Stable endpoint | The thought completes before the next shot |

**Layer plan:** source image and its surface treatment move together; highlight remains registered to the words; the next statement uses editable text rather than attempting a selector on the article pixels.

**Sound plan:** align one paper movement with the source arrival or reframe, not every color change. Listen under narration and adjust the chosen file’s level by ear.

**Risk and revision:** the highlighted source may be too small at the planned framing. Obtain a higher-resolution source or revise the crop; do not use texture to conceal illegibility. If the statement is long, remove the fill sweep and extend the reading hold.

**Acceptance:** source attribution and sentence meaning are preserved, texture never obscures type, the highlight tracks the page, and the final statement has one clear emphasis.

## 6. Original plan C — “From photograph to mechanism”

**Status:** Original plan using an appropriately licensed image of a physical object. A simplified schematic must be checked for explanatory accuracy. All shot timings are proposed.

**Narrative objective:** Begin with a real-world object in context, then change representation to explain one component while preserving visual continuity.

**Techniques and reasons:** IMG-02/03/04 (T09) prepare a subtle parallax opening; TRN-01 (T06) changes the object into a schematic at peak speed; SHP-01 and FIN-04/05 (T02) draw a component annotation; EDT-05 (T08) governs label timing; optional FIN-09 (T10) supplies a consistent stepped finish if it remains legible.

**Assets:** depth-rich photo; isolated object; repaired background; accurate simplified schematic; a common visual focal point; annotation path; one short label. A pure photograph of a flat document would not justify parallax.

**Suggested 14-second choreography:**

| Time | Picture/action | Construction and dependency | Verification |
|---|---|---|---|
| 0–4 s | Slow parallax establishes the object | Prepared depth planes and modest camera move | No exposed hole, halo, or plane edge |
| 4–5 s | Settle on the focal component | Finish camera move before handoff rig | Stable registration reference |
| 5–7 s | Accelerate object representation into transition | Shared motion driver; schematic parented/aligned | Photo and schematic match at intended cut |
| At measured peak within 5–7 s | Hard cut to schematic | TRN-01; actual graph peak, not assumed 6 s | No duplicate or empty frame |
| 7–9 s | Schematic decelerates to reading position | Same underlying motion continuation | Final scale and placement appropriate |
| 9–10.5 s | Draw a circle around one component | SHP-01 then restrained edge treatment | Annotation selects the correct part |
| 10.5–14 s | Reveal and hold the short label | EDT-05; no competing motion | Component and explanation readable together |

**Rig boundary:** the parallax camera and the matched-transition driver are different systems. A proposed production route is to precompose the prepared photo view for the handoff, then match that representation to the schematic. That precomposition solution is original, not shown in T06 or T09 as a combined workflow.

**Risk and revision:** complex depth movement can make registration difficult. Complete and settle the parallax first, or replace it with a simpler opening. If 12 fps sampling hides the most useful handoff state, revise the movement or omit the finish for that shot.

**Acceptance:** the real-to-diagram relationship is unmistakable, the transition shares momentum, the schematic is accurate, and only one component receives the initial annotation.

## 7. Adaptation policy for other software and code-based renderers

The universal principles can guide another compositor or an HTML/Canvas renderer, but no supplied clip demonstrates those environments. Treat every such implementation as **an adaptation requiring verification**. Preserve the result contract rather than inventing matching menu commands: a path reveal needs a visible-length control; a map focus needs one spatial field feeding darkening and blur; parallax needs separate depth-responsive layers; an expression needs a deterministic time input; tactile sound needs sample-accurate or perceptually checked synchronization.

Do not claim that a CSS filter, shader, or JavaScript noise function is an exact equivalent of the named After Effects effect without comparison. Test start, midpoint, endpoint, and continuous playback. Record substitutions so later agents can distinguish the original lesson from the new implementation.

# BOOK IX — TRAINING EXERCISES

All exercises below are original tasks. Their chosen durations, subjects, and acceptance tests are not source parameters. Each exercise produces a small inspectable result before techniques are combined into a larger sequence.

## Beginner exercises

### B1. One useful annotation

**Learning objective:** Separate path construction from path visibility.

**Relevant techniques:** SHP-01; EDT-05.

**Creative task:** Circle one phrase on a fictional one-page notice in a four-second shot.

**Required elements:** notice image, one shape path, stroke, Trim Paths.

**Construction plan:** Choose the exact phrase; draw a path that surrounds it without crossing letters; add Trim Paths; use a proposed End 0→100% animation; hold the complete mark. Keep all other elements still.

**Expected result:** A clear drawing action ends on the intended words.

**Evaluation:** First visible segment is intentional; no unexpected fill; complete stroke is continuous; target remains readable. Check a partial-reveal frame as well as the endpoint.

**Common problems:** wrong shape group, wrong path direction, circle too tight, unnecessary text movement.

### B2. A material sound with a specific job

**Learning objective:** Relate a sound event to a visible action and perform the missing auditory check.

**Relevant techniques:** EDT-01; IMG-01.

**Creative task:** Introduce a single paper card with one tactile sound.

**Required elements:** a card graphic, a chosen paper-related audio file, narration or a spoken placeholder, editable audio track.

**Construction plan:** Make the visual arrival; identify its meaningful onset; trim and align the sound’s event; audition with narration; adjust level; compare against a silent version.

**Expected result:** The sound reinforces the card’s action without masking speech.

**Evaluation:** Listen on headphones and ordinary speakers if available; check transient alignment and clipping. The exercise cannot pass through screenshots alone.

**Common problems:** lining up file start rather than sound onset, excessive gain, long distracting tails, assuming T03’s changing tooltip is a mix target.

### B3. Directed article reading

**Learning objective:** Move from source context to a readable target and stop.

**Relevant techniques:** IMG-01; TYP-01; EDT-05.

**Creative task:** Present a fictional report title, then one highlighted sentence in six seconds.

**Required elements:** high-resolution training article and a highlight graphic.

**Construction plan:** Define context and detail frames; animate scale/position; settle; reveal a simple highlight; hold. Label the highlight implementation as original because T07 omits construction.

**Expected result:** The viewer knows the source and immediately sees the relevant passage.

**Evaluation:** Read the target at actual delivery size; confirm no essential qualifier is cropped; verify highlight registration throughout the move.

**Common problems:** insufficient source resolution, highlight covering letters, no reading hold, overly broad selection.

## Intermediate exercises

### I1. Build and diagnose edge boil

**Learning objective:** Tune static roughness, fine disturbance, and broad movement separately.

**Relevant techniques:** FIN-04, FIN-05, FIN-06; SHP-01.

**Creative task:** Produce three versions of the same annotation: clean, fine boil, and fine-plus-broad boil.

**Required elements:** one stroked shape, Roughen Edges, two Turbulent Displace effects, Random Seed expression.

**Construction plan:** Start with a valid path reveal; apply the half-stroke-width border relationship; set the fine pass to Amount 80/Size 2 and Random Seed `time*4`; duplicate for a broader pass with increased Size and reduced Amount. Record your own final broad-pass values rather than claiming a source final preset.

**Expected result:** Each stage adds a distinguishable type of imperfection while retaining the same target.

**Evaluation:** Compare on/off for each pass; inspect clipping, line continuity, and target accuracy over several seconds.

**Common problems:** animating Evolution instead of Random Seed; using two aggressive passes; applying distortion to the source image.

### I2. One field, two map cues

**Learning objective:** Coordinate darkening and blur with a shared control field.

**Relevant techniques:** MAP-01; MAP-02; SHP-01.

**Creative task:** Move focus between two regions, then draw the second boundary.

**Required elements:** prepared map, radial gradient, Multiply blending, Compound Blur adjustment, accurate path.

**Construction plan:** Test gradient polarity; assign it as Blur Layer; reproduce the visible 15.0 blur and checked inversion/stretch states as a starting example; animate the center; reveal the boundary only after focus arrives.

**Expected result:** The brighter and sharper area moves as one cue.

**Evaluation:** Pause at both regions and halfway between them; check gradient source assignment, readable labels, and adjustment scope.

**Common problems:** choosing the hovered wrong layer, inverted attention, blur affecting labels, incompatible gradient-source sampling.

### I3. A reusable fill animation that survives new text

**Learning objective:** Separate animator behavior from source-specific layout.

**Relevant techniques:** TYP-02; WRK-01; EDT-05.

**Creative task:** Save one fill sweep and apply it to three different short phrases.

**Required elements:** editable text layers, Fill Color animator, selector animation.

**Construction plan:** Build and verify a simple selector sweep; select only intended reusable properties; save a preset; test on fresh short, medium, and longer phrases; document any timing adjustments.

**Expected result:** Consistent animation behavior without unintended relocation or content replacement.

**Evaluation:** Every phrase ends complete and readable; colors and selectors are correct; no unplanned properties are copied.

**Common problems:** source-text replacement, unintended Position values, an incomplete selected range, a long phrase receiving too little reading time.

## Advanced exercises

### A1. Cut the curve without a visual jump

**Learning objective:** Coordinate a continuous motion trajectory and discrete representation change.

**Relevant techniques:** TRN-01; MOT-01.

**Creative task:** Change a photographed object into a simple illustrative counterpart during one movement.

**Required elements:** two compatible representations, Position animation, parent link, speed graph.

**Construction plan:** Align a shared focal point; animate the first representation; parent the second; verify local offset/scale; place the cut at the measured speed peak; inspect the adjacent frames. Repeat with an asymmetric curve and relocate the cut accordingly.

**Expected result:** The viewer tracks one moving idea despite the change in appearance.

**Evaluation:** No gap, overlap, jump, or speed restart; destination readable. The second version proves that the cut was based on the graph rather than a memorized midpoint.

**Common problems:** assuming parenting aligns artwork, deleting the driver, cutting at half duration after reshaping the curve.

### A2. Parallax asset preparation under stress

**Learning objective:** Make separation and repair robust to the chosen camera move.

**Relevant techniques:** IMG-02; IMG-03; IMG-04; optional WRK-02.

**Creative task:** Turn a licensed depth-rich photograph into a modest moving shot, then test a larger move to expose preparation limits.

**Required elements:** original image, three or more justified planes, repaired hidden regions, camera rig.

**Construction plan:** Preserve original; isolate planes; repair behind subjects; import as layers; distribute depth; restore starting framing; add a small move; temporarily exaggerate it to find holes; fix or reduce the final move.

**Expected result:** Subtle relative motion, no newly exposed defects in the final range.

**Evaluation:** Compare original versus first frame; inspect side view and camera view; inspect maximum camera positions; verify all hidden areas that become visible.

**Common problems:** cloned repetition, cutout halos, background too small, unverified script behavior, excessive motion that invents implausible perspective.

### A3. An evidence-audited explanatory sequence

**Learning objective:** Combine techniques while preserving source confidence and narrative clarity.

**Relevant techniques:** EDT-02/03/04/05; choose at least one technique from T02, T04, T06, or T09; choose one supported typography or finishing treatment.

**Creative task:** Build a 12–18 second fictional training explainer with three information beats and one meaningful transition.

**Required elements:** short script, asset list, technique selection table, scene timing plan, visuals, optional tactile audio.

**Construction plan:** Identify claims; select representations; write starting/ending frames; build the main relationship; add one transition; add support; finish selectively. Log each setting as source-exact, approximate, or original. Conduct visual, motion, technical, story, and listening checks.

**Expected result:** A coherent sequence whose effect choices can be explained and traced.

**Evaluation:** A reviewer can understand the argument without the original tutorials; every missing-source implementation is labeled; no effect overload; no unsupported chart/data claims. Retain one revision explaining which effect was removed or simplified and why.

**Common problems:** using a showcase as if it supplied a rig, hiding missing explanation with texture, filling every moment with movement, reporting an unperformed audio or export check as complete.

## Experiment: resolve the exposure expression’s cadence

This optional diagnostic specifically addresses G03 in the gaps register. On a fixed test image, compare FIN-02’s original code with the proposed quantized-seed code. Hold strength constant. Change `freq` through two or more values and observe whether the sequence of held values changes. Record evaluated Exposure over several frame times. The original code’s unused `floorTime` should not control its output; the correction is intended to change only at quantized steps. Execute this in After Effects before claiming a verified behavior. A static code inspection is evidence of the unused variable, not a rendered result.

# BOOK X — MASTER TECHNIQUE INDEX

The two tables below are joined by Technique ID. Together they provide identity, category, difficulty, purpose, prerequisites, software, source, evidence type, and related techniques. Complete instructions are in Book VII under the exact same ID. No DAT entry is manufactured from the collection’s incidental numeric examples.

## Identity and purpose

| ID | Technique | Category | Difficulty | Purpose |
|---|---|---|---|---|
| MOT-01 | Rapid movement with a long settling ease | Motion | Intermediate | Shape a purposeful arrival |
| SHP-01 | Draw an annotation or border with Trim Paths | Shapes | Beginner/intermediate | Reveal a line along its route |
| FIN-01 | Subtle global Position jitter | Finishing | Intermediate | Give a composition small mechanical movement |
| FIN-02 | Exposure flicker, with an original-code caveat | Finishing | Intermediate | Create slight time-varying brightness |
| FIN-03 | Add a restrained grain finish | Finishing | Beginner | Unify a clean composition with fine image texture |
| FIN-04 | Roughen a drawn stroke before animating its edge | Finishing | Intermediate | Break a mechanically perfect annotation contour |
| FIN-05 | Animate fine edge boil through Random Seed | Finishing | Intermediate | Keep a hand-drawn contour subtly changing |
| FIN-06 | Add broader wobble with a second displacement pass | Finishing | Intermediate | Separate large contour motion from fine edge chatter |
| MAP-01 | Move a radial Multiply spotlight across a map | Maps | Intermediate | Direct attention while retaining geographic context |
| MAP-02 | Use the gradient as an inverted Compound Blur map | Maps | Intermediate | Make the highlighted region sharper than its surroundings |
| TRN-01 | Hard cut at peak velocity with shared parenting | Transitions | Intermediate | Maintain movement while changing representation |
| EDT-01 | Build tactile sound around visible material actions | Editing/audio | Beginner/intermediate | Give graphic actions a physical association |
| EDT-02 | Translate narrated claims into explanatory visual assets | Editorial | Beginner | Make abstract narration inspectable |
| EDT-03 | Plan ongoing visual progression without losing reading time | Editorial | Beginner | Maintain pacing and purposeful change |
| EDT-04 | Coordinate story, edit, and graphics as one production plan | Editorial | Beginner | Prevent isolated effects from substituting for explanation |
| TRN-02 | Plan zoom, slide, and compositional match transitions | Transitions | Beginner/intermediate | Connect scenes through a visible relationship |
| IMG-01 | Reframe an article from context to reading detail | Images | Beginner | Make a dense source document readable |
| FIN-07 | Integrate paper and surface textures | Finishing | Beginner/intermediate | Give documents and fills a material character |
| TYP-01 | Highlight the passage that narration discusses | Typography/annotation | Beginner | Direct reading within a source document |
| TYP-02 | Sweep a text animator’s Fill Color through characters | Typography | Intermediate | Create controlled character-level emphasis |
| TYP-03 | Random-order character appearance as a result target | Typography | Intermediate | Introduce a short phrase with scattered character timing |
| TYP-04 | Odometer-style text and numeric-display showcase | Typography | Intermediate/advanced | Give short labels or figures a mechanical reveal |
| WRK-01 | Save selected animation behavior as a preset | Workflow | Intermediate | Reuse text animation without rebuilding it |
| EDT-05 | Give animated typography one clear reading priority | Editorial/typography | Beginner | Prevent motion-driven reading conflict |
| IMG-02 | Separate a photograph into depth planes | Images | Intermediate | Prepare a still image for parallax |
| IMG-03 | Repair regions hidden behind extracted subjects | Images | Intermediate | Prevent holes when depth planes move apart |
| IMG-04 | Create parallax with 3D image planes and a camera move | Images/motion | Intermediate/advanced | Give a still photograph spatial depth |
| WRK-02 | Use the optional Depth script for parallax setup | Workflow | Intermediate | Reduce repetitive plane-spacing setup |
| FIN-08 | Add restrained chromatic edge separation | Finishing | Beginner/intermediate | Introduce subtle optical imperfection |
| FIN-09 | Apply a 12 fps picture-sampling treatment | Finishing | Beginner/intermediate | Create a deliberately stepped temporal character |
| WRK-03 | Enter and audit property expressions | Workflow | Intermediate | Apply code to the correct control and verify its function |

## Retrieval, prerequisites, and relationships

D = demonstrated interface/action; C = caption-supported instruction; R = result-only evidence. Proposed completion and universal explanation are marked as inference in the recipes. File identities resolve through the source registry and each recipe’s Source files line.

| ID | Prerequisites | Software | Source / timestamp | Tutorial evidence | Related techniques |
|---|---|---|---|---|---|
| MOT-01 | Transform keyframes and speed graph | After Effects | T10 13–16 s; T06 6–9 s | D/C | TRN-01, IMG-01, EDT-05 |
| SHP-01 | An editable stroked shape path | After Effects | T02 21–25 s; T04 18–20 s | D/R | FIN-04, FIN-05, MAP-02 |
| FIN-01 | 2D effect Position and expression entry | After Effects | T01 4–8 s; 15–20 s | D/C | WRK-03, FIN-02, FIN-03, FIN-09 |
| FIN-02 | Exposure effect and expressions | After Effects | T01 18–20.5 s; 22 s | D/C; code audit I | FIN-01, FIN-03, WRK-03 |
| FIN-03 | Effects panel and delivery-size preview | After Effects | T01 21–23 s | D/C | FIN-01, FIN-02, FIN-07 |
| FIN-04 | A stroked annotation shape | After Effects | T02 24–30 s | D/C | SHP-01, FIN-05, FIN-06 |
| FIN-05 | FIN-04, effect expressions | After Effects | T02 30–42 s | D/C | FIN-04, FIN-06, WRK-03 |
| FIN-06 | FIN-05 working on a stroke | After Effects | T02 42–48 s | D/C | FIN-04, FIN-05 |
| MAP-01 | Prepared map and blend modes | After Effects | T04 0–9.5 s; 14.5–17 s | D/C | MAP-02, SHP-01, EDT-05 |
| MAP-02 | MAP-01 and adjustment-layer scope | After Effects | T04 9.5–17 s | D/C | MAP-01, SHP-01 |
| TRN-01 | Position keyframes, speed graph, Parent & Link | After Effects | T06 0–21 s | D/C/R | MOT-01, TRN-02, EDT-05 |
| EDT-01 | Timeline audio placement and suitable sound files | Premiere-style timeline; After Effects also visible | T03 0–22 s | D/C; audio unverified | SHP-01, IMG-01, FIN-07 |
| EDT-02 | A script and relevant evidence/assets | Construction software not shown | T05 4–26 s | C/R | EDT-03, EDT-04, IMG-01, MAP-01, TYP-02 |
| EDT-03 | Script beats and a rough edit | Construction software not shown | T05 26–40 s; T08 22–26 s | C/R | EDT-02, EDT-05, IMG-01 |
| EDT-04 | Script and rough scene order | Construction software not shown | T05 48–58 s | C/R | EDT-02, EDT-03, EDT-05 |
| TRN-02 | Two shots with a meaningful correspondence | Construction software not shown | T05 40–47 s | C/R | TRN-01, MOT-01, IMG-01 |
| IMG-01 | High-resolution article image and a clear target passage | Construction software not shown | T07 3–7 s; 16–24 s | C/R | TYP-01, MOT-01, FIN-07, EDT-03 |
| FIN-07 | Readable base artwork and suitable texture assets | Result examples in T07; After Effects visible in T10 | T07 8–15 s; T10 17–20 s | C/R | IMG-01, FIN-03, TYP-01 |
| TYP-01 | Source image and correctly selected words | Construction software not shown | T07 16–24 s | C/R | IMG-01, SHP-01, EDT-05 |
| TYP-02 | Editable text and selector basics | After Effects | T08 5–8 s; 10–15 s | D/C/R | WRK-01, EDT-05, TYP-03 |
| TYP-03 | Editable text and a readable final phrase | After Effects context; construction not shown | T08 16–17 s | R | TYP-02, EDT-05, WRK-01 |
| TYP-04 | Editable text or prepared character elements | After Effects context; full construction not shown | T08 5.5 s; 18–21 s | R; limited D | TYP-02, WRK-01, EDT-05 |
| WRK-01 | A working animator and deliberate property selection | After Effects | T08 8–11 s | D/C | TYP-02, TYP-03, TYP-04 |
| EDT-05 | A scene with multiple text elements | After Effects examples; judgment is software-independent | T08 22–26 s; T07 16–24 s | C/R | TYP-01, TYP-02, EDT-03 |
| IMG-02 | Image selection, layer editing, and subject isolation | Photoshop | T09 13–20.5 s | D/C | IMG-03, IMG-04, WRK-02 |
| IMG-03 | IMG-02 and basic retouching | Photoshop | T09 21–24.5 s | D/C | IMG-02, IMG-04 |
| IMG-04 | IMG-02, IMG-03, 3D layers and camera basics | After Effects, following Photoshop preparation | T09 24.5–36 s | D/C/R | IMG-02, IMG-03, WRK-02, MOT-01 |
| WRK-02 | Separated layers and an understood parallax goal | After Effects with optional Depth utility | T09 28–31 s | D/C | IMG-04, IMG-02 |
| FIN-08 | A finishing layer and the named plugin | After Effects; Quick Chromatic Aberration 3 | T10 3–8 s; T01 16–22 s | D/C/R | FIN-01, FIN-03, FIN-09 |
| FIN-09 | An animated composition and effect scope | After Effects | T10 9–12 s; T01 22 s | D/C | MOT-01, FIN-01, FIN-05 |
| WRK-03 | Property hierarchy and basic expression syntax | After Effects | T01 16–20.5 s; T02 36–40 s | D/C; audit I | FIN-01, FIN-02, FIN-05 |

## Problem-based retrieval

| Need | Start here | Check before building |
|---|---|---|
| A still photo needs depth | IMG-02 → IMG-03 → IMG-04 | Does it have separable planes and enough repair coverage? |
| An article must be read quickly | IMG-01 → TYP-01 → EDT-05 | Is the relevant passage genuinely legible? |
| A line should draw on | SHP-01 | Is it a stroked shape path, and is its direction correct? |
| A line should look redrawn | FIN-04 → FIN-05; optional FIN-06 | Is distortion isolated to the annotation? |
| Map attention should travel | MAP-01 → MAP-02 | Does the bright region correspond to the sharp region? |
| A moving subject changes representation | TRN-01 | Are artwork registration and motion shared at the cut? |
| Text needs a reusable fill sweep | TYP-02 → WRK-01 | Are selector behavior and saved property scope validated? |
| A random or odometer reveal is requested | TYP-03 / TYP-04 | These are incomplete source implementations; plan a test or substitute |
| The image is too pristine | FIN-03 / FIN-07 first; consider other FIN entries | Does the finish preserve legibility? |
| A sound should feel physical | EDT-01 | Has the actual sound been auditioned under narration? |
| The sequence feels busy | EDT-05, then EDT-03 | Which event is unnecessary or mistimed? |
| The idea remains unclear despite good motion | EDT-02 and EDT-04 | Is the representation or sequence logic wrong? |

# BOOK XI — AI AGENT OPERATING MANUAL

## 1. Operational procedure

1. **Parse the new task.** Extract the claim, intended audience, available time, delivery constraints, and required assets. Identify whether the problem is geographic, quantitative, documentary, spatial, or rhetorical.
2. **Separate facts from visual choices.** Verify factual claims through appropriate sources for the actual project. The tutorials teach treatments, not the truth of a new story.
3. **Retrieve by problem.** Use Book X, then read the complete A–L recipe. Do not build from an index title alone.
4. **Grade support.** Identify what is demonstrated, caption-supported, result-only, and proposed. Prefer a well-supported method when time or tool access prevents experimentation.
5. **Check prerequisites.** Confirm editable text versus raster source, shape path versus mask, separated planes versus flat photo, and named plugin availability. Do not silently substitute a different asset type.
6. **Choose between alternatives.** Use the comparison tables in Books V–VI. Record why one method suits the narrative. Keep different source methods separate until an explicitly original combination is planned.
7. **Write the scene contract.** Specify starting frame, main change, final frame, eye target, timing relationships, layer structure, and source IDs. Every numeric value must be tagged source-exact, approximate, or original.
8. **Build the smallest working mechanism.** Test the untextured path, shared movement, selector, gradient field, or depth rig before adding finishing treatments. Diagnose structure before style.
9. **Add supporting elements.** Apply EDT-05 so labels, sound, and texture reinforce the main event. Reusing a preset does not waive the reading check.
10. **Evaluate and diagnose.** Run the gates below. Fix the earliest causal failure: source quality, geometry, scope, timing, hierarchy, then finish.
11. **Record limitations honestly.** If audio has not been auditioned, a plugin not loaded, or a render not produced, state that. A planned result is not a tested deliverable.
12. **Improve the reusable library.** Record the final validated values with project resolution and context. Preserve original-source values separately. Update proposed adaptations only after testing them.

## 2. Required scene specification

Use this compact record for every production scene:

```text
Scene ID and narrative claim:
Source asset / attribution / factual verification:
Reading target:
Initial frame:
Main visual relationship:
Final frame and readable hold:
Technique IDs and source tutorials:
Demonstrated steps retained:
Missing steps / proposed adaptations:
Layer order and parent/control relationships:
Animated properties and start/end states:
Timing and easing (source-exact / approximate / original):
Audio event and listening status:
Finishing scope and dependencies:
Next-scene connection:
Quality gates and observed result:
Remaining uncertainty / fallback:
```

## 3. Decision rules for recurring production questions

These rules are **expert synthesis** from the cited recipes, not direct quotations.

| Question | Working rule | Grounding |
|---|---|---|
| When should a photograph become a layered scene? | When visible depth separation helps explain or immerse, and clean isolation/repair is feasible | IMG-02–04 |
| When should framing replace parallax? | When the task is reading a source or the photo has weak depth | IMG-01 versus IMG-04 |
| When should masking replace opacity? | When a spatial reveal is needed rather than whole-object fading; select and validate a separate mask implementation because this corpus does not fully teach one | SHP-01 demonstrates path extent, not a general mask tutorial |
| When should motion be staggered? | When simultaneous events create competing reading targets | EDT-05 |
| When is camera movement useful? | When it reveals depth or a relevant change of viewpoint, not just because a 3D switch is available | IMG-04 |
| When should a transition be simple? | When no meaningful spatial or representational correspondence exists | TRN-01/02 and EDT-04 |
| When should a graphic remain static? | During a necessary reading or comparison window, especially after its main relationship is established | IMG-01, EDT-05 |
| When should typography be the moving subject? | When the exact words or number are the information, and their final state is verifiable | TYP-02–04 |
| How should multiple finishing effects be combined? | Add and evaluate one contribution at a time, then inspect the combined result at delivery size | FIN-01–09 |
| When should a source gap stop a complex build? | When it affects correctness or cannot be validated; use a supported simpler method rather than inventing certainty | TYP-03/04, WRK-02, gaps register |

## 4. Quality-assurance gates

“S” identifies a standard directly supported by a tutorial’s advice or result. “I” identifies an additional production check inferred here. Passing must be based on the actual project, not a statement of intention.

### Visual quality

| Gate | Basis | Pass condition | Failure action |
|---|---|---|---|
| Reading priority | S: T07/T08 | Main text target is obvious | Delay/remove competing event |
| Source readability | S: T07 | Target passage readable at final size | Reframe or improve source |
| Annotation accuracy | S/I: T02/T04 | Mark identifies intended word/region throughout motion | Correct path or reduce displacement |
| Material restraint | S/I: T01/T10 | Grain/fringes/texture do not dominate | Reduce or remove finish |
| Image integration | S/I: T09 | Separated planes still form one coherent scene | Repair edges, scale, registration |
| Color and alignment consistency | I | Repeated roles use consistent treatments and deliberate alignment | Standardize roles, not every asset’s appearance |

### Animation quality

| Gate | Basis | Pass condition | Failure action |
|---|---|---|---|
| Curve purpose | S: T06/T10 | Speed behavior suits handoff or arrival | Reshape graph against actual motion |
| Handoff continuity | S: T06 | Compatible position, direction, scale, and speed across cut | Fix registration and driver before polish |
| Focus synchronization | S: T04 | Bright and sharp areas coincide | Fix input layer and inversion |
| Controlled contour motion | S: T02 | Edge changes without losing annotation meaning | Adjust spatial scale/amount separately |
| Stable endpoint | S/I: T07/T08 | Information settles for reading | Finish motion earlier or lengthen hold |
| Blur, if additionally used | I | Helps motion without obscuring meaning or exposing edges | Tune or omit; no source blur preset exists |

### Technical quality

| Gate | Basis | Pass condition | Failure action |
|---|---|---|---|
| Expression scope and type | S/I: T01/T02 | Correct property, no errors, intended output | Inspect target path and return type |
| Expression control functionality | I: FIN-02 audit | Each advertised control actually affects the output | Repair and label the deviation from source |
| Compositing scope | S/I: T04 | Only intended layers blurred/darkened | Reorder or isolate adjustment |
| No exposed hidden regions | S: T09 | Camera range reveals no holes/duplicates | Extend repair or reduce move |
| Correct final text/value | I | Every character and punctuation mark resolves correctly | Repair selector/rig or simplify |
| Deterministic reuse | I | Preset/adaptation repeats predictably on fresh content | Remove unintended saved properties |
| Export | Gap | Requirements verified for the actual destination | Obtain delivery specification; no source export recipe exists |

### Storytelling and sound quality

| Gate | Basis | Pass condition | Failure action |
|---|---|---|---|
| Representation fit | S: T05 | Image exposes the sentence’s relationship | Change representation |
| Visual progression | S: T05 | Changes follow information beats | Retime or remove decorative changes |
| Combined story/edit/graphics | S: T05 | Rough sequence communicates before finishing | Revise structure |
| Source integrity | I | Crop/highlight preserves meaning and attribution | Restore context or rewrite claim |
| Tactile association | S: T03 | Sound supports a visible material action | Choose or place a more suitable event |
| Auditory clarity | I; T03 advises level adjustment | Narration clear, no clipping, intentional alignment | Audition and rebalance; never certify from screenshots |

## 5. Troubleshooting order

| Symptom | First diagnosis | Correction path |
|---|---|---|
| Map target becomes blurrier | Wrong polarity or input | MAP-02: check Invert Blur and actual gradient assignment |
| Drawn stroke destroys letters | Wrong effect scope or excessive roughness | FIN-04/05: isolate mark, check half-width relation and Size |
| Broad boil looks liquid | Second pass too strong | FIN-06: reduce Amount while retaining larger Size |
| Transition jumps despite parenting | Artwork registration/local offset | TRN-01: align focal geometry at the cut |
| Text preset moves to an old location | Unintended saved transforms | WRK-01: select a narrower property scope and retest |
| Random letters never finish | Incomplete visibility/selector endpoint | TYP-03: enforce full final state and hold |
| Number display looks impressive but is wrong | Decorative rig confused with factual values | TYP-04: validate endpoint and data separately |
| Parallax exposes a blank strip | Insufficient repaired/background coverage | IMG-03/04: extend coverage or reduce camera excursion |
| Jitter reveals frame edges | Inadequate coverage/overscan | FIN-01: cover actual movement range, verify crop |
| Flicker rate slider appears ineffective | Original `freq` logic unused | FIN-02: test original, then explicitly test proposed correction |
| Entire sequence is tiring | Competing onsets and no reading hold | EDT-05/03: simplify choreography before changing finish |
| Audio timing seems uncertain from the timeline | Sound’s meaningful onset is unknown | EDT-01: listen; inspect and align the actual event |

## 6. Tutorial Coverage Matrix

This matrix audits the supplied visual/caption content against the recipes. “Covered” means documented to the available evidence level; it does not certify full audio transcription or execution-tested reproduction.

| Tutorial | Extracted technique IDs | Primary and secondary knowledge preserved | Important limitation |
|---|---|---|---|
| T01 | FIN-01, FIN-02, FIN-03, FIN-08, FIN-09, WRK-03 | Global Position jitter; Exposure code; grain; expression entry; visible 12 fps and chromatic stack; code defect separated from correction | Full layer setup, final grain amount, and audio unverified |
| T02 | SHP-01, FIN-04, FIN-05, FIN-06, WRK-03 | Trim Paths; half-width roughness relationship; fine seed-driven boil; duplicate broad pass; order and intermediate adjustments | Final second-pass amount and complete saved effect state unresolved |
| T03 | EDT-01 | Material sound categories; recording/library routes; clip placement; level adjustment; complete on-screen sound list | No audition; exact synchronization and final mix unverified |
| T04 | SHP-01, MAP-01, MAP-02 | Radial Multiply layer; checked Compound Blur inversion; input selection; animated center; Trim Paths borders | Map construction and full control-field setup omitted |
| T05 | EDT-02, EDT-03, EDT-04, TRN-02 | Visualize claims; use motion to explain; ongoing progression; zoom/slide/match families; story/edit/graphics | Overview only; no operational chart or transition rigs |
| T06 | MOT-01, TRN-01 | Strong easing; second-to-first parenting; peak-speed hard cut; continuity examples | Alignment preparation and exact timing values omitted |
| T07 | IMG-01, FIN-07, TYP-01, EDT-05 | Article reframing; physical paper presentation; selected passage emphasis | Advertised full highlighter tutorial not supplied |
| T08 | EDT-03, TYP-02, TYP-03, TYP-04, WRK-01, EDT-05 | Text Animate menu; Fill Color/selector evidence; save command; random/odometer showcases; numeric example; clutter warning | Random/odometer rigs and complete selector keys absent |
| T09 | IMG-02, IMG-03, IMG-04, WRK-02 | Depth-rich photo; named planes; Clone Stamp repair; 3D distribution; optional Depth UI; camera move | Manual import/rig/keyframes and exact camera axis incomplete |
| T10 | MOT-01, FIN-07, FIN-08, FIN-09 | Named chromatic plugin; 12.0 Posterize Time; asymmetric easing graph; surface texture | No exact aberration parameters, texture recipe, or export specifications |

## 7. Chronological inspection ledger

Times are rounded local clip times. The full duration was visually surveyed at roughly one-second intervals; denser crops and full-resolution frames were used for selected details. End cards were inspected for additional instruction and not expanded into artificial techniques.

| Tutorial | Chronological content surveyed | Additional close inspection |
|---|---|---|
| T01 | 0–4 hook/result; 4–9 film-mechanism explanation; 9–15 clean/treated contrast; 15–21 effects and expressions; 21–24 grain/result; 24–28 preset promotion; 28–31.61 end card | 15–23 s at about 4 samples/s; expression slide and effects controls at full resolution |
| T02 | 0–10 annotation example; 10–21 frame-drawing explanation; 21–26 Trim Paths and stroke; 26–30 Roughen Edges; 30–36 fine displacement; 36–42 Random Seed expression/result; 42–49 second pass/result; 49–52.61 outro | 26–30 and 43–48 s at about 4 samples/s; full-resolution controls and code |
| T03 | 0–9 tactile concept and recording example; 9–14 materials and sound list; 14–17 sources/recording; 17–20 audio clips and gain; 20–23 sense association; 23–27.15 end card | Full-resolution timeline and gain frames; no audio audition |
| T04 | 0–6 map attention example; 6–10 gradient/Multiply; 10–15 adjustment and Compound Blur; 15–18 focus movement; 18–21 Trim Paths; 21–26.05 promotion/end card | 6–15 s at about 4 samples/s; blur checkboxes and animated Start Point at full resolution |
| T05 | 0–4 hook; 4–15 visualize information; 15–26 explanatory motion; 26–40 ongoing motion; 40–48 transitions; 48–59 story/edit/graphics; 59–63 promotion; 63–66.52 end card | Ordered result survey; no settings to recover |
| T06 | 0–6 examples/concept; 6–10 eased movement; 10–13 parenting; 13–17 peak and cut; 17–22 results; 22–27 promotion; 27–31.26 end card | 8–17 s at about 4 samples/s; Parent & Link and graph frames at full resolution |
| T07 | 0–3 hook; 3–8 article movement; 8–16 texture; 16–25 selective emphasis; 25–29 full-tutorial promotion; 29–32.95 end card | Ordered result survey; advertised external lesson not accessed |
| T08 | 0–5 type examples; 5–9 Animate/fill UI; 9–12 save/reuse context; 12–16 fill and figure examples; 16–18 random letters; 18–22 odometer/numbers; 22–27 clutter warning; 27–31 promotion; 31–34.80 end card | Full-resolution animator hierarchy, menu, and save command; motion from sampled sequence, not glyph-by-glyph playback |
| T09 | 0–9 flat/depth comparison; 9–13 examples/intro; 13–18 image selection and planes; 18–21 layer separation; 21–25 Clone Stamp; 25–28 AE import/3D; 28–32 optional script/manual advice; 32–37 camera/result; 37–41.39 end card | 13–25 s at about 4 samples/s; Photoshop, Depth panel, and transform states at full resolution |
| T10 | 0–3 hook; 3–9 chromatic treatment/plugin; 9–13 12 fps; 13–17 easing; 17–21 texture; 21–26 promotion; 26–30.15 end card | Full-resolution speed graph; ordered before/after and effect-control survey |

## 8. Knowledge Gaps Register

A gap is retained even when a proposed completion is supplied. Closing a gap requires the missing source, an explicit design decision, or a recorded application test—not more confident wording.

| Gap | Affected recipes | What is not established | Why it matters | Resolution question or experiment |
|---|---|---|---|---|
| G01 | All; especially EDT-01 | Independent audio transcript and listening assessment | Captions can omit words; sound quality cannot be inferred from screenshots | Audition original clips and compare speech with caption extraction |
| G02 | All motion recipes | Every intermediate video frame | Fast cursor actions or short motion states may be missed | Inspect frame-by-frame around any remaining operational uncertainty |
| G03 | FIN-02 | Intended versus actual flicker cadence | Displayed code leaves `floorTime` unused | Run the original/corrected comparison in Book IX |
| G04 | FIN-01/02/03 | Complete global finishing-layer construction | Scope and layer type affect reproduction | Rebuild a minimal stack and verify its coverage; obtain project if exact fidelity is required |
| G05 | FIN-03 | Final committed grain intensity | UI is scrubbed during the short shot | Inspect final source project or choose and label a new value by delivery-size testing |
| G06 | SHP-01 | Exact path creation, stroke settings, and reveal keys | Operator alone does not define the mark | Build a clean path first and record chosen End animation as original |
| G07 | FIN-04 | Full stroke width and all Roughen Edges settings | 7.10 only makes sense relative to the example line | Measure working stroke and test the captioned half-width relationship |
| G08 | FIN-05/06 | Rendered seed cadence and complete duplicate expression state | `time*4` is not proof of four visible drawings per second | Inspect evaluated seed and rendered frame changes; reopen duplicate’s expression |
| G09 | FIN-06 | Definitive final broad-pass Amount | Values change during dragging | Obtain final project or select an explicitly original amount by contour QA |
| G10 | EDT-01 | Exact final gain, onset offsets, EQ, fades, loudness, music integration | The shown tooltip is not a mix specification | Audition with narration and document the actual mix decisions |
| G11 | MAP-01/02 | Gradient creation method, exact colors/radius, complete input sampling | Wrong field or polarity changes focus | Build a test ramp, assign it, and verify bright-center/clear-center behavior |
| G12 | MAP-01/02/SHP-01 | Map source construction and regional geometry | Styling cannot establish geographic accuracy | Obtain verified geometry/assets; separately document map preparation |
| G13 | TRN-01 | Complete alignment and exact cut/keyframe coordinates | Parenting alone does not register visual artwork | Test adjacent cut frames and local transforms in a minimal two-object setup |
| G14 | TRN-02; EDT-02 | Operational montage rigs and chart/diagram construction | Result examples do not supply algorithms | Select a separate validated method when a full rig or data graphic is needed |
| G15 | IMG-01; FIN-07; TYP-01 | Full article, paper, and highlighter implementation | T07 promotes a longer lesson that is not attached | Rebuild a simple labeled adaptation or inspect the missing full lesson if later supplied |
| G16 | TYP-02 | Full selector keyframes and Advanced settings | Several mechanisms could produce the observed sweep | Test End versus Offset on a short phrase; record actual chosen method |
| G17 | TYP-03/04 | Random-letter and odometer rig internals | Cannot reproduce exact preset from name and endpoint | Obtain preset/project or build and validate an explicitly original substitute |
| G18 | WRK-01 | Selected saved properties and application-time behavior | Preset may carry unwanted state | Apply to fresh text of varied lengths and inspect changed properties |
| G19 | IMG-02/03 | Masking details, Clone Stamp brush settings, final hidden-region repair | Asset quality constrains camera range | Inspect isolated planes and maximum camera exposure; refine locally |
| G20 | IMG-04 | Import mode, manual camera/plane setup, compensation, exact axis/keyframes | Caption “dolly” is insufficient to infer a pure-Z move | Build a minimal manual rig; document depth order, apparent-size compensation, and actual movement |
| G21 | WRK-02; FIN-08 | Current utility/plugin availability, compatibility, license, installation | Source product mentions are not current dependency checks | Verify exact product through its authoritative documentation before production |
| G22 | FIN-08 | Aberration strength and channel settings | Too strong a substitute can harm readability | Compare a restrained test against target appearance at delivery size |
| G23 | MOT-01 | Exact property, handle values, duration, influence percentages | Graph appearance is not a numerical preset | Recreate qualitative curve and test actual displacement/settling |
| G24 | FIN-09 | Full-stack temporal behavior and export settings | Effect sampling differs from project/delivery cadence | Render short movement through the complete stack and inspect frame changes |
| G25 | All finished deliverables | Source-taught export codec, bit depth, color management, delivery specs | No complete render pipeline is taught | Obtain project-specific delivery requirements and validate a real export |
| G26 | All proposed completions | Execution in the target applications | Reproducible reasoning is not an application test | Open the actual software and perform the relevant exercise before calling a rig validated |

## 9. Final extraction audit

**Inventory:** ten supplied videos cataloged, each mapped to technique IDs and local timestamps. Thirty-one uniquely identified recipes contain the full A–L structure. The catalog, source registry, index, chronological ledger, and gaps register support retrieval without access to the original clips.

**Primary and secondary lessons:** the audit includes the principal topic of every clip and smaller operational details: Option-click entry; effect Position versus layer Position; half-stroke-width roughness; Random Seed versus Evolution; duplicate-pass tuning; gain adjustments; blur inversion and fitting; parent direction; preset saving; Clone Stamp; optional Depth settings; 12.0 sampling; and the qualitative easing curve.

**Corrections preserved:** live parameter drags are not converted into false final presets. The original exposure expression is retained alongside a labeled proposed repair. T08’s menu hover is not mistaken for its expanded Fill Color property. T04’s hovered dropdown item is not mistaken for the instructed blur source. The distinction between 24 Hz expression sampling and 12 fps picture sampling is retained.

**Reproducibility boundary:** complete source-backed mechanisms are taught in chronological order; missing setup is named; practical completions are separate. Showcase-only text styles and overview-only transitions remain explicitly incomplete as original-source constructions. No unseen preset, full external lesson, chart method, or export workflow is claimed as inspected.

**Knowledge transfer:** three original multi-source scene plans and nine progressive exercises demonstrate how to select, combine, diagnose, and evaluate the techniques. Their durations and additional implementation choices are clearly original.

**Validation status:** the document was checked for recipe structure, unique IDs, cross-reference consistency, tutorial coverage, and source-value distinctions. It is a visual/caption-derived instructional reference. Audible source review, frame-exhaustive review, and application/render validation remain open and are not represented as completed work.

## 10. Final operating principle

Preserve the sequence **claim → evidence → visual relationship → motion → support → finish**. Retrieve an effect because it solves a specific production problem. Preserve the creator’s actual instructions, mark what is missing, and test adaptations before treating them as reliable tools.