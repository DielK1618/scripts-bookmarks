# scripts-bookmarks 프로젝트

> **트러블슈팅**: 작업 전 또는 오류 발생 시 → [`TROUBLESHOOTING.md`](TROUBLESHOOTING.md) 먼저 확인. 없으면 LOG.md → 웹 검색 순으로 진행. 해결 후 반드시 `TROUBLESHOOTING.md`에 추가.

## 경로
- 소스: `Favorites/SourceHTML/` → 최신 파일 = 날짜가 가장 최근인 `즐겨찾기_YY. M. D..html`
- 출력: `Favorites/OutputHTML/Gen_즐겨찾기_YY.M.D.html` (공백·중복점 제거, Gen_ 접두사)

## 작업 방식
1. 소스 파일 파싱 → `url_map` 구축 (ICON 데이터 보존)
2. 새 구조로 재조립 → 출력 파일 저장
3. 작업 후 HANDOFF.md 업데이트

## 북마크 명명 규칙
- 형식: `영문 서비스명 – 한글 주요 용도` (반각 대시 ` – ` 사용)
- 예: `ChatGPT – 대화형 AI`, `Figma – UI/UX 협업 디자인`

## 폴더 명명 규칙
- 최상위: 전체 대문자 (`AI`, `RESOURCE`, `SOCIAL` 등)
- 하위: 첫 글자만 대문자 (`Ai chat`, `Free images`, `Design & editor`)
- 그룹(2단계): 전체 대문자 (`OFFICE`, `DESIGN`, `ASSETS`, `DEV`)

## 현재 최상위 구조
```
즐겨찾기 모음 (툴바)
AI_FAVORITE
AI_OTHER
  └─ Ai chat / Image gen / Video gen / Voice & sound / 3D gen / Ai tools / Ai dev
ZION
  └─ Official sites / Planning sites / Quick links / Related universities
REPOSITORY
  └─ Production
SOCIAL
  └─ Talk & mail / Video call / Media
LEARN
  └─ NJU / Edu LMS / Language / Coding / Bible / Car
RESOURCE
  ├─ OFFICE   → Docs & office / Note & collab
  ├─ DESIGN   → Design & editor / Template & mockup / Color tools / Design reference
  ├─ ASSETS   → Free images / Free icons / Free fonts / Free audio / Premium images
  ├─ DEV      → Web & dev tools / CMS & hosting / Data & BI / Download
  ├─ Cloud
  ├─ Map & translation
  ├─ Mindmap & diagram
  ├─ Converter & utils
  └─ Interior & floor plan
SHOPPING
  └─ Open market / General mall / PC & electronics / Welfare mall
     Entertainment / Second hand / Global shopping / Internet plans
SOS
  └─ Loss
```

## 코드 패턴
```python
# URL → 원본 태그 맵 (ICON 보존)
anchors = re.findall(r'<DT><A [^>]+>[^<]*</A>', content)
url_map = {}
for a in anchors:
    m = re.search(r'HREF="([^"]+)"', a)
    if m and m.group(1) not in url_map:
        url_map[m.group(1)] = a

def bm(url, title=None):
    tag = url_map.get(url, f'<DT><A HREF="{url}" ADD_DATE="0">{title}</A>')
    if title:
        tag = re.sub(r'>([^<]*)</A>', f'>{title}</A>', tag)
    return f'{tag}\n'

# DL 균형 검증 (필수)
assert content.count('<DL><p>') == content.count('</DL><p>')
```

## URL 입력 시 자동 동작
- URL만 입력되면 → 북마크 추가 요청으로 간주
- 사이트 접속 후 서비스명·용도 파악
- 규칙에 맞는 북마크명 생성 (`영문명 – 한글 용도`)
- 현재 구조에서 가장 적합한 폴더 판단
- 배치 계획 제시 → 컨펌 후 Gen_ 파일에 반영
- 폴더 판단 불명확 시 후보 제시 후 선택 요청

## 주의사항
- `<DL><p>` 열기/닫기 반드시 균형 확인 (→ `TROUBLESHOOTING.md` TS-B01)
- 소스 파일의 ICON data:image 보존 (→ `TROUBLESHOOTING.md` TS-B03)
- `&amp;` 인코딩 주의 (`&` vs `&amp;`) (→ `TROUBLESHOOTING.md` TS-B02)
- HANDOFF.md 참조: @HANDOFF.md
