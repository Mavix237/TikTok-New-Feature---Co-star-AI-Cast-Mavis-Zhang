# Assets folder

## Your Figma exports (recommended)

Drop **transparent PNGs** here with these exact names — the prototype will use them automatically:

| Filename | Screen |
|----------|--------|
| `selfie-face.png` | Selfie confirm (hex photo) |
| `loading-face.png` | Loading queue (optional; falls back to selfie-face) |
| `avatar-hero-1.png` … `avatar-hero-5.png` | Revealed — large hero per pose |
| `avatar-pose-1.png` … `avatar-pose-5.png` | Revealed — thumbnail row |
| `avatar-user-sm.png` | Your AI Self chip (cast / invite) |
| `char-lyrics.png`, `char-mich.png`, `char-timothy.png`, `char-luna.png` | Character pick |
| `ski-moment.png` | Moment + invite card image |
| `ski-moment-dm.png` | DM bubble image (optional) |

## Friend profile photos (invite screen)

Drop full profile PNG/JPG files into **`profile photo placeholders/`** (do not use screenshot crops), then run:

```bash
python3 sync-friend-photos.py
```

This copies every image into `assets/friends/` and updates `assets/friend-manifest.json`. The prototype uses **all** images in that folder.

## DM profile (optional)

- `assets/friends/friend-1.png` is used for the DM header after sync, or add `dm-friend-avatar.png`

## Regenerate crops from screenshots (optional)

```bash
python3 extract-assets.py
```

Crops are approximate; your separate exports will always look better.
