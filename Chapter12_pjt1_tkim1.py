from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests
import sys
from bs4 import BeautifulSoup as BS

searchLink = f'https://search.naver.com/search.naver?where=news&sm=tab_jum&query='
# Options() 및 add_argument 활용하여 여러 옵션 추가 가능(by 업무 자동화 - bhban)
options = Options()
# add_argument 안에 'headless' 넣으면 헤드리스 자동화 가능
options.add_argument('--window-size=1600,900')
# 책 대신 원래 쓰던 방식 활용 -> ChromeDriverManager().install()을 통해 직접 설치
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=options)

# 검색을 희망하는 단어를 sys.argv[1]을 통해 입력 -> 해당 페이지 selenium으로 열기
driver.get(searchLink + sys.argv[1])
page = driver.page_source
bs_obj = BS(page, 'html.parser')

# BeautifulSoup을 통해 클릭을 희망하는 부분('네이버뉴스') 찾기
obj_list = bs_obj.find_all('a', {'class':'info'})
# 해당 obj_list에서 get('href') 메서드 활용하여 링크를 수집하고 그 부분을 site_list에 리스트 화
# 다만 네이버뉴스만 열어야 하므로, startswith() 메서드 활용하여 해당 부분 지정
site_list = [x.get('href') for x in obj_list if x.get('href').startswith(f'https://n.news.naver')]

for site in site_list:
    # driver.execute_script("window.open('---');") 활용하여 해당 사이트 새로운 탭으로 오픈
    # driver.switch_to.window(driver.window_handles[i]) 활용하여 탭 간 이동 가능
    driver.execute_script(f"window.open('{site}');")

print('Process Done!')
