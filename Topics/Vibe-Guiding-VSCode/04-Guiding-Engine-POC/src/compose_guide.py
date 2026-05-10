from __future__ import annotations

import argparse
from pathlib import Path

from common import OUTPUT_DIR, read_json, write_text


def command_steps(manual: dict, context: dict) -> list[str]:
    guide_type = manual.get("guide_type")
    if guide_type == "install":
        return [
            "터미널에서 `npm install -g @gobi-ai/cli`를 실행합니다.",
            "새 터미널을 열고 `gobi --version`으로 설치 결과를 확인합니다.",
        ]
    if guide_type == "auth":
        return [
            "`gobi auth login`을 실행하고 표시되는 device-code flow를 완료합니다.",
            "`gobi auth status`로 로그인 사용자가 표시되는지 확인합니다.",
        ]
    if guide_type == "space_post":
        slug = context.get("active_space") or "<space-slug>"
        return [
            "`gobi space list`로 접근 가능한 Space slug를 확인합니다.",
            f"`gobi space create-post --space-slug {slug} --title \"Post 제목\" --content \"Post 본문\" --json`을 실행합니다.",
            f"응답의 `id`를 사용해 `gobi space get-post <postId> --space-slug {slug}`로 조회합니다.",
        ]
    if guide_type == "vault_publish":
        return [
            "`PUBLISH.md`가 vault 루트에 있는지 확인합니다.",
            "`gobi vault publish`를 실행합니다.",
            "`gobi vault status`로 발행 상태를 확인합니다.",
        ]
    if guide_type == "session":
        return [
            "`gobi session list`로 session id를 확인합니다.",
            "`gobi session create-reply <sessionId> --content \"답장 내용\"`을 실행합니다.",
            "`gobi session get <sessionId>`로 새 답장이 보이는지 확인합니다.",
        ]
    if guide_type == "desktop_applet":
        return [
            "먼저 GOBI Desktop 버전, Vault Path, Applet 경로, 현재 보이는 Settings 메뉴명을 확인합니다.",
            "확인되지 않은 메뉴 이름이나 버튼 위치는 단정하지 말고, 사용자가 보는 화면 기준으로 다음 단계를 좁힙니다.",
            "Applet 경로가 확인되면 custom homepage 파일 위치와 적용 절차를 같은 경로 기준으로 안내합니다.",
        ]
    if guide_type == "environment_check":
        return [
            "`node --version`, `npm --version`, `gobi --version`을 먼저 실행해 현재 환경을 확인합니다.",
            "GOBI CLI가 2.0.12 미만이면 `npm install -g @gobi-ai/cli`로 업데이트한 뒤 새 터미널을 엽니다.",
            "업데이트 전에는 v2.0.12 전용 명령어를 단정하지 말고, `gobi --help`에 실제 표시되는 명령어를 기준으로 안내합니다.",
        ]
    return ["Quick Reference에서 현재 작업에 맞는 명령어 그룹을 확인합니다."]


def compose(context: dict, decision: dict, retrieval: dict) -> str:
    manual = retrieval.get("selected_manual") or {}
    rule = decision.get("selected_rule", {})
    signal = context.get("problem_signal", {})
    replacements = manual.get("replacement_terms", {})

    lines = [
        "# Guide Response",
        "",
        "## 현재 상태 요약",
        "",
        f"- 문제 신호: `{signal.get('type', 'unknown')}`",
        f"- 사용자 메시지: {signal.get('message', '')}",
        f"- GOBI CLI 버전: {context.get('gobi_cli_version') or 'unknown'}",
        f"- 인증 상태: {context.get('auth_status') or 'unknown'}",
        f"- 활성 Space: {context.get('active_space') or 'unknown'}",
        "",
        "## 판단 근거",
        "",
        f"- 선택된 trigger rule: `{rule.get('rule_id', 'unknown')}`",
        f"- 이유: {rule.get('reason', 'No reason provided.')}",
        f"- 선택된 manual: `{manual.get('manual_id', 'unknown')}`",
        "",
    ]

    if replacements:
        lines.extend(["## 구 명령어 변환", ""])
        for old, new in replacements.items():
            lines.append(f"- `{old}` -> `{new}`")
        lines.append("")

    lines.extend(["## 실행 단계", ""])
    for idx, step in enumerate(command_steps(manual, context), start=1):
        lines.append(f"{idx}. {step}")
    lines.extend([
        "",
        "## 완료 신호",
        "",
        f"- {manual.get('completion_signal', '작업 결과를 확인합니다.')}",
        "",
        "## 실패 시 fallback",
        "",
    ])
    for fallback in manual.get("fallbacks", ["Quick Reference로 돌아가 관련 명령어를 확인합니다."]):
        lines.append(f"- {fallback}")

    lines.extend([
        "",
        "## Source Attribution",
        "",
        f"- `{manual.get('source_path', 'unknown')}`",
    ])
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Compose guide response.")
    parser.add_argument("--context", type=Path, default=OUTPUT_DIR / "user_context.json")
    parser.add_argument("--decision", type=Path, default=OUTPUT_DIR / "trigger_decision.json")
    parser.add_argument("--retrieval", type=Path, default=OUTPUT_DIR / "retrieval_result.json")
    parser.add_argument("--output", type=Path, default=OUTPUT_DIR / "guide_response.md")
    args = parser.parse_args()

    guide = compose(read_json(args.context), read_json(args.decision), read_json(args.retrieval))
    write_text(args.output, guide)
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
