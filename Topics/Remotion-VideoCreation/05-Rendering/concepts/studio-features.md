# Remotion Studio 활용 가이드 — 4.0.452 기준

## Studio 실행

```bash
cd my-first-video
npm run dev
# 브라우저에서 http://localhost:3000 접속
```

---

## 4.0.452 주요 개선사항

### 1. Timeline 오디오 파형 시각화 ✨NEW

Studio의 타임라인에서 오디오 트랙의 파형(waveform)을 시각적으로 확인할 수 있습니다.
TTS 나레이션 슬라이드 작업 시 오디오 위치와 길이를 직관적으로 파악할 수 있어 편리합니다.

### 2. Timeline Pinch-to-Zoom ✨NEW

트랙패드/터치스크린에서 핀치 제스처로 타임라인을 확대·축소할 수 있습니다.
긴 영상에서 특정 구간을 정밀하게 검토할 때 유용합니다.

### 3. 10MB LRU 프레임 캐시 ✨NEW

타임라인 스크러빙 시 최근 디코딩된 프레임을 캐싱하여 성능이 향상됐습니다.
OffthreadVideo를 사용하는 슬라이드에서 특히 효과적입니다.

### 4. 향상된 에러 오버레이 ✨NEW

에러 발생 시 스택 트레이스를 클립보드로 복사할 수 있는 버튼이 추가됐습니다.
AI 디버깅 시 에러 내용을 빠르게 복사해서 붙여넣을 수 있습니다.

### 5. staticFile() 미사용 감지 ✨NEW

`<Audio src="audio.mp3" />` 처럼 `staticFile()`로 감싸지 않은 경우
명확한 힌트 메시지를 표시합니다:
```
Hint: Did you mean staticFile('audio.mp3')?
```

---

## Studio 핵심 기능 정리

### Props 패널 (우측)

`<Composition>`에 `schema` prop이 설정된 경우 활성화:

```tsx
// Root.tsx
<Composition
  id="MyComp"
  schema={mySchema}
  defaultProps={{ title: "기본값" }}
  ...
/>
```

- Studio에서 실시간으로 Props 수정 가능
- 변경된 Props로 즉시 프리뷰 반영

### 렌더링 모달

Studio 상단의 **Render** 버튼으로 렌더링 설정 UI를 열 수 있습니다:
- 코덱, 비트레이트, CRF 설정
- 렌더링 범위 (전체 / 구간 지정)
- `Allow HTML in canvas` 토글 (실험적 — 4.0.447+)
- `--sample-rate` 등 오디오 설정

### 단축키

| 단축키 | 동작 |
|--------|------|
| `Space` | 재생/일시정지 |
| `←` / `→` | 1프레임 이동 |
| `Shift+←` / `Shift+→` | 1초 이동 |
| `0` | 처음으로 이동 |
| `J` / `L` | 뒤로/앞으로 재생 |
| `I` / `O` | In/Out 포인트 설정 |

---

## 개발 효율화 팁

### 특정 Composition만 개발할 때

Studio URL에서 직접 선택 가능:
```
http://localhost:3000/Live7Highlight
```

### 프레임 단위 디버깅

```tsx
// 특정 프레임에서만 콘솔 출력
const frame = useCurrentFrame();
if (frame === 60) console.log('Frame 60 debug:', someValue);
```

### 렌더링 전 타입체크

```bash
npx tsc --noEmit
```

TypeScript 오류를 렌더링 전에 확인. 특히 `SlideData` 타입 불일치를 사전에 방지합니다.
