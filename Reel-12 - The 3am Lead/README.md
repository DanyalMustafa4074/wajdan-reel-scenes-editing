# Reel #12 — "The 3am Lead" (Wajdan)

Wajdan Services reel. Narrative / lead-response explainer — the same weekend told twice. Doodle-on-cream,
Wajdan orange. **Vertical 9:16 (Instagram-native).** Built with the auto-character-reels pipeline.

> Note: this is the **Wajdan** Reel #12 (branch `claude/wajdan-reel-12-3am-lead`). It is separate from
> the StudyPrime Reel-12 "Ammi Abbu Ko Kaise Manayein" on its own branch.

- **Angle:** a 3am form-fill is your best, most-motivated lead. Without a system it dies by Monday
  ("bad lead"); with a system (instant text → video → self-booking → reminders) the same person shows
  up ready — and nobody worked the weekend. The gap isn't ad spend; it's the 18 seconds after the form.
- **Target audience:** business owners whose leads go cold before anyone replies.
- **CTA:** book a free 1-1 strategy call (LINK IN BIO). **Single CTA** — no organic/ad split this reel.
- **Length:** ~80s, **9:16 vertical**.

## What's different this reel
- **Vertical 9:16** scenes (native, full-bleed) instead of 16:9 floated on a plate.
- **New character:** **Sara**, the lead/customer — a fresh recurring face carrying both timelines.
- **Timestamps are editor overlays** (same corner/font both timelines), not AI-drawn — the repetition
  and the hard reset at the pivot are the whole visual argument.

## Package
| File | What |
|------|------|
| `Reel-12_VOICEOVER.txt` | Voiceover script + delivery cues + structure map + on-screen timestamps + CTA. |
| `Reel-12_CHARACTERS.md` | Character list — Sara (new) + SYS (Wajdan brand + prop kit). |
| `Reel-12_SCENE-PROMPTS.md` | 16 vertical 9:16 scene prompts, per-scene model + refs, strict text discipline. |
| `Reel-12_EDIT-SHEET.md` | Vertical frame, timeline + timestamps, the reset move, pacing, export. |
| `Reel-12_GOOGLE-AISTUDIO.md` | Ready-to-paste Gemini TTS VO (clean speech + style instruction). |
| `README.md` | This file. |

## Folders
- `Characters/` — new: Lead-Sara · reused: SYS-robot.
- `Scenes/` — generated `SC-01.png … SC-16.png` (9:16).

## Characters
- Sara (the lead) — SC-01, 02, 04, 05 (weekend one) · SC-09, 10, 13 (weekend two)
- SYS (the system) — SC-08 (pivot), SC-12 (reminders), SC-14 (the system did), SC-16 (CTA)
- Staff/team — objects only (ringing phone, empty chair).

## Generation
Object scenes → `recraft-v4-1`. Sara/SYS scenes → `imagen-nano-banana-2` with the sheet as an image
reference (single figure, NOT an expression sheet). Ratio **9:16**. Strict text discipline; timestamps
via editor. Style-approval gate: new Sara sheet + one test scene first.

## Status
- [x] Voiceover
- [x] Characters
- [x] Scene prompts
- [x] Edit sheet
- [x] Google AI Studio VO
- [x] README
- [x] New character sheet approved (Sara)
- [x] Test image approved (SC-01, full-bleed 9:16)
- [x] All 16 scenes generated + saved (vertical 9:16, all text clean, characters consistent)
- [x] Committed + pushed to `claude/wajdan-reel-12-3am-lead`

## Open questions
1. Vertical 9:16 confirmed as the new default for Instagram reels?
2. Sara's look — keep, or adjust (age / wardrobe)?
