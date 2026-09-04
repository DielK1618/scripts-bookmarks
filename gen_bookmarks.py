"""
?뚯뒪: 利먭꺼李얘린_26. 6. 8..html
異쒕젰: Gen_利먭꺼李얘린_26.6.8.html
?묒뾽: GitHub.dev 遺곷쭏?щ? AI_OTHER > Ai dev ??異붽? ??異쒕젰 ?뚯씪 ?앹꽦
"""
import os
import re


# 드라이브 문자를 하드코딩하지 않는다 — 여러 PC가 같은 OneDrive 계정을 서로 다른
# 드라이브 문자로 동기화할 수 있어서(2026-08-16), 이 스크립트 자신의 위치 기준
# 상대 경로로 찾는다.
_HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(_HERE, "Favorites", "SourceHTML", "利먭꺼李얘린_26. 6. 8..html")
DST = os.path.join(_HERE, "Favorites", "OutputHTML", "Gen_利먭꺼李얘린_26.6.8.html")

with open(SRC, encoding="utf-8") as f:
    content = f.read()

# GitHub.dev 遺곷쭏???쒓렇 (ICON ?놁쓬 ???뚯뒪???놁쑝誘濡?ADD_DATE留?
GITHUB_DEV_TAG = '                <DT><A HREF="https://github.dev/" ADD_DATE="1779846100">GitHub.dev ??釉뚮씪?곗? 肄붾뱶 ?몄쭛湲?/A>\n'

# Ai dev ?뱀뀡 ?リ린 ?쒓렇 諛붾줈 ?욎뿉 ?쎌엯
# ?꾩옱 Ai dev 留덉?留???ぉ: Phase ?ㅼ쓽 </DL><p>
AI_DEV_CLOSE = '            </DL><p>\n        </DL><p>\n        <DT><H3 ADD_DATE="1779770999" LAST_MODIFIED="1779770999">ZION</H3>'

# GitHub.dev媛 ?대? ?덉쑝硫??쎌엯 嫄대꼫?
if "https://github.dev/" not in content:
    # Phase ??ぉ ?? Ai dev ?リ린 ?쒓렇 ?욎뿉 ?쎌엯
    # Ai dev ?リ린 吏곸쟾 ?꾩튂 李얘린 ??Phase ?쒓렇 ?ㅼ쓬 以?    phase_line = '                <DT><A HREF="https://app.phase.com/view/u/modest1440799262/drafts"'
    insert_after = content.find(phase_line)
    if insert_after == -1:
        raise ValueError("Phase ?쒓렇瑜?李얠쓣 ???놁뒿?덈떎. ?뚯뒪 援ъ“ ?뺤씤 ?꾩슂.")
    # Phase 以??앷퉴吏 李얘린
    end_of_phase_line = content.find('\n', insert_after) + 1
    content = content[:end_of_phase_line] + GITHUB_DEV_TAG + content[end_of_phase_line:]
    print("GitHub.dev 遺곷쭏??異붽? ?꾨즺.")
else:
    print("GitHub.dev ?대? 議댁옱 ???쎌엯 嫄대꼫?.")

# DL 洹좏삎 寃利?open_count = content.count('<DL><p>')
close_count = content.count('</DL><p>')
print(f"<DL><p> ?닿린: {open_count}, ?リ린: {close_count}")
assert open_count == close_count, f"DL 遺덇퇏?? ?닿린={open_count}, ?リ린={close_count}"

with open(DST, "w", encoding="utf-8") as f:
    f.write(content)

print(f"異쒕젰 ?꾨즺: {DST}")

# 遺곷쭏???대뜑 ???뺤씤
bm_count = len(re.findall(r'<DT><A ', content))
folder_count = len(re.findall(r'<DT><H3 ', content))
print(f"遺곷쭏?? {bm_count}媛? ?대뜑: {folder_count}媛?)
