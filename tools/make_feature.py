# Builds feature.png (1024x500: link previews, and the Google Play feature graphic) from the game's art and fonts. See README.md.
from PIL import Image, ImageDraw, ImageFont, ImageFilter
G = '/Volumes/T7/Projects/regression_tazza/web'
S = '/Volumes/T7/Projects/regression-tazza-site'
W, H = 1024, 500
BLACK = (0x14, 0x10, 0x0d); AMBER = (0xe9, 0xa2, 0x3b); BRICK = (0xa8, 0x40, 0x2c); CREAM = (0xef, 0xe2, 0xc4)
img = Image.new('RGB', (W, H), BLACK)

def hero(name, w):
    im = Image.open(f'{G}/art/{name}.webp').convert('RGB')
    h = round(im.height * w / im.width)
    return im.resize((w, h), Image.LANCZOS).crop((0, 0, w, H))

# two heroes on the right, cut apart by a slanted ink line (like the menu poster)
PW = 330
left_x, right_x = W - 2 * PW + 40, W - PW
d_img = hero('hero_dongwook', PW + 60)
s_img = hero('hero_sujin', PW + 60)
img.paste(d_img, (left_x - 40, 0))
mask = Image.new('L', (W, H), 0)
md = ImageDraw.Draw(mask)
slant = 70
md.polygon([(right_x + slant, 0), (W, 0), (W, H), (right_x - slant, H)], fill=255)
layer = Image.new('RGB', (W, H), BLACK); layer.paste(s_img, (right_x - 60, 0))
img = Image.composite(layer, img, mask)
d = ImageDraw.Draw(img)
d.line([(right_x + slant, -5), (right_x - slant, H + 5)], fill=BLACK, width=10)

# fade the left edge of the art into black for the text
fade = Image.new('L', (W, H), 0)
fd = ImageDraw.Draw(fade)
x0 = left_x - 40
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
