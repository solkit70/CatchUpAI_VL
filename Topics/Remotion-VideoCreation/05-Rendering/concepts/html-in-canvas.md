# HTML-in-Canvas — 실험적 렌더링 모드

> **상태**: 실험적 (4.0.447+) — Breaking changes 발생 가능. 프로덕션 사용 주의.

## 개요

HTML-in-Canvas는 Remotion이 HTML을 CSS/DOM 방식이 아닌
**캔버스에 직접 래스터화**하여 렌더링하는 실험적 모드입니다.

### 기존 렌더링 vs HTML-in-Canvas

| | 기존 방식 | HTML-in-Canvas |
|--|---------|----------------|
| 렌더링 엔진 | Chrome headless (DOM → 스크린샷) | Canvas 래스터라이저 |
| 텍스트 서브픽셀 | OS에 따라 다름 | 완전히 동일 |
| CSS filter | 일부 제한 | 향상된 지원 |
| 속도 | 기준 | 비슷 또는 빠름 |
| 요구사항 | Chrome 일반 | **Chrome Canary 필요** |

---

## 활성화 방법

### CLI 플래그

```bash
npx remotion render MyComp out/video.mp4 --allow-html-in-canvas
```

### remotion.config.ts

```ts
import { Config } from '@remotion/cli/config';

Config.setAllowHtmlInCanvasEnabled(true);
```

### renderMedia() / renderStill() (프로그래매틱 렌더링)

```tsx
import { renderMedia } from '@remotion/renderer';

await renderMedia({
  composition: { ... },
  serveUrl: bundleLocation,
  codec: 'h264',
  outputLocation: 'out/video.mp4',
  allowHtmlInCanvas: true,  // ← 활성화
});
```

---

## Chrome Canary 요구사항

HTML-in-Canvas는 Chrome Canary에서만 완전히 지원됩니다:

```bash
# Chrome Canary 경로 지정
npx remotion render MyComp out/video.mp4 \
  --allow-html-in-canvas \
  --browser-executable="/path/to/Chrome Canary.app/Contents/MacOS/Google Chrome Canary"
```

Windows에서 Chrome Canary 경로:
```
C:\Users\<사용자명>\AppData\Local\Google\Chrome SxS\Application\chrome.exe
```

---

## 적합한 활용 사례

- 텍스트 서브픽셀 렌더링이 플랫폼 간에 완전히 동일해야 할 때
- `background-clip: text` + CSS gradient 텍스트 효과
- `drop-shadow` filter 합성이 정확해야 할 때
- SVG `clip-path` 효과 (polygon, ellipse, circle 등) — 4.0.450부터 개선

---

## 현재 프로젝트 적용 여부

Live6/Live7 하이라이트 영상은 기존 DOM 방식으로 문제없이 렌더링되므로
**현재는 HTML-in-Canvas 불필요**합니다.

그라데이션 텍스트, 복잡한 SVG 클리핑 등을 추가할 때 고려하세요.
