# Reel #13 — "Danyal vs You" (StudyPrime)

StudyPrime comparison / call-out reel. English-led / Urdu mix. Doodle-on-kraft style. Built with
`/REEL-PIPELINE-PLAYBOOK.md`.

- **Angle:** Danyal made avoidable mistakes (paid full fee upfront → visa reject → money stuck; bet on
  one university; panicked). YOU have the information: pay-after-visa in NZ, apply to multiple unis
  (UK + NZ), stay calm. "Don't be Danyal — be the one who had a plan."
- **Target audience:** students about to apply, at risk of the same avoidable mistakes.
- **CTA keyword:** "PLAN" (per Ending 1 — confirm before publishing).
- **Length:** ~60–75s, 9:16. **Two endings** (reel: save + comment "PLAN" · ad: book a call).

## Package
| File | What |
|------|------|
| `Reel-13_VOICEOVER.txt` | Voiceover-only script + delivery cues + two endings. |
| `Reel-13_CHARACTERS.md` | Character list — Danyal = Student 1, You = Student 2 (+ Good Consultant, Kiwi). |
| `Reel-13_SCENE-PROMPTS.md` | 14 concept scene prompts, per-scene model + references. |
| `Reel-13_EDIT-SHEET.md` | Frame, timeline, captions, two endings, pacing, export. |
| `Reel-13_GOOGLE-AISTUDIO.md` | Ready-to-paste Gemini TTS VO (clean speech + style instruction). |
| `README.md` | This file. |

## Folders
- `Characters/` — reused: Student 1 (Danyal), Student 2 (You), Good Consultant, Kiwi.
- `Scenes/` — generated `SC-01.png … SC-14.png`.

## Characters (all REUSE — no new sheets)
- **Danyal = Student 1** — SC-01,02,03,04,06,08,10 (the warning; sympathetic, not mocked)
- **You = Student 2** — SC-01,05,07,09,10,11,13 (the smart one)
- Good Consultant — SC-14 (ad ending)
- Kiwi mascot — SC-05, SC-07 (NZ advantage beats)

## Generation
Object scene (SC-12) → `recraft-v4-1`. Character/kiwi scenes → `imagen-nano-banana-2` with reused
sheet(s) as image references. Style-approval gate: one test image first, then the rest.

## Status
- [x] Voiceover
- [x] Characters
- [x] Scene prompts
- [x] Edit sheet
- [x] Google AI Studio VO
- [x] README
- [x] Test image approved (SC-01)
- [x] All 14 scenes generated + saved to `Scenes/`
- [x] Committed + pushed to `claude/reel-13-danyal-vs-you`

Art complete: SC-01…SC-14 (16:9 PNGs). Object scene (SC-12) = recraft-v4-1; character/kiwi scenes =
imagen-nano-banana-2 with Student 1 (Danyal) / Student 2 (You) / Good Consultant / Kiwi references.
SC-03/05/10/13 were regenerated to remove stray prompt-text artifacts. Two endings: reel =
SC-12→SC-13, ad = SC-14 (shared body SC-01→SC-11).

## Open questions
1. CTA keyword: "PLAN" (used) — keep?
2. Name "Danyal" kept per client (account-owner name match acknowledged).
