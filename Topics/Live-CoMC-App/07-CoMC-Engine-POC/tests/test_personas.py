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


def test_default_keeps_console_provider_override(isolated, monkeypatch):
    import spoken_player as player
    profile = isolated.current()
    meta = {k: profile[k] for k in ('id', 'name', 'speech', 'definition_sha256')}; meta['live'] = '30'
    monkeypatch.setattr(player, 'SPOKEN', common.out('spoken.json'))
    monkeypatch.setattr(player, 'LOG', common.out('spoken_log.jsonl'))
    monkeypatch.setattr(player, 'current_mode', lambda: 'LIVE')
    monkeypatch.setattr(player, 'load_provider', lambda *a: pytest.fail('default provider was changed'))
    def speak(*a, **kw):
        assert a[2] == 'openai' and 'voice' not in kw
        return {'voice': 'alloy', 'aborted': False, 'synth_ms': 1, 'played_ms': 1}
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
