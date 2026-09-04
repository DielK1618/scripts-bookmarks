# HANDOFF

## 현재 상태
- 최신 소스: `bookmarks_26. 7. 15..html` (소스 파일명이 `즐겨찾기_` → `bookmarks_` 접두사로 변경됨, Edge 다운로드 로케일 차이로 추정)
- 최신 출력: `Gen_즐겨찾기_26.8.31.html`
- 북마크 수: 327개 / 폴더 72개

## 완료된 작업 (채팅에서)
- [x] 전체 구조 재편 (v1~v5)
- [x] WORK → RESOURCE/OFFICE 통합
- [x] TOOL → RESOURCE 로 개명 및 2단계 계층화
- [x] MEDIA → ASSETS 개명, Art museums → Design reference 이동
- [x] UTILS 폐지 → 하위 폴더 RESOURCE 직속 승격
- [x] Adobe 7개 도구 기능별 폴더 분산 배치
- [x] Interior & floor plan 신규 폴더 + 5개 사이트 추가
- [x] Toolify Browser Ext → AI_OTHER > Ai tools 배치

## 완료된 작업 (Claude Code에서)
- [x] `Gen_즐겨찾기_26.6.8.html` 생성 (2026-06-09)
- [x] GitHub.dev – AI_OTHER > Ai dev 배치 (소스에서 RESOURCE > DEV > Web & dev tools → 이동)
- [x] `Gen_즐겨찾기_26.6.15.html` 생성 (2026-06-15): Claude Platform(신규) + Google AI Studio·OpenAI Platform(Ai tools→Ai dev 상단 이동, URL 갱신)
- [x] `Gen_즐겨찾기_26.6.22.html` 생성 (2026-06-22): RESOURCE > File transfer 폴더 신설(ToffeeShare·file.kiwi·Send Anywhere·Smash·WeTransfer) + HTML Vault URL 갱신 + weather_dashboard 제거 + GetDesign.md → Design reference 추가
- [x] `Gen_즐겨찾기_26.7.6.html` 생성 (2026-07-06): 프로젝트 호스팅·인프라 서비스 5개 추가 — RESOURCE > Cloud(Render·Vercel·Oracle Cloud·Cloudflare), RESOURCE > DEV > Backend & API(Google Cloud Console). GitHub·Firebase Console은 기존 등록되어 있어 제외
- [x] `Gen_즐겨찾기_26.7.15.html` 생성 (2026-07-15): **DEV 구조 대개편**
  - `AI_OTHER > Ai dev` 폴더 폐지 → 전체 항목을 `RESOURCE > DEV`로 이동 통합 (AI_OTHER는 이제 채팅/생성/에이전트 성격만 유지)
  - `RESOURCE > DEV`를 8개 하위 폴더로 재편: Repo & editor / AI API & Docs / MCP / Local AI & models / Hosting & deploy(구 CMS&hosting+Cloud 호스팅 통합) / Backend & API / Data & BI / Download
  - `RESOURCE > Cloud`는 개인 저장소만 남김: OneDrive, Google Drive (2개)
  - Phase(UI 디자인 프로토타입) → `RESOURCE > DESIGN > Template & mockup` 이동
  - `AI API & Docs`: OpenAI/Anthropic/Gemini API 콘솔·문서·상태를 각각 대표 URL 1개로 통합(중복 링크 제거 원칙), 설명에 "콘솔·문서·상태" 명시. Perplexity Console 신규 추가(1개 순증)
  - **원칙**: 같은 서비스의 하위 페이지(docs/status/console 등)는 별도 북마크로 늘리지 않고 대표 URL 하나 + 설명으로 통합
- [x] `AI_OTHER` 하위 6개 폴더(Ai chat/Image gen/Video gen/Voice & sound/3D gen/Ai tools, 총 87개) 무료 혜택순 재정렬 + 설명에 사용량 정보 추가 (2026-07-15)
  - 정렬 기준(사용자 제공 검증 리스트): 1) 완전무료·무제한 → 2) 정기 리셋형 넉넉한 무료 → 3) 체험 크레딧 소진 후 유료
  - 각 북마크 제목에 `(사용량 요약)` 괄호 추가, 예: `뤼튼 – 한국형 AI (완전무료·무제한)`
  - **미분류 항목** (사용자 리스트에 없어 원 설명 유지, 재검토 필요): Stability AI (Image gen), Audiobox (Voice & sound)

## 완료된 작업 (Claude Code에서 계속)
- [x] `Gen_즐겨찾기_26.8.31.html` 생성 (2026-08-31): `RESOURCE > ASSETS > Free icons`에 Lucide·Tabler Icons·Symbl 3개 추가 (신규 소스 없음, 직전 출력 복사 후 편집). 327개 / 72폴더

## 다음 할 일
- [ ] SOS 폴더 정리 (별도 관리 중, 변경 금지)
- [ ] REPOSITORY 폴더 정리 (별도 관리 중, 변경 금지)

## 변경 금지 폴더
- `SOS` — 사용자 별도 관리
- `REPOSITORY` — 사용자 별도 관리
- `ZION` — 사용자 별도 관리

## 파일명 규칙
- 소스: `즐겨찾기_YY. M. D..html` (Edge 다운로드 원본, 공백 있음)
- 출력: `Gen_즐겨찾기_YY.M.D.html` (공백·중복점 제거, Gen_ 접두사)
