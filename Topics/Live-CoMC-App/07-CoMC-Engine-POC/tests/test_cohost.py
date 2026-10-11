"""Regression for Live30 incidents and the conversational cohost contract."""
import json
import sys
from datetime import date
from pathlib import Path
from types import SimpleNamespace

import pytest

TOPIC = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(TOPIC / '07-CoMC-Engine-POC/src'))
sys.path.insert(0, str(TOPIC / '09-Desktop-Shell-and-Overlay/examples/engine'))
import cohost

@pytest.fixture
def vault(tmp_path):
    (tmp_path / 'AI/Roundup/Weekly').mkdir(parents=True)
    (tmp_path / 'Journal').mkdir()
    p = tmp_path / 'AI/Roundup/2026-09-27 - Live30 Weekly Rundown.md'
    p.write_text('---\ntitle: Live30\n---\n\n## 방송 정보\n- 방송 날짜·시간: 2026-10-04\n'
                 '## 1부: CoMC 시연\n계획: CoMC, Catch 시연.\n## 주말 기록\n10월 3일 축제 참석 완료.\n', encoding='utf-8')
    (tmp_path / 'Journal/2026-10-03.md').write_text('## Thoughts\n축제 참석 완료.\n', encoding='utf-8')
    (tmp_path / 'AI/Roundup/2026-09-27 - Weekly Progress and Planning.md').write_text('## 일정\n10/2 앱 준비\n', encoding='utf-8')
    (tmp_path / 'AI/Roundup/2026-04-06 - Daily Roundup.md').write_text('## 일정\n봄 잔디깎기 완료\n', encoding='utf-8')
    return tmp_path

def test_broadcast_date_is_not_rundown_filename(vault):
    assert cohost.broadcast_day('30', vault) == date(2026, 10, 4)
    assert cohost.week_window(cohost.broadcast_day('30', vault)) == (date(2026, 9, 27), date(2026, 10, 3))

@pytest.mark.parametrize('question', ['금요일과 토요일 일정은?', '이번 주 한 일', '지난주 일정', '만든 콘텐츠와 인사이트'])
def test_week_questions_never_search_old_matching_weekdays(vault, monkeypatch, question):
    monkeypatch.setattr(cohost.VaultIndex, 'search', lambda *a, **kw: pytest.fail('weekly request entered historic search'))
    docs, window = cohost.Context('30', vault).documents(question)
    assert window == (date(2026, 9, 27), date(2026, 10, 3))
    assert any('2026-10-03' in row['path'] for row in docs)
    assert all('2026-04' not in row['path'] for row in docs)
    assert '잔디' not in json.dumps(docs, ensure_ascii=False)

def test_explicit_dates_override_broadcast_week():
    assert cohost.requested_window('2026년 10월 2일과 10월 3일 일정', date(2026, 10, 11)) == (date(2026, 10, 2), date(2026, 10, 3))
    assert cohost.requested_window('2026-04-06 일정', date(2026, 10, 4)) == (date(2026, 4, 6),) * 2

def test_missing_rundown_uses_upcoming_sunday(tmp_path):
    assert cohost.broadcast_day('999', tmp_path, date(2026, 10, 8)) == date(2026, 10, 11)

def test_internal_markers_and_personal_details_are_not_model_context(vault):
    p = vault / 'Journal/2026-10-02.md'
    p.write_text('---\nvisibility: internal\n---\n## 일정\n비공개 행사\n', encoding='utf-8')
    assert cohost.Context('30', vault).read(p) is None
    assert 'secret' not in cohost.safe_text('## 공개\nsecret API key = secret\n공개 AI 시연\n')
    assert '010-' not in cohost.safe_text('연락처 010-1234-1234')

def test_parent_internal_marker_blocks_whole_folder(vault):
    p = vault / 'AI/Roundup/Weekly'
    (p / '_index.md').write_text('🔒 내부 자료', encoding='utf-8')
    target = p / 'public-looking.md'
    target.write_text('## 공개처럼 보임\n내부 데이터', encoding='utf-8')
    assert cohost.Context('30', vault).read(target) is None

def test_recording_epoch_and_full_source_saved(tmp_path):
    m = cohost.BroadcastMemory('30', tmp_path)
    first = m.start()['id']
    assert m.accept(first, 'CoMC 시연을 끝냈어요.', b'webm')
    m.stop(first)
    assert not m.accept(first, '늦은 결과')
    second = m.start()['id']
    assert second != first
    assert not m.accept(first, '이전 녹음 결과')
    assert m.accept(second, '이제 Catch를 시연합니다.')
    assert len(m.heard()) == 2
    assert m.snapshot()['audio_segments'] == 1
    assert 'CoMC' in m.path.read_text(encoding='utf-8')

def test_uncertain_or_prompt_echo_transcripts_are_not_progress_evidence(tmp_path):
    quality = cohost.transcription_quality('한국어 라이브 방송', [{'logprob': -0.01}])
    assert not quality['usable_for_assessment']
    m = cohost.BroadcastMemory('30', tmp_path)
    rid = m.start()['id']
    assert m.accept(rid, quality['text'], usable_for_assessment=False)
    assert m.snapshot()['lines'][-1]['text'] == '한국어 라이브 방송'
    assert m.heard() == []

def test_transcribed_sentence_requires_confidence_for_assessment():
    high = cohost.transcription_quality('코엠씨 마이크 테스트입니다.', [{'logprob': -0.1}])
    low = cohost.transcription_quality('코엠씨 마이크 테스트입니다.', [{'logprob': -2.0}])
    foreign_only = cohost.transcription_quality('No es posible.', [{'logprob': -1.2}])
    korean_with_english_terms = cohost.transcription_quality('AI 마켓 테스트입니다.', [{'logprob': -0.1}])
    isolated_app_name = cohost.transcription_quality('CoMC', [{'logprob': -0.1}])
    assert high['usable_for_assessment']
    assert not low['usable_for_assessment']
    assert not foreign_only['usable_for_assessment']
    assert korean_with_english_terms['usable_for_assessment']
    assert isolated_app_name['usable_for_assessment']

def test_transcriber_does_not_seed_asr_with_broadcast_prompt(vault, tmp_path):
    class Transcriptions:
        def __init__(self): self.kwargs = None
        def create(self, **kwargs):
            self.kwargs = kwargs
            return SimpleNamespace(text='코엠씨 마이크 테스트입니다.',
                                   logprobs=[SimpleNamespace(logprob=-0.1)])
    transcriptions = Transcriptions()
    client = SimpleNamespace(audio=SimpleNamespace(transcriptions=transcriptions))
    h = host(vault, tmp_path, client)
    result = h.transcribe_result(b'x' * 2048)
    assert result['usable_for_assessment']
    assert result['text'] == 'CoMC 마이크 테스트입니다.'
    assert transcriptions.kwargs['include'] == ['logprobs']
    assert 'prompt' not in transcriptions.kwargs
    assert transcriptions.kwargs['language'] == 'ko'

@pytest.mark.parametrize(('raw', 'expected'), [
    ('OMC 시연은 마쳤습니다.', 'CoMC 시연은 마쳤습니다.'),
    ('OMG, Catch App, Personal Ops Board 순서로 시연합니다.', 'CoMC, Catch App, Personal Ops Board 순서로 시연합니다.'),
    ('코엠씨와 캐치앱을 소개합니다.', 'CoMC와 Catch App을 소개합니다.'),
    ('퍼스널 옵스 보드', 'Personal Ops Board'),
])
def test_transcript_glossary_canonicalizes_known_variants(raw, expected):
    config = cohost.read_json(cohost.CONFIG)
    assert cohost.normalize_glossary(raw, config['stt_glossary']) == expected

def test_omg_stays_unchanged_without_app_list_context():
    config = cohost.read_json(cohost.CONFIG)
    assert cohost.normalize_glossary('OMG!', config['stt_glossary']) == 'OMG!'

class FakeClient:
    def __init__(self, reply):
        self.reply = reply
        self.calls = []
        self.responses = self

    def create(self, **kw):
        self.calls.append(kw)
        return SimpleNamespace(output_text=json.dumps(self.reply, ensure_ascii=False), output=[])

def host(vault, tmp_path, client):
    return cohost.CoHost('30', cohost.BroadcastMemory('30', tmp_path / 'runtime'), client, vault)

def test_general_conversation_without_document_evidence_can_answer(vault, tmp_path, monkeypatch):
    monkeypatch.setattr(cohost.VaultIndex, 'search', lambda *a, **kw: [])
    c = FakeClient({'say': '그 관점은 흥미롭네요. 어떤 사용자의 문제부터 풀어 볼까요?', 'screen': [], 'sources': [], 'uncertain': False})
    h = host(vault, tmp_path, c)
    assert h.reply('AI 제품의 가치에 대해 자유롭게 이야기하자')['say']
    assert c.calls[0]['tools'] == [{'type': 'web_search'}]

def test_private_schedule_never_uses_web(vault, tmp_path):
    c = FakeClient({'say': '10월 3일에는 축제에 참석했어요.', 'screen': [], 'sources': ['Journal/2026-10-03.md'], 'uncertain': False})
    h = host(vault, tmp_path, c)
    assert h.reply('이번 주 토요일 일정은?')['say'].startswith('10월 3일')
    assert 'tools' not in c.calls[0]
    payload = json.loads(c.calls[0]['input'])
    assert payload['local_documents']
    assert '2026-09-27 일요일~2026-10-03 토요일' in c.calls[0]['instructions']

def test_invented_source_becomes_honest_followup_not_silence(vault, tmp_path):
    c = FakeClient({'say': '봄 잔디깎기를 했어요.', 'screen': [], 'sources': ['Journal/2026-04-06.md'], 'uncertain': False})
    d = host(vault, tmp_path, c).reply('이번 주 금요일 일정')
    assert d['say'] and d['uncertain'] and not d['sources']
    assert '잔디' not in d['say']

def test_current_progress_is_not_inferred_from_plan(vault, tmp_path):
    c = FakeClient({'say': '아직 실제 방송을 듣지 못했어요. 지금 어떤 내용을 진행하고 계신가요?', 'screen': [], 'sources': [], 'uncertain': True})
    h = host(vault, tmp_path, c)
    d = h.reply('지금까지 한 일과 남은 일')
    assert '실제 방송을 듣지 못해서' in d['say']
    assert d['uncertain'] and not c.calls

def test_status_query_does_not_pull_weekly_completed_activities(vault):
    docs, _ = cohost.Context('30', vault).documents('지금까지 방송에서 한 일과 남은 일')
    assert len(docs) == 1 and 'Live30 Weekly Rundown' in docs[0]['path']

def test_assessment_is_grounded_in_heard_audio_not_drafts(vault, tmp_path):
    c = FakeClient({'topic': 'Catch 시연', 'done': ['CoMC 시연'], 'remaining': ['일정 앱 계획'], 'suggestion': '남은 계획을 확인할까요?', 'evidence': []})
    h = host(vault, tmp_path, c)
    rid=h.memory.start()['id'];h.memory.accept(rid, 'CoMC 시연을 끝냈어요. 이제 Catch를 시연합니다.')
    c.reply['evidence']=[{'at':h.memory.lines[0]['at'],'quote':'CoMC 시연을 끝냈어요.'}]
    h.history.append({'role': 'cohost_draft', 'text': '모든 시연 완료'})
    assert h.assess()['topic'] == 'Catch 시연'
    data = json.loads(c.calls[0]['input'])
    assert data['heard'][0]['text'].startswith('CoMC 시연을 끝냈어요')
    assert '모든 시연 완료' not in c.calls[0]['input']

def test_registered_viewer_greeting_has_no_roster_metadata(vault, tmp_path):
    h=host(vault,tmp_path,FakeClient({}))
    d=h.reply('인사해 주세요',viewer_records=[{'name':'크락드','id':'1','pronunciation':'','count':1}],viewer_scope='current')
    assert '크락드님' in d['say']
    assert '기록' not in d['say'] and '현재 시청' not in d['say']

def test_all_personas_have_female_voice_and_keep_casual_speech():
    from persona_store import definitions
    profiles=definitions()['personas']
    assert all(r['gender']=='female' and r['tts']['ko']=='ko-KR-SunHiNeural' for r in profiles)
    assert next(r for r in profiles if r['id']=='student')['speech']=='casual'

def test_assessment_rejects_invented_quotes(vault, tmp_path):
    c=FakeClient({'topic':'Catch', 'done':['모든 앱 시연 완료'], 'remaining':[], 'suggestion':'',
                  'evidence':[{'at':'invented','quote':'모든 앱 완료'}]})
    h=host(vault,tmp_path,c);rid=h.memory.start()['id'];h.memory.accept(rid,'CoMC 시연 중입니다.')
    d=h.assess()
    assert not d['done'] and not d['evidence']

def test_old_completion_evidence_survives_long_broadcast(vault, tmp_path):
    c=FakeClient({'topic':'Catch','done':['CoMC 시연'],'remaining':[],'suggestion':'','evidence':[]})
    h=host(vault,tmp_path,c);rid=h.memory.start()['id']
    for i in range(35):h.memory.accept(rid,f'첫 이야기 {i}')
    h.memory.accept(rid,'CoMC 시연을 마쳤어요.')
    row=h.memory.lines[-1];c.reply['evidence']=[{'at':row['at'],'quote':row['text']}];h.assess()
    for i in range(250):h.memory.accept(rid,f'다음 이야기 {i}')
    assert row in h.memory.heard()


class SeqClient:
    """Returns the given replies in order (the last one repeats)."""
    def __init__(self, replies):
        self.replies = list(replies)
        self.calls = []
        self.responses = self

    def create(self, **kw):
        self.calls.append(kw)
        reply = self.replies.pop(0) if len(self.replies) > 1 else self.replies[0]
        return SimpleNamespace(output_text=json.dumps(reply, ensure_ascii=False), output=[])


def test_unverified_web_source_retries_without_web_instead_of_dropping_the_answer(vault, tmp_path, monkeypatch):
    monkeypatch.setattr(cohost.VaultIndex, 'search', lambda *a, **kw: [])
    bad = {'say': '검증되지 않은 출처가 붙은 답', 'screen': [], 'sources': ['어딘가의 블로그'], 'uncertain': False}
    good = {'say': '제 의견으로는 문제를 먼저 정의하는 것이 중요해요.', 'screen': [], 'sources': [], 'uncertain': False}
    c = SeqClient([bad, good])
    d = host(vault, tmp_path, c).reply('AI 제품의 가치에 대해 자유롭게 이야기하자')
    assert d['say'].startswith('제 의견으로는') and not d['uncertain']
    assert c.calls[0]['tools'] == [{'type': 'web_search'}]
    assert 'tools' not in c.calls[1]
    assert 'web_check_unavailable' in json.loads(c.calls[1]['input'])


def test_retry_without_web_still_fails_closed_on_invented_source(vault, tmp_path, monkeypatch):
    monkeypatch.setattr(cohost.VaultIndex, 'search', lambda *a, **kw: [])
    bad = {'say': '지어낸 출처가 붙은 답', 'screen': [], 'sources': ['Journal/2099-01-01.md'], 'uncertain': False}
    c = SeqClient([bad])
    d = host(vault, tmp_path, c).reply('AI 제품의 가치에 대해 자유롭게 이야기하자')
    assert len(c.calls) == 2
    assert d['uncertain'] and not d['sources'] and '지어낸' not in d['say']


def test_private_question_is_not_retried_with_web(vault, tmp_path):
    bad = {'say': '봄 잔디깎기를 했어요.', 'screen': [], 'sources': ['Journal/2026-04-06.md'], 'uncertain': False}
    c = SeqClient([bad])
    d = host(vault, tmp_path, c).reply('이번 주 금요일 일정')
    assert len(c.calls) == 1 and 'tools' not in c.calls[0]
    assert d['uncertain']


def test_parenthetical_domain_citations_are_removed_from_the_reply(vault, tmp_path, monkeypatch):
    monkeypatch.setattr(cohost.VaultIndex, 'search', lambda *a, **kw: [])
    c = FakeClient({'say': '블록을 벗어나면 모두 기다려요. (docs.python.org) 하나라도 실패하면 취소해요. (docs.python.org)',
                    'screen': [], 'sources': [], 'uncertain': False})
    d = host(vault, tmp_path, c).reply('AI 제품의 가치에 대해 자유롭게 이야기하자')
    assert 'docs.python.org' not in d['say']
    assert d['say'].startswith('블록을 벗어나면') and '취소해요' in d['say']


def test_bare_product_domain_in_a_sentence_is_kept(vault, tmp_path, monkeypatch):
    monkeypatch.setattr(cohost.VaultIndex, 'search', lambda *a, **kw: [])
    c = FakeClient({'say': '브라우저에서 muse.ai 에 접속해 볼게요.', 'screen': [], 'sources': [], 'uncertain': False})
    d = host(vault, tmp_path, c).reply('AI 제품의 가치에 대해 자유롭게 이야기하자')
    assert 'muse.ai' in d['say']


def test_source_path_spelling_difference_is_accepted_when_it_is_the_same_file(vault, tmp_path):
    c = FakeClient({'say': '10월 3일에는 축제에 참석했어요.', 'screen': [], 'sources': ['Journal/2026-10-03'], 'uncertain': False})
    d = host(vault, tmp_path, c).reply('이번 주 토요일 일정은?')
    assert d['say'].startswith('10월 3일') and not d['uncertain']
    assert d['sources'] == ['Journal/2026-10-03.md']


@pytest.mark.parametrize('raw,expected', [
    ('오늘은 패치 앱 개선을 이야기했고 호엠씨 개편은 끝났습니다.', '오늘은 Catch App 개선을 이야기했고 CoMC 개편은 끝났습니다.'),
    ('소엠씨, 함께 방송할 준비가 됐니?', 'CoMC, 함께 방송할 준비가 됐니?'),
    ('뮤즈를 웹에서 열어 보겠습니다. 그록 봇과 인스팅트도 비교합니다.', 'Muse를 웹에서 열어 보겠습니다. Grok Bot과 Instinct도 비교합니다.'),
    ('빌더스 라운지에서 클로드 코드로 만들었어요.', 'Builders Lounge에서 Claude Code로 만들었어요.'),
])
def test_stt_glossary_fixes_the_misheard_names_from_the_live31_rehearsal(raw, expected):
    config = json.loads((Path(__file__).resolve().parents[1] / 'data/cohost_config.json').read_text(encoding='utf-8'))
    assert cohost.normalize_glossary(raw, config['stt_glossary']) == expected


@pytest.fixture(autouse=True)
def _tests_do_not_write_the_real_fallback_log(monkeypatch):
    monkeypatch.setattr(cohost, 'note_fallback', lambda *a, **kw: None)
