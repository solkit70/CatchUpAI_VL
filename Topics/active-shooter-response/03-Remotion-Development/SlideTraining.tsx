import React from 'react';
import {
  AbsoluteFill,
  interpolate,
  spring,
  useCurrentFrame,
  useVideoConfig,
} from 'remotion';

// VibeLearn AI v2.1 Learning Artifact - SlideTraining (SlideCompare) Component
//
// 이 특화 컴포넌트는 시민단체를 위한 공인 재난 대처 교육과정(FEMA, CRASE, ALICE) 3종을
// 3열 Glassmorphism 카드로 렌더링하며, Spring 기반의 Stagger 등장과 Spotlight 포커스 연쇄 애니메이션을 수행합니다.

interface SlideTrainingProps {
  data: {
    id: string;
    title?: string;
    eyebrow?: string;
    lines?: Array<{ text: string }>;
    spec?: {
      badgeText?: string;
      headers?: string[];
      rows?: string[][];
    };
  };
  durationInFrames: number;
}

export const SlideTraining: React.FC<SlideTrainingProps> = ({ data }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const spec = data.spec || {};
  const rows = spec.rows || [];
  const badgeText = spec.badgeText || '전문 안전 자격 획득';

  // 1. Spring 및 Stagger 딜레이 기본 파라미터 선언
  const baseDelay = 20;
  const staggerInterval = 18;

  // 2. 카드 전체가 등장하는 최종 프레임 계산 (이후 Spotlight 구동)
  const allAppearedFrame = baseDelay + rows.length * staggerInterval + 25;
  const cycleFrames = 60; // 2.0초(60프레임) 단위로 Spotlight 이동

  const activeIdx = frame >= allAppearedFrame
    ? Math.floor((frame - allAppearedFrame) / cycleFrames) % rows.length
    : -1;

  // 3. 타이틀 진입 애니메이션 (Spring)
  const titleSp = spring({ frame, fps, config: { damping: 16, stiffness: 90 } });
  const lineW = interpolate(frame, [10, 32], [0, 160], { extrapolateRight: 'clamp' });

  return (
    <AbsoluteFill
      style={{
        position: 'absolute',
        inset: 0,
        padding: '80px 110px 80px',
        display: 'flex',
        flexDirection: 'column',
        fontFamily: "'Pretendard', 'Noto Sans KR', sans-serif",
        color: '#F0F6FC',
        wordBreak: 'keep-all',
      }}
    >
      {/* ─── 상단 헤더 영역 ─── */}
      <div style={{ marginBottom: 36, display: 'flex', flexDirection: 'column' }}>
        <div style={{ display: 'flex', gap: 12, alignItems: 'center', marginBottom: 12 }}>
          {data.eyebrow ? (
            <span
              style={{
                fontSize: 24,
                fontWeight: 800,
                color: '#8B949E',
                letterSpacing: '1.5px',
              }}
            >
              {data.eyebrow}
            </span>
          ) : null}
          <span style={{ color: '#4F565E', fontSize: 20 }}>|</span>
          <span
            style={{
              padding: '4px 14px',
              borderRadius: 8,
              background: 'rgba(24, 144, 255, 0.15)',
              border: '1.5px solid rgba(24, 144, 255, 0.5)',
              color: '#1890ff',
              fontSize: 20,
              fontWeight: 800,
            }}
          >
            {badgeText}
          </span>
        </div>

        <h2
          style={{
            margin: 0,
            fontSize: 54,
            fontWeight: 900,
            lineHeight: 1.25,
            transform: `translateY(${interpolate(titleSp, [0, 1], [24, 0])}px)`,
            opacity: titleSp,
          }}
        >
          {data.title}
        </h2>

        <div
          style={{
            width: lineW,
            height: 6,
            borderRadius: 3,
            background: 'linear-gradient(90deg, #1890ff, rgba(24, 144, 255, 0.2))',
            marginTop: 14,
          }}
        />
      </div>

      {/* ─── 3열 Glassmorphism 그리드 ─── */}
      <div
        style={{
          flex: 1,
          display: 'flex',
          gap: 28,
          alignItems: 'stretch',
          justifyContent: 'center',
          marginTop: 16,
        }}
      >
        {rows.map((row, i) => {
          const delay = baseDelay + i * staggerInterval;
          // 각 카드별 물리 튀어오름 Spring
          const cardSp = spring({
            frame: frame - delay,
            fps,
            config: { damping: 18, stiffness: 100 },
          });

          const isActive = activeIdx === i;
          const cardAccent = '#1890ff'; // FEMA Blue 색상

          return (
            <div
              key={i}
              style={{
                flex: 1,
                display: 'flex',
                flexDirection: 'column',
                padding: '36px 30px',
                borderRadius: 16,
                background: 'rgba(33, 38, 45, 0.70)',
                backdropFilter: 'blur(12px)',
                border: `2px solid ${isActive ? cardAccent : 'rgba(240, 246, 252, 0.1)'}`,
                boxShadow: isActive
                  ? `0 0 ${24 + Math.sin(frame * 0.25) * 8}px rgba(24, 144, 255, 0.35)`
                  : '0 8px 32px rgba(0, 0, 0, 0.2)',
                transform: `translateY(${interpolate(cardSp, [0, 1], [48, 0])}px) scale(${isActive ? 1.04 : 1})`,
                opacity: interpolate(cardSp, [0, 0.3], [0, 1], { extrapolateRight: 'clamp' }),
                transition: 'border 0.2s, box-shadow 0.2s, transform 0.2s',
                position: 'relative',
                overflow: 'hidden',
              }}
            >
              {/* 교육 경로 및 플랫폼 URL */}
              <div
                style={{
                  fontSize: 18,
                  fontWeight: 800,
                  color: '#FF9F43',
                  letterSpacing: '1px',
                  textTransform: 'uppercase',
                  marginBottom: 12,
                }}
              >
                {row[1]}
              </div>

              {/* 교육 프로그램 제목 */}
              <h3
                style={{
                  margin: '0 0 20px',
                  fontSize: 34,
                  fontWeight: 900,
                  lineHeight: 1.3,
                  color: '#F0F6FC',
                }}
              >
                {row[0]}
              </h3>

              {/* 가로 단절선 */}
              <div
                style={{
                  width: 44,
                  height: 4,
                  background: cardAccent,
                  borderRadius: 2,
                  marginBottom: 20,
                }}
              />

              {/* 상세 특징 구문 */}
              <p
                style={{
                  margin: 0,
                  fontSize: 22,
                  fontWeight: 500,
                  lineHeight: 1.6,
                  color: '#8B949E',
                }}
              >
                {row[2]}
              </p>

              {/* Spotlight Active 코너 비콘 */}
              {isActive ? (
                <div
                  style={{
                    position: 'absolute',
                    top: 16,
                    right: 16,
                    width: 10,
                    height: 10,
                    borderRadius: '50%',
                    backgroundColor: cardAccent,
                    boxShadow: `0 0 12px ${cardAccent}`,
                  }}
                />
              ) : null}
            </div>
          );
        })}
      </div>

      {/* ─── 하단 툴팁/경고 구문 연출 ─── */}
      {data.lines && data.lines.length > 0 ? (
        <div
          style={{
            marginTop: 24,
            alignSelf: 'center',
            padding: '12px 28px',
            borderRadius: 12,
            background: 'rgba(24, 144, 255, 0.1)',
            border: '1.5px dashed rgba(24, 144, 255, 0.6)',
            fontSize: 22,
            fontWeight: 600,
            color: '#F0F6FC',
            opacity: interpolate(frame, [allAppearedFrame - 10, allAppearedFrame + 10], [0, 1], {
              extrapolateLeft: 'clamp',
              extrapolateRight: 'clamp',
            }),
          }}
        >
          💡 {data.lines[0].text}
        </div>
      ) : null}
    </AbsoluteFill>
  );
};
