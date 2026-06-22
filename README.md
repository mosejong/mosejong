# 모세종 | AI Service Pipeline Developer

> 물류 현장에서 익힌 흐름·병목·검수 감각을 바탕으로, **AI 모델의 출력이 실제 사용자 행동까지 이어지는 서비스 파이프라인**을 설계하고 구현하는 개발자를 지향합니다.

저는 AI API를 단순히 연결하는 것보다, 입력 데이터가 어떻게 정제되고 모델 출력이 어떤 기준으로 검증되며 사용자가 어떤 화면과 행동으로 이어지는지까지 보는 데 관심이 있습니다.  
특히 LLM/RAG, 번역·TTS, 안전 라우팅, 품질 검수 루프처럼 **모델 성능과 서비스 신뢰성 사이를 연결하는 구조**를 만들고 있습니다.

---

## What I Build

- 문서·데이터 입력을 구조화하고 AI가 처리하기 좋은 형태로 정제합니다.
- LLM/RAG 기반 응답 흐름을 설계하되, 모델 출력을 그대로 믿지 않고 검증 기준을 둡니다.
- 날짜·금액·URL·전화번호처럼 틀리면 안 되는 정보는 Slot Protection, Glossary, Template, 후처리로 보호합니다.
- 감정·위기·민감 정보가 포함된 서비스에서는 생성 전 안전 라우팅과 차단 기준을 우선 설계합니다.
- 사용자가 결과를 이해하고 행동할 수 있도록 API, 화면 흐름, 문서, 테스트 결과를 함께 정리합니다.

---

## Main Projects

### 1. [Rainbow Bridge](https://github.com/mosejong/Rainbow-Bridge)

반려동물의 시한부 선고부터 이별, 장례, 회복까지 이어지는 **AI 펫로스 케어 서비스**입니다.  
팀장으로 프로젝트 범위와 발표 흐름을 정리했고, 백엔드 API·AI 연동·위기 감지 안전 라우팅·배포 흐름을 중심으로 구현했습니다.

<img src="./assets/rainbow-bridge-demo.gif" width="720" alt="Rainbow Bridge demo" />

**Role**

- Team Lead / PM
- Backend API 설계 및 기능 통합
- Gemini 기반 메시지 생성 흐름 연동
- 감정 체크인 기반 L0~L3 위기 감지 및 1393 안내 라우팅 정리
- TTS, LivePortrait/GIF, 회복 리포트 등 멀티모달 출력 흐름 통합
- 발표 구조, 제출 산출물, README/문서 정리

**Result**

- 3주 프로토타입 기간 내 핵심 기능 8개 완성
- 감정 체크인, 기억 기반 추모 메시지, TTS, 미션, 타임라인, 회복 리포트 구현
- L2 이상 위기 감지 시 콘텐츠 생성을 차단하고 1393 안내로 전환하는 안전 구조 적용
- 골든셋 40건 기준 위기 감지 40/40 통과
- G-Eval 대화 품질 4.76~4.83 / 5.0, 윤리 준수 4.61 / 5.0
- TTS CER 3인칭 편지 1.0%, 1인칭 편지 5.5%
- LivePortrait 기반 동물 아바타 립싱크 평가 지표 설계 및 상관계수 0.896 측정

**Tech**  
`FastAPI` · `MongoDB` · `SQLite` · `Redis` · `Gemini API` · `ChromaDB` · `TTS` · `LivePortrait` · `FFmpeg` · `Docker` · `NCP` · `GitHub Actions`

---

### 2. [SchoolBridge](https://github.com/Maxmunzy/multicultural-ai)

다문화 가정 학부모를 위한 **가정통신문 AI 번역·요약·TTS 서비스**입니다.  
학교 안내문에서 학부모가 해야 할 일을 추출하고, 쉬운 한국어와 다국어 번역, 음성 안내, 체크리스트 화면까지 연결하는 팀 프로젝트입니다.

**Role**

- 번역/TTS 파이프라인 설계 및 구현
- NLLB 기반 8개 언어 번역 실험
- 학교 도메인 용어사전 구축
- 날짜·금액·URL·전화번호 등 핵심 정보 보존 후처리
- Edge-TTS 기반 음성 출력 실험
- 번역 품질 검수 루프, 실험 문서, 발표 흐름 정리

**Result**

- 한국어 가정통신문 → 할 일 추출 → 카테고리 분류 → 다국어 번역 → TTS → 학부모 체크리스트 흐름 구현
- 베트남어, 영어, 러시아어, 말레이시아어, 몽골어, 중국어, 태국어, 일본어 번역 지원
- 용어사전 적용 전후 품질 평가: NLLB 39.0점 → 사전 적용 89.6점
- backend pytest 27개와 GitHub Actions 기반 PR 게이트 구성
- Android 실기기 기반 E2E 파이프라인 검증 완료

**Tech**  
`Python` · `FastAPI` · `Transformers` · `facebook/nllb-200-distilled-600M` · `Pandas` · `CSV` · `Edge-TTS` · `Docker` · `Android`

---

### 3. [procurement-logistics-ai](https://github.com/mosejong/procurement-logistics-ai)

공공조달 데이터를 활용해 지역·품목별 공공수요와 물류 거점 후보를 분석하는 **데이터 기반 창업·입지 분석 프로젝트**입니다.  
물류 현장에서 경험한 수요 흐름과 납품 구조 감각을 공공데이터 분석으로 확장했습니다.

**Role**

- 공공데이터 API 수집·정제 파이프라인 구성
- 입찰공고·계약·발주계획·MAS·학교급식·인구·상권·물류창고 데이터 결합
- 지역/품목별 수요 점수와 물류 거점 점수 설계
- 데이터 부족, 제외 업종, 과장 해석 방지 기준 정리
- Streamlit 기반 분석 대시보드 구현

**Result**

- 조달청, aT, 행정안전부, 소상공인시장진흥공단, 국토교통부, KOSIS 등 6개 기관 / 9개 데이터 소스 결합
- 전국 17개 시도, 220개 지역 단위 분석 구조 구현
- 입찰공고 100,083건, 계약정보 38,367건, 학교급식 입찰·낙찰 734,242건 활용
- TF-IDF + Logistic Regression 기반 품목 분류 정확도 98.6%
- Streamlit 10개 탭 기반 라이브 데모 구현
- Gemini 기반 AI 해석 5종: 수요 설명, 수요 공백, 경쟁 구조, 물류 거점, 지역 비교

**Tech**  
`Python` · `Pandas` · `Scikit-learn` · `Logistic Regression` · `Public Data API` · `Gemini API` · `Streamlit` · `CSV`

---

## Tech Stack

### Language & Data

`Python` · `SQL` · `NumPy` · `Pandas` · `CSV` · `Public Data API`

### AI / ML / NLP

`Scikit-learn` · `PyTorch` · `Transformers` · `NLLB` · `LLM` · `Prompt Engineering` · `RAG` · `ChromaDB`

### Backend & Service

`FastAPI` · `REST API` · `MongoDB` · `SQLite` · `Redis` · `Streamlit` · `Docker`

### Voice / Multimodal

`Edge-TTS` · `Google Cloud TTS` · `LivePortrait` · `FFmpeg`

### Tools & Infra

`Git` · `GitHub` · `GitHub Actions` · `VS Code` · `NCP` · `DuckDNS` · `Let's Encrypt`

---

## Working Principles

- AI 출력은 결과가 아니라 **검증해야 할 중간 산출물**로 봅니다.
- 기능 구현만큼 실패 케이스, 예외 처리, 품질 기준을 중요하게 봅니다.
- 사용자가 실제로 이해하고 행동할 수 있는 흐름까지 연결되어야 서비스라고 생각합니다.
- 현장 경험에서 배운 병목·검수·납기 감각을 데이터 파이프라인과 AI 서비스 품질 관리로 확장하고 있습니다.

---

> 호기심을 실험으로 바꾸고, 실험을 기록으로 남기며, 흐름의 병목과 오류를 개선하는 개발자를 지향합니다.
