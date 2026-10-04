"""Small caption pages paired with the exact speech substring."""
import re
import time
import unicodedata
import os
import tempfile

from common import out, write_json

HOLD_S = 3.0


def wrap_lines(text, columns=48):
    lines, line, width = [], '', 0
    def weight_of(value):
        return sum(2 if unicodedata.east_asian_width(c) in ('W', 'F') else 1 for c in value)
    for char in text:
        weight = 2 if unicodedata.east_asian_width(char) in ('W', 'F') else 1
        if char == '\n':
            if line.strip(): lines.append(line.strip())
            line, width = '', 0
        elif width + weight > columns:
            boundary = line.rfind(' ')
            if boundary > 0 and boundary >= len(line) // 2:
                lines.append(line[:boundary].strip())
                line = line[boundary + 1:]
                width = weight_of(line)
            else:
                if line.strip(): lines.append(line.strip())
                line, width = '', 0
        if char != '\n':
            line += char
            width += weight
    if line.strip(): lines.append(line.strip())
    return lines


def pages(text):
    remaining = text.strip()
    result = []
    while remaining:
        end = 1
        while end <= len(remaining) and len(wrap_lines(remaining[:end])) <= 3:
            end += 1
        end = min(end - 1, len(remaining))
        if end < len(remaining):
            # Prefer a complete sentence, then a phrase/word boundary.
            prefix = remaining[:end]
            boundaries = [m.end() for m in re.finditer(r'[.!?。！？](?:\s|$)', prefix)]
            if boundaries:
                end = boundaries[-1]
            else:
                breaks = [m.end() for m in re.finditer(r'[,，;；]\s*|\s+', prefix)]
                if breaks and breaks[-1] >= end // 2: end = breaks[-1]
        speech = remaining[:end].strip()
        if speech:
            result.append({'speech': speech, 'text': '\n'.join(wrap_lines(speech))})
        remaining = remaining[end:].lstrip()
    return result


def publish(token, phase, text='', index=0, total=0):
    target = out('captions.json')
    target.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix='caption_', suffix='.json', dir=target.parent)
    os.close(fd)
    try:
        write_json(temporary, {'token': token, 'phase': phase, 'text': text,
                   'index': index, 'total': total,
                   'expires_at': time.time() + HOLD_S if phase == 'finished' else None})
        os.replace(temporary, target)
    finally:
        if os.path.exists(temporary): os.unlink(temporary)
