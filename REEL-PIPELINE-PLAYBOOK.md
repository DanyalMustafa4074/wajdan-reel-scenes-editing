# Reel Production Playbook — methodology + brand identities

Reusable guide for producing short-form vertical "story reels" as a repeatable pipeline.
Hand this file (or point a new Claude Code chat at this repo) and give a new script — it has
everything needed to build the full package. Reels so far: **#07 StudyPrime** ("Two Students, One
Plan"), **#08 Wajdan** ("You vs. Michael").

---

## THE PIPELINE — 5 deliverables (all text/markdown; Claude does NOT generate images itself)

For a given script, produce a self-contained production package in one folder (`Reel-NN - <title>/`):

1. **`Reel-NN_VOICEOVER.txt`** — narration cleaned, with pause/delivery cues, a section structure map,
   and word count (~90–95s ≈ ~250 words).
2. **`Reel-NN_CHARACTERS.md`** — character bible: per character a design lock + a copy-paste **SHEET
   PROMPT** (plain off-white bg, 3 poses, style-locked). Plus a reusable **prop & icon kit** (recurring
   doodle objects) and a brand-asset note.
3. **`Reel-NN_SCENE-PROMPTS.md`** — one self-contained image-gen prompt per scene (~18–22 scenes). Each
   names which character sheet(s) to **ATTACH**, sets **16:9**, keeps figures in the lower two-thirds
   with caption space up top + side margins, flags object-only scenes, ends with "organic wobbly
   hand-drawn marker look, NOT vector, NOT glossy 3D". Include a scene-index table.
4. **`Reel-NN_EDIT-SHEET.md`** — editor build guide: 1080×1920 canvas, each 16:9 scene floated in a
   band (top ~y=600) on a paper plate, a scene-by-scene timeline mapping each VO line → on-screen
   caption, brand colors, logo + handle placement, a branded CTA card, pacing/music/export.
5. **`README.md` + folders** (`Characters/`, `Scenes/`, `Brand/`) so generated art has a home.

## LOCKED ART STYLE
Hand-drawn doodle: thick black outlines, soft marker/colored-pencil fills, textured off-white paper
background, 16:9. Character consistency comes from **attaching the reference sheet** to every scene
prompt. Brand's primary color = "good/system/accent"; grey = "bad/dead/grind".

## PROVEN STORY STRUCTURE (adapt to the script)
Two-paths contrast arc: **HOOK → "bad path" protagonist (problem/grind) → TEASE ("stay till the end,
here's the way out") → "good path" protagonist (solution/system) → THE TRUTH (side-by-side "same X,
one difference") → MORAL + CTA.** If the script isn't two-paths, follow its own beats but keep
hook / build / turn / truth / CTA sections.

## IMAGE GENERATION (I generate; Claude orchestrates)
- Claude can't generate images. Generate them in a tool that accepts **reference images** for
  character consistency (Google Gemini "Nano Banana" app, Freepik, etc.). **Generate character sheets
  FIRST**, then attach them to each scene.
- **Automated**: Gemini image API needs a billing-enabled key (free tier = zero image quota; ~$1–3 per
  reel; a $300 Google Cloud trial credit covers it). Then a Python script loops prompts + refs → PNGs.
  (Freepik MCP `images_generate`, if connected, is another automated route.)
- **Manual transfer (what we used)**: Claude cannot save images pasted in chat — they aren't reachable
  files. Upload generated images to a **shared Google Drive folder** (shared with the Drive account
  connected to the session). Name each file by its scene number. Claude fetches via Drive tools,
  identifies by filename/content, converts JPG→PNG (Pillow), names them (`Scene 01.png` / `Owner.png`),
  commits, and pushes.

## GIT / WORKFLOW
One folder per reel. Commit in logical batches (docs → character sheets → scenes → finalize commit with
a status checklist). Push to a feature branch. Don't open a PR unless asked. Commit images as real files.

---

## BRAND IDENTITY LIBRARY

### 🎓 StudyPrime — education consultancy (Reel #07 reference)
- **Business:** study-abroad / education consultancy. Helps students go abroad (UK/Europe) the right way.
  A client of Wajdan Services.
- **Audience:** students and their parents (Pakistan) considering studying abroad; warns them about
  unqualified/overselling consultants.
- **Primary colors:** navy **`#162447`** (base text) + gold **`#C9A24B`** (emphasis word).
- **Frame plate:** beige **kraft paper**, full frame (the floating-band scroll-stopper).
- **Caption font:** heavy rounded sans (Poppins ExtraBold / Montserrat Black), thin cream outline + soft shadow.
- **Logo:** small **"SP"** monogram, top-left. **Handle:** `studyprime.pk`, bottom-center.
- **Tone:** calm, warm, plain-spoken, honest, slightly emotional; cautionary storytelling. Let key
  beats ("He's not.", "It was the plan.") breathe with near-silence.
- **Offer / CTA:** "Comment **CHECK**" → free **Student Checklist / Consultant Red-Flag Checklist**;
  or a free strategy call, link in bio.
- **Recurring cast:** Student 1 (grey-green tee), Student 2 (light-blue shirt, glasses), Bad Consultant
  (purple shirt, gold watch, fake grin), Good Consultant (beige cardigan, round glasses), Parents
  (elderly Pakistani couple). Reference sheets live in `/Character/`; scene art in `/Secens/`.
- **Signature arc:** two students, same grades, one has a plan and one doesn't → the difference is "the plan".

### 🟠 Wajdan Services — B2B marketing agency (Reel #08 reference)
- **Business:** Hungarian marketing & client-acquisition agency (Budapest). Builds lead-gen + automated
  client-acquisition systems: **Meta paid ads → CRM → automated follow-up / qualification / call
  booking** (core platform: GoHighLevel).
- **Audience:** business owners who run ads and chase every lead manually and stay stuck.
- **Primary color:** orange **`#E07B00`** (system/good/accent); charcoal `#23262B` base text; cream plate.
- **Logo:** **WAJDAN** wordmark (Arabic *nūn* flourish cradling an orange 4-point star); dark lockup on
  light, light lockup on dark/orange. **Handle:** `@wajdan.co`.
- **Tone:** direct, action-oriented, results-focused. Confident, plain-spoken.
- **Offer / CTA:** **Book a free strategy call** (link in bio) — "turn your ad spend into booked calls,
  not wasted months."
- **Recurring cast (Reel #08):** The Owner ("You", grey tee, tired), Michael (white rolled-sleeve
  shirt, calm), the Team (two people, headsets), SYS (cream helper-robot mascot for the automated
  system). Sheets in `Reel-08 - You vs Michael/Characters/`.
- **Signature arc:** "You" (grinds, chases leads) vs. Michael (built a system) → the difference is "the system".

---

## TO START A NEW REEL
Give: (1) the **new script**, (2) which **brand** (StudyPrime / Wajdan / other — if other, a short
brief with primary color hex, tone, logo, handle), (3) **characters** to reuse or introduce. Then build
all 5 deliverables above, generate character sheets first, then scenes, committing as you go.
