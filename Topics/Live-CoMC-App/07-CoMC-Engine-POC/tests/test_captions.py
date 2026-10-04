"""Audio page boundaries, caption lifecycle and OBS state in isolated output."""
import json
import sys
from pathlib import Path
from types import SimpleNamespace

import numpy as np
import pytest

SRC = Path(__file__).resolve().parents[1] / 'src'
sys.path[:0] = [str(SRC), str(SRC.parents[1] / '09-Desktop-Shell-and-Overlay/examples/engine')]
import common
import caption_pages as captions
import spoken_player as player
import overlay_server as overlay


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    monkeypatch.setattr(common, 'OUTPUT', tmp_path)
    monkeypatch.setattr(common, 'TRACE', tmp_path / 'trace.jsonl')
    for name, file in [('OVERLAY', 'overlay.json'), ('CAPTIONS', 'captions.json'),
                       ('MODE', 'mode.json'), ('SESSION', 'session_state.json')]:
        monkeypatch.setattr(overlay, name, common.out(file))
    common.write_json(overlay.OVERLAY, {'text': 'Full answer.', 'updated_at': 'token',
                                      'captioned': True, 'persona': 'AI student', 'part_id': '1'})
    common.write_json(overlay.MODE, {'mode': 'REVIEW'})
    return tmp_path


@pytest.mark.parametrize('text', ['가' * 500, 'This is a lengthy English sentence. ' * 20,
                                   '숫자는 3.14예요. 이름은 지우님이에요. ' * 15,
                                   '안녕하세요.\n여러분 반가워요.', 'W' * 500])
def test_all_content_preserved_and_at_most_three_lines(text):
    pages = captions.pages(text)
    clean = lambda s: ''.join(s.split())
    assert clean(''.join(p['speech'] for p in pages)) == clean(text)
    assert clean(''.join(p['text'] for p in pages)) == clean(text)
    assert all(1 <= len(p['text'].splitlines()) <= 3 for p in pages)


def test_pending_playing_expiry_and_mute(isolated, monkeypatch):
    captions.publish('token', 'ready')
    assert overlay.snapshot()['text'] == '답변 준비됨 · 승인 대기'
    common.write_json(overlay.SESSION, {'current_part_id': '2'})
    captions.publish('token', 'playing', 'First\nSecond', 1, 2)
    assert overlay.snapshot()['text'] == 'First\nSecond'
    assert overlay.snapshot()['part_id'] == '2'
    assert overlay.snapshot()['persona'] == 'AI student'
    captions.publish('token', 'finished', 'Last page', 2, 2)
    assert overlay.snapshot()['text'] == 'Last page'
    expires = common.read_json(overlay.CAPTIONS)['expires_at']
    monkeypatch.setattr(overlay.time, 'time', lambda: expires + 1)
    assert overlay.snapshot()['text'] == ''
    captions.publish('token', 'playing', 'Old page')
    common.write_json(overlay.MODE, {'mode': 'MUTE'})
    assert overlay.snapshot()['text'] == ''


def test_stale_caption_and_clear_do_not_show_old_answer(isolated):
    captions.publish('old-token', 'playing', 'Stale')
    assert overlay.snapshot()['text'] == '답변 준비됨 · 승인 대기'
    common.clear_overlay('test', 'clear')
    assert overlay.snapshot()['text'] == ''


@pytest.mark.parametrize('abort_at', [None, 0])
def test_prepares_all_pages_then_publishes_at_playback(isolated, monkeypatch, abort_at):
    text = '가나다라마바 사아자차카타 파하입니다. ' * 12
    pages = captions.pages(text); events = []
    def prepare(text, prov, provider, device, tag, voice, rate, pitch):
        events.append(('prepare', text))
        return {'data': np.ones(100), 'sr': 100, 'synth_ms': 2, 'audio_s': 1,
                'voice': voice, 'audio': tag + '.mp3'}
    count = [0]
    def play(*args):
        state = common.read_json(overlay.CAPTIONS)
        events.append(('play', state['text']))
        assert state['index'] == count[0] + 1
        assert state['phase'] == 'playing'
        aborted = count[0] == abort_at; count[0] += 1
        return {'aborted': aborted, 'abort_reason': 'MUTE' if aborted else None, 'played_ms': 10}
    monkeypatch.setattr(player, 'prepare_audio', prepare)
    monkeypatch.setattr(player, 'play', play)
    monkeypatch.setattr(player, 'current_mode', lambda: 'REVIEW')
    res = player.speak(text, SimpleNamespace(voice='old'), 'edge', None, True, 'test',
                       ('LIVE', 'REVIEW'), voice='fixed', caption_token='token')
    assert all(e[0] == 'prepare' for e in events[:len(pages)])
    assert [e[1] for e in events[len(pages):]] == [p['text'] for p in pages[:count[0]]]
    assert res['aborted'] == (abort_at is not None)
    assert common.read_json(overlay.CAPTIONS)['phase'] == ('stopped' if res['aborted'] else 'finished')


def test_synthesis_failure_never_plays_partial_answer(isolated, monkeypatch):
    calls = [0]
    def prepare(*a):
        calls[0] += 1
        if calls[0] == 2: raise RuntimeError('network failed')
        return {'data': np.ones(10), 'sr': 100, 'synth_ms': 1}
    monkeypatch.setattr(player, 'prepare_audio', prepare)
    monkeypatch.setattr(player, 'play', lambda *a: pytest.fail('partial playback'))
    monkeypatch.setattr(player, 'current_mode', lambda: 'LIVE')
    with pytest.raises(RuntimeError):
        player.speak('긴 답변입니다. ' * 60, SimpleNamespace(voice='old'), 'edge', None,
                     True, 'test', caption_token='token')
    assert common.read_json(overlay.CAPTIONS)['phase'] == 'stopped'


def test_panic_during_preparation_cancels_remaining_pages(isolated, monkeypatch):
    mode = ['LIVE']
    def prepare(*a):
        mode[0] = 'MUTE'
        return {'data': np.ones(10), 'sr': 100, 'synth_ms': 1}
    monkeypatch.setattr(player, 'prepare_audio', prepare)
    monkeypatch.setattr(player, 'current_mode', lambda: mode[0])
    monkeypatch.setattr(player, 'play', lambda *a: pytest.fail('playback after panic'))
    res = player.speak('긴 답변입니다. ' * 60, SimpleNamespace(voice='old'), 'edge', None,
                       True, 'test', caption_token='token')
    assert res['aborted']
    assert common.read_json(overlay.CAPTIONS)['phase'] == 'stopped'


def test_display_name_and_pronunciation_remain_separate(isolated, monkeypatch):
    heard = []
    def prepare(text, *a):
        heard.append(text)
        return {'data': np.ones(10), 'sr': 100, 'synth_ms': 1, 'audio_s': 1,
                'voice': 'fixed', 'audio': 'test.mp3'}
    monkeypatch.setattr(player, 'prepare_audio', prepare)
    monkeypatch.setattr(player, 'current_mode', lambda: 'LIVE')
    def play(*a):
        assert common.read_json(overlay.CAPTIONS)['text'] == 'Alice님 안녕하세요.'
        return {'aborted': False, 'played_ms': 1}
    monkeypatch.setattr(player, 'play', play)
    player.speak('앨리스님 안녕하세요.', SimpleNamespace(voice='old'), 'edge', None, True, 'test',
                 caption_token='token', caption_text='Alice님 안녕하세요.', caption_aliases={'Alice': '앨리스'})
    assert heard == ['앨리스님 안녕하세요.']
