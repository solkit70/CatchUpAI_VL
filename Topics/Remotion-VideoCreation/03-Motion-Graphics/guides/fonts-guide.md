# 폰트 로딩 가이드 — Google Fonts + 한국어 폰트

## 왜 폰트 로딩이 중요한가?

브라우저 기본 `sans-serif`는 한국어 영상에서 OS마다 다른 폰트로 렌더링됩니다.
렌더링 서버(headless Chrome)에서도 동일한 폰트를 보장하려면 명시적 로딩이 필요합니다.

---

## 방법 1: @remotion/google-fonts (권장)

### 설치

```bash
npx remotion add @remotion/google-fonts
```

### 한국어 폰트 예시 — Noto Sans KR

```tsx
import { loadFont } from '@remotion/google-fonts/NotoSansKR';

// 컴포넌트 외부 (모듈 최상단)에서 호출
const { fontFamily } = loadFont('normal', {
  weights: ['400', '700', '900'],
  subsets: ['korean', 'latin'],
});

export const KoreanTitle: React.FC<{ text: string }> = ({ text }) => (
  <div style={{ fontFamily, fontSize: 72, fontWeight: 900, color: '#202124' }}>
    {text}
  </div>
);
```

### 영어 폰트 예시 — Inter

```tsx
import { loadFont } from '@remotion/google-fonts/Inter';

const { fontFamily } = loadFont('normal', {
  weights: ['400', '600', '800'],
  subsets: ['latin'],
});
```

### 다중 폰트 조합

```tsx
import { loadFont as loadNoto } from '@remotion/google-fonts/NotoSansKR';
import { loadFont as loadInter } from '@remotion/google-fonts/Inter';

const { fontFamily: koreanFont } = loadNoto('normal', {
  weights: ['700'],
  subsets: ['korean'],
});
const { fontFamily: englishFont } = loadInter('normal', {
  weights: ['700'],
  subsets: ['latin'],
});
```

### 로딩 완료 대기 (선택)

렌더링 전 폰트가 반드시 로드되어야 한다면:

```tsx
const { fontFamily, waitUntilDone } = loadFont('normal', {
  weights: ['700'],
  subsets: ['korean'],
});

// calculateMetadata나 useDelayRender 내부에서:
await waitUntilDone();
```

---

## 방법 2: @remotion/fonts (로컬 폰트 파일)

OS 기본 폰트나 라이선스 폰트를 직접 포함할 때:

### 설치

```bash
npx remotion add @remotion/fonts
```

### 사용법

1. 폰트 파일을 `public/fonts/` 에 복사
2. 컴포넌트 파일 최상단에서 로드:

```tsx
import { loadFont } from '@remotion/fonts';
import { staticFile } from 'remotion';

// 비동기 로딩 — Promise를 반환
loadFont({
  family: 'Pretendard',
  url: staticFile('fonts/Pretendard-Bold.woff2'),
  weight: '700',
  style: 'normal',
});

export const MyComp: React.FC = () => (
  <div style={{ fontFamily: 'Pretendard', fontWeight: 700 }}>
    안녕하세요
  </div>
);
```

### 여러 굵기 동시 로드

```tsx
await Promise.all([
  loadFont({ family: 'Pretendard', url: staticFile('fonts/Pretendard-Regular.woff2'), weight: '400' }),
  loadFont({ family: 'Pretendard', url: staticFile('fonts/Pretendard-Bold.woff2'),    weight: '700' }),
  loadFont({ family: 'Pretendard', url: staticFile('fonts/Pretendard-Black.woff2'),   weight: '900' }),
]);
```

---

## 한국어 영상 권장 폰트

| 폰트 | Google Fonts 패키지명 | 특징 |
|------|----------------------|------|
| **Noto Sans KR** | `NotoSansKR` | 가독성 최고, 무게 다양 |
| **Black Han Sans** | `BlackHanSans` | 강렬한 제목용 단일 굵기 |
| **Nanum Gothic** | `NanumGothic` | 부드럽고 친근한 느낌 |
| **Do Hyeon** | `DoHyeon` | 게임/유튜브 자막 스타일 |
| **Gmarket Sans** | 로컬 파일 | 현대적, 커머스 콘텐츠 |

---

## 현재 프로젝트 상황

Live6/Live7 슬라이드 컴포넌트들은 `fontFamily: 'sans-serif'` 기본값을 사용 중.
Windows에서는 맑은 고딕, macOS에서는 Apple SD Gothic Neo로 렌더링됩니다.

일관된 한국어 폰트를 보장하려면 슬라이드 컴포넌트의 루트에 `NotoSansKR` 로딩을 추가하세요:

```tsx
// 예: BulletSlide.tsx 상단에 추가
import { loadFont } from '@remotion/google-fonts/NotoSansKR';
const { fontFamily } = loadFont('normal', { weights: ['400', '700', '800'], subsets: ['korean', 'latin'] });

// 이후 스타일에서 fontFamily 변수 사용
style={{ fontFamily, fontSize: 40 }}
```
