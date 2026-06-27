# 모세종 | AI Service Builder

> **Operations-driven AI Service Builder**  
> 현장 운영 경험을 바탕으로, 사용자의 실제 문제와 서비스 제약을 먼저 보고 AI 기능을 서비스 흐름으로 연결하는 주니어 개발자입니다.

저는 물류·운영 현장에서 흐름, 병목, 검수, 납기 감각을 익혔습니다.  
이후 AI 국비교육과정에서 두 번의 실서비스형 팀 프로젝트를 진행하며, AI 서비스는 모델을 붙이는 것만으로 완성되지 않는다는 것을 배웠습니다.

제가 집중하는 방향은 다음과 같습니다.

- 사용자가 처한 상황과 비용 구조를 먼저 이해하는 것
- AI 모델의 출력을 그대로 믿지 않고, 글로사리·템플릿·후처리·검증 기준으로 보정하는 것
- 프론트엔드, 백엔드, 인프라, AI 기능이 하나의 사용자 흐름으로 연결되도록 설계하는 것
- AI가 모든 결정을 대신하는 구조가 아니라, 사람이 검토하고 승인할 수 있는 **Human-in-the-loop** 구조를 만드는 것

---

## Main Narrative

### 1. SchoolBridge  
**다문화 가정통신문 AI 도우미**  
제가 현재 가장 깊게 설명할 수 있는 대표 프로젝트입니다.

### 2. Rainbow Bridge  
**펫로스 애프터케어 AI 서비스**  
팀장/PM으로 서비스 흐름, 협업, 실서버 운영을 경험한 프로젝트입니다.

### 3. Context Capsule  
**AI 작업 인수인계 도구**  
두 번의 팀 프로젝트와 AI 협업 과정에서 직접 느낀 문제를 바탕으로 만든 개인 프로젝트입니다.

---

## Projects

### 1. [SchoolBridge](https://github.com/Maxmunzy/multicultural-ai)

다문화가정 학부모가 한국어 가정통신문에서 날짜, 준비물, 비용, 제출 여부 같은 핵심 정보를 놓치지 않도록 돕는 **AI 번역·요약·TTS 서비스**입니다.

#### Problem

가정통신문은 단순 번역만으로는 충분하지 않았습니다.  
학부모에게 중요한 것은 문장 전체의 자연스러운 번역보다, 실제로 해야 할 일을 정확히 이해하는 것이었습니다.

예를 들어 다음과 같은 정보는 틀리면 서비스 신뢰도가 크게 떨어집니다.

- 날짜 / 시간
- 준비물
- 비용
- 제출 여부
- 장소
- 전화번호 / URL
- 학교 행정 용어

#### My Role

- 번역/TTS 파이프라인 설계 및 구현
- NLLB 기반 8개 언어 번역 실험
- 학교 도메인 용어 글로사리 구축
- 날짜·금액·URL·전화번호 등 핵심 정보 보존 후처리
- Edge-TTS 기반 음성 출력 실험
- 번역 품질 검수 루프와 발표 흐름 정리

#### Design Intention

이 서비스는 다국적 학부모를 대상으로 하며, 사용자가 유료로 부담하기 어려운 구조라고 판단했습니다.  
그래서 외부 유료 API 의존도를 낮추고, 무료 또는 로컬 기반 번역 모델을 활용하는 방향을 검토했습니다.

다만 일반 번역 모델은 학교 현장에서 자주 쓰이는 표현을 오역할 가능성이 있었습니다.

예를 들면 다음과 같은 표현입니다.

- 스쿨뱅킹
- 현장체험학습
- 방과후학교
- 제출서류
- 가정통신문

이를 줄이기 위해 **글로사리 + 템플릿 기반 보정 구조**를 설계했습니다.  
모델이 번역을 담당하되, 학교 도메인에서 반드시 보호해야 하는 표현은 별도 사전과 후처리 구조로 보정하는 방식입니다.

프로젝트 이후 사용 모델의 라이선스 검토 필요성을 인지했습니다.  
실제 서비스 적용 시에는 라이선스 문제가 없는 모델로 교체해야 한다고 판단하고 있습니다.

다만 모델이 교체되더라도 **글로사리와 템플릿 기반 보정 구조는 유지 가능**하므로, 번역 품질 개선과 운영 비용 절감 측면에서 확장 가능한 설계라고 보고 있습니다.

#### Result

- 한국어 가정통신문 → 할 일 추출 → 카테고리 분류 → 다국어 번역 → TTS → 체크리스트 흐름 구현
- 베트남어, 영어, 러시아어, 말레이시아어, 몽골어, 중국어, 태국어, 일본어 번역 지원
- 용어사전 적용 전후 품질 평가: NLLB 39.0점 → 사전 적용 89.6점
- backend pytest 27개와 GitHub Actions 기반 PR 게이트 구성
- Android 실기기 기반 E2E 파이프라인 검증

#### Tech

`Python` · `FastAPI` · `Transformers` · `facebook/nllb-200-distilled-600M` · `Pandas` · `CSV` · `Edge-TTS` · `Docker` · `Android`

---

### 2. [Rainbow Bridge](https://github.com/mosejong/Rainbow-Bridge)

반려동물의 시한부 선고부터 이별, 장례, 회복까지 이어지는 **AI 펫로스 애프터케어 서비스**입니다.

이 프로젝트는 제가 모든 기술 파트를 깊게 구현했다기보다, 팀장/PM으로서 여러 파트가 하나의 사용자 흐름으로 연결되도록 조율한 프로젝트입니다.

<img src="./assets/rainbow-bridge-demo.gif" width="720" alt="Rainbow Bridge demo" />

#### My Role

- Team Lead / PM
- 서비스 흐름 설계 및 발표 구조 정리
- 역할 분담, 일정 관리, 기능 우선순위 조율
- 백엔드 API 및 기능 통합 참여
- NCP 서버 운영
- Docker 기반 배포 환경 구성
- nginx / HTTPS 운영 경험
- GPU 터널링 및 외부 AI 기능 연동 경험
- 안전 라우팅, 평가 리포트, 제출 산출물 정리

#### What I Learned

Rainbow Bridge를 통해 AI 서비스는 모델 하나만 잘 붙인다고 완성되지 않는다는 것을 배웠습니다.

감정 체크인, 미션, 추모 메시지, TTS, 영상 생성, 안전 라우팅, 사용자 화면, 서버 운영이 서로 맞물려야 실제 시연 가능한 서비스가 되었습니다.

특히 팀장으로서 다음의 중요성을 경험했습니다.

- 기능보다 먼저 전체 서비스 흐름을 정리하는 것
- 각 파트가 연결될 수 있도록 API와 데이터 구조를 맞추는 것
- 인프라를 먼저 열어 팀원이 같은 환경에서 테스트할 수 있게 하는 것
- AI 서비스에서 안전 라우팅과 차단 기준을 우선 설계하는 것
- 발표와 문서화까지 포함해야 프로젝트가 설명 가능한 결과물이 되는 것

#### Result

- 3주 프로토타입 기간 내 핵심 사용자 흐름 구현
- 감정 체크인, 기억 기반 추모 메시지, TTS, 미션, 타임라인, 회복 리포트 구현
- L2 이상 위기 감지 시 콘텐츠 생성을 차단하고 1393 안내로 전환하는 안전 구조 적용
- NCP 기반 실서버 배포 및 Android 시연 경험
- README, 평가 리포트, 호출 로그, 팀 회고 등 제출 산출물 정리

#### Tech

`FastAPI` · `MongoDB` · `SQLite` · `Redis` · `Gemini API` · `TTS` · `LivePortrait` · `FFmpeg` · `Docker` · `NCP` · `nginx` · `GitHub Actions`

---

### 3. [Context Capsule](https://github.com/mosejong/context-capsule)

팀 프로젝트와 AI 협업 과정에서 직접 느낀 문제를 바탕으로 만든 **AI 작업 인수인계 도구**입니다.

AI에게 작업을 맡길 때 가장 큰 문제는 단순히 모델 성능이 아니었습니다.  
필요한 컨텍스트를 얼마나 정확하고 적게 전달하느냐가 결과 품질에 큰 영향을 줬습니다.

전체 레포지토리를 무작정 읽히면 토큰이 낭비되고,  
반대로 필요한 파일을 놓치면 AI가 잘못된 방향으로 작업할 수 있었습니다.

Context Capsule은 이 문제를 줄이기 위해 만든 개인 프로젝트입니다.

#### Why I Built This

팀 프로젝트를 하면서 다음과 같은 문제를 반복해서 겪었습니다.

- AI에게 작업을 맡길 때 어떤 파일을 보여줘야 할지 매번 고민해야 함
- 전체 레포를 넣으면 토큰은 많이 쓰지만 정작 핵심 파일을 놓칠 수 있음
- 팀원에게 작업을 넘길 때 배경, 금지사항, 완료 기준이 누락되기 쉬움
- AI가 제안한 변경을 사람이 검토하고 승인할 수 있는 구조가 필요함

그래서 레포지토리와 작업 요청을 분석해, AI나 팀원에게 넘길 수 있는 작업 브리프를 생성하는 도구를 만들고 있습니다.

#### Core Features

- 레포지토리 구조 분석
- 작업 요청 기반 관련 파일 추천
- AI 작업용 인수인계 프롬프트 생성
- 팀원 작업 가이드 생성
- 주니어 개발자용 설명 생성
- 작업 리스크 분석
- GitHub Issue Packet 생성
- 토큰 사용량 절감 추정
- Streamlit 대시보드 / CLI / Windows 실행 지원

#### Direction

Context Capsule은 AI가 마음대로 코드를 수정하게 만드는 도구가 아닙니다.

제가 중요하게 보는 방향은 **AI가 제안하고, 사람이 검토하고, 승인하는 구조**입니다.

즉, AI 작업을 완전 자동화하기보다 사람이 통제 가능한 형태로 AI에게 일을 넘겨주는 도구를 목표로 하고 있습니다.

#### Tech

`Python` · `Streamlit` · `CLI` · `GitHub Issue Workflow` · `RAG-like Retrieval` · `Token Budgeting` · `Windows Launcher`

---

## Additional Experience

### [procurement-logistics-ai](https://github.com/mosejong/procurement-logistics-ai)

공공조달 데이터를 활용해 지역·품목별 공공수요와 물류 거점 후보를 분석한 데이터 기반 창업·입지 분석 프로젝트입니다.  
물류 현장에서 경험한 수요 흐름과 납품 구조 감각을 공공데이터 분석으로 확장했습니다.

`Python` · `Pandas` · `Scikit-learn` · `Public Data API` · `Gemini API` · `Streamlit`

---

## Tech Stack

### Backend / API

`Python` · `FastAPI` · `REST API` · `SQLite` · `MongoDB` · `Redis`

### AI / NLP

`LLM API` · `Prompt Engineering` · `Transformers` · `NLLB` · `Glossary` · `TTS` · `RAG-like Retrieval`

### Data

`Pandas` · `CSV` · `Public Data API` · `Scikit-learn`

### Infra / Deployment

`Docker` · `NCP Server` · `nginx` · `HTTPS` · `GitHub Actions` · `DuckDNS` · `Let's Encrypt`

### Frontend / Tools

`React` · `Vite` · `Tailwind CSS` · `Streamlit` · `Android`

---

## Working Principles

- AI 출력은 최종 답이 아니라 **검증해야 할 중간 산출물**로 봅니다.
- 기술 선택은 사용자 상황, 비용 구조, 운영 제약과 함께 판단해야 한다고 생각합니다.
- 기능 구현만큼 실패 케이스, 예외 처리, 품질 기준을 중요하게 봅니다.
- 팀 프로젝트에서는 역할, 인터페이스, 완료 기준이 명확해야 협업이 가능하다고 생각합니다.
- AI가 모든 결정을 대신하기보다, 사람이 검토하고 승인할 수 있는 구조를 선호합니다.

---

## Current Focus

현재는 AI 서비스를 단순히 “모델을 붙이는 것”이 아니라, 실제 사용자가 이해하고 사용할 수 있는 흐름으로 설계하는 것에 집중하고 있습니다.

특히 다음 주제에 관심이 있습니다.

- AI 서비스 기획과 백엔드 구현
- LLM 기반 업무 보조 도구
- 번역/TTS 기반 접근성 개선
- AI 작업 인수인계와 협업 자동화
- 운영 경험을 반영한 실용적인 AI 서비스

---

## Positioning

저는 비전공자로 AI 개발을 시작했지만, 운영 현장에서 쌓은 문제 정의 능력과 팀 프로젝트 경험을 바탕으로 기술을 실제 서비스 흐름으로 연결하는 개발자가 되고자 합니다.

제가 지향하는 개발자는 가장 화려한 모델을 고르는 사람이 아니라, 사용자의 문제와 운영 조건을 이해하고 그 안에서 동작 가능한 AI 서비스를 만들어내는 사람입니다.

---

## Contact

- GitHub: [github.com/mosejong](https://github.com/mosejong)
- Resume: 준비 중
- Portfolio: 준비 중
