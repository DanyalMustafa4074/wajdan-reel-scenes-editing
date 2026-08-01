# StudyPrime — Instagram Carousel THEME (Working Spec)

Goal: value-first carousels for students (~5 slides). Slide 1 = face-led hook in a bold,
scroll-stopping style inspired by the "WB" orange-black photographic template, softened with a
hand-drawn **doodle** layer, rendered in the **Study Prime** palette.

---

## PART A — Reference teardown ("WB" bold photographic style)

The formula every WB slide repeats:
1. **Real photographed person**, cut out, slightly desaturated, on a flat/near-flat background.
2. **One giant condensed uppercase headline** (Anton / Druk / Bebas-Compressed feel) — owns ~40–50%
   of the frame. Ultra high-contrast.
3. **Two-tone headline logic** — most of the word is white/black, the ONE emotional word is the
   brand accent color (WHY, BRAND, TIMINGS, INTERN, HIRING).
4. **Small hand-scribble / doodle accents** — underlines, arrows, hearts, question marks, sketch
   marks. This is the personality layer.
5. **Persistent small logo chip**, top-center, every slide.
6. **9:16 vertical**; person in lower two-thirds, headline top / over the shoulders.

Why it works: instant thumb-stop (contrast), ONE idea per slide (single accent word), relatable
human emotion (curiosity), repeatable template (only photo + word change → recognizable series),
doodles add warmth/meme-native feel, casual Hinglish voice reads insider/community.

---

## PART B — Asset inventory (folder: studyprimecarousalimages, 13 imgs, char = Ahsan Khan)

Character is CONSISTENT across all. Cutouts are palette-agnostic → reusable under any template.

| # | Outfit / scene | Mood | Best use |
|---|---|---|---|
| 01 | Green cardigan + cream turtleneck, hand-to-head at laptop, grey bg (cutout, white stroke) | Thoughtful/stressed | Problem slide |
| 02 | Grey cable-knit, at desk laptop, colorful (orange/green) office (cutout) | Working, approachable | Context / intro |
| 03 | Brown houndstooth blazer + turtleneck, mug, HP laptop, looking down | Focused | Mid-slide |
| 04 | Grey 3-piece herringbone suit, finger-to-temple thinking, orange+green wall | Sharp/considering | Hook or problem |
| 05 | Maroon sweater + check shirt, candid at office PC | Real/BTS | Filler / relatable |
| 06 | GROUP of 5 diverse pros (Ahsan among them), dark boardroom (cutout) | Team/authority | "We/Team" slide |
| 07 | Charcoal wool coat, assembling puzzle pieces (arrows), turf bg, "?" doodle | Problem-solving | Concept / steps |
| 08 | Charcoal herringbone blazer, MacBook, peach-coral gradient bg (clean) | Premium, calm | **Clean hero portrait** |
| 09 | ILLUSTRATED doodle-render — design desk, orange chair, dual monitors, "AHSAN KHAN – Principal Designer" nameplate | Creative | Illustrated-style slide |
| 10 | **B&W cutout + ORANGE outline stroke, giant faded tiled "WHY" bg** | Bold hook | **SLIDE-1 TEMPLATE (half body)** |
| 11 | **Full-body, navy coat + brown polo, adjusting glasses, faded "WHY" tiled bg, orange stroke** | Bold hook | **SLIDE-1 TEMPLATE (full body)** |
| 12 | Green fair-isle sweater, hands-on-chest sincere gesture, orange accent-wall office | Sincere/trust | CTA / values |
| 13 | Navy double-breasted suit, hands clasped at desk, dark moody premium bg | CEO authority | Authority / closing |

Ready-made hook templates: **#10 and #11** already ARE the WB structure (cutout + accent stroke +
tiled headline). Cleanest standalone portrait: **#08**. Team shot: **#06**. Authority: **#13**.

NOTE: generated accent = ORANGE. Study Prime brand accent (from reel) = GOLD `#C9A24B` + NAVY
`#162447`. Palette decision pending (see Part D).

---

## PART C — Slide-1 theme spec (proposed)

- **Canvas:** 1080 × 1350 (4:5) or 1080×1920 (9:16) — carousel standard is 4:5.
- **Background:** off-white/cream with a **giant faded tiled hook-word** watermark (like #10/#11).
- **Subject:** Ahsan cutout (B&W or full-color), lower-right or center, with a **thin accent
  outline stroke** (gold instead of orange).
- **Headline:** condensed uppercase, 2–4 words, ONE word in accent. e.g.
  "WHY 90% STUDENTS **FAIL** THIS" / "THE SCHOLARSHIP **SACH**".
- **Doodle layer:** hand-drawn underline/arrow/circle on the accent word; small sketch marks.
- **Logo:** SP monogram chip, top-center or top-left, persistent.
- **Handle:** studyprime.pk, small, bottom.
- **Font:** Anton / Druk-condensed for headline; Poppins ExtraBold for sub/body.

---

## PART D — LOCKED DECISIONS

1. **Accent palette:** ✅ **GOLD + NAVY** — BG warm cream · tiled hook-word faded NAVY · cutout
   stroke GOLD `#C9A24B` · headline navy `#162447` with ONE gold pop-word · doodles navy/gold.
2. **Slide-1 subject:** ✅ **B&W Ahsan cutout + gold outline stroke** (#10/#11 treatment).
3. **Format:** 4:5 (1080×1350) — IG carousel standard [default unless you say 9:16].

## BUILD PLAN — Slide 1
- Subject cutout via Freepik remove-background on a clean portrait, desaturated to B&W in template.
- Template built in HTML/CSS (pixel-perfect fonts/gold word/doodles), rendered to PNG via Chromium.
- Reusable: future slides swap only the subject image + hook word.

## LOCKED STYLE RULES (from client feedback)
1. **Hook = few, HUGE words.** 3–6 words total, WB-style hierarchy: tiny connector words +
   1–2 giant anchor words. Make the main words big and bold (Anton, up to ~230px). One word in
   gold (the "pop"/title word). No small multi-line paragraphs.
2. **No brand furniture on the slide.** Remove SP logo, handle, and swipe affordance — keep it
   clean like the WB samples (headline + subject + faded watermark + doodle only).
3. **Outfit rule for Ahsan — every NEW carousel:** dress him as a decent professional in either a
   **summer-vibe** or **winter old-money** style. (Slide-1 uses the navy herringbone overcoat =
   winter old-money.) Generate fresh outfit/BG per carousel; keep the same face.
4. Keep: cream ground, faded-navy tiled watermark word, B&W cutout + gold stroke, doodle accents.
</content>
</invoke>
