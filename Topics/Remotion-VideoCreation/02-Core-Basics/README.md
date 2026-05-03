# M2 - Remotion Core 기초

**학습일**: 2026-02-06
**Topic**: Remotion-VideoCreation
**예상 시간**: 4h / **실제 소요**: ~2h

---

## 📖 학습 순서

이 폴더를 처음 여는 분은 아래 순서대로 읽으세요.

| 순서 | 문서 | 설명 |
|------|------|------|
| 1 | [concepts/animation-basics.md](concepts/animation-basics.md) | 핵심 애니메이션 API 개념 (interpolate, spring, Sequence) |
| 2 | [guides/animation-cheatsheet.md](guides/animation-cheatsheet.md) | 애니메이션 치트시트 (자주 쓰는 패턴 모음) |
| 3 | [concepts/calculate-metadata.md](concepts/calculate-metadata.md) | calculateMetadata — 동적 영상 길이·Props 설정 ✨NEW |

**이전 모듈**: [01-Setup](../01-Setup/) | **다음 모듈**: [03-Motion-Graphics](../03-Motion-Graphics/)

---

## 학습 내용 요약

Remotion Core의 3대 핵심 API를 실습을 통해 학습했습니다:

1. **interpolate()** - 프레임 기반 선형 애니메이션
2. **spring()** - 물리 기반 자연스러운 애니메이션
3. **Sequence** - 장면 시간 배치

---

## 실습 결과물

### 1. FadeInText (interpolate 학습)
- **파일**: `my-first-video/src/FadeInText.tsx`
- **효과**: 텍스트 페이드인 + 슬라이드업 + 딜레이 부제목 + 페이드아웃
- **핵심**: `interpolate(frame, [시작, 끝], [출력시작, 출력끝], { clamp })`

### 2. SpringBounce (spring 학습)
- **파일**: `my-first-video/src/SpringBounce.tsx`
- **효과**: 3개 박스가 각각 다른 damping으로 바운스 등장
- **핵심**: `spring({ frame, fps, config: { damping, stiffness, mass } })`
- **발견**: damping이 낮을수록 많이 바운스, 높으면 안정적

### 3. MultiScene (Sequence 학습)
- **파일**: `my-first-video/src/MultiScene.tsx`
- **효과**: 인트로 → 포인트 설명 → 아웃트로 (3장면, 10초)
- **핵심**: `<Sequence from={프레임} durationInFrames={길이}>`
- **발견**: Sequence 안에서 useCurrentFrame()은 0부터 시작 (로컬 시간)

---

## 핵심 개념 정리

| API | 용도 | 특징 |
|-----|------|------|
| `interpolate()` | 정밀한 값 변환 | 선형적, 입출력 범위 직접 지정 |
| `spring()` | 자연스러운 모션 | 물리 기반, 0→1 변화, 파라미터 조절 |
| `Sequence` | 장면 시간 배치 | from으로 시작 시점, 자식은 로컬 시간 |
| `calculateMetadata` | 동적 Composition 설정 | 오디오 길이 자동 계산, 외부 데이터 로딩 |
| `useDelayRender` | 비동기 렌더링 대기 | 데이터 로딩 완료 후 렌더링 시작 |

## ✨ 추가된 개념 (2026-04 업데이트)

### calculateMetadata
Composition이 렌더링되기 전에 실행되는 비동기 함수. 오디오 파일 길이를 읽어 영상 길이를 자동으로 맞추는 데 활용:

```tsx
const calculateMetadata: CalculateMetadataFunction<Props> = async ({ props }) => {
  const dur = await getAudioDurationInSeconds(staticFile(props.audioSrc));
  return { durationInFrames: Math.ceil(dur * 30) + 36 }; // +1.2s 패딩
};
```

→ 상세 가이드: [concepts/calculate-metadata.md](concepts/calculate-metadata.md)

## 참조 자료

- 개념 정리: `concepts/animation-basics.md`
- 애니메이션 치트시트: `guides/animation-cheatsheet.md`
- Remotion 공식 문서: https://www.remotion.dev/docs/animating-properties
