# Qwen3-TTS API 설정 가이드 (M2)

> 실행: Alibaba Cloud Model Studio / DashScope **Intl(싱가포르)**, OpenAI 호환 모드
> 각 단계에 "완료 신호"가 있습니다. 그 신호가 나오면 성공입니다.
> 정확한 최신 모델명은 단계 3에서 **공식 Model Studio 문서로 최종 확인**(웹 검색은 보조).

## 단계 1 — 계정 & Intl API 키 발급 (45분)
1. https://www.alibabacloud.com 가입 → **Model Studio(국제)** 활성화
2. DashScope 콘솔 → **API-KEY 관리** → 키 생성
3. ⚠️ **반드시 Intl(국제) 키**. China 키는 Intl 엔드포인트와 호환 안 됨.
> 완료 신호: 콘솔에 활성 API 키가 보임. (발급 불가 시 → troubleshooting의 Replicate 폴백)

## 단계 2 — 키를 환경변수로 설정
PowerShell:
```powershell
setx DASHSCOPE_API_KEY "발급받은_키"
```
- 새 터미널을 열어야 반영됨.
> 완료 신호:
> ```powershell
> $env:DASHSCOPE_API_KEY
> ```
> 키 문자열이 출력됨(코드/노트에 평문 저장 금지).

## 단계 3 — SDK 설치 & 모델명 확인
```powershell
pip install -U openai      # OpenAI 호환 모드 사용
# 또는: pip install -U dashscope   (네이티브 SDK)
```
- 공식 Model Studio 문서에서 **Qwen3-TTS 모델명**을 확인해 메모:
  - 보이스 클론: `qwen3-tts-vc-*` (예: `qwen3-tts-vc-2026-01-22`)
  - 음색 디자인: `qwen3-tts-vd-*`
  - 실시간: `qwen3-tts-vc-realtime-*`
> 완료 신호: 사용할 정확한 모델명 1개를 `examples/model_name.txt`에 기록.

## 단계 4 — 첫 한국어 합성 (OpenAI 호환)
`examples/hello.py` (개념 골격 — 모델명/음성 파라미터는 단계 3 확인값 사용):
```python
import os, time
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["DASHSCOPE_API_KEY"],
    base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
)

for txt, out in [
    ("안녕하세요. 큐원 삼 티티에스 API 첫 한국어 합성 테스트입니다.", "examples/hello_ko.mp3"),
    ("Hello. First Qwen3-TTS API test in English.",                 "examples/hello_en.mp3"),
]:
    t = time.time()
    resp = client.audio.speech.create(
        model="<단계3에서 확인한 모델명>",
        voice="<공식 문서의 기본 음성>",
        input=txt,
    )
    resp.stream_to_file(out)
    print(out, "elapsed", round(time.time()-t, 1), "s")
```
> 완료 신호: `examples/hello_ko.mp3`, `hello_en.mp3` 생성 + 정상 재생. 호출 지연(초)을 WorkLog에 기록.

## 단계 5 — 재현성 확정
- 단계 1~4 + 실제 지연(초) + 확인한 모델명을 WorkLog에 기록.
- 오류는 `../troubleshooting/known-issues.md`에 증상→원인→해결로 기록.

### 검증 체크 (DoD)
- [ ] Intl 키 발급 + 환경변수 인식
- [ ] SDK 설치 + 정확한 모델명 기록
- [ ] `hello_ko.mp3`/`hello_en.mp3` 생성·재생
- [ ] 호출 지연 기록
- [ ] 트러블슈팅 1건 이상
