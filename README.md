# 뚝딱뚝딱 파이썬 자동화 연습 - Al Sweigart 저
### 중요사항
1. 이전 여러 번 학습하였으나, 새로운 마음가짐으로 다시 학습 및 코드 주석 추가
  - 주석을 추가하느라 시간이 오래 걸리긴 하는데.. 더 자세히 공부하는 취지로 접근
  - 주석을 통해 다른 곳에서도 내 Github 접속함을 통해 눈으로 복습 가능
2. 책에 있는 코드를 단순히 따라하는 것이 아니라 나만의 코드로 작성
3. 일부 라이브러리는 책 라이브러리가 아닌 유명 라이브러리로 대체(ezsheets -> gspread 등)
4. 변수명의 경우 편의상 책 스타일에 따름(Snake Case 대신 Camel Case 활용)
5. 커널은 jupyter notebook의 파이썬 3.9.12 활용

## 신규 README.md 방식
### Chapter.7 - 정규표현식을 활용한 더 많은 패턴 대조
1. re 모듈 함수 및 메서드 플로우
  - compile 함수를 통한 Regex객체 생성 → search, findall 메서드로 검색 후 Match 객체 반환
  - group 메서드를 전달하여 호출 및 값 출력
    - 정규식에 소괄호를 넣으면 그룹 생성 가능. groups 메서드로 그룹들 튜플 출력
  - findall은 group 전달 없이 그 자체로 문자열로 구성된 리스트 호출
  - 역슬래시를 통한 이스케이프 가능
  - compile 함수 활용 시 전달인자를 통해 컨트롤 가능
    - re.I(re.IGNORECASE) 인자로 대소문자 미구분
    - re.VERBOSE 인자로 여러 줄에 걸쳐 주석과 함께 작성
    - re.DOTALL 후술
    - 해당 인자들을 파이프 문자로 결합 가능
  - sub 메서드에 치환할 문자열 및 정규식과 대조할 문자열 전달하여 치환 결과 문자열 반환
2. 정규식 자체 사용법
  - 파이프문자로 여러 그룹 대조(소괄호를 통한 일부 그룹 가능)
  - 소괄호와 물음표, 별표, 플러스를 사용한 선택적 대조
  - 중괄호로 특정 횟수의 반복과 일치 가능
    - 최소값, 최대값 지정도 가능
    - 기본적으로는 최대 일치 → 중괄호 뒤에 물음표를 붙여 최소일치 가능
  - 축약 문자 클래스 및 사용자 정의 문자 클래스 사용
    - \d(0-9숫자), \w(글자, 숫자, 밑줄 중 하나), \s(빈칸, 탭, 개행문자 중 하나)
      - 대문자의 경우 축약에 대한 반대 문자 클래스
    - 대괄호를 이용한 사용자 정의 문자 클래스
      - 하이픈을 사용하여 글자나 숫자의 범위 포함 가능(ex. [a-zA-Z0-9])
      - 대괄호 안에서는 역슬래시를 통한 이스케이프 불필요
      - 캐럿 기호(^)를 통해 반대 문자 클래스 가능
  - 캐럿/달러 기호 문자를 이용하여 시작/끝 부분 일치 가능
    - 동시 사용의 경우 전체 문자열이 정규식과 일치해야
  - 마침표 문자는 와일드카드로 사용 가능 → 마침표-별표 기호로 모든 문자 일치
    - 마침표-별표-물음표로 최소 일치 가능
    - re.DOTALL 인자 전달하여 개행 문자를 포함한 모든 문자와 일치 가능

### Chapter.8 - pyinputplus 모듈
1. 주요 함수 종류
  - inputStr()
  - inputNum() / inputInt() / inputFloat()
  - inputChoice() / inputMenu() - 제공한 선택사항 중 하나만 입력
  - inputYesNo() / inputBool()
  - inputEmail()
  - inputCustom() - 사용자 정의 함수 전달(input 형태이므로 기본적으로는 문자열을 입력받는 것)
2. 활용 가능한 전달인자
  - prompt
  - min, max, greaterThan, lessThan
  - blank=True
  - limit, timeout → default 인자를 통한 예외 처리
  - allowRegexes, blockRegexes → allowRegexes가 더 높은 우선순위
    - 튜플로 묶어서 전달할 경우 첫 번째가 전달하는 정규식, 두 번째는 금지 표현식 작성 시 회신

### Chapter.9 - 파일과 파일 경로
1. pathlib 모듈 Path 함수 및 os 모듈
  - 슬래시(/)를 사용해 연결 → 기존 os.path.join() 함수 대체
  - Path.home(), Path.cwd() → os.chdir() 함수로 Current Working Directory 수정 가능
  - 절대 경로와 상대 경로
    - 마침표 한 개(.)는 현재 디렉터리 축약, 마침표 두 개(..)는 상위 폴더를 의미
    - is_absolute 메서드로 절대 경로 여부 확인 가능
    - os.path.abspath() 함수 및 os.path.relpath() 함수로 상호 변경 가능
  - os.makedirs() 함수로 새로운 폴더 생성 가능 → Path 객체의 mkdir 메서드와 유사(os.mkdir())
    - exist_ok=True 인자 전달하여 예외발생 방지 가능
  - 파일 경로의 일부분 얻기 → Path 객체의 속성 이용
    - anchor, parent(Path 객체 반환), name, stem, suffix, drive
    - parents 속성 이용하여 상위 폴더들 가져오기 가능
    - os.path.dirname(), os.path.basename()도 활용 → os.path.split(path)로 이분할 가능
    - os.sep 속성(구분자 - 슬래시 혹은 역슬래시) 이용하여 파이썬의 split 연계
  - os.listdir(path)로 path에 있는 파일 이름 리스트 반환 혹은 Path 객체의 glob 메서드 이용
    - 문자열(파일이름) 반환이냐 Path 객체 반환이냐
    - glob 메서드는 '*.txt', 'project?.docx' 형태 등 활용 가능
  - 경로 유효성 검사
    - p.exists(), p.is_file(), p.is_dir()
2. 파일 읽기/쓰기 및 파일에 변수 저장
  - open() 함수를 호출하면 File 객체를 반환 → File 객체에 메서드 호출로 처리
  - mode='r' / 'rb' 인자 전달하여 읽기
    - read, readline, readlines 메서드 혹은 read().splitlines()
  - mode='w' / 'wb' / 'a' 인자 전달하여 쓰기
  - shelve 모듈 사용하여 변수들을 shelf 파일로 저장 가능
    - shelve.open() 함수는 Path 객체 사용 불가 → str로 형변환 필요

### Chapter.10 - 파일 정리하기
1. shutil 모듈 및 send2trash 모듈을 통한 파일 정리
  - shutil.copy(), shutil.copytree() 함수를 통한 복사
    - copytree 함수는 덮어쓰기가 안되므로 예외 처리 필요
  - shutil.move() 함수를 통한 파일 이동 및 이름 바꾸기
  - os.unlink(), os.rmdir(), shutil.rmtree(), send2trash.send2trach() 함수를 통한 삭제
    - 삭제 시에는 send2trash 이용(파일 영구 삭제가 아닌 휴지통으로 이동)
    - 주석 처리하고 print를 통해 삭제할 파일을 먼저 확인 필요
2. 디렉터리 트리 탐색
  - os.walk() 함수 활용 → 폴더 경로 문자열, 하위 폴더 문자열 리스트, 폴더 내 파일 문자열 리스트
3. zipfile 모듈을 활용한 파일/폴더 압축
  - ZipFile() 함수 활용하여 경로 확인 → ZipFile 객체 반환
    - namelist 메서드로 압축 파일 내 파일 이름들 확인
    - getinfo(파일 이름) 메서드 → file_size, compress_size 속성 등
    - extractall(경로), extract(파일, 경로) 메서드로 압축 풀기
  - ZipFile() 함수에 mode='w' 인자 전달하여 압축 가능('a' 전달하면 압축 파일에 추가도 가능)
    - write 메서드 활용 시 compress_type=zipfile.ZIP_DEFLATED 전달 필요
    - os.walk() 등과 연계하여 폴더 내 모든 파일도 압축 가능
    - Path.home()에서 상위 폴더들까지 압축경로로 이어지는 문제 해결해야..

### Chapter.11 - 디버깅
1. raise Exception()을 통한 예외 일으키기
2. assert문을 통한 AssertionError 일으키키
  - assert '조건' → 조건이 거짓이면 예외를 일으키는 형태
  - 프로그램의 정상적인 작업 부분에서 발생하는 오류는 assert 대신 raise 형태로 진행
  - try ~ except 문과 함께 활용하여 처리하지 말아야
3. logging 모듈
  - basicConfig(level=, filename=), debug(), disable() 함수 등 이용
  - DEBUG, INFO, WARNING, ERROR, CRITICAL 순서
  



## 과거 README.md 방식(신규 완성 이후 삭제 예정)
### 2022년 7월 22일
1. Chapter 7 정규표현식 기초 관련 복습 진행

### 2022년 7월 23일
1. Chapter 8 입력값 검증하기 기초 관련 복습 진행 - pyinputplus 라이브러리
2. Chapter 9 파일과 파일 경로 기초 관련 복습 진행 - pathlib, os 모듈 등
3. Chapter 10 파일 정리하기 기초 관련 복습 진행 - shutil 모듈, 디렉터리 트리, zipfile 모듈 등
4. Chapter 11 예외처리, 단언, 로깅 기초 관련 복습 진행
5. Chapter 12 웹 크롤링, 스크리팽 기초 관련 복습 진행 - requests, bs4, selenium 등
6. Chapter 13 엑셀 스프레드시트 다루기 기초 관련 복습 진행 - openpyxl 기본 및 gspread와의 차이

### 2022년 7월 24일
1. Chapter 14 구글 스프레드시트 다루기 - gspread 활용. 보안상 문제로 패스
2. Chapter 15 PDF 문서 다루기 기초 관련 복습 진행 - PyPDF2 활용 -> 워드 문서 다루기는 패스
3. Chapter 16 CSV와 JSON 데이터 다루기 기초 관련 복습 진행 - csv, json 모듈 등
4. Chapter 17 시간 관리, 프로그램 실행 기초 관련 복습 진행 - datetime, time, threading, subprocess 모듈 등
5. Chapter 18 이메일 보내고 받기 기초 관련 복습 진행 - 책 내용 대신 smtplib, email, imaplib 모듈 활용하여 연습

### 2022년 7월 25일
1. Chapter 20 GUI 자동화로 키보드, 마우스 제어 기초 관련 복습 진행 - pyautogui 라이브러리

### 2022년 7월 26일
1. Chapter 7 정규표현식 초간단 프로젝트 학습
2. Chapter 8 입력값 검증하기 초간단 프로젝트 학습
3. Chapter 9 파일 읽고 쓰기 초간단 프로젝트 학습
4. Chapter 10 파일 정리하기 초간단 프로젝트 학습
5. Chapter 12 웹 스크래핑 초간단 프로젝트 학습 - 책과는 다르게 나만의 프로젝트 + 코드 작성
6. Chapter 13 엑셀 스프레드시트 다루기 초간단 프로젝트 학습 - 일부는 나만의 방식으로 pandas 활용
7. Chapter 15 PDF 문서 다루기 초간단 프로젝트 학습

### 2022년 7월 27일
1. Chapter 16 CSV, JSON 데이터 다루기 초간단 프로젝트 학습 - json의 경우 api 변경으로 인하여 코드 약간 변경

### 2022년 7월 28일
1. Chapter 17 시간관리, 작업예약, 프로그램 실행 초간단 프로젝트 학습
2. Chapter 18 이메일 보내기 초간단 프로젝트 학습

### 2022년 7월 29일
1. Chapter 20 GUI자동화로 키보드와 마우스 제어하기 초간단 프로젝트 학습