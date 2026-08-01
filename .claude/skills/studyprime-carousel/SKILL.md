---
name: studyprime-carousel
description: >-
  Create branded Instagram/LinkedIn carousels for Study Prime (studyprime.pk), the study-abroad
  advisory brand. Use this whenever the user wants a Study Prime carousel, slide post, or multi-slide
  graphic — e.g. "make a Study Prime carousel about X", "build slides for studyprime", "new carousel
  idea + slides", "turn this hook into a carousel", or when they hand over a hook image and want the
  rest of the slides. Handles the full pipeline: idea + 3 hook options, then generation of the inner
  slides (Slides 2–5) in the locked navy/gold house style, a preview strip, a per-carousel zip, and a
  ready-to-post LinkedIn caption. Trigger even if they don't say the word "carousel" but clearly want
  Study Prime slide content or graphics.
---

# Study Prime Carousel Builder

Produces value-first study-abroad carousels for **Study Prime** (`studyprime.pk`) in a locked house
style: bold condensed **navy + gold-3D** headlines, a bubbly readable body font, cream background,
and a Save/Share + **1-1 consultation (link in bio)** call-to-action. The character face used on hook
slides is **Ahsan** (a saved **@ahsan** character in the user's Freepik account).

Carousels are usually **5 slides**: Slide 1 = a face-led **hook** (the user builds this in Freepik/
their editor), Slides 2–4 = value, Slide 5 = CTA. This skill generates Slides 2–5 and packages
everything; it does not need to recreate the hook.

## Pipeline (full)

1. **Idea + hooks.** If the user gives a topic, propose the concept in Study Prime's honest,
   plan-first, anti-hype voice, then give **exactly 3 hook options** (2–4 words, one gold pop-word
   marked). Keep hooks in the reusable idea space — see `references/content-formula.md` for the idea
   bank, hook formula, and the brand voice. The user picks one and builds Slide 1 themselves.
2. **Content.** Write Slides 2–5 (≤5 slides total). Every factual claim must be **true** — this brand
   was built warning students against hype and scams, so never invent statistics or fees. Prefer
   qualitative wording ("most students") over fake percentages, and verify any volatile fact (fees,
   visa rules, PR pathways) against an official source before it goes on a slide.
3. **Build.** Encode the content as a **spec JSON** (schema in `references/spec-format.md`) and run the
   generator. It renders Slides 2–5 as PNGs, then zips them with the hook + LinkedIn caption.
4. **Deliver.** Send the preview + the zip. Offer edits.

If the user only wants the build step (they already have a hook image + approved content), skip to
step 3.

## Building the slides

Write the carousel to a spec file, then run the wrapper:

```bash
bash scripts/build.sh path/to/spec.json path/to/workdir
```

This writes `workdir/slides/slide2.png … slide5.png` and `workdir/StudyPrime-Carousel-<slug>.zip`
(zip contains `slide1.png`–`slide5.png` + `LinkedIn-Post.txt`). It uses Python + Playwright/Chromium,
which are preinstalled in the Claude-Code-web sandbox; the script auto-locates Chromium under
`/opt/pw-browsers`. Fonts (Anton, Bricolage Grotesque) are bundled in `assets/fonts` and embedded
automatically — no network needed.

`slide1.png` (the hook) comes from the user. Put its path in the spec's `hook_image`. If they haven't
supplied it yet, build without it (the zip just starts at slide2) and add it later.

To show the user a **preview strip** (hook + all slides in a row) before/after building, render a
simple HTML row of the PNGs with Playwright — see `references/spec-format.md` for the montage snippet.

## The house style (do not drift)

Full spec in `references/theme.md`. The essentials:

- **Canvas** 1080×1440 (3:4), rendered @2x.
- **Colors** navy `#17264D`, gold `#C9A233`, cream `#F4ECD8`.
- **Headline** condensed display (Anton), two lines: navy top word + **gold word with a navy 3D
  extrude**. This mirrors the user's hook slides and is the thread that ties the set together.
- **Body** Bricolage Grotesque (bundled) — distinctive but readable; never a plain default sans.
- **Highlights** wrap key phrases in `**…**` → they render as gold.
- **CTA slide** three rows (🔖 save / ↗ share / 💬 consult) + a navy "1-1 CONSULTATION — LINK IN BIO"
  bar. On LinkedIn the link goes in the **first comment**, not the body (reach penalty).

## Reference files

- `references/theme.md` — exact colors, dimensions, type rules, layout anatomy.
- `references/content-formula.md` — brand voice, hook formula, slide structures, LinkedIn caption
  template, the accuracy rule, and the standing idea bank.
- `references/spec-format.md` — the spec JSON schema, one full worked example, and the preview-strip
  snippet.
- `assets/example-spec.json` — a complete, runnable spec you can copy and adapt.
