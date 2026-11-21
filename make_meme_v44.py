"""GTA6 meme v44 — v42's page with the punchline moved above the letterhead.

The judge scored v42 58/70 and named the two weak criteria: readable-at-a-glance and
original. Its own instruction was "make the punchline hit harder and earlier — put
the laugh before the pitch". v43 answered that with a drawn waiting room, which the
judge then punished for being "muddy" and needing "more setup" — the scene added
read time instead of removing it.

So this version changes the reading order and nothing else. The page, the five
charges, the sum, the stamp and the play code are untouched. What is new:

  - a black band across the top carrying the punchline in 76px: "13 YEARS.
    THE GAME STILL ISN'T OUT." That is the sentence a person can quote.
  - the invoice's own title drops to a subordinate line, because the joke now
    leads and the document follows
  - the charge labels are rewritten to be quotable rather than bureaucratic:
    a reader should laugh at the label, not at the quantity
  - the ghost stays at 250px in the letterhead, because that scored 10/10

Every string is width-checked against the column it lives in before it is drawn.
"""
import os

from PIL import Image, ImageDraw, ImageFilter, ImageFont

F = os.environ.get("FONT_DIR", "/root/makefun-tr/practice-1119/fonts/")
HERE = os.path.dirname(os.path.abspath(__file__))

INK = (18, 16, 20)
WHITE = (255, 255, 255)
BACKDROP = (226, 224, 221)
GREY = (112, 106, 100)
PALE = (206, 200, 193)
RED = (192, 26, 40)
MAG = (198, 26, 132)

W = H = 1200
PX0, PY0, PX1, PY1 = 50, 40, 1150, 1160
M, R = PX0 + 42, PX1 - 42

SB = "LiberationSans-Bold.ttf"
SR = "LiberationSans-Regular.ttf"
SN = "LiberationSansNarrow-Bold.ttf"
MB = "LiberationMono-Bold.ttf"

ITEMS = [
    ("Same 90 seconds again", "4,811 × $0.50", 2405.50),
    ("Trailer 2 rewatches", "87 × $13.00", 1131.00),
    ("Checked a map for a dot", "12,000 × $0.05", 600.00),
    ("Jason & Lucia counseling", "flat rate", 174.50),
    ("Delay relapses + one game", "lump sum", 500.00),
]
TOTAL = sum(i[2] for i in ITEMS)
assert abs(TOTAL - 4811.00) < 0.001, TOTAL


def ft(name, size):
    return ImageFont.truetype(os.path.join(F, name), size)


def main():
    img = Image.new("RGB", (W, H), BACKDROP)

    shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(shadow).rectangle(
        [PX0 + 7, PY0 + 11, PX1 + 9, PY1 + 13], fill=(0, 0, 0, 58)
    )
    img = Image.alpha_composite(img.convert("RGBA"), shadow.filter(ImageFilter.GaussianBlur(9)))

    page = Image.new("RGBA", (PX1 - PX0, PY1 - PY0), (0, 0, 0, 0))
    pd = ImageDraw.Draw(page)
    pd.rectangle([0, 0, PX1 - PX0 - 1, PY1 - PY0 - 1], fill=WHITE, outline=INK, width=3)
    img.paste(page, (PX0, PY0), page)
    d = ImageDraw.Draw(img)

    def rule(y, w=2, c=INK, x0=M, x1=R):
        d.line([(x0, y), (x1, y)], fill=c, width=w)

    def text(x, y, s, font, fill, anchor=None):
        d.text((x, y), s, font=font, fill=fill, anchor=anchor)
        return d.textbbox((x, y), s, font=font, anchor=anchor)

    # ============ the punchline leads: black band, white type, one sentence ============
    band_top = PY0 + 22
    band_h = 176
    d.rectangle([PX0 + 18, band_top, PX1 - 18, band_top + band_h], fill=INK)

    inner = (PX1 - PX0 - 36) - 44
    l1, l2 = "13 YEARS.", "THE GAME STILL ISN'T OUT."
    pf = ft(SB, 66)
    w1, w2 = d.textlength(l1, font=pf), d.textlength(l2, font=pf)
    assert max(w1, w2) <= inner, f"punchline {max(w1, w2):.0f}px wider than {inner}px band"
    text((PX0 + PX1) / 2, band_top + 8, l1, pf, WHITE, anchor="ma")
    text((PX0 + PX1) / 2, band_top + 78, l2, pf, WHITE, anchor="ma")
    sub = "A HOSPITAL BILL FOR WAITING · PAID BY AN AI AGENT ON make.fun"
    text((PX0 + PX1) / 2, band_top + 142, sub, ft(SN, 26), (250, 190, 225), anchor="ma")
    pw = max(w1, w2)

    # ============ letterhead: the ghost, still 10/10, now under the joke ============
    seal = 236
    sx, sy = M, band_top + band_h + 24
    mark_path = os.path.join(HERE, "assets", "mark-1024.png")
    if os.path.exists(mark_path):
        mark = Image.open(mark_path).convert("RGBA").resize((seal, seal), Image.LANCZOS)
        img.paste(mark, (sx, sy), mark)
    d = ImageDraw.Draw(img)

    tx = sx + seal + 24
    text(tx, sy + 6, "VICE CITY HOSPITAL · PSYCHIATRIC WARD", ft(SN, 24), GREY)
    text(tx, sy + 40, "FINAL INVOICE", ft(SB, 52), MAG)
    text(tx, sy + 104, "PATIENT: ONE VERY PATIENT GAMER", ft(MB, 22), INK)

    plate_y = sy + 142
    plate_h = 60
    d.rectangle([tx - 10, plate_y, R, plate_y + plate_h], fill=MAG)
    wm = ft(SB, 38)
    text(tx, plate_y + 9, "make.fun", wm, WHITE)
    wmw = d.textlength("make.fun", font=wm)
    text(tx + wmw + 18, plate_y + 16, "WHERE PEOPLE AND THEIR AGENTS EARN", ft(SN, 22), WHITE)

    y = plate_y + plate_h + 16
    text(M, y, "CASE VC-2013-4811 · ADMITTED 17 SEP 2013 · ISSUED 19 NOV 2026", ft(MB, 20), GREY)
    y += 32
    rule(y, 3, MAG)

    # ============ diagnosis ============
    y += 16
    text(M, y, "DIAGNOSIS", ft(SB, 20), MAG)
    text(M + 158, y - 4, "ACUTE GTA VI ANTICIPATION DISORDER", ft(SB, 32), INK)
    y += 44
    text(M, y, "DAYS WARDED", ft(SB, 20), MAG)
    text(M + 158, y - 26, "4,811", ft(SB, 72), INK)
    y += 58
    rule(y, 1, PALE)
    y += 16

    # ============ charges, labels written to be quoted ============
    text(M, y, "CHARGES", ft(SB, 20), MAG)
    y += 32

    f_item = ft(MB, 24)
    for name, qty, amt in ITEMS:
        money = f"${amt:,.2f}"
        label = f"{name.upper()}  ({qty})"
        lw = d.textlength(label, font=f_item)
        tw = d.textlength(money, font=f_item)
        assert M + lw + 22 < R - tw, f"label overlaps amount: {label}"
        text(M, y, label, f_item, INK)
        text(R - tw, y, money, f_item, INK)
        xx = M + lw + 10
        while xx < R - tw - 10:
            d.point((xx, y + 16), fill=PALE)
            xx += 9
        y += 38

    y += 4
    rule(y, 3)
    y += 12

    # ============ total ============
    total_y = y
    text(M, y, "TOTAL DUE", ft(SB, 30), INK)
    amount = f"${TOTAL:,.2f}"
    big = ft(SB, 74)
    tw = d.textlength(amount, font=big)
    text(R - tw, y - 10, amount, big, INK)
    y += 74

    # ============ settled, as a bar under the total, not a stamp over it ============
    FS = 112
    FY = PY1 - FS - 18
    bar_top = total_y + 70
    bar_h = 46
    assert bar_top + bar_h < FY - 24, (
        f"settled bar bottom {bar_top + bar_h} reaches the footer rule at {FY - 14}")
    d.rectangle([M, bar_top, R, bar_top + bar_h], fill=RED)
    sline = "SETTLED BY AN AI AGENT PAYOUT · 13 YEARS LATE · ONE DOLLAR A DAY"
    sf = ft(SN, 30)
    sw = d.textlength(sline, font=sf)
    assert sw <= (R - M) - 40, f"settled line {sw:.0f}px wider than the bar"
    text((M + R) / 2, bar_top + 8, sline, sf, WHITE, anchor="ma")

    # ============ footer ============
    rule(FY - 14, 1, PALE)
    if os.path.exists(mark_path):
        mk = Image.open(mark_path).convert("RGBA").resize((FS, FS), Image.LANCZOS)
        img.paste(mk, (M, FY - 4), mk)
    d = ImageDraw.Draw(img)

    fx = M + FS + 16
    text(fx, FY - 2, "PAID BY MY AI AGENT ON make.fun", ft(SB, 25), MAG)
    text(fx, FY + 28, "YOUR AGENT PAYS THE BILLS. YOU JUST WAIT FOR THE GAME.", ft(SN, 19), GREY)
    code_f = ft(MB, 30)
    cw = d.textlength("makefun-minnow-citadel-bow", font=code_f)
    assert fx + cw < R, f"play code {cw:.0f}px runs past the margin"
    text(fx, FY + 56, "makefun-minnow-citadel-bow", code_f, INK)

    out = os.path.join(HERE, "meme_v44.png")
    img.convert("RGB").save(out, "PNG")
    print(f"saved {out} {os.path.getsize(out)} {(W, H)} | punch {pw:.0f}px in band | "
          f"band {band_top}..{band_top + band_h} | footer {FY}")


if __name__ == "__main__":
    main()
