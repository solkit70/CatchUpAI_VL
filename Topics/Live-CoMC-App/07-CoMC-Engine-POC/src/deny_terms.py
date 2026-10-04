"""CVL8 private, operator-managed terms. Never report matched text."""
import json
import re
import sys
import unicodedata

_warned = set()
# 파일을 한 번 읽어 두고 수정 시각 · 크기가 바뀔 때만 다시 읽는다 (CVL8 후속, 10/2).
# 예전에는 matches() 마다 파일을 읽어 볼트 검색 1회에 약 5만 번 읽었다 (18.6초 → 2.1초).
# 방송 중 진행자가 목록을 고치면 다음 호출에서 바로 반영된다.
_cache = {'key': None, 'rows': [], 'warning': None, 'terms': []}


def normalize(text):
    return re.sub(r'\s+', ' ', unicodedata.normalize('NFKC', str(text))).strip().casefold()


def _stamp(path):
    try:
        st = path.stat()
        return (str(path), st.st_mtime_ns, st.st_size)
    except OSError:
        return (str(path), None, None)


def load():
    from common import out
    path = out('private') / 'm11' / 'deny_terms.json'
    key = _stamp(path)
    if _cache['key'] == key:
        return _cache['rows'], _cache['warning']
    rows, warning = _read(path)
    _cache.update(key=key, rows=rows, warning=warning, terms=[(normalize(r['term']), r['kind']) for r in rows])
    return rows, warning


def _read(path):
    warning = None
    try:
        data = json.loads(path.read_text(encoding='utf-8-sig'))
        if data.get('version') != 1 or not isinstance(data.get('terms'), list):
            raise ValueError()
        rows = data['terms']
        if any(not isinstance(r, dict) or not isinstance(r.get('term'), str) or not normalize(r['term'])
               or r.get('kind') not in ('customer', 'partner', 'money') for r in rows):
            raise ValueError()
    except FileNotFoundError:
        rows, warning = [], 'missing'
    except (OSError, ValueError, TypeError, AttributeError):
        rows, warning = [], 'unreadable'
    if warning and (str(path), warning) not in _warned:
        _warned.add((str(path), warning))
        print('⚠ 금칙 목록을 읽을 수 없어 빈 목록으로 진행합니다.', file=sys.stderr)
    return rows, warning


def status():
    rows, warning = load()
    return {'count': len(rows), 'warning': warning,
            'kinds': sorted({r['kind'] for r in rows})}


def matches(text):
    load()
    if not _cache['terms']:
        return []
    hay = normalize(text)
    return [kind for term, kind in _cache['terms'] if term in hay]


def excluded(evidence):
    return any(matches(evidence.get(k, '')) for k in ('quote', 'title', 'path'))


def redact(value):
    if isinstance(value, str):
        return '[금칙 정보 제외]' if matches(value) else value
    if isinstance(value, list):
        return [redact(x) for x in value]
    if isinstance(value, dict):
        return {('[금칙 정보 제외]' if matches(k) else k): redact(v) for k, v in value.items()}
    return value


def review_sources(draft, kept):
    paths = list(dict.fromkeys(c['evidence_path'] for c in draft.get('claim_map', [])
                              if c.get('sentence_idx') in kept and not matches(c.get('evidence_path', ''))))
    personal = any(p.replace('\\', '/').casefold().startswith(('journal/', 'ai/roundup/')) for p in paths)
    return {'personal_record': personal, 'sources': paths}
