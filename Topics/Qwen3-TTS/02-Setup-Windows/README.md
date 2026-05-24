# (부록) Windows 로컬 검토 — 채택 안 함 (Superseded)

> ⛔ **이 모듈은 M2 정식 경로가 아닙니다.** 로컬 구동을 검토한 기록(부록)으로 보존합니다.
> 실제 M2는 **API 경로** → [02-Setup-API](../02-Setup-API/README.md)
>
> **로컬 부적합 결론**: 이 PC는 GPU 없음 + Intel i7-1355U(15W 저전력) + RAM 16GB. 공식 `qwen-tts`는 CPU 미지원(전부 CUDA, flash-attn=Linux 전용), 유일한 CPU 경로인 비공식 Rust/Q4도 강력한 i9에서 겨우 실시간 → 이 저전력 칩에선 비효율. 따라서 **API 기반으로 전환 확정**.

**상태**: 📌 부록(검토 기록) · **난이도**: ⭐⭐

아래는 로컬 구동을 시도할 경우의 참고 자료입니다. 핵심은 **FlashAttention2(Linux 전용) 회피 → SDPA 사용**과 **GPU/CPU 분기**였습니다.

## 📚 학습 순서
1. [guides/windows-setup.md](guides/windows-setup.md) — 단계 0(GPU 판별) → conda → torch(분기) → `qwen-tts` → 첫 wav. 각 단계 완료 신호 포함
2. [troubleshooting/known-issues.md](troubleshooting/known-issues.md) — flash-attn/CUDA/CPU 속도/다운로드 등 알려진 이슈
3. `examples/` — 생성될 `hello_ko.wav`, `hello_en.wav` (단계 4 산출)

## ✅ 환경 결정 (확정)
- **Windows 로컬 채택** (API 전환·로드맵 재작성 검토했으나 취소). 근거: CPU도 30초 음성 ≈ 40~90초로 실용 가능, GPU 시 더 빠름.

## ⚠️ 핵심 주의
- flash-attn 설치 금지(Windows 비호환) → `attn_implementation="sdpa"`
- GPU 없으면 경량 `0.6B` 모델 사용
- 정확한 Windows 실행 플래그는 공식 Windows 가이드로 단계 0에서 최종 확인

## 🔗 이동
- 이전: [M1 — 개요](../01-Overview/README.md)
- 다음: M3 — 보이스 클론 & 음색 설계 (`../03-VoiceClone/`)
- 로드맵: [20260516_RoadMap_Qwen3-TTS](../vl_roadmap/20260516_RoadMap_Qwen3-TTS.md) · WorkLog: [20260516_M2_Qwen3-TTS](../vl_worklog/20260516_M2_Qwen3-TTS.md)
