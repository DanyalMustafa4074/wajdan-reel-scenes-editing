#!/usr/bin/env python3
"""Package one finished carousel into a ready-to-post zip.

Usage: python pack.py <spec.json> <slides_dir> <out_dir>

Zip contents (StudyPrime-Carousel-<slug>.zip):
  Instagram/slide1.png .. slideN.png   -> post as an IG carousel (separate images)
  StudyPrime-Carousel-<slug>.pdf       -> upload to LinkedIn as a document post
  Captions.txt                         -> Instagram caption + LinkedIn caption

Spec fields used: slug, hook_image (slide1), slides[].n, instagram, linkedin.
Needs Chromium for the PDF (via to_pdf.js) — build.sh exports CHROME/NODE_PATH."""
import json, os, pathlib, subprocess, sys, zipfile

HERE = pathlib.Path(__file__).resolve().parent

def caption_doc(spec):
    ig = (spec.get("instagram") or "").strip()
    li = (spec.get("linkedin") or "").strip()
    return (
        "=========================================\n"
        " INSTAGRAM CAPTION\n"
        "=========================================\n\n"
        f"{ig}\n\n\n"
        "=========================================\n"
        " LINKEDIN CAPTION  (put the link in the FIRST COMMENT, not the post)\n"
        "=========================================\n\n"
        f"{li}\n"
    )

def main():
    spec = json.loads(pathlib.Path(sys.argv[1]).read_text())
    slides_dir = pathlib.Path(sys.argv[2])
    out_dir = pathlib.Path(sys.argv[3]); out_dir.mkdir(parents=True, exist_ok=True)
    slug = spec["slug"]

    # Ordered list of every slide PNG (slide1 = chosen hook, then inner slides).
    ordered = []
    if spec.get("hook_image"):
        ordered.append(("slide1.png", pathlib.Path(spec["hook_image"])))
    for s in spec["slides"]:
        ordered.append((f"slide{s['n']}.png", slides_dir / f"slide{s['n']}.png"))

    # Build the LinkedIn PDF from the ordered PNGs via Chromium.
    pdf_path = out_dir / f"StudyPrime-Carousel-{slug}.pdf"
    subprocess.run(
        ["node", str(HERE / "to_pdf.js"), str(pdf_path), *[str(p) for _, p in ordered]],
        check=True, env={**os.environ},
    )

    zpath = out_dir / f"StudyPrime-Carousel-{slug}.zip"
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        for name, path in ordered:                      # Instagram: separate images
            z.write(path, f"Instagram/{name}")
        z.write(pdf_path, pdf_path.name)                # LinkedIn: one PDF document
        z.writestr("Captions.txt", caption_doc(spec))   # both captions
    print("wrote", zpath)

if __name__ == "__main__":
    main()
