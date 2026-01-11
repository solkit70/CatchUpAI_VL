#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
YouTube Transcript to Markdown Generator
YouTube 자막을 구조화된 마크다운 문서로 변환합니다.

필요 라이브러리:
- youtube-transcript-api
- anthropic
"""

import sys
import io
import os
import re
from datetime import datetime

# Windows 콘솔 UTF-8 인코딩 설정
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

from youtube_transcript_api import YouTubeTranscriptApi


def extract_video_id(url):
    """YouTube URL에서 video ID 추출"""
    patterns = [
        r'(?:youtube\.com\/watch\?v=)([a-zA-Z0-9_-]+)',
        r'(?:youtu\.be\/)([a-zA-Z0-9_-]+)',
        r'(?:youtube\.com\/embed\/)([a-zA-Z0-9_-]+)',
    ]

    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)

    return url


def get_transcript(video_id, languages=['en']):
    """YouTube 영상의 자막 추출"""
    try:
        api = YouTubeTranscriptApi()
        transcript_list = api.list(video_id)

        try:
            transcript = transcript_list.find_transcript(languages)
        except:
            print("[!] 요청한 언어를 찾을 수 없습니다. 첫 번째 사용 가능한 자막을 사용합니다.")
            transcript = next(iter(transcript_list))

        fetched = transcript.fetch()
        return fetched

    except Exception as e:
        print(f"[X] 자막 추출 실패: {e}")
        return None


def format_timestamp(seconds):
    """초를 HH:MM:SS 형식으로 변환"""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)

    if hours > 0:
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
    else:
        return f"{minutes:02d}:{secs:02d}"


def create_timeline(transcript):
    """타임라인 생성 (5분 간격으로 요약)"""
    timeline = []
    interval = 300  # 5분 = 300초

    current_time = 0
    current_texts = []

    for entry in transcript:
        if entry.start >= current_time + interval:
            if current_texts:
                # 현재 구간 요약
                timestamp = format_timestamp(current_time)
                timeline.append(f"- **{timestamp}**: {' '.join(current_texts[:50])}...")
                current_texts = []
            current_time += interval

        current_texts.append(entry.text.strip())

    # 마지막 구간
    if current_texts:
        timestamp = format_timestamp(current_time)
        timeline.append(f"- **{timestamp}**: {' '.join(current_texts[:50])}...")

    return "\n".join(timeline)


def summarize_with_claude(transcript_text, video_title="", api_key=None):
    """
    Claude API를 사용하여 자막 요약

    Args:
        transcript_text: 전체 자막 텍스트
        video_title: 영상 제목
        api_key: Claude API 키

    Returns:
        dict: summary, key_points, sections
    """
    if not api_key:
        api_key = os.getenv('ANTHROPIC_API_KEY')

    if not api_key:
        print("\n[!] Claude API 키가 없습니다. 요약을 건너뜁니다.")
        return {
            'summary': "요약을 생성하려면 ANTHROPIC_API_KEY 환경변수를 설정하세요.",
            'key_points': ["요약 없음"],
            'sections': []
        }

    try:
        from anthropic import Anthropic

        client = Anthropic(api_key=api_key)

        # 요약 프롬프트
        prompt = f"""다음은 YouTube 영상 "{video_title}"의 자막입니다.

자막 내용:
{transcript_text[:15000]}  # 처음 15000자만 사용

다음 형식으로 요약해주세요:

## 요약
(2-3문장으로 영상 전체 내용 요약)

## 핵심 포인트
- (핵심 포인트 1)
- (핵심 포인트 2)
- (핵심 포인트 3)
- ...

## 주요 섹션
### 섹션 1: [제목]
- (핵심 내용)

### 섹션 2: [제목]
- (핵심 내용)

...

모든 내용을 한국어로 작성하세요."""

        response = client.messages.create(
            model="claude-sonnet-4-5-20250929",
            max_tokens=4000,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        result_text = response.content[0].text

        # 파싱 (간단한 방식)
        summary_match = re.search(r'## 요약\n(.+?)(?=\n## |\Z)', result_text, re.DOTALL)
        key_points_match = re.search(r'## 핵심 포인트\n(.+?)(?=\n## |\Z)', result_text, re.DOTALL)
        sections_match = re.search(r'## 주요 섹션\n(.+)', result_text, re.DOTALL)

        summary = summary_match.group(1).strip() if summary_match else "요약 없음"
        key_points_text = key_points_match.group(1).strip() if key_points_match else ""
        key_points = [line.strip() for line in key_points_text.split('\n') if line.strip().startswith('-')]

        sections_text = sections_match.group(1).strip() if sections_match else ""

        return {
            'summary': summary,
            'key_points': key_points,
            'sections': sections_text
        }

    except ImportError:
        print("\n[X] anthropic 라이브러리가 설치되지 않았습니다.")
        return {
            'summary': "Claude API를 사용하려면 anthropic 라이브러리를 설치하세요.",
            'key_points': ["요약 없음"],
            'sections': ""
        }
    except Exception as e:
        print(f"\n[X] 요약 생성 실패: {e}")
        return {
            'summary': "요약 생성 중 오류가 발생했습니다.",
            'key_points': ["요약 없음"],
            'sections': ""
        }


def generate_markdown(video_id, video_url, video_title, transcript, api_key=None):
    """
    마크다운 문서 생성

    Args:
        video_id: YouTube video ID
        video_url: YouTube URL
        video_title: 영상 제목
        transcript: 자막 데이터
        api_key: Claude API 키

    Returns:
        markdown_content: 마크다운 문서 내용
    """
    # 전체 자막 텍스트 생성
    full_text = " ".join([entry.text.strip() for entry in transcript])

    # Claude로 요약 생성
    print("\n[Note] Claude API로 영상 요약 중...")
    analysis = summarize_with_claude(full_text, video_title, api_key)

    # 타임라인 생성
    timeline = create_timeline(transcript)

    # 마크다운 템플릿
    today = datetime.now().strftime("%Y-%m-%d")

    markdown = f"""# {video_title}

**원본 영상**: [{video_url}]({video_url})
**작성일**: {today}
**Video ID**: {video_id}

---

## 요약

{analysis['summary']}

---

## 핵심 포인트

"""

    for point in analysis['key_points']:
        markdown += f"{point}\n"

    markdown += f"""
---

## 주요 내용

{analysis['sections']}

---

## 타임라인

{timeline}

---

## 전체 자막 (타임스탬프 포함)

"""

    # 전체 자막 추가
    for entry in transcript:
        timestamp = format_timestamp(entry.start)
        markdown += f"**[{timestamp}]** {entry.text.strip()}\n\n"

    markdown += f"""
---

*이 문서는 YouTube 자막을 기반으로 자동 생성되었습니다.*
*생성 도구: YouTube-to-MD Skill*
"""

    return markdown


def main():
    """메인 함수"""
    print("=" * 60)
    print("YouTube Transcript to Markdown Generator")
    print("=" * 60)

    if len(sys.argv) < 2:
        print("\n사용법: python md-generator.py <YouTube_URL> [제목]")
        print("\n예시:")
        print("  python md-generator.py https://www.youtube.com/watch?v=VIDEO_ID \"영상 제목\"")
        return

    url = sys.argv[1]
    video_id = extract_video_id(url)
    video_url = f"https://www.youtube.com/watch?v={video_id}"

    # 제목이 주어지지 않으면 Video ID 사용
    if len(sys.argv) >= 3:
        video_title = sys.argv[2]
    else:
        video_title = f"YouTube Video {video_id}"

    print(f"\n[Video] Video ID: {video_id}")
    print(f"        제목: {video_title}")

    # 자막 추출
    print("\n[Search] 자막 추출 중...")
    transcript = get_transcript(video_id)

    if not transcript:
        print("\n[X] 자막을 가져올 수 없습니다.")
        return

    print(f"[OK] 자막 추출 성공! (총 {len(list(transcript))} 세그먼트)")

    # 마크다운 생성
    print("\n[Note] 마크다운 생성 중...")
    markdown_content = generate_markdown(
        video_id=video_id,
        video_url=video_url,
        video_title=video_title,
        transcript=transcript,
        api_key=os.getenv('ANTHROPIC_API_KEY')
    )

    # 파일 저장
    output_dir = "outputs/markdown"
    os.makedirs(output_dir, exist_ok=True)

    # 안전한 파일명 생성
    safe_title = re.sub(r'[^\w\s-]', '', video_title).strip()
    safe_title = re.sub(r'[-\s]+', '-', safe_title)
    filename = f"{datetime.now().strftime('%Y%m%d')}_{safe_title}_{video_id}.md"
    filepath = os.path.join(output_dir, filename)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(markdown_content)

    print(f"\n[OK] 마크다운 파일 저장: {filepath}")

    # 간단한 통계
    print(f"\n[Note] 통계:")
    print(f"        자막 길이: {len(list(transcript))} 세그먼트")
    print(f"        마크다운 크기: {len(markdown_content)} 글자")

    print("\n" + "=" * 60)
    print("[OK] 변환 완료!")
    print("=" * 60)


if __name__ == "__main__":
    main()
