import {
  AbsoluteFill,
  Audio,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
  interpolate,
  spring,
} from 'remotion';
import { COLORS, SECTION_COLORS } from '../data';
import { AnimatedBgV2 } from '../common/AnimatedBgV2';
import type { SlideData } from '../data';

// 파티클 데이터 (20개)
const PARTICLES = Array.from({ length: 20 }, (_, i) => ({
  angle: (i / 20) * Math.PI * 2,
  distance: 300 + (i % 4) * 60,
  size: 3 + (i % 5),
  delay: i * 4,
}));

// Phase 2: 학습 분야 아이콘 (9개)
const FIELD_ICONS = [
  { emoji: '💻', label: 'Python/JS' },
  { emoji: '🤖', label: 'AI/ML' },
  { emoji: '⚛️', label: 'React' },
  { emoji: '📊', label: '데이터 분석' },
  { emoji: '🎨', label: 'UI/UX' },
  { emoji: '🌍', label: '외국어' },
  { emoji: '📈', label: 'SQL/통계' },
  { emoji: '🎬', label: '영상 제작' },
  { emoji: '🎓', label: '분야 무관' },
];

interface TitleSlideV2Props {
  data: SlideData;
  durationInFrames: number;
}

export const TitleSlideV2: React.FC<TitleSlideV2Props> = ({ data, durationInFrames }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // ─── Phase 경계 (30fps 기준) ─────────────────
  const P2_START = fps * 8; // 240
  const P2_END = fps * 18;  // 540
  const P3_START = fps * 18; // 540
  const P3_END = fps * 28;  // 840
  const P4_START = fps * 28; // 840

  // Phase 1: 파티클 + 채널명 + 타이틀 + 서브타이틀
  const channelChars = (data.content || '').split('');
  const channelReveal = Math.min(channelChars.length, Math.max(0, Math.floor((frame - 10) / 3)));
  const titleSpring = spring({ frame: frame - 30, fps, config: { damping: 14, stiffness: 80 } });
  const titleOpacity = interpolate(frame, [30, 60], [0, 1], { extrapolateRight: 'clamp' });
  const subOpacity = interpolate(frame, [60, 90], [0, 1], { extrapolateRight: 'clamp' });

  // 제목 지속 glow pulse (3초 주기)
  const titleGlow = 30 + Math.sin((frame / fps) * (Math.PI * 2 / 3)) * 20;

  // Phase 2: 학습 분야 아이콘 (8~18초)
  const p2Opacity = interpolate(frame, [P2_START, P2_START + 30], [0, 1], { extrapolateRight: 'clamp' });
  const p2FadeOut = interpolate(frame, [P2_END - 20, P2_END], [1, 0], { extrapolateRight: 'clamp' });

  // Phase 3: 통계 카운터 (18~28초)
  const p3Opacity = interpolate(frame, [P3_START, P3_START + 30], [0, 1], { extrapolateRight: 'clamp' });
  const p3FadeOut = interpolate(frame, [P3_END - 20, P3_END], [1, 0], { extrapolateRight: 'clamp' });

  const hoursCount = interpolate(frame - P3_START - 30, [0, 90], [0, 9.5], { extrapolateRight: 'clamp' });
  const outputsCount = Math.floor(interpolate(frame - P3_START - 30, [0, 90], [0, 22], { extrapolateRight: 'clamp' }));

  // Phase 4: CTA (28~34초)
  const p4Opacity = interpolate(frame, [P4_START, P4_START + 30], [0, 1], { extrapolateRight: 'clamp' });

  // 전체 페이드아웃
  const fadeOut = interpolate(frame, [durationInFrames - 20, durationInFrames], [1, 0], {
    extrapolateRight: 'clamp',
  });

  const isPhase2 = frame >= P2_START && frame < P2_END;
  const isPhase3 = frame >= P3_START && frame < P3_END;
  const isPhase4 = frame >= P4_START;

  return (
    <AbsoluteFill style={{ opacity: fadeOut }}>
      <AnimatedBgV2 sectionColor={SECTION_COLORS.intro} intensity={0.5} />

      {/* 파티클 폭발 (Phase 1) */}
      <AbsoluteFill>
        <svg width="100%" height="100%" viewBox="0 0 1920 1080" style={{ position: 'absolute' }}>
          {PARTICLES.map((p, i) => {
            const progress = spring({ frame: frame - p.delay, fps, config: { damping: 20, stiffness: 60 } });
            const x = 960 + Math.cos(p.angle) * p.distance * progress;
            const y = 540 + Math.sin(p.angle) * p.distance * progress;
            const particleOpacity = interpolate(progress, [0, 0.2, 0.8, 1], [0, 1, 1, 0]);
            return (
              <circle key={i} cx={x} cy={y} r={p.size} fill={COLORS.primary} opacity={particleOpacity} />
            );
          })}
        </svg>
      </AbsoluteFill>

      {/* Phase 1: 채널명 + 타이틀 + 서브타이틀 */}
      <AbsoluteFill
        style={{
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          justifyContent: 'center',
          gap: 20,
        }}
      >
        {/* 채널명 타이핑 */}
        <div
          style={{
            fontSize: 20,
            color: COLORS.primary,
            letterSpacing: 8,
            fontFamily: 'sans-serif',
            fontWeight: 600,
            textTransform: 'uppercase',
          }}
        >
          {channelChars.slice(0, channelReveal).join('')}
          {channelReveal < channelChars.length && (
            <span style={{ opacity: frame % 20 < 10 ? 1 : 0 }}>|</span>
          )}
        </div>

        {/* 구분선 */}
        <div
          style={{
            width: `${titleSpring * 400}px`,
            height: 2,
            background: `linear-gradient(90deg, transparent, ${COLORS.primary}, transparent)`,
          }}
        />

        {/* 메인 타이틀 (지속 glow pulse) */}
        <div
          style={{
            fontSize: 88,
            fontWeight: 900,
            color: COLORS.text,
            fontFamily: 'sans-serif',
            textAlign: 'center',
            lineHeight: 1.1,
            opacity: titleOpacity,
            transform: `scale(${0.7 + titleSpring * 0.3})`,
            textShadow: `0 0 ${titleGlow}px ${COLORS.primary}66`,
          }}
        >
          {data.title}
        </div>

        {/* 서브타이틀 */}
        <div
          style={{
            fontSize: 28,
            color: COLORS.textMuted,
            fontFamily: 'sans-serif',
            textAlign: 'center',
            fontWeight: 400,
            maxWidth: 800,
            opacity: subOpacity,
            transform: `translateY(${interpolate(frame, [60, 90], [20, 0], { extrapolateRight: 'clamp' })}px)`,
          }}
        >
          {data.sub}
        </div>

        {/* 하단 데코 라인 */}
        <div style={{ display: 'flex', gap: 8, marginTop: 8, opacity: subOpacity }}>
          {[COLORS.primary, COLORS.accent, COLORS.coral].map((c, i) => (
            <div key={i} style={{ width: 40, height: 3, background: c, borderRadius: 2, boxShadow: `0 0 8px ${c}` }} />
          ))}
        </div>

        {/* 슬라이드 번호 표시 */}
        <div
          style={{
            position: 'absolute',
            top: 40,
            right: 60,
            fontSize: 16,
            color: COLORS.textMuted,
            fontFamily: 'monospace',
            opacity: subOpacity,
          }}
        >
          1 / 24
        </div>
      </AbsoluteFill>

      {/* ─── Phase 2: 학습 분야 아이콘 그리드 (8~18초) ─── */}
      {(isPhase2 || isPhase3 || isPhase4) && (
        <AbsoluteFill
          style={{
            opacity: isPhase2 ? p2Opacity * p2FadeOut : isPhase3 ? p3FadeOut * 0 : 0,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            justifyContent: 'flex-end',
            paddingBottom: 80,
            gap: 24,
          }}
        >
          <div style={{ opacity: p2Opacity * (isPhase2 ? p2FadeOut : 0) }}>
            <div style={{ fontSize: 18, color: COLORS.accent, fontFamily: 'sans-serif', textAlign: 'center', marginBottom: 24, letterSpacing: 2 }}>
              어떤 주제에도 적용 가능합니다
            </div>
            <div style={{ display: 'flex', gap: 20, flexWrap: 'wrap', justifyContent: 'center', maxWidth: 1400 }}>
              {FIELD_ICONS.map((icon, i) => {
                const iconDelay = P2_START + i * 15;
                const iconOpacity = interpolate(frame - iconDelay, [0, 20], [0, 1], { extrapolateRight: 'clamp' });
                const iconSpring = spring({ frame: frame - iconDelay, fps, config: { damping: 14, stiffness: 100 } });
                return (
                  <div
                    key={i}
                    style={{
                      display: 'flex',
                      flexDirection: 'column',
                      alignItems: 'center',
                      gap: 8,
                      padding: '16px 20px',
                      background: `${COLORS.primary}15`,
                      border: `1px solid ${COLORS.primary}44`,
                      borderRadius: 12,
                      opacity: iconOpacity,
                      transform: `scale(${0.5 + iconSpring * 0.5})`,
                      minWidth: 110,
                    }}
                  >
                    <span style={{ fontSize: 28 }}>{icon.emoji}</span>
                    <span style={{ fontSize: 13, color: COLORS.textMuted, fontFamily: 'sans-serif' }}>{icon.label}</span>
                  </div>
                );
              })}
            </div>
          </div>
        </AbsoluteFill>
      )}

      {/* ─── Phase 3: 케이스 수치 카운터 (18~28초) ─── */}
      {isPhase3 && (
        <AbsoluteFill
          style={{
            opacity: p3Opacity * p3FadeOut,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            justifyContent: 'flex-end',
            paddingBottom: 80,
            gap: 24,
          }}
        >
          <div style={{ fontSize: 18, color: COLORS.accent, fontFamily: 'sans-serif', letterSpacing: 2, marginBottom: 8 }}>
            실제 케이스 — Clearly 앱 학습
          </div>
          <div style={{ display: 'flex', gap: 60, alignItems: 'center' }}>
            {/* 9.5h */}
            <div style={{ textAlign: 'center' }}>
              <div style={{ fontSize: 72, fontWeight: 900, color: COLORS.primary, fontFamily: 'sans-serif', lineHeight: 1, textShadow: `0 0 30px ${COLORS.primary}66` }}>
                {hoursCount.toFixed(1)}
                <span style={{ fontSize: 32, color: COLORS.textMuted }}>h</span>
              </div>
              <div style={{ fontSize: 18, color: COLORS.textMuted, fontFamily: 'sans-serif', marginTop: 8 }}>총 학습 시간</div>
            </div>

            <div style={{ width: 2, height: 80, background: `linear-gradient(to bottom, transparent, ${COLORS.accent}, transparent)` }} />

            {/* 22개 */}
            <div style={{ textAlign: 'center' }}>
              <div style={{ fontSize: 72, fontWeight: 900, color: COLORS.accent, fontFamily: 'sans-serif', lineHeight: 1, textShadow: `0 0 30px ${COLORS.accent}66` }}>
                {outputsCount}
                <span style={{ fontSize: 32, color: COLORS.textMuted }}>개</span>
              </div>
              <div style={{ fontSize: 18, color: COLORS.textMuted, fontFamily: 'sans-serif', marginTop: 8 }}>생성된 산출물</div>
            </div>

            <div style={{ width: 2, height: 80, background: `linear-gradient(to bottom, transparent, ${COLORS.green}, transparent)` }} />

            {/* YouTube 영상 */}
            <div style={{ textAlign: 'center' }}>
              <div style={{ fontSize: 72, fontWeight: 900, color: COLORS.green, fontFamily: 'sans-serif', lineHeight: 1, textShadow: `0 0 30px ${COLORS.green}66` }}>
                2<span style={{ fontSize: 32, color: COLORS.textMuted }}>개</span>
              </div>
              <div style={{ fontSize: 18, color: COLORS.textMuted, fontFamily: 'sans-serif', marginTop: 8 }}>YouTube 영상</div>
            </div>
          </div>
        </AbsoluteFill>
      )}

      {/* ─── Phase 4: GitHub CTA (28~34초) ─── */}
      {isPhase4 && (
        <AbsoluteFill
          style={{
            opacity: p4Opacity,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            justifyContent: 'flex-end',
            paddingBottom: 80,
            gap: 20,
          }}
        >
          <div style={{ fontSize: 16, color: COLORS.textMuted, fontFamily: 'sans-serif', letterSpacing: 2 }}>
            지금 바로 시작하세요
          </div>
          <div
            style={{
              background: `linear-gradient(135deg, ${COLORS.primary}33, ${COLORS.accent}22)`,
              border: `2px solid ${COLORS.primary}`,
              borderRadius: 16,
              padding: '16px 48px',
              fontSize: 22,
              fontWeight: 700,
              color: COLORS.primary,
              fontFamily: 'monospace',
              boxShadow: `0 0 ${20 + Math.sin(frame * 0.1) * 10}px ${COLORS.primary}44`,
            }}
          >
            🔗 github.com/solkit70/VibeLearn-AI
          </div>
          <div style={{ fontSize: 18, color: COLORS.textMuted, fontFamily: 'sans-serif' }}>
            무료 · 오픈소스 · 어떤 AI 도구에서도 사용 가능
          </div>
        </AbsoluteFill>
      )}

      <Audio src={staticFile(data.audioSrc)} />
    </AbsoluteFill>
  );
};
