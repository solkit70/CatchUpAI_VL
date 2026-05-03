# HTML-in-Canvas — 실험적 렌더링 모드

> **상태**: 실험적 (4.0.447+, 설정 옵션 확장 4.0.455) — Breaking changes 발생 가능. 프로덕션 사용 주의.

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
| 요구사항 | Chrome 일반 | **Chrome Canary 필요** (일반 Chrome은 부분 지원) |

---

## 활성화 방법 (4가지)

### 1. CLI 플래그

```bash
npx remotion render MyComp out/video.mp4 --allow-html-in-canvas
```

### 2. remotion.config.ts

```ts
import { Config } from '@remotion/cli/config';

Config.setAllowHtmlInCanvasEnabled(true);
```

### 3. renderMedia() / renderStill() (프로그래매틱 렌더링)

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

### 4. Studio UI 토글 (4.0.455+) 🆕

Remotion Studio 상단 메뉴 → **Render** 설정 패널에서
`Allow HTML in Canvas` 체크박스로 켜고 끌 수 있습니다.
코드 변경 없이 빠르게 비교 테스트할 때 유용합니다.

---

## Chrome 지원 현황 (4.0.455 기준)

| 브라우저 | 지원 수준 | 비고 |
|---------|----------|------|
| Chrome Canary | ✅ 완전 지원 | `canvas.requestPaint()` 지원 |
| Chrome 일반 | ⚠️ 부분 지원 | `drawElementImage` API만 지원, 렌더링 불일치 가능 |
| Firefox / Safari | ❌ 미지원 | — |

```bash
# Chrome Canary 경로 지정 (Windows)
npx remotion render MyComp out/video.mp4 \
  --allow-html-in-canvas \
  --browser-executable="C:\Users\<사용자명>\AppData\Local\Google\Chrome SxS\Application\chrome.exe"

# macOS
npx remotion render MyComp out/video.mp4 \
  --allow-html-in-canvas \
  --browser-executable="/path/to/Chrome Canary.app/Contents/MacOS/Google Chrome Canary"
```

> **Fallback 동작**: HTML-in-Canvas를 활성화했어도 지원되지 않는 환경에서는
> 자동으로 기존 DOM 렌더링으로 폴백됩니다.

---

## 적합한 활용 사례

- 텍스트 서브픽셀 렌더링이 플랫폼 간에 완전히 동일해야 할 때
- `background-clip: text` + CSS gradient 텍스트 효과
- `drop-shadow` filter 합성이 정확해야 할 때 (4.0.455에서 `drop-shadow` 정식 지원 추가)
- SVG `clip-path` 효과 (polygon, ellipse, circle 등) — 4.0.450부터 개선
- 3D scale 변환 + `drop-shadow` 조합 (4.0.455+: precompose 자동 적용)

---

## 현재 프로젝트 적용 여부

Live6/Live7 하이라이트 영상은 기존 DOM 방식으로 문제없이 렌더링되므로
**현재는 HTML-in-Canvas 불필요**합니다.

그라데이션 텍스트, 복잡한 SVG 클리핑, 정밀한 `drop-shadow` 합성 등을 추가할 때 고려하세요.
