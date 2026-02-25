import { Composition } from "remotion";
import { HelloWorld, myCompSchema } from "./HelloWorld";
import { Logo, myCompSchema2 } from "./HelloWorld/Logo";
import { FadeInText } from "./FadeInText";
import { SpringBounce } from "./SpringBounce";
import { MultiScene } from "./MultiScene";
import { TitleCard, titleCardSchema } from "./TitleCard";
import { CounterInfoGraphic, counterSchema } from "./CounterInfoGraphic";
import { SequentialList, sequentialListSchema } from "./SequentialList";
import { SkillsHelloWorld, skillsHelloWorldSchema } from "./SkillsHelloWorld";
import { ChannelIntro, channelIntroSchema } from "./ChannelIntro";
import { ExplanationScene, explanationSchema } from "./ExplanationScene";
import { WorkflowScene, workflowSchema } from "./WorkflowScene";
import { OutroScene, outroSchema } from "./OutroScene";
import { VibeLearnIntro, vibeLearnIntroSchema } from "./VibeLearnIntro";
import { ClearlyIntroKr } from "./clearly-kr/ClearlyIntroKr";
import { TOTAL_FRAMES as KR_TOTAL_FRAMES } from "./clearly-kr/slideData";
import { ClearlyIntroEn } from "./clearly-en/ClearlyIntroEn";
import { TOTAL_FRAMES as EN_TOTAL_FRAMES } from "./clearly-en/slideData";

// Each <Composition> is an entry in the sidebar!

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        // You can take the "id" to render a video:
        // npx remotion render HelloWorld
        id="HelloWorld"
        component={HelloWorld}
        durationInFrames={210}
        fps={30}
        width={1920}
        height={1080}
        // You can override these props for each render:
        // https://www.remotion.dev/docs/parametrized-rendering
        schema={myCompSchema}
        defaultProps={{
          titleText: "CatchUp AI",
          titleColor: "#FFFFFF",
          logoColor1: "#FF6B6B",
          logoColor2: "#4ECDC4",
        }}
      />

      {/* Mount any React component to make it show up in the sidebar and work on it individually! */}
      <Composition
        id="OnlyLogo"
        component={Logo}
        durationInFrames={150}
        fps={30}
        width={1920}
        height={1080}
        schema={myCompSchema2}
        defaultProps={{
          logoColor1: "#91dAE2" as const,
          logoColor2: "#86A8E7" as const,
        }}
      />
      {/* M2 실습 1: interpolate 학습용 */}
      <Composition
        id="FadeInText"
        component={FadeInText}
        durationInFrames={120}
        fps={30}
        width={1920}
        height={1080}
      />
      {/* M2 실습 2: spring 바운스 학습용 */}
      <Composition
        id="SpringBounce"
        component={SpringBounce}
        durationInFrames={150}
        fps={30}
        width={1920}
        height={1080}
      />
      {/* M2 실습 3: Sequence 장면 구성 학습용 */}
      <Composition
        id="MultiScene"
        component={MultiScene}
        durationInFrames={300}
        fps={30}
        width={1920}
        height={1080}
      />
      {/* M3 실습 1: 재사용 가능한 타이틀 카드 */}
      <Composition
        id="TitleCard"
        component={TitleCard}
        durationInFrames={120}
        fps={30}
        width={1920}
        height={1080}
        schema={titleCardSchema}
        defaultProps={{
          title: "Remotion으로 만드는 영상 제작!!!",
          subtitle: "코드 한 줄로 시작하는 모션그래픽의 세계",
          gradientFrom: "#667eea",
          gradientTo: "#764ba2",
          accentColor: "#FFD700",
        }}
      />
      {/* M3 실습 2: 숫자 카운트업 인포그래픽 */}
      <Composition
        id="CounterInfoGraphic"
        component={CounterInfoGraphic}
        durationInFrames={180}
        fps={30}
        width={1920}
        height={1080}
        schema={counterSchema}
        defaultProps={{
          heading: "CatchUp AI 채널 성과",
          stats: [
            { label: "구독자", value: 85, suffix: "K", color: "#FF6B6B" },
            { label: "영상 수", value: 42, suffix: "개", color: "#4ECDC4" },
            { label: "총 조회수", value: 95, suffix: "만", color: "#A78BFA" },
          ],
        }}
      />
      {/* M3 실습 3: 순차 등장 리스트 */}
      <Composition
        id="SequentialList"
        component={SequentialList}
        durationInFrames={300}
        fps={30}
        width={1920}
        height={1080}
        schema={sequentialListSchema}
        defaultProps={{
          heading: "Remotion을 배워야 하는 5가지 이유",
          items: [
            { icon: "\u{1F3AC}", text: "코드로 영상을 만들어 버전 관리 가능" },
            { icon: "\u{1F504}", text: "데이터만 바꾸면 영상이 자동 생성" },
            { icon: "\u{26A1}", text: "React 지식으로 바로 시작 가능" },
            { icon: "\u{1F916}", text: "AI와 협업하여 빠르게 제작" },
            { icon: "\u{1F3AF}", text: "유튜브 모션그래픽에 최적화" },
          ],
          accentColor: "#4ECDC4",
          summary: "가지 이유로 Remotion을 추천합니다",
        }}
      />
      {/* M4 실습 1: Skills로 생성한 첫 AI 영상 */}
      <Composition
        id="SkillsHelloWorld"
        component={SkillsHelloWorld}
        durationInFrames={300}
        fps={30}
        width={1920}
        height={1080}
        schema={skillsHelloWorldSchema}
        defaultProps={{
          text: "Hello World 나는 Catch Up AI야!!!",
          textColor: "#FFFFFF",
          backgroundColor: "#2563EB",
        }}
      />
      {/* M4 실습 2: 채널 인트로 (반복 개선) */}
      <Composition
        id="ChannelIntro"
        component={ChannelIntro}
        durationInFrames={150}
        fps={30}
        width={1920}
        height={1080}
        schema={channelIntroSchema}
        defaultProps={{
          channelName: "Catch Up AI",
          tagline: "AI와 함께 배우는 개발의 모든 것",
          subscribeText: "구독하기",
          bgColor: "#1a1a2e",
          accentColor: "#FFD700",
        }}
      />
      {/* M4 실습 3: 설명 영상 장면 (Series 패턴) */}
      <Composition
        id="ExplanationScene"
        component={ExplanationScene}
        durationInFrames={450}
        fps={30}
        width={1920}
        height={1080}
        schema={explanationSchema}
        defaultProps={{
          heading: "AI 학습의 3가지 핵심 원칙",
          points: [
            {
              icon: "\u{1F4A1}",
              title: "실습 우선",
              description:
                "이론 20%, 실습 80%로 배우면 기억에 오래 남습니다",
            },
            {
              icon: "\u{1F4DD}",
              title: "기록을 남겨라",
              description:
                "WorkLog로 매일 학습 과정을 기록하고 다음 학습자를 위한 교과서를 만듭니다",
            },
            {
              icon: "\u{1F91D}",
              title: "AI와 협업",
              description:
                "AI를 학습 파트너로 활용하여 효율적으로 배우고 빠르게 성장합니다",
            },
          ],
          accentColor: "#4ECDC4",
          bgColor: "#1a1a2e",
        }}
      />
      {/* M6 개별 장면: 워크플로우 */}
      <Composition
        id="WorkflowScene"
        component={WorkflowScene}
        durationInFrames={360}
        fps={30}
        width={1920}
        height={1080}
        schema={workflowSchema}
        defaultProps={{
          title: "학습 워크플로우",
          steps: [
            { emoji: "📋", label: "Topic\n설정" },
            { emoji: "🗺️", label: "Roadmap\n생성" },
            { emoji: "📝", label: "일일\n학습" },
            { emoji: "📊", label: "WorkLog\n기록" },
            { emoji: "🔄", label: "회고 &\n개선" },
          ],
          accentColor: "#4ECDC4",
          bgColor: "#1a1a2e",
        }}
      />
      {/* M6 개별 장면: 아웃트로 */}
      <Composition
        id="OutroScene"
        component={OutroScene}
        durationInFrames={150}
        fps={30}
        width={1920}
        height={1080}
        schema={outroSchema}
        defaultProps={{
          channelName: "Catch Up AI",
          message: "VibeLearn AI로 함께 배워봐요!",
          subscribeText: "구독하기",
          accentColor: "#FFD700",
          bgColor: "#1a1a2e",
        }}
      />
      {/* M6 Capstone: VibeLearn AI 소개 영상 (전체 통합) */}
      <Composition
        id="VibeLearnIntro"
        component={VibeLearnIntro}
        durationInFrames={1380}
        fps={30}
        width={1920}
        height={1080}
        schema={vibeLearnIntroSchema}
        defaultProps={{
          accentColor: "#FFD700",
          bgColor: "#1a1a2e",
        }}
      />
      {/* M3 산출물: Clearly App 소개 영상 (한국어) — Remotion 버전 */}
      <Composition
        id="ClearlyIntroKr"
        component={ClearlyIntroKr}
        durationInFrames={KR_TOTAL_FRAMES}
        fps={30}
        width={1920}
        height={1080}
      />
      {/* M3 산출물: Clearly App Introduction (English) — Remotion version */}
      <Composition
        id="ClearlyIntroEn"
        component={ClearlyIntroEn}
        durationInFrames={EN_TOTAL_FRAMES}
        fps={30}
        width={1920}
        height={1080}
      />
    </>
  );
};
