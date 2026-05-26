# 모세종 | AI Service Pipeline Developer

> 물류 현장에서 배운 흐름 최적화 감각을 바탕으로,  
> 빠른 AI API 호출보다 서비스 품질을 통제할 수 있는 AI 파이프라인을 설계하는 개발자를 지향합니다.

저는 문제를 발견하면 감으로 넘기지 않고,  
실험을 통해 원인을 좁히고 결과를 기록하며 개선하는 방식으로 프로젝트를 진행합니다.

입력 데이터가 어떻게 정제되고,  
각 단계의 출력이 다음 단계의 입력으로 어떻게 전달되며,  
어디서 정보 손실과 오류가 발생하는지를 관찰하고 개선하는 데 관심이 있습니다.

---

## Focus

- 문서·데이터 기반 AI 서비스 파이프라인 설계
- AI 모델 출력의 실패 가능성 분석
- 입력 → 처리 → 출력 → 검수로 이어지는 구조 설계
- Slot Protection, Glossary, Template, 검수 루프를 통한 품질 통제
- Before / After가 보이는 실험 기록
- 사용자가 실제로 이해하고 행동할 수 있는 서비스 흐름 구현

---

## Project Highlights

- **SchoolBridge**  
  다문화 가정 학부모를 위한 학교 가정통신문 AI 번역·요약·TTS 서비스에서  
  번역/TTS 파이프라인, 학교 용어사전, 슬롯 보존 후처리 구조를 담당했습니다.

- **procurement-logistics-ai**  
  공공조달 데이터를 활용해 지역·품목별 수요 흐름과 창업 기회를 분석하는  
  데이터 기반 Streamlit 대시보드를 구현했습니다.

- **translation-tts-lab**  
  SchoolBridge 번역/TTS 파트를 별도 실험 레포에서 검증하며,  
  Slot Protection, Glossary Injection, Template-based Translation을 실험했습니다.

---

## About Me

- AI Human 교육과정을 기반으로 Python, ML/DL, NLP, FastAPI, Streamlit 프로젝트를 진행하고 있습니다.
- 물류 현장 경험을 바탕으로 데이터 흐름, 병목, 검수 기준을 AI 서비스 파이프라인 설계 관점으로 확장하고 있습니다.
- 단순히 AI API를 연결하는 것보다, 서비스에서 중요한 정보가 어디서 손실될 수 있는지 확인하고 통제 가능한 구조로 개선하는 것을 중요하게 생각합니다.
- 프로젝트 과정에서 실험 결과를 기록하고, 실패 원인을 수치와 구조로 정리하며 개선하는 방식을 선호합니다.

---

## Main Projects

### 1. [procurement-logistics-ai](https://github.com/mosejong/procurement-logistics-ai)

공공조달 데이터를 활용해 지역·품목별 수요 흐름과 창업 기회를 분석하는 데이터 기반 프로젝트입니다.

단순히 공고 수를 보여주는 것이 아니라,  
공고 데이터와 계약/낙찰 데이터를 구분해  
“수요 의향”과 “실제 계약 흐름”을 함께 해석하는 구조를 설계했습니다.

#### Key Features

- 공공조달 API 데이터 수집 및 전처리
- 지역/품목별 수요 흐름 분석
- 추천 / 제외 / 데이터 부족 기준 설계
- Streamlit 기반 분석 대시보드 구현
- 공고 데이터와 계약/낙찰 데이터를 구분한 분석 구조 설계
- 물류 경험을 공공조달 데이터 분석 관점으로 확장한 개인 대표 프로젝트

#### What I Focused On

- 공공데이터를 단순 조회가 아닌 의사결정 보조 흐름으로 구조화
- 수치 기반 분석 결과가 과장되지 않도록 해석 기준 설계
- 데이터 부족, 표본 부족, 지역 편차를 사용자에게 명확히 전달하는 방식 고민
- 물류 현장에서 경험한 흐름·병목·입지 감각을 데이터 분석 프로젝트로 확장

---

### 2. [SchoolBridge](https://github.com/Maxmunzy/multicultural-ai)

다문화 가정 학부모를 위한 학교 가정통신문 AI 번역·요약·TTS 서비스입니다.

학교 가정통신문에서 중요한 할 일 문장을 추출하고,  
카테고리 분류, 다국어 번역, TTS 음성 안내까지 연결하는 팀 프로젝트입니다.

#### Service Flow

```text
Korean school notice
→ 할 일 문장 추출
→ 카테고리 분류
→ 다국어 번역
→ TTS
→ 학부모용 체크리스트 / 캘린더 / 안내 화면
```

#### My Role

- 번역/TTS 파이프라인 설계 및 구현
- 학교 도메인 용어사전 구축
- 날짜·금액·URL·전화번호 등 핵심 정보 보존 후처리
- NLLB 기반 다국어 번역 실험
- Edge-TTS 기반 음성 출력 실험
- README, 발표 흐름, 기술 설명 정리

#### What I Focused On

- 생성형 AI API를 메인 번역기로 바로 사용하는 대신,  
  NLLB 기반 번역 파이프라인에 Slot Protection, Glossary, Template Translation, 검수 루프를 결합했습니다.

- 날짜, 금액, URL, 전화번호, 준비물, 제출기한처럼  
  틀리면 안 되는 정보를 보호하는 구조를 설계했습니다.

- 번역 품질 문제를 단순히 “모델 성능 부족”으로 보지 않고,  
  도메인 용어, 입력 문장 구조, 후처리, 검수 기준의 문제로 나누어 개선했습니다.

---

### 3. [translation-tts-lab](https://github.com/mosejong/translation-tts-lab)

SchoolBridge 번역/TTS 파트를 개인적으로 검증한 실험 레포입니다.

팀 프로젝트에 바로 넣기 어려운 번역 품질 개선 아이디어를  
별도 실험 레포에서 검증하고 정리했습니다.

#### Key Experiments

- NLLB 기반 다국어 번역 실험
- Slot Protection을 통한 날짜·금액·URL·전화번호 보호
- 학교 도메인 용어사전 기반 Glossary Injection
- 준비물/제출물 안내를 위한 Template-based Translation
- Edge-TTS 기반 다국어 음성 출력
- 번역 품질 개선 및 검수 루프 설계

#### What I Focused On

- 번역 결과에서 어떤 정보가 손실되는지 확인
- 학교 도메인 용어가 잘못 번역되는 원인 분석
- 규칙 기반 후처리와 모델 번역의 역할 분리
- 테스트 케이스를 통해 개선 전후 결과 비교

---

## Tech Stack

### Language & Data

`Python` · `SQL` · `NumPy` · `Pandas`

### Machine Learning / Deep Learning

`Scikit-learn` · `TensorFlow/Keras` · `PyTorch` · `Transformers`

### NLP / LLM

`NLLB` · `Hugging Face Transformers` · `Prompt Engineering` · `LangChain` · `RAG`

### Backend & Service

`FastAPI` · `Streamlit` · `REST API`

### Tools

`Git` · `GitHub` · `Docker` · `VS Code`

---

## What I Focus On

### 1. Data Flow

입력 데이터가 어떤 형태로 들어오고,  
어떤 전처리를 거쳐 다음 단계로 전달되는지 확인합니다.

### 2. Failure Analysis

AI 모델의 결과를 그대로 신뢰하기보다,  
어디서 오류가 발생하는지 관찰하고 실패 유형을 나누어 봅니다.

### 3. Controllable Pipeline

빠른 API 호출보다,  
서비스에서 중요한 정보가 손실되지 않도록 통제 가능한 구조를 설계하는 데 관심이 있습니다.

### 4. Experiment Records

개선 전후 결과를 비교하고,  
실험 과정과 판단 근거를 기록으로 남기는 방식을 선호합니다.

### 5. User-Oriented Service Flow

기술 구현에서 끝나는 것이 아니라,  
사용자가 실제로 이해하고 행동할 수 있는 서비스 흐름을 만드는 데 집중합니다.

---

## Direction

저는 모델 하나의 성능보다,  
입력 데이터와 모델 출력이 서비스 안에서 어떻게 연결되고 검증되는지에 관심이 있습니다.

앞으로는 LLM, RAG, 데이터 기반 AI 서비스를 중심으로  
문서와 데이터를 구조화하고,  
AI가 근거 있게 답변하도록 돕는 서비스 파이프라인을 만들어가고자 합니다.

---

> 호기심을 실험으로 바꾸고,  
> 실험을 기록으로 남기며,  
> 흐름의 병목과 오류를 개선하는 개발자를 지향합니다.
