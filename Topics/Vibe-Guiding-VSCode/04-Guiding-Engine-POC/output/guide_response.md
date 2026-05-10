# Guide Response

## 현재 상태 요약

- 문제 신호: `space_post_blocked`
- 사용자 메시지: Space에 글을 올리고 싶은데 Thread 생성 명령어만 기억납니다.
- GOBI CLI 버전: 2.0.12
- 인증 상태: authenticated
- 활성 Space: changbal

## 판단 근거

- 선택된 trigger rule: `old_thread_command_used`
- 이유: GOBI CLI v2.0.12에서는 Thread 명령어가 Post 명령어로 변경되었습니다.
- 선택된 manual: `gobi-cli-space-create-post`

## 구 명령어 변환

- `thread` -> `post`
- `create-thread` -> `create-post`
- `list-threads` -> `list-posts`
- `get-thread` -> `get-post`

## 실행 단계

1. `gobi space list`로 접근 가능한 Space slug를 확인합니다.
2. `gobi space create-post --space-slug changbal --title "Post 제목" --content "Post 본문" --json`을 실행합니다.
3. 응답의 `id`를 사용해 `gobi space get-post <postId> --space-slug changbal`로 조회합니다.

## 완료 신호

- `gobi space create-post` returns a post id and `gobi space get-post <id>` can retrieve it.

## 실패 시 fallback

- Run `gobi space list` to confirm the slug.
- Run `gobi auth status` if the command returns an auth error.

## Source Attribution

- `Topics/Vibe-Guiding-VSCode/03-Vibe-Manual-CVL/sample-manual/gobi-cli-getting-started.md`
