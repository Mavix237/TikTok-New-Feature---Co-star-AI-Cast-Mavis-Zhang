#!/usr/bin/env python3
"""Extract UI assets from Figma full-screen exports (402×874). Run: python3 extract-assets.py"""
from pathlib import Path
from PIL import Image

OUT = Path('assets')
OUT.mkdir(exist_ok=True)
W, H = 402, 874

def crop(src, box, name):
    Image.open(src).crop(box).save(OUT / name, optimize=True)
    print(f'  {name}')

print('Extracting from design screenshots…')
crop('001 camera taking selfie.png', (108, 268, 294, 500), 'selfie-face.png')
crop('002 loading AI self creation.png', (108, 268, 294, 500), 'loading-face.png')
crop('02 AI self revealed.png', (20, 168, 382, 640), 'avatar-hero.png')
crop('02 AI self revealed.png', (50, 190, 352, 600), 'avatar-fog.png')

for i, cx in enumerate([63, 131, 199, 267, 335], 1):
    crop('02 AI self revealed.png', (cx - 33, 645, cx + 33, 711), f'avatar-pose-{i}.png')
    crop('02 AI self revealed.png', (max(0, cx - 140), 155, min(W, cx + 140), 655), f'avatar-hero-{i}.png')

Image.open(OUT / 'avatar-pose-5.png').save(OUT / 'avatar-user-sm.png')

for name, box in [
    ('char-lyrics.png', (24, 352, 200, 532)),
    ('char-mich.png', (202, 352, 378, 532)),
    ('char-timothy.png', (24, 532, 200, 712)),
    ('char-luna.png', (202, 532, 378, 712)),
]:
    crop('03 Co-star options.png', box, name)

crop('04 Moment created.png', (52, 318, 350, 575), 'ski-moment.png')
crop('05 Share to friends.png', (48, 355, 354, 555), 'ski-moment-invite.png')
crop('06 Friend dm page.png', (155, 118, 247, 210), 'dm-friend-avatar.png')
crop('06 Friend dm page.png', (58, 268, 344, 528), 'ski-moment-dm.png')

# Friend avatars: use profile photo placeholders/ + sync-friend-photos.py (not screenshot crops)

print('Done → assets/')
