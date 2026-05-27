#!/usr/bin/env python3
"""Copy invite-friend profile photos → assets/friends/ and update manifest."""
import json
import shutil
from pathlib import Path

SRC = Path('profile photo placeholders')
DST = Path('assets/friends')
MANIFEST = Path('assets/friend-manifest.json')

# Invite friends row — image 19–25 from profile photo placeholders/
FRIEND_SOURCES = [
    'image 19.png',
    'image 20.png',
    'image 21.png',
    'image 22.png',
    'image 23.png',
    'image 24.png',
    'image 25.png',
]


def main():
    if not SRC.is_dir():
        print(f'Missing folder: {SRC}')
        return

    DST.mkdir(parents=True, exist_ok=True)
    manifest = []

    for i, name in enumerate(FRIEND_SOURCES, start=1):
        src = SRC / name
        if not src.is_file():
            print(f'Missing: {src}')
            continue
        dest = DST / f'friend-{i}.png'
        shutil.copy2(src, dest)
        entry = f'assets/friends/friend-{i}.png'
        manifest.append(entry)
        print(f'  {entry}  ← {name}')

    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST.write_text(json.dumps(manifest, indent=2) + '\n')
    print(f'Wrote {len(manifest)} photo(s) → {MANIFEST}')


if __name__ == '__main__':
    main()
