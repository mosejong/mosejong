# 모세종 | AI Service Pipeline Developer

> 물류 현장에서 배운 흐름 최적화 감각을 바탕으로,  
> 빠른 AI API 호출보다 서비스 품질을 통제할 수 있는 AI 파이프라인을 설계하는 개발자를 지향합니다.

저는 단순히 모델을 붙이는 것보다,  
입력 데이터가 어떻게 정제되고, 각 단계의 출력이 다음 단계의 입력으로 어떻게 전달되며,  
어디서 정보 손실과 오류가 발생하는지를 관찰하고 개선하는 데 관심이 있습니다.

물류 현장에서 쌓은 경험을 통해  
흐름, 병목, 검수 기준, 단계별 품질 관리의 중요성을 배웠고,  
이를 AI 서비스 개발에서도 입력·처리·출력·검수 구조를 설계하는 방식으로 확장하고 있습니다.

---

## About Me

- AI Human 교육과정을 기반으로 Python, ML/DL, NLP, FastAPI, Streamlit 프로젝트를 진행하고 있습니다.
- 물류 현장 경험을 바탕으로 데이터 흐름, 병목 개선, 검수 기준 설계에 관심이 있습니다.
- AI API를 빠르게 붙이는 것보다, 서비스에서 중요한 정보가 어디서 손실될 수 있는지 확인하고 통제 가능한 구조로 개선하는 것을 중요하게 생각합니다.
- 프로젝트 과정에서 실험 결과를 기록하고, 실패 원인을 수치와 구조로 정리하며 개선하는 방식을 선호합니다.

---

## Main Projects

### 1. [procurement-logistics-ai](https://github.com/mosejong/procurement-logistics-ai)

공공조달 데이터를 활용해 지역·품목별 수요 흐름과 창업 기회를 분석하는 데이터 기반 프로젝트입니다.

- 공공조달 API 데이터 수집 및 전처리
- 지역/품목별 수요 흐름 분석
- 추천 / 제외 / 데이터부족 기준 설계
- Streamlit 기반 분석 대시보드 구현
- 물류 경험을 공공조달 데이터 분석 관점으로 확장한 개인 대표 프로젝트

---

### 2. [SchoolBridge](https://github.com/Maxmunzy/multicultural-ai)

다문화 가정 학부모를 위한 학교 가정통신문 AI 번역·요약·TTS 서비스입니다.

- Korean school notice → 할 일 추출 → 카테고리 분류 → 다국어 번역 → TTS
- 담당: 번역/TTS 파이프라인, 학교 용어사전, 슬롯 보존 후처리, OCR 안정성 실험
- 핵심: 날짜·금액·URL·전화번호·준비물·제출기한처럼 틀리면 안 되는 정보를 보호하는 구조 설계
- 생성형 AI API를 메인 번역기로 쓰지 않고, NLLB 기반 파이프라인에 Slot Protection, Glossary, Template Translation, 검수 루프를 결합

---

### 3. [translation-tts-lab](https://github.com/mosejong/translation-tts-lab)

SchoolBridge 번역/TTS 파트를 개인적으로 검증한 실험 레포입니다.

- NLLB 기반 다국어 번역 실험
- Slot Protection을 통한 날짜·금액·URL·전화번호 보호
- 학교 도메인 용어사전 기반 Glossary Injection
- 준비물/제출물 안내를 위한 Template-based Translation
- Edge-TTS 기반 다국어 음성 출력
- 번역 품질 개선 및 검수 루프 설계

---

## Related Experiments

### [ocr-lab-schoolbridge](https://github.com/mosejong/ocr-lab-schoolbridge)

학교 가정통신문 이미지 입력 안정성을 검증하기 위한 OCR 실험 레포입니다.

OCR 결과를 바로 번역이나 학습 데이터로 사용하지 않고,  
CER/F1 기준으로 검증한 뒤 `review_required` 보조 입력 경로로 두는 방향을 실험했습니다.

---

## Tech Stack

### Language & Data

`Python` · `SQL` · `NumPy` · `Pandas`

### Machine Learning / Deep Learning

`Scikit-learn` · `TensorFlow/Keras` · `PyTorch` · `Transformers`

### Backend & Service

`FastAPI` · `Streamlit` · `REST API`

### Tools

`Git` · `GitHub` · `Docker` · `VS Code`

---

## What I Focus On

- 데이터 전처리와 품질 검수
- AI 모델 출력의 실패 가능성 분석
- 입력 → 처리 → 출력으로 이어지는 파이프라인 구조 설계
- Before / After가 보이는 실험 기록
- 사용자가 실제로 이해하고 행동할 수 있는 서비스 흐름 만들기

---

> 호기심을 실험으로 바꾸고,  
> 실험을 기록으로 남기며,  
> 흐름의 병목과 오류를 개선하는 개발자를 지향합니다.
