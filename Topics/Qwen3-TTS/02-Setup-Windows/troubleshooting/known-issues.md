# M2 트러블슈팅 — Windows 로컬 (증상 → 원인 → 해결)

## 1. flash-attn 설치 실패 (Windows)
- **증상**: `pip install flash-attn` 빌드 에러 / 휠 없음 / CUDA 컴파일 실패
- **원인**: FlashAttention 2는 **Linux 전용**. Windows 미지원.
- **해결**: flash-attn을 **설치하지 않는다**. 모델 로드 시 `attn_implementation="sdpa"`(PyTorch 내장)로 대체. 정확한 플래그/인자는 공식 Windows 가이드(`andimarafioti/faster-qwen3-tts/WINDOWS_SETUP_GUIDE.md`) 또는 공식 repo `--no-flash-attn` 확인.

## 2. `torch.cuda.is_available()` 가 False (GPU 있는데도)
- **증상**: GPU 장착인데 False
- **원인**: CPU용 torch 설치됨 / CUDA 빌드 불일치
- **해결**: GPU 경로 휠 재설치 — `pip install torch torchvision --index-url https://download.pytorch.org/whl/cu128` (드라이버/CUDA 버전에 맞는 인덱스 사용)

## 3. CPU에서 너무 느림
- **증상**: 30초 음성에 90초 이상
- **원인**: 1.7B 모델 + 복잡한 음색 프롬프트 + CPU
- **해결**: 경량 `0.6B` 모델 사용, 프롬프트 단순화. 30초 음성 ≈ 40~90초가 정상 범위. 대량 배치는 야간/일괄 처리.

## 4. 모델 다운로드 지연/중단
- **증상**: HuggingFace 다운로드 매우 느림/중단
- **원인**: 네트워크 / 본토 미러 필요
- **해결**: 재시도, 또는 ModelScope 미러 `modelscope download --model Qwen/<model>` 사용. 캐시 경로/용량(수 GB) 사전 확보.

## 5. bfloat16 관련 오류 (CPU)
- **증상**: CPU에서 bfloat16 연산 에러
- **원인**: 일부 CPU 경로에서 bf16 비효율/미지원
- **해결**: CPU 경로는 `dtype=torch.float32` 사용.

> 새 이슈 발생 시 같은 형식(증상→원인→해결)으로 계속 추가.
