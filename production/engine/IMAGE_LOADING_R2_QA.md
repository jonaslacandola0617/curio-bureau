# Loaded-image Canvas fallback — 14 October 2026

The photographic R2 scene exposed Chromium async `HTMLImageElement.decode()` rejections for valid loaded images. Source images passed local full decode and loaded with nonzero natural dimensions; a synchronous Canvas draw and pixel read succeeded. The build preload now permits this verified loaded-image Canvas path after a decode-hint rejection. Missing/zero-dimension images still reject, and a Canvas draw/read failure still propagates. No rendering, fonts, film, audio, caption or endcard code changes.

R2 evidence: all twelve image slots loaded, 2160×3840 demanding frames rendered, no scene errors; invalid data image rejected; repeated scrub at 1.85s is pixel deterministic. This is a targeted image-loading check, not a claim that every damaged file can be detected by image natural dimensions. Item hashes and local source decode remain separate input checks. Historical source movie bytes remain unchanged.
