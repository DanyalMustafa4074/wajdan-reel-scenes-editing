# Reel #12 "The 3am Lead" — Google AI Studio (Gemini TTS)

Calm, warm, plain-spoken read (Wajdan). English. **Gemini TTS speaks the text verbatim** — the script
is **clean speech only** (no tags, no direction words). Emotion/pacing lives in the STYLE INSTRUCTION,
which the model follows but does NOT read aloud.

---

## 1) SETUP
- **Where:** AI Studio → "Generate speech" (or API `gemini-2.5-flash-preview-tts`).
- **Voice:** **Charon** (calm, grounded, believable) — best for this "told as a story" tone. Warmer
  alt: **Puck**. Deeper alt: **Orus**.
- **Temperature:** ~1.0.
- **How:** put the STYLE INSTRUCTION (§2) as the directive, the SCRIPT (§3) as the content. Single box?
  Use `Say the following <style>: <script>` — it speaks only the script.

---

## 2) STYLE INSTRUCTION (paste as the directive — NOT read aloud)

Read this like a calm, warm person telling a true story to one other person — plain-spoken, unhurried,
never hyped, never sarcastic, never a hard sell. Keep an even pace around 150 words per minute. Deliver
"Nothing. For two days." completely flat and final, with a beat of silence either side — the flatter it
is, the harder it lands. Tell the first weekend gently and evenly; you are describing a real person, not
scoring a point, so keep all sarcasm out. On "Now here's the same weekend — with a system behind the
form," lean in slightly and warm up — this is the turn. Tell the second weekend at the SAME calm pace as
the first, so the two feel like one story told twice; do NOT speed up or brighten, that instinct turns it
into an ad. Land "Your staff didn't work the weekend." then a full stop, then "The system did." as its
own quiet, certain beat — that's the line the whole thing exists for. Keep the closing invitation
confident and warm, not pushy, and land on the word "leaking."

---

## 3) SCRIPT — MAIN BODY (clean speech, SC-01 → SC-15)

Someone filled out your form at three in the morning on a Saturday.

Nobody does that out of curiosity.

That's a person who couldn't sleep because of the problem you fix.

Best lead you'll get all week.

Watch what happens to them.

Nothing. For two days.

Saturday morning, they check their email. Nothing from you.

By Sunday, the worry has passed. It's just a normal weekend again.

Monday, quarter past nine, your staff finally calls.

They don't answer. They're at work.

Your team writes them off as a bad lead.

Now here's the same weekend — with a system behind the form.

Three a.m. They hit submit. Eighteen seconds later, a text arrives. Confirmed. Someone's got this.

Two minutes later, a short video lands — while they're still awake, still worried.

They book their own slot. At three in the morning. Because the calendar was open.

Then the reminders go out. A day before. Two hours before. Fifteen minutes before.

Monday, they show up ready to talk. And nobody on your team lifted a finger.

Your staff didn't work the weekend.

The system did.

That's the difference between a client and a lead marked bad on Monday.

And it doesn't cost more ad spend. It's what happens in the eighteen seconds after the form.

---

## 4) CTA (generate separately, same voice — confident, warm, land on "leaking")

Click the link in my bio and book a free one-to-one strategy call — and I'll show you exactly where
yours is leaking.

---

## 5) PRONUNCIATION / DICTION
- "3am" → "three a.m."; "9:15" → "quarter past nine"; "18 seconds" → "eighteen seconds". (Already
  written out in §3 — keep it that way so the model doesn't misread digits.)
- Keep "The system did." slow and separated from the line before it.

## 6) MAX-CONTROL OPTION
Generate in 3 passes and stitch: (A) hook + the gap + weekend one, (B) pivot + weekend two, (C) the
truth + CTA. Guarantees both weekends stay the same calm pace and "The system did." gets its beat.

### NOTE
Do NOT paste any §2 style words into the spoken text — Gemini would read them. §3/§4 are already clean.
