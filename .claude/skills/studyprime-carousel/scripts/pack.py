#!/usr/bin/env python3
"""Package one carousel into a zip: slide1..N.png + LinkedIn-Post.txt.
Usage: python pack.py <spec.json> <slides_dir> <out_dir>
- <spec.json> has "hook_image" (path to slide 1) and "linkedin" (caption text).
- <slides_dir> holds the rendered slide2.png..slideN.png (from render.js).
Produces <out_dir>/StudyPrime-Carousel-<slug>.zip"""
import json, pathlib, sys, zipfile

def main():
    spec = json.loads(pathlib.Path(sys.argv[1]).read_text())
    slides_dir = pathlib.Path(sys.argv[2])
    out_dir = pathlib.Path(sys.argv[3]); out_dir.mkdir(parents=True, exist_ok=True)
    slug = spec["slug"]
    zpath = out_dir / f"StudyPrime-Carousel-{slug}.zip"
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        if spec.get("hook_image"):
            z.write(spec["hook_image"], "slide1.png")
        for s in spec["slides"]:
            n = s["n"]
            z.write(slides_dir / f"slide{n}.png", f"slide{n}.png")
        z.writestr("LinkedIn-Post.txt", spec["linkedin"].strip() + "\n")
    print("wrote", zpath)

if __name__ == "__main__":
    main()
