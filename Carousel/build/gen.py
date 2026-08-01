import base64, pathlib, re, os
BASE=pathlib.Path("/tmp/claude-0/-home-user-wajdan-reel-scenes-editing/401e892c-7512-5158-bea0-11da6fe9478c/scratchpad")
def d(p): return "data:font/ttf;base64,"+base64.b64encode((BASE/p).read_bytes()).decode()
ANTON=d("fonts/Anton.ttf"); BB=d("fonts/Bricolage-Bold.ttf"); BM=d("fonts/Bricolage-Med.ttf")
def hl(s): return re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)

CSS=f"""
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
.stack .q{{font-size:66px;color:var(--navy);}}
.stack .q b{{color:var(--gold);}}
.stack .chain{{font-family:'Anton';font-size:60px;color:var(--gold);letter-spacing:1px;
 -webkit-text-stroke:2px var(--navy);paint-order:stroke fill;line-height:1;text-transform:uppercase;}}
.stack .sm{{font-family:'BricM';font-weight:500;font-size:40px;color:rgba(23,38,77,.7);}}
.note{{margin-top:38px;font-family:'Bric';font-weight:700;font-size:44px;color:var(--gold);
 -webkit-text-stroke:1px var(--navy);}}
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

def dots(n):
    return '<span class="dots">'+''.join(f'<i class="{"on" if i==n-1 else ""}"></i>' for i in range(5))+'</span>'

def head(h): return f'<div class="head"><span class="n">{h[0]}</span><span class="g">{h[1]}</span></div>'

def body_list(items):
    rows=''.join(f'<div class="item"><div class="num">{n}</div><div class="txt">{hl(t)}</div></div>' for n,t in items)
    return f'<div class="body"><div class="list">{rows}</div></div>'

def body_stack(parts):
    out=''
    for p in parts:
        cls,txt=p
        out+=f'<div class="{cls}">{hl(txt)}</div>'
    return f'<div class="body"><div class="stack">{out}</div></div>'

def body_cta(rows):
    r=''.join(f'<div class="crow"><div class="ic">{ic}</div><div class="ct">{hl(t)}</div></div>' for ic,t in rows)
    return f'<div class="body" style="bottom:280px"><div class="cta">{r}</div></div>'

def slide(kicker,h,bodyhtml,n,emoji='',cta=False,note='',bio=''):
    em=f'<div class="emoji">{emoji}</div>' if emoji else ''
    nt=f'' # note handled inside body for list
    biobar=f'<div class="biobar">🎯 1-1 CONSULTATION — LINK IN BIO</div>' if bio else ''
    rt='↗ SHARE' if cta else 'SWIPE →'
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="slide"><div class="grain"></div><div class="kicker">{kicker}</div>{em}
{head(h)}{bodyhtml}{biobar}
<div class="foot"><span>studyprime.pk</span>{dots(n)}<span class="rt">{rt}</span></div>
</div></body></html>"""

# ---- DATA ----
S=[]  # (carousel, slidenum, html)
def add(c,n,html): S.append((c,n,html))

# CAROUSEL 1
K="THE 3-YEAR METHOD"
add(1,2,slide(K,("WRONG FIRST","QUESTION"),body_stack([("l",'Everyone starts with **"UK? Canada? Australia?"**'),("l","It feels smart — it's how students waste **years and lakhs.**")]),2))
add(1,3,slide(K,("A COUNTRY ISN'T","A PLAN"),body_stack([("l","Fees, visa rules and job markets **shift every year.**"),("l","Pick a place first and your degree can lead **nowhere.**")]),3))
add(1,4,slide(K,("ASK THIS","INSTEAD"),body_stack([("l q",'"Where do I want to be in **3 years?**"'),("sm","Then work backwards ↓"),("chain","Goal → Pathway → Course → Country"),("l","Country is the **last** box you tick.")]),4))
add(1,5,slide(K,("SAVE THIS","FOR LATER"),body_cta([("🔖",'Save before you Google **"best country"**'),("↗","Share with a friend choosing blindly"),("💬","Want a plan around **your goal?**")]),5,cta=True,bio=1))

# CAROUSEL 2
K="RANKINGS ARE A TRAP"
add(2,2,slide(K,("RANKINGS DON'T","HIRE YOU"),body_stack([("l","A #1 logo on your degree **doesn't get you a job.**"),("l","Skills, outcomes and the **right course** do.")]),2))
add(2,3,slide(K,("WHAT RANKINGS","HIDE"),body_stack([("l","They rarely measure **graduate jobs** or your actual **course quality**,"),("l","**post-study work rights**, or cost vs. return.")]),3))
add(2,4,slide(K,("RANK ON","THIS INSTEAD"),body_list([("1","Does the **course** lead to your goal?"),("2","Do its graduates **actually get hired?**"),("3","**Post-study work** + real support?")]),4))
add(2,5,slide(K,("SAVE","+ SHARE"),body_cta([("🔖","Save before you shortlist universities"),("↗","Send it to someone chasing a ranking"),("💬","Not sure which **course** fits your goal?")]),5,cta=True,bio=1))

# CAROUSEL 3
K="COURSE › COUNTRY › UNIVERSITY"
add(3,2,slide(K,("MOST DO IT","BACKWARDS"),body_stack([("l","They pick the **country** first, then a uni, then any course that fits."),("l","That's how you get a degree that leads **nowhere.**")]),2))
add(3,3,slide(K,("THE RIGHT","ORDER"),body_list([("1","**COURSE** — matches your goal & strengths"),("2","**COUNTRY** — allows that career + a way to stay"),("3","**UNIVERSITY** — the best one for that course")]),3))
add(3,4,slide(K,("WHY IT","MATTERS"),body_stack([("l","Right course, wrong country = **no work rights.**"),("l","Right uni, wrong course = **wasted years.**"),("l","Get the order right and everything **lines up.**")]),4))
add(3,5,slide(K,("SAVE","THIS"),body_cta([("🔖","Save it before you apply anywhere"),("↗","Share with a student rushing it"),("💬","Want the order **mapped for you?**")]),5,cta=True,bio=1))

# CAROUSEL 4
K="CONSULTANT RED FLAGS"
add(4,2,slide(K,("WATCH FOR","THESE"),body_stack([("l","A good consultant **changes your life.** A bad one **takes your money.**"),("l","6 red flags to catch **before you commit.**")]),2,emoji="🚩"))
add(4,3,slide(K,("FIRST 3","RED FLAGS"),body_list([("1","Pushes the **same** country or university on everyone"),("2",'Promises a **"100% guaranteed"** visa'),("3","Won't explain what you're **actually paying** for")]),3))
add(4,4,slide(K,("NEXT 3","RED FLAGS"),body_list([("4",'Rushes you to **pay "today only"**'),("5","**No track record**, no references"),("6","Never asks about your **actual goal**")]),4))
add(4,5,slide(K,("SAVE BEFORE","YOU SIGN"),body_cta([("🔖","Save before your next meeting"),("↗","Share it — it protects someone"),("💬","Want an **honest** second opinion?")]),5,cta=True,bio=1))

# CAROUSEL 5
K="BEFORE YOU PAY"
add(5,2,slide(K,("IT'S YOUR","MONEY"),body_stack([("l q","Before you hand over a **single rupee** —"),("l","get these answered **in writing.**")]),2))
add(5,3,slide(K,("ASK ABOUT","THE MONEY"),body_list([("1","Exactly what does this **fee cover?**"),("2","What's **NOT** included (visa, tests, deposits)?"),("3","What's the **refund policy** if I'm rejected?")]),3))
add(5,4,slide(K,("ASK ABOUT","THE DEAL"),body_list([("4","Is all of this in a **written contract?**"),("5","Do you earn **commission** from any university?")])[:-6]+'<div class="note">No clear answers? Walk away.</div></div>',4))
add(5,5,slide(K,("SAVE THIS","CHECKLIST"),body_cta([("🔖","Screenshot before your next meeting"),("↗","Share with someone about to pay"),("💬","Want a **no-pressure** review first?")]),5,cta=True,bio=1))

# CAROUSEL 6
K="GREEN FLAGS"
add(6,2,slide(K,("YOU'RE","HIRING THEM"),body_stack([("l","You're the client — **act like it.** Treat meeting 1 like a **job interview.**"),("l","Here's what a **good one** looks like.")]),2,emoji="✅"))
add(6,3,slide(K,("GREEN","FLAGS"),body_list([("1","Asks about **your goal** before selling"),("2","Shows **real past students** & results"),("3","Explains options honestly — even **cheaper** ones")]),3))
add(6,4,slide(K,("PROOF, NOT","PROMISES"),body_list([("4","Properly **registered / certified**"),("5","Happy to share **references**"),("6","**Never pressures** you to pay on the spot")]),4))
add(6,5,slide(K,("SAVE","+ SHARE"),body_cta([("🔖","Save before you choose anyone"),("↗","Share with a student consultant-shopping"),("💬","Want to feel what **honest** guidance is like?")]),5,cta=True,bio=1))

# CAROUSEL 7
K="APPLICATION MISTAKES"
add(7,2,slide(K,("SMALL SLIPS,","BIG REJECTIONS"),body_stack([("l","Strong students get rejected over **avoidable mistakes.**"),("l","Fix these **before** you apply.")]),2))
add(7,3,slide(K,("MISTAKES","1–3"),body_list([("1","A vague, **copy-paste** statement of purpose"),("2","No clear reason for your **course or country**"),("3","**Weak or unexplained** finances")]),3))
add(7,4,slide(K,("MISTAKES","4–5"),body_list([("4","Gaps or grades left **unexplained**"),("5","Applying **last-minute**, no proofreading")])[:-6]+'<div class="note">Every one of these is fixable.</div></div>',4))
add(7,5,slide(K,("SAVE","THIS"),body_cta([("🔖","Save before you write your application"),("↗","Share with someone applying this year"),("💬","Want your **SOP & profile** reviewed?")]),5,cta=True,bio=1))

out=BASE/"build/slides"; out.mkdir(parents=True,exist_ok=True)
for c,n,html in S:
    (out/f"c{c}_s{n}.html").write_text(html)
print("generated",len(S),"slides")
