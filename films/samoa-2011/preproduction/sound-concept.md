# Audio bible / cue design

Audio delivers explanatory movement, not decorative noise. Previous film failed because synthesized oscillator music was quieter than expected and SFX gains were below perceptual audibility.

## Target buses & levels
- VOICE: primary; controlled and de-essed, high intelligibility.
- MUSIC: genuine sustained documentary bed, evolving every 8 seconds. Mix under speech at approx -20 to -26 LUFS *short-term* depending on voice; rise 2–4 dB in breath gaps. Never render so quiet as to disappear.
- AMBIENCE: distant analog press/tape room and airy Pacific map bed if asset license permits.
- TRANSITIONS: independent whoosh levels ~ -18 to -12 dBFS peak depending overlap.
- DETAIL SFX: paper taps, clicks, typewriter ~ -22 to -15 dBFS peak.
- IMPACTS: date jump and closing reveal, around -12 to -8 dBFS peak; never clip combined mix.
- MASTER: measured integrated target approx -14 LUFS, true peak <= -1 dBTP; correct using two-pass loudnorm if necessary; listen critically, never assume numbers mean aesthetic success.

## SFX design direction
- Calendar leaf: physical flip / crackle and sweep, not sci-fi zap.
- 30 deleted: weighty paper tear and muted impact.
- Date-line trace: airy, high-frequency gliding sweep.
- Trade grid: distinct metal click/grid registration and dry typographic tick.
- Clock: tactile tick escalating toward midnight; no overpowering cinematic bass blast.
- Law: typewriter clicks + pen underline.
- Wage sheet: paper slap and firm rubber-stamp pulse.
- End card: warm tonal resolution, not an overused trailer whoosh.

## Automation
Every SFX cue defined in one machine-readable cue JSON or JS array with: timestamp, actual Drive filename, trigger, volume, fade, pan, layer. Render mix separate from narration and detect individual signal energy at cue times. Analyze via ffmpeg ebur128/loudnorm; extract 10 critical 2-second intervals for listening.
