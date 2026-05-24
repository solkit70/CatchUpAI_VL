# Qwen3-TTS Windows 로컬 설치 가이드 (M2)

> 환경: Windows 11 · PowerShell · conda
> 검증된 핵심 사실(M1/M2 웹 검증)에 기반. **단계 0의 GPU 판별 결과에 따라 GPU 경로 / CPU 경로로 분기**합니다.
> 각 단계에는 "완료 신호"가 있습니다. 그 신호가 나오면 성공입니다(추측 금지).

## ⚠️ Windows 핵심 이슈 (반드시 먼저 이해)
- 공식 `qwen-tts`는 예제에서 **FlashAttention 2**를 사용하는데, **flash-attn은 Linux 전용**이라 Windows 설치가 어렵습니다.
- **우회**: PyTorch 내장 **SDPA**(Scaled Dot-Product Attention)를 사용 → 공식 실행 시 `--no-flash-attn` 플래그(또는 attention 구현을 sdpa로 지정). flash-attn 설치는 **건너뜁니다**.
- 참고 경로: 공식 repo(`--no-flash-attn`), 커뮤니티 Windows 가이드 `github.com/andimarafioti/faster-qwen3-tts/blob/main/WINDOWS_SETUP_GUIDE.md`, SDPA 포크 `Qwen3-TTS-JP`.
- 성능: GPU(NVIDIA) 권장. CPU도 동작하며 30초 음성 ≈ 40~90초(모델·옵션별, 실시간 대비 1.5~2.5배). **CPU면 경량 `0.6B` 모델 권장.**

## 단계 0 — GPU/CUDA 판별 (분기 결정, 1분)
PowerShell에서:
```powershell
nvidia-smi
```
- **NVIDIA GPU 정보가 출력됨** → **GPU 경로** (단계 1-A)
- `'nvidia-smi'을(를) 찾을 수 없습니다` 또는 GPU 없음 → **CPU 경로** (단계 1-B), 모델은 `0.6B` 사용

> 완료 신호: GPU 경로/CPU 경로 중 하나를 확정하고 아래에서 해당 분기만 따라감.

## 단계 1 — conda 환경 생성 (공통)
```powershell
conda create -n qwen3-tts python=3.12 -y
conda activate qwen3-tts
```
> 완료 신호: 프롬프트가 `(qwen3-tts)` 로 바뀜.

## 단계 2 — PyTorch 설치 (분기)

### 1-A. GPU 경로 (NVIDIA + CUDA)
```powershell
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu128
```

### 1-B. CPU 경로
```powershell
pip install torch torchvision
```
> 완료 신호:
> ```powershell
> python -c "import torch; print(torch.__version__, torch.cuda.is_available())"
> ```
> GPU 경로면 `... True`, CPU 경로면 `... False` 가 출력되면 정상.

## 단계 3 — Qwen3-TTS 설치 (공통, flash-attn 제외)
```powershell
pip install -U qwen-tts
```
- **flash-attn 은 설치하지 않습니다** (Windows 비호환). SDPA로 동작.
> 완료 신호:
> ```powershell
> python -c "import qwen_tts; print('qwen_tts OK')"
> ```
> `qwen_tts OK` 출력.

## 단계 4 — 모델 가중치 다운로드 & 첫 음성 (Hello World)
- 모델 선택: GPU = `Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice`, CPU = `Qwen/Qwen3-TTS-12Hz-0.6B-CustomVoice`
- HuggingFace에서 자동 다운로드(수 GB). 첫 실행은 다운로드로 오래 걸림.
- 실행 시 **SDPA 사용**(flash-attn 미사용) 옵션을 적용. 정확한 인자 표기는 단계 0의 공식 Windows 가이드(위 링크)로 최종 확인 — 일반 형태:

```python
# examples/hello.py (개념 골격 — 디바이스/attn 옵션은 공식 Windows 가이드로 확정)
import torch, time
from qwen_tts import Qwen3TTSModel

MODEL = "Qwen/Qwen3-TTS-12Hz-0.6B-CustomVoice"   # GPU면 1.7B로 교체
DEVICE = "cuda:0" if torch.cuda.is_available() else "cpu"
DTYPE  = torch.bfloat16 if torch.cuda.is_available() else torch.float32

model = Qwen3TTSModel.from_pretrained(
    MODEL, device_map=DEVICE, dtype=DTYPE,
    attn_implementation="sdpa",   # flash-attn 대체 (Windows)
)

for lang, txt, out in [
    ("Korean",  "안녕하세요. 큐원 삼 티티에스 윈도우 첫 음성 테스트입니다.", "examples/hello_ko.wav"),
    ("English", "Hello. This is the first Qwen3-TTS test on Windows.",      "examples/hello_en.wav"),
]:
    t = time.time()
    wavs, sr = model.generate_custom_voice(text=txt, language=lang, speaker="Vivian")
    # wavs 저장 (라이브러리 저장 유틸 또는 soundfile 사용)
    print(lang, "elapsed", round(time.time()-t, 1), "s")
```
> 완료 신호: `examples/hello_ko.wav`, `examples/hello_en.wav` 두 파일 생성 + 재생 시 음성 정상. 각 합성 소요 시간(초)을 WorkLog에 기록.

## 단계 5 — 재현성 확정
- 위 전체 절차 + 단계 0 분기 결과 + 실제 합성 시간(초)을 WorkLog에 기록.
- 발생한 오류는 `../troubleshooting/known-issues.md`에 증상→원인→해결로 기록.

---

### 검증 체크 (DoD)
- [ ] 단계 0 GPU/CPU 분기 확정
- [ ] `(qwen3-tts)` 환경 + `torch.cuda.is_available()` 결과 기록
- [ ] `qwen_tts OK`
- [ ] `hello_ko.wav` / `hello_en.wav` 생성 및 재생 확인
- [ ] 합성 소요 시간 기록 (CPU면 30초 음성 대비 배수 확인)
- [ ] 트러블슈팅 1건 이상 기록
