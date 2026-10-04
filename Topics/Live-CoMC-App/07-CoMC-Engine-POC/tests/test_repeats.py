"""Repeat suppression at the actual playback boundary; no devices or network."""
import json
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

SRC = Path(__file__).resolve().parents[1] / 'src'
sys.path[:0] = [str(SRC), str(SRC.parents[1] / '09-Desktop-Shell-and-Overlay/examples/engine')]
import common
import spoken_player as player


@pytest.fixture
def playback(tmp_path, monkeypatch):
    monkeypatch.setattr(common, 'OUTPUT', tmp_path)
    monkeypatch.setattr(player, 'SPOKEN', tmp_path / 'spoken.json')
    monkeypatch.setattr(player, 'LOG', tmp_path / 'log.jsonl')
    monkeypatch.setattr(common, 'TRACE', tmp_path / 'trace.jsonl')
    monkeypatch.setattr(player, '_last_completed', None)
    monkeypatch.setattr(player, 'current_mode', lambda: 'LIVE')
    clock = [100.0]
    monkeypatch.setattr(player.time, 'monotonic', lambda: clock[0])
    calls = []
    def speak(text, *args, **kw):
        calls.append(text)
        return {'aborted': False, 'synth_ms': 1, 'played_ms': 1}
    monkeypatch.setattr(player, 'speak', speak)
    def consume(text='Same answer.', **extra):
        common.write_json(player.SPOKEN, {'text': text, 'spoken_at': str(clock[0]), **extra})
        return player.consume_one(SimpleNamespace(voice='voice'), 'edge', None)
    return consume, calls, clock


def test_duplicate_consumed_without_second_synthesis(playback):
    consume, calls, clock = playback
    assert consume()
    clock[0] += 5
    assert consume('  Same   answer.  ', approved=True)
    assert calls == ['Same answer.']
    assert not player.SPOKEN.exists()
    events = [json.loads(line)['event'] for line in player.LOG.read_text().splitlines()]
    assert events == ['played', 'repeat_suppressed']


def test_window_is_from_completion_not_suppression(playback):
    consume, calls, clock = playback
    consume(); clock[0] += 29; consume()
    clock[0] += 1; consume()
    assert len(calls) == 2


def test_only_consecutive_equal_answers_are_blocked(playback):
    consume, calls, clock = playback
    consume(); consume('Different answer.'); consume()
    assert len(calls) == 3


@pytest.mark.parametrize('failure', ['aborted', 'exception'])
def test_failed_or_interrupted_can_retry(playback, monkeypatch, failure):
    consume, calls, clock = playback
    original = player.speak
    def fail(*a, **kw):
        if failure == 'exception': raise RuntimeError('test synthesis failure')
        return {'aborted': True, 'abort_reason': 'MUTE', 'synth_ms': 1, 'played_ms': 1}
    monkeypatch.setattr(player, 'speak', fail); consume()
    monkeypatch.setattr(player, 'speak', original); consume()
    assert len(calls) == 1


def test_persona_voice_episode_change_has_distinct_key():
    prov = SimpleNamespace(voice='default')
    base = {'text': 'Same answer.', 'persona': {'id': 'student', 'live': '30', 'definition_sha256': 'a'},
            'voice': 'student', 'provider': 'edge', 'rate': '+6%', 'pitch': '+8Hz'}
    key = player.repeat_key(base, 'edge', prov)
    for field, value in [('voice', 'other'), ('rate', '+2%'), ('pitch', '+0Hz')]:
        assert key != player.repeat_key({**base, field: value}, 'edge', prov)
    for field, value in [('id', 'friend'), ('live', '31'), ('definition_sha256', 'b')]:
        assert key != player.repeat_key({**base, 'persona': {**base['persona'], field: value}}, 'edge', prov)


def test_newer_request_is_not_deleted_during_suppression(playback, monkeypatch):
    consume, calls, clock = playback
    consume(); original = player.log
    def publish_new(event):
        original(event)
        if event['event'] == 'repeat_suppressed':
            common.write_json(player.SPOKEN, {'text': 'New answer.', 'spoken_at': 'new'})
    monkeypatch.setattr(player, 'log', publish_new)
    consume()
    assert common.read_json(player.SPOKEN)['text'] == 'New answer.'
