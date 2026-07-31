<div align="center">

# 모세종 | Python · FastAPI 기반 AI 서비스 개발자

### 현장에서 발견한 문제를 데이터와 AI가 동작하는 서비스로 바꿉니다.

물류·운영 현장에서 **8년 9개월** 동안 재고·납기·구매·출고 흐름을 경험했습니다.  
이제는 그 문제 정의 경험을 바탕으로 **Python / FastAPI / AI 기능을 실제 서비스 흐름에 연결**하고 있습니다.

[![Resume](https://img.shields.io/badge/WEB_RESUME-2563EB?style=for-the-badge&logo=readme&logoColor=white)](https://mosejong.github.io/mosejong/resume.html)
[![PDF](https://img.shields.io/badge/PDF_RESUME-E11D48?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](./assets/모세종.pdf)
[![GitHub](https://img.shields.io/badge/GITHUB-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/mosejong)

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-009639?style=flat-square&logo=nginx&logoColor=white)

</div>

---

## 👋 About Me

저는 **AI 모델을 호출하는 코드 하나**보다, 그 기능이 실제 서비스 안에서 어떻게 쓰이는지를 더 중요하게 생각합니다.

- 사용자 문제를 **기능 요구사항과 데이터 흐름**으로 정리합니다.
- AI 기능을 **API · DB · UI · 배포 흐름**에 연결합니다.
- 결과가 그럴듯한지보다 **테스트 · 지표 · 근거 · 실패 케이스**로 검증하려고 합니다.
- 현장에서 익힌 우선순위·병목·검수 감각을 소프트웨어 설계에 가져옵니다.

> **물류·운영 8년 9개월 → KDT AI Human 4기 수료 → Python/FastAPI 기반 AI 서비스 개발**

---

## 🚀 Selected Projects

| Project | What I did | Evidence |
|---|---|---|
| **[SchoolBridge](https://github.com/Maxmunzy/multicultural-ai)** | 번역·TTS 파이프라인 설계, NLLB, 학교 용어사전, 정보 보존 후처리 | **39.0 → 89.6**, 8개 언어, backend 27 tests, Android E2E |
| **[공공조달 수요 기반 입지·물류 거점 분석](https://github.com/mosejong/procurement-logistics-ai)** | 물류 현장 경험을 공공데이터 제품으로 확장, 수집·분석·추천·AI 해석 구현 | 6개 기관·9개 데이터소스, 전국 분석, **공모전 대면심사 진출** |
| **[나의 진로 아카데미아](https://github.com/neunglog-sys/job_simulator)** | Reporting · Data Pipeline, 적합도 리포트·추천 근거 개인화·커리어넷 연동·CI | 직무군 38개, 시나리오 37종, 프로젝트 전체 pytest 564 cases |
| **[Rainbow Bridge](https://github.com/mosejong/Rainbow-Bridge)** | Team Lead · PM, Backend Integration, 배포·운영 흐름 정리 | FastAPI · NCP · Docker · nginx · Expo 기반 통합 시연 |

---

## 🥇 SchoolBridge

### 다문화 가정 학부모를 위한 가정통신문 AI 번역 · TTS 서비스

**제가 가장 깊게 설명할 수 있는 AI 파이프라인 설계 프로젝트입니다.**

가정통신문은 단순히 문장을 자연스럽게 번역하는 것보다 **날짜·시간·비용·준비물·제출 여부 같은 행동 정보가 틀리지 않는 것**이 더 중요하다고 판단했습니다.

### My Role

- `facebook/nllb-200-distilled-600M` 기반 **8개 언어 번역 파이프라인** 설계
- 학교 현장 표현을 위한 **도메인 용어사전(Glossary)** 구축
- 날짜·금액·전화번호·URL 등 **핵심 정보 보존 후처리**
- Edge-TTS 언어별 보이스 매핑 및 음성 출력
- 번역 품질 검수 루프와 Round-trip 평가
- FastAPI 통합 파이프라인 및 Android 실기기 E2E 검증 참여

### Result

`NLLB 39.0 → Glossary 적용 89.6` · `8 languages` · `backend pytest 27` · `GitHub Actions PR gate`

**Project Result:** KDT 팀 프로젝트 **최우수상**

### Tech

`Python` · `FastAPI` · `Transformers` · `NLLB` · `Pandas` · `Glossary` · `Edge-TTS` · `Docker` · `Android`

🔗 **[Repository](https://github.com/Maxmunzy/multicultural-ai)**

---

## 🚚 공공조달 수요 기반 입지 · 물류 거점 분석

### 8년 9개월의 물류 경험을 처음으로 소프트웨어 제품에 연결한 개인 프로젝트

물류 현장에서 일하며 쌓은 **수요·납품·재고·거점에 대한 감각**을 경험으로만 남기지 않고, 공공데이터를 이용해 확인할 수 있는 제품으로 만들었습니다.

나라장터 입찰공고를 단순 검색하는 대신 **지역·품목별 공공수요 신호**로 해석하고, 계약·인구·상권·물류창고·학교급식 데이터를 함께 연결했습니다.

### What I Built

- 조달청·aT·행정안전부·소상공인시장진흥공단·국토교통부·KOSIS 등 **6개 기관 / 9개 데이터소스 결합**
- 나라장터 입찰공고 **100,083건**, 계약정보 **38,367건** 수집·분석
- aT 학교급식 입찰·낙찰 **734,242건**으로 수요 근거 보강
- TF-IDF + Logistic Regression 기반 공고 분류
- 지역·품목별 `opportunity_score`, 인구 보정, 경쟁도, 물류 거점 지표 설계
- Gemini API 기반 **AI 해석 5종**
- Streamlit 기반 전국 지도·지역 비교·물류 거점 분석 대시보드

### External Validation

**2026 공공조달데이터·AI 활용 창업경진대회 출품 → 대면심사 진출**

### Tech

`Python` · `Pandas` · `Scikit-learn` · `Public Data API` · `Gemini API` · `Streamlit`

🔗 **[Repository](https://github.com/mosejong/procurement-logistics-ai)** · **[Live Demo](https://procurement-logistics-ai-5qian47widxpcuqefpjipy.streamlit.app)**

---

## 🎓 나의 진로 아카데미아

### AI 아바타와 상담하고, 가상 회사에서 직무를 직접 체험하는 진로 탐색 플랫폼

KDT 과정의 최종 팀 프로젝트로, **읽고 고르는 진로 탐색이 아니라 직접 해보고 판단하는 경험**을 목표로 구현했습니다.

### My Role — Reporting · Data Pipeline

- 직무 적합도 **리포트 구조 설계**: 역량 레이더 · AI 해석 · 평가 근거 각주 · PDF 출력
- 상담·체험 기록을 이용한 **추천 근거 개인화**
- **커리어넷 진로심리검사 연동**
- 캐릭터 스프라이트 작업
- **CI 파이프라인** 구성

### Project Scale

`직무군 38개` · `세부직업 204개` · `체험 시나리오 37종` · `pytest 564 cases (project-wide)`

### Architecture

`React 19` · `TypeScript` · `FastAPI` · `PostgreSQL + pgvector` · `Redis` · `OpenAI` · `Gemini` · `MuseTalk` · `Docker Compose` · `Nginx`

🔗 **[Repository](https://github.com/neunglog-sys/job_simulator)**

---

## 🌈 Rainbow Bridge

### AI 펫로스 애프터케어 서비스 · 6인 팀 프로젝트

이 프로젝트에서 제 핵심 역할은 특정 모델 하나를 깊게 구현하는 것보다 **여러 기능이 하나의 사용자 흐름으로 연결되도록 팀과 서비스를 정리하는 것**이었습니다.

### My Role — Team Lead · PM · Backend Integration

- 역할 분담·일정·기능 우선순위 조율
- 서비스 흐름 및 API 통합 참여
- NCP 서버 운영
- Docker 기반 배포 환경 구성
- nginx / HTTPS 운영
- Expo 기반 iOS·Android 모바일 시연
- AI 기능·GPU 터널링·멀티미디어 파이프라인 통합
- 안전 라우팅·평가 리포트·제출 산출물 정리

### What It Proved

**모델 → API → 서버 → 모바일 → 시연**까지 여러 파트를 연결하는 경험과, 6인 팀의 개발 흐름을 끝까지 운영한 경험을 얻었습니다.

### Tech

`FastAPI` · `MongoDB` · `SQLite` · `Redis` · `Gemini API` · `TTS` · `LivePortrait` · `FFmpeg` · `Docker` · `NCP` · `nginx` · `Expo`

🔗 **[Repository](https://github.com/mosejong/Rainbow-Bridge)**

---

## 🧪 R&D / Side Project

### [Context Capsule](https://github.com/mosejong/context-capsule)

AI에게 레포지토리 작업을 넘길 때 필요한 **관련 파일·작업 범위·금지 영역·완료 기준을 정리하는 AI Handoff 도구**입니다.

현재 대표 포트폴리오에서는 한 단계 뒤에 두고 있지만, 개인적으로 **Retrieval · FastAPI · 테스트 · 릴리즈 자동화**를 실험하고 개선하는 프로젝트로 유지하고 있습니다.

`Python` · `FastAPI` · `Streamlit` · `CLI` · `Retrieval` · `GitHub Actions`

---

## 🛠 Tech Stack

| Area | Stack |
|---|---|
| **Backend / API** | Python, FastAPI, REST API, Pydantic, SQLite, MongoDB, PostgreSQL, Redis |
| **AI / NLP** | LLM API, OpenAI, Gemini, Transformers, NLLB, RAG, pgvector, TTS, Prompt Engineering |
| **Data** | Pandas, CSV, Scikit-learn, Public Data API |
| **Infra / Delivery** | Docker, Docker Compose, NCP, nginx, HTTPS, GitHub Actions |
| **Frontend / Client** | React, TypeScript, Vite, Streamlit, Android, Expo |
| **Validation** | pytest, E2E, quality evaluation, regression checks, CI gates |

---

## 🧭 How I Work

**Problem → Design → Build → Verify → Explain**

1. **Problem** — 사용자와 현장의 문제를 먼저 정의합니다.
2. **Design** — 데이터 흐름·실패 케이스·검증 기준을 함께 설계합니다.
3. **Build** — Python/FastAPI를 중심으로 AI 기능을 서비스에 연결합니다.
4. **Verify** — 테스트와 지표로 결과를 확인합니다.
5. **Explain** — README·리포트·발표 자료로 왜 이렇게 만들었는지 남깁니다.

---

## 💼 Experience

### 물류 · 운영 · 재고 · 납기 관리 — 8년 9개월

- 입고·출고·재고·납기·구매·거래처 커뮤니케이션
- 제한된 인력 환경에서 업무 우선순위와 병목 관리
- 팀장 대행 및 소규모 인력 운영 경험
- 현장에서 익힌 검수 기준과 예외 대응을 개발 문제 정의에 활용

### KDT AI Human 4기 — 2026.03 ~ 2026.07 **수료**

AI 모델 자체보다 **AI 기능이 실제 사용자 흐름 안에서 동작하도록 연결하고 검증하는 과정**에 집중했습니다.

---

<div align="center">

**GitHub** · [github.com/mosejong](https://github.com/mosejong)  
**Resume** · [Web](https://mosejong.github.io/mosejong/resume.html) · [PDF](./assets/모세종.pdf)

</div>
