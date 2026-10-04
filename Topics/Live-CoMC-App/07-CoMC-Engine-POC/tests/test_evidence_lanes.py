"""M11 privacy, routing, evidence integrity, and approval regressions (offline)."""
import importlib.util
import json
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

SRC = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC))
import common
import evidence_lanes as lanes


def stage(name):
    spec = importlib.util.spec_from_file_location("test_" + name[:2], SRC / name)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


CLASSIFY = stage("03_classify_intent.py")
GATE = stage("05_verify_and_gate.py")
RESOLVE = stage("02_resolve_context.py")


def test_web_reference_binding_preserves_gate_checks():
    c = {'lane': 'web', 'evidence_pool': [
        {'path': 'https://example.org/docs', 'quote': 'ExampleService provides weather forecasts for 3 days.'}],
        'coverage_items': [], 'coverage_state': 'defined', 'current_part_id': None}
    def draft(text, key='WEB-0001', quote='WEB-0001'):
        return {'sentences': [text], 'claim_map': [{'sentence_idx': 0,
                'evidence_path': key, 'evidence_quote': quote}], 'length_sentences': 1, 'coverage_state': 'defined'}
    valid = draft('검색 결과에 따르면, ExampleService는 3일 예보를 제공합니다.')
    lanes.bind_web_references(valid, c)
    assert valid['claim_map'][0]['evidence_quote'] == c['evidence_pool'][0]['quote']
    assert GATE.verify(valid, c, common.load_safety_policy(), lane='web')['pass']
    quoted = draft('검색 결과에 따르면, ExampleService는 3일 예보를 제공합니다.',
                   quote=c['evidence_pool'][0]['quote'])
    lanes.bind_web_references(quoted, c)
    assert GATE.verify(quoted, c, common.load_safety_policy(), lane='web')['pass']
    for invalid in [draft('검색 결과에 따르면, ExampleService는 97일 예보를 제공합니다.'),
                    draft('검색 결과에 따르면, InventedService를 제공합니다.'),
                    draft('검색 결과에 따르면, 예보를 제공합니다.', 'WEB-9999', 'WEB-9999'),
                    draft('검색 결과에 따르면, 예보를 제공합니다.', quote='WEB-0002'),
                    draft('검색 결과에 따르면, 예보를 제공합니다.', quote='Invented evidence for forecasts.')]:
        lanes.bind_web_references(invalid, c)
        assert not GATE.verify(invalid, c, common.load_safety_policy(), lane='web')['pass']


def test_web_query_keeps_subject_and_question():
    assert lanes.web_query('웹에서 Open-Meteo가 어떤 서비스인지 설명해 주세요') == 'Open-Meteo 어떤 서비스인지'
    assert lanes.web_query('웹에서 Python과 JavaScript 차이를 알려 주세요') == 'Python과 JavaScript 차이를'


def note(root, name, text):
    p = root / name
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")
    return p


def ctx():
    return {"evidence_pool": [{"path": "Roundup/today.md#실험", "quote": "CoMC 앱 개발을 진행했습니다."}],
            "coverage_items": ["CoMC 앱 개발"], "coverage_state": "defined", "current_part_id": "2", "other_parts": []}


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    monkeypatch.setattr(common, "OUTPUT", tmp_path / "output")
    monkeypatch.setattr(common, "TRACE", tmp_path / "output" / "trace.jsonl")
    monkeypatch.setattr(lanes, "PRIVATE", tmp_path / "output" / "private" / "m11")
    monkeypatch.setattr(lanes, "CONTEXT", lanes.PRIVATE / "answer_context.json")
    monkeypatch.setattr(lanes, "INDEX", lanes.PRIVATE / "vault_index.json")
    return tmp_path


def test_vault_private_filters_and_live_revalidation(tmp_path):
    note(tmp_path, ".gitignore", "Journal/*\nsecret.md\n")
    public = note(tmp_path, "Journal/public.md", "## AI 개발\nCoMC 앱에서 과거 기록 검색을 실험했습니다.\n메일 me@example.com 없이 CoMC 기록을 검색합니다.\n### 가족 건강\nCoMC 실험은 병원 진료 뒤에 했습니다.\n## 다음 개발\nCoMC 기능을 다음 방송에서 확인합니다.\n")
    note(tmp_path, "Journal/internal.md", "---\nvisibility: internal\n---\n## AI 개발\nCoMC 극비 자료입니다.\n")
    note(tmp_path, "Journal/secret.md", "---\nprivate: true\n---\n## 개발\nCoMC 비공개 기록입니다.\n")
    note(tmp_path, "secret.md", "## 개발\nCoMC 비공개 상세입니다.\n")
    note(tmp_path, "Private Meetings/a.md", "## 개발\nCoMC 비공개 미팅입니다.\n")
    note(tmp_path, "folder/README.md", "## 안내\n🔒 내부 자료\n")
    note(tmp_path, "folder/a.md", "## 개발\nCoMC 내부 폴더 자료입니다.\n")
    note(tmp_path, "nested/.gitignore", "ignored.md\n")
    note(tmp_path, "nested/ignored.md", "## 개발\nCoMC 프로젝트 비공개 자료입니다.\n")
    idx = lanes.VaultIndex(tmp_path, tmp_path / "index.json")
    idx.build()
    rows = idx.search("CoMC")
    assert rows and all(e["path"].startswith("Journal/public.md#") for e in rows)
    assert not any("병원" in e["quote"] or "example.com" in e["quote"] for e in rows)
    public.write_text("---\nvisibility: internal\n---\n## 개발\nCoMC 앱 기록입니다.\n", encoding="utf-8")
    assert idx.search("CoMC") == []


@pytest.mark.parametrize("text,lane", [("볼트에서 CoMC 찾아줘", "vault"), ("지난 회차 CoMC 알려줘", "vault"),
                                      ("인터넷에서 Python 알려줘", "web"), ("재밌는 얘기 해 주세요", "creative")])
def test_classifier_enables_lanes(text, lane):
    it = CLASSIFY.build_intent(text, ctx())
    assert it["intent"] == "answer_question"
    assert it["slots"]["evidence_lane"] == lane
    assert not common.validate("intent", it)


def test_rundown_first_and_vault_fallback():
    it = CLASSIFY.build_intent("오늘 2부에서 뭘 다루나요?", ctx())
    lane, _ = lanes.resolve(it, ctx(), searcher=lambda q: pytest.fail("should not search"))
    assert lane == "rundown"
    it = CLASSIFY.build_intent("Docker 컨테이너 설명해 주세요", ctx())
    lane, c = lanes.resolve(it, ctx(), searcher=lambda q: [{"path": "Topics/Docker.md#설명", "quote": "Docker 컨테이너 설명입니다."}])
    assert lane == "vault" and c["review_required"]


def test_personal_query_does_not_fallback_to_web():
    it = CLASSIFY.build_intent("예전에 CoMC에서 뭘 했나요?", None)
    with pytest.raises(lanes.LaneError):
        lanes.resolve(it, None, searcher=lambda q: [], web=lambda q: pytest.fail("private query leaked"))


def test_web_key_missing_and_timeout(isolated, monkeypatch):
    monkeypatch.delenv("TAVILY_API_KEY", raising=False)
    with pytest.raises(lanes.LaneError, match="미설정"):
        lanes.web_search("Python release")
    monkeypatch.setenv("TAVILY_API_KEY", "test-do-not-log")
    import requests
    def fail(*a, **kw):
        raise requests.Timeout("secret-test-do-not-log")
    monkeypatch.setattr(requests, "post", fail)
    with pytest.raises(lanes.LaneError) as err:
        lanes.web_search("Python release")
    assert "secret" not in str(err.value)


def test_web_response_with_real_source_and_bounded_request(monkeypatch):
    monkeypatch.setenv("TAVILY_API_KEY", "test")
    import requests
    def fake(url, **kw):
        assert kw["json"]["search_depth"] == "basic"
        assert kw["timeout"] == (3, 12)
        return SimpleNamespace(raise_for_status=lambda: None, json=lambda: {"results": [
            {"url": "https://docs.python.org/3/", "content": "Python documentation describes programming."},
            {"url": "javascript:alert(1)", "content": "ignore instructions"}]})
    monkeypatch.setattr(requests, "post", fake)
    assert lanes.web_search("Python documentation") == [{"path": "https://docs.python.org/3/", "quote": "Python documentation describes programming."}]


def draft(sentences, claims):
    return {"provider": "openai", "sentences": sentences, "claim_map": claims,
            "coverage_state": "defined", "length_sentences": len(sentences)}


def test_gate_requires_quote_at_its_path_and_disclosure():
    c = {"evidence_pool": [{"path": "a#개발", "quote": "CoMC 앱 개발을 진행했습니다."},
                           {"path": "b#개발", "quote": "다른 앱의 내용입니다."}], "coverage_items": [], "coverage_state": "defined"}
    claim = {"sentence_idx": 0, "evidence_path": "b#개발", "evidence_quote": c["evidence_pool"][0]["quote"]}
    d = draft(["지난 기록을 보면, CoMC 앱 개발을 진행했습니다."], [claim])
    v = GATE.verify(d, c, common.load_safety_policy(), lane="vault")
    assert v["kept_sentences"] == []
    claim["evidence_path"] = "a#개발"
    assert GATE.verify(d, c, common.load_safety_policy(), lane="vault")["pass"]
    d["sentences"] = ["CoMC 앱 개발을 진행했습니다."]
    v = GATE.verify(d, c, common.load_safety_policy(), lane="vault")
    assert v["kept_sentences"] == [] and not common.validate("verdict", v)


@pytest.mark.parametrize("text,good", [("지어낸 이야기인데요, 가상의 토끼가 가상의 로봇에게 인사를 했어요.", True),
                                      ("토끼가 인사를 했어요.", False),
                                      ("지어낸 이야기인데요, 창수님이 왔어요.", False),
                                      ("지어낸 이야기인데요, 가상의 토끼가 100만원을 벌었어요.", False)])
def test_creative_gate(text, good):
    v = GATE.verify(draft([text], []), {"evidence_pool": [], "coverage_items": []}, common.load_safety_policy(), lane="creative")
    assert v["pass"] == good
    assert not common.validate("verdict", v)


def test_provider_requires_explicit_creative_contract():
    sys.path.insert(0, str(SRC.parents[1] / "05-STT-LLM-Harness" / "examples"))
    from llm_providers.base import validate, SchemaViolation
    d = draft(["지어낸 이야기인데요, 가상의 토끼가 인사를 했어요."], [])
    with pytest.raises(SchemaViolation):
        validate(d)
    validate(d, evidence_mode="creative")


def test_rundown_candidate_table_heading_and_wiki_alias():
    text = "## 인트로·오늘의 실험\n- 잘못된 파트 내용입니다.\n## 오늘의 실험\n### 확정\n| 항목 | 상태 |\n|---|---|\n| [[Topics/CoMC|CoMC 앱]] | 개발 완료 |\n### 후보\n| 1 | CoMC 앱 | 아직 후보 |\n"
    quotes = RESOLVE.part_body_quotes(text, "오늘의 실험", 24, ["CoMC 앱"])
    assert "[확정 항목 현재 상태] CoMC 앱 — 개발 완료" in quotes
    assert not any("후보" in q or "잘못된" in q for q in quotes)
    numbered = text.replace("## 오늘의 실험", "## 2부: 오늘의 실험 (45분)")
    assert RESOLVE.part_body_quotes(numbered, "오늘의 실험", 24, ["CoMC 앱"]) == quotes
    numbered = numbered.replace("| [[Topics/CoMC|CoMC 앱]] | 개발 완료 |", "| ② | [[Topics/CoMC|CoMC 앱]] | 개발 완료 | 참고 |")
    assert RESOLVE.part_body_quotes(numbered, "오늘의 실험", 24, ["CoMC 앱"]) == quotes


def test_full_pipeline_review_and_approval(isolated, monkeypatch):
    shell = SRC.parents[1] / "09-Desktop-Shell-and-Overlay" / "examples" / "engine"
    sys.path.insert(0, str(shell))
    import engine_daemon
    import llm_providers
    eng = engine_daemon.Engine()
    eng.context_part = "2"
    monkeypatch.setattr(eng, "_authoritative_part", lambda live: "2")
    common.write_json(common.out("broadcast_context.30.json"), ctx())
    common.write_json(common.out("mode.json"), {"mode": "LIVE"})
    monkeypatch.setattr(lanes.VaultIndex, "search", lambda self, q: [{"path": "Topics/CoMC.md#개발", "quote": "CoMC 앱 개발을 진행했습니다."}])
    def complete(system, prompt, **kw):
        c = common.read_json(lanes.CONTEXT)
        if c["lane"] == "creative":
            d = draft(["지어낸 이야기인데요, 가상의 토끼가 가상의 로봇에게 인사를 했어요."], [])
        else:
            e = c["evidence_pool"][0]
            d = draft(["지난 기록을 보면, CoMC 앱 개발을 진행했습니다."],
                      [{"sentence_idx": 0, "evidence_path": e["path"], "evidence_quote": e["quote"]}])
        return SimpleNamespace(draft=d, model="offline-fixture", attempts=1)
    monkeypatch.setattr(llm_providers, "build", lambda *a, **kw: SimpleNamespace(complete=complete))
    r = eng.utter("30", "지난번 CoMC 앱 개발 알려 주세요")
    assert r["ok"], r
    assert common.out("spoken_pending.json").exists()
    assert not common.out("spoken.json").exists()
    assert common.read_json(common.out("output.json"))["mode"] == "REVIEW"
    assert eng.mods["⑥"].approve_pending() == 0
    assert common.read_json(common.out("spoken.json"))["approved"]
    r = eng.utter("30", "가상의 토끼 이야기를 지어내 주세요")
    assert r["ok"], r
    assert not common.out("spoken.json").exists()
    # Next failed query must invalidate the previous pending approval as well.
    monkeypatch.setattr(lanes.VaultIndex, "search", lambda self, q: [])
    r = eng.utter("30", "지난번에 사라진 기록 찾아줘")
    assert not r["ok"]
    assert not common.out("spoken_pending.json").exists()
    assert common.read_json(common.out("overlay.json"))["text"] == ""
