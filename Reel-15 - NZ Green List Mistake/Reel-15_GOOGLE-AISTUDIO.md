# Reel #15 "Ek Ghalati Jo NZ Applicants Karte Hain" — Google AI Studio (Gemini TTS)

Calm, warm, honest-expert / warning read (StudyPrime). **English-led with light Roman-Urdu.** **Gemini
TTS speaks the text verbatim** — the script is **clean speech only** (no tags, no direction words).
Emotion/pacing lives in the STYLE INSTRUCTION, which the model follows but does NOT read aloud.

---

## 1) SETUP
- **Where:** AI Studio → "Generate speech" (or API `gemini-2.5-flash-preview-tts`).
- **Voice:** **Charon** (calm, informative, authoritative — fits the honest-expert warning). Warmer
  alt: **Puck**. Deeper alt: **Orus**.
- **Temperature:** ~1.0.
- **Language:** English-led with light Urdu phrases — Gemini handles the code-switch. Respell any Urdu
  word phonetically if it drifts (see §5).
- **How:** put the STYLE INSTRUCTION (§2) as the directive, the SCRIPT (§3) as the content. Single box?
  Use `Say the following <style>: <script>` — it speaks only the script.

---

## 2) STYLE INSTRUCTION (paste as the directive — NOT read aloud)

Read this like a calm, honest expert giving a warning — someone who genuinely wants you to get this
right, not someone selling. Plain-spoken, warm, confident, never hyped. English-led with a light natural
Roman-Urdu mix; smooth code-switching, clear pronunciation. Open slow and serious on "Most students
applying to New Zealand make one mistake — and they don't realise it until it's too late." — this is the
hook, let it land. Say "Yehi galati hai." flat and direct-to-camera, then a small beat. Slow down
slightly on "That permanent right to live and work there is called PR." — make it a helpful teaching
moment, not technical. Take a tiny silence just before "It's called the Green List." Say "Agar aap ki
field is list mein hai…" clearly — that's the value. Slow down on "Don't choose your field, then hope."
— that's the lesson. Close confident and knowing on "That's the difference between studying abroad… and
actually settling there for good." Keep the ending inviting and warm.

---

## 3) SCRIPT — MAIN BODY (clean speech, SC-01 → SC-14)

Most students applying to New Zealand make one mistake — and they don't realise it until it's too late.

They pick a field first. Naam dekh kar, trend dekh kar. And they choose the university around that.
Sounds normal, right? Yehi galati hai.

Because in New Zealand, your field decides one big thing — whether you can settle there permanently
later, or not. That permanent right to live and work there is called PR — Permanent Residency.

And there's a list that decides who gets there faster. It's called the Green List. These are the
occupations that lead to a clear PR route — a straight path to settling in New Zealand.

Agar aap ki field is list mein hai — the road after your degree is simple.

Pick a field that's not on it, and you can still get the degree… but that easy path to settling there
may not be open.

So the fix is simple. Don't choose your field, then hope. Pehle dekho rasta kahan jaata hai — then
choose the field that takes you there.

That's the difference between studying abroad… and actually settling there for good.

---

## 4) ENDINGS (generate each separately, same voice)

**Ending 1 — reel** (style: warm, genuinely helpful; land on "on it"):
Save this before you pick your field — this mistake is hard to fix later. Comment "GREENLIST" — and I'll
personally check if your field is on it.

**Ending 2 — ad** (style: warm, low-friction invite):
Neechay button dabayein aur consultant ke saath ek free call book karein.

---

## 5) PRONUNCIATION / DICTION
- "PR" → say as two letters "P R".  ·  "Green List" → natural English.
- "GREENLIST" → keep crisp as one word for the CTA.
- "Yehi galati hai" (this is the mistake), "rasta" (the road/route), "field is list mein hai" — keep the
  Urdu crisp; respell phonetically if Gemini drifts (e.g., "galati" → "gha-la-ti").

## 6) MAX-CONTROL OPTION
Generate in 2–3 passes and stitch: (A) warning + reframe (SC-01→03), (B) PR + Green List teaching
(SC-04→10), (C) the fix + moral + ending. Guarantees the warning stays serious and "Green List" gets its
beat of silence.

### NOTE
Do NOT paste any §2 style words into the spoken text — Gemini would read them. §3/§4 are already clean.
Record BOTH endings separately (organic reel vs paid ad).
