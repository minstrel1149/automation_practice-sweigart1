from pathlib import Path
import os
import zipfile
from zipfile import ZipFile
import time
import sys

# zip파일이 생성될 경로 지정
zipPath = Path.cwd() / 'result_attachments'

# backupToZip 함수로 만들어서 실행 -> folder 매개변수 활용
def backupToZip(folder):
    # folder가 절대경로인지 확인 및 절대경로로 변환
    folder = os.path.abspath(folder)
    # 파일 이름 지정 시 'folder_n' 형태로 지정하기 위해
    number = 1
    while True:
        # 이름을 'folder_1'부터 만들어본 뒤
        zipFilename = f'{os.path.basename(folder)}_{number}.zip'
        # 이게 없으면 break -> 이름 확정
        if not os.path.exists(zipFilename):
            break
        # 있으면 'folder_2'로 다시 순환
        number += 1
    
    print(f'Creating {zipFilename}..')
    time.sleep(0.5)

    # backupZip으로 ZipFile 객체 쓰기모드로 생성
    backupZip = ZipFile(zipPath / zipFilename, mode='w')

    # os.walk()를 통해 foldername, subfolders, filenames로 삼등분 후 순환
    for foldername, subfolders, filenames in os.walk(folder):
        print(f'Additing files in {foldername}..')
        time.sleep(0.5)
        # 일단 backupZip에 foldername을 쓰고 -> 그 후 하위 파일들도 추가해야
        backupZip.write(foldername)
        # 하위 파일들의 경우 filenames를 filename으로 순환시키면서 추가 -> os.path.join(foldername, filename) 활용
        for filename in filenames:
            # 중복 추가를 하지 않기 위해 if ~ continue 활용 필요 -> 백업한 zip파일을 백업할 때 포함하지 않기
            # 왜냐면 각 subfolders가 다시 foldername으로 변하기 때문?
            newBase = f'{os.path.basename(folder)}_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername, filename))

    backupZip.close()
    print('Process Done!')

# sys.argv를 활용해 원하는 폴더 지정
backupToZip(zipPath / sys.argv[1])