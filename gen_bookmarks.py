"""
소스: 즐겨찾기_26. 6. 8..html
출력: Gen_즐겨찾기_26.6.8.html
작업: GitHub.dev 북마크를 AI_OTHER > Ai dev 에 추가 후 출력 파일 생성
"""
import re

SRC = r"d:\CLOUD\OneDrive\DIEL_VAULT\DEVELOPMENT\Git\Browser-favorites\Favorites\SourceHTML\즐겨찾기_26. 6. 8..html"
DST = r"d:\CLOUD\OneDrive\DIEL_VAULT\DEVELOPMENT\Git\Browser-favorites\Favorites\OutputHTML\Gen_즐겨찾기_26.6.8.html"

with open(SRC, encoding="utf-8") as f:
    content = f.read()

# GitHub.dev 북마크 태그 (ICON 없음 — 소스에 없으므로 ADD_DATE만)
GITHUB_DEV_TAG = '                <DT><A HREF="https://github.dev/" ADD_DATE="1779846100">GitHub.dev – 브라우저 코드 편집기</A>\n'

# Ai dev 섹션 닫기 태그 바로 앞에 삽입
# 현재 Ai dev 마지막 항목: Phase 뒤의 </DL><p>
AI_DEV_CLOSE = '            </DL><p>\n        </DL><p>\n        <DT><H3 ADD_DATE="1779770999" LAST_MODIFIED="1779770999">ZION</H3>'

# GitHub.dev가 이미 있으면 삽입 건너뜀
if "https://github.dev/" not in content:
    # Phase 항목 뒤, Ai dev 닫기 태그 앞에 삽입
    # Ai dev 닫기 직전 위치 찾기 — Phase 태그 다음 줄
    phase_line = '                <DT><A HREF="https://app.phase.com/view/u/modest1440799262/drafts"'
    insert_after = content.find(phase_line)
    if insert_after == -1:
        raise ValueError("Phase 태그를 찾을 수 없습니다. 소스 구조 확인 필요.")
    # Phase 줄 끝까지 찾기
    end_of_phase_line = content.find('\n', insert_after) + 1
    content = content[:end_of_phase_line] + GITHUB_DEV_TAG + content[end_of_phase_line:]
    print("GitHub.dev 북마크 추가 완료.")
else:
    print("GitHub.dev 이미 존재 — 삽입 건너뜀.")

# DL 균형 검증
open_count = content.count('<DL><p>')
close_count = content.count('</DL><p>')
print(f"<DL><p> 열기: {open_count}, 닫기: {close_count}")
assert open_count == close_count, f"DL 불균형! 열기={open_count}, 닫기={close_count}"

with open(DST, "w", encoding="utf-8") as f:
    f.write(content)

print(f"출력 완료: {DST}")

# 북마크/폴더 수 확인
bm_count = len(re.findall(r'<DT><A ', content))
folder_count = len(re.findall(r'<DT><H3 ', content))
print(f"북마크: {bm_count}개, 폴더: {folder_count}개")
