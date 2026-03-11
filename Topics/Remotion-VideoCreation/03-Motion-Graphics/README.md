# M3: 모션그래픽 컴포넌트

## 📖 학습 순서

이 폴더를 처음 여는 분은 아래 순서대로 읽으세요.

| 순서 | 문서 | 설명 |
|------|------|------|
| 1 | [concepts/reusable-components.md](concepts/reusable-components.md) | 재사용 가능한 컴포넌트 설계 (Zod 스키마, Props 패턴) |
| 2 | [concepts/css-in-js-for-video.md](concepts/css-in-js-for-video.md) | 영상에서의 CSS 스타일링 방법 |
| 3 | [guides/motion-patterns.md](guides/motion-patterns.md) | 자주 쓰는 모션 패턴 모음 (frame-delay, SVG 게이지 등) |
| 4 | [examples/title-card/README.md](examples/title-card/README.md) | TitleCard 컴포넌트 예시 |
| 5 | [examples/counter-infographic/README.md](examples/counter-infographic/README.md) | CounterInfoGraphic 컴포넌트 예시 |
| 6 | [examples/sequential-list/README.md](examples/sequential-list/README.md) | SequentialList 컴포넌트 예시 |

**이전 모듈**: [02-Core-Basics](../02-Core-Basics/) | **다음 모듈**: [04-Skills](../04-Skills/)

---

## 개요

Remotion으로 재사용 가능한 모션그래픽 컴포넌트 3종을 제작합니다.
각 컴포넌트는 Zod 스키마로 Props를 정의하여, 데이터만 변경하면 다양한 영상에 재사용할 수 있습니다.

## 컴포넌트 목록

| 컴포넌트 | 파일 | 주요 기법 |
|----------|------|-----------|
| TitleCard | `src/TitleCard.tsx` | 레이어링, 그라데이션, spring 등장 |
| CounterInfoGraphic | `src/CounterInfoGraphic.tsx` | SVG 원형 게이지, interpolate 카운트업 |
| SequentialList | `src/SequentialList.tsx` | frame-delay 순차 등장, Sequence 장면 전환 |

## 핵심 학습 내용

### 1. Props 재사용 패턴 (Zod 스키마)

```tsx
export const titleCardSchema = z.object({
  title: z.string(),
  subtitle: z.string(),
  gradientFrom: zColor(),
  gradientTo: zColor(),
  accentColor: zColor(),
});
```

- `schema` prop으로 Composition에 등록하면 Studio Props 패널에서 실시간 편집 가능
- 데이터만 교체하여 같은 컴포넌트로 다양한 영상 생성

### 2. 레이어링 (AbsoluteFill 중첩)

```
AbsoluteFill (배경: 그라데이션)
  └── AbsoluteFill (장식: 회전 원)
      └── AbsoluteFill (콘텐츠: 텍스트)
```

### 3. frame-delay 패턴 vs Sequence

- **Sequence**: 전체 화면 교체 (장면 전환)에 사용. 내부적으로 `AbsoluteFill`(absolute position)을 렌더링
- **frame-delay**: 같은 화면 안에서 여러 요소 순차 등장에 사용. flex 레이아웃과 호환

```tsx
// frame-delay 패턴
const itemSpring = spring({
  frame: frame - delay,  // delay만큼 뒤에 시작
  fps,
  config: { damping: 14, stiffness: 100 },
});
```

### 4. SVG 원형 프로그래스바

`stroke-dasharray` + `stroke-dashoffset`으로 원형 게이지 애니메이션 구현.

## 폴더 구조

```
03-Motion-Graphics/
├── README.md                          # 이 파일
├── concepts/
│   ├── css-in-js-for-video.md         # 영상에서의 CSS 스타일링
│   └── reusable-components.md         # 재사용 가능한 컴포넌트 설계
├── examples/
│   ├── title-card/                    # TitleCard 예시 코드 참조
│   ├── counter-infographic/           # CounterInfoGraphic 예시 코드 참조
│   └── sequential-list/              # SequentialList 예시 코드 참조
└── guides/
    └── motion-patterns.md             # 자주 쓰는 모션 패턴 모음
```

## 실행 방법

```bash
cd my-first-video
npm run dev
```

Studio 좌측 사이드바에서 `TitleCard`, `CounterInfoGraphic`, `SequentialList`를 선택하여 확인.

---

**방법론**: CUA_VL (Catch Up AI Vibe Learning)
