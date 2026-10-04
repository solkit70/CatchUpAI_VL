"""Operator-entered display names and episode attendance; private, atomic JSON storage."""
from __future__ import annotations

import json
import os
import re
import tempfile
import threading
import unicodedata
import uuid
from datetime import date, datetime
from pathlib import Path
from contextlib import contextmanager

from common import out

_LOCK = threading.RLock()


def clean_name(value: str, optional: bool = False) -> str:
    if not isinstance(value, str) or any(unicodedata.category(c).startswith('C') and c != '\u200d' for c in value):
        raise ValueError('이름에 제어 문자나 줄바꿈을 넣을 수 없습니다')
    value = ' '.join(unicodedata.normalize('NFKC', value).split())
    if (not value and not optional) or len(value) > 50:
        raise ValueError('표시 이름과 읽는 법은 1~50자로 입력해 주세요')
    if re.search(r'https?://|\S+@\S+\.\S+', value, re.I):
        raise ValueError('계정의 표시 이름만 입력해 주세요 (URL·이메일 제외)')
    return value


def local_time() -> str:
    return datetime.now().astimezone().isoformat(timespec='seconds')


class ViewerStore:
    def __init__(self, root: Path | None = None):
        self.root = root or out('private') / 'viewers'
        self.path = self.root / 'roster.json'

    @contextmanager
    def _locked(self):
        # Console and standalone player may both write; protect read-modify-replace across processes.
        with _LOCK:
            self.root.mkdir(parents=True, exist_ok=True)
            with (self.root / 'roster.lock').open('a+b') as lock_file:
                lock_file.seek(0, 2)
                if lock_file.tell() == 0:
                    lock_file.write(b'0'); lock_file.flush()
                lock_file.seek(0)
                if os.name == 'nt':
                    import msvcrt
                    msvcrt.locking(lock_file.fileno(), msvcrt.LK_LOCK, 1)
                else:
                    import fcntl
                    fcntl.flock(lock_file, fcntl.LOCK_EX)
                try:
                    yield
                finally:
                    lock_file.seek(0)
                    if os.name == 'nt':
                        msvcrt.locking(lock_file.fileno(), msvcrt.LK_UNLCK, 1)
                    else:
                        fcntl.flock(lock_file, fcntl.LOCK_UN)

    def _load(self):
        if not self.path.exists():
            return {'version': 1, 'viewers': {}, 'episodes': {}}
        data = json.loads(self.path.read_text(encoding='utf-8'))
        if data.get('version') != 1 or not isinstance(data.get('viewers'), dict) or not isinstance(data.get('episodes'), dict):
            raise ValueError('시청자 기록 형식 오류 — 기존 파일을 덮어쓰지 않습니다')
        return data

    def _save(self, data):
        self.root.mkdir(parents=True, exist_ok=True)
        fd, tmp = tempfile.mkstemp(prefix='roster-', suffix='.tmp', dir=self.root)
        try:
            with os.fdopen(fd, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
                f.write('\n'); f.flush(); os.fsync(f.fileno())
            os.replace(tmp, self.path)
        finally:
            Path(tmp).unlink(missing_ok=True)

    @staticmethod
    def _episode(data, live):
        live = str(live)
        if not re.fullmatch(r'[1-9]\d{0,4}', live):
            raise ValueError('회차 번호가 올바르지 않습니다')
        return data['episodes'].setdefault(live, {'date': date.today().isoformat(), 'participants': {}})

    @staticmethod
    def _rows(data, live=None):
        rows = []
        for vid, viewer in data['viewers'].items():
            episodes = sorted((n for n, ep in data['episodes'].items() if vid in ep['participants']), key=int)
            if not episodes or (live is not None and str(live) not in episodes):
                continue
            participation = data['episodes'][str(live)]['participants'][vid] if live is not None else {}
            previous = [n for n in episodes if live is not None and int(n) < int(live)]
            rows.append({'id': vid, **viewer, **participation, 'count': len(episodes),
                         'previous_count': len(previous), 'first_live': episodes[0], 'last_live': episodes[-1]})
        return sorted(rows, key=lambda r: r['name'].casefold())

    def snapshot(self, live):
        with self._locked():
            data = self._load()
            ep = self._episode(data, live)
            return {'live': str(live), 'date': ep['date'], 'current': self._rows(data, live), 'all': self._rows(data)}

    def add(self, live, names):
        if isinstance(names, str):
            names = names.split(',')
        if not isinstance(names, list) or not 1 <= len(names) <= 100:
            raise ValueError('한 번에 1~100개의 표시 이름을 입력해 주세요')
        names = [clean_name(n) for n in names]  # validate entire request before writing
        with self._locked():
            data = self._load(); ep = self._episode(data, live)
            keys = {v['name'].casefold(): vid for vid, v in data['viewers'].items()}
            for name in names:
                key = name.casefold(); vid = keys.get(key)
                if vid is None:
                    vid = uuid.uuid4().hex; keys[key] = vid
                    data['viewers'][vid] = {'name': name, 'pronunciation': ''}
                ep['participants'].setdefault(vid, {'added_at': local_time(), 'greeted_at': None})
            self._save(data)
        return self.snapshot(live)

    def set_date(self, live, value):
        value = date.fromisoformat(value).isoformat()
        with self._locked():
            data = self._load(); self._episode(data, live)['date'] = value; self._save(data)
        return self.snapshot(live)

    def edit(self, live, vid, name, pronunciation=''):
        name, pronunciation = clean_name(name), clean_name(pronunciation, optional=True)
        with self._locked():
            data = self._load()
            if vid not in data['viewers']:
                raise ValueError('시청자를 찾을 수 없습니다')
            if any(i != vid and v['name'].casefold() == name.casefold() for i, v in data['viewers'].items()):
                raise ValueError('이미 있는 이름입니다 — 다른 이름으로 수정해 주세요')
            data['viewers'][vid] = {'name': name, 'pronunciation': pronunciation}
            self._save(data)
        return self.snapshot(live)

    def delete(self, live, vid, everywhere=False):
        with self._locked():
            data = self._load(); self._episode(data, live)
            episodes = data['episodes'].values() if everywhere else [data['episodes'][str(live)]]
            for ep in episodes:
                ep['participants'].pop(vid, None)
            if not any(vid in ep['participants'] for ep in data['episodes'].values()):
                data['viewers'].pop(vid, None)
            self._save(data)
        return self.snapshot(live)

    def greeting_batch(self, live, ids=None, scope='selected'):
        snap = self.snapshot(live)
        if scope not in ('selected', 'ungreeted', 'all'):
            raise ValueError('인사 범위가 올바르지 않습니다')
        rows = snap['all'] if scope == 'all' else snap['current']
        if scope == 'ungreeted':
            rows = [r for r in rows if not r.get('greeted_at')]
        elif scope == 'selected' or (scope == 'all' and ids is not None):
            ids = ids or []
            if not isinstance(ids, list) or any(i not in {r['id'] for r in rows} for i in ids):
                raise ValueError('현재 회차의 이름을 선택해 주세요')
            rows = [r for r in rows if r['id'] in ids]
        batches, batch, chars = [], [], 0
        for row in rows:
            size = max(len(row['name']), len(row['pronunciation']))
            if batch and (len(batch) == 4 or chars + size > 100):
                batches.append(batch); batch = []; chars = 0
            batch.append(row); chars += size
        if batch: batches.append(batch)
        return batches

    def mark_greeted(self, live, recipients):
        with self._locked():
            data = self._load(); ep = self._episode(data, live)
            for r in recipients:
                # An edited/deleted identity must not be marked by an older pending greeting.
                viewer = data['viewers'].get(r['id'], {})
                if viewer.get('name') == r['name'] and r['id'] in ep['participants']:
                    ep['participants'][r['id']]['greeted_at'] = local_time()
            self._save(data)


def mentioned(text, name):
    return re.search(r'(?<![\w])' + re.escape(name) + r'(?:(?![\w])|(?=님))', text) is not None


def greeting_output(text, live, slots):
    """Only gated names actually present in final text receive a completion receipt."""
    rows = [r for r in slots.get('viewer_records', []) if mentioned(text, r['name'])]
    aliases = {r['name']: r['pronunciation'] for r in rows if r.get('pronunciation')}
    if aliases:
        pattern = r'(?<![\w])(' + '|'.join(re.escape(n) for n in sorted(aliases, key=len, reverse=True)) + r')(?:(?![\w])|(?=님))'
        spoken_text = re.sub(pattern, lambda m: aliases[m[0]], text)
    else:
        spoken_text = text
    return spoken_text, {'live': str(live), 'recipients': [{'id': r['id'], 'name': r['name']} for r in rows]}
