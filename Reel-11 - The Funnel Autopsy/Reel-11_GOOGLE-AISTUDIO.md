# Reel #11 "The Funnel Autopsy" — Google AI Studio (Gemini TTS)

Calm, warm, confident "diagnostician" read (Wajdan). English. **Gemini TTS speaks the text verbatim** —
the script is **clean speech only** (no tags, no direction words). Emotion/pacing lives in the STYLE
INSTRUCTION, which the model follows but does NOT read aloud.

---

## 1) SETUP
- **Where:** AI Studio → "Generate speech" (or API `gemini-2.5-flash-preview-tts`).
- **Voice:** **Charon** (calm, informative, authoritative) — best fit for this diagnostician tone.
  Warmer alt: **Puck**. Deeper alt: **Orus**.
- **Temperature:** ~1.0.
- **How:** put the STYLE INSTRUCTION (§2) as the directive, the SCRIPT (§3) as the content. Single box?
  Use `Say the following <style>: <script>` — it speaks only the script.

---

## 2) STYLE INSTRUCTION (paste as the directive — NOT read aloud)

Read this like a calm, warm expert quietly diagnosing a problem for a business owner — plain-spoken,
confident, genuinely helpful, never hyped, never a hard sell. Keep a steady, even pace, around 150 words
per minute. Deliver the opening "I can tell your consultancy is bleeding leads — without ever talking to
you." with quiet certainty, then a small pause. Handle the three questions like a real diagnosis, not a
recited list: a slight pause before each "One —", "Two —", "Three —", then let the "if the answer is…"
part land conversationally. Slow down and soften on "Not because you forgot. Because nothing was ever
built to catch it." — that's the empathy beat, take the blame off the founder. Go slower and lower on
"You don't need more leads. You need to stop losing the ones you already have." — that's the reframe,
give it weight. Read the three "automatic" fixes with an even rhythm, one clear beat each — do NOT speed
up. Say "Nothing waits on a human to remember." flat and final, then a small pause. Keep the ending
call-to-action warm and inviting.

---

## 3) SCRIPT — MAIN BODY (clean speech, SC-01 → SC-14)

I can tell your consultancy is bleeding leads — without ever talking to you.

I don't need your numbers. I don't need a call.

Three questions, and I'll know exactly where it's leaking.

One — when someone messages you, how long before they hear back?

If the answer is "whenever I see it" — that's leak number one. The lead already messaged three other
consultancies while they waited.

Two — if someone wants to book a call with you right now, is there one link that does it? Or does it
depend on you being free to reply?

If it depends on you — that's leak number two. You're the bottleneck, even when you don't mean to be.

Three — when someone shows interest and then goes quiet, does anything follow up with them automatically?

If nothing's set up for that — that's leak number three. Not because you forgot. Because nothing was ever
built to catch it.

Here's the truth: none of these are marketing problems.

You don't need more leads. You need to stop losing the ones you already have.

Smart consultancies fix all three before they spend a single dollar on ads.

Fast replies — automatic. One clear place to book — automatic. Follow-up when someone goes quiet —
automatic.

Nothing waits on a human to remember.

If even one of those three sounds like you, you're not short on leads. You're short on a system.

---

## 4) CTA (generate each separately, same voice)

**Variation A — reel** (style: warm, genuinely helpful, not a hard sell; land on "leaking"):
Comment "AUDIT" below, and I'll tell you exactly where yours is leaking.

**Variation B — ad** (style: slight pace pickup, real urgency not desperation; land on "before they're gone"):
We've got 15 free strategy calls left this month. Book yours through the link below before they're gone.

---

## 5) PRONUNCIATION / DICTION
- "CRM" → "C R M".  ·  "AUDIT" → keep crisp as one word for the CTA.
- Read the leak numbers as words: "leak number one / two / three".

## 6) MAX-CONTROL OPTION
Generate in 3 passes and stitch for perfect control: (A) hook + the three questions, (B) reframe + the
three automatic fixes, (C) moral + CTA. Guarantees the three questions and the three fixes never speed
up and the reframe/moral get their weight.

### NOTE
Do NOT paste any §2 style words into the spoken text — Gemini would read them. §3/§4 are already clean.
