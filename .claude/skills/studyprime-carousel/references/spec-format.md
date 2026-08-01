# Spec JSON format

One spec = one carousel. Feed it to `scripts/build.sh <spec.json> <workdir>`.

## Top-level fields
| field | required | meaning |
|---|---|---|
| `slug` | yes | kebab-case id → zip name `StudyPrime-Carousel-<slug>.zip` |
| `kicker` | yes | small gold topic label shown on every inner slide (UPPERCASE) |
| `total_slides` | no | total incl. hook (default = inner slides + 1). Drives the progress dots. |
| `hook_image` | no | path to the user's Slide 1 PNG. If omitted, the zip starts at slide2. |
| `slides` | yes | array of inner slides (usually n = 2,3,4,5) |
| `linkedin` | yes | the ready-to-post LinkedIn caption (string) |

## Slide object
- `n` (int) — slide number (2–5). Sets which progress dot is active and the output filename.
- `head` — `["NAVY WORD(S)", "GOLD POP-WORD"]` (two lines).
- `emoji` (optional) — accent shown top-right, e.g. `"🚩"`.
- `type` — one of `stack` | `list` | `cta`:
  - **stack**: `"lines": [["l","text"], ["q","big quote"], ["sm","muted"], ["chain","A → B → C"]]`
  - **list**: `"items": [["1","text"], ["2","text"]]`, optional `"note":"gold footnote"`
  - **cta**: `"rows": [["🔖","..."],["↗","..."],["💬","..."]]`, `"bio": true` for the consult bar
- In any body text, wrap a phrase in `**...**` to render it gold.

## Minimal worked example
```json
{
  "slug": "wrong-order",
  "kicker": "COURSE › COUNTRY › UNIVERSITY",
  "hook_image": "hooks/wrong-order.png",
  "slides": [
    {"n":2,"head":["MOST DO IT","BACKWARDS"],"type":"stack",
     "lines":[["l","They pick the **country** first, then a uni, then any course that fits."],
              ["l","That's how you get a degree that leads **nowhere.**"]]},
    {"n":3,"head":["THE RIGHT","ORDER"],"type":"list",
     "items":[["1","**COURSE** — matches your goal & strengths"],
              ["2","**COUNTRY** — allows that career + a way to stay"],
              ["3","**UNIVERSITY** — the best one for that course"]]},
    {"n":4,"head":["WHY IT","MATTERS"],"type":"stack",
     "lines":[["l","Right course, wrong country = **no work rights.**"],
              ["l","Right uni, wrong course = **wasted years.**"]]},
    {"n":5,"head":["SAVE","THIS"],"type":"cta","bio":true,
     "rows":[["🔖","Save it before you apply anywhere"],
             ["↗","Share with a student rushing it"],
             ["💬","Want the order **mapped for you?**"]]}
  ],
  "linkedin": "Most students pick their degree in the wrong order...\n\n#studyabroad #studyprime"
}
```
See `assets/example-spec.json` for a full one.

## Preview strip (optional, to show the user before delivering)
Render a horizontal row of the PNGs (hook + slides) and screenshot with Playwright:
```python
# imgs = [hook.png, slide2.png, ... slide5.png]; base64-embed each into a flex row on a navy bg,
# height ~940px per cell, then screenshot full-page. (See scripts/render.js for the Chromium launch.)
```
Keep the montage HTML tiny; embed images as data URIs so it renders offline.
