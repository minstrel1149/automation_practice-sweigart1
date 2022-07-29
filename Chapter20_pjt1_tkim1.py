# Selenium으로 새로운 창을 열어 동적으로 진행
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pyautogui as pag
import time

# Options() 및 add_argument 활용하여 여러 옵션 추가 가능(by 업무 자동화 - bhban)
options = Options()
# add_argument 안에 'headless' 넣으면 헤드리스 자동화 가능
options.add_argument('--window-size=1600,900')
# 책 대신 원래 쓰던 방식 활용 -> ChromeDriverManager().install()을 통해 직접 설치
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=options)

# 설문지를 제출할 데이터를 딕셔너리의 리스트로 구성
formData = [{'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand',
            'robocop': 4, 'comments': 'Tell Bob I said hi.'},
            {'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4,
            'comments': 'n/a'},
            {'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball',
            'robocop': 1, 'comments': 'Please take the puppets out of the break room.'},
            {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money',
            'robocop': 5, 'comments': 'Protect the innocent. Serve the public trust. Uphold the law.'},
           ]

# Selenium의 get()메서드로 창을 열고
driver.get('https://autbor.com/form')
# pyautogui의 getWindowsWithTitle() 함수를 통해 해당 창을 활성화 -> Selenium 자체만으로 활성화되므로 불필요
# activeWindow = pag.getWindowsWithTitle('Generic Form')[0]
# activeWindow.active

# 함수가 호출될 때마다 1초간 대기? -> 해당 창이 활성화 되기를 기다리는 시간
pag.PAUSE = 1
print('Ensure that the browser window is active and the form is loaded')

# formData의 리스트를 순환하면서 person으로 지정
for person in formData:
    print('5 seconds pause to let user press ctrl c')
    time.sleep(5)

    print(f'Entering {person["name"]} info..')
    # 탭 네번을 통해 이름 칸으로 이동
    pag.write(['\t', '\t', '\t', '\t'])
    # 이름을 넣고 탭 진행
    pag.write(person['name'] + '\t', 0.2)
    # fear를 넣고 탭 진행
    pag.write(person['fear'] + '\t', 0.2)

    # person['source']가 어떤거냐에 따라 항목 선택 -> 'down'과 'enter', '\t' 이용
    if person['source'] == 'wand':
        pag.write(['down', 'enter', '\t'], 0.5)
    elif person['source'] == 'amulet':
        pag.write(['down', 'down', 'enter', '\t'], 0.5)
    elif person['source'] == 'crystal ball':
        pag.write(['down', 'down', 'down', 'enter', '\t'], 0.5)
    elif person['source'] == 'money':
        pag.write(['down', 'down', 'down', 'down', 'enter', '\t'], 0.5)
    
    # person['robocop']가 어떤거냐에 따라 항목 선택 -> 'right'과 'left', '\t' 이용(탭 한번으로는 '선택해제'로 이동하므로 한번 더 진행)
    if person['robocop'] == 1:
        pag.write(['right', 'left', '\t', '\t'], 0.5)
    elif person['robocop'] == 2:
        pag.write(['right', '\t', '\t'], 0.5)
    elif person['robocop'] == 3:
        pag.write(['right', 'right', '\t', '\t'], 0.5)
    elif person['robocop'] == 4:
        pag.write(['right', 'right', 'right', '\t', '\t'], 0.5)
    elif person['robocop'] == 4:
        pag.write(['right', 'right', 'right', 'right', '\t', '\t'], 0.5)
    
    pag.write(person['comments'] + '\t')

    time.sleep(0.5)
    # pag.press('enter')를 통해 설문 제출
    pag.press('enter')

    print('submitted form.')
    time.sleep(5)

    # 제출 후 페이지에서 다른 설문 제출을 위해 탭 이후 엔터 진행
    pag.write(['\t', 'enter'])