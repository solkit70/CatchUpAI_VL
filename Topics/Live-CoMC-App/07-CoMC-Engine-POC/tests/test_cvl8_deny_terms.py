"""CVL8 uses only synthetic private terms and synthetic personal sources."""
import importlib.util
import json
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

SRC = Path(__file__).resolve().parents[1] / 'src'
sys.path.insert(0, str(SRC))
import common
import deny_terms as deny
import evidence_lanes as lanes


def stage(name):
    spec = importlib.util.spec_from_file_location('cvl8_' + name[:2], SRC / name)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m


GATE = stage('05_verify_and_gate.py')
RENDER = stage('06_render_output.py')
CANARY = '회귀금칙카나리아'


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    monkeypatch.setattr(common, 'OUTPUT', tmp_path / 'output')
    monkeypatch.setattr(common, 'TRACE', tmp_path / 'output/private/trace.jsonl')
    monkeypatch.setattr(lanes, 'CONTEXT', tmp_path / 'output/private/m11/context.json')
    monkeypatch.setattr(lanes, 'PRIVATE', tmp_path / 'output/private/m11')
    p = common.out('private') / 'm11/deny_terms.json'
    common.write_json(p, {'version': 1, 'terms': [{'term': CANARY, 'kind': 'customer', 'note': ''},
                                                {'term': 'Test Partner', 'kind': 'partner', 'note': ''}]})
    return tmp_path, p


@pytest.mark.parametrize('text', [CANARY + '는', CANARY + '의', 'ＴＥＳＴ　ＰＡＲＴＮＥＲ의', 'test   partner가'])
def test_normalized_partial_match(isolated, text):
    assert deny.matches(text)


@pytest.mark.parametrize('field', ['quote', 'title', 'path'])
def test_index_and_use_recheck(isolated, field):
    root, p = isolated
    vault = root / 'vault'; (vault / 'Journal').mkdir(parents=True)
    note = vault / 'Journal/합성.md'
    note.write_text('## 합성 실험\n회귀실험 개발 확인을 완료했고 방송 확인이 남아 있다.\n', encoding='utf-8')
    idx = lanes.VaultIndex(vault, root / 'index.sqlite3'); idx.build()
    assert idx.search('회귀실험')
    if field == 'quote':
        note.write_text(f'## 합성 실험\n회귀실험 {CANARY}는 개발 확인을 완료했다.\n', encoding='utf-8')
    elif field == 'path':
        note = note.rename(note.with_name(CANARY + '.md'))
    else:
        # A section title is also part of the evidence path.
        note.write_text(f'## {CANARY}\n회귀실험 개발 확인을 완료했다.\n', encoding='utf-8')
    assert idx.search('회귀실험') == []
    idx.build()
    assert idx.search('회귀실험') == []


def test_new_terms_exclude_preexisting_index(isolated):
    root, p = isolated
    vault = root / 'vault'; vault.mkdir()
    (vault / '합성.md').write_text('## 공개 실험\n회귀실험 미래금칙합성어 테스트는 완료했다.\n', encoding='utf-8')
    idx = lanes.VaultIndex(vault, root / 'index.sqlite3'); idx.build()
    assert idx.search('회귀실험')
    common.write_json(p, {'version': 1, 'terms': [{'term': '미래금칙합성어', 'kind': 'money'}]})
    assert idx.search('회귀실험') == []


@pytest.mark.parametrize('lane', ['vault', 'web', 'auto'])
def test_question_refused_without_search(isolated, lane):
    intent = {'transcript': CANARY + '의 기록을 설명해 주세요', 'slots': {}, 'ambiguity_flags': []}
    with pytest.raises(lanes.LaneError, match='방송에서 다루지 않는'):
        lanes.resolve(intent, {}, selected=lane,
                      searcher=lambda q: pytest.fail('vault called'), web=lambda q: pytest.fail('web called'))
    with pytest.raises(lanes.LaneError):lanes.web_search(intent['transcript'])


@pytest.mark.parametrize('lane', ['broadcast', 'casual', 'vault', 'web', 'creative'])
def test_gate_drops_sentence_all_lanes(isolated, lane):
    sent = CANARY + '는 이번 실험을 진행했다.'
    ctx = {'evidence_pool': [{'path': 'Topics/합성#실험', 'quote': sent}],
           'coverage_items': ['실험'], 'coverage_state': 'defined', 'current_part_id': '1'}
    draft = {'sentences': [sent], 'claim_map': [{'sentence_idx': 0,
             'evidence_path': ctx['evidence_pool'][0]['path'], 'evidence_quote': sent}],
             'coverage_state': 'defined', 'length_sentences': 1}
    v = GATE.verify(draft, ctx, common.load_safety_policy(), lane=lane)
    assert not v['pass'] and not v['final_text']
    assert v['violations'][0]['rule_id'] == 'm11.deny_term'
    assert CANARY not in json.dumps(v, ensure_ascii=False)


@pytest.mark.parametrize('bad', [None, '{', '{"version":1,"terms":null}', '[]'])
def test_missing_or_broken_list_safe(isolated, bad):
    _, p = isolated
    if bad is None:p.unlink()
    else:p.write_text(bad, encoding='utf-8')
    assert deny.status()['count'] == 0 and deny.status()['warning']
    assert not deny.matches(CANARY)


def test_no_term_in_trace_or_public_output(isolated):
    common.trace('synthetic', detail=CANARY + '의 자료', values={'path': 'Journal/' + CANARY})
    common.write_json(common.OUTPUT / 'public.json', {'text': CANARY + '는 공개하지 않는다'})
    assert CANARY not in common.TRACE.read_text(encoding='utf-8')
    assert CANARY not in (common.OUTPUT / 'public.json').read_text(encoding='utf-8')


@pytest.mark.parametrize('path,expected', [('Journal/합성.md#실험', True), ('AI/Roundup/합성.md#실험', True),
                                         ('AI/Tasks/items/합성.md#실험', False), ('Topics/합성.md#실험', False)])
def test_warning_from_kept_claim_map_only(isolated, path, expected):
    d = {'claim_map': [{'sentence_idx': 0, 'evidence_path': path},
                       {'sentence_idx': 1, 'evidence_path': 'Journal/버린문장.md#제외'}]}
    result = deny.review_sources(d, [0])
    assert result['personal_record'] == expected and result['sources'] == [path]


def test_web_evidence_filters_all_fields(isolated, monkeypatch):
    import requests
    monkeypatch.setenv('TAVILY_API_KEY', 'synthetic')
    rows = [{'url': 'https://example.org/good', 'title': '합성 공개 서비스', 'content': '합성 공개 서비스 설명입니다.'},
            {'url': 'https://example.org/' + CANARY, 'title': '합성', 'content': '합성 서비스 설명입니다.'},
            {'url': 'https://example.org/title', 'title': CANARY, 'content': '합성 서비스 설명입니다.'},
            {'url': 'https://example.org/quote', 'title': '합성', 'content': CANARY + '의 합성 설명입니다.'}]
    monkeypatch.setattr(requests, 'post', lambda *a, **kw: SimpleNamespace(raise_for_status=lambda: None, json=lambda: {'results': rows}))
    assert [e['path'] for e in lanes.web_search('합성 공개 서비스')] == ['https://example.org/good']


def test_render_warning_private_not_overlay(isolated, monkeypatch):
    ctx = {'current_part_id': '1'}
    common.write_json(common.out('broadcast_context.30.json'), ctx)
    common.write_json(common.out('mode.json'), {'mode': 'REVIEW'})
    common.write_json(common.out('answer_draft.json'), {'claim_map': [{'sentence_idx': 0, 'evidence_path': 'Journal/합성.md#실험'}]})
    common.write_json(common.out('verdict.json'), {'pass': True, 'kept_sentences': [0], 'dropped_sentences': [], 'final_text': '합성 공개 실험을 진행했습니다.'})
    monkeypatch.setattr(sys, 'argv', ['render', '--live', '30'])
    assert RENDER.main() == 0
    metadata = common.read_json(common.out('private') / 'm11/review_sources.json')
    assert metadata['personal_record'] and metadata['sources'] == ['Journal/합성.md#실험']
    assert metadata['spoken_at'] == common.read_json(common.out('spoken_pending.json'))['spoken_at']
    assert 'personal_record' not in common.read_json(common.out('overlay.json'))
    assert RENDER.approve_pending() == 0


@pytest.mark.parametrize('same_pending', [True, False])
def test_console_warning_matches_pending_answer(isolated, monkeypatch, same_pending):
    sys.path.insert(0, str(SRC.parents[1] / '09-Desktop-Shell-and-Overlay/examples/engine'))
    import comc_console as console
    con = console.Console.__new__(console.Console)
    con.live = '30'; con.busy = con.playing = False; con.results = []; con.log = []
    con.preflight = None; con.started = ''; con.parts = lambda: []; con.brief_status = lambda: None
    con.viewers = con.personas = SimpleNamespace(snapshot=lambda live: {})
    monkeypatch.setattr(console.spoken_player, 'current_mode', lambda: 'REVIEW')
    common.write_json(common.out('spoken_pending.json'), {'spoken_at': 'new'})
    common.write_json(common.out('private') / 'm11/review_sources.json',
                      {'spoken_at': 'new' if same_pending else 'old', 'personal_record': True, 'sources': ['Journal/합성#실험']})
    result = con.state()
    assert bool(result['review_sources']) == same_pending
    assert result['deny_terms']['count'] == 2


def test_console_log_redacts_term(isolated, monkeypatch):
    import io
    sys.path.insert(0, str(SRC.parents[1] / '09-Desktop-Shell-and-Overlay/examples/engine'))
    import comc_console as console
    stream = io.StringIO(); monkeypatch.setattr(console.ROUTER, 'real', stream)
    con = console.Console.__new__(console.Console); con.log = []
    con.note('ask', CANARY + '의 합성 질문')
    assert CANARY not in stream.getvalue() and CANARY not in json.dumps(con.log, ensure_ascii=False)


# ── CVL8 후속 (10/2): 금칙 목록 캐시 — 볼트 검색 1회에 파일을 수만 번 읽던 지연 해소 ──

def test_cache_reads_file_once_while_unchanged(isolated, monkeypatch):
    _, p = isolated
    calls = []
    real = deny._read
    monkeypatch.setattr(deny, '_read', lambda path: calls.append(path) or real(path))
    deny._cache['key'] = None
    for _ in range(500):
        assert deny.matches(CANARY + '는') == ['customer']
    assert len(calls) == 1


def test_edit_during_broadcast_is_picked_up(isolated):
    _, p = isolated
    deny._cache['key'] = None
    assert deny.matches('새금칙단어') == []
    import os, time
    common.write_json(p, {'version': 1, 'terms': [{'term': '새금칙단어', 'kind': 'money', 'note': '추가'}]})
    st = os.stat(p)
    os.utime(p, ns=(st.st_atime_ns, st.st_mtime_ns + 1_000_000))   # 같은 시각에 고쳐도 바뀐 것으로 보이게
    assert deny.matches('새금칙단어는') == ['money']
    assert deny.matches(CANARY) == []


def test_deleted_file_falls_back_to_empty_list(isolated):
    _, p = isolated
    deny._cache['key'] = None
    assert deny.matches(CANARY)
    p.unlink()
    assert deny.matches(CANARY) == []
    assert deny.status()['warning'] == 'missing'
