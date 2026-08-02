# Slide 1 (the hook) — generation recipe

Slide 1 is the scroll-stopper: a big navy+gold headline over **Ahsan** (Study Prime's recurring
face). This skill now **generates Slide 1 itself** via Freepik, and always produces **two
variations** so the user picks. Both share the exact same headline, doodles, colours and type — only
the background treatment differs.

- **Variation A — "clean cream".** Ahsan cut out (background removed) and dropped onto a cream
  background with a faint tiled pop-word motif. Loud, graphic, meme-native. Template:
  `assets/hook-templates/cream.html`.
- **Variation B — "real scene".** Ahsan photographed inside a believable Study-Prime scenario
  (consultancy office, campus, airport desk) used full-bleed, with a cream top scrim so the headline
  stays crisp. Warmer, more "real advisor". Template: `assets/hook-templates/office.html`.

## Locked look (do not drift)
- Headline top-anchored, two lines: small **navy** line + huge **gold** line with a navy 3D extrude
  (that stacked `text-shadow` in the templates). Anton, uppercase.
- 2–3 **doodles** in gold/navy line-art (clock, calendar, ?, flag, etc.) themed to the hook, scattered
  around the headline. A big gold **?** is a good default accent.
- Ahsan is **warm and approachable** — soft smile, glasses, knit sweater. Never stern.
- **No @handle / no watermark** on Slide 1 (the cleaner look we locked). The handle lives on the
  inner slides' footer instead.

## Step 1 — get the Ahsan image from Freepik
Ahsan is a **saved character** in the user's Freepik library. Find it with `library_show`
(type `character`) or `library_list`, then generate with the character as reference so the face stays
consistent.

- **For Variation A (cutout):** generate a clean waist-up portrait of Ahsan — warm slight smile,
  glasses, cream/tan cable-knit sweater, simple/blurred background, soft natural light, eye contact.
  Then run `images_remove_background` on the result → that PNG is `cutout_image`.
- **For Variation B (scene):** generate Ahsan **inside the scenario**, portrait 3:4, e.g.
  *"warm, candid photo of the same man sitting at a desk in a modern study-abroad consultancy office,
  soft orange and sage-green tones, laptop and books blurred in the background, natural window light,
  friendly approachable expression, shot on 50mm, shallow depth of field."* Keep him centred and
  roughly waist-up with headroom at the top for the scrim+headline. No text in the image. That PNG is
  `scene_image` (used full, **not** cut out).

Match the scenario to the topic when it helps (airport = visas, campus = universities, desk with
paperwork = applications), but a friendly office shot is the safe default and matches the reference
set. Follow the Freepik tool `instruction` fields; preview with `creations_show`.

## Step 2 — compose both variations
Write a **hook spec JSON** (see below) and run:
```bash
python3 scripts/build_hook.py hook.json workdir/hook
NODE_PATH=/opt/node22/lib/node_modules CHROME=<chrome> node scripts/render.js workdir/hook
```
This writes `slide1_A.png` (if `cutout_image` given) and `slide1_B.png` (if `scene_image` given).
Show **both** to the user. They pick one, ask for tweaks, or ask for more scenes — regenerate the
Freepik image and rebuild until one is locked. Copy the chosen PNG to the carousel's `hook_image`.

### Hook spec fields
| field | meaning |
|---|---|
| `slug` | id for filenames |
| `navy` | top headline line (small navy), UPPERCASE |
| `gold` | bottom headline line (big gold 3D pop), UPPERCASE — this is the pop-word |
| `motif` | faint tiled word behind Variation A (usually the gold word, no punctuation) |
| `cutout_image` | Ahsan PNG with background removed → builds Variation A |
| `scene_image` | full Freepik scene PNG → builds Variation B |
| `doodles` | raw SVG string of the per-topic line-art doodles (shared by A & B) |

### Doodles
Hand-authored inline SVGs, `class="dood"`, absolutely positioned (`left/top/width/height`), gold
stroke `#C9A233` / navy `#17264D`, ~7px strokes, optional small rotation. Keep them clear of the face
and the headline. See `assets/hook-templates/` comments and the worked clock/calendar examples. A
standalone big gold **?** can be added as its own `.dood` SVG or a styled text element.
