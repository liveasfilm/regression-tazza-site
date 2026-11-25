# 회귀한 타짜 · Regression Gambler — 마케팅 사이트

게임 `../regression_tazza` 의 마케팅 사이트와 개인정보처리방침이다. GitHub Pages(`liveasfilm/regression-tazza-site`)로 낸다.

- 마케팅 URL, 지원 URL: https://liveasfilm.github.io/regression-tazza-site/ (지원은 `#support` 에 있다. `?lang=en` 이나 `?lang=ko` 로 언어를 고정할 수 있다. 없으면 브라우저 언어를 따른다.)
- 개인정보처리방침 URL: https://liveasfilm.github.io/regression-tazza-site/privacy.html (한국어와 영어가 한 쪽에 같이 있다. 영어는 `#en`.)

## 파일

- `index.html`: 한 쪽에 한국어와 영어를 같이 쓰고 `data-l="ko|en"` 으로 하나만 보인다. 오른쪽 위 단추로 바꾼다. 자바스크립트가 없으면 둘 다 보인다.
- `privacy.html`: 앱이 실제로 하는 것만 적었다. 광고, 분석, 계정, 앱 자체의 네트워크 호출이 없고, 진행·이어하기·설정은 기기의 웹 저장소(아이폰 WKWebView, 안드로이드 WebView의 localStorage, `tazza.*` 일곱 키: `cleared`, `best`, `purse`, `loops`, `save`, `settings`, `muted`)에만 있다. 앱은 App Store와 Google Play에서 파는 유료 앱이고 앱 안 결제가 없어서, 구매 표시(`tazza.unlocked`)는 쓰지 않는다(게임 `web/src/store.js` 의 `isPaidApp`). 앱에 새로 무엇을 모으게 되면 이 문서를 먼저 고친다.
- 가격: 구매 칸(`.ticket .stub` 두 칸)은 한 가격만 적는다. 한국어 ₩3,000, 영어 $1.99(사용자 2026-11-23, 출시 기념가와 정가 구분 없음). 기준은 게임 `store/metadata.json` 의 `pricing`. 가격이 바뀌면 두 칸을 같이 고친다.
- 스토어: 2026-11-25부터 안드로이드만 낸다(아이폰은 Apple이 개인 계정의 모의 도박 앱을 받지 않아 보류, 게임 `store/review_rejection.md`). 그래서 `index.html` 의 출시 칩, 가격 안내, 다시 받기와 환불 안내는 Google Play 기준이다. Play 는 모의 도박 앱이라 한국에서 팔지 않으니 한국어 가격 안내에 그 말을 적었다. 출시되면 칩을 Play 링크로 바꾼다. `privacy.html` 은 두 스토어를 그대로 둔다.
- `art/`: 게임의 `web/art/*.webp` 를 그대로 복사했다. `icon.png`, `apple-touch-icon.png` 는 `docs/art/icon/app_icon.png` 를 줄인 것이다.
- `feature.png`(1024×500): 링크 미리보기 그림. 구글 플레이 그래픽 이미지로도 쓸 수 있다. `python3 tools/make_feature.py` 로 다시 만든다.
- 색은 게임의 네 가지(검정 `#14100d`, 호박색 `#e9a23b`, 벽돌색 `#a8402c`, 크림 `#efe2c4`)만 쓴다. 게임 DESIGN.md §12.

## 제목 글꼴

제목은 Black Han Sans(SIL OFL, `fonts/OFL-BlackHanSans.txt`)를 쓴다. 쓰인 글자만 잘라 `fonts/BlackHanSans-site.woff2`(약 20KB)로 넣었다. 제목, 소제목, 가격 글을 고치면 다시 잘라야 한다. 안 그러면 새 글자만 다른 글꼴로 나온다.

```bash
python3 -m venv /tmp/fontenv && /tmp/fontenv/bin/pip install fonttools brotli
python3 tools/heading_glyphs.py index.html privacy.html > /tmp/glyphs.txt
/tmp/fontenv/bin/pyftsubset ../regression_tazza/web/fonts/BlackHanSans-Regular.ttf --text-file=/tmp/glyphs.txt --flavor=woff2 --layout-features='*' --output-file=fonts/BlackHanSans-site.woff2
```

## 미리보기

```bash
python3 -m http.server 4190 --bind 127.0.0.1
```
