import json
import requests
import sys
from pathlib import Path
import pyinputplus as pyip

if len(sys.argv) < 2:
    print('Usage: Chapter16_pjt2_tkim1.py city_name 2-letter_country_code')
    sys.exit()

location = ' '.join(sys.argv[1:])

url = f'https://api.openweathermap.org/data/3.0/onecall?lat={latitude}&lon={longitude}&exclude={part}&appid={apikey}'
res = requests.get(url)
res.raise_for_status()

weatherData = json.loads(res.text)

weather = weatherData['list']
print(f'Current weather in {location}')
print(weather[0]['weather'][0]['main'], '-', weather[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(weather[1]['weather'][0]['main'], '-', weather[1]['weather'][0]['description'])
print()
print('Day after Tomorrow:')
print(weather[2]['weather'][0]['main'], '-', weather[2]['weather'][0]['description'])


# API키가 activate 되고 나서 실행해야 할듯