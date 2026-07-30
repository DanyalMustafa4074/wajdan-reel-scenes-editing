# Reel #10 — "The Order Smart Businesses Build In" (Wajdan)

Wajdan Services reel + paid-ad variant. Framework/system explainer. Doodle-on-cream, Wajdan orange.
Built with `/REEL-PIPELINE-PLAYBOOK.md`.

- **Angle:** The gap isn't ads — it's what's built *after* the click. The smart ones build six pieces
  in this order: 01 Funnel → 02 Landing Page → 03 VSL → 04 CRM + Automation → 05 Meta Ads (last!) →
  06 Conversion Tracking. Miss one and you're funding a leak.
- **Target audience:** business owners running ads with a leaky/empty calendar.
- **CTA keyword:** "GUIDE" (CTA A — confirm before publishing).
- **Length:** ~85–90s, 9:16. **Two CTA variations** (A: comment "GUIDE" · B: book a call, 15 left).

## Package
| File | What |
|------|------|
| `Reel-10_VOICEOVER.txt` | Voiceover-only script + delivery cues + two CTAs. |
| `Reel-10_CHARACTERS.md` | Character list — Owner + SYS robot (Wajdan brand + prop kit). |
| `Reel-10_SCENE-PROMPTS.md` | 16 concept scene prompts, per-scene model + refs, strict text discipline. |
| `Reel-10_EDIT-SHEET.md` | Frame, timeline, the six-layer stacking motion, two CTAs, pacing, export. |
| `Reel-10_GOOGLE-AISTUDIO.md` | Ready-to-paste Gemini TTS VO (clean speech + style instruction). |
| `README.md` | This file. |

## Folders
- `Characters/` — reused: Owner, SYS-robot.
- `Scenes/` — generated `SC-01.png … SC-16.png`.

## Characters (REUSE from Reel-08 — no new sheets)
- The Owner ("You") — SC-02 (bad calendar), SC-14 (funding a leak)
- SYS robot — SC-05 (the order), SC-09 (CRM/automation), SC-15 (GUIDE)
- (Michael, Team not used — this is the system-order explainer, not the You-vs-Michael story.)

## Generation
Object/diagram scenes → `recraft-v4-1`. Owner/SYS scenes → `imagen-nano-banana-2` with the reused sheet
as an image reference (single figure, NOT an expression sheet). Strict text discipline (only intended
words on art). Style-approval gate: one test image first, then the rest.

## Status
- [x] Voiceover
- [x] Characters
- [x] Scene prompts
- [x] Edit sheet
- [x] Google AI Studio VO
- [x] README
- [ ] Test image approved
- [ ] All 16 scenes generated + saved
- [ ] Committed + pushed to `claude/reel-10-wajdan-order`

## Open questions
1. CTA keyword: "GUIDE" (used) — keep?
2. CTA B "15 free strategy calls" — confirm the real current number before publishing.
