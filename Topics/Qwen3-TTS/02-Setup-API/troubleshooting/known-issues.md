# M2(API) 트러블슈팅 (증상 → 원인 → 해결)

## 1. 401/인증 실패
- **증상**: `invalid api key` / 401
- **원인**: China 키를 Intl 엔드포인트에 사용, 또는 키 미설정
- **해결**: **Intl 키**인지 확인, `base_url`이 `dashscope-intl...compatible-mode/v1`인지 확인, `$env:DASHSCOPE_API_KEY` 인식 확인(새 터미널)

## 2. Intl 키 발급 불가 (거주/결제)
- **증상**: 국제 계정/결제 수단 문제로 키 발급 안 됨
- **원인**: 리전·결제 제약
- **해결**: **폴백 → Replicate** `replicate.com/qwen/qwen3-tts` (토큰 발급 단순). Skill의 백엔드 인자로 `replicate` 추가 설계.

## 3. 모델명 오류 (model not found)
- **증상**: 지정 모델명으로 404/모델 없음
- **원인**: 추정 모델명 사용 (날짜 버전 변동)
- **해결**: 공식 Model Studio 문서에서 현재 유효한 `qwen3-tts-*` 모델명 재확인 후 `model_name.txt` 갱신

## 4. 한국어 발음/품질 이슈
- **증상**: 한국어 부자연/오발음
- **원인**: language 파라미터 누락, 음성/모델 부적합
- **해결**: 공식 문서의 language 지정·권장 음성 사용, 음색 디자인 모델로 대안 테스트(M3에서 심화)

## 5. 과금/쿼터
- **증상**: 무료 쿼터 소진/과금 발생
- **원인**: 테스트 호출량 누적 (합성 ≈ $0.013/1k자, 클론 $0.01/건)
- **해결**: 테스트는 짧은 문장, 호출 수/문자 수 로깅, 90일 무료 쿼터 잔량 모니터링

## 6. OpenAI 호환 모드 404 (TTS 미지원)
- **증상**: `openai.NotFoundError: Error code: 404` — `/compatible-mode/v1/audio/speech` 호출 시
- **원인**: DashScope의 OpenAI 호환 엔드포인트(`/compatible-mode/v1`)는 **LLM(채팅) 전용**. TTS API를 지원하지 않음
- **해결**: `pip install dashscope` 후 `dashscope.MultiModalConversation.call()` 사용. 엔드포인트는 `https://dashscope-intl.aliyuncs.com/api/v1`

> 새 이슈는 동일 형식(증상→원인→해결)으로 계속 추가.
