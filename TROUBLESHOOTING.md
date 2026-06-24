# TROUBLESHOOTING.md — scripts-bookmarks

오류 발생 시 이 문서를 먼저 확인한다. 해결책이 없으면 LOG.md / 웹 검색 순으로 진행하고, 해결 후 이 문서에 추가한다.

---

## 파일 파싱 / 구조 오류

### TS-B01 · `<DL><p>` 열기/닫기 불균형 — 파일 손상

**증상**: 생성된 북마크 파일을 브라우저에서 가져올 때 일부 폴더가 누락되거나 구조가 무너짐

**원인**: `<DL><p>` 열기 태그와 `</DL><p>` 닫기 태그 수가 불일치 (중첩 실수)

**해결**: 파일 생성 후 반드시 균형 검증 실행

```python
assert content.count('<DL><p>') == content.count('</DL><p>'), \
    f"DL 불균형: 열기 {content.count('<DL><p>')}, 닫기 {content.count('</DL><p>')}"
```

---

### TS-B02 · `&amp;` 이중 인코딩

**증상**: 북마크 URL에 `&amp;amp;` 또는 `&&` 등 깨진 문자가 포함됨

**원인**: HTML 파싱 시 `&amp;`를 `&`로 디코딩한 후, 출력 시 다시 `&amp;`로 인코딩 (또는 반대) — 이중 처리

**해결**:
- 소스 파일의 `&amp;`는 그대로 유지 (HTML 규격)
- URL 비교 시에는 `html.unescape()` 후 비교
- 출력 시 원본 태그(`url_map`의 값)를 그대로 사용

---

### TS-B03 · ICON `data:image` 손실

**증상**: 생성된 파일에서 사이트 파비콘(북마크 아이콘)이 사라짐

**원인**: 북마크 태그를 재구성할 때 `ICON="data:image/png;base64,..."` 속성을 누락

**해결**: 반드시 `url_map`에서 원본 태그를 가져와 사용. 직접 태그 생성 시에는 ICON 속성 포함 확인

```python
# 원본 태그에서 ICON 보존
url_map = {}
for a in anchors:
    m = re.search(r'HREF="([^"]+)"', a)
    if m and m.group(1) not in url_map:
        url_map[m.group(1)] = a  # 원본 태그 전체 보존

def bm(url, title=None):
    tag = url_map.get(url, f'<DT><A HREF="{url}" ADD_DATE="0">{title}</A>')
    if title:
        tag = re.sub(r'>([^<]*)</A>', f'>{title}</A>', tag)
    return f'{tag}\n'
```
