# 모세종 · AI 서비스 개발자

AI API와 데이터 처리를 사용자 서비스에 연결하는 **신입 개발자**입니다.  
Python·FastAPI를 중심으로 화면·API·DB를 연결하고, 실행 결과와 실패 조건을 확인하며 개선합니다.

[프로젝트와 이력 보기](./RESUME.md) · [개발 기록](https://github.com/mosejong/finshield-ai/tree/main/docs/devlog) · [이메일](mailto:ahtpwhd95@gmail.com)

## 대표 프로젝트

### [FinShield AI](https://github.com/mosejong/finshield-ai)

금융사기 위험 신호를 분석하고 공식 근거와 행동 안내를 함께 제공하는 개인 프로젝트입니다.

- **담당:** 기획, AI 도구를 활용한 개발, 서비스 통합, GCP 배포·검증
- 규칙 코드가 판정을 확정하고 LLM이 설명하도록 역할을 나눴습니다.
- 배포 환경의 502 오류에서 컨테이너 직접 호출과 외부 콜드·웜 요청을 비교해 프록시 시간 제한을 확인했습니다.
- 공개 데모는 **2026.09.22 종료**했습니다. 저장소에서 구현과 운영 기록을 볼 수 있습니다.

[502 원인 분석](https://github.com/mosejong/finshield-ai/blob/main/docs/devlog/2026-09-05/products-cold-start-502.md) · [구조와 실행 방법](https://github.com/mosejong/finshield-ai#readme)

### [Jobiverse](https://github.com/neunglog-sys/job_simulator)

상담·직무 체험 데이터를 AI 진로 리포트로 연결하는 6인 팀 프로젝트입니다.

- **본인 담당:** Reporting / Data Pipeline, 커리어넷 API 연동, 데이터 정합성·CI 검토
- 역량 점수·AI 해석·추천 근거·각주가 포함된 PDF 리포트를 연결했습니다.
- 이스트캠프 KDT AI Human 4기 **최종 프로젝트 대상**을 수상했습니다.

[리포트 구현 보기](https://github.com/neunglog-sys/job_simulator/blob/main/services/api/app/domains/reporting/service.py)

### [SchoolBridge](https://github.com/Maxmunzy/multicultural-ai)

다문화가정의 가정통신문 이해를 돕는 5인 팀 프로젝트입니다.

- **본인 담당:** 베트남어 번역, 학교 용어사전, 오역 검토, 번역·TTS 연동
- 날짜·금액·연락처·URL을 보존하면서 번역 결과와 음성 파일을 팀 서비스에 연결했습니다.
- 팀 서비스는 8개 언어를 지원하며, KDT **1차 프로젝트 최우수상**을 수상했습니다.

[번역 실험 기록](https://github.com/Maxmunzy/multicultural-ai/blob/main/docs/experiments/2026-04-28-translation-glossary-quality.md)

## 다른 프로젝트

| 프로젝트 | 본인 담당과 확인할 내용 |
|---|---|
| [공공조달 수요·물류 거점 분석](https://github.com/mosejong/procurement-logistics-ai) | 개인 프로젝트. 6개 기관·9개 공공데이터 소스를 정제하고 지역·품목별 지표를 AI 설명과 지도 화면에 연결. 창업경진대회 대면심사 진출 |
| [Rainbow Bridge](https://github.com/mosejong/Rainbow-Bridge) | 6인 팀. 팀 리드, MVP 범위·일정 조율, API·서비스 통합, NCP 배포. [개인 기여 기록](https://github.com/mosejong/Rainbow-Bridge/blob/dev/CONTRIBUTION.md) |

## 개발 방식

요구사항과 작업 범위, 확인 기준을 정한 뒤 AI 개발 도구와 함께 구현합니다.  
FinShield에서는 **Claude Code가 프론트엔드·통합·문서, Codex가 백엔드·테스트**를 맡도록 작업을 나눴습니다.  
변경 이유와 실행 결과를 확인하고, 팀 전체 결과와 본인 기여를 구분해 기록합니다.

## 프로젝트에서 사용한 기술

| 영역 | 기술 |
|---|---|
| 언어·API | Python, FastAPI, REST API, Pydantic, SQLAlchemy |
| AI·데이터 | OpenAI / Gemini API, PostgreSQL, Pandas, scikit-learn |
| 배포·검증 | Docker, GCP / NCP, GitHub Actions, pytest |

이스트소프트 운영 **이스트캠프 KDT AI Human 4기 · 800시간 수료 · 우수수료생**  
이전 물류·구매 경력은 비개발 직무이며, 개발 직무는 신입으로 지원합니다.
