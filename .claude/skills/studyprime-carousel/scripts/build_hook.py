#!/usr/bin/env python3
"""Render Slide 1 (the hook) in BOTH house variations from a hook spec JSON.

Usage: python build_hook.py <hook.json> <out_html_dir>
Writes <out_dir>/slide1_A.html (clean cream, Ahsan cut out) and
       <out_dir>/slide1_B.html (real scene, Ahsan full-bleed).
Then run scripts/render.js on <out_dir> to get slide1_A.png / slide1_B.png,
show both to the user, and copy the chosen one to the carousel's hook_image.

Hook spec fields:
  slug          kebab id (for filenames only)
  navy          top headline line (small navy), UPPERCASE
  gold          bottom headline line (big gold 3D pop), UPPERCASE
  motif         faint tiled pop-word behind variation A (e.g. "LATE")
  cutout_image  path to Ahsan PNG with background removed  -> variation A
  scene_image   path to the full Freepik scene PNG (Ahsan in scenario) -> variation B
  doodles       (optional) raw SVG string of per-topic line-art doodles, shared by A & B
Any variation whose image is missing is skipped (you can build A first, B later)."""
import base64, json, mimetypes, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
TPL = HERE.parent / "assets" / "hook-templates"
FONTS = HERE.parent / "assets" / "fonts"

def font_uri(p): return "data:font/ttf;base64," + base64.b64encode((FONTS / p).read_bytes()).decode()

def img_uri(path):
    b = pathlib.Path(path).read_bytes()
    mime = mimetypes.guess_type(str(path))[0] or "image/png"
    return f"data:{mime};base64," + base64.b64encode(b).decode()

def main():
    spec = json.loads(pathlib.Path(sys.argv[1]).read_text())
    out = pathlib.Path(sys.argv[2]); out.mkdir(parents=True, exist_ok=True)
    anton = font_uri("Anton.ttf")
    doodles = spec.get("doodles", "")
    # Headline sizes: default to the locked 158/268; shrink per-hook for longer words
    # so the line never wraps or overflows the 1080px canvas.
    nsize = str(spec.get("navy_size", 158))
    gsize = str(spec.get("gold_size", 268))
    made = []

    if spec.get("cutout_image"):
        html = (TPL / "cream.html").read_text()
        html = (html.replace("__ANTON__", anton)
                    .replace("__CUTOUT__", img_uri(spec["cutout_image"]))
                    .replace("__MOTIF__", spec.get("motif", spec["gold"].strip("?!.")))
                    .replace("__NSIZE__", nsize).replace("__GSIZE__", gsize)
                    .replace("__NAVY__", spec["navy"]).replace("__GOLD__", spec["gold"])
                    .replace("<!-- __DOODLES__", doodles + "\n<!-- __DOODLES__"))
        (out / "slide1_A.html").write_text(html); made.append("A (cream)")

    if spec.get("scene_image"):
        html = (TPL / "office.html").read_text()
        html = (html.replace("__ANTON__", anton)
                    .replace("__BG__", img_uri(spec["scene_image"]))
                    .replace("__NSIZE__", nsize).replace("__GSIZE__", gsize)
                    .replace("__NAVY__", spec["navy"]).replace("__GOLD__", spec["gold"])
                    .replace("<!-- __DOODLES__", doodles + "\n<!-- __DOODLES__"))
        (out / "slide1_B.html").write_text(html); made.append("B (scene)")

    print("wrote hook variations:", ", ".join(made) or "(none — no images given)")

if __name__ == "__main__":
    main()
