import { AbsoluteFill, Series } from 'remotion';
import {
  SLIDES,
  SECTION_HEADERS,
  AUDIO_DURATIONS,
  SECTION_HEADER_FRAMES,
  SECTION_COLORS,
  SEC,
} from './data';
import { SectionHeader } from './common/SectionHeader';
import { FloatingKeywords } from './common/FloatingKeywords';
import { ProgressBar } from './common/ProgressBar';
import { TitleSlideV2 } from './slides/TitleSlideV2';
import { BulletSlideV2 } from './slides/BulletSlideV2';
import { CycleSlide } from './slides/CycleSlide';
import { DefinitionSlideV2 } from './slides/DefinitionSlideV2';
import { WordBreakdownSlide } from './slides/WordBreakdownSlide';
import { WorkflowSlide } from './slides/WorkflowSlide';
import { StepSlideV2 } from './slides/StepSlideV2';
import { StatSlide } from './slides/StatSlide';
import { TimelineSlide } from './slides/TimelineSlide';
import { CompareSlideV2 } from './slides/CompareSlideV2';
import { FolderSlide } from './slides/FolderSlide';
import { SummarySlide } from './slides/SummarySlide';
import { OutroSlide } from './slides/OutroSlide';
import type { SlideData } from './data';

// 슬라이드 타입 → v2 컴포넌트 매핑
const SlideComponent: React.FC<{ data: SlideData; durationInFrames: number }> = ({
  data,
  durationInFrames,
}) => {
  switch (data.type) {
    case 'title':
      return <TitleSlideV2 data={data} durationInFrames={durationInFrames} />;
    case 'bullet':
      return <BulletSlideV2 data={data} durationInFrames={durationInFrames} />;
    case 'cycle':
      return <CycleSlide data={data} durationInFrames={durationInFrames} />;
    case 'definition':
      return <DefinitionSlideV2 data={data} durationInFrames={durationInFrames} />;
    case 'wordbreakdown':
      return <WordBreakdownSlide data={data} durationInFrames={durationInFrames} />;
    case 'workflow':
      return <WorkflowSlide data={data} durationInFrames={durationInFrames} />;
    case 'step':
      return <StepSlideV2 data={data} durationInFrames={durationInFrames} />;
    case 'stat':
      return <StatSlide data={data} durationInFrames={durationInFrames} />;
    case 'timeline':
      return <TimelineSlide data={data} durationInFrames={durationInFrames} />;
    case 'compare':
      return <CompareSlideV2 data={data} durationInFrames={durationInFrames} />;
    case 'folder':
      return <FolderSlide data={data} durationInFrames={durationInFrames} />;
    case 'summary':
      return <SummarySlide data={data} durationInFrames={durationInFrames} />;
    case 'outro':
      return <OutroSlide data={data} durationInFrames={durationInFrames} />;
    default:
      return <BulletSlideV2 data={data} durationInFrames={durationInFrames} />;
  }
};

// 섹션 전환이 필요한 슬라이드 ID 앞에 섹션 헤더 삽입
const SECTION_BREAKS_BEFORE: Record<number, number> = {
  3: 0,  // Section 2 header (index 0)
  6: 1,  // Section 3 header
  10: 2, // Section 4 header
  15: 3, // Section 5 header
  19: 4, // Section 6 header
};

// 슬라이드 section → accent 색상
const SECTION_ACCENT: Record<number, string> = {
  1: SECTION_COLORS.intro,
  2: SECTION_COLORS.problem,
  3: SECTION_COLORS.intro2,
  4: SECTION_COLORS.howto,
  5: SECTION_COLORS.casestudy,
  6: SECTION_COLORS.outro,
};

// FloatingKeywords + ProgressBar 공통 오버레이를 포함한 슬라이드 래퍼
const SlideWithOverlays: React.FC<{
  children: React.ReactNode;
  durationInFrames: number;
  sectionColor: string;
}> = ({ children, durationInFrames, sectionColor }) => (
  <AbsoluteFill>
    {children}
    <FloatingKeywords sectionColor={sectionColor} />
    <ProgressBar durationInFrames={durationInFrames} color={sectionColor} />
  </AbsoluteFill>
);

export const VibeLearnIntroKRv2: React.FC = () => {
  const sequences: Array<{ key: string; frames: number; element: React.ReactNode }> = [];

  for (const slide of SLIDES) {
    // 섹션 전환 헤더 삽입
    if (slide.id in SECTION_BREAKS_BEFORE) {
      const headerIdx = SECTION_BREAKS_BEFORE[slide.id];
      const headerData = SECTION_HEADERS[headerIdx];
      sequences.push({
        key: `section-header-${headerData.section}`,
        frames: SECTION_HEADER_FRAMES,
        element: (
          <SlideWithOverlays durationInFrames={SECTION_HEADER_FRAMES} sectionColor={headerData.color}>
            <SectionHeader data={headerData} />
          </SlideWithOverlays>
        ),
      });
    }

    // 슬라이드 추가
    const durationInFrames = SEC(AUDIO_DURATIONS[slide.id]);
    const sectionColor = SECTION_ACCENT[slide.section] || SECTION_COLORS.intro;

    sequences.push({
      key: `slide-${slide.id}`,
      frames: durationInFrames,
      element: (
        <SlideWithOverlays durationInFrames={durationInFrames} sectionColor={sectionColor}>
          <SlideComponent data={slide} durationInFrames={durationInFrames} />
        </SlideWithOverlays>
      ),
    });
  }

  return (
    <AbsoluteFill>
      <Series>
        {sequences.map((seq) => (
          <Series.Sequence key={seq.key} durationInFrames={seq.frames}>
            {seq.element}
          </Series.Sequence>
        ))}
      </Series>
    </AbsoluteFill>
  );
};
