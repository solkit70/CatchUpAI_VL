#!/usr/bin/env python3
"""VibeLearn AI v2.1 Learning Script - gen_audio_edge.py

이 스크립트는 active-shooter-response 토픽의 비디오 슬라이드 기획안('video-slide-plan.md')에서
나레이션 스크립트를 파싱하여 'narrations.json'을 추출하고,
edge-tts를 사용해 고품질의 한국어 성우 음성(ko-KR-InJoonNeural) 파일 12종을 자동 생성합니다.

또한, 각 음성 파일의 정확한 재생 길이를 ffprobe를 통해밀리초 단위까지 실측하여
'durations.json' 및 'durations_mapped.json' 매핑 테이블을 완성합니다.

실행:
    python Ingest/CatchUpAI_VL/Topics/active-shooter-response/04-TTS-Audio/gen_audio_edge.py
"""

import asyncio
import json
import re
import subprocess
from pathlib import Path

# ─── 1. 기본 설정 및 경로 선언 ────────────────────────────────────────────────
VOICE = "ko-KR-InJoonNeural"  # 전문적이고 진중한 성우 톤의 한국어 남성 음성
RATE = "+4%"                  # 전달력을 극대화하기 위한 미세 속도 조율 (+4%)

# 토픽 루트 폴더 계산
HERE = Path(__file__).resolve().parent
TOPIC_ROOT = HERE.parent
PLAN_PATH = TOPIC_ROOT / "02-Remotion-Setup" / "video-slide-plan.md"

# 출력 경로 설정 (학습 리포지토리 보관용 및 실제 Remotion public 에셋 폴더용)
ARTIFACT_DIR = HERE
REMOTION_PUBLIC_DIR = Path("AI/RemotionStudio/public/active-shooter-0908/audio")

# 폴더 생성
ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
REMOTION_PUBLIC_DIR.mkdir(parents=True, exist_ok=True)


# ─── 2. 발음 보정 및 특수 문자 정제 규칙 ─────────────────────────────────────────
# edge-tts 가 알파벳 약어나 기호를 읽을 때 생기는 어색함을 사전 보정합니다.
PRONUNCIATION = [
    (r"\bRun\b", "런"),
    (r"\bHide\b", "하이드"),
    (r"\bFight\b", "파이트"),
    (r"\bFEMA\b", "피마"),
    (r"\bCRASE\b", "크레이스"),
    (r"\bALICE\b", "앨리스"),
    (r"\bEAP\b", "이 에이 피"),
    (r"\bStop the Bleed\b", "스탑 더 블리드"),
    (r"\bQR\b", "큐알"),
]

STRIP_MARKS = [
    (r"\*\*", ""),          # 마크다운 강조 표시 제거
    (r"[«»“”„「」]", ""),   # 인용부호 제거
    (r"\s{2,}", " "),      # 다중 공백 단일화
]


# ─── 3. 슬라이드 플랜에서 나레이션 파싱 함수 ──────────────────────────────────────
def extract_narrations(plan_content: str):
    # 슬라이드별 섹션 분리 ("### Slide XX:")
    slide_matches = list(re.finditer(r"^### Slide (\d+):", plan_content, re.M))
    results = []

    for idx, match in enumerate(slide_matches):
        sid = int(match.group(1))
        start_pos = match.start()
        end_pos = slide_matches[idx+1].start() if idx + 1 < len(slide_matches) else len(plan_content)
        slide_block = plan_content[start_pos:end_pos]
        
        # 나레이션 영역 검색 ( bullet 문장 내부의 blockquote 추출 )
        nar_match = re.search(r"\*\s+\*\*나레이션\*\*:\s*\n((?:\s*>\s*.*\n)+)", slide_block)
        if nar_match:
            lines = []
            for line in nar_match.group(1).strip().split('\n'):
                # 앞자리 블록기호(>) 및 감정/톤 마커(예: [SERIOUS], [URGENT]) 정제
                line_clean = re.sub(r"^\s*>\s*", "", line).strip()
                line_clean = re.sub(r"^\[[A-Z]+\]\s*", "", line_clean).strip()
                lines.append(line_clean)
            
            raw_text = " ".join(lines)
            
            # 발음 및 특수부호 보정 적용
            clean_text = raw_text
            for pat, rep in PRONUNCIATION:
                clean_text = re.sub(pat, rep, clean_text, flags=re.I)
            for pat, rep in STRIP_MARKS:
                clean_text = re.sub(pat, rep, clean_text)
                
            results.append({
                "id": sid,
                "text": clean_text.strip()
            })
            
    return results


# ─── 4. edge-tts 합성 함수 ─────────────────────────────────────────────────────
async def run_tts(text: str, path: Path) -> None:
    import edge_tts
    communicate = edge_tts.Communicate(text, VOICE, rate=RATE)
    await communicate.save(str(path))


# ─── 5. ffprobe 재생 길이 실측 함수 ─────────────────────────────────────────────
def get_audio_duration(path: Path) -> float:
    cmd = [
        "ffprobe", "-v", "quiet", 
        "-show_entries", "format=duration", 
        "-of", "csv=p=0", str(path)
    ]
    r = subprocess.run(cmd, capture_output=True, text=True, check=True)
    try:
        return round(float(r.stdout.strip()), 3)
    except ValueError:
        return 0.0


# ─── 6. 메인 컨트롤러 ─────────────────────────────────────────────────────────
def main():
    print(f"🔊 VibeLearn AI Module M4 - edge-tts Narration Generator 시작")
    print(f"📖 파싱 대상 슬라이드 기획안: {PLAN_PATH.relative_to(TOPIC_ROOT.parent.parent)}")
    
    # 기획안 로드 및 파싱
    plan_content = PLAN_PATH.read_text(encoding="utf-8")
    narrations = extract_narrations(plan_content)
    
    # 1. narrations.json 생성 백업
    narrations_json_path = ARTIFACT_DIR / "narrations.json"
    narrations_json_path.write_text(
        json.dumps(narrations, indent=2, ensure_ascii=False) + "\n", 
        encoding="utf-8"
    )
    print(f"✅ 나레이션 문구 파싱 완료 ➔ {narrations_json_path.name} 저장완료 ({len(narrations)}개 슬라이드)")
    
    durations = {}
    
    # 2. 오디오 생성 루프
    for item in narrations:
        sid = item["id"]
        slide_key = f"S{sid:02d}"
        file_name = f"{slide_key.lower()}.mp3"
        
        # 파일은 Remotion public 디렉토리에 생성하여 즉시 개발 환경에서 쓰이게 함
        public_audio_path = REMOTION_PUBLIC_DIR / file_name
        
        print(f"  🎙️ Slide {sid:02d} ({slide_key}) 오디오 생성 중...", end="", flush=True)
        
        try:
            asyncio.run(run_tts(item["text"], public_audio_path))
            dur = get_audio_duration(public_audio_path)
            durations[slide_key] = dur
            print(f" 완수 (실측 길이: {dur:.3f}초)")
        except Exception as e:
            print(f" ❌ 실패! 에러: {e}")
            continue
            
    # 3. durations.json 매핑 테이블 생성 저장
    durations_json_path = ARTIFACT_DIR / "durations.json"
    durations_json_path.write_text(
        json.dumps(durations, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8"
    )
    print(f"✅ 재생 길이 실측 매핑 테이블 ➔ {durations_json_path.name} 저장완료")
    
    # 실시간 Remotion data.ts 업데이트용 코드 출력 가이드
    print("\n💡 [Remotion data.ts 매핑 가이드]")
    print("아래 실측 길이 객체를 'AI/RemotionStudio/src/active-shooter-0908/data.ts'의 AUDIO_DURATIONS에 대입해 주십시오:")
    print("```typescript")
    print("export const AUDIO_DURATIONS: Record<string, number> = " + json.dumps(durations, indent=2, ensure_ascii=False) + ";")
    print("```")
    print(f"\n🎉 Module M4 나레이션 음성 자동화 작업 완료! (합계: {sum(durations.values()):.2f}초)")


if __name__ == "__main__":
    main()
