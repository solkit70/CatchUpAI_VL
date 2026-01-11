#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
YouTube Transcript Extraction and Translation Test
테스트용 스크립트: YouTube 영상에서 자막을 추출하고 번역합니다.

필요 라이브러리:
- youtube-transcript-api: pip install youtube-transcript-api
- anthropic: pip install anthropic
"""

import sys
import io

# Windows 콘솔 UTF-8 인코딩 설정
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

from youtube_transcript_api import YouTubeTranscriptApi
import re
import os


def extract_video_id(url):
    """
    YouTube URL에서 video ID 추출

    지원 형식:
    - https://www.youtube.com/watch?v=VIDEO_ID
    - https://youtu.be/VIDEO_ID
    - https://www.youtube.com/embed/VIDEO_ID
    """
    patterns = [
        r'(?:youtube\.com\/watch\?v=)([a-zA-Z0-9_-]+)',
        r'(?:youtu\.be\/)([a-zA-Z0-9_-]+)',
        r'(?:youtube\.com\/embed\/)([a-zA-Z0-9_-]+)',
    ]

    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)

    # URL이 아닌 경우 그대로 video_id로 간주
    return url


def get_transcript(video_id, languages=['en', 'en-US', 'en-GB']):
    """
    YouTube 영상의 자막 추출

    Args:
        video_id: YouTube video ID
        languages: 시도할 언어 목록 (기본: 영어)

    Returns:
        transcript: 자막 리스트 (딕셔너리 형태)
    """
    try:
        # YouTubeTranscriptApi 인스턴스 생성
        api = YouTubeTranscriptApi()

        # 자막 목록 가져오기
        transcript_list = api.list(video_id)

        # 원하는 언어의 자막 찾기
        try:
            transcript = transcript_list.find_transcript(languages)
        except:
            # 언어를 찾을 수 없으면 첫 번째 사용 가능한 자막 사용
            print("[!] 요청한 언어를 찾을 수 없습니다. 첫 번째 사용 가능한 자막을 사용합니다.")
            transcript = next(iter(transcript_list))

        # 자막 데이터 가져오기
        fetched = transcript.fetch()
        return fetched

    except Exception as e:
        print(f"[X] 자막 추출 실패: {e}")

        # 사용 가능한 자막 목록 출력
        try:
            api2 = YouTubeTranscriptApi()
            transcript_list = api2.list(video_id)
            print("\n사용 가능한 자막:")
            for t in transcript_list:
                print(f"  - {t.language} ({t.language_code})")
        except:
            pass

        return None


def format_transcript_with_timestamps(transcript):
    """
    타임스탬프와 함께 자막 포맷팅

    Args:
        transcript: 자막 리스트 (FetchedTranscript 객체)

    Returns:
        formatted_text: 포맷된 텍스트 (타임스탬프 포함)
    """
    formatted_lines = []

    for entry in transcript:
        # FetchedTranscriptSnippet 객체의 속성 접근
        # 초 단위를 mm:ss 형식으로 변환
        seconds = int(entry.start)
        minutes = seconds // 60
        secs = seconds % 60
        timestamp = f"[{minutes:02d}:{secs:02d}]"

        text = entry.text.strip()
        formatted_lines.append(f"{timestamp} {text}")

    return "\n".join(formatted_lines)


def format_transcript_plain(transcript):
    """
    타임스탬프 없이 순수 텍스트만 추출

    Args:
        transcript: 자막 리스트 (FetchedTranscript 객체)

    Returns:
        plain_text: 순수 텍스트
    """
    # FetchedTranscript 객체를 텍스트로 변환
    lines = []
    for entry in transcript:
        lines.append(entry.text.strip())
    return " ".join(lines)


def get_video_info(video_id):
    """
    비디오 기본 정보 출력 (실제로는 YouTube Data API 필요하지만, 여기서는 생략)
    """
    return {
        'video_id': video_id,
        'url': f"https://www.youtube.com/watch?v={video_id}"
    }


def translate_with_claude(text, api_key=None):
    """
    Claude API를 사용하여 영어를 한국어로 번역

    Args:
        text: 번역할 텍스트
        api_key: Claude API 키 (환경변수에서 가져오거나 직접 입력)

    Returns:
        translated_text: 번역된 텍스트
    """
    # Claude API 사용은 별도로 구현 필요
    # 여기서는 placeholder 제공

    if not api_key:
        api_key = os.getenv('ANTHROPIC_API_KEY')

    if not api_key:
        print("\n[!]  Claude API 키가 없습니다. 번역을 건너뜁니다.")
        print("   환경변수 ANTHROPIC_API_KEY를 설정하거나 직접 전달하세요.")
        return None

    try:
        from anthropic import Anthropic

        client = Anthropic(api_key=api_key)

        # 텍스트가 너무 길면 분할 (Claude API 토큰 제한 고려)
        max_chunk_length = 15000  # 안전한 길이

        if len(text) > max_chunk_length:
            print(f"\n[Note] 텍스트가 길어 {len(text) // max_chunk_length + 1}개 청크로 분할합니다...")
            chunks = [text[i:i+max_chunk_length] for i in range(0, len(text), max_chunk_length)]
            translated_chunks = []

            for i, chunk in enumerate(chunks, 1):
                print(f"   청크 {i}/{len(chunks)} 번역 중...")
                response = client.messages.create(
                    model="claude-sonnet-4-5-20250929",
                    max_tokens=8000,
                    messages=[
                        {
                            "role": "user",
                            "content": f"다음 영어 텍스트를 한국어로 자연스럽게 번역해주세요. 타임스탬프 형식([mm:ss])은 그대로 유지하세요:\n\n{chunk}"
                        }
                    ]
                )
                translated_chunks.append(response.content[0].text)

            return "\n\n".join(translated_chunks)
        else:
            response = client.messages.create(
                model="claude-sonnet-4-5-20250929",
                max_tokens=8000,
                messages=[
                    {
                        "role": "user",
                        "content": f"다음 영어 텍스트를 한국어로 자연스럽게 번역해주세요. 타임스탬프 형식([mm:ss])은 그대로 유지하세요:\n\n{text}"
                    }
                ]
            )
            return response.content[0].text

    except ImportError:
        print("\n[X] anthropic 라이브러리가 설치되지 않았습니다.")
        print("   설치 명령: pip install anthropic")
        return None
    except Exception as e:
        print(f"\n[X] 번역 실패: {e}")
        return None


def main():
    """메인 함수"""
    print("=" * 60)
    print("YouTube Transcript Extraction & Translation Test")
    print("=" * 60)

    # 테스트용 YouTube URL (AI Memory 360 Tour 또는 다른 영상)
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        print("\n사용법: python youtube-transcript-test.py <YouTube_URL>")
        print("\n예시:")
        print("  python youtube-transcript-test.py https://www.youtube.com/watch?v=dQw4w9WgXcQ")

        # 기본 테스트 URL (짧은 영상 권장)
        url = input("\nYouTube URL을 입력하세요 (Enter: 기본 테스트 영상): ").strip()
        if not url:
            # 기본 테스트 영상 (예: TED Talk 짧은 영상)
            url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
            print(f"기본 URL 사용: {url}")

    # Video ID 추출
    video_id = extract_video_id(url)
    print(f"\n[Video] Video ID: {video_id}")
    print(f"        URL: https://www.youtube.com/watch?v={video_id}")

    # 자막 추출
    print("\n[Search] 자막 추출 중...")
    transcript = get_transcript(video_id)

    if not transcript:
        print("\n[X] 자막을 가져올 수 없습니다.")
        return

    print(f"[OK] 자막 추출 성공! (총 {len(transcript)}개 세그먼트)")

    # 타임스탬프 포함 포맷
    print("\n" + "=" * 60)
    print("[Note] 자막 (타임스탬프 포함)")
    print("=" * 60)
    formatted_with_ts = format_transcript_with_timestamps(transcript)
    print(formatted_with_ts[:500])  # 처음 500자만 출력
    if len(formatted_with_ts) > 500:
        print(f"\n... (총 {len(formatted_with_ts)} 글자, 일부만 표시)")

    # 순수 텍스트
    print("\n" + "=" * 60)
    print("[Note] 자막 (순수 텍스트)")
    print("=" * 60)
    plain_text = format_transcript_plain(transcript)
    print(plain_text[:500])
    if len(plain_text) > 500:
        print(f"\n... (총 {len(plain_text)} 글자, 일부만 표시)")

    # 번역 시도
    print("\n" + "=" * 60)
    print("[Translate] 한국어 번역 시도")
    print("=" * 60)

    # 짧은 샘플만 번역 테스트 (전체 번역은 비용/시간 소모)
    sample_text = formatted_with_ts[:1000]  # 처음 1000자만
    print(f"\n샘플 텍스트 번역 중 (처음 1000자)...")

    translated = translate_with_claude(sample_text)

    if translated:
        print("\n[OK] 번역 성공!")
        print(translated)
    else:
        print("\n[!]  번역을 건너뛰었습니다.")

    # 파일로 저장
    print("\n" + "=" * 60)
    print("[Save] 결과 저장")
    print("=" * 60)

    output_dir = "outputs/test"
    os.makedirs(output_dir, exist_ok=True)

    # 원본 자막 저장
    with open(f"{output_dir}/{video_id}_original.txt", "w", encoding="utf-8") as f:
        f.write(formatted_with_ts)
    print(f"[OK] 원본 자막 저장: {output_dir}/{video_id}_original.txt")

    # 번역본 저장 (있다면)
    if translated:
        with open(f"{output_dir}/{video_id}_translated.txt", "w", encoding="utf-8") as f:
            f.write(translated)
        print(f"[OK] 번역본 저장: {output_dir}/{video_id}_translated.txt")

    print("\n" + "=" * 60)
    print("[OK] 테스트 완료!")
    print("=" * 60)


if __name__ == "__main__":
    main()
