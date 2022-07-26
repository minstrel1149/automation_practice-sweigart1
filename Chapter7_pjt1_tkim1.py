import re
import pyperclip

phoneRegex = re.compile(r'''
(\d{3,4}|\(\d{3,4}\))?   # area code
(\s|-|\.)?               # sep
(\d{3,4})                # mid code
(\s|-|\.)                # sep
(\d{4})                  # end code
''', re.VERBOSE)

# 전체를 괄호 안에 묶어줘야 해당 괄호(이메일 주소)를 찾을 수가 있음
emailRegex = re.compile(r'''(
# user name만 괄호를 묶을 경우 '@' 앞에 있는 한 글자 밖에 못찾는데.. 이걸 어떻게 해결? -> '@'와 같이 묶는 수 밖에..
[a-zA-Z0-9._%+-]+        # user name
@                        # at
# domain name과 최상위 domain을 괄호로 묶음으로써 도메인 추출 가능
([a-zA-Z0-9.-]+          # domain name
\.[a-zA-Z]{2,4})         # .com, co.kr, etc
)''', re.VERBOSE)

# pyperclip.paste() 함수 통해 클립보드에 있는 것을 붙여넣어 text로
text = str(pyperclip.paste())

# 빈 matches를 생성 이후
matches = []
# 전화번호를 000-000-0000 형식으로 matches 리스트에 추가
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[0], groups[2], groups[4]])
    matches.append(phoneNum)
# 이메일을 matches 리스트에 추가
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# 클립보드에 정리된 내용을 추가 -> 바로 붙여넣기 가능
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard: ')
    print('\n'.join(matches))
else:
    print('There is no phone number or e-mail address.')