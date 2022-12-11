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
  - compile 함수를 통한 Regex객체 생성 → search(), findall() 메서드로 검색 후 Match 객체 반환
  - group() 메서드를 전달하여 호출 및 값 출력
    - 정규식에 소괄호를 넣으면 그룹 생성 가능. groups() 메서드로 그룹들 튜플 출력
  - findall() 메서드는 group 전달 없이 그 자체로 문자열로 구성된 리스트 호출
  - 역슬래시를 통한 이스케이프 가능
  - compile 함수 활용 시 전달인자를 통해 컨트롤 가능
    - re.I(re.IGNORECASE) 인자로 대소문자 미구분
    - re.VERBOSE 인자로 여러 줄에 걸쳐 주석과 함께 작성
    - re.DOTALL 후술
    - 해당 인자들을 파이프 문자로 결합 가능
  - sub() 메서드에 치환할 문자열 및 정규식과 대조할 문자열 전달하여 치환 결과 문자열 반환
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
    - is_absolute() 메서드로 절대 경로 여부 확인 가능
    - os.path.abspath() 함수 및 os.path.relpath() 함수로 상호 변경 가능
  - os.makedirs() 함수로 새로운 폴더 생성 가능 → Path 객체의 mkdir() 메서드와 유사(os.mkdir())
    - exist_ok=True 인자 전달하여 예외발생 방지 가능
  - 파일 경로의 일부분 얻기 → Path 객체의 속성 이용
    - anchor, parent(Path 객체 반환), name, stem, suffix, drive
    - parents 속성 이용하여 상위 폴더들 가져오기 가능
    - os.path.dirname(), os.path.basename()도 활용 → os.path.split(path)로 이분할 가능
    - os.sep 속성(구분자 - 슬래시 혹은 역슬래시) 이용하여 파이썬의 split 연계
  - os.listdir(path)로 path에 있는 파일 이름 리스트 반환 혹은 Path 객체의 glob() 메서드 이용
    - 문자열(파일이름) 반환이냐 Path 객체 반환이냐
    - glob() 메서드는 '*.txt', 'project?.docx' 형태 등 활용 가능
  - 경로 유효성 검사
    - p.exists(), p.is_file(), p.is_dir()
2. 파일 읽기/쓰기 및 파일에 변수 저장
  - open() 함수를 호출하면 File 객체를 반환 → File 객체에 메서드 호출로 처리
  - mode='r' / 'rb' 인자 전달하여 읽기
    - read(), readline(), readlines() 메서드 혹은 read().splitlines()
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
    - namelist() 메서드로 압축 파일 내 파일 이름들 확인
    - getinfo(파일 이름) 메서드 → file_size, compress_size 속성 등
    - extractall(경로), extract(파일, 경로) 메서드로 압축 풀기
  - ZipFile() 함수에 mode='w' 인자 전달하여 압축 가능('a' 전달하면 압축 파일에 추가도 가능)
    - write() 메서드 활용 시 compress_type=zipfile.ZIP_DEFLATED 전달 필요
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

### Chapter.12 - 웹 스크래핑
1. webbrowser 모듈 및 requests 모듈
  - webbrowser.open() 함수 활용하여 특정 URL에 접속
  - requests.get(URL 문자열) → Response 객체 반환
    - raise_for_status() 메서드로 오류 검사 → try ~ except 문으로 처리 가능
    - 텍스트 파일일 경우 text 속성으로 확인 가능(단, 이진문서임을 고려)
    - for문과 iter_content() 메서드 이용하여 PC에 저장 가능
2. bs4 모듈을 통한 웹 크롤링 및 스크래핑
  - BS(res.text, 'html.parser') 형태로 BeautifulSoup 객체 반환 → 'html.parser'는 구문 분석기
  - select() 메서드 → CSS 선택자의 문자열을 통한 검색
    - bsObj.select('div') : 이름이 div인 모든 요소
    - bsObj.select('div span') : div 요소 내 존재하는 요소 중 이름이 span인 모든 요소
    - bsObj.select('#author') : id 속성이 author인 요소
    - bsObj.select('.notice') : CSS class 속성의 이름이 notice인 요소
    - bsObj.select('input[name]') : 이름이 input인 요소 중 name 속성 값이 있는 모든 요소
    - bsObj.select('input[type="button"]') : 이름이 input인 요소 중 type 속성 값이 button인 경우
  - find / find_all() 메서드
    - bsObj.find_all('img', {'class':'img-responsive'}) 형태로 활용
  - get() 메서드를 활용하여 해당 속성 값 반환 가능
    - attrs 속성을 이용해서 속성에 대한 키-값 반환도 가능
3. selenium 모듈을 사용하여 브라우저 제어
  - import 필요한 모듈
    - from selenium import webdriver
    - from selenium.webdriver.chrome.service import Service
    - from webdriver_manager.chrome import ChromeDriverManager
    - from selenium.webdriver.common.by import By
    - from selenium.webdriver.common.keys import Keys
    - from selenium.webdriver.chrome.options import Options
    - driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) 형태로 오픈
  - get() 메서드에 사이트 주소 전달하여 사이트 오픈
  - 페이지에서 요소를 찾는 메서드로 find_element(s) 이용
    - find_element(s) 종류
      - By.CLASS_NAME, By.ID, By.LINK_TEXT, By.PARTIAL_LINK_TEXT, By.NAME, By.TAG_NAME
    - tag_name 속성 이용하여 태그 이름 추출
    - text 속성 이용하여 텍스트 추출
    - get_attribute() 메서드 이용하여 name 속성에 해당하는 값 추출
    - LINK_TEXT 관련 객체의 경우 click() 메서드를 이용해 드라이버 조종 가능
    - send_keys() 메서드 및 submit() 메서드를 이용해 작성 후 제출 가능
    - send_keys() 메서드에 Keys 모듈 결합 가능
      - By.TAG_NAME('html')을 통해 사이트 자체를 컨트롤하도록 만든 후 진행
      - DOWN, UP, LEFT, RIGHT, ENTER, HOME, END, PAGE_UP, PAGE_DOWN, ESCAPE, BACK_SPACE, TAB 등
  - driver에 back(), forward(), refresh(), quit() 메서드로 driver 컨트롤 가능

### Chapter.13/14 - 엑셀/구글 스프레드시트 다루기
1. openpyxl 모듈을 이용한 엑셀 컨트롤
  - load_workbook() 함수를 통한 불러오기 혹은 Workbook() 함수를 통한 쓰기 → 엑셀 파일(workbook) 객체 생성
    - sheetnames 속성으로 시트들 이름 확인 가능
    - create_sheet(index, title) 메서드를 이용하여 새로운 시트 추가 가능
    - del wb['sheetname'] 연산자를 이용해 시트 삭제 가능
  - wb['sheet'] 형태로 특정 시트 얻기 혹은 wb.active 속성 이용 → Sheet 객체
    - title 속성으로 해당 시트 이름 확인 가능
    - max_row, max_column 속성으로 시트 크기 결정 가능
    - row_dimensions, column_dimensions의 height, width 속성 값 변경하여 행 높이, 열 너비 설정
    - merge_cells(), unmerge_cells()를 이용해 셀 병합 및 셀 분할
    - freeze_panes 속성을 바꿔주면서 틀 고정
  - sheet['A1'] 혹은 sheet.cell(1, 1) 형태로 셀 객체 얻기
    - 셀 객체에 value, row, column, coordinate 속성 존재
      - sheet['A1'].value = 'Hello' 혹은 sheet.cell(1, 1).value = 'Hello' 형태로 값 수정
    - sheet 객체 슬라이스도 가능(ex. sheet['A1':'C3']) → for문 활용하여 값 추출
    - list(sheet.columns)[0] 형태로 특정 행이나 열에 존재하는 셀 들에 접근
  - openpyxl.utils 모듈에서 get_column_letter(), column_index_from_string() 함수 이용
  - openpyxl.styles 모듈에서 Font, Alignment 등 설정 가능
    - Font()함수를 이용하여 Font 객체를 생성한 후 셀 객체의 속성(font)으로 변화시키는 형태
  - 차트 생성 : Reference 객체 → Series 객체 → Chart 객체 → Chart 객체에 Series 객체 추가
    - openpyxl.chart 모듈 활용
    - Reference 객체 : openpyxl.chart.Reference(Sheet, min_col, min_row, max_col, max_row)
    - Series 객체 : openpyxl.chart.Series(Ref, title)
    - Chart 객체 : openpyxl.chart.BarChart()
      - title 속성으로 이름 변경
      - append 메서드를 통해 Series 객체 전달
    - sheet.add_chart(Chart, '위치') 를 통해 시트에 그래프 추가
2. win32com.client 모듈을 활용한 엑셀 컨트롤(추가) → win32com.client.Dispatch('Excel.Application')
  - excel.Visible = True 이용하여 엑셀을 보면서 컨트롤 가능
  - excel.Workbooks.Add() 혹은 excel.Workbooks.Open(경로)를 통해 엑셀 오픈
  - Worksheets(이름) 메서드 이용하여 시트 호출
  - ws.Rows().EntireRow.Insert()/Delete() 이용하여 행열 추가/삭제
  - ws.Range(범위).Copy() 이후 ws.Range(범위).Select()로 옮길 범위 지정 후 ws.Paste()로 복사-붙여넣기
    - ws.Range(범위).PasteSpecial(n) 형태로 선택하여 붙여넣기
      - -4122 : 서식 붙여넣기
      - -4123 : 수식 붙여넣기
      - 11 : 수식과 표시 형식 붙여넣기
      - -4163 : 값 붙여넣기
      - 12 : 값과 표시 형식 붙여넣기
  - ws.Range(범위).ClearContents()로 내용 삭제 가능
  - ws.Range('F1:F2').AutoFill(ws.Range('F1:F7')) 형태로 값 및 수식 자동 채우기
3. gspread 모듈을 통한 구글 스프레드 시트 컨트롤
  - wb = gc.open(링크) 형태로 오픈
    - worksheets 메서드 → worksheet 객체들 리스트로 반환
    - add_worksheet(title=) 메서드로 새로운 시트 생성
    - del_worksheet(sheet) 메서드로 시트 삭제 → worksheet 객체가 들어가야
  - wb.get_worksheet(i) 혹은 wb.worksheet(이름) 형태로 특정 시트 얻기 → worksheet 객체
  - sheet.acell('A1') 혹은 sheet.cell(1, 1) 형태로 셀 객체 얻기
    - sheet.acell('A1').value, sheet.cell(1, 1).value 형태로 셀 값 얻기도 가능
    - sheet.get('A1:C3') 형태로 범위 내 값 수집
    - sheet.update('A1:B2', [[1, 2] [3, 4]]) 형태로 셀 값 수정 가능
    - sheet.row_values(n), sheet.col_values(n) 형태로 행/열 모든 값 리스트로 수집
    - get_all_values 메서드로 전체 값을 리스트로 수집
    - sheet.batch_clear(['A1:B2']) 형태로 값 삭제 가능
  - sheet.format('A1:B1', {}) 형태로 셀 포맷 수정
    - 'backgroundcolor', 'horizontalAlignment', 'textFormat'(→ 'fontsize', 'bold') 등

### Chapter.15 - PDF문서 다루기(PyPDF2)
1. PDF 읽기 및 쓰기 컨트롤
  - PyPDF2의 PdfFileReader(File객체) 함수 이용하여 PDF파일 읽기 → PDFReader 객체
    - numPages 속성으로 페이지 수 확인
    - getPage(i) 메서드로 Page 객체 생성
  - PdfFileWriter() 함수 이용하여 새 PDF 파일 생성 → PDFWriter 객체
    - PDFWriter 객체에서 addPage 메서드로 페이지 추가 가능(제일 마지막 페이지에 추가)
    - PDFWriter 객체에서 write(File 객체) 메서드 이용하여 PDF파일 최종 쓰기
  - Page 객체에서 rotateClockwise(각도) 메서드로 페이지 회전 가능(inplace 적용)
  - Page 객체에서 mergePage(다른 Page 객체) 메서드로 페이지 덧입히기 가능(inplace 적용)
2. 기타
  - Page 객체에서 extractText() 메서드로 페이지 내 텍스트 추출
  - PDFReader 객체에서 isEncrypted 속성으로 암호화 여부 판단
    - decrypt 메서드 이용하여 비밀번호 해제(단, PDFFile 객체를 해독할 뿐, 실제 PDF는 계속 비밀번호)
    - encrypt 메서드 이용하여 비밀번호 설정

### Chapter.16 - CSV 파일과 JSON 데이터 다루기
1. csv 모듈
  - csv 읽기
    - csv.reader(File 객체) 함수를 통해 csv 읽기 → reader 객체
      - reader 객체는 단 한 번만 반복 → 다시 읽으려면 다시 reader 객체를 생성해야
    - list()에 전달 → 일반 파이썬 리스트로 변환하여 값에 접근
    - reader 객체의 line_num 속성으로 몇 번째 줄에 위치하는지 파악
    - csv.DictReader(File 객체, [헤더 리스트]) 함수로 헤더를 지정한 csv 읽기
      - pd.read_csv() 에서는 header 인자 전달하여 가능
  - csv 쓰기
    - csv.writer(File 객체) 함수를 통해 csv 쓰기 → writer 객체
      - csv.writer 함수 활용 시 delimiter='\t', lineterminator='\n\n' 등 선택 인자 전달 가능
        - delimiter는 구분자, lineterminator는 줄 끝 문자
    - File 객체 생성 시 newline='' 인자 꼭 전달해줘야
    - writer 객체에서 writerow(s) 메서드 이용하여 내용 삽입 가능
    - csv.DictWriter(File 객체, [헤더 리스트]) 함수로 헤더를 지정한 csv 쓰기
      - writer 객체에서 writeheader 메서드 이용하여 파일에 헤더 행 삽입
      - writerow 메서드 활용 시 딕셔너리로 전달
2. json 모듈
  - json.loads() 함수 : json → 딕셔너리
  - json.dumps() 함수 : 딕셔너리 → json

### Chapter.17 - 시간 관리, 작업 예약, 프로그램 실행
1. 시간 관련 모듈 → time 모듈, datetime 모듈
  - time 모듈
    - Unix epoch(1970/1/1 00:00:00) 기준 경과 초 → time.time 함수
    - time.ctime 함수 : 현재 시각에 관한 설명을 문자열로 반환
    - time.sleep 함수를 통해 프로그램 잠시 중지 가능
  - datetime 모듈(from datetime import ..) → 고유의 datetime 및 timedelta 자료형
    - datetime 값은 특정 시점의 시각
      - datetime(year, month, day, hour, minute) 형태로 활용
      - datetime.now() == datetime.fromtimestamp(time.time())
      - 더 나중 시점의 datetime 객체는 더 큰 값 → 비교 가능
    - timedelta 값은 기간에 대한 시간
      - timedelta(days, hours, minutes, seconds, microseconds) 형태로 활용
      - days, seconds, microseconds 속성 및 total_seconds 메서드로 확인 가능
      - str로 형변환도 가능
      - datetime 값에 대해 날짜 산술 수행 가능
    - datetime의 strftime 메서드 이용하여 문자열 형식으로 출력
      - %Y(%y), %m(%B, %b), %d, %A(%a), %H(%I), %M, %S, %F, %D 형식 등
    - strptime(문자열, 지시자) 함수로 strftime 메서드의 반대 역할 수행도 가능
2. 멀티스레딩 → threading 모듈
  - 지연 또는 예약 실행을 하려는 코드는 별도의 스레드에서 실행
  - threading.Thread(target, (kw)args) 함수 → Thread 객체 생성
    - target에는 함수 지정, args/kwargs에는 인자 전달
    - Thread 객체를 변수에 할당 후 start 메서드 통해 대상 함수 실행
3. 프로그램 실행 → subprocess 모듈
  - subprocess.Popen(경로) 함수 이용하여 다른 프로그램 실행
    - 프로세스가 실행 중일 경우 poll 메서드는 None을 반환
    - wait 메서드로 프로세스가 종료될 때까지 실행을 멈추기 가능(프로그램 대기)
      - 단 calc.exe(계산기) 같이 특수 프로그램은 실행과 동시에 스스로 종료
  - subprocess.Popen([실행 파일, 경로]) 함수 형태로도 가능
    - 기본 연결 프로그램으로 실행할 경우 subprocess.Popen(['start', 경로], shell=True) 형태

### 이메일 보내기 및 확인하기
1. 이메일 보내기 → smtplib 모듈
  - smtplib.SMTP() 함수 활용하여 smtp 객체 생성
    - smtplib.SMTP('smtp.gmail.com', 587/465) 형태
    - smtp 객체 생성 후에는 ehlo 메서드 및 starttls 메서드 호출 필요
    - 모두 완료되었을 경우 quit 메서드를 통해 종료
  - login(id, password) 메서드로 로그인(단, 2단계 인증 활성화 되어있을 경우 사용 불가)
  - email.mime.multipart.MIMEMultipart, email.mime.text.MIMEText 모듈 활용하여 메시지 작성
    - msg['subject'], msg['to'], msg['from'], msg['cc'], msg['bcc'] 활용
    - attach 메서드를 활용하여 Multipart()에 MIMEText() 객체 삽입
  - sendmail(from, to, msg.as_string()) 메서드 이용하여 메일 송부
2. 이메일 확인하기 → imaplib 모듈
  - imaplib.IMAP4_SSL() 함수를 통해 imap 객체 생성
    - imaplib.IMAP4_SSL('imap.gmail.com') 형태
    - 모두 완료되었을 경우 logout 메서드 이용하여 로그아웃
  - login(id, password) 메서드로 로그인(앱 비밀번호로 로그인 가능)
  - select 메서드를 통하여 메일함 지정 -> 'INBOX' 등
    - readonly=True 인자를 통해 읽기 전용으로 열기도 가능
    - imap 객체의 list 메서드를 통해 메일함 확인 가능
  - search 메서드 활용 → 첫 번째 인자는 charset, 두 번째 인자는 찾고자 하는 내용
    - status와 result(uid의 한 묶음 리스트 형태)의 튜플로 반환
    - result는 한 묶음 리스트 형태이므로, index 0 지정 후 split()으로 새로운 리스트로 분류
  - fetch 메서드를 활용하여 확인 → 첫 번째 인자는 확인하고자 하는 메일의 uid, 두 번째 인자는 '(RFC822)'로 고정
    - 마찬가지로 status와 result(인코딩 이전 메시지 형태의 한 묶음 리스트 형태)를 튜플로 반환
    - result는 한 묶음 리스트 형태이므로, index 0 지정 및 index 1 지정으로 인코딩 이전 메시지 추출
    - email 모듈의 message_from_bytes(result[0][1]) 함수 이용하여 message 객체 생성
      - keys 메서드 이용하여 어떠한 키들이 있는지 확인 → 즉, 딕셔너리 형태
      - 키들을 이용해 수신인, 발신인, 제목, 일시 등 확인 가능
      - get_payload 메서드 이용해 본문 확인 가능(텍스트인 경우)
        - is_multipart 메서드가 True일 경우 별도 방법 필요

### Chapter.20 - GUI 자동화로 키보드와 마우스 제어 → pyautogui 모듈
1. 마우스 움직임 제어
  - size() 함수는 화면의 너비와 높이를 네임드 튜플로 반환
  - 마우스 커서 옮기기
    - moveTo(x, y, duration) 함수로 마우스 커서를 화면의 특정 위치로 옮기기
    - move(x, y, duration) 함수로 마우스 현재 위치에서 이동시키기
  - position() 함수로 마우스의 현재 위치 확인
  - click(x, y, button) 함수로 희망하는 위치 클릭
    - doubleClick(), rightClick(), middleClick() 함수도 활용 가능
    - click(left, top, width, height) 형태도 가능 → 해당 영역의 중앙 부분 클릭
  - 마우스 드래그하기
    - dragTo(x, y, duration) 함수로 마우스 커서를 화면의 특정 위치로 드래그
    - drag(x, y, duration) 함수로 마우스 커서를 화면의 현재 위치에서 상대적인 위치로 드래그
  - mouseInfo() 함수로 클릭하려는 것의 좌표 알아내기 가능
  - screenshot() 함수로 스크린샷 가능 → Image 객체로 반환
2. 키보드 제어
  - write() 함수 통해 가상의 키 입력 전송
    - 두 번째 위치 인자로 작성 시간 지정 가능(duration 키워드 인자는 아님)
    - 리스트를 전달하여 키보드 키 입력 가능
  - press() 함수로 키 입력 → keyDown() 및 keyUp() 함수의 조합
  - hotkey() 함수로 단축키 조합 → pyperclip과 연결 가능 등
3. 기타 컴퓨터 제어
  - pixel(x, y) 함수로 특정 픽셀의 RGB 색상 값 얻기 가능
    - pixelMatchesColor(x, y, (R, G, B)) 함수로 일치 여부 확인 → 불린 값
  - locateOnScreen(파일 경로) 함수로 이미지를 찾아낸 좌표(left, top, width, height) 반환
    - locateAllOnScreen(파일 경로) 함수는 Generator 객체 반환 → 리스트에 전달 가능
    - click(파일 경로) 함수로 직접 클릭 가능
  - 창 정보 얻기 → Window 객체
    - Window 객체는 크기, 위치, 제목 등 속성 → 속성 값 변경하여 제어 가능
      - left, right, top, bottom
      - topleft, topright, bottomleft, bottomright
      - width, height
      - size, area
      - center, centerx, centery
      - box(left, top, width, height)
      - title
    - getActiveWindow() 함수로 활성화 Window 객체 생성 가능
      - getAllWindows(), getWindowsWithTitle(title) 등 함수도 가능
    - isMaximize, isMiniMize, isActive 속성 및 maximize, restore, activate, close 메서드 등 활용 가능
4. 기타 - pyperclip 모듈
  - pyperclip.copy 함수를 통해 클립보드에 복사 가능
  - pyperclip.paste 함수를 통해 클립보드에 복사된 내용을 붙여넣기 → 변수에 할당도 가능



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