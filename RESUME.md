# 모세종 Resume

> **AI Service Builder / Backend-oriented Junior Developer**  
> 운영 현장 경험을 바탕으로 사용자 문제, 비용 구조, 서비스 흐름을 함께 고려하는 AI 서비스 개발자를 지향합니다.

---

## Profile

물류·운영 현장에서 8년 9개월 동안 입고, 출고, 재고, 납기, 구매 업무와 거래처 커뮤니케이션을 경험했습니다.  
이 경험을 통해 서비스와 시스템은 기능만으로 완성되지 않고, 실제 사용자의 상황과 운영 흐름을 함께 고려해야 한다는 관점을 갖게 되었습니다.

현재는 AI 국비교육과정을 통해 Python, FastAPI, 데이터 처리, LLM API, TTS, 배포, 협업 기반 개발을 학습하고 있습니다.  
특히 AI 모델을 단순히 연결하는 것보다, 사용자가 이해하고 행동할 수 있는 서비스 흐름으로 설계하는 데 관심이 있습니다.

저는 다음과 같은 방향을 지향합니다.

- 사용자 문제와 서비스 제약을 먼저 이해하는 개발자
- AI 출력의 오류 가능성을 인정하고, 글로사리·템플릿·후처리·검증 기준으로 보정하는 개발자
- 팀 프로젝트에서 역할, 일정, 인터페이스, 완료 기준을 정리할 수 있는 개발자
- AI가 모든 결정을 대신하기보다 사람이 검토하고 승인할 수 있는 Human-in-the-loop 구조를 선호하는 개발자

---

## Core Strengths

- **현장 기반 문제 정의**: 물류·운영 경험을 바탕으로 실제 사용자와 운영 제약을 함께 고려합니다.
- **AI 서비스 흐름 설계**: LLM, 번역, TTS, 안전 라우팅을 단일 기능이 아닌 사용자 흐름으로 연결합니다.
- **백엔드/API 구현 경험**: FastAPI 기반 API, SQLite/MongoDB, JWT, Docker 배포 흐름을 경험했습니다.
- **품질 보정 관점**: AI 출력의 오류를 줄이기 위해 글로사리, 템플릿, 후처리, 테스트 기준을 함께 설계합니다.
- **팀 리딩/협업 경험**: 6인 팀 프로젝트에서 팀장/PM으로 역할 분담, 일정 관리, 발표/문서화를 담당했습니다.

---

## Technical Skills

### Backend / API

`Python` · `FastAPI` · `REST API` · `SQLite` · `MongoDB` · `JWT` · `Redis`

### AI / NLP / Voice

`LLM API` · `Prompt Engineering` · `Transformers` · `NLLB` · `Glossary` · `TTS` · `Edge-TTS` · `Google TTS`

### Data / Evaluation

`Pandas` · `CSV` · `Scikit-learn` · `Public Data API` · `Evaluation Report` · `Test Case Design`

### Infra / Collaboration

`Docker` · `NCP Server` · `nginx` · `HTTPS` · `GitHub Actions` · `Git` · `GitHub PR/Issue`

### Frontend / Tools

`React` · `Vite` · `Tailwind CSS` · `Streamlit` · `Android 실기기 테스트`

---

## Projects

## 1. SchoolBridge

**다문화 가정통신문 AI 도우미**  
Repository: [github.com/Maxmunzy/multicultural-ai](https://github.com/Maxmunzy/multicultural-ai)

### Summary

다문화가정 학부모가 한국어 가정통신문에서 날짜, 준비물, 비용, 제출 여부 같은 핵심 정보를 놓치지 않도록 돕는 AI 번역·요약·TTS 서비스입니다.

### My Role

- 번역/TTS 파이프라인 설계 및 구현
- NLLB 기반 8개 언어 번역 실험
- 학교 도메인 용어 글로사리 구축
- 날짜·금액·URL·전화번호 등 핵심 정보 보존 후처리
- Edge-TTS 기반 음성 출력 실험
- 번역 품질 검수 루프, 실험 문서, 발표 흐름 정리

### Design Intention

이 프로젝트에서 가장 중요하게 본 것은 “다문화가정 학부모에게 실제로 도움이 되는 구조인가”였습니다.  
가정통신문은 문장 전체를 자연스럽게 번역하는 것보다, 학부모가 해야 할 일을 정확히 이해하는 것이 더 중요하다고 판단했습니다.

또한 서비스 대상이 다국적 사용자이며 유료 과금이 어려운 구조라고 보았습니다.  
그래서 외부 유료 API 의존도를 낮추고, 무료 또는 로컬 기반 번역 모델을 활용하는 방향을 검토했습니다.

다만 일반 번역 모델은 학교 행정 용어를 오역할 수 있다고 판단했습니다.  
예를 들어 “스쿨뱅킹”, “현장체험학습”, “방과후학교”, “제출서류” 같은 표현은 일반 번역으로는 의미가 흔들릴 수 있습니다.

이를 줄이기 위해 **글로사리 + 템플릿 기반 보정 구조**를 설계했습니다.  
모델이 번역을 담당하되, 학교 도메인에서 반드시 보호해야 하는 표현은 별도 사전과 후처리 구조로 보정하는 방식입니다.

프로젝트 이후 사용 모델의 라이선스 검토 필요성을 인지했습니다.  
실제 서비스 적용 시에는 라이선스 문제가 없는 모델로 교체해야 한다고 판단하고 있습니다.  
다만 모델이 바뀌더라도 글로사리와 템플릿 기반 보정 구조는 유지 가능하므로, 번역 품질 개선과 운영 비용 절감 측면에서 확장 가능한 설계라고 보고 있습니다.

### Result

- 한국어 가정통신문 → 할 일 추출 → 카테고리 분류 → 다국어 번역 → TTS → 체크리스트 흐름 구현
- 베트남어, 영어, 러시아어, 말레이시아어, 몽골어, 중국어, 태국어, 일본어 번역 지원
- 용어사전 적용 전후 품질 평가: NLLB 39.0점 → 사전 적용 89.6점
- backend pytest 27개와 GitHub Actions 기반 PR 게이트 구성
- Android 실기기 기반 E2E 파이프라인 검증

### Tech

`Python` · `FastAPI` · `Transformers` · `facebook/nllb-200-distilled-600M` · `Pandas` · `CSV` · `Edge-TTS` · `Docker` · `Android`

---

## 2. Rainbow Bridge

**펫로스 애프터케어 AI 서비스**  
Repository: [github.com/mosejong/Rainbow-Bridge](https://github.com/mosejong/Rainbow-Bridge)

### Summary

펫로스를 겪는 보호자를 대상으로 감정 체크인, 미션, 추모 메시지, TTS/영상 생성 흐름을 제공하는 AI 애프터케어 서비스입니다.

### My Role

- Team Lead / PM
- 서비스 흐름 설계 및 발표 구조 정리
- 역할 분담, 일정 관리, 기능 우선순위 조율
- 백엔드 API 및 기능 통합 참여
- NCP 서버 운영
- Docker 기반 배포 환경 구성
- nginx / HTTPS 운영 경험
- GPU 터널링 및 외부 AI 기능 연동 경험
- 안전 라우팅, 평가 리포트, 제출 산출물 정리

### Contribution

Rainbow Bridge는 제가 모든 기술 파트를 깊게 구현한 프로젝트라기보다, 팀장/PM으로서 여러 파트가 하나의 사용자 흐름으로 연결되도록 조율한 프로젝트입니다.

AI 서비스는 모델 하나만 잘 붙인다고 완성되지 않았습니다.  
감정 체크인, 미션, 추모 메시지, TTS, 영상 생성, 안전 라우팅, 사용자 화면, 서버 운영이 서로 맞물려야 실제로 시연 가능한 서비스가 되었습니다.

이 프로젝트를 통해 기능 구현뿐 아니라 협업 구조, 우선순위 조정, 배포 환경, 실서버 운영, 문서화의 중요성을 경험했습니다.

### Result

- 3주 프로토타입 기간 내 핵심 사용자 흐름 구현
- 감정 체크인, 기억 기반 추모 메시지, TTS, 미션, 타임라인, 회복 리포트 구현
- L2 이상 위기 감지 시 콘텐츠 생성을 차단하고 1393 안내로 전환하는 안전 구조 적용
- NCP 기반 실서버 배포 및 Android 시연 경험
- README, 평가 리포트, 호출 로그, 팀 회고 등 제출 산출물 정리

### Tech

`FastAPI` · `MongoDB` · `SQLite` · `Redis` · `Gemini API` · `TTS` · `LivePortrait` · `FFmpeg` · `Docker` · `NCP` · `nginx` · `GitHub Actions`

---

## 3. Context Capsule

**AI 작업 인수인계 도구**  
Repository: [github.com/mosejong/context-capsule](https://github.com/mosejong/context-capsule)

### Summary

팀 프로젝트와 AI 협업 과정에서 직접 느낀 문제를 바탕으로 만든 개인 프로젝트입니다.  
레포지토리와 작업 요청을 분석해 AI나 팀원에게 넘길 수 있는 작업 브리프를 생성하는 도구입니다.

### Why I Built This

AI에게 작업을 맡길 때 가장 큰 문제는 모델 성능만이 아니었습니다.  
필요한 컨텍스트를 얼마나 정확하고 적게 전달하느냐가 결과 품질에 큰 영향을 준다고 느꼈습니다.

전체 레포지토리를 무작정 읽히면 토큰이 낭비되고, 반대로 필요한 파일을 놓치면 AI가 잘못된 방향으로 작업할 수 있습니다.  
또한 팀원에게 작업을 넘길 때 배경, 금지사항, 완료 기준이 빠지면 작업 품질이 흔들릴 수 있습니다.

Context Capsule은 이 문제를 줄이기 위해 만든 도구입니다.

### Core Features

- 레포지토리 구조 분석
- 작업 요청 기반 관련 파일 추천
- AI 작업용 인수인계 프롬프트 생성
- 팀원 작업 가이드 생성
- 주니어 개발자용 설명 생성
- 작업 리스크 분석
- GitHub Issue Packet 생성
- 토큰 사용량 절감 추정
- Streamlit 대시보드 / CLI / Windows 실행 지원

### Direction

Context Capsule은 AI가 마음대로 코드를 수정하게 만드는 도구가 아닙니다.  
제가 중요하게 보는 방향은 **AI가 제안하고, 사람이 검토하고, 승인하는 구조**입니다.

즉, AI 작업을 완전 자동화하기보다 사람이 통제 가능한 형태로 AI에게 일을 넘겨주는 도구를 목표로 하고 있습니다.

### Tech

`Python` · `Streamlit` · `CLI` · `GitHub Issue Workflow` · `RAG-like Retrieval` · `Token Budgeting` · `Windows Launcher`

---

## Additional Project

## procurement-logistics-ai

**공공조달 기반 창업·입지 분석 프로젝트**  
Repository: [github.com/mosejong/procurement-logistics-ai](https://github.com/mosejong/procurement-logistics-ai)

물류 현장에서 경험한 수요 흐름과 납품 구조 감각을 공공데이터 분석으로 확장한 프로젝트입니다.  
공공조달, 학교급식, 인구, 상권, 물류창고 데이터를 결합해 지역·품목별 공공수요와 물류 거점 후보를 분석했습니다.

- 공공데이터 API 수집·정제 파이프라인 구성
- 지역/품목별 수요 점수와 물류 거점 점수 설계
- 데이터 부족, 제외 업종, 과장 해석 방지 기준 정리
- Streamlit 기반 분석 대시보드 구현

`Python` · `Pandas` · `Scikit-learn` · `Public Data API` · `Gemini API` · `Streamlit`

---

## Work Experience

## 미래부품 계열

**물류 / 운영 / 재고 / 납기 관리**  
경력: 8년 9개월

### Main Responsibilities

- 입고, 출고, 재고, 납기 관리
- 구매 업무 및 거래처 커뮤니케이션
- 물류 흐름과 재고 상태 점검
- 소규모 인력 환경에서 업무 우선순위 조정
- 팀장 대행 및 현장 실무 조율 경험
- 의사결정권자 및 주요 거래처 담당자와 직접 커뮤니케이션

### Transferable Strengths

- 업무 흐름과 병목을 빠르게 파악하는 능력
- 납기와 품질 기준을 지키기 위한 검수 감각
- 제한된 인력과 자원 안에서 우선순위를 정하는 경험
- 현장 사용자의 불편과 운영 제약을 이해하는 관점

---

## Education

## AI Human 국비교육과정

- Python, 데이터 처리, AI 기초 학습
- FastAPI 기반 백엔드 API 개발 경험
- LLM API, 번역 모델, TTS 기반 AI 서비스 프로젝트 수행
- GitHub PR, Issue, README, 평가 리포트 기반 협업 경험
- 팀 프로젝트 2회 수행 및 팀장 경험

---

## Resume Positioning

저는 비전공자로 AI 개발을 시작했지만, 운영 현장에서 쌓은 문제 정의 능력과 팀 프로젝트 경험을 바탕으로 기술을 실제 서비스 흐름으로 연결하는 개발자가 되고자 합니다.

제가 지향하는 개발자는 가장 화려한 모델을 고르는 사람이 아니라, 사용자의 문제와 운영 조건을 이해하고 그 안에서 동작 가능한 AI 서비스를 만들어내는 사람입니다.

---

## Links

- GitHub: [github.com/mosejong](https://github.com/mosejong)
- Profile README: [github.com/mosejong/mosejong](https://github.com/mosejong/mosejong)
- SchoolBridge: [github.com/Maxmunzy/multicultural-ai](https://github.com/Maxmunzy/multicultural-ai)
- Rainbow Bridge: [github.com/mosejong/Rainbow-Bridge](https://github.com/mosejong/Rainbow-Bridge)
- Context Capsule: [github.com/mosejong/context-capsule](https://github.com/mosejong/context-capsule)
