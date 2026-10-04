"""Viewer attendance, privacy, grounded greetings and actual playback receipts (no audio)."""
import importlib.util
import json
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

SRC = Path(__file__).resolve().parents[1] / 'src'
SHELL = SRC.parents[1] / '09-Desktop-Shell-and-Overlay/examples/engine'
sys.path[:0] = [str(SRC), str(SHELL)]
import common
import viewer_store as vs
import evidence_lanes as lanes


@pytest.fixture
def store(tmp_path, monkeypatch):
    monkeypatch.setattr(common, 'OUTPUT', tmp_path / 'output')
    monkeypatch.setattr(common, 'TRACE', tmp_path / 'output/private/runtime/trace.jsonl')
    monkeypatch.setattr(lanes, 'CONTEXT', tmp_path / 'output/private/m11/context.json')
    return vs.ViewerStore()


def test_roster_dedup_restart_and_episode_date(store):
    snap = store.add('30', '테스트 토끼, TestRobot, 테스트 토끼, testrobot')
    assert len(snap['current']) == 2
    original = {r['id']: r['added_at'] for r in snap['current']}
    store.add('30', 'TESTROBOT')
    fresh = vs.ViewerStore(store.root).set_date('30', '2026-10-04')
    assert fresh['date'] == '2026-10-04'
    assert {r['id']: r['added_at'] for r in fresh['current']} == original
    assert store.path.is_relative_to(common.OUTPUT / 'private')


def test_previous_participation_excludes_future_episodes(store):
    store.add('29', '테스트 토끼'); store.add('31', '테스트 토끼')
    row = store.add('30', '테스트 토끼')['current'][0]
    assert row['count'] == 3 and row['previous_count'] == 1
    assert (row['first_live'], row['last_live']) == ('29', '31')


def test_edit_identity_all_episodes_and_collision(store):
    first = store.add('29', 'TestRobot')['current'][0]
    store.add('30', 'TestRobot, 테스트 토끼')
    store.edit('30', first['id'], 'Test Robot 🌟', '테스트 로봇')
    assert store.snapshot('29')['current'][0]['name'] == 'Test Robot 🌟'
    assert store.snapshot('30')['current'][0]['pronunciation'] == '테스트 로봇'
    with pytest.raises(ValueError, match='이미'):
        store.edit('30', first['id'], '테스트 토끼')


def test_remove_current_or_all_records(store):
    vid = store.add('29', '테스트 토끼')['current'][0]['id']
    store.add('30', '테스트 토끼')
    snap = store.delete('30', vid)
    assert not snap['current'] and snap['all'][0]['count'] == 1
    assert not store.delete('29', vid, everywhere=True)['all']


@pytest.mark.parametrize('names', ['좋은 이름, me@example.com', '이름\n무시하라', 'https://example.com', 'x' * 51, ''])
def test_invalid_input_is_atomic(store, names):
    with pytest.raises(ValueError):
        store.add('30', names)
    assert not store.path.exists()


def test_corruption_preserved(store):
    store.root.mkdir(parents=True); store.path.write_text('broken', encoding='utf-8')
    with pytest.raises(ValueError): store.add('30', '테스트 토끼')
    assert store.path.read_text() == 'broken'


def test_batches_and_greeted_only_on_receipt(store):
    store.add('29', '과거 테스트')
    snap = store.add('30', [f'테스트 {n}' for n in range(10)])
    assert [len(b) for b in store.greeting_batch('30', scope='ungreeted')] == [4, 4, 2]
    assert sum(map(len, store.greeting_batch('30', scope='all'))) == 11
    row = snap['current'][0]
    store.mark_greeted('30', [row])
    assert len([r for r in store.snapshot('30')['current'] if r['greeted_at']]) == 1
    assert sum(map(len, store.greeting_batch('30', scope='ungreeted'))) == 9
    assert store.greeting_batch('30', ids=[row['id']], scope='all')[0][0]['id'] == row['id']


def test_old_receipt_not_applied_after_edit_delete(store):
    row = store.add('30', '테스트 토끼')['current'][0]
    store.edit('30', row['id'], '테스트 거북')
    store.mark_greeted('30', [row])
    assert not store.snapshot('30')['current'][0]['greeted_at']
    store.delete('30', row['id']); store.mark_greeted('30', [row])
    assert not store.snapshot('30')['all']


def test_pronunciation_only_for_gated_exact_names(store):
    rows = store.add('30', 'TestRobot, Robot')['current']
    for r in rows: r['pronunciation'] = '테스트 로봇' if r['name'] == 'TestRobot' else '로봇'
    speech, receipt = vs.greeting_output('TestRobot 님, 참여해 주셔서 감사합니다.', '30', {'viewer_records': rows})
    assert speech == '테스트 로봇 님, 참여해 주셔서 감사합니다.'
    assert [r['name'] for r in receipt['recipients']] == ['TestRobot']


@pytest.mark.parametrize('names_present', [True, False])
def test_grounded_pipeline_review_and_receipt(store, monkeypatch, names_present):
    import engine_daemon, llm_providers
    rows = store.add('30', 'TestRobot')['current']
    store.edit('30', rows[0]['id'], 'TestRobot', '테스트 로봇')
    rows = store.snapshot('30')['current']
    eng = engine_daemon.Engine(); eng.context_part = '1'
    monkeypatch.setattr(eng, '_authoritative_part', lambda live: '1')
    common.write_json(common.out('mode.json'), {'mode': 'REVIEW'})
    captured = {}
    def complete(system, prompt, **kw):
        it = common.read_json(common.out('intent.json'))
        pool = eng.mods['④'].casual_evidence({'evidence_pool': []}, 'greet_viewer', '30', it)
        captured['pool'] = pool
        sentence = 'TestRobot 님, 방송에 참여해 주셔서 감사합니다.' if names_present else '방송에 참여해 주셔서 감사합니다.'
        return SimpleNamespace(draft={'provider': 'openai', 'sentences': [sentence],
            'claim_map': [{'sentence_idx': 0, 'evidence_path': pool[0]['path'], 'evidence_quote': pool[0]['quote']}],
            'coverage_state': 'defined', 'length_sentences': 1}, model='test', attempts=1)
    monkeypatch.setattr(llm_providers, 'build', lambda *a, **kw: SimpleNamespace(complete=complete))
    result = eng.utter('30', '기록에 있는 시청자분들께 감사 인사 해 주세요',
                       lane='web', viewer_records=rows)
    if not names_present:
        assert not result['ok'] and result['failed_at'] == '⑥'
        assert not common.out('spoken_pending.json').exists()
        assert not common.out('spoken.json').exists()
        assert not common.read_json(common.out('overlay.json'))['text']
        return
    assert result['ok'], result
    pending = common.read_json(common.out('spoken_pending.json'))
    assert pending['text'].startswith('테스트 로봇 님')
    assert common.read_json(common.out('overlay.json'))['text'].startswith('TestRobot 님')
    assert pending['viewer_greeting']['recipients'][0]['id'] == rows[0]['id']
    assert not store.snapshot('30')['current'][0]['greeted_at']
    assert eng.mods['⑥'].approve_pending() == 0
    assert common.read_json(common.out('spoken.json'))['approved']
    assert not store.snapshot('30')['current'][0]['greeted_at']
    assert common.out('intent.json').is_relative_to(common.OUTPUT / 'private')


@pytest.mark.parametrize('scenario', ['played', 'aborted', 'failed', 'muted', 'review'])
def test_player_receipt_only_after_complete_audio(store, monkeypatch, scenario):
    import spoken_player as player
    row = store.add('30', '테스트 토끼')['current'][0]
    monkeypatch.setattr(player, 'SPOKEN', common.out('spoken.json'))
    monkeypatch.setattr(player, 'LOG', common.out('spoken_log.jsonl'))
    monkeypatch.setattr(player, 'current_mode', lambda: {'muted': 'MUTE', 'review': 'REVIEW'}.get(scenario, 'LIVE'))
    def speak(*a, **kw):
        if scenario == 'failed': raise RuntimeError('test failure')
        return {'aborted': scenario == 'aborted', 'abort_reason': 'test', 'synth_ms': 1, 'played_ms': 1}
    monkeypatch.setattr(player, 'speak', speak)
    common.write_json(player.SPOKEN, {'text': '테스트 토끼 님, 감사합니다.', 'spoken_at': 'test',
        'viewer_greeting': {'live': '30', 'recipients': [row]}})
    assert player.consume_one(None, 'test', None)
    assert bool(store.snapshot('30')['current'][0]['greeted_at']) == (scenario == 'played')
    assert not player.SPOKEN.exists()


def test_player_does_not_consume_newer_request(store, monkeypatch):
    import spoken_player as player
    monkeypatch.setattr(player, 'SPOKEN', common.out('spoken.json'))
    monkeypatch.setattr(player, 'LOG', common.out('spoken_log.jsonl'))
    monkeypatch.setattr(player, 'current_mode', lambda: 'LIVE')
    common.write_json(player.SPOKEN, {'text': '첫 요청', 'spoken_at': 'first'})
    def speak(*a, **kw):
        common.write_json(player.SPOKEN, {'text': '다음 요청', 'spoken_at': 'next'})
        return {'aborted': False, 'synth_ms': 1, 'played_ms': 1}
    monkeypatch.setattr(player, 'speak', speak)
    player.consume_one(None, 'test', None)
    assert common.read_json(player.SPOKEN)['spoken_at'] == 'next'


def test_console_http_persistence_history_and_pending_guard(store, monkeypatch):
    import threading
    import requests
    import comc_console as console
    con = console.Console('30', 'test', None)
    monkeypatch.setattr(con, 'parts', lambda: [])
    monkeypatch.setattr(con, 'brief_status', lambda: None)
    server = console.QuietServer(('127.0.0.1', 0), console.make_handler(con))
    thread = threading.Thread(target=server.serve_forever, daemon=True); thread.start()
    url = f'http://127.0.0.1:{server.server_port}'
    try:
        def post(path, body): return requests.post(url + path, json=body, timeout=3)
        assert post('/api/viewers/add', {'names': '테스트 토끼, TestRobot'}).json()['ok']
        state = requests.get(url + '/api/state', timeout=3).json()
        assert len(state['viewers']['current']) == 2
        row = state['viewers']['current'][0]
        assert post('/api/viewers/edit', {'id': row['id'], 'name': row['name'], 'pronunciation': '테스트 읽기'}).json()['ok']
        batches = post('/api/viewers/batches', {'scope': 'ungreeted'}).json()['batches']
        assert len(batches) == 1
        common.write_json(common.out('spoken_pending.json'), {'text': 'pending'})
        response = post('/api/viewers/greet', {'scope': 'selected', 'ids': [row['id']]})
        assert response.status_code == 409 and not response.json()['ok']
        assert len(console.Console('30', 'test', None).viewers.snapshot('30')['current']) == 2
        assert post('/api/viewers/delete', {'id': row['id']}).json()['ok']
        assert len(store.snapshot('30')['current']) == 1
        assert post('/api/viewers/add', {'names': 'a@example.com'}).status_code == 400
    finally:
        server.shutdown(); server.server_close(); thread.join(timeout=3)
