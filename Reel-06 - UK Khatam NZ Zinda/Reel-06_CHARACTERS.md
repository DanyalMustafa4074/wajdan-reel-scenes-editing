# StudyPrime — Reel #06 "UK Khatam, NZ Zinda" — CHARACTERS

All characters are REUSED from the approved library in `/Character/`. **No new character sheets
required.** The doodle style + faces stay consistent by attaching these sheets as image
references on every character scene (model: `imagen-nano-banana-2` / Nano Banana Pro).

## Reused (from /Character/)

| Character | File | Look (locked) | Used in scenes |
|-----------|------|---------------|----------------|
| **Student 1** | `Student 1.png` | grey-green t-shirt, same face/hair | SC-01 |
| **Student 2** | `Student 2.png` | light-blue collared shirt, glasses | SC-04, SC-11, SC-17 |
| **Good Consultant** | `Good COnsultant.png` | beige cardigan, round glasses, friendly | SC-19 (AD ending) |

## Available but NOT used in this reel
- **Bad Consultant** (`Bad Consultant.png`) — not needed; this script has no villain-consultant beat.
- **Parents** (`Parents.png`) — optional. Script doesn't feature parents. Add only if you want a
  "better life for family" cutaway (would slot near SC-04).

## NEW mascot (generated for this reel)
| Character | File | Look | Used in scenes |
|-----------|------|------|----------------|
| **Kiwi guide** | `Characters/Kiwi.png` (to generate) | plump brown kiwi, long beak, big friendly eyes, small green scarf/fern accent | SC-09, SC-10, SC-12, SC-13, SC-17, SC-18 |

Generated once as the first NZ asset, then passed as an image reference on each kiwi scene so the
mascot stays identical. Recurring NZ guide — same role the robot plays in the reference reels.

## One-off (NOT a library character)
- **PhD partner** (SC-11): a generic doodle spouse figure holding a briefcase. Appears once, so it
  does NOT need a consistency sheet. If you want a reusable "Partner/Spouse" character for future
  reels, say so and I'll generate + add ONE new sheet to `/Character/`.

## Reference-passing rule (how faces stay consistent)
1. Character sheets are uploaded to Freepik once → each returns a creation identifier.
2. Character scenes pass the relevant sheet(s) as `references: [{type:"image", identifier:...}]`
   with `mode: "imagen-nano-banana-2"`.
3. Object-only scenes use `recraft-v4-1` (or `imagen4`) with NO character ref; attach a sheet as an
   optional style anchor only if the doodle style drifts.
