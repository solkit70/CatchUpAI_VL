import { AbsoluteFill, Series } from 'remotion';
import {
  SLIDES,
  SECTION_HEADERS,
  AUDIO_DURATIONS,
  SECTION_HEADER_FRAMES,
  SEC,
} from './data';
import { SectionHeader } from './common/SectionHeader';
import { TitleSlide } from './slides/TitleSlide';
import { BulletSlide } from './slides/BulletSlide';
import { CycleSlide } from './slides/CycleSlide';
import { DefinitionSlide } from './slides/DefinitionSlide';
import { WordBreakdownSlide } from './slides/WordBreakdownSlide';
import { WorkflowSlide } from './slides/WorkflowSlide';
import { StepSlide } from './slides/StepSlide';
import { StatSlide } from './slides/StatSlide';
import { TimelineSlide } from './slides/TimelineSlide';
import { CompareSlide } from './slides/CompareSlide';
import { FolderSlide } from './slides/FolderSlide';
import { SummarySlide } from './slides/SummarySlide';
import { OutroSlide } from './slides/OutroSlide';
import type { SlideData } from './data';

// 슬라이드 타입 → 컴포넌트 매핑
const SlideComponent: React.FC<{ data: SlideData; durationInFrames: number }> = ({
  data,
  durationInFrames,
}) => {
  switch (data.type) {
    case 'title':
      return <TitleSlide data={data} durationInFrames={durationInFrames} />;
    case 'bullet':
      return <BulletSlide data={data} durationInFrames={durationInFrames} />;
    case 'cycle':
      return <CycleSlide data={data} durationInFrames={durationInFrames} />;
    case 'definition':
      return <DefinitionSlide data={data} durationInFrames={durationInFrames} />;
    case 'wordbreakdown':
      return <WordBreakdownSlide data={data} durationInFrames={durationInFrames} />;
    case 'workflow':
      return <WorkflowSlide data={data} durationInFrames={durationInFrames} />;
    case 'step':
      return <StepSlide data={data} durationInFrames={durationInFrames} />;
    case 'stat':
      return <StatSlide data={data} durationInFrames={durationInFrames} />;
    case 'timeline':
      return <TimelineSlide data={data} durationInFrames={durationInFrames} />;
    case 'compare':
      return <CompareSlide data={data} durationInFrames={durationInFrames} />;
    case 'folder':
      return <FolderSlide data={data} durationInFrames={durationInFrames} />;
    case 'summary':
      return <SummarySlide data={data} durationInFrames={durationInFrames} />;
    case 'outro':
      return <OutroSlide data={data} durationInFrames={durationInFrames} />;
    default:
      return <BulletSlide data={data} durationInFrames={durationInFrames} />;
  }
};

// 섹션 전환이 필요한 슬라이드 ID 앞에 섹션 헤더 삽입
// Section 2: slide 3 앞, Section 3: slide 6 앞, Section 4: slide 10 앞,
// Section 5: slide 15 앞, Section 6: slide 19 앞
const SECTION_BREAKS_BEFORE: Record<number, number> = {
  3: 0,  // Section 2 header (index 0 in SECTION_HEADERS)
  6: 1,  // Section 3 header
  10: 2, // Section 4 header
  15: 3, // Section 5 header
  19: 4, // Section 6 header
};

export const VibeLearnIntroKR: React.FC = () => {
  // Series.Sequence 목록 구성
  const sequences: Array<{ key: string; frames: number; element: React.ReactNode }> = [];

  for (const slide of SLIDES) {
    // 섹션 전환 헤더 삽입 체크
    if (slide.id in SECTION_BREAKS_BEFORE) {
      const headerIdx = SECTION_BREAKS_BEFORE[slide.id];
      const headerData = SECTION_HEADERS[headerIdx];
      sequences.push({
        key: `section-header-${headerData.section}`,
        frames: SECTION_HEADER_FRAMES,
        element: <SectionHeader data={headerData} />,
      });
    }

    // 슬라이드 추가
    const durationInFrames = SEC(AUDIO_DURATIONS[slide.id]);
    sequences.push({
      key: `slide-${slide.id}`,
      frames: durationInFrames,
      element: <SlideComponent data={slide} durationInFrames={durationInFrames} />,
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
