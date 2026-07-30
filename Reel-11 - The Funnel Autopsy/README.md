# Reel #11 — "The Funnel Autopsy" (Wajdan)

Wajdan Services reel + paid-ad variant. Diagnostic / three-leaks explainer. Doodle-on-cream, Wajdan orange.
Built with `/REEL-PIPELINE-PLAYBOOK.md`.

- **Angle:** "I can tell your consultancy is bleeding leads without ever talking to you." Three questions
  expose three leaks — (1) slow to reply, (2) no single way to book, (3) goes quiet, nothing follows up.
  None are marketing problems. You're not short on leads; you're short on a system.
- **Target audience:** consultancy/agency owners with leads coming in but slipping away.
- **CTA keyword:** "AUDIT" (CTA A — confirm before publishing).
- **Length:** ~85s, 9:16. **Two CTA variations** (A: comment "AUDIT" · B: book a call, 15 left).

## Package
| File | What |
|------|------|
| `Reel-11_VOICEOVER.txt` | Voiceover-only script + delivery cues + structure map + two CTAs. |
| `Reel-11_CHARACTERS.md` | Character list — Owner + SYS robot (Wajdan brand + prop kit). |
| `Reel-11_SCENE-PROMPTS.md` | 16 concept scene prompts, per-scene model + refs, strict text discipline. |
| `Reel-11_EDIT-SHEET.md` | Frame, timeline, the three-leak rhythm, two CTAs, pacing, export. |
| `Reel-11_GOOGLE-AISTUDIO.md` | Ready-to-paste Gemini TTS VO (clean speech + style instruction). |
| `README.md` | This file. |

## Folders
- `Characters/` — reused: Owner, SYS-robot.
- `Scenes/` — generated `SC-01.png … SC-16.png`.

## Characters (REUSE from Reel-08 / Reel-10 — no new sheets)
- The Owner ("You") — SC-01 (bleeding funnel at his desk), SC-06 (the bottleneck)
- SYS robot — SC-02 (the autopsy), SC-11 (seals the 3 leaks), SC-13 (nothing waits on a human), SC-15 (AUDIT)
- (Michael, Team not used — this is the self-diagnosis autopsy, not the You-vs-Michael story.)

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
- [ ] Committed + pushed to `claude/reel-11-funnel-autopsy`

## Open questions
1. CTA keyword: "AUDIT" (used) — keep?
2. CTA B "15 free strategy calls" — confirm the real current number before publishing.
