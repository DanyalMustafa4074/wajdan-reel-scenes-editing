# Reel #06 — "UK Khatam, NZ Zinda" (New Zealand angle)

StudyPrime organic reel + paid-ad variant. Roman-Urdu, host-narrated, hand-drawn doodle-on-kraft
style (same brand system as Reel-07).

- **Angle:** UK/Canada/Australia are tightening → New Zealand is the overlooked best option.
- **Target audience:** students disappointed with UK / Canada / Australia tightening.
- **CTA keyword:** "NZ" (script header also says "NZopen" — CONFIRM which; see notes below).
- **Length:** ~50–60s, vertical 9:16.

## Package (5 parts)
| File | What |
|------|------|
| `Reel-06_VOICEOVER.txt` | Voiceover-only script + delivery cues (record via ElevenLabs). |
| `Reel-06_CHARACTERS.md` | Character list — all reused from `/Character/`, no new sheets. |
| `Reel-06_SCENE-PROMPTS.md` | 19 copy-paste prompts, per-scene model + reference assignments. |
| `Reel-06_EDIT-SHEET.md` | Frame, timeline, captions, two endings, pacing, export. |
| `README.md` | This file. |

## Folders
- `Characters/` — reference character sheets used for this reel (copied from `/Character/`).
- `Scenes/` — generated scene art `SC-01.png … SC-19.png`.

## Characters (all REUSE — no new sheets)
- Student 1 (grey-green tee) — SC-01
- Student 2 (light-blue shirt, glasses) — SC-04, SC-11, SC-17
- Good Consultant (beige cardigan) — SC-19 (ad ending)
- (Parents / Bad Consultant available but not used.)

## Generation method (Freepik connector)
1. **Character sheets first:** upload `/Character/` sheets → get creation identifiers.
2. **Character scenes:** `imagen-nano-banana-2` (Nano Banana Pro) + the character sheet passed as
   an image reference (faces stay consistent).
3. **Object scenes:** `recraft-v4-1` (or `imagen4`), no ref; style anchor only if it drifts.
4. **Style-approval gate:** ONE test image approved first, then the rest.
5. Download each result → save to `Scenes/SC-NN.png` → commit + push.

## Status
- [x] Voiceover
- [x] Characters
- [x] Scene prompts
- [x] Edit sheet
- [x] README
- [ ] Test image approved
- [ ] All scenes generated + saved
- [ ] Committed + pushed to `claude/second-reel-script-assets-8rulhj`

## Open questions for the client
1. **CTA keyword:** "NZ" (used here) or "NZopen" (script header)?
2. **Parents cutaway** near SC-04 — include or skip? (currently skipped)
3. **Reusable Partner/Spouse character** for SC-11 — one-off doodle (current) or mint a new sheet?
