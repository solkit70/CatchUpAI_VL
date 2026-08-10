---
title: "사진 4인 맺음말(말하는) 영상 프롬프트 — Gemini/Veo 생성용"
created: 2026-08-10 00:20:00
source:
  - "02-AI-Segment-Plan/expansion-scripts-20260809.md (맺음말 원문)"
  - "vl_materials/honorees/restored/ (복원 사진 — 얼굴 레퍼런스)"
  - "public/fedway-honorees-0803/videos/*_closing.mp4 (파일럿 3인 규격)"
tags:
  - fedway-liberation-day-2026
  - honorees
  - closing-video
  - prompt
---

## 이 문서의 용도

사진 있는 4인(**노태준·이재덕·장수산·오노미**)의 **맺음말(말하는) 영상**을 박창수님이 Gemini(Veo)에서 직접 생성하기 위한 프롬프트입니다. 나레이션(①생애 ②시애틀·유족 연결)은 이미 Qwen3-TTS로 만들어 슬라이드에 들어갔고, **각 슬라이드 끝에서 이 맺음말 영상이 이어 재생**됩니다(파일럿 3인과 동일 구조).

### 생성 규격 (파일럿 3인과 맞춤)

- **화면비/해상도**: 세로 **9:16, 720×1280** (파일럿과 동일)
- **길이**: Veo 기본 **8초** 권장 (맺음말 한 문장 + 앞뒤 여백). 최종 `closingVideoSec`은 제가 제공된 파일 길이를 실측해 코드에 넣습니다 — 6초든 8초든 그대로 반영됩니다.
- **얼굴 레퍼런스**: 각 인물의 **AI 복원 사진을 레퍼런스 이미지로 첨부**해 주세요. 파일럿 때 Veo가 복원 사진과 매우 유사한 인물을 만들어 낸 것과 같은 방식입니다.
  - 노태준: `vl_materials/honorees/restored/노태준_AI복원.png`
  - 이재덕: `vl_materials/honorees/restored/이재덕_AI복원.png`
  - 장수산: `vl_materials/honorees/restored/장수산_AI복원.png`
  - 오노미: `AI/RemotionStudio/public/fedway-honorees-0803/images/onomi.png` (유족 제공본)
- **음성**: 인물이 **한국어로 맺음말 한 문장을 차분하게** 말합니다. 과장된 감정 없이 담담하고 위엄 있게(추모 톤).
- **파일명**: 생성 후 아래 이름으로 저장해 `public/fedway-honorees-0803/videos/`에 넣어 주세요.
  - `notaejun_closing.mp4` / `ijaedeok_closing.mp4` / `jangsusan_closing.mp4` / `onomi_closing.mp4`

> ⚠️ 맺음말은 공훈 기록이 아니라 생전 활동을 바탕으로 **구성한 문장**입니다(1인칭 5원칙 예외). 영상 재생 구간 내내 화면에 "이 맺음말과 영상은 공훈 기록이 아니라, 생전의 활동을 바탕으로 AI로 구성한 것입니다"라는 고지가 자동으로 뜨도록 코드에 이미 반영돼 있습니다.

---

## 1. 노태준 (盧泰俊 / 건국훈장 독립장)

**맺음말 (한국어 대사)**
> 아버지와 제가 걸은 길을, 이 땅의 젊은 세대가 기억해 주기를 바랍니다.

**Veo 프롬프트 (붙여넣기용)**
```
A photorealistic, restored archival portrait video of a dignified middle-aged Korean man
from the early 20th century, matching the attached reference photo: short neat black hair,
round tortoise-shell eyeglasses, a white collared shirt, against a warm brown studio backdrop.
He looks directly into the camera and speaks calmly and with quiet dignity in Korean, saying:
"아버지와 제가 걸은 길을, 이 땅의 젊은 세대가 기억해 주기를 바랍니다."
Vertical 9:16 framing, gentle warm sepia tone, subtle natural head movement and blinking,
soft archival film grain. Solemn, respectful, memorial mood. Clean spoken Korean audio.
```

**영어 자막 (closingCaptions — 제가 코드에 넣습니다)**
> I hope the young people of this land remember the path my father and I walked.

## 2. 이재덕 (李在德 / 건국훈장 애족장)

**맺음말 (한국어 대사)**
> 이름 없이 모은 작은 정성들이 모여, 오늘의 우리가 되었습니다.

**Veo 프롬프트 (붙여넣기용)**
```
A photorealistic, restored archival portrait video of a dignified elderly Korean man
from the early 20th century, matching the attached reference photo: a long white beard,
a traditional black Korean horsehair hat (gat), and a white traditional robe (hanbok),
against a soft neutral gray backdrop. He looks directly into the camera and speaks slowly,
gently, and with quiet dignity in Korean, saying:
"이름 없이 모은 작은 정성들이 모여, 오늘의 우리가 되었습니다."
Vertical 9:16 framing, gentle warm sepia tone, subtle natural head movement and blinking,
soft archival film grain. Solemn, respectful, memorial mood. Clean spoken Korean audio.
```

**영어 자막 (closingCaptions)**
> Countless small, nameless devotions gathered — and became who we are today.

## 3. 장수산 (張水山 / 건국훈장 애국장)

**맺음말 (한국어 대사)**
> 그날 우리가 부른 만세는, 아직 끝나지 않았습니다.

**Veo 프롬프트 (붙여넣기용)**
```
A photorealistic, restored archival portrait video of a weathered, resolute Korean man
from the early 20th century, matching the attached reference photo: a brown brimmed
fedora-style hat, a rough light-colored work shirt, standing outdoors in front of trees.
He looks directly into the camera and speaks firmly but calmly, with quiet conviction, in Korean, saying:
"그날 우리가 부른 만세는, 아직 끝나지 않았습니다."
Vertical 9:16 framing, gentle warm sepia tone, subtle natural head movement and blinking,
soft archival film grain, soft natural daylight. Solemn, respectful, memorial mood. Clean spoken Korean audio.
```

**영어 자막 (closingCaptions)**
> The cry for freedom we raised that day is not yet finished.

## 4. 오노미 (吳魯美 / 대통령표창)

**맺음말 (한국어 대사)**
> 장터에 뿌린 한 장의 글이, 누군가의 가슴에 불씨가 되기를 바랐습니다.

**Veo 프롬프트 (붙여넣기용)**
```
A photorealistic portrait video of a dignified elderly Korean man in traditional dress,
matching the attached reference photo: a black traditional Korean horsehair hat (gat) with
a black chin strap, a gray mustache, and a white silk hanbok robe with subtle embroidery,
standing in a traditional hanok courtyard. He looks directly into the camera and speaks
gently and warmly, with quiet dignity, in Korean, saying:
"장터에 뿌린 한 장의 글이, 누군가의 가슴에 불씨가 되기를 바랐습니다."
Vertical 9:16 framing, gentle warm tone, subtle natural head movement and blinking.
Solemn, respectful, memorial mood. Clean spoken Korean audio.
```

**영어 자막 (closingCaptions)**
> I hoped that single sheet I scattered at the market would become a spark in someone's heart.

---

## 제공 후 제가 할 일 (참고)

4개 영상이 `videos/` 폴더에 들어오면:
1. 각 파일 길이 실측(ffprobe) → data.ts의 해당 슬라이드(4·7·8·10)에 `closingVideoSrc`, `closingVideoSec`, `closingCaptions`, `closingCaptionTimings` 추가.
2. `getSlideDurationSec`가 맺음말 유무를 자동 처리하므로 전체 길이는 자동 반영.
3. 4인 슬라이드는 나레이션 → (0.6초 숨) → 맺음말 영상 순으로 재생됩니다.
