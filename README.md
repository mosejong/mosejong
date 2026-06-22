# 모세종 | AI Service Pipeline Developer

> 물류 현장에서 배운 흐름·병목·검수 감각을 바탕으로, AI API를 단순 연결하는 것보다 **사용자 행동까지 이어지는 AI 서비스 파이프라인**을 설계하고 구현하는 개발자를 지향합니다.

저는 입력 데이터가 어떻게 정제되고, 모델 출력이 서비스 안에서 어떻게 검증되며, 어디서 정보 손실이 생기는지 관찰하고 개선하는 데 관심이 있습니다.

---

## Focus

- AI 서비스 파이프라인 설계 및 구현
- LLM/RAG 기반 응답 흐름 설계
- 모델 출력 실패 가능성 분석 및 안전 라우팅
- Slot Protection, Glossary, Template, 검수 루프를 통한 품질 통제
- FastAPI 기반 백엔드 API 설계
- 사용자가 실제로 이해하고 행동할 수 있는 서비스 흐름 구현

---

## Main Projects

### 1. [Rainbow Bridge](https://github.com/mosejong/Rainbow-Bridge)

펫로스 보호자를 위한 AI 애도·회복 케어 서비스입니다. 팀장으로 프로젝트 흐름을 정리하고, 백엔드 API·AI 연동·안전 라우팅·배포 흐름을 중심으로 구현했습니다.

**Key Points**

- FastAPI 기반 API 설계
- MongoDB/SQLite 기반 데이터 관리
- Gemini 기반 위로 메시지 생성
- 감정 체크인, 미션, 타임라인, 회복 리포트 흐름
- 위기 표현 감지 및 1393 안내 안전 라우팅
- TTS·LivePortrait/GIF 기반 멀티모달 출력 흐름

**What I Focused On**

- 단순 챗봇이 아니라 사용자의 회복 단계와 행동으로 이어지는 서비스 흐름 설계
- 민감한 감정 데이터를 다루는 서비스에서 안전 장치와 차단 기준 정리
- 팀장으로 기능 범위, 발표 구조, 제출 산출물, 배포 흐름 관리

---

### 2. [SchoolBridge](https://github.com/Maxmunzy/multicultural-ai)

다문화 가정 학부모를 위한 학교 가정통신문 AI 번역·요약·TTS 서비스입니다. 학교 안내문에서 핵심 할 일을 추출하고, 번역과 음성 안내까지 연결하는 팀 프로젝트입니다.

**Service Flow**

```text
Korean school notice
→ 할 일 문장 추출
→ 카테고리 분류
→ 다국어 번역
→ TTS
→ 학부모용 체크리스트 / 캘린더 / 안내 화면
```

**My Role**

- 번역/TTS 파이프라인 설계 및 구현
- 학교 도메인 용어사전 구축
- 날짜·금액·URL·전화번호 등 핵심 정보 보존 후처리
- NLLB 기반 다국어 번역 실험
- Edge-TTS 기반 음성 출력 실험
- README, 발표 흐름, 기술 설명 정리

**What I Focused On**

- 생성형 AI API를 메인 번역기로 바로 쓰기보다 NLLB 기반 번역 파이프라인에 Slot Protection, Glossary, Template Translation, 검수 루프를 결합
- 날짜, 금액, URL, 전화번호, 준비물, 제출기한처럼 틀리면 안 되는 정보 보호
- 번역 품질 문제를 모델 성능, 도메인 용어, 입력 문장 구조, 후처리 문제로 나누어 개선

---

### 3. [procurement-logistics-ai](https://github.com/mosejong/procurement-logistics-ai)

공공조달 데이터를 활용해 지역·품목별 수요 흐름과 창업 기회를 분석하는 데이터 기반 프로젝트입니다.

**Key Points**

- 공공조달 API 데이터 수집 및 전처리
- 공고 데이터와 계약/낙찰 데이터를 구분한 분석 구조
- 지역/품목별 수요 흐름 분석
- 추천 / 제외 / 데이터 부족 기준 설계
- Streamlit 기반 분석 대시보드 구현
- 물류 경험을 공공데이터 분석 관점으로 확장

**What I Focused On**

- 공공데이터를 단순 조회가 아닌 의사결정 보조 흐름으로 구조화
- 수치 기반 분석 결과가 과장되지 않도록 해석 기준 설계
- 데이터 부족, 표본 부족, 지역 편차를 사용자에게 명확히 전달하는 방식 고민

---

## Tech Stack

### Language & Data

`Python` · `SQL` · `NumPy` · `Pandas`

### AI / ML / NLP

`Scikit-learn` · `PyTorch` · `Transformers` · `NLLB` · `Prompt Engineering` · `RAG`

### Backend & Service

`FastAPI` · `Streamlit` · `REST API` · `Docker`

### Tools

`Git` · `GitHub` · `VS Code` · `NCP`

---

## Direction

저는 모델 하나의 성능보다, 입력 데이터와 모델 출력이 서비스 안에서 어떻게 연결되고 검증되는지에 관심이 있습니다.

앞으로는 LLM, RAG, 데이터 기반 AI 서비스를 중심으로 문서와 데이터를 구조화하고, AI가 근거 있게 답변하도록 돕는 서비스 파이프라인을 만들어가고자 합니다.

---

> 호기심을 실험으로 바꾸고, 실험을 기록으로 남기며, 흐름의 병목과 오류를 개선하는 개발자를 지향합니다.
