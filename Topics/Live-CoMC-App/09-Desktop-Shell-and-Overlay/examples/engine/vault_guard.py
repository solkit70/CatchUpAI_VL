#!/usr/bin/env python3
"""M9 실습 5 — 볼트 읽기 전용 접근 강제.

## 무엇을 막는가

M2 App Boundary 의 제외 항목 3번:

> | 3 | 볼트 파일 쓰기 | 방송 중 문서 변조 사고 리스크 — **앱은 읽기 전용** |

이 앱은 방송 중에 볼트를 **읽기만** 한다. Rundown 을 읽고, 근거를 찾고, 인용한다.
쓸 일이 없다. 그런데 *쓸 일이 없다*는 것과 *쓸 수 없다*는 것은 다르다.

**규칙은 문서에만 있으면 지켜지지 않는다.** 코드가 막아야 한다.

## 왜 "우리 코드가 조심하면 된다"로는 부족한가

세 가지 경로로 사고가 난다.

1. **실수** — 디버깅하다 임시 파일을 볼트 경로에 쓴다
2. **라이브러리** — 우리가 안 부른 코드가 캐시를 남긴다. 어디에 쓰는지 모른다
3. **경로 조작** — `../../` 가 섞인 상대 경로가 볼트 밖에서 안으로 들어온다

1번은 리뷰로 잡을 수 있지만 2·3번은 못 잡는다. **런타임에서 막아야 한다.**

## 어떻게 막는가 — 두 겹

### ① 정상 통로 (`read_vault`)

볼트를 읽는 **유일한 사관 통로**다. 경로를 정규화하고 볼트 안인지 확인한 뒤 연다.
`..` 로 빠져나가는 경로는 여기서 걸린다.

### ② 런타임 가드 (`guard()`)

`builtins.open` 과 `Path.open` 을 감싸, **볼트 경로에 쓰기 모드로 여는 시도를
예외로 만든다.** 우리 코드든 남의 코드든 상관없다.

    with guard():
        ...엔진 실행...          # 이 안에서는 볼트에 못 쓴다

⚠️ **이것은 보안 경계가 아니라 안전장치다.** 작정하고 우회하면 `os.open`,
`ctypes`, 서브프로세스 등 뚫을 길이 있다. 목적은 **악의를 막는 것이 아니라
사고를 막는 것**이다. 이 앱의 위협 모델은 공격자가 아니라 새벽 두 시의 나다.

실행:
    python vault_guard.py --selftest
"""
from __future__ import annotations

import argparse
import builtins
import io
import os
import sys
from contextlib import contextmanager
from pathlib import Path

HERE = Path(__file__).resolve().parent
M7_SRC = HERE.parents[2] / "07-CoMC-Engine-POC" / "src"
if str(M7_SRC) not in sys.path:
    sys.path.insert(0, str(M7_SRC))

from common import VAULT  # noqa: E402

VAULT_ROOT = Path(VAULT).resolve()

# 볼트 안이지만 **앱 자신의 작업 산출물**이라 쓰기를 허용하는 곳.
# 이 Topic 폴더는 학습 산출물이고, 방송 중 참조하는 "문서"가 아니다.
WRITABLE = (
    (VAULT_ROOT / "Ingest" / "CatchUpAI_VL" / "Topics" / "Live-CoMC-App").resolve(),
)

WRITE_HINTS = ("w", "a", "x", "+")


class VaultWriteBlocked(PermissionError):
    """볼트에 쓰려 했을 때. PermissionError 를 상속해 기존 except 절에도 걸린다."""


def _resolved(path) -> Path:
    """심볼릭 링크와 `..` 를 편 절대 경로. 존재하지 않아도 계산된다."""
    return Path(os.path.abspath(os.path.realpath(str(path))))


def in_vault(path) -> bool:
    try:
        return _resolved(path).is_relative_to(VAULT_ROOT)
    except (ValueError, OSError):
        return False


def is_writable_area(path) -> bool:
    p = _resolved(path)
    return any(p.is_relative_to(w) for w in WRITABLE)


def _is_write_mode(mode: str) -> bool:
    return any(h in mode for h in WRITE_HINTS)


# ── ① 정상 통로 ────────────────────────────────────────────────────────
def read_vault(rel: str, encoding: str = "utf-8") -> str:
    """볼트 파일을 읽는 유일한 사관 통로.

    `..` 로 볼트 밖을 가리키는 경로는 여기서 거부한다. 경로 문자열을 그대로
    믿지 않고 **정규화한 뒤 볼트 안인지 확인**한다.
    """
    target = _resolved(VAULT_ROOT / rel)
    if not target.is_relative_to(VAULT_ROOT):
        raise VaultWriteBlocked(
            f"볼트 밖을 가리키는 경로입니다: {rel} → {target}")
    if not target.exists():
        raise FileNotFoundError(f"볼트에 없는 파일: {rel}")
    with io.open(target, "r", encoding=encoding) as f:
        return f.read()


# ── ② 런타임 가드 ──────────────────────────────────────────────────────
_original_open = builtins.open
_original_path_open = Path.open


def _blocked(path, mode) -> bool:
    return (_is_write_mode(mode) and in_vault(path)
            and not is_writable_area(path))


@contextmanager
def guard(strict: bool = True):
    """이 블록 안에서는 볼트에 쓰기가 막힌다.

    strict=False 면 막지 않고 경고만 찍는다 — 기존 코드에 붙여 보고
    무엇이 걸리는지 먼저 보고 싶을 때.
    """
    hits: list[str] = []

    def guarded_open(file, mode="r", *a, **kw):
        if _blocked(file, mode):
            hits.append(f"{file} (mode={mode})")
            if strict:
                raise VaultWriteBlocked(
                    f"볼트는 읽기 전용입니다 (M2 App Boundary 제외 3번): {file}")
            print(f"  ⚠️ [vault_guard] 쓰기 시도: {file} mode={mode}", file=sys.stderr)
        return _original_open(file, mode, *a, **kw)

    def guarded_path_open(self, mode="r", *a, **kw):
        if _blocked(self, mode):
            hits.append(f"{self} (mode={mode})")
            if strict:
                raise VaultWriteBlocked(
                    f"볼트는 읽기 전용입니다 (M2 App Boundary 제외 3번): {self}")
            print(f"  ⚠️ [vault_guard] 쓰기 시도: {self} mode={mode}", file=sys.stderr)
        return _original_path_open(self, mode, *a, **kw)

    builtins.open = guarded_open
    Path.open = guarded_path_open
    try:
        yield hits
    finally:
        builtins.open = _original_open
        Path.open = _original_path_open


# ── 자기 검증 ──────────────────────────────────────────────────────────
def selftest() -> int:
    import tempfile
    print("\n=== 볼트 읽기 전용 가드 자기 검증 ===\n")
    print(f"  볼트 루트   {VAULT_ROOT}")
    print(f"  쓰기 허용   {WRITABLE[0].relative_to(VAULT_ROOT)}\n")

    ok = True
    def check(label: str, passed: bool, detail: str = ""):
        nonlocal ok
        ok &= passed
        print(f"  {'✅' if passed else '❌'} {label}" + (f"   {detail}" if detail else ""))

    # 1. 정상 통로로 읽기
    try:
        txt = read_vault("Ingest/CatchUpAI_VL/Topics/Live-CoMC-App/topic_starter.md")
        check("정상 통로로 볼트 파일 읽기", len(txt) > 0, f"{len(txt)}자")
    except Exception as e:
        check("정상 통로로 볼트 파일 읽기", False, f"{type(e).__name__}: {e}")

    # 2. 경로 조작 차단
    try:
        read_vault("Ingest/../../../Windows/System32/drivers/etc/hosts")
        check("`..` 경로 조작 차단", False, "차단되지 않았다")
    except VaultWriteBlocked:
        check("`..` 경로 조작 차단", True, "VaultWriteBlocked")
    except FileNotFoundError:
        check("`..` 경로 조작 차단", True, "볼트 안으로 정규화돼 파일 없음")

    # 3. 가드 안에서 볼트 문서에 쓰기 → 막혀야 한다
    victim = VAULT_ROOT / "AI" / "_vault_guard_test.md"
    with guard() as hits:
        try:
            with open(victim, "w", encoding="utf-8") as f:
                f.write("이 파일은 만들어지면 안 된다")
            check("볼트 문서 쓰기 차단 (builtins.open)", False, "쓰기가 성공했다")
        except VaultWriteBlocked:
            check("볼트 문서 쓰기 차단 (builtins.open)", True)
        try:
            with victim.open("w", encoding="utf-8") as f:
                f.write("이것도 안 된다")
            check("볼트 문서 쓰기 차단 (Path.open)", False, "쓰기가 성공했다")
        except VaultWriteBlocked:
            check("볼트 문서 쓰기 차단 (Path.open)", True)
    check("차단 후 파일이 생기지 않았다", not victim.exists())
    if victim.exists():
        victim.unlink()

    # 4. 앱 자신의 산출물 폴더는 쓸 수 있어야 한다
    own = (VAULT_ROOT / "Ingest/CatchUpAI_VL/Topics/Live-CoMC-App"
           / "07-CoMC-Engine-POC/output/_guard_probe.tmp")
    with guard():
        try:
            own.parent.mkdir(parents=True, exist_ok=True)
            with open(own, "w", encoding="utf-8") as f:
                f.write("ok")
            check("앱 산출물 폴더는 쓰기 허용", own.exists())
        except VaultWriteBlocked as e:
            check("앱 산출물 폴더는 쓰기 허용", False, str(e)[:50])
    if own.exists():
        own.unlink()

    # 5. 볼트 밖은 영향 없음
    with guard():
        try:
            tmp = Path(tempfile.gettempdir()) / "_guard_outside.tmp"
            with open(tmp, "w", encoding="utf-8") as f:
                f.write("ok")
            check("볼트 밖 쓰기는 그대로 허용", tmp.exists())
            tmp.unlink(missing_ok=True)
        except Exception as e:
            check("볼트 밖 쓰기는 그대로 허용", False, f"{type(e).__name__}")

    # 6. 가드를 빠져나오면 원래대로
    check("가드 해제 후 open 복원", builtins.open is _original_open)

    # 7. 읽기는 가드 안에서도 자유로워야 한다
    with guard():
        try:
            read_vault("Ingest/CatchUpAI_VL/Topics/Live-CoMC-App/topic_starter.md")
            check("가드 안에서 읽기는 자유", True)
        except Exception as e:
            check("가드 안에서 읽기는 자유", False, f"{type(e).__name__}")

    print("\n  " + ("✅ 전부 통과" if ok else "❌ 실패 항목 있음"))
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        raise SystemExit(selftest())
    print(__doc__)


if __name__ == "__main__":
    main()
