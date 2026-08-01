import base64, pathlib
BASE=pathlib.Path(".")
def b64(p): return "data:image/png;base64,"+base64.b64encode(pathlib.Path(p).read_bytes()).decode()
# carousel -> (title, hook_file)
M={1:("1 · WHICH COUNTRY? — 3-Year Method","firstslides/s5.png"),
   2:("2 · FORGET THE RANKING — Rankings Trap","firstslides/s2.png"),
   3:("3 · WRONG ORDER — Course>Country>Uni","firstslides/s1.png"),
   4:("4 · YOUR AGENT IS LYING — Red Flags","firstslides/s4.png"),
   5:("5 · BEFORE YOU PAY — Money Questions","firstslides/s7.png"),
   6:("6 · INTERVIEW YOUR CONSULTANT — Green Flags","firstslides/s6.png"),
   7:("7 · THIS GETS YOU REJECTED — App Mistakes","firstslides/s3.png")}
labels=["1 · HOOK","2","3","4","5 · CTA"]
outdir=pathlib.Path("build/previews"); outdir.mkdir(parents=True,exist_ok=True)
for c,(title,hook) in M.items():
    imgs=[hook]+[f"build/slides/c{c}_s{n}.png" for n in (2,3,4,5)]
    cells=""
    for i,im in enumerate(imgs):
        cells+=f'<div class="cell"><img src="{b64(im)}"><div class="lbl">{labels[i]}</div></div>'
    html=f"""<!doctype html><html><head><meta charset="utf-8"><style>
    *{{margin:0;padding:0;box-sizing:border-box;font-family:sans-serif}}
    body{{background:#14213E;padding:44px}}
    .title{{color:#F4A417;font-size:38px;font-weight:800;margin-bottom:28px;letter-spacing:1px}}
    .row{{display:flex;gap:26px}}
    .cell{{display:flex;flex-direction:column;gap:14px}}
    .cell img{{height:940px;width:auto;border-radius:14px;box-shadow:0 10px 30px rgba(0,0,0,.4);border:2px solid rgba(255,255,255,.08)}}
    .lbl{{color:#EBE0C6;font-size:26px;font-weight:700;text-align:center;letter-spacing:2px}}
    </style></head><body>
    <div class="title">{title}</div><div class="row">{cells}</div></body></html>"""
    (outdir/f"carousel{c}.html").write_text(html)
print("montages built")
