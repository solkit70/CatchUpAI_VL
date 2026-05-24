# Qwen3-TTS 개요·아키텍처 요약 (M1)

## 한 줄 정의
Qwen3-TTS는 알리바바 Qwen 팀이 2026년 1월 Apache-2.0으로 공개한 오픈소스 TTS 패밀리로, **3초 보이스 클론·자연어 음색 설계·스트리밍 합성·10개 언어(한국어 포함)**를 제공한다.

## 왜 이 토픽인가 (도입 동기)
현재 영상 제작 파이프라인은 OpenAI TTS와 MS edge-tts에 의존한다. Qwen3-TTS는 (1) 오픈소스/상업적 사용 가능, (2) 짧은 샘플로 일관된 캐릭터 보이스 구축, (3) 자연어로 톤 설계가 가능해 영상 내레이션·라이브 가이딩에 활용 가치가 크다.

## 핵심 기능 4가지
1. **보이스 클론(Base 모델)** — 3초 참조 음성 + 참조 텍스트로 화자 음색 복제. 입력은 파일/URL/base64/numpy.
2. **자연어 음색 설계(VoiceDesign 모델)** — "차분한 중년 남성" 같은 텍스트 지시(`instruct`)로 음색 생성.
3. **프리셋 + instruct 제어(CustomVoice 모델)** — 9종 프리셋 음성을 감정·어조 지시로 변형.
4. **스트리밍/비스트리밍** — 한 글자 입력 즉시 첫 패킷 출력, 지연 최저 ~97ms (실시간 가이딩 잠재력).

## 모델 선택 가이드 (본 토픽 기준)
- **영상 내레이션 일관 캐릭터** → `1.7B-Base`(클론) 또는 `1.7B-VoiceDesign`(설계)
- **빠른 프리셋 음성** → `1.7B-CustomVoice`
- **저사양/경량 테스트** → `0.6B-*`
- 본 토픽 Capstone(Remotion 연동)은 **배치 합성** 중심 → 스트리밍은 후속(라이브 가이딩) 확장 포인트

## 아키텍처 메모
- 공통 **`Qwen3-TTS-Tokenizer-12Hz`** 오디오 코덱 위에 1.7B / 0.6B LM 백본 + 용도별 헤드(Base/CustomVoice/VoiceDesign).
- 예제 기준 추론: PyTorch, `device_map="cuda:0"`, `dtype=torch.bfloat16`, 선택적 FlashAttention2.

## 기존 파이프라인과의 관계
- 현행 `gen_audio.py`(edge-tts)·OpenAI TTS는 **프리셋 음성·간단**하지만 **커스텀 화자 클론 불가**.
- Qwen3-TTS는 **클론·음색 설계**가 강점이나 **로컬 설치·GPU 의존**이 비용. → M3에서 품질 A/B, M5에서 채택 기준 문서화.

## 리스크 (M2 실증 대상)
- Windows 공식 지원 미명시(예제 CUDA/bfloat16/flash-attn 가정). NVIDIA GPU 필요 가능성, flash-attn 설치 난이도.
