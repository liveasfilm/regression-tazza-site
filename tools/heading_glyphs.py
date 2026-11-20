# Prints the characters used in headings (h1-h3, top bar title, price) plus ASCII, for the Black Han Sans subset. See README.md.
import sys
from html.parser import HTMLParser
DISPLAY_TAGS = {'h1', 'h2', 'h3'}
class P(HTMLParser):
    def __init__(self):
        super().__init__(); self.stack = []; self.chars = set()
    def handle_starttag(self, tag, attrs):
        a = dict(attrs); cls = a.get('class') or ''
        on = tag in DISPLAY_TAGS or (tag == 'b' and self.stack and 'bar' in str(self.stack)) or 'price' in cls or (tag == 'a' and self.stack and 'top' in str(self.stack))
        self.stack.append((tag, cls, on))
    def handle_endtag(self, tag):
        while self.stack:
            t = self.stack.pop()
            if t[0] == tag: break
    def handle_data(self, d):
        if any(s[2] for s in self.stack): self.chars |= set(d)
p = P()
for f in sys.argv[1:]: p.feed(open(f, encoding='utf-8').read())
ascii_ = {chr(c) for c in range(32, 127)}
extra = set('₩·…—–“”‘’?!')
print(''.join(sorted((p.chars | ascii_ | extra) - {'\n'})))
