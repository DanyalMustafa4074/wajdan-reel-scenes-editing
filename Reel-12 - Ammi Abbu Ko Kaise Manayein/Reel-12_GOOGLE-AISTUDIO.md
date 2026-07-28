# Reel #12 "Ammi Abbu Ko Kaise Manayein" — Google AI Studio (Gemini TTS)

Fast-paced, energetic, emotionally dynamic. English-led / Roman-Urdu mix.
**Key difference from ElevenLabs:** Gemini TTS speaks the text *exactly as written*. So the script below
is **clean speech only** — no direction words, no tags. All the emotion/pacing lives in the STYLE
INSTRUCTION, which the model follows but does NOT read aloud.

---

## 1) SETUP
- **Where:** AI Studio → "Generate speech" (or the Gemini API `gemini-2.5-flash-preview-tts`).
- **Voice:** **Puck** (upbeat, warm young male) — best fit. For a more excitable read, try **Fenrir**.
  Softer alt: **Leda** (youthful). It reads Roman-Urdu phonetically, so spot-check the words in §5.
- **Temperature:** ~1.0 (default) is fine.
- **How to use the two fields:** paste the STYLE INSTRUCTION (§2) as the directive, then the SCRIPT
  (§3) as the content. If it's a single prompt box, use the pattern: `Say the following <style>: <script>`
  — Gemini speaks only the script, in that style.

---

## 2) STYLE INSTRUCTION  (paste as the directive — NOT read aloud)

Read this like an energetic, confident young mentor talking fast and punchy to a friend, in a warm
English / Urdu mix. Keep the pace quick and lively so it never drags — this is a social-media reel.
Use a big dynamic range: bright, excited and slightly higher-pitched on the tips and reveals; push
the energy on the key words. BUT for the part about "safety," gear-change completely — slow right
down, lower the pitch, and go gentle, warm and reassuring, like calming a worried parent; then lift
back up, hopeful, for the last point. End the whole thing warm and sincere, with a small smile in the
voice — inviting, not salesy. Natural short breaths at the pauses; do not sound robotic or monotone.

---

## 3) SCRIPT — MAIN BODY (clean speech, SC-01 → SC-11)

You're ready to go abroad. The real problem? Ammi Abbu maan nahi rahe.

"Beta… yahin reh kar kuch kar lo." Every convinced student has heard this line.

So let me give you the things your parents actually want to hear. Zabardasti nahi… just the truth.

Number one — the degree is globally recognised. Whatever you study in the UK or New Zealand, it works
everywhere in the world. It doesn't go to waste.

Number two — you can work while you're there. Part-time during your studies, and a full post-study
work visa after. Bacha khud ko support karta hai — the child supports himself.

Number three… a parent's biggest fear. Safety. New Zealand is the fourth most peaceful country in the
world. Yeh baat unko sab se zyada sukoon degi.

And number four — after the degree, there's a clear PR pathway too. This isn't just studying… it's a
whole future.

Parents say no because they're scared. Jab yeh chaar cheezein samajh aa jayein… the fear turns into
trust.

---

## 4) ENDINGS (generate each separately, same voice)

**Ending 1 — organic reel** (style: warm, friendly, inviting, direct-to-camera):
Save this reel, and next time the topic comes up, show it to your Ammi Abbu — yeh baatein unke liye
hain. Comment "PARENTS", and I'll personally send you the full list you can show your parents.

**Ending 2 — paid ad** (style: confident, warm, a touch more upbeat):
Neechay button dabayein aur consultant ke saath ek free call book karein — with your parents too.

---

## 5) PRONUNCIATION — respell if the voice trips (Gemini reads Roman-Urdu phonetically)
- sukoon → "su-koon"  ·  bharosa → "bha-ro-sa"  ·  Ammi → "um-mee"  ·  Abbu → "ub-boo"
- bacha → "buch-cha"  ·  zabardasti → "za-bar-das-tee"  ·  rukhsat → "rukh-sat"
- Keep **PR** as "P R" (two letters) so it says "pee-arr," not "per."
Tip: generate once, listen, then only respell the few words that sound off.

## 6) IF YOU WANT MAXIMUM CONTROL OVER THE "SAFETY" GEAR-CHANGE
Generate the reel in 2 passes and stitch in the editor:
1. Pass A (energetic instruction): everything EXCEPT the "Number three… safety…" paragraph.
2. Pass B (soft instruction: "slow, low, gentle, warm, reassuring — calming a worried parent"): just
   the "Number three… sukoon degi." paragraph.
This guarantees the emotional contrast that keeps viewers watching.

---

### NOTE
Do NOT paste any of the §2 style words into the spoken text — Gemini would read them. The script in
§3/§4 is already clean; the emotion comes only from the instruction.
