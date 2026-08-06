# Reel #16 "Statement Mein Yeh Ghalati Mat Karna" — Google AI Studio (Gemini TTS)

Calm, warm, honest-expert how-to read (StudyPrime). **English-led with light Roman-Urdu.** **Gemini TTS
speaks the text verbatim** — the script is **clean speech only** (no tags, no direction words).
Emotion/pacing lives in the STYLE INSTRUCTION, which the model follows but does NOT read aloud.

---

## 1) SETUP
- **Where:** AI Studio → "Generate speech" (or API `gemini-2.5-flash-preview-tts`).
- **Voice:** **Charon** (calm, informative). Warmer alt: **Puck**. Softer alt: **Leda**.
- **Temperature:** ~1.0.
- **Language:** English-led with a light Roman-Urdu mix; smooth code-switching. Respell any Urdu word
  phonetically if it drifts (see §5).
- **How:** put the STYLE INSTRUCTION (§2) as the directive, the SCRIPT (§3) as the content. Single box?
  Use `Say the following <style>: <script>` — it speaks only the script.

---

## 2) STYLE INSTRUCTION (paste as the directive — NOT read aloud)

Read this like a calm, warm expert giving a genuinely helpful how-to — a mentor sharing one useful
trick, not selling anything. Plain-spoken, confident, never hyped. English-led with a light natural
Roman-Urdu mix; smooth code-switching, clear pronunciation. Open slow on "Your grades can be good, your
documents complete… and your application still gets ignored." — that's the hook, let it land. Deliver
"The admissions officer has read that exact line a thousand times." flat and a little knowing, let it
sting slightly. Take a tiny silence just before "Yeh raha the fix." and shift warmer and more helpful
there — that's the turn. Say "The problem you solved. The moment it clicked for you." clearly — that's
the teaching. Close confident and warm on "that's what they remember." Keep the ending inviting.

---

## 3) SCRIPT — MAIN BODY (clean speech, SC-01 → SC-14) — v2 punchy Urdu-led

Grades achi hain. Documents complete hain. Phir bhi application ignore ho jati hai?

Wajah ek chhoti si cheez hai — jo 90% students ko pata hi nahi.

Woh statement, jo aap apne baare mein likhte ho.

New Zealand university poochti hai — why this course, why you? Aur yahin sab log ek jaisi ghalati karte hain.

Sab likhte hain: "I've been passionate about this since childhood." Yeh line admission officer hazaar
baar padh chuka hai. Isse aap ke baare mein kuch pata nahi chalta.

Fix simple hai — mat kaho ke passionate ho. Dikhao, ek real cheez se.

"I love computer science" ke bajaye, likho woh cheez jo aap ne khud banayi. Jo problem solve ki. Woh
lamha jab click hua.

Ek sach-much wali example aap ki poori application ko alag kar deti hai — kyunke woh sirf aap ki kahani
hai. Baaqi sab general baatein likhte reh jate hain.

Rule yaad rakho: general baat bhula do. Ek asli cheez, achi tarah se — yehi wo yaad rakhte hain.

---

## 4) ENDINGS (generate each separately, same voice)

**Ending 1 — reel** (style: warm, genuinely helpful; land on "structure bhej dunga"):
Yeh reel save karo apni statement likhne se pehle. Comment karo "STATEMENT" — main aap ko ek simple
structure bhej dunga.

**Ending 2 — ad** (style: warm, low-friction invite):
Neechay button dabayein aur consultant ke saath ek free call book karein.

---

## 5) PRONUNCIATION / DICTION
- Read the clichéd line "I have been passionate about this field since childhood" in a slightly flat,
  bored monotone so the contrast lands.
- "STATEMENT" → keep crisp as one word for the CTA.
- "Aksar wajah" (usually the reason), "likho" (write), "sach-much wali cheez" (a genuine/real thing) —
  keep the Urdu crisp; respell phonetically if Gemini drifts.

## 6) MAX-CONTROL OPTION
Generate in 2–3 passes and stitch: (A) hook + the problem (SC-01→06), (B) the fix + why it works
(SC-07→12), (C) moral + ending. Guarantees the "1000×" sting and the "Yeh raha the fix" turn land.

### NOTE
Do NOT paste any §2 style words into the spoken text — Gemini would read them. §3/§4 are already clean.
Record BOTH endings separately (organic reel vs paid ad).
