# Tutorial effects — implementation and approval boundaries

Owner correction, 12 October 2026: the previous map test omitted a gradient-controlled compound-blur focus system and did not demonstrate the requested full set of film/ink effects. Surface texture alone is insufficient. This document registers those techniques and their actual implementation status without changing Bible v1.4.

## Shared focus field (T04 / MAP-01–02)

The supplied tutorial builds a radial gradient, uses Multiply for tonal emphasis, and uses Compound Blur for selective focus. Preserve **one spatial field for both blur and luminance**. Keep the relevant region sharper/brighter while context becomes progressively softer/darker. Track the focus center through the map camera; do not pin it to the screen while the selected location moves.

`CurioFinishing.FocusPass` is an original Canvas adaptation: it renders a five-level Gaussian blur pyramid, interpolates levels per pixel from an elliptical gradient, and uses that same field for brightness gain. This is a multilevel approximation of spatially varying blur, not an identical implementation of After Effects' proprietary Compound Blur. It is more specific than blurring the whole scene and punching one binary hole in it.

For the approved map choreography, derive the center from Paris's projected screen coordinate at each absolute time. Ramp strength into the selection, keep London/Paris comparison labels and narration captions sharp on separate overlays, and hold the focus through the resolved view. Do not blur all important evidence to imply depth. All supplied example settings are original proposed values, not measured tutorial presets.

```javascript
const focus = new CurioFinishing.FocusPass(mapCanvas.width, mapCanvas.height);
focus.apply(mapCanvas, focusedContext, {
  cx: parisScreenX, cy: parisScreenY, rx: 280 * renderScale,
  ry: 250 * renderScale, feather: 1, maxBlur: 9 * renderScale,
  outsideGain: 0.70, strength: selectionProgress
});
// Compose critical markers and captions AFTER the attention pass.
```

## Film movement, exposure and grain (T01 / FIN-01–03)

Mechanical movement is a restrained frame-level effect, separate from the logical explanatory camera. `filmState` gives deterministic held jitter and exposure values from absolute time; `filmFinish` applies them with overscan and optional optical grain. Its cadence controls actually participate in the seed. The inherited manual identifies an unused frequency variable in the source's displayed exposure expression; this adaptation uses a quantized time seed deliberately.

Do not use optical grain in place of the owner's real paper/plastic textures. Keep amplitudes small, judge at delivery size and protect captions. The previous approval of smooth camera motion is preserved; a new old-film treatment still needs a separate moving review. Jitter and exposure are off by default, not accidentally applied to every analytical shot.

## Annotation edge boil (T02)

`boilPath` adds deterministic normal displacement to an authored polyline at a separately controlled cadence, with optional locked endpoints. Coarse/fine spatial variation makes a drawn contour breathe while its explanatory attachment survives. Apply it to circles, routes and hand-drawn marks; do not move true geographic boundaries, data values, source text or caption UI. This is a Canvas line-contour adaptation, not a copied Roughen Edges/Turbulent Displace rig.

## Ink absorption

`drawInkStroke` draws a restrained blurred low-opacity spread beneath a sharp ink core. Match the bleed to the paper plane and actual pixel resolution. Avoid a detached drop shadow, thick glowing halo or illegible type. Ink bleed is the owner's requested material refinement; exact construction and settings are not established as a fully demonstrated recipe in the supplied short clips.

## Multi-plane parallax (T09)

`parallaxTransform` and `renderParallax` provide perspective/depth-dependent movement for independently prepared image planes. The demonstration requirement remains: separated foreground/midground/background, repaired hidden areas, enough overscan and consistent occlusion. Moving one flattened poster cannot establish that requirement. The map focus test does not need parallax; a photographic moving proof is a later separate exercise.

## Status and tests

Reusable source: [curio-finishing.js](../motion-lab/curio-finishing/curio-finishing.js). Technical report: [verification.json](../motion-lab/curio-finishing/verification.json).

Technical verification checks deterministic time sampling, sharp center/darkened defocused context, progressive blur, held film cadence, annotation endpoint attachment, bleed pixels outside a crisp core, and depth-dependent parallax displacement. These checks do not certify a 100% Vox match or a completed artistic moving review. The old Study 01/02 video files do not gain these effects merely because the library exists; a new rendered integration is required.

Use the actual owner-supplied materials after private import, inspect intermediate motion and encoded output, and obtain separate owner feedback on focus, film finish, ink and parallax before calling them mastered.
