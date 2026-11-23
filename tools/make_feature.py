# Builds feature.png (1024x500: link previews, and the Google Play feature graphic) from the game's art and fonts. See README.md.
from PIL import Image, ImageDraw, ImageFont, ImageFilter
G = '/Volumes/T7/Projects/regression_tazza/web'
S = '/Volumes/T7/Projects/regression-tazza-site'
W, H = 1024, 500
BLACK = (0x14, 0x10, 0x0d); AMBER = (0xe9, 0xa2, 0x3b); BRICK = (0xa8, 0x40, 0x2c); CREAM = (0xef, 0xe2, 0xc4)
img = Image.new('RGB', (W, H), BLACK)

def hero(name, w, top):
    im = Image.open(f'{G}/art/{name}.webp').convert('RGB')
    h = round(im.height * w / im.width)
    return im.resize((w, h), Image.LANCZOS).crop((0, top, w, top + H))

# the one hero, Danny Young (윤동욱), on the right under the bulb. The second hero stays off the site (game CLAUDE.md).
PW, TOP = 560, 40
x0 = W - PW
img.paste(hero('hero_dongwook', PW, TOP), (x0, 0))

# fade the left edge of the art into black for the text
fade = Image.new('L', (W, H), 0)
fd = ImageDraw.Draw(fade)
for x in range(0, 230):
    a = int(255 * (1 - x / 230) ** 1.4)
    fd.line([(x0 + x, 0), (x0 + x, H)], fill=a)
fd.rectangle([0, 0, x0, H], fill=255)
img = Image.composite(Image.new('RGB', (W, H), BLACK), img, fade)
# bottom shade
shade = Image.new('L', (W, H), 0); sd = ImageDraw.Draw(shade)
for y in range(H - 140, H):
    sd.line([(0, y), (W, y)], fill=int(170 * ((y - (H - 140)) / 140) ** 1.6))
img = Image.composite(Image.new('RGB', (W, H), BLACK), img, shade)

d = ImageDraw.Draw(img)
bhs = f'{G}/fonts/BlackHanSans-Regular.ttf'
title = ImageFont.truetype(bhs, 104)
small = ImageFont.truetype(bhs, 22)
noto = ImageFont.truetype(f'{G}/fonts/NotoSansKR-Variable.ttf', 23)
try: noto.set_variation_by_axes([600])
except Exception: pass
X = 56
d.text((X, 92), '서울, 1997', font=small, fill=AMBER)
d.text((X - 4, 122), '회귀한', font=title, fill=CREAM)
d.text((X - 4, 226), '타짜', font=title, fill=CREAM)
d.text((X, 352), 'REGRESSION GAMBLER', font=small, fill=AMBER)
d.text((X, 400), '다 털린 날로 회귀했더니,', font=noto, fill=CREAM)
d.text((X, 434), '다음 카드가 보인다.', font=noto, fill=CREAM)
img.save(f'{S}/feature.png', optimize=True)
print(img.size)
