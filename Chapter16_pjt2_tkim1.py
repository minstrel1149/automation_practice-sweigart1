import json
import requests
import sys
from pathlib import Path
import pyinputplus as pyip

# api의 차이가 생겼는지, 위도와 경도를 기록하도록 바뀌어야
if len(sys.argv) < 2:
    print('Usage: Chapter16_pjt2_tkim1.py latitude logitude apikey')
    sys.exit()

lat = sys.argv[1]
lon = sys.argv[2]
# apikey의 경우 pyip.inputStr(prompt='API KEY: ')를 사용할 수도
# apikey는 https://home.openweathermap.org/api_keys 여기서 활용
apikey = sys.argv[3]

url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={apikey}'
res = requests.get(url)
res.raise_for_status()

# json 파일을 딕셔너리로 변경
weatherData = json.loads(res.text)

print(f'Current weather in {weatherData["name"]}')
print(weatherData['weather'][0]['main'], '-', weatherData['weather'][0]['description'])