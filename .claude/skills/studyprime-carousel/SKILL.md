---
name: studyprime-carousel
description: >-
  Create branded Instagram/LinkedIn carousels for Study Prime (studyprime.pk), the study-abroad
  advisory brand. Use this whenever the user wants a Study Prime carousel, slide post, or multi-slide
  graphic — e.g. "make a Study Prime carousel about X", "build slides for studyprime", "new carousel
  idea + slides", "turn this hook into a carousel". Runs the full interactive pipeline: content ideas →
  3 hook options → a generated Slide 1 in TWO variations (clean-cream + real-scene) via Freepik →
  inner slides in the locked navy/gold house style → a ready-to-post zip (separate Instagram PNGs, a
  LinkedIn PDF, and Instagram + LinkedIn captions). Trigger even if they don't say the word "carousel"
  but clearly want Study Prime slide content or graphics.
---

# Study Prime Carousel Builder

Produces value-first study-abroad carousels for **Study Prime** (`studyprime.pk`) in a locked house
style: bold condensed **navy + gold-3D** headlines, a bubbly readable body font, cream background, and
a Save/Share + **free 1-1 consultation** call-to-action. The recurring face is **Ahsan** (a saved
character in the user's Freepik library).

Carousels are **5 slides**: Slide 1 = a face-led **hook**, Slides 2–4 = value, Slide 5 = CTA.

## This is an interactive pipeline — stop at every checkpoint

Run these steps **in order** and **wait for the user** at each ⏸️. Do not run ahead.

1. **Ideas.** Propose a short list of carousel concepts in Study Prime's honest, plan-first, anti-hype
   voice (draw from the idea bank in `references/content-formula.md`). ⏸️ **The user picks one idea.**

2. **3 hooks.** For the chosen idea, give **exactly 3 hook options**. Hooks are **3–6 words**,
   understandable at a glance (a reader gets the gist instantly), split into a navy line + one gold
   pop-word. See the hook formula in `references/content-formula.md` — good vs. bad examples matter.
   ⏸️ **The user picks a hook** (or asks for more).

3. **Slide 1, both variations.** Generate the hook image via Freepik and build **both** house
   variations — **A "clean cream"** (Ahsan cut out on cream) and **B "real scene"** (Ahsan in a
   believable office/campus scenario, full-bleed). Same headline, doodles, colours in both. Full
   recipe in `references/slide1-recipe.md`. Show **both** side by side. ⏸️ **The user picks A or B**,
   asks for tweaks, or asks for more scene ideas — regenerate until one Slide 1 is locked.

4. **Inner content.** Write the copy for Slides 2–5 (problem/reframe → value → CTA) and show it as
   plain text first. Every factual claim must be **true** — this brand warns students against hype and
   scams, so never invent statistics or fees (see the accuracy rule in `content-formula.md`). ⏸️
   **The user approves the content** (or edits).

5. **Build the full carousel.** Encode everything as a **spec JSON** (schema in
   `references/spec-format.md`), run the builder, and show a preview strip of all 5 slides. ⏸️ **The
   user confirms all slides look good** (or requests fixes — re-render).

6. **Deliver the zip.** Produce the ready-to-post `StudyPrime-Carousel-<slug>.zip`:
   - `Instagram/slide1.png … slide5.png` — separate images to post as an IG carousel.
   - `StudyPrime-Carousel-<slug>.pdf` — all slides in one PDF to upload to LinkedIn as a document.
   - `Captions.txt` — the Instagram caption **and** the LinkedIn caption.
   Send the zip. Offer edits.

If the user hands over an approved hook + content and just wants the build, jump to step 5.

## Building Slide 1 (step 3)

See `references/slide1-recipe.md` for the Freepik generation details. In short: pull the **Ahsan**
character from the Freepik library, generate a warm portrait (→ `images_remove_background` for the
cutout, variation A) and a warm in-scenario scene (variation B), write a small **hook spec**, then:

```bash
python3 scripts/build_hook.py hook.json workdir/hook
NODE_PATH=/opt/node22/lib/node_modules CHROME=<chrome> node scripts/render.js workdir/hook
```

That writes `workdir/hook/slide1_A.png` and `slide1_B.png`. Show both. Copy the chosen one to the
spec's `hook_image`.

## Building the carousel (steps 5–6)

Write the carousel to a spec file, then run the wrapper:

```bash
bash scripts/build.sh path/to/spec.json path/to/workdir
```

This renders Slides 2–5, builds the LinkedIn PDF, and writes the zip (Instagram PNGs + PDF +
`Captions.txt`). It uses Python + Playwright/Chromium, preinstalled in the Claude-Code-web sandbox;
the script auto-locates Chromium under `/opt/pw-browsers`. Fonts (Anton, Bricolage Grotesque) are
bundled in `assets/fonts` and embedded automatically — no network needed.

To show a **preview strip** (all slides in a row) before delivering, render a simple HTML row of the
PNGs with Playwright — see `references/spec-format.md` for the montage snippet.

## The house style (do not drift)

Full spec in `references/theme.md`. The essentials:

- **Canvas** 1080×1440 (3:4), rendered @2x.
- **Colors** navy `#17264D`, gold `#C9A233`, cream `#F4ECD8`.
- **Headline** condensed display (Anton), two lines: navy top word + **gold word with a navy 3D
  extrude**. This thread ties every slide together, hook included.
- **Body** Bricolage Grotesque (bundled) — distinctive but readable; never a plain default sans.
- **Highlights** wrap key phrases in `**…**` → they render as gold.
- **Slide 1** = warm Ahsan + navy/gold headline + themed doodles; **no handle/watermark**.
- **CTA slide** three rows (🔖 save / ↗ share / 💬 consult) + a navy "1-1 CONSULTATION" bar.

## Reference files

- `references/slide1-recipe.md` — how Slide 1 is generated (Freepik Ahsan + both variations, hook spec).
- `references/theme.md` — exact colors, dimensions, type rules, layout anatomy.
- `references/content-formula.md` — brand voice, hook formula, slide structures, the two caption
  templates (IG + LinkedIn), the accuracy rule, and the standing idea bank.
- `references/spec-format.md` — the spec JSON schema, a full worked example, the preview-strip snippet.
- `assets/hook-templates/` — the locked Slide-1 HTML (cream + office variations).
- `assets/example-spec.json` — a complete, runnable spec you can copy and adapt.
