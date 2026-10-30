# 모세종 · AI 서비스 개발자

**개발 신입 · Python · FastAPI**  
[GitHub](https://github.com/mosejong) · [이메일](mailto:ahtpwhd95@gmail.com)

AI API와 데이터 처리를 사용자 서비스에 연결하는 신입 개발자입니다. 호출 경로·실행 결과·실패 사례를 비교하며 기능과 최종 산출물의 동작을 확인합니다.

## 주요 기술과 개발 방식

- **언어·API:** Python, FastAPI, REST API, Pydantic, SQLAlchemy
- **AI·데이터:** OpenAI / Gemini API, PostgreSQL, Pandas, scikit-learn
- **배포·검증:** Docker, GCP / NCP, GitHub Actions, pytest

Claude Code·Codex에 작업을 나누고 요구사항·작업 범위·확인 기준을 전달합니다. AI가 만든 화면·API·DB를 통합하고 수정 이유와 실행 결과를 확인합니다. 아래 기술은 프로젝트에서 활용한 범위이며, 상용 서비스 실무 경력은 신입입니다.

## 프로젝트

### FinShield AI · 금융사기 예방·행동 안내 서비스

**2026.08–09 · 개인 프로젝트**  
Python / FastAPI / Gemini API / Docker / GCP  
[저장소](https://github.com/mosejong/finshield-ai) · [502 원인 분석 기록](https://github.com/mosejong/finshield-ai/blob/main/docs/devlog/2026-09-05/products-cold-start-502.md)

- **담당:** 기획, AI 도구를 활용한 개발, 서비스 통합, 배포·검증
- 금융 계산·위험 판정은 규칙 엔진이 확정하고 LLM은 결과 설명을 담당하도록 경계를 설정했습니다. 생성 실패 시에도 확정된 판정과 행동 안내를 유지합니다.
- 외부 502 오류에서 컨테이너 직접 호출과 외부 콜드·웜 요청을 비교해 프록시의 8초 제한을 원인으로 좁혔습니다. 페이지 크기·캐시·호출 예산 변경과 회귀 조건을 확인했습니다.
- PWA·API·DB를 연결하고 GCP·Docker Compose·HTTPS로 공개 데모를 배포했습니다. **공개 데모는 2026.09.22 종료**했습니다.
- Claude Code는 프론트엔드·통합·문서, Codex는 백엔드·테스트를 맡도록 작업을 나누고 확인 기준을 전달했습니다. Gemini는 서비스가 호출하는 런타임 모델로 사용했습니다.

### Jobiverse · AI 진로 탐색·직무 체험 리포트

**2026.07.06–07.31 · 6인 팀**  
FastAPI / PostgreSQL / ReportLab / LLM API  
[팀 저장소](https://github.com/neunglog-sys/job_simulator) · [리포트 구현](https://github.com/neunglog-sys/job_simulator/blob/main/services/api/app/domains/reporting/service.py)

- **본인 담당:** Reporting / Data Pipeline
- 상담·미션 데이터를 역량 점수·AI 해석·추천 근거·각주가 포함된 PDF 리포트로 연결했습니다.
- 커리어넷 심리검사 API를 연동하고 데이터 정합성·CI 검토를 담당했습니다. 팀원이 조사한 자료를 바탕으로 AI와 추가 직무 조사·비교 및 작업 지시문을 정리했습니다.
- **팀 성과:** KDT AI Human 4기 최종 프로젝트 대상

### SchoolBridge · 다국어 가정통신문 안내

**2026.04.24–05.13 · 5인 팀**  
Python / NLLB / Edge-TTS  
[팀 저장소](https://github.com/Maxmunzy/multicultural-ai) · [번역 실험 기록](https://github.com/Maxmunzy/multicultural-ai/blob/main/docs/experiments/2026-04-28-translation-glossary-quality.md)

- **본인 담당:** 베트남어 번역, 학교 용어사전, 오역 검토, 번역·TTS 연동
- 학교 용어사전과 슬롯·마스킹으로 날짜·금액·연락처·URL을 보존하고 번역 결과와 음성 파일을 팀 서비스에 연결했습니다.
- **팀 서비스·평가:** NLLB 8개 언어·TTS 지원. 가정통신문 19개·용어 144개 기반 Gemini 루브릭 내부 평가를 진행했습니다. 원어민 검수나 외부 번역 벤치마크와 구분합니다.
- **팀 성과:** KDT 1차 프로젝트 최우수상

### 공공조달 수요 기반 입지·물류 거점 분석

**2026.05.13–07.21 · 개인 프로젝트**  
Pandas / scikit-learn / Streamlit / Gemini API  
[저장소](https://github.com/mosejong/procurement-logistics-ai)

- AI 도구를 활용해 6개 기관·9개 공공데이터 소스를 통합하고 품목 분류와 지역·품목별 지표를 Gemini 설명·지도 화면으로 연결했습니다.
- 나라장터 입찰 100,083건·계약 38,367건 등을 분석했습니다.
- **2026 공공조달데이터·AI 활용 창업경진대회 대면심사 진출**

### Rainbow Bridge · AI 펫로스 애프터케어

**2026.06.02–06.19 · 6인 팀**  
FastAPI / MongoDB / Docker / NCP  
[저장소](https://github.com/mosejong/Rainbow-Bridge) · [개인 기여·팀 평가 기록](https://github.com/mosejong/Rainbow-Bridge/blob/dev/CONTRIBUTION.md)

- **본인 담당:** Team Lead, API·서비스 통합, NCP 배포
- MVP 범위·역할·일정을 조율하고 감정 체크인부터 AI 메시지·TTS·미션·리포트까지 API·데이터 흐름을 통합했습니다.
- 콘텐츠 해금 규칙과 데모 데이터를 구성하고 실서버를 연동했습니다. 에이전트 로직 자체는 다른 팀원의 담당 영역입니다.
- 발표 후 공개 서버 운영을 종료했습니다.

## 교육·학력

- **이스트소프트 운영 이스트캠프 KDT AI Human 4기** — 2026.03–07, 직무교육 800시간 수료·우수수료생
- **진건고등학교** — 2011.03–2014.02, 졸업

## 이전 경력

아래는 비개발 직무 경력입니다. 개발 직무는 신입으로 지원합니다.

| 회사·직무 | 기간 | 담당 업무 |
|---|---|---|
| (주)정우금속이엔지 · 물류팀 대리 | 2021.02.22–2026.01.30 | 입출고·재고·납기·구매 관리 |
| (주)미래부품 · 구매팀 대리 | 2017.06.05–2020.01.02 | 매입·발주·재고·납기 관리 |
