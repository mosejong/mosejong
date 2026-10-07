# 모세종 | AI 서비스 개발자

**Python · FastAPI**

Python·FastAPI로 AI 기능과 데이터를 사용자 서비스에 연결하는 신입 AI 서비스 개발자입니다.  
개인 프로젝트 FinShield AI에서 규칙 판정·LLM 설명·공식 근거를 분리하고, PWA부터 GCP 공개 데모 배포까지 구현했습니다.  
팀 프로젝트에서는 AI 진로 리포트·추천 근거와 8개 언어 번역·TTS 파이프라인을 담당했습니다.  
물류·운영 **8년 9개월**의 현장 경험을 바탕으로 요구사항과 예외 조건을 정리하고, 테스트·근거·실패 케이스로 결과를 검증합니다.

- 개발 경력: **신입**
- 이스트캠프 KDT AI Human 4기 **우수수료생**
- Jobiverse — KDT 최종 프로젝트 **대상**
- SchoolBridge — KDT 1차 프로젝트 **최우수상**

## Profile

현장과 사용자의 문제를 기능 요구사항 · 데이터 흐름 · 예외 조건으로 정리합니다.  
AI 기능을 API · DB · 사용자 흐름에 연결하고, 생성 실패와 데이터 정합성 문제를 다루며 실제 동작하는 서비스로 구현합니다.  
개인 기여와 팀 성과, 내부 평가와 실사용 성능을 구분해 기록합니다.

## Core Stack

- **AI / LLM / Retrieval**: OpenAI API, Gemini API, Vector Search, Transformers, NLLB, Edge-TTS, 내부 LLM 평가
- **Backend / API**: Python, FastAPI, REST API, Pydantic, SQLAlchemy
- **Data / Database**: PostgreSQL, pgvector, Redis, MongoDB, SQLite, Pandas, Scikit-learn
- **Infra / Validation**: Docker, Docker Compose, Nginx, Caddy, NCP, GCP, GitHub Actions, pytest, E2E
- **Frontend / Product**: Next.js, React, PWA, Streamlit

## Projects

### 나의 진로 아카데미아(Jobiverse) — AI 진로 탐색·직무 체험 리포트

**Reporting · Data Pipeline** · 2026.07.06 - 07.31 · 6인 팀 · KDT Final Project  
[GitHub](https://github.com/neunglog-sys/job_simulator) · [Case Study](https://mosejong.github.io/projects/jobiverse.html)

**개인 기여**

- 상담·미션 데이터를 역량 점수 → AI 해석 → 추천 근거·각주 → PDF 리포트로 연결하는 흐름 설계·구현
- 개인화 추천 근거 및 커리어넷 심리검사 API 연동, 데이터 정합성·CI 검증 담당

**프로젝트 검증·성과**

- 내부 검색 평가에서 top-1 직무 오염률 **12.5% → 0%**, 추천 적중 시 정답 근거 포함률 **95% → 100%**
- 임베딩 응답 p90 약 **1.3초 → 0.4초**
- backend **pytest 564개**는 팀 전체 결과
- KDT AI Human 4기 최종 프로젝트 **대상**

### FinShield AI — 근거 기반 금융사기 예방·행동 안내 서비스

**개인 기획 · 개발 · 배포** · 2026.08 - 09  
[GitHub](https://github.com/mosejong/finshield-ai) · [평가 기록](https://github.com/mosejong/finshield-ai/blob/main/docs/32-fraud-evaluation-benchmark.md) · [종료 문서 PR](https://github.com/mosejong/finshield-ai/pull/147)

**문제 해결·구현**

- 규칙 엔진이 위험도·유형·행동을 확정하고 LLM은 설명만 생성하도록 분리; 생성 실패 시에도 판정·행동 안내 유지
- 금융위원회 공공데이터의 출처·기준월을 연결하고, 생성된 기관명·법률·숫자·확정적 표현을 검증
- PWA·API·DB 흐름 통합, 암호화 프로필의 백업·복원 검증
- GCP · Docker Compose · HTTPS로 공개 데모 배포·운영

**검증·배포 이력**

- 합성 한국어 문자 **865건** 누적 회귀 평가 **F1 0.9830**
- 규칙 개선에 재사용한 내부 데이터의 재측정 결과이며, 독립 평가·실사용자 성능과 구분
- 종료 문서 PR #147의 기록 기준 **pytest 1,292 passed · 2 skipped**, GitHub CI 검사 **8개 통과**
- **2026 금융 AI Challenge 출품**; 공개 데모는 **2026.09.22 종료**

### SchoolBridge — 다문화가정 가정통신문 AI 안내 서비스

**Translation · TTS Pipeline** · 2026.04.24 - 05.13 · 5인 팀  
[GitHub](https://github.com/Maxmunzy/multicultural-ai) · [번역 평가 기록](https://github.com/Maxmunzy/multicultural-ai/blob/main/docs/experiments/2026-04-28-translation-glossary-quality.md)

**개인 기여**

- 베트남어 번역·학교 용어사전·반복 오역 검토를 담당하고 NLLB **8개 언어**·Edge-TTS 파이프라인으로 확장
- 용어사전과 슬롯·마스킹으로 날짜·금액·연락처 등 핵심정보 보존
- 번역 결과와 음성 파일이 서비스에서 전달되도록 팀과 연동

**프로젝트 검증·성과**

- 가정통신문 **19개**·학교 용어 **144개** 기반 Gemini 루브릭 내부 번역 평가 **39.0 → 89.6**; 원어민·외부 품질 평가와 구분
- backend **pytest 27개** 및 Android 실기기 E2E 검증은 팀 전체 결과
- KDT 1차 프로젝트 **최우수상**

### 공공조달 수요 기반 창업 입지·물류 거점 분석

**개인 기획 · Data Pipeline · AI 리포트** · 2026.05.13 - 07.21  
[GitHub](https://github.com/mosejong/procurement-logistics-ai) · [공개 데모](https://procurement-logistics-ai-5qian47widxpcuqefpjipy.streamlit.app)

**문제 해결·구현**

- 물류 현장의 수요·납품·거점 판단 문제를 정의하고 **6개 기관·9개 공공데이터 소스**를 수집·정제
- TF-IDF · Logistic Regression 품목 분류와 지역·품목별 수요·경쟁도·거점 지표 설계
- 분석 수치를 Gemini 근거형 리포트와 Streamlit 지도·지역 비교 대시보드에 연결

**데이터·성과**

- 나라장터 입찰 **100,083건**·계약 **38,367건**, 학교급식 BID/AWARD **734,242건** 분석
- 2026 공공조달데이터·AI 활용 창업경진대회 **대면심사 진출**

### Rainbow Bridge — AI 기반 펫로스 애프터케어 서비스

**Team Lead · API 및 서비스 통합** · 2026.06.02 - 06.19 · 6인 팀  
[GitHub](https://github.com/mosejong/Rainbow-Bridge) · [개인 기여·팀 평가 기록](https://github.com/mosejong/Rainbow-Bridge/blob/dev/CONTRIBUTION.md)

**개인 기여**

- 팀 리드로 일정·역할을 조율하고 핵심 사용자 흐름 중심으로 MVP 범위 정리
- 감정 체크인 → AI 메시지 → TTS·영상 → 미션 → 리포트의 API·데이터 흐름 통합
- recovery_score 기반 콘텐츠 해금 규칙, 데모 계정·데이터 구성, NCP 배포·실서버 연동 담당

**프로젝트 검증·성과**

- Android 실서버 E2E 시연 완료; 공개 서버는 발표 후 종료
- 팀 안전성 평가 골든셋 **40/40**, 팀 G-Eval **4.76–4.83/5**
- 위 평가는 팀 전체 결과이며 개인 구현 범위와 구분

## How I Work

**Problem → Design → Build → Verify**

현장·사용자 문제를 요구사항과 예외 조건으로 정리하고, 데이터와 AI 기능을 서비스 흐름으로 연결합니다.  
테스트 · 내부 평가 · 근거 · 실패 케이스로 개선 전후를 확인합니다.

## Career

아래는 개발 직무 이전의 사회 경험입니다. 군 복무·공백 기간을 제외한 건강보험 기준 산업 경력은 총 **8년 9개월**이며, 개발 경력은 신입입니다.

### (주)정우금속이엔지

**물류팀 · 대리** · 2021.02.22 - 2026.01.30

- 입출고 · 재고 · 납기 · 구매 · 사무/전산 운영 및 거래처 대응
- 월 재고손실률 **10% 이상** 문제를 보고하고 재고 추적·관리 체계를 개선해 **5% 미만 안정화**에 기여
- 팀장 공석 기간 업무 순서·인력 배치를 조율하고 재고·매입 보고 수행

### (주)미래부품

**구매팀 · 대리** · 2017.06.05 - 2020.01.02

- 매입 · 발주 · 재고 · 지역별 납품 및 거래처 주문에 따른 납기 일정 관리
- 팀장 공석 기간 운영 업무 대행, 재고·매입 보고서와 데이터 관리

---

GitHub: [mosejong](https://github.com/mosejong) · Portfolio: [mosejong.github.io](https://mosejong.github.io/)
