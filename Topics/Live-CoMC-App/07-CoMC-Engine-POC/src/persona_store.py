"""Editable character styles; private selection/history; immutable per-answer snapshots."""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

from common import ROOT, now_iso, out
from viewer_store import ViewerStore

CONFIG = ROOT / 'data/personas.json'


def definitions(path=None):
    data = json.loads((path or CONFIG).read_text(encoding='utf-8'))
    rows = data['personas']
    if data.get('version') != 1 or len({r['id'] for r in rows}) != len(rows):
        raise ValueError('Persona 정의의 버전 또는 ID가 올바르지 않습니다')
    for r in rows:
        if r['speech'] not in ('polite', 'casual') or not re.fullmatch(r'[a-z][a-z0-9_]{0,30}', r['id']):
            raise ValueError('Persona 말투 또는 ID가 올바르지 않습니다')
        for key in ('name', 'background', 'length', 'humor', 'style'):
            if not isinstance(r[key], str) or not 1 <= len(r[key]) <= 1000:
                raise ValueError('Persona 정의의 문장이 올바르지 않습니다')
        if r['tts'] is not None:
            t = r['tts']
            if t['provider'] != 'edge' or not re.fullmatch(r'[+-]\d{1,2}%', t['rate']) or not re.fullmatch(r'[+-]\d{1,2}Hz', t['pitch']):
                raise ValueError('Persona 음성 설정이 올바르지 않습니다')
            if not t['ko'].startswith('ko-KR-') or not t['en'].startswith('en-US-'):
                raise ValueError('Persona 음성 언어가 올바르지 않습니다')
    if data['default'] not in {r['id'] for r in rows}:
        raise ValueError('기본 Persona가 정의에 없습니다')
    return data


class PersonaStore(ViewerStore):
    """Reuse the existing private atomic JSON writer and interprocess lock."""
    def __init__(self, root=None, config=None):
        super().__init__(root or out('private') / 'personas')
        self.path = self.root / 'state.json'
        self.config = config

    def _load(self):
        if not self.path.exists():
            return {'version': 1, 'selected': definitions(self.config)['default'], 'episodes': {}}
        data = json.loads(self.path.read_text(encoding='utf-8'))
        if data.get('version') != 1 or not isinstance(data.get('episodes'), dict):
            raise ValueError('Persona 기록 형식 오류 — 기존 파일을 덮어쓰지 않습니다')
        return data

    def current(self):
        with self._locked():
            data = self._load()
        rows = definitions(self.config)['personas']
        row = next((r for r in rows if r['id'] == data['selected']), None)
        if row is None:
            raise ValueError('선택한 Persona가 정의에서 삭제됐습니다. 다른 Persona를 선택해 주세요')
        row = dict(row)
        row['definition_sha256'] = hashlib.sha256(json.dumps(row, sort_keys=True, ensure_ascii=False).encode()).hexdigest()
        return row

    def snapshot(self, live):
        with self._locked():
            data = self._load()
        return {'current': self.current(), 'options': definitions(self.config)['personas'],
                'history': data['episodes'].get(str(live), {}).get('events', [])[-20:],
                'notes': data['episodes'].get(str(live), {}).get('notes', '')}

    def select(self, live, persona_id):
        profile = next((r for r in definitions(self.config)['personas'] if r['id'] == persona_id), None)
        if profile is None:
            raise ValueError('정의된 Persona를 선택해 주세요')
        with self._locked():
            data = self._load(); data['selected'] = persona_id
            ep = data['episodes'].setdefault(str(live), {'events': [], 'notes': ''})
            ep['events'].append({'event': 'selected', 'persona_id': persona_id, 'name': profile['name'], 'at': now_iso()})
            self._save(data)
        return self.snapshot(live)

    def note_episode(self, live, text):
        if not isinstance(text, str) or len(text) > 2000:
            raise ValueError('반응 메모는 2000자 이내로 입력해 주세요')
        with self._locked():
            data = self._load(); ep = data['episodes'].setdefault(str(live), {'events': [], 'notes': ''})
            ep['notes'] = text; self._save(data)
        return self.snapshot(live)

    def record_answer(self, live, profile, spoken_at, mode):
        with self._locked():
            data = self._load(); ep = data['episodes'].setdefault(str(live), {'events': [], 'notes': ''})
            ep['events'].append({'event': 'rendered', 'persona_id': profile['id'], 'name': profile['name'],
                'definition_sha256': profile['definition_sha256'], 'at': spoken_at, 'mode': mode})
            self._save(data)

    def record_played(self, live, profile, spoken_at, voice):
        with self._locked():
            data = self._load(); ep = data['episodes'].setdefault(str(live), {'events': [], 'notes': ''})
            ep['events'].append({'event': 'played', 'persona_id': profile['id'], 'name': profile['name'],
                'definition_sha256': profile['definition_sha256'], 'at': now_iso(),
                'spoken_at': spoken_at, 'voice': voice})
            self._save(data)


def host_story(text):
    low = text.lower()
    past = any(k in low for k in ('예전', '지난', '추억', '과거', '기억', '어제', 'past', 'memories', 'yesterday'))
    if not past and re.search(r'\d+\s*부|파트|오늘\s*방송|지금\s*방송|현재\s*방송|today.?s?\s+(?:show|broadcast)', low):
        return False
    return any(k in low for k in ('창수', '진행자', '우리 둘', '나랑', '나하고', 'changsoo', 'host', 'you and i')) and (
        past or any(k in low for k in ('일화', '이야기', '얘기', '함께', '했었', 'story', 'stories', 'together')))


def prompt_block(profile):
    return '\n\n[말하는 방식 — 근거나 실제 경력이 아닌 가상 캐릭터 설정]\n' + json.dumps({k: profile[k] for k in
        ('name', 'age', 'background', 'speech', 'length', 'humor', 'expressions', 'avoid', 'style')}, ensure_ascii=False) + '''
너는 언제나 AI 공동 진행자 코엠씨다. 실제 사람·학생·아나운서·진행자의 실존 친구라고 주장하지 않는다.
말투와 종결 어미는 이 Persona의 speech와 style을 따른다. 자연스러운 반말도 허용하지만 해라체에 요를 붙이는 ~다요는 쓰지 않는다.
설정의 나이·학교생활·경력·경험을 실제 사실이나 근거로 사용하지 않는다. 이름·숫자·날짜·완료 상태는 근거대로 유지한다.
완료·진행 중·대기·미확인·남아 있음 상태를 서로 바꾸지 않는다. 일부 개발 검증 완료를 전체 운영 검증 완료라고 바꾸지 않는다.
기본 규칙과 충돌하면 근거·인용·개인정보 제외·창작 제한·출처를 알리는 첫 구절이 우선한다.
목차나 쉼표 목록을 그대로 읽지 말고 핵심 한두 가지를 쉽게 풀어 말한다. 모든 항목이나 개수를 물었을 때는 생략하지 않는다.
짧은 문장과 설명 문장을 섞어 리듬을 만들고 같은 어미를 반복하지 않는다. 맞장구도 사실을 덧붙이지 않는 범위에서만 쓴다.
분수형 수치는 같은 값을 유지하며 '8개 중 7개'처럼 말하기 편한 표현으로 풀어 쓴다.
파일 경로·근거 경로·문서 제목·ID·대괄호 라벨은 소리 내어 읽지 않는다. 각 sentences 요소는 끝맺음과 문장 부호를 갖춘 한 문장으로 쓴다.
지어낸 공동 경험이나 추억은 말하지 않는다. 근거가 없으면 추측 대신 답변을 멈춘다.'''


def voice_settings(profile, language):
    t = profile.get('tts')
    if t is None:
        return None
    return {'provider': t['provider'], 'voice': t['en' if language == 'en' else 'ko'],
            'rate': t['rate'], 'pitch': t['pitch']}


def finish_sentences(sentences):
    """Add missing spoken sentence boundaries without rewriting names, values or claims."""
    result = []
    for sentence in sentences:
        text = sentence.strip()
        if text and not text.endswith(('.', '!', '?', '…')):
            text += '?' if re.search(r'(?:까요|까|니|나요)$', text) else '.'
        result.append(text)
    return result


def bind_intent(intent, selected_lane='auto'):
    if intent['intent'] in ('stop', 'repeat', 'advance_part'):
        return selected_lane  # emergency/control actions must not depend on character configuration
    if 'persona' not in intent['slots']:
        intent['slots']['persona'] = PersonaStore().current()
    profile = intent['slots']['persona']
    if profile['id'] == 'friend' and host_story(intent['transcript']) and intent['intent'] not in (
            'stop', 'repeat', 'advance_part', 'out_of_scope', 'greet_viewer'):
        intent['intent'] = 'answer_question'
        intent['slots']['evidence_lane'] = 'vault'
        intent['ambiguity_flags'] = [f for f in intent['ambiguity_flags'] if f == 'forbidden_topic_requested']
        return 'vault'
    return selected_lane


def apply_policy(verdict, draft, intent):
    profile = intent.get('slots', {}).get('persona')
    if not profile or profile['id'] == 'default':
        return verdict
    bad = []
    for i in verdict['kept_sentences']:
        text = draft['sentences'][i]
        if re.search(r'출처를?\s*알리는\s*첫\s*구절|출처\s*공개\s*첫\s*구절|claim_map|evidence_quote|sentence_idx', text, re.I):
            bad.append(i)
            continue
        pretends_real = re.search(r'(?:나는|난|저는|내가|제가).{0,15}(?:실제|진짜).{0,10}(?:학생|아나운서|친구)|\bI(?: am|\x27m).{0,12}(?:real|actual).{0,12}(?:student|announcer|friend)', text, re.I)
        denies_real = re.search(r'(?:실제|진짜).{0,15}(?:학생|친구|아나운서).{0,8}아니|\bnot\b.{0,8}(?:real|actual)\b', text, re.I)
        if denies_real:
            pretends_real = None
        shared_memory = profile['id'] == 'friend' and intent.get('slots', {}).get('evidence_lane') != 'creative' and re.search(
            r'(?:우리(?:는|가)?|우린|나랑|내가|저랑).{0,30}(?:예전|그때|직접|같이|함께).{0,30}(?:했|갔|봤|만났|기억|었|았|나눴)|\b(?:we|I)\b.{0,20}(?:went|met|visited|remember when we|did together)', text, re.I)
        if pretends_real or shared_memory:
            bad.append(i)
    if '자기소개' in intent.get('transcript', '') and not re.search(r'\bAI\b|인공지능', verdict['final_text'], re.I):
        bad = list(verdict['kept_sentences'])
    if bad:
        verdict['kept_sentences'] = [i for i in verdict['kept_sentences'] if i not in bad]
        verdict['dropped_sentences'] += [{'sentence_idx': i, 'reason': 'persona_policy'} for i in bad]
        verdict['violations'].append({'rule_id': 'persona_policy', 'detail': '실존 인물 행세·공동 경험 주장·자기소개 AI 표시 누락·내부 지시문 낭독'})
        verdict['final_text'] = ' '.join(draft['sentences'][i] for i in verdict['kept_sentences'])
        verdict['length_after'] = len(verdict['kept_sentences'])
        verdict['absence_by_closure'] = [i for i in verdict.get('absence_by_closure', []) if i not in bad]
        verdict['pass'] = False
    return verdict
