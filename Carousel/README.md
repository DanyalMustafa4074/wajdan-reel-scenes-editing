# StudyPrime Carousel — Slide Template (reusable)

Slide 1 theme proof: `slide1-theme-proof.png`. Full theme spec: `../StudyPrime-Carousel-THEME.md`.

## Locked theme
Gold `#C9A24B` + Navy `#162447` on warm cream. B&W character cutout with gold sticker-stroke,
faded-navy tiled watermark word, ONE gold pop-word, hand-drawn doodle accents, SP chip + handle.
Format 1080×1350 (4:5). Headline font Anton; UI font Poppins.

## Rebuild a slide
Character cutouts are made by removing the background from a source photo (Freepik) — the
transparent PNG goes in `assets/`. Then:

```
# from the scratchpad working copy of this folder:
python3 build/inject.py                 # embeds fonts + cutout into build/final.html
NODE_PATH=/opt/node22/lib/node_modules \
  node build/shot.js build/out.png      # renders 1080x1350 @2x via Chromium
```

To make a new slide: swap the cutout path in `inject.py` and edit the headline / pop-word /
tiled watermark word in `build/template.html`. Everything else stays constant for series consistency.

## Source characters
Consistent "Ahsan Khan" character images live in Google Drive folder `studyprimecarousalimages`
(13 outfits/scenes). `assets/ahsan-cutout-11.png` = background-removed version of the full-body
glasses-adjust pose used on slide 1.
