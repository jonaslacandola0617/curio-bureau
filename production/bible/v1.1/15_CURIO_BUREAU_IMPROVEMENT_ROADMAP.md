# 15 — CURIO BUREAU REPAIR ROADMAP (evidence-backed, ordered)
## Priority/effort matrix
| Rank | Priority | Work | Film evidence | Expected outcome | Effort | Verification |
|---|---|---|---|---|---|---|
| 1 | P0 | Permanent voice-trimmed timeline and intra/inter clip gap linter | EP004 7 gaps 3.04–5.37s; EP005 2.86–5.12s | zero accidental 3–5s narration voids | S (1–2 days) | isolated WAV + encoded full listen |
| 2 | P0 | Center captions with word-alignment and UI mask renderer | low EP001/004/005 captions, user-reported app occlusion; estimated EP005–007 timing | readable mobile captions throughout | M (2–4 days) | verified SRT, final MP4 & WebM overlay screenshots |
| 3 | P0 | Native 4K dual-codec + effective raster resolution gate | EP007 photo-grade 941×1672 raster in 2160×3840 MP4; previous upscaling concerns | actual sharp video and clear claims | M (2–3 days) | 100% pixel QA + asset logs |
| 4 | P1 | 3 strong hook variants + first-frame mute pass | EP001 pilot & EP004 static open; EP005 consequence strongest | stronger visual comprehension and first-question clarity | M (2–5 days/first use) | blinded phone test + eventual retention |
| 5 | P1 | Premium storyboard visual complexity gate | EP007 illustrated intro vs flat sections | no cross-scene quality cliff | M–L (4–8 days setup) | 5 reviewed difficult-style frames |
| 6 | P1 | Fourteen-family shot grammar / fingerprint ledger | EP005 waves/city, EP006 street, EP007 image repeated | distinct shots without channel incoherence | M (2–4 days setup) | rolling six-shot audit |
| 7 | P1 | Real archival/evidence pipeline | EP005 authentic photos add depth; others limited use | credible documentary texture | M–L (rights dependent) | image-specific licenses & footage notes |
| 8 | P1 | Sound director review with source recordings & score motifs | 004/005 low-score/pacing history; 007 procedural Foley | improved perceived cinematic quality | M–L (per film) | blind headphone+phone listen, cue audit |
| 9 | P1 | More designed environment models/multi-part reusable primitives | EP006 cars/facades; EP007 jacks | more premium 2D/2.5D production | L (asset design) | subject silhouette / technical detail check |
|10 | P2 | Source hash+font identity implementation | code references to Playfair/Manrope not enough | reliable family/weights across builds | S–M | full font diagnostic output |
|11 | P2 | End card/folio kit | 001/004/006 varying label & empty outro | brand consistent but less intrusive | S | contact strip of end cards |
|12 | P2 | Actual post-release retention dashboard | private analytics not yet connected | evidence-based first-3s improvement | M | matched retention baselines after 30d |

## Retrospective: highest-return film repairs
- **001 Samoa:** keep premise/calendar idea but replace empty first 2s with animated missing Dec 30, lift captions into center, rebuild first 5s. Do not remake geography explanation until original named final master is found.
- **004 Lake Peigneur:** P0 remaster timing from final voice, reposition captions, reillustrate flooded mine and physically identifiable rig/boats; archive/rights investigation. Would be a substantial edit because original captions are baked.
- **005 Boston:** P0 fix VO padding and captions, P1 change wave/city angle and strain diagram; strengthen archived aftermath earlier. Re-render required due to baked text.
- **006 Sweden:** existing voice pacing better; focus on different period road angles, original multi-part vehicles, meaningful side-cross choreography, font certainty and forced-align captions.
- **007 Chicago:** biggest P1 art continuity repair: replace low-detail houses, people, screw supports, sewer with the same authored richness as opening; segment image into physical planes and use genuine purposeful motion rather than reusing image at 55–71s; align words, verify source art resolution and rights.
- **002/003:** no valid repair decision without original final video; prioritize locating, not remaking from guesses.

## Delivery / milestones
**Week 1:** lock Bible v1 and font files; implement silence report, SRT forced alignment, center-caption checker, 4K source resolution QA; recover Episodes 002–003. **Week 2:** build three benchmark scenes and 14-family shot fingerprint system; do blind phone design test. **Week 3:** pilot a single 30–40s *premium* animation sample (Chicago jacks or Sweden traffic) with full VO/evidence/audio/fonts/caption verification and adjust tooling. **Future episodes:** full creative signoff on five styles and low-res complete animatic before final 4K encoding. These are estimates, not background work commitments.

## Explicit success metrics / limitations
Technically: no >1.20s speech gaps, zero occluded captions, 2 correctly probed native-4K encodes, exact font lock, all assets rights tagged. Artistically: five-frame min-quality test passes, six-shot near-duplicate audit passes, meaningful motion visible in each main beat, musical score passes human playback check. Audience: improved 1s/3s retention and completion **only if measured from first-party analytics**, not inferred from competitor public view counts.