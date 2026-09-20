#!/usr/bin/env python3
"""시그니처 끝인사 — 15개 언어 대본 → mp3 (CVL 4, 2026-09-17).

방송 마지막에 배경음악 위로 15개 언어로 인사한다 (진행자 결정: 2분 16초, 전문). 대본은
`output/private/signoff.json` 이 원본이다 — 번역을 고치면 이 스크립트가 바뀐 줄만 다시 합성한다.
런타임에는 합성하지 않는다: 방송 끝에 네트워크가 흔들려도 끝인사는 나가야 한다.

언어 순서 = 총 화자 수 순 (Ethnologue 2024 대략치), 한국어만 맨 앞 (우리 방송이니까).

실행:
    python signoff_build.py            # 대본 없으면 기본 대본 생성 + 전부 합성 · 있으면 바뀐 줄만
    python signoff_build.py --force    # 전부 다시
    python signoff_build.py --play     # 합성 뒤 기본 출력 장치로 순서대로 들어 본다 (OBS 아님)
    python signoff_build.py --set intro  # 방송 중간 자기소개 샘플 (9/18)
"""
from __future__ import annotations

import argparse
import asyncio
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
M7_SRC = HERE.parents[2] / "07-CoMC-Engine-POC" / "src"
sys.path.insert(0, str(M7_SRC))
from common import now_iso, out, read_json, write_json  # noqa: E402

# 세트: signoff(끝인사) · intro(방송 중간 자기소개 샘플, 9/18 추가). --set 으로 고른다.
SETS = {}

SIGNATURE = "오늘도 Catch Up AI 의 라이브 방송에 참여해 주셔서 감사합니다. 다음 주에 다시 뵙겠습니다. 감사합니다."
DEFAULT_LINES = [
    ("ko", "한국어",   "ko-KR-SunHiNeural",     SIGNATURE),
    ("en", "English",  "en-US-JennyNeural",     "Thank you for joining the Catch Up AI live stream today. See you again next week. Thank you."),
    ("zh", "中文",     "zh-CN-XiaoxiaoNeural",  "感谢您今天参与 Catch Up AI 的直播。下周再见。谢谢大家。"),
    ("hi", "हिन्दी",   "hi-IN-SwaraNeural",     "आज Catch Up AI के लाइव प्रसारण में शामिल होने के लिए धन्यवाद। अगले सप्ताह फिर मिलेंगे। धन्यवाद।"),
    ("es", "Español",  "es-MX-DaliaNeural",     "Gracias por acompañarnos hoy en la transmisión en vivo de Catch Up AI. Nos vemos la próxima semana. Gracias."),
    ("fr", "Français", "fr-FR-DeniseNeural",    "Merci d'avoir participé au direct de Catch Up AI aujourd'hui. À la semaine prochaine. Merci."),
    ("ar", "العربية",  "ar-SA-ZariyahNeural",   "شكرًا لانضمامكم اليوم إلى البث المباشر لـ Catch Up AI. نراكم الأسبوع المقبل. شكرًا لكم."),
    ("bn", "বাংলা",    "bn-BD-NabanitaNeural",  "আজ Catch Up AI-এর লাইভ সম্প্রচারে যোগ দেওয়ার জন্য ধন্যবাদ। আগামী সপ্তাহে আবার দেখা হবে। ধন্যবাদ।"),
    ("pt", "Português", "pt-BR-FranciscaNeural", "Obrigado por participar da transmissão ao vivo do Catch Up AI hoje. Até a próxima semana. Obrigado."),
    ("ru", "Русский",  "ru-RU-SvetlanaNeural",  "Спасибо, что присоединились сегодня к прямому эфиру Catch Up AI. Увидимся на следующей неделе. Спасибо."),
    ("ur", "اردو",     "ur-PK-UzmaNeural",      "آج Catch Up AI کی لائیو نشریات میں شامل ہونے کا شکریہ۔ اگلے ہفتے پھر ملیں گے۔ شکریہ۔"),
    ("id", "Bahasa Indonesia", "id-ID-GadisNeural", "Terima kasih telah bergabung di siaran langsung Catch Up AI hari ini. Sampai jumpa minggu depan. Terima kasih."),
    ("de", "Deutsch",  "de-DE-KatjaNeural",     "Vielen Dank, dass Sie heute beim Catch Up AI Livestream dabei waren. Bis nächste Woche. Danke schön."),
    ("ja", "日本語",   "ja-JP-NanamiNeural",    "本日も Catch Up AI のライブ配信にご参加いただき、ありがとうございました。また来週お会いしましょう。ありがとうございました。"),
    ("vi", "Tiếng Việt", "vi-VN-HoaiMyNeural",  "Cảm ơn bạn đã tham gia buổi phát trực tiếp của Catch Up AI hôm nay. Hẹn gặp lại vào tuần sau. Xin cảm ơn."),
]
SETS["signoff"] = (SIGNATURE, DEFAULT_LINES)

# 방송 중간 샘플 — 전문 (사용자 결정 9/18: 「길어도 괜찮다」). 언어당 7~9초, 합계 약 2분.
# 짧은 한 문장 판(「AI 부MC 코엠씨입니다」, 1분 25초)도 만들어 봤지만 원래 문장으로 확정.
INTRO_KO = "안녕하세요, 저는 Catch Up AI 라이브의 AI 부MC 코엠씨입니다. 만나서 반갑습니다."
INTRO_LINES = [
    ("ko", "한국어",   "ko-KR-SunHiNeural",     INTRO_KO),
    ("en", "English",  "en-US-JennyNeural",     "Hello, I'm CoMC, the AI co-host of the Catch Up AI live stream. Nice to meet you."),
    ("zh", "中文",     "zh-CN-XiaoxiaoNeural",  "大家好，我是 Catch Up AI 直播的 AI 副主持人 CoMC。很高兴见到大家。"),
    ("hi", "हिन्दी",   "hi-IN-SwaraNeural",     "नमस्ते, मैं CoMC हूँ, Catch Up AI लाइव की AI सह-होस्ट। आपसे मिलकर खुशी हुई।"),
    ("es", "Español",  "es-MX-DaliaNeural",     "Hola, soy CoMC, la co-presentadora de IA del directo de Catch Up AI. Mucho gusto."),
    ("fr", "Français", "fr-FR-DeniseNeural",    "Bonjour, je suis CoMC, la co-animatrice IA du direct Catch Up AI. Enchantée."),
    ("ar", "العربية",  "ar-SA-ZariyahNeural",   "مرحبًا، أنا CoMC، المقدمة المساعدة بالذكاء الاصطناعي في بث Catch Up AI المباشر. سعيدة بلقائكم."),
    ("bn", "বাংলা",    "bn-BD-NabanitaNeural",  "নমস্কার, আমি CoMC, Catch Up AI লাইভের AI সহ-উপস্থাপক। আপনাদের সাথে দেখা হয়ে ভালো লাগলো।"),
    ("pt", "Português", "pt-BR-FranciscaNeural", "Olá, eu sou a CoMC, co-apresentadora de IA da live do Catch Up AI. Prazer em conhecê-los."),
    ("ru", "Русский",  "ru-RU-SvetlanaNeural",  "Здравствуйте, я CoMC, ИИ-соведущая прямого эфира Catch Up AI. Рада знакомству."),
    ("ur", "اردو",     "ur-PK-UzmaNeural",      "السلام علیکم، میں CoMC ہوں، Catch Up AI لائیو کی AI شریک میزبان۔ آپ سے مل کر خوشی ہوئی۔"),
    ("id", "Bahasa Indonesia", "id-ID-GadisNeural", "Halo, saya CoMC, co-host AI dari siaran langsung Catch Up AI. Senang bertemu dengan Anda."),
    ("de", "Deutsch",  "de-DE-KatjaNeural",     "Hallo, ich bin CoMC, die KI-Co-Moderatorin des Catch Up AI Livestreams. Schön, Sie kennenzulernen."),
    ("ja", "日本語",   "ja-JP-NanamiNeural",    "こんにちは、Catch Up AI ライブの AI 副MC、コエムシーです。よろしくお願いします。"),
    ("vi", "Tiếng Việt", "vi-VN-HoaiMyNeural",  "Xin chào, tôi là CoMC, đồng dẫn chương trình AI của buổi phát trực tiếp Catch Up AI. Rất vui được gặp các bạn."),
]
SETS["intro"] = (INTRO_KO, INTRO_LINES)
RATE = {"signoff": "+0%", "intro": "+0%"}    # 둘 다 보통 속도 (사용자 9/18: 길어도 괜찮다)


def sig(voice: str, text: str) -> str:
    return hashlib.sha256(f"{voice}|{text}".encode("utf-8")).hexdigest()[:12]


async def build(force: bool, set_name: str = "signoff") -> dict:
    import edge_tts
    import soundfile as sf
    signature, default_lines = SETS[set_name]
    D = out("private") / set_name
    J = out("private") / f"{set_name}.json"
    D.mkdir(parents=True, exist_ok=True)
    doc = read_json(J) if J.exists() else {"set": set_name, "signature": signature, "lines": [
        {"code": c, "name": n, "voice": v, "text": t} for c, n, v, t in default_lines]}
    total = 0.0
    for ln in doc["lines"]:
        ln.setdefault("file", f"{ln['code']}.mp3")
        p = D / ln["file"]
        rate = RATE.get(set_name, "+0%")
        h = sig(ln["voice"], ln["text"] + rate)
        if force or ln.get("sig") != h or not p.exists():
            await edge_tts.Communicate(ln["text"], ln["voice"], rate=rate).save(str(p))
            data, sr = sf.read(str(p))
            ln["seconds"] = round(len(data) / sr, 1)
            ln["sig"] = h
            print(f"  합성 {ln['seconds']:5.1f}s  {ln['name']:<18} {ln['voice']}")
        else:
            print(f"  유지 {ln.get('seconds', 0):5.1f}s  {ln['name']:<18}")
        total += ln.get("seconds", 0)
    doc["total_seconds"] = round(total)
    doc["built_at"] = now_iso()
    write_json(J, doc)
    print(f"  합계 {doc['total_seconds']}초 · {len(doc['lines'])}개 언어 → {J.name}")
    return doc


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--play", action="store_true", help="기본 출력 장치로 들어 본다")
    ap.add_argument("--set", default="signoff", choices=sorted(SETS), help="signoff(끝인사) · intro(자기소개 샘플)")
    args = ap.parse_args()
    doc = asyncio.run(build(args.force, args.set))
    if args.play:
        import sounddevice as sd
        import soundfile as sf
        for ln in doc["lines"]:
            data, sr = sf.read(str(out("private") / args.set / ln["file"]), dtype="float32")
            print(f"  ▶ {ln['name']}")
            sd.play(data, sr)
            sd.wait()
    return 0


if __name__ == "__main__":
    sys.exit(main())
