# Qwen3-TTS 공식 1차 출처

> 수집일 2026-05-16 · WebSearch + WebFetch로 직접 검증한 1차 출처만 기록 (추측 배제)

## 공식 출처
- **GitHub (코드·README·예제)**: https://github.com/QwenLM/Qwen3-TTS — 설치(`pip install -U qwen-tts`)·추론 예제·모델 변형·라이선스의 1차 출처
- **공식 블로그(발표)**: https://qwen.ai/blog?id=qwen3tts-0115 — Qwen3-TTS 패밀리 오픈소스 발표(보이스 디자인·클론·다국어)
- **HuggingFace 모델**: `Qwen/Qwen3-TTS-*` — 가중치 다운로드·모델 카드
- **ModelScope**: `modelscope download --model Qwen/[model_name]` — 중국 본토 미러

## 핵심 사실 (출처 검증됨)
- **공개**: 2026년 1월, Alibaba Cloud Qwen 팀
- **라이선스**: Apache-2.0 (연구 + 상업적 사용 가능)
- **지원 언어(10)**: 중국어·영어·일본어·**한국어**·독일어·프랑스어·러시아어·포르투갈어·스페인어·이탈리아어 (+ 베이징/쓰촨 등 방언)
- **보이스 클론**: 3초 샘플 + **참조 텍스트(`ref_text`) 필수**. 입력은 로컬 경로/URL/base64/`(numpy_array, sample_rate)` 허용
- **스트리밍**: 지원, 종단 합성 지연 최저 ~97ms
- **배포**: HuggingFace + ModelScope

## 모델 변형 (5종, 공통 `Qwen3-TTS-Tokenizer-12Hz` 코덱)
| 모델 ID (HuggingFace) | 용도 |
|---|---|
| `Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign` | 자연어 설명으로 음색 설계 |
| `Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice` | 9종 프리셋 음성 + instruct 제어 |
| `Qwen/Qwen3-TTS-12Hz-1.7B-Base` | 3초 샘플 보이스 클론 |
| `Qwen/Qwen3-TTS-12Hz-0.6B-CustomVoice` | 경량 프리셋 음성 |
| `Qwen/Qwen3-TTS-12Hz-0.6B-Base` | 경량 클론 |
| `Qwen/Qwen3-TTS-Tokenizer-12Hz` | 공통 코덱(토크나이저) |

## 미확정 / M2에서 실증 필요
- **Windows 지원 명시 없음**: 예제가 `device_map="cuda:0"`·`torch.bfloat16`·FlashAttention2(GPU) 기반. Windows + NVIDIA GPU 가정하 동작 여부, flash-attn 미설치 시 동작 여부 → M2 실습 1에서 검증.
