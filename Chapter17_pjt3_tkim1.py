import time
import subprocess
from pathlib import Path
import pyautogui as pag

p1 = Path.cwd() / 'attachments'

# 3초 뒤 timeLeft 종료
timeLeft = 3
while timeLeft > 0:
    print(timeLeft, end=' ')
    time.sleep(1)
    timeLeft -= 1

try:
    # subprocess.Popen() 함수 통해 알람파일 실행
    subprocess.Popen(['start', p1 / 'alarm.wav'], shell=True)
    # 3초 뒤
    time.sleep(3)
    # pyautogui.getWindwsWithTitle() 통해서 alarm창 객체 생성하고
    alarm = pag.getWindowsWithTitle('groove')[0]
    # 해당 창 종료
    alarm.close()
except:
    print('There is no file.')

print('Process Done!')