# 작업 로그

> **보관 기록 (2026-10-16 고정)** — 대표 문서이며 모델은 수정하지 않는다. 새 기록은 같은 폴더의 `LOG.<모델>.md`(예: `LOG.claude.md`, `LOG.codex.md`)에 쓰고, 읽을 때는 이 문서와 `LOG.*.md`를 모두 읽는다. 규칙: `Git/CLAUDE.md` 3절.

## 2026-04-14 ~ 2026-06-08 (채팅 세션)

### 확정된 규칙
- 북마크명: `영문명 – 한글 용도`
- 최상위 폴더: 전체 대문자
- 하위 폴더: 첫 글자만 대문자

### 주요 결정 사항
| 날짜 | 결정 |
|---|---|
| 4/14 | 전체 구조 초안 (v1): 404→377개, 95→60폴더 |
| 4/16 | Adobe 6개 도구 추가 (v2→v3): 기능별 폴더 분산 배치 |
| 5/21 | WORK→RESOURCE/OFFICE 통합, 2단계 계층화 (v4) |
| 5/21 | TOOL→RESOURCE 개명, UTILS 도입 |
| 5/26 | MEDIA→ASSETS, UTILS 폐지, Interior & floor plan 신규 (v5) |
| 6/8  | Claude Code 전환, CLAUDE.md/HANDOFF.md/LOG.md 생성 |

### Adobe 배치 결정
- Firefly → AI_OTHER > Image gen (기존)
- Express·Photoshop·Lightroom → RESOURCE > DESIGN > Design & editor
- Acrobat → RESOURCE > Converter & utils
- Stock → RESOURCE > ASSETS > Premium images
- Fonts → RESOURCE > ASSETS > Free fonts (구 Typekit 대체)
- Color → RESOURCE > DESIGN > Color tools (기존)

### 폴더명 변경 이력
| 구 이름 | 새 이름 | 이유 |
|---|---|---|
| TOOL | RESOURCE | 도구+리소스 포괄 의미 |
| MEDIA | ASSETS | 소재·에셋 성격 정확히 반영 |
| UTILS | (폐지) | 범위 모호, 하위 폴더 직속 승격 |
| Typekit | Adobe Fonts | 서비스명 변경 반영 |

### 미완료 (Claude Code에서 계속)
- GitHub.dev 북마크 추가
- 최신 소스(`즐겨찾기_26. 6. 8..html`) 기준 Gen_ 파일 생성

## 2026-07-06

- 최신 소스(`즐겨찾기_26. 7. 6..html`) 기준 프로젝트 호스팅·인프라 서비스 5개 추가
  - `RESOURCE > Cloud`: Render, Vercel, Oracle Cloud, Cloudflare
  - `RESOURCE > DEV > Backend & API`: Google Cloud Console (Firebase Console 옆)
  - GitHub·Firebase Console은 기존 등록 확인되어 제외
- `Gen_즐겨찾기_26.7.6.html` 생성 (327개 북마크 / 71개 폴더), DL 태그 균형 검증 통과

## 2026-07-15

- 소스 파일명 규칙 확장: `bookmarks_YY. M. D..html`(Chrome) 추가 확인, `즐겨찾기_...`(Edge)와 병행 사용 → `CLAUDE.md` 파일명 규칙 업데이트
- **DEV 구조 대개편**
  - `AI_OTHER > Ai dev` 폴더 폐지 → 전체 항목 `RESOURCE > DEV`로 이동 통합 (AI_OTHER는 채팅/생성/에이전트 성격만 유지)
  - `RESOURCE > DEV`를 8개 하위 폴더로 재편: Repo & editor / AI API & Docs / MCP / Local AI & models / Hosting & deploy(구 CMS&hosting+Cloud 호스팅 통합) / Backend & API / Data & BI / Download
  - `RESOURCE > Cloud`는 개인 저장소만 남김: OneDrive, Google Drive
  - Phase(UI 디자인 프로토타입) → `RESOURCE > DESIGN > Template & mockup` 이동
  - `AI API & Docs`: OpenAI/Anthropic/Gemini API 콘솔·문서·상태를 대표 URL 1개로 통합, Perplexity Console 신규 추가 → **북마크 중복 방지 원칙** 확립(같은 서비스 하위 페이지는 별도 등록 금지, 대표 URL+설명 통합)
- **AI_OTHER 6개 폴더(87개) 무료 혜택순 재정렬**
  - 정렬 기준: 1) 완전무료·무제한 → 2) 정기 리셋형 넉넉한 무료 → 3) 체험 크레딧 소진 후 유료
  - 각 북마크 제목에 `(사용량 요약)` 괄호 추가
  - 미분류 항목(Stability AI, Audiobox)은 원 설명 유지, 추후 재검토 필요
- `Gen_즐겨찾기_26.7.15.html` 생성 (324개 북마크 / 72개 폴더), DL 태그·URL 개수 검증 통과
- 오래된 소스 스냅샷 정리: `즐겨찾기_26. 6. 22..html`, `즐겨찾기_26. 7. 6..html` 삭제 (최신 소스만 유지)

## 2026-08-21

- INDEX.md 추가 — 스크립트 처리 단계·중복 방지 로직 → 파일 경로 매핑. 인덱싱 중 `gen_bookmarks.py`가 2026-06 이후 방치된 1회성 스크립트이고, 서비스 단위 중복 방지는 코드가 아니라 HANDOFF.md의 판단 규칙으로만 존재함을 확인.

## 2026-08-31

- `RESOURCE > ASSETS > Free icons`에 아이콘·기호 사이트 3개 추가
  - `Lucide – 오픈소스 아이콘 라이브러리` (https://lucide.dev/icons/)
  - `Tabler Icons – 무료 오픈소스 SVG 아이콘` (https://tabler.io/icons)
  - `Symbl – 유니코드 문자·기호·이모지 검색` (https://symbl.cc/)
  - 기존 Free icons 3개(Flaticon·The Noun Project·Iconscout)와 중복 없음 확인
- `Gen_즐겨찾기_26.8.31.html` 생성 (327개 북마크 / 72개 폴더), DL 태그 균형 검증 통과 (73/73)
- 최신 소스는 `bookmarks_26. 7. 15..html` 그대로 (신규 소스 없음, 직전 출력 복사 후 편집)
