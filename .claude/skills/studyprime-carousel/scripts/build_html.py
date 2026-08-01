#!/usr/bin/env python3
"""Render StudyPrime carousel inner-slide HTML from a spec JSON.
Usage: python build_html.py <spec.json> <out_html_dir>
Fonts are read from ../assets/fonts relative to this script and embedded as base64.
See references/spec-format.md for the spec schema."""
import base64, json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
FONTS = HERE.parent / "assets" / "fonts"
def font(p): return "data:font/ttf;base64," + base64.b64encode((FONTS / p).read_bytes()).decode()
ANTON, BB, BM = font("Anton.ttf"), font("Bricolage-Bold.ttf"), font("Bricolage-Med.ttf")

def hl(s): return re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)

CSS = f"""
@font-face{{font-family:'Anton';src:url({ANTON}) format('truetype');}}
@font-face{{font-family:'Bric';src:url({BB}) format('truetype');font-weight:700;}}
@font-face{{font-family:'BricM';src:url({BM}) format('truetype');font-weight:500;}}
:root{{--cream:#F4ECD8;--cream2:#EBE0C6;--navy:#17264D;--gold:#C9A233;}}
*{{margin:0;padding:0;box-sizing:border-box;}}
.slide{{position:relative;width:1080px;height:1440px;overflow:hidden;
 background:radial-gradient(120% 80% at 50% 0%,#FBF5E6,var(--cream) 55%,var(--cream2));}}
.grain{{position:absolute;inset:0;opacity:.5;mix-blend-mode:multiply;pointer-events:none;
 background-image:radial-gradient(rgba(23,38,77,.05) 1px,transparent 1px);background-size:6px 6px;}}
.kicker{{position:absolute;top:70px;left:80px;font-family:'Bric';font-weight:700;
 font-size:25px;letter-spacing:5px;text-transform:uppercase;color:var(--gold);}}
.emoji{{position:absolute;top:150px;right:88px;font-size:118px;transform:rotate(8deg);}}
.head{{position:absolute;top:120px;left:76px;font-family:'Anton';text-transform:uppercase;line-height:.9;}}
.head .n{{display:block;color:var(--navy);font-size:100px;white-space:nowrap;}}
.head .g{{display:block;color:var(--gold);font-size:150px;white-space:nowrap;
 -webkit-text-stroke:3px var(--navy);paint-order:stroke fill;
 text-shadow:2px 2px 0 var(--navy),4px 4px 0 var(--navy),6px 6px 0 var(--navy),8px 8px 0 var(--navy),10px 10px 0 var(--navy);}}
.body{{position:absolute;top:520px;left:80px;right:80px;bottom:150px;}}
.list{{display:flex;flex-direction:column;gap:42px;}}
.item{{display:flex;align-items:flex-start;gap:30px;}}
.num{{flex:0 0 auto;width:84px;height:84px;border-radius:50%;background:var(--gold);
 border:4px solid var(--navy);display:flex;align-items:center;justify-content:center;
 font-family:'Anton';font-size:48px;color:var(--navy);box-shadow:4px 4px 0 rgba(23,38,77,.25);}}
.txt{{font-family:'Bric';font-weight:700;color:var(--navy);font-size:50px;line-height:1.08;padding-top:6px;}}
.txt b,.stack b{{color:var(--gold);-webkit-text-stroke:1px var(--navy);}}
.stack{{display:flex;flex-direction:column;gap:34px;}}
.stack .l{{font-family:'Bric';font-weight:700;color:var(--navy);font-size:58px;line-height:1.14;}}
.stack .q{{font-size:66px;}}
.stack .chain{{font-family:'Anton';font-size:60px;color:var(--gold);letter-spacing:1px;
 -webkit-text-stroke:2px var(--navy);paint-order:stroke fill;line-height:1;text-transform:uppercase;}}
.stack .sm{{font-family:'BricM';font-weight:500;font-size:40px;color:rgba(23,38,77,.7);}}
.note{{margin-top:38px;font-family:'Bric';font-weight:700;font-size:44px;color:var(--gold);-webkit-text-stroke:1px var(--navy);}}
.cta{{display:flex;flex-direction:column;gap:40px;}}
.crow{{display:flex;align-items:center;gap:28px;}}
.crow .ic{{flex:0 0 auto;width:88px;height:88px;border-radius:24px;background:var(--navy);
 display:flex;align-items:center;justify-content:center;font-size:44px;}}
.crow .ct{{font-family:'Bric';font-weight:700;font-size:46px;color:var(--navy);line-height:1.05;}}
.biobar{{position:absolute;left:80px;right:80px;bottom:150px;background:var(--navy);border-radius:22px;
 padding:34px 40px;display:flex;align-items:center;justify-content:center;gap:16px;
 font-family:'Anton';font-size:44px;color:var(--gold);text-transform:uppercase;letter-spacing:1px;
 box-shadow:6px 6px 0 rgba(23,38,77,.2);}}
.foot{{position:absolute;bottom:56px;left:80px;right:80px;display:flex;align-items:center;
 justify-content:space-between;font-family:'Bric';font-weight:700;color:var(--navy);font-size:30px;}}
.dots{{display:flex;gap:10px;}}.dots i{{width:14px;height:14px;border-radius:50%;background:rgba(23,38,77,.25);}}
.dots i.on{{background:var(--gold);width:38px;border-radius:8px;}}
.rt{{color:var(--gold);letter-spacing:2px;text-transform:uppercase;}}
"""

def dots(n, total):
    return '<span class="dots">' + ''.join(
        f'<i class="{"on" if i==n-1 else ""}"></i>' for i in range(total)) + '</span>'

def head(h): return f'<div class="head"><span class="n">{h[0]}</span><span class="g">{h[1]}</span></div>'

def body_list(items, note=""):
    rows = ''.join(f'<div class="item"><div class="num">{n}</div><div class="txt">{hl(t)}</div></div>' for n, t in items)
    nt = f'<div class="note">{hl(note)}</div>' if note else ''
    return f'<div class="body"><div class="list">{rows}</div>{nt}</div>'

def body_stack(lines):
    out = ''.join(f'<div class="{cls}">{hl(txt)}</div>' for cls, txt in lines)
    return f'<div class="body"><div class="stack">{out}</div></div>'

def body_cta(rows):
    r = ''.join(f'<div class="crow"><div class="ic">{ic}</div><div class="ct">{hl(t)}</div></div>' for ic, t in rows)
    return f'<div class="body" style="bottom:280px"><div class="cta">{r}</div></div>'

def render(slide, kicker, total):
    n = slide["n"]; h = slide["head"]; t = slide.get("type", "stack")
    emoji = f'<div class="emoji">{slide["emoji"]}</div>' if slide.get("emoji") else ''
    if t == "list":
        bodyhtml = body_list([tuple(x) for x in slide["items"]], slide.get("note", ""))
    elif t == "cta":
        bodyhtml = body_cta([tuple(x) for x in slide["rows"]])
    else:
        bodyhtml = body_stack([tuple(x) for x in slide["lines"]])
    biobar = '<div class="biobar">🎯 1-1 CONSULTATION — LINK IN BIO</div>' if slide.get("bio") else ''
    rt = '↗ SHARE' if t == "cta" else 'SWIPE →'
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="slide"><div class="grain"></div><div class="kicker">{kicker}</div>{emoji}
{head(h)}{bodyhtml}{biobar}
<div class="foot"><span>studyprime.pk</span>{dots(n,total)}<span class="rt">{rt}</span></div>
</div></body></html>"""

def main():
    spec = json.loads(pathlib.Path(sys.argv[1]).read_text())
    outdir = pathlib.Path(sys.argv[2]); outdir.mkdir(parents=True, exist_ok=True)
    kicker = spec["kicker"]; total = spec.get("total_slides", len(spec["slides"]) + 1)
    for s in spec["slides"]:
        (outdir / f"slide{s['n']}.html").write_text(render(s, kicker, total))
    print(f"wrote {len(spec['slides'])} slide HTML files to {outdir}")

if __name__ == "__main__":
    main()
