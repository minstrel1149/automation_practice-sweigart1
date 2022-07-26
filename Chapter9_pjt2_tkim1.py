import shelve
import pyperclip
import sys
from pathlib import Path

# mcbShelf를 저장할 경로 지정
pathMcb = str(Path.cwd() / 'result_attachments' / 'walnut_path_mkdir' / 'mcb')

# mchShelf 열기
mcbShelf = shelve.open(pathMcb)

# sys.argv가 세개인 경우 / 두 번째가 save인 경우 -> keyword를 클립보드에 저장
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    # mcbShelf['keyword']에 pyperclip.paste()를 지정
    mcbShelf[sys.argv[2]] = pyperclip.paste()
# sys.argv가 두개인 경우
elif len(sys.argv) == 2:
    # 두 번째가 list인 경우 -> 모든 키워드를 클립보드로 불러오기
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    # 두 번째가 keyword인 경우 -> 키워드를 클립보드로 불러오기
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

print(pyperclip.paste())
mcbShelf.close()