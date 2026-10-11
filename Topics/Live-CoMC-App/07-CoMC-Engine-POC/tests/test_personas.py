"""Persona style isolation, persistence, voice routing and friend-source restrictions."""
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
import persona_store as ps
import evidence_lanes as lanes


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    monkeypatch.setattr(common, 'OUTPUT', tmp_path / 'output')
    monkeypatch.setattr(common, 'TRACE', tmp_path / 'trace.jsonl')
    monkeypatch.setattr(lanes, 'CONTEXT', tmp_path / 'context.json')
    return ps.PersonaStore()


def context():
    return {'evidence_pool': [{'path': 'Topics/CoMC.md#실험', 'quote': 'CoMC 앱 실험은 3개이며 완료됐다.'}],
            'coverage_items': ['CoMC 앱'], 'coverage_state': 'defined', 'current_part_id': '2', 'other_parts': []}


def setup_engine(monkeypatch):
    import engine_daemon
    eng = engine_daemon.Engine(); eng.context_part = '2'
    monkeypatch.setattr(eng, '_authoritative_part', lambda live: '2')
    common.write_json(common.out('broadcast_context.30.json'), context())
    common.write_json(common.out('mode.json'), {'mode': 'REVIEW'})
    return eng


def test_definitions_and_selection_persistence(isolated):
    assert len(ps.definitions()['personas']) == 5
    assert isolated.current()['id'] == 'default'
    isolated.select('30', 'friend')
    assert ps.PersonaStore().current()['id'] == 'friend'
    isolated.note_episode('30', '테스트 반응 메모')
    snap = ps.PersonaStore().snapshot('30')
    assert snap['history'][0]['event'] == 'selected'
    assert snap['notes'] == '테스트 반응 메모'
    assert not isolated.snapshot('31')['history']
    assert isolated.path.is_relative_to(common.out('private'))
    with pytest.raises(ValueError): isolated.select('30', 'unknown')
    assert isolated.current()['id'] == 'friend'


def test_bad_state_and_configuration_preserved(isolated, tmp_path):
    isolated.root.mkdir(parents=True); isolated.path.write_text('broken')
    with pytest.raises(ValueError): isolated.select('30', 'anchor')
    assert isolated.path.read_text() == 'broken'
    data = ps.definitions(); data['personas'][1]['tts']['pitch'] = 'malformed'
    p = tmp_path / 'bad.json'; p.write_text(json.dumps(data), encoding='utf-8')
    with pytest.raises(ValueError): ps.definitions(p)


@pytest.mark.parametrize('persona_id', ['student', 'college', 'anchor', 'friend'])
def test_same_facts_and_frozen_persona_across_pipeline(isolated, monkeypatch, persona_id):
    import llm_providers
    isolated.select('30', persona_id); profile = isolated.current()
    eng = setup_engine(monkeypatch)
    end = '완료됐어.' if profile['speech'] == 'casual' else '완료됐어요.'
    sentence = 'CoMC 앱 실험은 3개이고 ' + end
    def complete(system, prompt, **kwargs):
        assert profile['style'] in system and 'AI 공동 진행자' in system
        # Switch during generation: current output must retain the captured character/voice.
        isolated.select('30', 'default')
        ev = context()['evidence_pool'][0]
        return SimpleNamespace(draft={'provider': 'openai', 'sentences': [sentence.rstrip('.')],
            'claim_map': [{'sentence_idx': 0, 'evidence_path': ev['path'], 'evidence_quote': ev['quote']}],
            'coverage_state': 'defined', 'length_sentences': 1}, model='fixture', attempts=1)
    monkeypatch.setattr(llm_providers, 'build', lambda *a, **kw: SimpleNamespace(complete=complete))
    result = eng.utter('30', 'CoMC 앱 실험은 몇 개이며 상태가 뭐예요?', lane='rundown')
    assert result['ok'], result
    output = common.read_json(common.out('output.json'))
    assert output['overlay']['text'] == sentence
    assert output['spoken']['voice'] == profile['tts']['ko']
    assert output['spoken']['rate'] == profile['tts']['rate']
    assert output['spoken']['persona']['id'] == persona_id
    assert not common.out('spoken.json').exists()
    assert eng.mods['⑥'].approve_pending() == 0
    assert common.read_json(common.out('spoken.json'))['persona']['id'] == persona_id
    assert isolated.current()['id'] == 'default'
    assert isolated.snapshot('30')['history'][-1]['persona_id'] == persona_id
    assert isolated.snapshot('30')['history'][-1]['event'] == 'rendered'


def test_friend_story_forces_vault_and_missing_source_never_web(isolated, monkeypatch):
    isolated.select('30', 'friend'); eng = setup_engine(monkeypatch)
    monkeypatch.setattr(lanes.VaultIndex, 'search', lambda *a: [])
    monkeypatch.setattr(lanes, 'web_search', lambda *a: pytest.fail('private story leaked to web'))
    result = eng.utter('30', '창수님의 예전 CoMC 개발 이야기를 지어내 주세요', lane='creative')
    assert not result['ok'] and result['failed_at'] == '④'
    intent = common.read_json(common.out('intent.json'))
    assert intent['slots']['evidence_lane'] == 'vault'
    assert not common.out('spoken_pending.json').exists()


def test_friend_privacy_and_control_intents(isolated):
    isolated.select('30', 'friend')
    for intent_name in ['stop', 'repeat', 'advance_part', 'out_of_scope', 'greet_viewer']:
        intent = {'intent': intent_name, 'transcript': '창수님의 가족 건강과 예전 이야기', 'slots': {}, 'ambiguity_flags': []}
        assert ps.bind_intent(intent) == 'auto'
        assert intent['intent'] == intent_name


@pytest.mark.parametrize('text,blocked', [
    ('우리 예전에 함께 CoMC 앱을 만들었잖아.', True),
    ('나는 실제 고등학생이야.', True),
    ("I'm a real student.", True),
    ("I'm not a real student. I am an AI co-host.", False),
    ('나는 실제 친구는 아니고 AI 공동 진행자야.', False),
    ('지난 기록을 보면, 창수님이 CoMC 앱을 개발했어.', False),
    ('나는 AI 공동 진행자 코엠씨야.', False)])
def test_character_identity_and_shared_memory_policy(isolated, text, blocked):
    isolated.select('30', 'friend')
    intent = {'transcript': '설명해 주세요', 'slots': {'persona': isolated.current()}}
    verdict = {'pass': True, 'kept_sentences': [0], 'dropped_sentences': [], 'violations': [],
               'final_text': text, 'length_after': 1, 'absence_by_closure': []}
    result = ps.apply_policy(verdict, {'sentences': [text]}, intent)
    assert result['pass'] == (not blocked)
    if blocked: assert result['dropped_sentences'][0]['reason'] == 'persona_policy'


def test_self_introduction_must_disclose_ai(isolated):
    isolated.select('30', 'student')
    intent = {'transcript': '자기소개 해 주세요', 'slots': {'persona': isolated.current()}}
    verdict = {'pass': True, 'kept_sentences': [0], 'dropped_sentences': [], 'violations': [],
               'final_text': '나는 하늘이야.', 'length_after': 1, 'absence_by_closure': []}
    assert not ps.apply_policy(verdict, {'sentences': ['나는 하늘이야.']}, intent)['pass']


def test_introduction_instruction_recital_is_blocked(isolated):
    isolated.select('30', 'student')
    text = '출처를 알리는 첫 구절: 나는 AI 공동 진행자 코엠씨야.'
    verdict = {'pass': True, 'kept_sentences': [0], 'dropped_sentences': [], 'violations': [],
               'final_text': text, 'length_after': 1, 'absence_by_closure': []}
    result = ps.apply_policy(verdict, {'sentences': [text]},
                             {'transcript': '자기소개 해 주세요', 'slots': {'persona': isolated.current()}})
    assert not result['pass'] and result['final_text'] == ''


def test_emergency_controls_ignore_corrupted_character_state(isolated):
    isolated.root.mkdir(parents=True); isolated.path.write_text('broken')
    intent = {'intent': 'stop', 'transcript': '멈춰', 'slots': {}, 'ambiguity_flags': []}
    assert ps.bind_intent(intent) == 'auto'
    assert not intent['slots']


@pytest.mark.parametrize('sentence,expected', [('CoMC 앱 실험은 3개이며 완료됐어.', True),
                                            ('CoMC 앱 실험은 3개이며 완료됐다요.', False),
                                            ('CoMC 앱 실험은 47개이며 완료됐어.', False)])
def test_casual_endings_do_not_weaken_facts(isolated, sentence, expected):
    spec = importlib.util.spec_from_file_location('persona_gate', SRC / '05_verify_and_gate.py')
    gate = importlib.util.module_from_spec(spec); spec.loader.exec_module(gate)
    ev = context()['evidence_pool'][0]
    draft = {'provider': 'openai', 'sentences': [sentence], 'claim_map': [
        {'sentence_idx': 0, 'evidence_path': ev['path'], 'evidence_quote': ev['quote']}],
        'coverage_state': 'defined', 'length_sentences': 1}
    assert gate.verify(draft, context(), common.load_safety_policy())['pass'] == expected


@pytest.mark.parametrize('failure', [False, True])
def test_voice_rate_pitch_applied_and_restored(isolated, monkeypatch, failure):
    import numpy as np
    import spoken_player as player
    monkeypatch.setattr(player, 'AUDIO_DIR', common.out('debug') / 'audio')
    seen = []
    prov = SimpleNamespace(voice='old', rate='+0%', pitch='+0Hz')
    def synth(text, path):
        seen.append((prov.voice, prov.rate, prov.pitch))
        if failure: raise RuntimeError('fixture failure')
        return SimpleNamespace(path=path)
    prov.synth = synth
    monkeypatch.setattr(player, 'load_audio', lambda *a: (np.zeros(10), 100))
    monkeypatch.setattr(player, 'play', lambda *a, **kw: {'aborted': False, 'played_ms': 1})
    kwargs = dict(watch_mode=False, tag='test', voice='en-US-GuyNeural', rate='+6%', pitch='+8Hz')
    if failure:
        with pytest.raises(RuntimeError): player.speak('Hello everyone.', prov, 'edge', None, **kwargs)
    else:
        result = player.speak('Hello everyone.', prov, 'edge', None, **kwargs)
        assert result['voice'] == 'en-US-GuyNeural'
    assert seen == [('en-US-GuyNeural', '+6%', '+8Hz')]
    assert (prov.voice, prov.rate, prov.pitch) == ('old', '+0%', '+0Hz')


def test_english_voice_mapping(isolated):
    for profile in ps.definitions()['personas']:
        if profile['tts']:
            assert ps.voice_settings(profile, 'en')['voice'].startswith('en-US-')
            assert ps.voice_settings(profile, 'ko')['voice'].startswith('ko-KR-')


def test_friend_today_part_authority_and_english_privacy(isolated, monkeypatch):
    isolated.select('30', 'friend')
    intent = {'intent': 'answer_question', 'transcript': '창수님 오늘 3부에서 하는 이야기 설명해 주세요',
              'slots': {}, 'ambiguity_flags': []}
    assert ps.bind_intent(intent) == 'auto'
    intent = {'intent': 'unknown', 'transcript': "Tell us about the host's past family stories", 'slots': {}, 'ambiguity_flags': []}
    assert ps.bind_intent(intent, 'web') == 'vault'
    with pytest.raises(lanes.LaneError, match='민감'):
        lanes.resolve(intent, context(), selected='vault', searcher=lambda *a: pytest.fail('privacy lookup'))


@pytest.mark.parametrize('aborted', [False, True])
def test_player_uses_frozen_voice_and_records_actual_playback(isolated, monkeypatch, aborted):
    import spoken_player as player
    isolated.select('30', 'student'); profile = isolated.current()
    meta = {k: profile[k] for k in ('id', 'name', 'speech', 'definition_sha256')}; meta['live'] = '30'
    settings = ps.voice_settings(profile, 'ko')
    monkeypatch.setattr(player, 'SPOKEN', common.out('spoken.json'))
    monkeypatch.setattr(player, 'LOG', common.out('spoken_log.jsonl'))
    monkeypatch.setattr(player, 'current_mode', lambda: 'REVIEW')
    monkeypatch.setattr(player, 'load_provider', lambda name: ('edge', SimpleNamespace(voice='old')))
    def speak(*a, **kw):
        assert kw['voice'] == settings['voice'] and kw['rate'] == settings['rate'] and kw['pitch'] == settings['pitch']
        return {'voice': settings['voice'], 'aborted': aborted, 'abort_reason': 'fixture', 'synth_ms': 1, 'played_ms': 1}
    monkeypatch.setattr(player, 'speak', speak)
    common.write_json(player.SPOKEN, {'text': 'AI 코엠씨의 테스트 인사야.', 'persona': meta, 'approved': True,
                                    'spoken_at': 'fixture', **settings})
    isolated.select('30', 'anchor')
    assert player.consume_one(None, 'openai', None)
    played = [r for r in isolated.snapshot('30')['history'] if r['event'] == 'played']
    assert bool(played) == (not aborted)
    if played:
        assert played[0]['persona_id'] == 'student' and played[0]['voice'] == settings['voice']
    assert isolated.current()['id'] == 'anchor'


def test_default_now_uses_explicit_female_persona_voice(isolated, monkeypatch):
    import spoken_player as player
    profile = isolated.current()
    meta = {k: profile[k] for k in ('id', 'name', 'speech', 'definition_sha256')}; meta['live'] = '30'
    monkeypatch.setattr(player, 'SPOKEN', common.out('spoken.json'))
    monkeypatch.setattr(player, 'LOG', common.out('spoken_log.jsonl'))
    monkeypatch.setattr(player, 'current_mode', lambda: 'LIVE')
    monkeypatch.setattr(player, 'load_provider', lambda *a: ('edge', None))
    def speak(*a, **kw):
        assert a[2] == 'edge' and kw['voice'] == 'ko-KR-SunHiNeural'
        return {'voice': kw['voice'], 'aborted': False, 'synth_ms': 1, 'played_ms': 1}
    monkeypatch.setattr(player, 'speak', speak)
    common.write_json(player.SPOKEN, {'text': '기본 음성 테스트입니다.', 'persona': meta,
                                    'provider': 'edge', 'voice': 'ko-KR-SunHiNeural', 'spoken_at': 'fixture'})
    assert player.consume_one(None, 'openai', None)


def test_console_persona_api_persistence_and_busy_selection(isolated, monkeypatch):
    import threading, requests
    import comc_console as console
    con = console.Console('30', 'test', None)
    monkeypatch.setattr(con, 'parts', lambda: [])
    monkeypatch.setattr(con, 'brief_status', lambda: None)
    server = console.QuietServer(('127.0.0.1', 0), console.make_handler(con))
    thread = threading.Thread(target=server.serve_forever, daemon=True); thread.start()
    url = f'http://127.0.0.1:{server.server_port}'
    try:
        con.busy = True
        assert requests.post(url+'/api/persona', json={'id': 'college'}, timeout=3).json()['ok']
        assert requests.post(url+'/api/persona/notes', json={'notes': '테스트 반응 메모'}, timeout=3).json()['ok']
        state = requests.get(url+'/api/state', timeout=3).json()
        assert state['persona']['current']['id'] == 'college'
        assert state['persona']['notes'] == '테스트 반응 메모'
        assert console.Console('30', 'test', None).personas.current()['id'] == 'college'
        assert requests.post(url+'/api/persona', json={'id': 'missing'}, timeout=3).status_code == 400
    finally:
        server.shutdown(); server.server_close(); thread.join(timeout=3)


def test_persona_intro_does_not_need_weather_or_brief(isolated, monkeypatch):
    import llm_providers
    isolated.select('30', 'student'); eng = setup_engine(monkeypatch)
    def complete(*a, **kw):
        it = common.read_json(common.out('intent.json'))
        pool = eng.mods['④'].casual_evidence({'evidence_pool': []}, 'small_talk', '30', it)
        ev = next(e for e in pool if e['path'] == 'persona#ai_character')
        return SimpleNamespace(draft={'provider': 'openai', 'sentences': ['나는 AI 공동 진행자 코엠씨고 가상의 고등학생 캐릭터로 진행해.'],
            'claim_map': [{'sentence_idx': 0, 'evidence_path': ev['path'], 'evidence_quote': ev['quote']}],
            'coverage_state': 'defined', 'length_sentences': 1}, model='fixture', attempts=1)
    monkeypatch.setattr(llm_providers, 'build', lambda *a, **kw: SimpleNamespace(complete=complete))
    assert eng.utter('30', '코엠씨 자기소개 해 주세요')['ok']
    assert common.read_json(common.out('spoken_pending.json'))['persona']['id'] == 'student'


def test_varied_voice_mode_defaults_to_free_and_persists(isolated):
    store = isolated
    assert store.voice_mode() == 'free'
    assert store.snapshot('31')['voice_mode'] == 'free'
    snap = store.set_voice_mode('31', 'varied')
    assert snap['voice_mode'] == 'varied' and ps.PersonaStore().voice_mode() == 'varied'
    with pytest.raises(ValueError):
        store.set_voice_mode('31', 'other')
    assert store.voice_mode() == 'varied'


def test_varied_voices_follow_the_requested_providers_and_are_distinct():
    rows = {r['id']: r for r in ps.definitions()['personas']}
    got = {pid: ps.voice_settings(r, 'ko', 'varied') for pid, r in rows.items()}
    assert got['default']['provider'] == 'edge'
    assert got['college']['provider'] == got['anchor']['provider'] == 'openai'
    assert got['student']['provider'] == got['friend']['provider'] == 'qwen'
    assert len({(g['provider'], g['voice']) for g in got.values()}) == 5


def test_free_mode_keeps_every_persona_on_edge_tts():
    for r in ps.definitions()['personas']:
        s = ps.voice_settings(r, 'ko')
        assert s['provider'] == 'edge' and s['voice'].startswith('ko-KR-')
        assert ps.voice_settings(r, 'ko', 'free') == s


def test_varied_voice_definition_is_validated(tmp_path):
    data = ps.definitions()
    data['personas'][1]['tts_varied']['provider'] = 'unknown'
    path = tmp_path / 'bad_varied.json'
    path.write_text(json.dumps(data, ensure_ascii=False), encoding='utf-8')
    with pytest.raises(ValueError):
        ps.definitions(path)


def test_paid_voice_failure_falls_back_to_edge_instead_of_going_silent(isolated, monkeypatch):
    import numpy as np
    import spoken_player as player
    monkeypatch.setattr(player, 'AUDIO_DIR', common.out('debug') / 'audio')
    paid = SimpleNamespace(voice='old')
    def fail(text, path):
        raise RuntimeError('network down')
    paid.synth = fail
    edge = SimpleNamespace(voice='ko-KR-SunHiNeural', rate='+0%', pitch='+0Hz')
    edge.synth = lambda text, path: SimpleNamespace(path=path)
    monkeypatch.setattr(player, 'load_provider', lambda name: ('edge', edge))
    monkeypatch.setattr(player, 'load_audio', lambda *a: (np.zeros(10), 100))
    r = player.prepare_audio('안녕하세요.', paid, 'openai', None, 'fb', voice='nova')
    assert r['provider'] == 'edge' and r['fallback_from'] == 'openai' and r['voice'] == 'ko-KR-SunHiNeural'
    assert paid.voice == 'old'


def _prefetch_setup(monkeypatch, synth_s, play_s, n_chunks, fail_at=None):
    import time
    import numpy as np
    import spoken_player as player
    monkeypatch.setattr(player, 'AUDIO_DIR', common.out('debug') / 'audio')
    log = []
    prov = SimpleNamespace(voice='nova')
    def synth(text, path):
        log.append(('synth_start', text, time.perf_counter()))
        time.sleep(synth_s)
        if fail_at is not None and text == 'c%d' % fail_at:
            raise RuntimeError('synthesis failed')
        log.append(('synth_end', text, time.perf_counter()))
        return SimpleNamespace(path=path)
    prov.synth = synth
    monkeypatch.setattr(player, 'load_audio', lambda *a: (np.zeros((10, 1)), 100))
    def fake_play(data, sr, device, watch_mode, stop_unless=('LIVE',)):
        log.append(('play_start', None, time.perf_counter()))
        time.sleep(play_s)
        log.append(('play_end', None, time.perf_counter()))
        return {'played_ms': int(play_s * 1000), 'aborted': False, 'abort_reason': None, 'progress': 1.0}
    monkeypatch.setattr(player, 'play', fake_play)
    monkeypatch.setattr(player, '_caption_chunks',
                        lambda *a, **kw: [{'speech': 'c%d' % i, 'text': 'c%d' % i} for i in range(n_chunks)])
    return player, prov, log


def test_next_caption_page_is_synthesized_while_the_current_one_plays(isolated, monkeypatch):
    import time
    player, prov, log = _prefetch_setup(monkeypatch, synth_s=0.3, play_s=0.5, n_chunks=4)
    t0 = time.perf_counter()
    r = player.speak('x', prov, 'openai', None, watch_mode=False, tag='pf', voice='nova')
    elapsed = time.perf_counter() - t0
    # 순차 합성이면 4*(0.3+0.5)=3.2초. 미리 합성하면 0.3 + 4*0.5 = 2.3초 안팎.
    assert elapsed < 2.8, elapsed
    plays = [e for e in log if e[0] in ('play_start', 'play_end')]
    for k in range(1, 4):
        gap = plays[2 * k][2] - plays[2 * k - 1][2]
        assert gap < 0.15, (k, gap)
    assert r['played_ms'] == 2000 and not r['aborted']


def test_prefetched_synthesis_failure_stops_playback_and_raises(isolated, monkeypatch):
    player, prov, log = _prefetch_setup(monkeypatch, synth_s=0.05, play_s=0.1, n_chunks=4, fail_at=2)
    with pytest.raises(RuntimeError):
        player.speak('x', prov, 'edge', None, watch_mode=False, tag='pf2', voice='nova')
    assert len([e for e in log if e[0] == 'play_start']) == 2


def test_single_caption_page_does_not_start_a_background_thread(isolated, monkeypatch):
    import threading
    player, prov, log = _prefetch_setup(monkeypatch, synth_s=0.01, play_s=0.01, n_chunks=1)
    before = threading.active_count()
    player.speak('x', prov, 'edge', None, watch_mode=False, tag='pf3', voice='nova')
    assert threading.active_count() == before


def test_non_edge_voices_synthesize_the_first_two_pages_in_parallel_and_edge_one_at_a_time(isolated, monkeypatch):
    player, prov, log = _prefetch_setup(monkeypatch, synth_s=0.3, play_s=0.2, n_chunks=3)
    player.speak('x', prov, 'openai', None, watch_mode=False, tag='pp', voice='nova')
    starts = {e[1]: e[2] for e in log if e[0] == 'synth_start'}
    assert abs(starts['c1'] - starts['c0']) < 0.1

    player, prov, log = _prefetch_setup(monkeypatch, synth_s=0.3, play_s=0.2, n_chunks=3)
    player.speak('x', prov, 'edge', None, watch_mode=False, tag='pe', voice='nova')
    starts = {e[1]: e[2] for e in log if e[0] == 'synth_start'}
    ends = {e[1]: e[2] for e in log if e[0] == 'synth_end'}
    assert starts['c1'] >= ends['c0'] - 0.01


def test_parallel_synthesis_does_not_overwrite_the_shared_provider_voice(isolated, monkeypatch):
    player, prov, log = _prefetch_setup(monkeypatch, synth_s=0.1, play_s=0.05, n_chunks=4)
    player.speak('x', prov, 'qwen', None, watch_mode=False, tag='pv', voice='Cherry')
    assert prov.voice == 'nova'


def _pause_setup(monkeypatch, n_chunks=3):
    import numpy as np
    import caption_pages
    import spoken_player as player
    monkeypatch.setattr(player, 'AUDIO_DIR', common.out('debug') / 'audio')
    prov = SimpleNamespace(voice='nova', synth=lambda text, path: SimpleNamespace(path=path))
    monkeypatch.setattr(player, 'load_audio', lambda *a: (np.ones((100, 1), dtype='float32'), 100))
    played = []
    def fake_play(data, sr, device, watch_mode, stop_unless=('LIVE',)):
        played.append(len(data))
        return {'played_ms': 1, 'aborted': False, 'abort_reason': None, 'progress': 1.0}
    monkeypatch.setattr(player, 'play', fake_play)
    monkeypatch.setattr(caption_pages, 'publish', lambda *a, **kw: None)
    monkeypatch.setattr(player, '_caption_chunks',
                        lambda *a, **kw: [{'speech': 'c%d' % i, 'text': 'c%d' % i} for i in range(n_chunks)])
    return player, prov, played


def test_second_and_later_caption_pages_get_a_short_pause_before_the_sound(isolated, monkeypatch):
    player, prov, played = _pause_setup(monkeypatch)
    monkeypatch.setattr(player, 'PAGE_PAUSE_S', 0.3)
    player.speak('x', prov, 'openai', None, watch_mode=False, tag='pz', voice='nova',
                 caption_token='tok', caption_text='x')
    # 한 묶음은 100샘플(1초 @100Hz). 첫 묶음은 그대로, 이후 묶음은 0.3초(30샘플)가 앞에 붙는다.
    assert played == [100, 130, 130]


def test_page_pause_can_be_turned_off_and_is_not_added_without_captions(isolated, monkeypatch):
    player, prov, played = _pause_setup(monkeypatch)
    monkeypatch.setattr(player, 'PAGE_PAUSE_S', 0.0)
    player.speak('x', prov, 'openai', None, watch_mode=False, tag='pz0', voice='nova',
                 caption_token='tok', caption_text='x')
    assert played == [100, 100, 100]
    player, prov, played = _pause_setup(monkeypatch)
    monkeypatch.setattr(player, 'PAGE_PAUSE_S', 0.3)
    player.speak('x', prov, 'openai', None, watch_mode=False, tag='pz1', voice='nova')
    assert played == [100, 100, 100]
