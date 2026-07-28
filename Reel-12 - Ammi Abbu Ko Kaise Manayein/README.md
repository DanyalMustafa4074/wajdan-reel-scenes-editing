# Reel #12 — "Ammi Abbu Ko Kaise Manayein" (StudyPrime)

StudyPrime organic reel + paid-ad variant. English-led / Urdu mix, warm and respectful
parent-convincing reel. Doodle-on-kraft style (same brand system as Reel-06/07/09). Built with
`/REEL-PIPELINE-PLAYBOOK.md`.

- **Angle:** Give students the 4 truths their parents actually want to hear — (1) globally recognised
  degree, (2) work while studying + post-study work visa, (3) safety (NZ 4th most peaceful),
  (4) clear PR pathway — so parents' fear turns into trust.
- **Target audience:** students whose parents won't agree to sending them abroad.
- **CTA keyword:** "PARENTS" (per Ending 1 — confirm before publishing).
- **Length:** ~60–70s, 9:16. **Two endings** (reel: save + comment "PARENTS" · ad: book a call).

## Package
| File | What |
|------|------|
| `Reel-12_VOICEOVER.txt` | Voiceover-only script + delivery cues + two endings. |
| `Reel-12_CHARACTERS.md` | Character list — all reused (Student 1, Parents, Good Consultant, Kiwi). |
| `Reel-12_SCENE-PROMPTS.md` | 10 concept scene prompts, per-scene model + references. |
| `Reel-12_EDIT-SHEET.md` | Frame, timeline, captions, two endings, pacing, export. |
| `README.md` | This file. |

## Folders
- `Characters/` — reused sheets: Student 1, Parents, Good Consultant, Kiwi.
- `Scenes/` — generated `SC-01.png … SC-10.png`.

## Characters (all REUSE — Parents redesigned middle-aged)
- Student 1 — SC-01, 02, 04, 06, 11, 13
- Parents — SC-01, 02, 04, 10, 11, 13, 14  (their first featured reel; redesigned ~50, proper dress)
- Good Consultant — SC-14 (ad ending)
- Kiwi mascot — SC-07 (safety), SC-08 (PR)

**14 scenes** (expanded from 10): added SC-03 (relatable montage), SC-09 (recap card), SC-11 (proud
send-off payoff), SC-12 (SAVE THIS REEL / Ending 1a).

## Generation
Object scenes → `recraft-v4-1`. Character/kiwi scenes → `imagen-nano-banana-2` with the reused sheet(s)
as image references. Style-approval gate: one test image first, then the rest.

## Status
- [x] Voiceover
- [x] Characters
- [x] Scene prompts
- [x] Edit sheet
- [x] README
- [x] Test image approved (SC-01)
- [x] Parents redesigned — middle-aged (~50), Abbu in shalwar kameez + waistcoat, Ammi in eastern kurta + dupatta (`Characters/Parents.png` updated)
- [x] All 14 scenes generated + saved to `Scenes/`
- [x] Committed + pushed to `claude/reel-12-parents`

Art complete: SC-01…SC-14 (16:9 PNGs). Object scenes (SC-03, 05, 09, 12) = recraft-v4-1;
character/kiwi scenes = imagen-nano-banana-2 with Student 1 / Parents / Good Consultant / Kiwi
references. Two endings: reel = SC-12→SC-13, ad = SC-14 (shared body SC-01→SC-11). Next: assemble
both cuts per the edit sheet.

## Open questions
1. CTA keyword: "PARENTS" (used) — keep, or change?
2. Safety stat: script says NZ "4th most peaceful" — confirm the current Global Peace Index ranking.
3. Keep Student 1 as the student, or switch to Student 2?
