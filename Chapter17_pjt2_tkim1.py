import requests
import os
import threading
from bs4 import BeautifulSoup as BS
from pathlib import Path

p1 = Path.cwd() / 'attachments'
os.makedirs(Path.cwd() / 'result_attachments' / 'xkcd', exist_ok=True)
p2 = Path.cwd() / 'result_attachments' / 'xkcd'

# xkcd 이미지 파일을 다운로드 하는 함수 생성
def downloadXkcd(startComic, endComic):
    for urlNum in range(startComic, endComic):
        print(f'Downloading page https://xkcd.com/{urlNum}..')
        # urlNum에 해당하는 페이지를 get() 함수를 통해 다운로드
        res = requests.get(f'https://xkcd.com/{urlNum}')
        res.raise_for_status

        bs_obj = BS(res.text, 'html.parser')
        # select() 메서드 통해 id = "comic"인 이미지 파일 추출
        comicElem = bs_obj.select('#comic img')
        if comicElem == []:
            print('Could not find comic image.')
        else:
            # BeautifulSoup get() 메서드를 통해 img src 추출 후
            comicUrl = comicElem[0].get('src')
            print(f'Downloading image {comicUrl}..')
            # requests.get() 함수를 통해 다운로드
            res = requests.get(f'https:{comicUrl}')
            res.raise_for_status

            # 다운로드한 response 파일을 이진 모드로 연 후 res.iter_content()를 순환시켜 진행
            with open(p2 / os.path.basename(comicUrl), mode='wb') as imgFile:
                for chunk in res.iter_content(100000):
                    imgFile.write(chunk)
            
# 모든 Thread 객체를 담을 빈 리스트 생성
downloadThreads = []
# 14번 반복하여 Thread를 14개 생성
for i in range(0, 140, 10):
    start = i
    end = i + 9
    if start == 0:
        start = 1
    downloadThread = threading.Thread(target=downloadXkcd, args=(start, end))
    # downloadThreads 리스트에 downloadThread 객체 추가
    downloadThreads.append(downloadThread)
    downloadThread.start()

# 모든 Thread가 종료될 때 까지 기다리기
for downloadThread in downloadThreads:
    downloadThread.join()

print('Process Done!')