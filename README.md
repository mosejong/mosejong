<div align="center">

# 모세종 | Python · FastAPI 기반 AI 서비스 개발자

### 현장에서 발견한 문제를 데이터와 AI가 동작하는 서비스로 바꿉니다.

물류·운영 현장에서 **8년 9개월** 동안 재고·납기·구매·출고 흐름을 경험했습니다.  
이제는 그 문제 정의 경험을 바탕으로 **Python / FastAPI / AI 기능을 실제 서비스 흐름에 연결**하고 있습니다.

**KDT AI Human 4기 우수수료생 · 최종 프로젝트 대상**

[![Resume](https://img.shields.io/badge/WEB_RESUME-2563EB?style=for-the-badge&logo=readme&logoColor=white)](https://mosejong.github.io/mosejong/resume.html)
[![PDF](https://img.shields.io/badge/PDF_RESUME-E11D48?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](./assets/모세종_이력서.pdf)
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

저는 AI 모델 자체보다 **그 기능이 사용자에게 도달하기까지의 흐름**에 관심이 있습니다.

- 현장·사용자 문제를 **기능 요구사항과 데이터 흐름**으로 정리합니다.
- AI 기능을 **API · DB · UI · 배포 흐름**에 연결합니다.
- 결과를 **테스트 · 지표 · 근거 · 실패 케이스**로 검증합니다.
- 현장에서 익힌 우선순위·병목·검수 감각을 소프트웨어 설계에 가져옵니다.

> **물류·운영 8년 9개월 → KDT AI Human 4기 우수수료생 → Python/FastAPI 기반 AI 서비스 개발**

---

## 🏅 Highlights

- **KDT AI Human 4기 우수수료생**
- **나의 진로 아카데미아 — KDT 최종 프로젝트 대상**
- **SchoolBridge — KDT 팀 프로젝트 최우수상**
- **2026 공공조달데이터·AI 활용 창업경진대회 — 대면심사 진출**

---

## 🚀 Representative Projects

| Project | My Role | What I Owned | Evidence |
|---|---|---|---|
| **[SchoolBridge](https://github.com/Maxmunzy/multicultural-ai)** | **Translation · TTS Pipeline** | NLLB 번역, 학교 용어사전, 핵심정보 보존, TTS, 품질 검증 | **39.0 → 89.6**, 8개 언어, 27 tests, Android E2E, **최우수상** |
| **[공공조달 수요 기반 입지·물류 거점 분석](https://github.com/mosejong/procurement-logistics-ai)** | **Solo Product · Data Pipeline** | 공공데이터 수집·분류·지표·AI 해석·대시보드 | 6개 기관·9개 데이터소스, 전국 분석, **공모전 대면심사 진출** |
| **[나의 진로 아카데미아](https://github.com/neunglog-sys/job_simulator)** | **Reporting · Data Pipeline** | 적합도 리포트, 추천 근거 개인화, 커리어넷 연동, CI | 직무군 38개 · 세부직업 204개 · 시나리오 37종 · 프로젝트 전체 564 tests · **대상** |
| **[Rainbow Bridge](https://github.com/mosejong/Rainbow-Bridge)** | **Team Lead · Backend Integration** | 팀 운영, 서비스 흐름, API 통합, 서버·배포·모바일 시연 | FastAPI · NCP · Docker · nginx · Expo 통합 |

---

## 1️⃣ SchoolBridge — Translation · TTS Pipeline

### 다문화 가정 학부모를 위한 가정통신문 AI 번역 · TTS 서비스

**Role Scope**  
번역·TTS 파이프라인을 맡아 **모델 선택 → 용어사전 → 정보 보존 → 음성 출력 → 품질 검증** 흐름을 설계했습니다.

### Problem I Focused On

가정통신문에서는 문장이 자연스러운 것만큼 **날짜·시간·비용·준비물·제출 여부 같은 행동 정보가 틀리지 않는 것**이 중요하다고 판단했습니다.

### What I Designed & Built

- `facebook/nllb-200-distilled-600M` 기반 **8개 언어 번역 파이프라인**
- 학교 현장 표현을 위한 **도메인 용어사전(Glossary)**
- 날짜·금액·전화번호·URL 등 **핵심 정보 보존 후처리**
- Edge-TTS 언어별 보이스 매핑 및 음성 출력
- 번역 품질 검수 루프와 Round-trip 평가
- FastAPI 통합 파이프라인 및 Android 실기기 E2E 검증 참여

### Evidence

- 용어사전 적용 전후 품질 평가: **39.0 → 89.6**
- **8개 언어** 번역 지원
- backend **pytest 27개** + GitHub Actions PR gate
- Android 실기기 기반 E2E 파이프라인 검증
- **KDT 팀 프로젝트 최우수상**

`Python` · `FastAPI` · `Transformers` · `NLLB` · `Pandas` · `Glossary` · `Edge-TTS` · `Docker` · `Android`

🔗 **[Repository](https://github.com/Maxmunzy/multicultural-ai)**

---

## 2️⃣ 공공조달 수요 기반 입지 · 물류 거점 분석 — Solo Product · Data Pipeline

### 8년 9개월의 물류 경험을 소프트웨어 제품으로 연결한 개인 프로젝트

**Role Scope**  
개인 프로젝트로 문제 정의부터 **데이터 수집·정제·분류·지표 설계·AI 해석·대시보드 구현**까지 전 과정을 진행했습니다.

### Why I Built It

물류 현장에서 경험한 수요·납품·재고·거점 판단을 경험으로만 남기지 않고, **공공데이터 근거로 비교할 수 있는 제품**으로 만들고 싶었습니다.

### What I Designed & Built

- 조달청·aT·행정안전부·소상공인시장진흥공단·국토교통부·KOSIS 등 **6개 기관 / 9개 데이터소스 결합**
- 나라장터 입찰공고 **100,083건**, 계약정보 **38,367건** 수집·분석
- aT 학교급식 입찰·낙찰 **734,242건**으로 수요 근거 보강
- TF-IDF + Logistic Regression 기반 공고 분류
- 지역·품목별 `opportunity_score`, 인구 보정, 경쟁도, 물류 거점 지표 설계
- Gemini API 기반 **AI 해석 5종**
- Streamlit 기반 전국 지도·지역 비교·물류 거점 분석 대시보드

### External Validation

**2026 공공조달데이터·AI 활용 창업경진대회 출품 → 대면심사 진출**

`Python` · `Pandas` · `Scikit-learn` · `Public Data API` · `Gemini API` · `Streamlit`

🔗 **[Repository](https://github.com/mosejong/procurement-logistics-ai)** · **[Live Demo](https://procurement-logistics-ai-5qian47widxpcuqefpjipy.streamlit.app)**

---

## 3️⃣ 나의 진로 아카데미아 — Reporting · Data Pipeline

### AI 상담 → 가상 직무 체험 → 근거 기반 적합도 리포트로 이어지는 진로 탐색 플랫폼

**Role Scope**  
6인 팀에서 **Reporting · Data Pipeline**을 맡았습니다. 프로젝트 전체 기능을 제 역할처럼 넓혀 쓰지 않고, 제가 담당한 리포트·추천 근거·외부 데이터 연동·CI 범위를 중심으로 정리합니다.

### What I Designed & Built

- 직무 적합도 **리포트 구조 설계**
  - 역량 레이더
  - AI 해석
  - 평가 근거 각주
  - PDF 출력
- 상담·체험 기록을 활용한 **추천 근거 개인화**
- **커리어넷 진로심리검사 연동**
- **CI 파이프라인** 구성

### Project Context

프로젝트 전체 기준으로:

`직무군 38개` · `세부직업 204개` · `체험 시나리오 37종` · `pytest 564 cases`

> 위 규모와 테스트 수치는 **팀 전체 프로젝트 기준**이며, 제 개인 기여량으로 표시하지 않습니다.

### Result

**KDT 최종 프로젝트 대상 — 1팀**

### Project Stack

`React 19` · `TypeScript` · `FastAPI` · `PostgreSQL + pgvector` · `Redis` · `OpenAI` · `Gemini` · `MuseTalk` · `Docker Compose` · `Nginx`

🔗 **[Repository](https://github.com/neunglog-sys/job_simulator)**

---

## 4️⃣ Rainbow Bridge — Team Lead · Backend Integration

### AI 펫로스 애프터케어 서비스 · 6인 팀 프로젝트

**Role Scope**  
특정 AI 모델 하나를 깊게 구현하는 역할보다는 **팀과 여러 기능이 하나의 사용자 흐름으로 연결되도록 조율하고 통합하는 역할**을 맡았습니다.

### What I Owned

- Team Lead / PM
- 역할 분담·일정·기능 우선순위 조율
- 서비스 흐름 및 백엔드 API 통합 참여
- NCP 서버 운영
- Docker 기반 배포 환경 구성
- nginx / HTTPS 운영
- Expo 기반 iOS·Android 모바일 시연 흐름 확인
- 외부 AI·멀티미디어 기능 연결 과정 조율
- 평가·발표·제출 산출물 정리

### What This Project Shows

**모델 → API → 서버 → 모바일 → 시연**으로 이어지는 서비스 통합 경험과, 6인 팀의 개발 흐름을 운영한 경험을 보여주는 프로젝트입니다.

`FastAPI` · `MongoDB` · `SQLite` · `Redis` · `Gemini API` · `TTS` · `LivePortrait` · `FFmpeg` · `Docker` · `NCP` · `nginx` · `Expo`

🔗 **[Repository](https://github.com/mosejong/Rainbow-Bridge)**

---

## 🧪 R&D / Side Project

### [Context Capsule](https://github.com/mosejong/context-capsule) — AI Handoff Tool

AI에게 레포지토리 작업을 넘길 때 필요한 **관련 파일·작업 범위·금지 영역·완료 기준을 정리하는 도구**입니다.

대표 포트폴리오에서는 후순위로 두고 있으며, 개인적으로 `Retrieval · FastAPI · 테스트 · 릴리즈 자동화`를 실험하고 개선하는 R&D 프로젝트로 유지하고 있습니다.

---

## 🛠 Tech Stack

| Area | Used in Projects |
|---|---|
| **Backend / API** | Python, FastAPI, REST API, Pydantic, SQLite, MongoDB, PostgreSQL, Redis |
| **AI / NLP** | OpenAI API, Gemini API, Transformers, NLLB, RAG, pgvector, TTS |
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

## 💼 Previous Experience

### 물류 · 운영 · 재고 · 납기 관리 — 8년 9개월

- 입고·출고·재고·납기·구매·거래처 커뮤니케이션
- 제한된 인력 환경에서 업무 우선순위와 병목 관리
- 팀장 대행 및 소규모 인력 운영 경험
- 현장에서 익힌 검수·예외 대응 감각을 현재의 서비스 설계와 데이터 검증 방식에 연결

---

<div align="center">

**현장을 이해하고, 근거를 만들고, 동작하는 서비스까지 연결하는 개발자를 지향합니다.**

</div>