# 신청 Form — 배포 링크

**모듈**: M1 — 신청 접수 Form + 영상 안내 문구
**작성일**: 2026-07-21

---

## 배포 링크

```
https://docs.google.com/forms/d/e/1FAIpQLScLIGwXR4SR467JJcRbVWkoKZP9Xd0bhHDSM64noospnK1X8w/viewform
```

Build with AI 영상 설명란·아웃트로에는 이 링크를 사용한다. (편집 화면에서 복사된 원본 링크에는
`?usp=publish-editor`가 붙어 있었으나, 응답자에게 배포할 때는 뒤에 붙는 쿼리 없이 이 형태로 쓴다.)

## 상태

- [x] Form 게시(Publish) 완료
- [x] 모든 문항 Required(필수) 토글 On 처리
- [x] 🇺🇸 미국 선택 분기 테스트 — Section 2(워싱턴주 질문) 노출 확인
- [x] 🇰🇷 한국 선택 분기 테스트 — Section 2 건너뛰고 바로 Section 3 확인
- [x] Sheets 연동 확인 (Responses 탭 → View in Sheets)
- [x] 테스트 응답 삭제 (Form Responses 탭 → Delete all responses, Sheets에도 반영됨 → 0 responses 확인)

**테스트 완료일**: 2026-07-21 — 모든 분기·필수 입력·Sheets 연동 정상 확인.

## 참고

- Form 구조: Section 1(성함·이메일·나라) → 🇺🇸 미국이면 Section 2(워싱턴주 거주 여부) → Section 3(만들고 싶은 앱)
- 자세한 문항 내용: [form-questions.md](form-questions.md)
