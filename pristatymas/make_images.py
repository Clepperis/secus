"""Compose the picture for each slide from the source images (saltiniai/)."""
import os
from PIL import Image, ImageDraw, ImageFilter, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'saltiniai')
OUT = os.path.join(HERE, 'nuotraukos')
W, H = 1600, int(1600 / (5.75 / 3.9))  # picture slot ratio
PURPLE = (0x70, 0x41, 0xA5)
INK = (0x25, 0x26, 0x38)
MUTED = (0x6B, 0x66, 0x75)
FONT = os.path.expanduser('~/.fonts/Manrope-400.ttf')
FONT_B = os.path.expanduser('~/.fonts/Manrope-700.ttf')

def background():
    # Soft diagonal gradient matching the template's picture frame tint.
    a, b, c = (228, 239, 232), (237, 237, 239), (246, 234, 246)
    bg = Image.new('RGB', (W, H))
    px = bg.load()
    for y in range(H):
        for x in range(W):
            t = (x / W + y / H) / 2
            if t < 0.5:
                u = t / 0.5; p, q = a, b
            else:
                u = (t - 0.5) / 0.5; p, q = b, c
            px[x, y] = tuple(int(p[i] + (q[i] - p[i]) * u) for i in range(3))
    return bg

def card(img, w=None, h=None, radius=22):
    img = img.convert('RGB')
    if w: h = round(img.height * w / img.width)
    else: w = round(img.width * h / img.height)
    img = img.resize((w, h), Image.LANCZOS)
    mask = Image.new('L', (w, h), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, w - 1, h - 1), radius, fill=255)
    return img, mask

def paste_card(bg, img, mask, x, y):
    sh = Image.new('L', (img.width + 80, img.height + 80), 0)
    ImageDraw.Draw(sh).rounded_rectangle((40, 48, 40 + img.width, 48 + img.height), 22, fill=70)
    sh = sh.filter(ImageFilter.GaussianBlur(18))
    bg.paste((60, 40, 80), (x - 40, y - 40), sh)
    bg.paste(img, (x, y), mask)

def single(name, out, pad=50):
    bg = background()
    img = Image.open(os.path.join(SRC, name))
    h = H - 2 * pad
    w = round(img.width * h / img.height)
    if w > W - 2 * pad:
        c, m = card(img, w=W - 2 * pad)
    else:
        c, m = card(img, h=h)
    paste_card(bg, c, m, (W - c.width) // 2, (H - c.height) // 2)
    bg.save(os.path.join(OUT, out))

def slide1():
    bg = background()
    pad, gap = 50, 50
    v, vm = card(Image.open(os.path.join(SRC, 'lrt_video_uzrakintos_durys.webp')), h=H - 2 * pad)
    paste_card(bg, v, vm, pad, pad)
    rw = W - 2 * pad - gap - v.width
    a, am = card(Image.open(os.path.join(SRC, 'lrytas_kaunas_2026-11-12.png')), w=rw)
    paste_card(bg, a, am, pad + v.width + gap, (H - a.height) // 2)
    bg.save(os.path.join(OUT, '1.png'))

def slide5(items, total_label, sub):
    bg = background()
    d = ImageDraw.Draw(bg)
    f_hero = ImageFont.truetype(FONT_B, 120)
    f_sub = ImageFont.truetype(FONT, 40)
    f_lab = ImageFont.truetype(FONT, 42)
    f_val = ImageFont.truetype(FONT_B, 42)
    x0 = 90
    d.text((x0, 70), total_label, font=f_hero, fill=INK)
    d.text((x0, 215), sub, font=f_sub, fill=MUTED)
    top, row = 330, 170
    maxv = max(v for _, v in items)
    barw = W - 2 * x0 - 230
    for i, (lab, v) in enumerate(items):
        y = top + i * row
        d.text((x0, y), lab, font=f_lab, fill=INK)
        bw = max(12, round(barw * v / maxv))
        d.rounded_rectangle((x0, y + 62, x0 + bw, y + 62 + 46), 10, fill=PURPLE)
        val = f'{v:,} €'.replace(',', ' ')
        d.text((x0 + bw + 24, y + 58), val, font=f_val, fill=INK)
    bg.save(os.path.join(OUT, '5.png'))

if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    single('lrytas_kaunas_2026-11-12.png', '1.png')
    single('spynos_koncepcija.webp', '2.png')
    single('latkauskas_2026-10-05.png', '3.png')
    single('lrt_istatyme_atsakymo_nera.png', '4.png')
    items = [('Spynos (12 × 250 €)', 3000), ('Kūrimas ir bandymai', 1500),
             ('Teisinė pagalba', 800), ('Montavimas (su ryšiu)', 700)]
    assert sum(v for _, v in items) == 6000
    slide5(items, '6 000 €', 'pilotui: 12 spynų Visagino priedangose')
    print('ok')
