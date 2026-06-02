# M2 — DashScope API 환경 구축

**상태**: 🔄 진행 중 (가이드 작성 완료, 키 발급·실행 대기) · **예상 학습 시간**: 3h · **난이도**: ⭐⭐

GPU 없는 환경이라 로컬 대신 **Alibaba Cloud Model Studio / DashScope API(Intl, OpenAI 호환)**로 Qwen3-TTS를 사용합니다.

## 📚 학습 순서
1. [guides/api-setup.md](guides/api-setup.md) — 키 발급 → 환경변수 → SDK → 첫 한국어 합성 (각 단계 완료 신호)
2. [troubleshooting/known-issues.md](troubleshooting/known-issues.md) — 인증/리전/모델명/과금/폴백
3. `examples/` — 생성될 `hello_ko.mp3`, `hello_en.mp3`, `model_name.txt`

## ✅ 환경 결정 (확정)
- **API 채택**. 근거: GPU 없음 + i7-1355U(15W) + RAM 16GB → 로컬 부적합. 로컬 검토 기록은 [02-Setup-Windows](../02-Setup-Windows/README.md)(부록)에 보존.
- 핵심 이점: **OpenAI 호환 엔드포인트** → 기존 Remotion OpenAI-TTS 코드에 `base_url`만 교체해 M5 연동 최소화.

## ⚠️ 핵심 주의
- 반드시 **Intl(싱가포르) 키** (China 키 비호환)
- 정확한 모델명은 공식 Model Studio 문서로 확정
- Intl 키 발급 불가 시 → **Replicate 폴백**

## 🔗 이동
- 이전: [M1 — 개요](../01-Overview/README.md)
- 다음: M3 — API 보이스 클론 & 음색 설계 (`../03-VoiceClone/`)
- 로드맵: [20260516_RoadMap_Qwen3-TTS](../vl_roadmap/20260516_RoadMap_Qwen3-TTS.md) · WorkLog: [20260516_M2_Qwen3-TTS](../vl_worklog/20260516_M2_Qwen3-TTS.md)
