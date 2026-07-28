# Reel #13 "Danyal vs You" — Google AI Studio (Gemini TTS)

Punchy comparison read. English-led / Roman-Urdu mix. **Gemini TTS speaks the text verbatim** — so the
script is **clean speech only** (no tags, no direction words). Emotion/pacing lives in the STYLE
INSTRUCTION, which the model follows but does NOT read aloud.

---

## 1) SETUP
- **Where:** AI Studio → "Generate speech" (or API `gemini-2.5-flash-preview-tts`).
- **Voice:** **Puck** (upbeat, warm young male) — best fit. More assertive alt: **Orus** / **Fenrir**.
  Reads Roman-Urdu phonetically; spot-check §5.
- **Temperature:** ~1.0.
- **How:** put the STYLE INSTRUCTION (§2) as the directive, the SCRIPT (§3) as the content. Single box?
  Use `Say the following <style>: <script>` — it speaks only the script.

---

## 2) STYLE INSTRUCTION (paste as the directive — NOT read aloud)

Read this like a sharp, confident young mentor doing a fast comparison call-out to a friend, warm
English/Urdu mix, quick and punchy so it never drags. Two clear modes that alternate:
(1) When talking about "Danyal," go plain, factual and a touch lower/cooler — a serious warning, NEVER
mocking or laughing at him. (2) Every time you say "You?", snap to direct-to-camera: firmer, warmer,
brighter, a small lift in pitch — this is the punch; leave a tiny beat of silence right before it.
Keep the energy high on the contrasts. For the final line, "Don't be Danyal. Be the one who had a
plan," slow down and land it — confident and final. End the CTAs warm and inviting, not salesy.

---

## 3) SCRIPT — MAIN BODY (clean speech, SC-01 → SC-11)

Aap aur Danyal mein sirf ek farak hai… aur woh farak aaj decide hoga.

But watch what Danyal did.

Danyal paid his full tuition upfront. Lakhs of rupees, before anything was confirmed. Phir visa reject
ho gaya… and his money got stuck for months.

You? You don't have to do that. In New Zealand, in many cases, tuition is paid after your visa is
approved. Pehle visa haath mein… phir paisa. Aap ka paisa safe rehta hai.

Danyal ne ek hi university pe sab kuch laga diya. Woh reject hui, toh puri planning khatam.

You? You apply smart… multiple universities, UK aur New Zealand dono mein. Agar ek se offer na aaye,
doosri se aa jata hai. Ek darwaza band, doosra khula.

Danyal panicked and rushed. Aap ke paas information hai… that's the difference between him and you.

Danyal aaj bhi wahin hai. Aur aap? Aap ke paas abhi bhi choice hai… woh choice jo Danyal ke paas nahi thi.

Don't be Danyal. Be the one who had a plan.

---

## 4) ENDINGS (generate each separately, same voice)

**Ending 1 — organic reel** (style: warm, confident, inviting):
Save this so you don't make Danyal's mistakes. Comment "PLAN", and I'll personally show you the smarter
route, step by step.

**Ending 2 — paid ad** (style: confident, warm, a touch urgent):
Neechay button dabayein aur consultant ke saath ek free call book karein — before you become Danyal.

---

## 5) PRONUNCIATION — respell if the voice trips
- farak → "fu-ruk"  ·  paisa → "pie-sa"  ·  darwaza → "dur-wa-za"  ·  khula → "khu-la"
- Danyal → "DAN-yaal"  ·  aaj → "aaj"  ·  lakhs → "lakhs" (or say "hundreds of thousands of rupees" if it trips)
- Keep "PLAN" crisp as one word for the CTA.

## 6) MAX-CONTROL OPTION (for the "You?" punch)
If you want the flips razor-sharp, generate in 2 passes and interleave in the editor:
- Pass A (plain/cool instruction): the "Danyal" sentences.
- Pass B (bright/direct instruction): the "You?" sentences + the final "have a plan" line.

### NOTE
Do NOT paste any §2 style words into the spoken text — Gemini would read them. §3/§4 are already clean.
