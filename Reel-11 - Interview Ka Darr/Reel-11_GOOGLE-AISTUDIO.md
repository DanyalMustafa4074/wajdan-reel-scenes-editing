# Reel #11 "Interview Ka Darr" — Google AI Studio (Gemini TTS)

Warm, reassuring read (talks a nervous student down). English-led / Roman-Urdu mix. **Gemini TTS speaks
the text verbatim** — so the script is **clean speech only** (no tags, no direction words). Emotion/pacing
lives in the STYLE INSTRUCTION, which the model follows but does NOT read aloud.

---

## 1) SETUP
- **Where:** AI Studio → "Generate speech" (or API `gemini-2.5-flash-preview-tts`).
- **Voice:** **Puck** (warm, upbeat young male) — or **Leda** for a softer, gentler feel (good for this
  reassuring reel). Reads Roman-Urdu phonetically; spot-check §5.
- **Temperature:** ~1.0.
- **How:** put the STYLE INSTRUCTION (§2) as the directive, the SCRIPT (§3) as the content. Single box?
  Use `Say the following <style>: <script>` — it speaks only the script.

---

## 2) STYLE INSTRUCTION (paste as the directive — NOT read aloud)

Read this like a calm, warm, reassuring mentor gently talking a nervous student down off a ledge — kind
and steady, never hype, never a hard sell. Keep a comfortable, unhurried pace, but not slow enough to
drag. Go a little lower and softer, slightly worried, on the inner-fear lines ("what if I freeze? what
if I get rejected?"). Leave a tiny beat of silence before "Number one" and "Number two," then deliver
both reveals steady, confident and reassuring. Warm up into a gentle, hopeful smile for the ending line
"the fear handles itself," and keep the CTAs friendly and inviting.

---

## 3) SCRIPT — MAIN BODY (clean speech, SC-01 → SC-10)

Kuch countries mein student visa ke liye interview hota hi nahi. Most Pakistani students ko yeh pata hi nahi.

Aur yehi darr… interview ka darr… bohot capable students ko peeche kheench leta hai.

Admission ready, funds ready… phir bhi woh apply nahi karte. Sirf ek sawaal dimaag mein chalta rehta
hai… what if I freeze? What if I get rejected?

So let me tell you two things.

Number one… New Zealand mein na koi university interview hota hai, na embassy interview. None at all.
Sirf aap ki file aur documents baat karte hain.

Number two… UK mein agar interview hota bhi hai, you get more than one chance. Ek attempt theek na
jaye, darwaza band nahi hota.

So the thing scaring you the most? Ya to woh exist hi nahi karti… ya utni scary nahi jitni aap ne apne
dimaag mein bana rakhi hai.

Darr aksar sirf information ki kami se aata hai. Jab poori picture saamne aa jaye… the fear handles itself.

---

## 4) ENDINGS (generate each separately, same voice)

**Ending 1 — organic reel** (style: warm, caring, inviting):
Save this and send it to a friend who's holding back just because of interview fear. Comment "INFO",
aur main khud personally aap ko batata hoon ke aap ke case mein interview hoga bhi ya nahi.

**Ending 2 — paid ad** (style: warm, confident):
Neechay button dabayein aur consultant ke saath ek free call book karein.

---

## 5) PRONUNCIATION — respell if the voice trips
- darr → "dur" (rhymes with "her")  ·  peeche → "pee-chay"  ·  sawaal → "sa-waal"
- dimaag → "di-maagh"  ·  darwaza → "dur-waa-za"  ·  poori → "poo-ree"
- Keep "INFO" crisp as one word for the CTA.

## 6) MAX-CONTROL OPTION
Generate in 2 passes and stitch: Pass A (soft/low instruction) for the fear lines (SC-02–04); Pass B
(steady/reassuring) for the reveals + ending. Guarantees the emotional dip-then-lift.

### NOTE
Do NOT paste any §2 style words into the spoken text — Gemini would read them. §3/§4 are already clean.
