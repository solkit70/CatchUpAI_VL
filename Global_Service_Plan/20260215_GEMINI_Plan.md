# GEMINI's English Language Service Expansion Plan

**Date:** 2026-02-15
**Author:** GEMINI
**Status:** Proposed

## 1. Introduction

This document outlines a plan to internationalize the CUA_VL project from Korean to English. The primary goal is to make the project's documentation, guides, and templates fully accessible to English-speaking users, thereby expanding its user base and global reach.

## 2. Proposed Strategy: File-Based Localization

For a project of this scale, which primarily consists of Markdown documentation and templates, a direct file-based translation approach is the most efficient and easiest to maintain.

### 2.1. File Naming Convention

All English-language files will be created by appending a `.en` suffix before the file extension. This provides a clear and immediate distinction between Korean (original) and English (translated) content.

*   **Example:**
    *   `README.md` (Korean)
    *   `README.en.md` (English)

### 2.2. Directory Structure Modification

The existing directory structure will be preserved. Translated files will reside in the same directory as their original counterparts.

**Example: Root Directory**
```
/
├── README.md         (Korean)
├── README.en.md      (English)
├── GETTING_STARTED.md  (Korean)
├── GETTING_STARTED.en.md (English)
...
```

**Example: Templates Directory**
```
/templates/
├── daily_learning_prompt.md        (Korean)
├── daily_learning_prompt.en.md     (English)
├── roadmap_prompt_template.md      (Korean)
├── roadmap_prompt_template.en.md   (English)
...
```

### 2.3. Translation Workflow

1.  **Duplicate Files:** For each file in the translation scope, create a copy and append `.en` to the filename.
2.  **Translate Content:** Systematically translate the content of each new `.en.md` file from Korean to English.
3.  **Update Scripts:** The `scripts/sync-prompts.ps1` script needs to be reviewed and potentially updated. It must be able to handle both the original and the new `.en.md` template files to ensure that generated prompts for both languages are kept in sync.

## 3. Scope of Work (Initial Phase)

The initial translation effort will focus on the core project files that are essential for a new user to understand and use the CUA_VL methodology.

### Core Documentation:
- `README.md`
- `GETTING_STARTED.md`
- `AGENTS.md`
- `CLAUDE.md`
- `GEMINI.md`

### Templates:
- `templates/daily_learning_prompt.md`
- `templates/quick_start_prompt.md`
- `templates/roadmap_prompt_template.md`
- `templates/topic_starter.md`
- `templates/workflow_guide.md`

## 4. Conclusion

This file-based approach provides a simple, scalable, and low-overhead method for introducing English support. By following the naming convention and translation workflow, we can effectively create a parallel English experience for the project. The most critical technical task is ensuring the `sync-prompts.ps1` script is adapted to handle the new language files.

---

# GEMINI의 영어 서비스 확장 계획

**날짜:** 2026-02-15
**작성자:** GEMINI
**상태:** 제안됨

## 1. 소개

이 문서는 CUA_VL 프로젝트를 한국어에서 영어로 국제화하는 계획을 설명합니다. 주요 목표는 프로젝트의 문서, 가이드 및 템플릿을 영어 사용자가 완전히 접근할 수 있도록 만들어 사용자 기반과 글로벌 도달 범위를 확장하는 것입니다.

## 2. 제안 전략: 파일 기반 현지화

주로 마크다운 문서와 템플릿으로 구성된 이 규모의 프로젝트의 경우, 직접적인 파일 기반 번역 접근 방식이 가장 효율적이고 유지 관리가 쉽습니다.

### 2.1. 파일 이름 규칙

모든 영어 파일은 파일 확장자 앞에 `.en` 접미사를 추가하여 생성됩니다. 이는 한국어(원본)와 영어(번역) 콘텐츠를 명확하고 즉각적으로 구분합니다.

*   **예시:**
    *   `README.md` (한국어)
    *   `README.en.md` (영어)

### 2.2. 디렉토리 구조 수정

기존 디렉토리 구조는 유지됩니다. 번역된 파일은 원본 파일과 동일한 디렉토리에 위치합니다.

**예시: 루트 디렉토리**
```
/
├── README.md         (한국어)
├── README.en.md      (영어)
├── GETTING_STARTED.md  (한국어)
├── GETTING_STARTED.en.md (영어)
...
```

**예시: 템플릿 디렉토리**
```
/templates/
├── daily_learning_prompt.md        (한국어)
├── daily_learning_prompt.en.md     (영어)
├── roadmap_prompt_template.md      (한국어)
├── roadmap_prompt_template.en.md   (영어)
...
```

### 2.3. 번역 워크플로우

1.  **파일 복제:** 번역 범위에 있는 각 파일에 대해 복사본을 만들고 파일 이름에 `.en`을 추가합니다.
2.  **콘텐츠 번역:** 새로운 `.en.md` 파일 각각의 콘텐츠를 한국어에서 영어로 체계적으로 번역합니다.
3.  **스크립트 업데이트:** `scripts/sync-prompts.ps1` 스크립트를 검토하고 잠재적으로 업데이트해야 합니다. 두 언어에 대해 생성된 프롬프트가 동기화되도록 원본 및 새로운 `.en.md` 템플릿 파일을 모두 처리할 수 있어야 합니다.

## 3. 작업 범위 (초기 단계)

초기 번역 작업은 새로운 사용자가 CUA_VL 방법론을 이해하고 사용하는 데 필수적인 핵심 프로젝트 파일에 중점을 둡니다.

### 핵심 문서:
- `README.md`
- `GETTING_STARTED.md`
- `AGENTS.md`
- `CLAUDE.md`
- `GEMINI.md`

### 템플릿:
- `templates/daily_learning_prompt.md`
- `templates/quick_start_prompt.md`
- `templates/roadmap_prompt_template.md`
- `templates/topic_starter.md`
- `templates/workflow_guide.md`

## 4. 결론

이 파일 기반 접근 방식은 영어 지원을 도입하기 위한 간단하고 확장 가능하며 오버헤드가 적은 방법을 제공합니다. 명명 규칙 및 번역 워크플로우를 따르면 프로젝트에 대한 병렬 영어 경험을 효과적으로 만들 수 있습니다. 가장 중요한 기술적 과제는 `sync-prompts.ps1` 스크립트가 새로운 언어 파일을 처리하도록 조정되었는지 확인하는 것입니다.
