# AIBA Lab 웹사이트 - Google Sheets 연동 가이드

이 가이드는 Google Sheets로 웹사이트 데이터를 관리하고 자동 배포하는 방법을 설명합니다.

## 📋 개요

- **Google Sheets**: 멤버, 논문, 강의, 파트너, 갤러리 정보 관리
- **GitHub Actions**: 시트 수정 시 자동으로 사이트 재빌드
- **딜레이**: 약 1-2분

---

## 🚀 설정 단계

### 1단계: Google Sheets 생성

1. [Google Sheets](https://sheets.google.com)에서 새 스프레드시트 생성
2. 이름: `AIBA Lab Website Data`
3. 아래 시트들을 생성하고 첫 행에 컬럼명 입력:

#### Members 시트
| role | name_en | name_ko | position | affiliation | email | website | photo | research_area | bio | graduation_info |
|------|---------|---------|----------|-------------|-------|---------|-------|---------------|-----|-----------------|
| Faculty | Donghyuk Shin | 신동혁 | Associate Professor | KAIST College of Business | dhs@kaist.ac.kr | https://dshin32.github.io | shin.jpg | Economics of AI/IT, AI/ML Applications | Ph.D. in CS, UT Austin\nML Scientist, Amazon | |
| PhD | Jaehyung Park | 박재형 | | | | | park_jaehyung.jpg | IT/AI | | |
| PhD | Junha Baek | 백준하 | | | | | baek_junha.png | Generative AI | | |
| MS | Woohyun Park | 박우현 | | | | | park_woohyun.png | Platform | | |
| Alumni | Woojeong Yoo | 유우정 | | | | | yoo_woojeong.png | | | M.S. 2025 · PwC |

**role 값**: `Faculty`, `PhD`, `MS`, `Undergrad`, `Alumni`

#### Publications 시트
| type | bibtex_key | title | authors | venue | year | volume | number | pages | abbr | selected | award |
|------|------------|-------|---------|-------|------|--------|--------|-------|------|----------|-------|
| journal | shin2024misq | Disinformation Spillover... | Lee, Sangwook and Shin, Donghyuk and... | MIS Quarterly | 2024 | | | | MISQ | TRUE | |
| conference | shin2025cikm | PlaceSim: An LLM-based... | Lee, Suhyeon and Yu, Youngjun and... | CIKM | 2025 | | | | CIKM | TRUE | |

**type 값**: `journal`, `conference`

#### Teaching 시트
| course_code | course_name | description | topics | semester | is_current |
|-------------|-------------|-------------|--------|----------|------------|
| MGT 562 | Business Analytics | Graduate level course on data analytics | Machine Learning, Deep Learning, NLP | | TRUE |
| MGT 565 | IT and Strategy | Graduate level course on IT | Platform Economics, AI/IT Economics | | TRUE |
| | Data Science for Business | | | 2022-2023 | FALSE |

#### Industry 시트
| name | type | logo | description |
|------|------|------|-------------|
| Baemin | Collaborator | baemin.jpg | |
| Hankook Tire | Collaborator | hankook.png | |
| NRF | Funding | nrf.png | National Research Foundation of Korea |

**type 값**: `Collaborator`, `Funding`

#### Gallery 시트
| image | caption | category | date |
|-------|---------|----------|------|
| cist.png | CIST 2024, Atlanta | Conferences | 2024-10 |
| teachers-day.png | 스승의 날 이벤트 | Lab Life | 2024-05 |

**category 값**: `Conferences`, `Lab Life`

---

### 2단계: Google Cloud 서비스 계정 생성

1. [Google Cloud Console](https://console.cloud.google.com) 접속
2. 새 프로젝트 생성 (예: `aiba-lab-website`)
3. **APIs & Services** → **Enable APIs** → `Google Sheets API` 활성화
4. **IAM & Admin** → **Service Accounts** → **Create Service Account**
   - 이름: `github-actions`
   - 역할: 없음 (나중에 시트에서 직접 공유)
5. 서비스 계정 클릭 → **Keys** → **Add Key** → **Create new key** → **JSON**
6. 다운로드된 JSON 파일 내용을 복사

---

### 3단계: Google Sheets 공유

1. Google Sheets 열기
2. 우측 상단 **공유** 클릭
3. 서비스 계정 이메일 추가 (예: `github-actions@your-project.iam.gserviceaccount.com`)
4. **뷰어** 권한 부여

---

### 4단계: GitHub Secrets 설정

1. GitHub 저장소 → **Settings** → **Secrets and variables** → **Actions**
2. **New repository secret** 클릭:

   **GOOGLE_CREDENTIALS**
   ```
   (서비스 계정 JSON 전체 내용 붙여넣기)
   ```

   **SHEET_ID**
   ```
   (Google Sheets URL에서 /d/ 뒤의 ID)
   예: https://docs.google.com/spreadsheets/d/1ABC123xyz.../edit
   → 1ABC123xyz...
   ```

---

### 5단계: GitHub Personal Access Token 생성

1. GitHub → **Settings** → **Developer settings** → **Personal access tokens** → **Tokens (classic)**
2. **Generate new token**
3. 권한: `repo` (전체 체크)
4. 토큰 복사 (한 번만 보임!)

---

### 6단계: Google Apps Script 설정 (자동 트리거)

1. Google Sheets에서 **확장 프로그램** → **Apps Script**
2. `scripts/google_apps_script.js` 내용 복사하여 붙여넣기
3. `CONFIG.GITHUB_TOKEN`을 실제 토큰으로 변경
4. 저장 (Ctrl+S)
5. `setupTrigger` 함수 실행 (한 번만)
6. 권한 승인

---

## ✅ 테스트

### 수동 테스트
1. GitHub → **Actions** → **Sync Google Sheets to Jekyll** → **Run workflow**
2. 1-2분 후 사이트 확인

### 자동 트리거 테스트
1. Google Sheets에서 아무 셀 수정
2. 1분 후 GitHub Actions 실행 확인
3. 2분 후 사이트 업데이트 확인

---

## 🔧 문제 해결

### Actions가 실행 안 됨
- GitHub Secrets 확인 (GOOGLE_CREDENTIALS, SHEET_ID)
- Apps Script 토큰 확인

### 시트 데이터가 반영 안 됨
- 시트 이름 정확히 확인 (Members, Publications, Teaching, Industry, Gallery)
- 컬럼명 정확히 확인 (첫 행)
- Google Sheets 공유 설정 확인

### 이미지가 안 보임
- `assets/img/members/`, `assets/img/partners/`, `assets/img/gallery/` 폴더에 이미지 업로드
- 파일명이 시트의 photo/logo/image 컬럼과 일치하는지 확인

---

## 📁 파일 구조

```
aiba-kaist.github.io/
├── .github/
│   └── workflows/
│       └── sync-sheets.yml      # GitHub Actions 워크플로우
├── scripts/
│   ├── sync_sheets.py           # 동기화 스크립트
│   └── google_apps_script.js    # Apps Script (참조용)
├── _pages/
│   ├── team.md                  # 자동 생성
│   ├── teaching.md              # 자동 생성
│   ├── industry.md              # 자동 생성
│   └── gallery.md               # 자동 생성
└── _bibliography/
    └── papers.bib               # 자동 생성
```

---

## 📞 지원

문제가 있으면 GitHub Issues에 등록하거나 dhs@kaist.ac.kr로 연락하세요.
