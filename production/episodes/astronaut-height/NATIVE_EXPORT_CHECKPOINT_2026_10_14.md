# Astronaut Height R2 — owner approval and native export checkpoint
Date: 14 October 2026

Owner approved the complete R2 moving picture and sound and authorized 4K rendering and posting copy. No social publishing is authorized by this task.

Image-led direction and earlier approved instructions adopted on main in production Bible v1.4.3, commit 9669a27241ca205bf1ed4903798f858101486f70. See production/approved-benchmarks/IMAGE_LED_OWNER_DIRECTION.md.

## Native export status
All 1,172 frames captured at native 2160×3840, 30 fps, 39.066667 seconds. Exact contiguous frame order checked. Native Canvas/CDP pixel equality at 0, 17.8 and 38.8 seconds passed; rebuilt infrastructure pixel parity at 17.8 seconds passed.
Master encoding started, then execution environment disconnected and reported environment_offline. No completed 4K MP4/WebM has been verified or made available. Do not claim completion or invent a download link.

Approved source commit: 0dc0cfb6d943938ce33f527c5990dd92ae0e4bbf.
scenes.js SHA256: 83e5b59342625c19dedc33fb6ff44481545ac7b6e12784bd3bc596140b296d9c.
episode.json SHA256: 30496b07d31e7297d9f4a5170a86a5eed28a07f9eb512f52a4bbb3d133fc712d.
Approved mix SHA256: 12f6260a92de4e7999cf42e93e465c5287444f449cea7bc7f965f6a9e45c5f68.
Keep the approved mix, voice, music, Foley, captions, picture and exact endcard unchanged. Resolution-only rebuild; no asset generation or upscale.

## Recovery
First check existing outputs, Native_QA.json and process state under /tmp/astronaut_native. Do not start a second writer to a file that is still being encoded.
Retain existing lossless native intermediates and verified SEGMENT_QA.json/segments.txt. finish.py closes partial-prefix containers by video stream remux, then encodes native master MP4, WebM and upload MP4 directly from native lossless frames plus exact approved mix.
Paths may disappear if the disconnected environment is reset. If missing, restore approved private source from Astronaut_Height_Private_Project.zip version 1 and source from the approved commit, then reconstruct native export. No private source assets or restricted stock should be uploaded into public Git.

Verified frame ranges (start/count/file):
0/142/segment_00.mkv
142/54/remainder_00.mkv
196/143/segment_01.mkv
339/53/remainder_01.mkv
392/107/range_0392.mkv
499/80/bounded_0499.mkv
579/9/bounded_0579.mkv
588/77/range_0588.mkv
665/80/bounded_0665.mkv
745/39/bounded_0745.mkv
784/46/range_0784.mkv
830/80/bounded_0830.mkv
910/70/bounded_0910.mkv
980/39/range_0980.mkv
1019/80/bounded_1019.mkv
1099/73/bounded_1099.mkv

Final approval checks still required for encoded native files: dimensions/frame count/fps/duration/codecs, full decode, audio loudness and true peak, hashes, and successful durable file save. Approved review mix measured -14.46 LUFS / -2.66 dBTP; preserve this owner-approved level rather than silently remastering.

## Durable approved source
Astronaut_Height_Review_1080p.mp4 Library ID libfile_8a715ee22434819187a4df29af98b440 version 1.
Astronaut_Height_Private_Project.zip Library ID libfile_4fbec0871f408191939021530f706242 version 1.
Public source and credits remain in the episode branch.
