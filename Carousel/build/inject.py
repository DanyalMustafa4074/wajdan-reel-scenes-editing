import base64, pathlib
b=pathlib.Path("build/template.html").read_text()
def d(p,mime):
    return f"data:{mime};base64,"+base64.b64encode(pathlib.Path(p).read_bytes()).decode()
b=b.replace("__ANTON__", d("fonts/Anton.ttf","font/ttf"))
b=b.replace("__BALOO__", d("fonts/Baloo2-800.ttf","font/ttf"))
b=b.replace("__CUTOUT__", d("ahsan_cutout.png","image/png"))
pathlib.Path("build/final.html").write_text(b)
print("ok", len(b))
