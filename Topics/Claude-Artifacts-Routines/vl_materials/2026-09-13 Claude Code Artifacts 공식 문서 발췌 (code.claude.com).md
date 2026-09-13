---
title: "Claude Code — Share session output as artifacts (공식 문서 발췌)"
source: https://code.claude.com/docs/en/artifacts
created: 2026-09-13 07:20:00
tags:
  - claude-artifacts-routines
  - clipping
  - official-doc
---

## 출처

Claude Code 공식 문서 「Share session output as artifacts」 — https://code.claude.com/docs/en/artifacts. 2026-09-13 07:20 PST WebFetch. 아래는 **원문 인용**(영문 그대로)과 그 옆의 한 줄 요약. 전문은 링크.

## 공유 범위

> A new artifact is visible only to you. To share it, open the artifact in your browser and use the **Share** control in the page header.

> **Within your organization**: on Team and Enterprise plans, grant access to specific people in your organization, or to everyone in it. Viewers sign in to claude.ai as members of your organization to see the page.
> **Publicly**: share a link that anyone on the internet can open, with no claude.ai sign-in required. On Pro and Max plans, a public link is the only way to share an artifact. On Team and Enterprise plans, public sharing is off until an Owner enables it for the organization.

→ 공유 범위는 **셋**: 나만 · 조직(Team/Enterprise) · 공개 링크. Pro/Max 는 「나만」 아니면 「공개」뿐이다.

> A viewer who opens a public link without signing in, or from outside your organization, sees the label `Content is user-generated and unverified.` instead of your name.

→ 9/13 시크릿 창에서 부스 현황판·요양보호사·입장 안내 상단에 이 문구가 보였다 = **공개 링크로 열린 것**의 표식 `[실측 09-13]`.

## 런타임 기능과 공유

> An artifact that calls connectors can't be shared to a public link on any plan. On Team and Enterprise plans, you can keep it private or share it within your organization. On Pro and Max plans, where a public link is the only way to share, a connector-backed artifact stays private to you.

→ **커넥터(mcp)를 쓰는 페이지는 어떤 플랜에서도 공개 불가.** db 에 대한 같은 문장은 이 문서에 **없다** — 세션 스킬(artifact-capabilities)에는 `assets` 가 "organization-internal (never public)" 이라고 적혀 있다. **db 는 두 문서 어디에도 명시가 없다** → 실습 2 로.

> After you approve an artifact once, Claude Code republishes it without asking, and asks again in some cases, including when: Claude declares a runtime capability for the page … You have since shared it publicly …

## 버전

> Each publish becomes a version, and from the **Share** control in the page header you can choose which version viewers see.

> To update an artifact from a different session, give Claude its URL, or attach it with `/artifacts`. Without either, a new session creates a new artifact instead of updating one.

→ 9/7 "공유 링크가 옛 버전" 은 **Share 에서 고른 버전이 고정**돼 있었을 가능성 — 스크린샷의 "Always share latest version" 토글이 그 스위치다 `[문서]`. 실습 3 에서 확인.

## 편집자·댓글

> People you share with are viewers by default … On Team and Enterprise plans, you can also make someone an editor.

> When you share an artifact within your organization, the people you share it with can leave comments on the page … You need Claude Code v2.1.221 or later and a Team or Enterprise plan, because only an artifact you share within your organization takes comments.

> If you share an artifact publicly, viewers can't comment on it: the page says `Comments aren't available while this Artifact is shared publicly.`

→ **댓글은 조직 공유(Team/Enterprise)에서만.** 공개 링크에는 댓글이 없다. A6 설명 페이지의 "댓글을 남길 수 있다"는 **플랜 조건이 빠진 문장**이었다.

> After your session publishes an artifact, Claude Code watches that artifact for comments for as long as the session runs.

## 제약

> An artifact is a capture of work: one self-contained page with no backend … It can't authenticate viewers itself.

> The rendered page must be 16 MiB or smaller. Large embedded images are the usual cause when a publish fails for size.

> The CSP blocks every external image and all other external scripts … Claude therefore loads any library the page needs from one of those CDNs, inlines all other CSS and JavaScript, and embeds images as data URIs.

## 조직 관리 (Team/Enterprise)

> Artifact content is stored on Anthropic-operated infrastructure and is visible only to authenticated members of the publishing organization, unless the artifact is shared publicly.

> Public sharing is off by default on Team and Enterprise plans … Turning it back off blocks access through existing public links without changing each artifact's audience.
