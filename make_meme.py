"""GTA6 meme v11 — Vice City Hospital invoice, SQUARE, MEME-FIRST.
Rank-1 lesson: 5 big items, one huge TOTAL, one dominant stamp, huge type.
Everything readable at 400px feed size. Itemised sum = $4,811.00.
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math, random, os

F = os.environ.get('FONT_DIR', '/System/Library/Fonts/Supplemental/')

def ft(n, s): return ImageFont.truetype(F + n, s)
SB, SR = 'LiberationSans-Bold.ttf', 'LiberationSans-Regular.ttf'
MB = 'LiberationMono-Bold.ttf'
INK = (18, 14, 20); CREAM = (250, 246, 236); GREY = (110, 102, 96)
RED = (196, 30, 44); MAG = (196, 28, 131); YEL = (255, 204, 66)

W = H = 1600
PX0, PY0, PX1, PY1 = 92, 60, 1508, 1540
M, R = PX0 + 56, PX1 - 56

# 5 items, big numbers, sum exactly 4811
ITEMS = [
    ("Trailer 2 rewatches",         "87 × $13",       1131.00),
    ("Same 90 seconds, again",      "4,811 × $0.50",  2405.50),
    ("Map-dot checks",              "12,000 × $0.05",  600.00),
    ("Jason & Lucia counselling",   "flat",            174.50),
    ("Delay relapses + game",       "5 + 1",           500.00),
]
TOTAL = sum(i[2] for i in ITEMS)
assert abs(TOTAL - 4811.00) < 0.001

# ---------- bg ----------
bg = Image.new('RGB', (W, H)); bd = ImageDraw.Draw(bg)
stops = [(0.00, (22, 10, 44)), (0.18, (78, 16, 88)), (0.38, (158, 28, 106)),
         (0.56, (216, 62, 96)), (0.72, (246, 124, 74)), (0.88, (255, 178, 86)),
         (1.00, (255, 216, 132))]
for y in range(H):
    t = y / H
    c = stops[-1][1]
    for i in range(len(stops) - 1):
        a0, c0 = stops[i]; b0, c1 = stops[i + 1]
        if a0 <= t <= b0:
            f = (t - a0) / (b0 - a0)
            c = tuple(int(c0[j] + (c1[j] - c0[j]) * f) for j in range(3)); break
    bd.line([(0, y), (W, y)], fill=c)
sx, sy = W // 2, int(H * 0.82)
for r, al in ((540, 26), (400, 34), (300, 44), (210, 58)):
    gl = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(gl).ellipse([sx - r, sy - r, sx + r, sy + r], fill=(255, 228, 152, al))
    bg = Image.alpha_composite(bg.convert('RGBA'), gl.filter(ImageFilter.GaussianBlur(46))).convert('RGB')
bd = ImageDraw.Draw(bg)
bd.ellipse([sx - 190, sy - 190, sx + 190, sy + 190], fill=(255, 238, 180))
random.seed(9); base = int(H * 0.955); x = 0
while x < W:
    bw = random.randint(56, 126); bh = random.randint(80, 230)
    bd.rectangle([x, base - bh, x + bw, base], fill=(46, 16, 52))
    x += bw + random.randint(5, 17)
bd.rectangle([0, base, W, H], fill=(34, 12, 40))
def palm(cx, by, s=1.0, col=(34, 12, 40)):
    bd.rectangle([cx - 4 * s, by - 220 * s, cx + 4 * s, by], fill=col)
    for ang in (-1.35, -0.95, -0.45, 0.45, 0.95, 1.35, 0):
        L = 110 * s
        ex, ey = cx + math.sin(ang) * L, by - 220 * s - math.cos(ang) * L * 0.55
        mx, my = cx + math.sin(ang) * L * 0.6, by - 220 * s - math.cos(ang) * L * 0.75
        bd.line([(cx, by - 220 * s), (mx, my), (ex, ey)], fill=col, width=int(7 * s), joint='curve')
for px_, ps in ((160, 1.2), (1450, 1.05)): palm(px_, base + 46, ps)

img = bg.convert('RGBA')
sh = Image.new('RGBA', (W, H), (0, 0, 0, 0))
ImageDraw.Draw(sh).rounded_rectangle([PX0 + 9, PY0 + 16, PX1 + 15, PY1 + 22], radius=24, fill=(20, 6, 26, 160))
img = Image.alpha_composite(img, sh.filter(ImageFilter.GaussianBlur(18)))

pp = Image.new('RGBA', (PX1 - PX0, PY1 - PY0), (0, 0, 0, 0))
pd = ImageDraw.Draw(pp)
pd.rounded_rectangle([0, 0, PX1 - PX0 - 1, PY1 - PY0 - 1], radius=22, fill=CREAM)
random.seed(5)
for _ in range(22000):
    v = random.randint(243, 251)
    pd.point((random.randrange(PX1 - PX0), random.randrange(PY1 - PY0)), fill=(v, v - 3, v - 9, 255))
img.paste(pp, (PX0, PY0), pp)
d = ImageDraw.Draw(img)

def rule(y, w=2, c=(206, 198, 188)): d.line([(M, y), (R, y)], fill=c, width=w)


# ---------- HEADER (thick, high contrast) ----------
d.rectangle([PX0 + 1, PY0 + 1, PX1 - 1, PY0 + 150], fill=INK)
# ---------- header medical cross icon ----------
ICX, ICY, ICR = M + 46, PY0 + 74, 46
d.ellipse([ICX - ICR, ICY - ICR, ICX + ICR, ICY + ICR], fill=(255, 255, 255), outline=YEL, width=5)
cw2, ch2 = 16, 48
d.rectangle([ICX - cw2 // 2, ICY - ch2 // 2, ICX + cw2 // 2, ICY + ch2 // 2], fill=RED)
d.rectangle([ICX - ch2 // 2, ICY - cw2 // 2, ICX + ch2 // 2, ICY + cw2 // 2], fill=RED)

d.text((M + 118, PY0 + 22), "VICE CITY HOSPITAL", font=ft(SB, 56), fill=(255, 255, 255))
d.text((M + 118, PY0 + 92), "PSYCHIATRIC WARD  ·  FINAL INVOICE", font=ft(SB, 25), fill=YEL)
d.text((R - 250, PY0 + 34), "CASE FILE", font=ft(SR, 17), fill=(190, 184, 178))
d.text((R - 250, PY0 + 60), "VC-2013-4811", font=ft(MB, 27), fill=(255, 255, 255))

# ---------- KEY FIELDS (huge, 3 across) ----------
y = 232
d.text((M, y), "ADMITTED", font=ft(SB, 17), fill=GREY)
d.text((M, y + 24), "LOS SANTOS", font=ft(SB, 40), fill=INK)
d.text((M, y + 74), "SEP 17, 2013", font=ft(MB, 26), fill=GREY)
d.text((M + 560, y), "DISCHARGED", font=ft(SB, 17), fill=GREY)
d.text((M + 560, y + 24), "VICE CITY", font=ft(SB, 40), fill=INK)
d.text((M + 560, y + 74), "NOV 19, 2026", font=ft(MB, 26), fill=GREY)
d.text((R - 330, y), "DAYS WAITING", font=ft(SB, 17), fill=GREY)
d.text((R - 330, y + 16), "4,811", font=ft(SB, 92), fill=INK)
rule(404)

# ---------- DIAGNOSIS (one big line) ----------
d.text((M, 424), "ACUTE GTA VI ANTICIPATION DISORDER", font=ft(SB, 44), fill=INK)
rule(492)

# ---------- ITEMS (6 rows, BIG) ----------
yy = 512
for name, qty, amt in ITEMS:
    d.text((M, yy), name, font=ft(SB, 40), fill=INK)
    d.text((M + 780, yy + 6), qty, font=ft(MB, 27), fill=GREY)
    money = f"${amt:,.2f}"
    tw = d.textlength(money, font=ft(MB, 40))
    d.text((R - tw, yy), money, font=ft(MB, 40), fill=INK)
    yy += 92
    for xx in range(M, R, 14):
        d.point((xx, yy - 12), fill=(206, 198, 188))

# ---------- TOTAL (dominant) ----------
rule(yy + 4, 4, INK)
d.text((M, yy + 24), "TOTAL DUE", font=ft(SB, 46), fill=INK)
tw = d.textlength(f"${TOTAL:,.2f}", font=ft(SB, 132))
d.text((R - tw, yy + 8), f"${TOTAL:,.2f}", font=ft(SB, 132), fill=INK)
d.text((M, yy + 84), "One dollar per day of waiting.", font=ft(SR, 24), fill=GREY)

# ---------- STAMP (dominant, overlapping total area is intentional) ----------
st = Image.new('RGBA', (560, 240), (0, 0, 0, 0)); sd = ImageDraw.Draw(st)
sd.rounded_rectangle([6, 6, 554, 234], radius=10, outline=(196, 30, 44, 240), width=13)
sd.text((38, 26), "SETTLED", font=ft(SB, 88), fill=(196, 30, 44, 240))
sd.text((42, 132), "13 YEARS LATE", font=ft(SB, 42), fill=(196, 30, 44, 240))
sd.text((42, 184), "BY AI AGENT PAYOUT", font=ft(SB, 26), fill=(196, 30, 44, 240))
st = st.rotate(-8, expand=True, resample=Image.BICUBIC)
img.paste(st, (M + 120, yy + 120), st)

# ---------- GHOST (right of stamp, clear) ----------
gx, gy, bh, bw = 1230, 1480, 210, 165
cx = gx; top = gy - bh
d.ellipse([cx - bw // 2, top, cx + bw // 2, top + bh * 0.85], fill=(255, 255, 255), outline=INK, width=7)
d.rectangle([cx - bw // 2, top + bh * 0.40, cx + bw // 2, gy], fill=(255, 255, 255))
d.ellipse([cx - bw // 2, gy - bh * 0.34, cx + bw // 2, gy + bh * 0.16], fill=(255, 255, 255), outline=INK, width=7)
d.line([(cx - bw // 2, top + bh * 0.42), (cx - bw // 2, gy - bh * 0.16)], fill=INK, width=7)
d.line([(cx + bw // 2, top + bh * 0.42), (cx + bw // 2, gy - bh * 0.16)], fill=INK, width=7)
def sparkle(sx2, sy2, r):
    p = []
    for i in range(8):
        ang = math.pi / 2 + i * math.pi / 4
        rr = r if i % 2 == 0 else r * 0.30
        p.append((sx2 + math.cos(ang) * rr, sy2 - math.sin(ang) * rr))
    d.polygon(p, fill=INK)
sparkle(cx - 30, top + bh * 0.30, 19)
sparkle(cx + 30, top + bh * 0.30, 19)
# cap with cross
cap_y = top - 4
d.rounded_rectangle([cx - 58, cap_y - 34, cx + 58, cap_y + 6], radius=11, fill=(255, 255, 255), outline=INK, width=7)
d.rectangle([cx - 64, cap_y - 2, cx + 64, cap_y + 10], fill=(255, 255, 255), outline=INK, width=6)
d.rectangle([cx - 6, cap_y - 28, cx + 6, cap_y - 4], fill=RED)
d.rectangle([cx - 16, cap_y - 21, cx + 16, cap_y - 11], fill=RED)

# star badge on ghost (mascot signature detail from the press kit)
bx0, by0 = cx + bw // 2 - 14, top + bh * 0.46
d.ellipse([bx0, by0, bx0 + 54, by0 + 54], fill=MAG, outline=INK, width=4)
def star5(sx3, sy3, ro, ri, col):
    pts = []
    for i in range(10):
        ang = -math.pi / 2 + i * math.pi / 5
        rr = ro if i % 2 == 0 else ri
        pts.append((sx3 + math.cos(ang) * rr, sy3 + math.sin(ang) * rr))
    d.polygon(pts, fill=col)
star5(bx0 + 27, by0 + 28, 18, 7.5, (255, 255, 255))

# ---------- FOOTER ----------
FH = 128
d.rectangle([PX0 + 1, PY1 - FH, PX1 - 1, PY1 - 1], fill=MAG)
mk = Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets', 'mark-1024.png')).convert('RGBA').resize((80, 80), Image.LANCZOS)
img.paste(mk, (M - 6, PY1 - FH + 24), mk)
d.text((M + 88, PY1 - FH + 22), "PAID BY MY AI AGENT", font=ft(SB, 34), fill=(255, 255, 255))
d.text((M + 88, PY1 - FH + 66), f"it settled ${TOTAL:,.2f} with a bounty payout on", font=ft(SR, 23), fill=(252, 222, 238))
pw, ph = 200, 52
px, py = R - pw, PY1 - FH + 38
d.rounded_rectangle([px, py, px + pw, py + ph], radius=26, fill=(255, 255, 255))
tw = d.textlength("make.fun", font=ft(SB, 29))
d.text((px + (pw - tw) / 2, py + 9), "make.fun", font=ft(SB, 29), fill=INK)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'meme.png')
img.convert('RGB').save(out)
print("saved", out, os.path.getsize(out), img.size, "| total", f"${TOTAL:,.2f}")
